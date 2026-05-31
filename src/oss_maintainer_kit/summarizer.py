from __future__ import annotations

from collections import Counter
from datetime import datetime, timedelta, timezone

from .models import MaintainerBrief, WorkItem


def build_brief(
    repository: str,
    items: list[WorkItem],
    *,
    now: datetime | None = None,
    stale_after_days: int = 30,
    recent_limit: int = 8,
) -> MaintainerBrief:
    current_time = now or datetime.now(timezone.utc)
    stale_before = current_time - timedelta(days=stale_after_days)

    open_items = [item for item in items if item.state == "open"]
    stale_items = tuple(item for item in open_items if item.updated_at < stale_before)
    recent_items = tuple(sorted(open_items, key=lambda item: item.updated_at, reverse=True)[:recent_limit])
    draft_pull_requests = tuple(item for item in open_items if item.is_pull_request and item.draft)

    labels: Counter[str] = Counter()
    for item in open_items:
        labels.update(item.labels)

    return MaintainerBrief(
        repository=repository,
        generated_at=current_time,
        total_open=len(open_items),
        open_issues=sum(1 for item in open_items if not item.is_pull_request),
        open_pull_requests=sum(1 for item in open_items if item.is_pull_request),
        stale_items=stale_items,
        recent_items=recent_items,
        draft_pull_requests=draft_pull_requests,
        label_counts=dict(labels.most_common()),
    )
