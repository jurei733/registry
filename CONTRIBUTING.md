# Contributing

This repository is generated. The source of truth is:

- GitHub repository metadata
- Latest release or latest tag metadata
- Module metadata extracted from HTML, preferring release assets and then the matching release or tag ref

## Updating the registry

The sync workflow supports three triggers:

- Daily schedule
- Manual `workflow_dispatch`
- `repository_dispatch` with `event_type=registry-sync`

The daily schedule is only a fallback. For low-activity public repositories, GitHub can disable scheduled workflows after long periods without repository activity, so upstream `repository_dispatch` events are the more reliable sync trigger.

The generated artifacts are:

- `README.md`
- `registry.json`

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

If this repository should publish a website, set the Pages source to `GitHub Actions`. The workflow already uploads `README.md`, `registry.json`, and `index.html` as the Pages artifact.
