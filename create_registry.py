#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any
from urllib.parse import quote

import requests
from bs4 import BeautifulSoup

API_ROOT = "https://api.github.com"
DEFAULT_OWNER = "iqb-berlin"
TIMEOUT_SECONDS = 30

HTML_METADATA_FIELDS = {
    "data-version": "version",
    "data-repository-url": "repository_url",
    "data-api-version": "api_version",
    "data-supported-browsers": "supported_browsers",
    "content": "content",
}


class GitHubClient:
    def __init__(self, token: str | None) -> None:
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/vnd.github+json",
                "User-Agent": "verona-registry-sync",
            }
        )
        if token:
            self.session.headers["Authorization"] = f"Bearer {token}"

    def get_json(self, url: str, *, optional: bool = False, **params: Any) -> Any:
        response = self.session.get(url, params=params, timeout=TIMEOUT_SECONDS)
        if optional and response.status_code == 404:
            return None
        response.raise_for_status()
        return response.json()

    def get_text(self, url: str, *, optional: bool = False) -> str | None:
        response = self.session.get(url, timeout=TIMEOUT_SECONDS)
        if optional and response.status_code == 404:
            return None
        response.raise_for_status()
        return response.text

    def iter_paginated(self, url: str, **params: Any) -> list[dict[str, Any]]:
        items: list[dict[str, Any]] = []
        page = 1
        while True:
            payload = self.get_json(url, per_page=100, page=page, **params)
            if not isinstance(payload, list):
                raise RuntimeError(f"Expected a list from {url}, received {type(payload)!r}")
            if not payload:
                return items
            items.extend(payload)
            if len(payload) < 100:
                return items
            page += 1


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate the Verona registry README and JSON index."
    )
    parser.add_argument(
        "--owner",
        action="append",
        dest="owners",
        help="GitHub owner to scan. Can be provided multiple times.",
    )
    parser.add_argument(
        "--output-dir",
        default=".",
        help="Directory where README.md and registry.json will be written.",
    )
    return parser.parse_args()


def parse_date(value: str | None) -> str | None:
    if not value:
        return None
    return value.split("T", 1)[0]


def clean_optional_text(value: str | None) -> str | None:
    if value is None:
        return None
    value = value.strip()
    return value or None


def parse_meta_value(value: str) -> Any:
    value = value.strip()
    if not value:
        return value
    if value[0] in "[{":
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value
    return value


def extract_metadata_from_html(html: str) -> dict[str, Any] | None:
    soup = BeautifulSoup(html, "html.parser")

    json_ld = soup.find("script", {"type": "application/ld+json"})
    if json_ld is not None:
        content = json_ld.string or "".join(str(part) for part in json_ld.contents)
        if content:
            try:
                return {
                    "kind": "json-ld",
                    "data": json.loads(content),
                }
            except json.JSONDecodeError:
                pass

    metadata: dict[str, Any] = {}
    for tag in soup.find_all("meta"):
        for attribute, field_name in HTML_METADATA_FIELDS.items():
            value = tag.get(attribute)
            if value:
                metadata[field_name] = parse_meta_value(value)

    if metadata:
        return {
            "kind": "html-meta",
            "data": metadata,
        }

    return None


def pick_release_html_asset(release: dict[str, Any] | None) -> dict[str, Any] | None:
    if not release:
        return None

    candidates: list[tuple[int, str, dict[str, Any]]] = []
    for asset in release.get("assets", []):
        name = asset.get("name", "")
        lower_name = name.lower()
        content_type = asset.get("content_type", "")
        if not lower_name.endswith(".html") and content_type != "text/html":
            continue

        score = 100
        if lower_name.endswith(".html"):
            score -= 40
        if lower_name.endswith("index.html"):
            score -= 20
        if "player" in lower_name or "editor" in lower_name:
            score -= 10
        candidates.append((score, lower_name, asset))

    if not candidates:
        return None

    candidates.sort(key=lambda item: (item[0], item[1]))
    return candidates[0][2]


def pick_repository_html_path(tree: dict[str, Any] | None) -> str | None:
    if not tree:
        return None

    candidates: list[tuple[int, int, str]] = []
    for entry in tree.get("tree", []):
        path = entry.get("path", "")
        lower_path = path.lower()
        if entry.get("type") != "blob" or not lower_path.endswith(".html"):
            continue
        if lower_path.startswith(".github/") or "/.github/" in lower_path:
            continue
        if lower_path.startswith("node_modules/") or "/node_modules/" in lower_path:
            continue

        score = 100
        if lower_path.endswith("index.html"):
            score -= 40
        if lower_path.startswith("dist/") or "/dist/" in lower_path:
            score -= 20
        if lower_path.startswith("build/") or "/build/" in lower_path:
            score -= 15
        if lower_path.startswith("docs/") or "/docs/" in lower_path:
            score += 20
        if lower_path.startswith("storybook-static/") or "/storybook-static/" in lower_path:
            score += 30

        candidates.append((score, lower_path.count("/"), path))

    if not candidates:
        return None

    candidates.sort(key=lambda item: (item[0], item[1], item[2]))
    return candidates[0][2]


