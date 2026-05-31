from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


def parse_github_time(value: str) -> datetime:
    """Parse the timestamp format returned by the GitHub REST API."""
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)


@dataclass(frozen=True)
class WorkItem:
    number: int
    title: str
    state: str
    html_url: str
    updated_at: datetime
    created_at: datetime
    labels: tuple[str, ...] = ()
    is_pull_request: bool = False
    draft: bool = False
    author: str | None = None

    @classmethod
    def from_github(cls, payload: dict[str, Any]) -> "WorkItem":
        labels = tuple(label["name"] for label in payload.get("labels", []))
        pull_request = payload.get("pull_request")
        return cls(
            number=int(payload["number"]),
            title=str(payload["title"]),
            state=str(payload["state"]),
            html_url=str(payload["html_url"]),
            updated_at=parse_github_time(str(payload["updated_at"])),
            created_at=parse_github_time(str(payload["created_at"])),
            labels=labels,
            is_pull_request=pull_request is not None,
            draft=bool(payload.get("draft", False)),
            author=(payload.get("user") or {}).get("login"),
        )


@dataclass(frozen=True)
class MaintainerBrief:
    repository: str
    generated_at: datetime
    total_open: int
    open_issues: int
    open_pull_requests: int
    stale_items: tuple[WorkItem, ...] = field(default_factory=tuple)
    recent_items: tuple[WorkItem, ...] = field(default_factory=tuple)
    draft_pull_requests: tuple[WorkItem, ...] = field(default_factory=tuple)
    label_counts: dict[str, int] = field(default_factory=dict)
