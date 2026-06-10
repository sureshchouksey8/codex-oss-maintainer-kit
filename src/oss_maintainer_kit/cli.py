from __future__ import annotations

import argparse
import importlib.metadata

from .github import fetch_open_items, load_fixture
from .render import render_json, render_text
from .summarizer import build_brief


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate a GitHub OSS maintainer triage brief.")
    parser.add_argument("owner", nargs="?", help="GitHub repository owner")
    parser.add_argument("repo", nargs="?", help="GitHub repository name")
    parser.add_argument("--fixture", help="Read GitHub issue API JSON from a local fixture file")
    parser.add_argument("--limit", type=int, default=50, help="Maximum open GitHub items to fetch")
    parser.add_argument("--stale-after-days", type=int, default=30, help="Mark items stale after this many days")
    parser.add_argument("--format", choices=("text", "json"), default="text", help="Output format")
    parser.add_argument("--codex-prompt", action="store_true", help="Append a Codex-ready prompt block")
    parser.add_argument("--version", action="version", version=f"%(prog)s {importlib.metadata.version('codex-oss-maintainer-kit')}", help="Show version and exit")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.fixture:
        items = load_fixture(args.fixture)
        repository = f"{args.owner or 'fixture'}/{args.repo or 'local'}"
    else:
        if not args.owner or not args.repo:
            parser.error("owner and repo are required unless --fixture is provided")
        items = fetch_open_items(args.owner, args.repo, limit=args.limit)
        repository = f"{args.owner}/{args.repo}"

    brief = build_brief(repository, items, stale_after_days=args.stale_after_days)
    if args.format == "json":
        print(render_json(brief), end="")
    else:
        print(render_text(brief, include_codex_prompt=args.codex_prompt), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
