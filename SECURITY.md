# Security Policy

## Supported versions

The current `main` branch is supported during early development.

## Reporting a vulnerability

Please open a private report through GitHub security advisories if available, or email `nasindia8@gmail.com` with:

- a short description of the issue
- steps to reproduce
- expected impact
- any suggested fix

## Security design

Codex OSS Maintainer Kit is read-only by default. It fetches public GitHub issue and pull request metadata, renders local summaries, and does not post comments, close issues, merge pull requests, or send repository data to a third-party service.

Future write-capable features should be opt-in, clearly labeled, and covered by tests.
