#!/usr/bin/env python3
"""Refresh the generated repository activity block in profile/README.md."""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


START_MARKER = "<!-- repo-status:start -->"
END_MARKER = "<!-- repo-status:end -->"
README_PATH = Path("profile/README.md")
API_ROOT = os.environ.get("GITHUB_API_URL", "https://api.github.com")


def request_json(path: str) -> Any:
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GH_TOKEN or GITHUB_TOKEN is required")

    req = urllib.request.Request(
        f"{API_ROOT}{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "profile-readme-updater",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API request failed: {exc.code} {path}\n{body}") from exc


def event_payload() -> dict[str, Any]:
    event_path = os.environ.get("PROFILE_EVENT_PATH") or os.environ.get("GITHUB_EVENT_PATH")
    if not event_path:
        return {}

    path = Path(event_path)
    if not path.exists():
        return {}

    return json.loads(path.read_text(encoding="utf-8"))


def repository_name_from_event(payload: dict[str, Any]) -> str | None:
    client_payload = payload.get("client_payload") or {}
    repository = client_payload.get("repository") or payload.get("repository") or {}
    full_name = repository.get("full_name")
    if isinstance(full_name, str) and "/" in full_name:
        return full_name

    owner = repository.get("owner")
    owner_login = owner.get("login") if isinstance(owner, dict) else None
    name = repository.get("name")
    if owner_login and name:
        return f"{owner_login}/{name}"

    return None


def configured_repositories() -> list[str]:
    raw = os.environ.get("PROFILE_SOURCE_REPOS", "")
    return [repo.strip() for repo in raw.split(",") if repo.strip()]


def repository_summary(full_name: str) -> dict[str, Any]:
    repo = request_json(f"/repos/{full_name}")
    branches = request_json(f"/repos/{full_name}/branches?per_page=100")
    default_branch = repo.get("default_branch") or "main"
    default_branch_info = next(
        (branch for branch in branches if branch.get("name") == default_branch),
        {},
    )

    return {
        "full_name": repo["full_name"],
        "name": repo["name"],
        "description": repo.get("description") or "",
        "html_url": repo["html_url"],
        "default_branch": default_branch,
        "pushed_at": repo.get("pushed_at"),
        "updated_at": repo.get("updated_at"),
        "language": repo.get("language"),
        "stars": repo.get("stargazers_count", 0),
        "forks": repo.get("forks_count", 0),
        "archived": repo.get("archived", False),
        "private": repo.get("private", False),
        "branch_sha": (default_branch_info.get("commit") or {}).get("sha"),
    }


def sort_timestamp(repo: dict[str, Any]) -> str:
    return repo.get("pushed_at") or repo.get("updated_at") or ""


def short_sha(sha: str | None) -> str:
    return sha[:7] if sha else "unknown"


def friendly_date(value: str | None) -> str:
    if not value:
        return "unknown"
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return parsed.strftime("%Y-%m-%d %H:%M UTC")


def render_block(repositories: list[dict[str, Any]], source_event: str | None) -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [
        START_MARKER,
        "",
        "## Repository activity",
        "",
        f"_Last refreshed: {now}._",
        "",
    ]

    if source_event:
        lines.extend([f"_Most recent trigger: `{source_event}`._", ""])

    if not repositories:
        lines.extend(
            [
                "No source repositories are configured yet.",
                "",
                END_MARKER,
                "",
            ]
        )
        return "\n".join(lines)

    lines.extend(
        [
            "| Repository | Status | Last push | Default branch |",
            "| --- | --- | --- | --- |",
        ]
    )

    for repo in sorted(repositories, key=sort_timestamp, reverse=True):
        visibility = "private" if repo["private"] else "public"
        archived = ", archived" if repo["archived"] else ""
        language = f", {repo['language']}" if repo.get("language") else ""
        status = f"{visibility}{archived}{language}"
        branch = f"`{repo['default_branch']}` @ `{short_sha(repo.get('branch_sha'))}`"
        description = f"<br>{repo['description']}" if repo["description"] else ""
        name = f"[`{repo['full_name']}`]({repo['html_url']}){description}"
        lines.append(
            f"| {name} | {status} | {friendly_date(repo.get('pushed_at'))} | {branch} |"
        )

    lines.extend(["", END_MARKER, ""])
    return "\n".join(lines)


def replace_generated_block(readme: str, block: str) -> str:
    if START_MARKER in readme and END_MARKER in readme:
        before = readme.split(START_MARKER, 1)[0].rstrip()
        after = readme.split(END_MARKER, 1)[1].lstrip()
        return f"{before}\n\n{block}\n{after}".rstrip() + "\n"

    if readme.strip():
        return f"{readme.rstrip()}\n\n{block}\n"

    return f"# Welcome\n\n{block}\n"


def main() -> int:
    payload = event_payload()
    source_event = repository_name_from_event(payload)
    repos = configured_repositories()

    if source_event and source_event not in repos:
        repos.append(source_event)

    summaries = [repository_summary(repo) for repo in dict.fromkeys(repos)]
    block = render_block(summaries, source_event)

    README_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing = README_PATH.read_text(encoding="utf-8") if README_PATH.exists() else ""
    README_PATH.write_text(replace_generated_block(existing, block), encoding="utf-8")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
