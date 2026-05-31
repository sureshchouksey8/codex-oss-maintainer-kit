from __future__ import annotations

import json
from dataclasses import asdict
from datetime import datetime
from typing import Any

from .models import MaintainerBrief, WorkItem


def _format_item(item: WorkItem) -> str:
    labels = f" [{', '.join(item.labels)}]" if item.labels else ""
    kind = "PR" if item.is_pull_request else "Issue"
    draft = " draft" if item.draft else ""
    return f"- {kind}{draft} #{item.number}: {item.title}{labels}\n  {item.html_url}"


def render_text(brief: MaintainerBrief, *, include_codex_prompt: bool = False) -> str:
    lines = [
        f"# Maintainer brief: {brief.repository}",
        "",
        f"Generated: {brief.generated_at.isoformat()}",
        f"Open items: {brief.total_open} ({brief.open_issues} issues, {brief.open_pull_requests} PRs)",
        f"Draft PRs: {len(brief.draft_pull_requests)}",
        f"Stale items: {len(brief.stale_items)}",
        "",
        "## Recent activity",
    ]
    lines.extend(_format_item(item) for item in brief.recent_items)

    if brief.stale_items:
        lines.append("")
        lines.append("## Stale attention queue")
        lines.extend(_format_item(item) for item in brief.stale_items[:8])

    if brief.label_counts:
        labels = ", ".join(f"{label}: {count}" for label, count in list(brief.label_counts.items())[:12])
        lines.extend(["", "## Label counts", labels])

    if include_codex_prompt:
        lines.extend(
            [
                "",
                "## Codex prompt",
                "Review this maintainer brief. Identify the three highest-leverage actions, call out any risky PRs or stale issues, and propose next steps that keep the maintainer in control. Do not post comments or merge anything without explicit approval.",
            ]
        )

    return "\n".join(lines).strip() + "\n"


def _json_default(value: Any) -> str:
    if isinstance(value, datetime):
        return value.isoformat()
    raise TypeError(f"Object of type {type(value).__name__} is not JSON serializable")


def render_json(brief: MaintainerBrief) -> str:
    return json.dumps(asdict(brief), default=_json_default, indent=2, sort_keys=True) + "\n"
