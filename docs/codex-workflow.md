# Codex Workflow

This project is designed for a human-maintained Codex loop:

1. Generate a repository brief.
2. Pick the small set of issues or pull requests that deserve attention.
3. Ask Codex to inspect those items deeply.
4. Apply code or documentation changes locally.
5. Run tests.
6. Let the maintainer approve any GitHub comments, merges, or releases.

## Example prompt

```text
Use this maintainer brief as context. Find the top three actions that reduce maintainer load this week. Separate quick documentation fixes from code changes, and do not suggest posting comments, closing issues, or merging pull requests without explicit approval.
```

## Why read-only first

Maintainer automation can become noisy quickly. This tool starts with read-only summaries because the safest useful automation is often context gathering, not account action.
