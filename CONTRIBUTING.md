# Contributing

Thanks for considering a contribution. This project is intentionally small and maintainer-focused, so the best contributions are practical improvements to triage quality, output clarity, tests, and documentation.

## Development setup

```bash
python3 -m pip install -e ".[dev]"
python3 -m pytest
```

## Good first contributions

- Add a renderer for Markdown tables.
- Improve stale-item scoring.
- Add support for release milestone grouping.
- Add fixtures for common GitHub issue and pull request shapes.
- Improve README examples.

## Pull request expectations

- Keep changes small and reviewable.
- Add or update tests for behavior changes.
- Do not add telemetry, background network calls, or write actions without a clear maintainer discussion first.
- Make it clear when a feature only reads GitHub data versus when it could write to GitHub.

## Maintainer stance

This tool is designed to help humans make decisions. It should not auto-close issues, post comments, merge pull requests, or make release decisions without explicit maintainer approval.