def fetch_module_metadata(
    client: GitHubClient,
    repo: dict[str, Any],
    release: dict[str, Any] | None,
) -> dict[str, Any] | None:
    release_asset = pick_release_html_asset(release)
    if release_asset:
        html = client.get_text(release_asset["browser_download_url"], optional=True)
        if html:
            metadata = extract_metadata_from_html(html)
            if metadata:
                return {
                    "source": {
                        "type": "release-asset",
                        "name": release_asset["name"],
                        "url": release_asset["browser_download_url"],
                    },
                    **metadata,
                }

    tree = client.get_json(
        f"{API_ROOT}/repos/{repo['full_name']}/git/trees/{repo['default_branch']}",
        optional=True,
        recursive=1,
    )
    html_path = pick_repository_html_path(tree)
    if not html_path:
        return None

    raw_path = quote(html_path, safe="/")
    html = client.get_text(
        "https://raw.githubusercontent.com/"
        f"{repo['full_name']}/{repo['default_branch']}/{raw_path}",
        optional=True,
    )
    if not html:
        return None

    metadata = extract_metadata_from_html(html)
    if not metadata:
        return None

    return {
        "source": {
            "type": "default-branch-file",
            "path": html_path,
            "branch": repo["default_branch"],
            "url": f"{repo['html_url']}/blob/{repo['default_branch']}/{html_path}",
        },
        **metadata,
    }


def build_version_info(
    client: GitHubClient, repo: dict[str, Any]
) -> tuple[dict[str, Any] | None, dict[str, Any] | None]:
    release = client.get_json(
        f"{API_ROOT}/repos/{repo['full_name']}/releases/latest",
        optional=True,
    )
    tags = client.get_json(
        f"{API_ROOT}/repos/{repo['full_name']}/tags",
        per_page=1,
    )
    tag = tags[0] if tags else None

    version: dict[str, Any] | None = None
    if release:
        version = {
            "type": "release",
            "name": release["tag_name"],
            "url": release["html_url"],
            "published_at": parse_date(release.get("published_at")),
        }
    elif tag:
        encoded_tag_name = quote(tag["name"], safe="")
        version = {
            "type": "tag",
            "name": tag["name"],
            "url": f"{repo['html_url']}/releases/tag/{encoded_tag_name}",
        }

    return version, release


def collect_repositories(client: GitHubClient, owners: list[str]) -> list[dict[str, Any]]:
    repositories: list[dict[str, Any]] = []

    for owner in owners:
        owner_repositories = client.iter_paginated(f"{API_ROOT}/users/{owner}/repos")
        for repo in owner_repositories:
            if repo.get("archived"):
                continue
            if repo.get("fork"):
                continue
            if "verona" not in repo["name"].lower():
                continue

            version, release = build_version_info(client, repo)
            is_module = (
                repo["name"].startswith("verona-player")
                or repo["name"].startswith("verona-editor")
            )

            repository: dict[str, Any] = {
                "name": repo["name"],
                "full_name": repo["full_name"],
                "owner": owner,
                "description": clean_optional_text(repo.get("description")),
                "html_url": repo["html_url"],
                "default_branch": repo["default_branch"],
                "pushed_at": parse_date(repo.get("pushed_at")),
                "updated_at": parse_date(repo.get("updated_at")),
                "version": version,
            }

            if is_module:
                module_metadata = fetch_module_metadata(client, repo, release)
                if module_metadata:
                    repository["module_metadata"] = module_metadata

            repositories.append(repository)

    repositories.sort(key=lambda repo: repo["name"].lower())
    return repositories


def render_readme(registry: dict[str, Any]) -> str:
    owners = ", ".join(f"`{owner}`" for owner in registry["owners"])
    lines = [
        "# Verona Registry",
        "",
        "This repository is a generated catalog of Verona-related repositories.",
        "",
        f"- Scanned owners: {owners}",
        "- Sync triggers: daily schedule, manual dispatch, and `repository_dispatch` with `event_type=registry-sync`",
        "- Generated files: `README.md` and `registry.json`",
        "- Metadata precedence: release asset HTML, then default-branch HTML, then GitHub release/tag metadata",
        "",
        "## Repositories",
        "",
    ]

    for repo in registry["repositories"]:
        lines.append(f"### [{repo['name']}]({repo['html_url']})")
        description = repo.get("description") or "No repository description."
        lines.append(f"- Description: {description}")
        lines.append(f"- Default branch: `{repo['default_branch']}`")
        if repo.get("pushed_at"):
            lines.append(f"- Last pushed: {repo['pushed_at']}")

        version = repo.get("version")
        if version:
            version_label = "Latest release" if version["type"] == "release" else "Latest tag"
            version_line = f"- {version_label}: [{version['name']}]({version['url']})"
            if version.get("published_at"):
                version_line += f" ({version['published_at']})"
            lines.append(version_line)
        else:
            lines.append("- Latest release: none")

        module_metadata = repo.get("module_metadata")
        if module_metadata:
            source = module_metadata["source"]
            if source["type"] == "release-asset":
                source_label = f"release asset `{source['name']}`"
            else:
                source_label = (
                    f"default branch file [`{source['path']}`]({source['url']})"
                )
            lines.append(
                f"- Module metadata: `{module_metadata['kind']}` extracted from {source_label}"
            )
            lines.append("")
            lines.append("```json")
            lines.append(
                json.dumps(
                    module_metadata["data"],
                    ensure_ascii=False,
                    indent=2,
                    sort_keys=True,
                )
            )
            lines.append("```")

        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def write_file(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def main() -> int:
    args = parse_args()
    owners = args.owners or [DEFAULT_OWNER]
    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    token = os.environ.get("GITHUB_TOKEN")
    client = GitHubClient(token=token)
    registry = {
        "owners": owners,
        "repositories": collect_repositories(client, owners),
    }

    write_file(
        output_dir / "registry.json",
        json.dumps(registry, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
    )
    write_file(output_dir / "README.md", render_readme(registry))
    return 0


if __name__ == "__main__":
    sys.exit(main())
