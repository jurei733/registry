# Contributing

This repository is generated. Do not hand-edit `README.md` or `registry.json`; regenerate them through `create_registry.py`.

The source of truth is:

- GitHub repository metadata
- Latest release or latest tag metadata
- Module metadata extracted from HTML, preferring release assets and then the matching release or tag ref

## Local workflow

Install dependencies and regenerate the catalog locally:

```sh
python3 -m pip install -r requirements.txt
GITHUB_TOKEN="$(gh auth token)" python3 create_registry.py
```

Useful checks before committing:

```sh
python3 -m py_compile create_registry.py
git diff --check
```

## Updating the registry

The sync workflow supports three triggers:

- Daily schedule
- Manual `workflow_dispatch`
- `repository_dispatch` with `event_type=registry-sync`

The daily schedule is only a fallback. For low-activity public repositories, GitHub can disable scheduled workflows after long periods without repository activity, so upstream `repository_dispatch` events are the more reliable sync trigger.

The generated artifacts are:

- `README.md`
- `registry.json`

## How metadata is resolved

For player and editor repositories, the generator uses this order:

1. HTML release asset from the latest GitHub Release
2. HTML file from the same release tag or Git tag that is shown in the catalog
3. Plain GitHub release/tag metadata when no HTML metadata can be extracted

This prevents the registry from mixing a released version with metadata from a newer default-branch commit. It does not add a second fallback to the default branch when a release or tag already exists.

The `module_metadata.source.type` field in `registry.json` currently uses these values:

- `release-asset`
- `release-tag-file`
- `tag-file`
- `default-branch-file`

For tag-only repositories, version links point to the tag ref (`/tree/<tag>`) instead of a GitHub Release URL, because a release page may not exist.

## Workflow behavior

The GitHub Actions workflow has two jobs:

- `sync`: regenerates `README.md` and `registry.json`, commits them only when they changed, and uploads the Pages artifact
- `deploy`: publishes the uploaded artifact to GitHub Pages

No-op runs are expected and should finish without creating a commit.

## Cross-repository sync

The long-term way to keep this repository fresh is to notify it when a tracked Verona repository publishes a release or changes its metadata file.

Those repositories can trigger:

```sh
curl -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer ${REGISTRY_DISPATCH_TOKEN}" \
  https://api.github.com/repos/verona-interfaces/registry/dispatches \
  -d '{"event_type":"registry-sync"}'
```

`REGISTRY_DISPATCH_TOKEN` should be a fine-scoped token or GitHub App token that can dispatch events to `verona-interfaces/registry`.

## GitHub Pages

The workflow uploads `README.md`, `registry.json`, and `index.html` as the Pages artifact, and the deploy job can publish that artifact. To use that path, set the repository Pages source to `GitHub Actions`.
