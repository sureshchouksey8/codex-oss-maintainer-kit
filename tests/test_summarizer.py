from datetime import datetime, timezone

from oss_maintainer_kit.github import load_fixture
from oss_maintainer_kit.summarizer import build_brief


def test_build_brief_counts_issues_prs_stale_and_labels():
    items = load_fixture("tests/fixtures/sample_items.json")
    brief = build_brief(
        "example/project",
        items,
        now=datetime(2026, 6, 1, tzinfo=timezone.utc),
        stale_after_days=30,
    )

    assert brief.total_open == 3
    assert brief.open_issues == 1
    assert brief.open_pull_requests == 2
    assert [item.number for item in brief.stale_items] == [15]
    assert [item.number for item in brief.draft_pull_requests] == [15]
    assert brief.label_counts["release"] == 2
    assert brief.label_counts["security"] == 1


def test_recent_items_are_sorted_by_updated_time():
    items = load_fixture("tests/fixtures/sample_items.json")
    brief = build_brief(
        "example/project",
        items,
        now=datetime(2026, 6, 1, tzinfo=timezone.utc),
    )

    assert [item.number for item in brief.recent_items] == [14, 12, 15]
