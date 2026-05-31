from __future__ import annotations

import json
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from .models import WorkItem


class GitHubFetchError(RuntimeError):
    pass


def fetch_open_items(owner: str, repo: str, limit: int = 50) -> list[WorkItem]:
    query = urlencode(
        {
            "state": "open",
            "sort": "updated",
            "direction": "desc",
            "per_page": max(1, min(limit, 100)),
        }
    )
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?{query}"
    request = Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "codex-oss-maintainer-kit"})

    try:
        with urlopen(request, timeout=20) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        raise GitHubFetchError(f"GitHub returned HTTP {exc.code} for {owner}/{repo}") from exc
    except OSError as exc:
        raise GitHubFetchError(f"Could not fetch {owner}/{repo}: {exc}") from exc

    return [WorkItem.from_github(item) for item in payload]


def load_fixture(path: str) -> list[WorkItem]:
    with open(path, "r", encoding="utf-8") as handle:
        payload = json.load(handle)
    return [WorkItem.from_github(item) for item in payload]
