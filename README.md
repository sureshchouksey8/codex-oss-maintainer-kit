# Codex OSS Maintainer Kit

Codex OSS Maintainer Kit is a small command-line tool for maintainers who want a clean, auditable briefing before using Codex on open-source project work.

It turns GitHub issues and pull requests into a compact maintenance brief: stale items, recently updated work, labels, draft PRs, likely review targets, and a prompt block that can be pasted into Codex for deeper triage.

## Why this exists

Maintainers spend a lot of time collecting context before they can make decisions. This project keeps that first pass simple and reproducible:

- fetch public GitHub issues and pull requests without requiring a token
- summarize review and triage queues in plain text or JSON
- produce a Codex-ready prompt that keeps the human maintainer in charge
- run locally, with no background service and no telemetry

## Install

```bash
python3 -m pip install .
```

For local development:

```bash
python3 -m pip install -e ".[dev]"
python3 -m pytest
```

## Usage

Summarize a public repository:

```bash
oss-maintainer-kit sureshchouksey8 codex-oss-maintainer-kit
```

Use JSON output:

```bash
oss-maintainer-kit sureshchouksey8 codex-oss-maintainer-kit --format json
```

Include a Codex prompt block:

```bash
oss-maintainer-kit sureshchouksey8 codex-oss-maintainer-kit --codex-prompt
```

Use local fixture data instead of the GitHub API:

```bash
oss-maintainer-kit --fixture tests/fixtures/sample_items.json --codex-prompt
```

## Maintainer workflow

The intended workflow is:

1. Run the CLI against a repository.
2. Read the brief and choose the items worth attention.
3. Paste the generated prompt into Codex.
4. Let Codex inspect the selected issues or PRs in depth.
5. Review and approve any proposed code, comments, or release notes yourself.

The tool is intentionally conservative. It does not post comments, close issues, merge pull requests, or make account decisions.

See [docs/codex-workflow.md](docs/codex-workflow.md) for a longer Codex-assisted workflow and [examples/sample-brief.md](examples/sample-brief.md) for example output.

## Project status

This is a new open-source project maintained by Suresh Chouksey as part of a broader Codex-assisted OSS workflow. The first milestone is a dependable triage brief for small and medium public repositories.

## License

MIT
