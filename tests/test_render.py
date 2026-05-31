from datetime import datetime, timezone

from oss_maintainer_kit.github import load_fixture
from oss_maintainer_kit.render import render_json, render_text
from oss_maintainer_kit.summarizer import build_brief


def _brief():
    items = load_fixture("tests/fixtures/sample_items.json")
    return build_brief(
        "example/project",
        items,
        now=datetime(2026, 6, 1, tzinfo=timezone.utc),
        stale_after_days=30,
    )


def test_render_text_includes_codex_prompt_when_requested():
    output = render_text(_brief(), include_codex_prompt=True)

    assert "# Maintainer brief: example/project" in output
    assert "Open items: 3 (1 issues, 2 PRs)" in output
    assert "## Codex prompt" in output
    assert "Do not post comments or merge anything without explicit approval." in output


def test_render_json_outputs_repository_and_counts():
    output = render_json(_brief())

    assert '"repository": "example/project"' in output
    assert '"open_pull_requests": 2' in output
