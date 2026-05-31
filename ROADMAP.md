# Roadmap

## 0.1

- Read open GitHub issues and pull requests.
- Produce a concise text summary.
- Produce JSON for downstream automation.
- Include a Codex-ready maintainer prompt.
- Keep all behavior read-only.

## 0.2

- Group items by milestone.
- Add optional severity scoring for stale security and release items.
- Add Markdown table output.
- Add repository health checks for missing license, README, security policy, and contribution guide.

## 0.3

- Add release-note draft generation from merged pull requests.
- Add local cache support to avoid repeated API calls.
- Add optional authenticated GitHub requests for higher rate limits.

## Guardrails

- No write actions without explicit maintainer approval.
- No telemetry.
- No hidden third-party data transfer.
- No automatic merging, closing, or commenting.
