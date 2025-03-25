import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_OWNER_REPO = os.getenv("GITHUB_OWNER_REPO")
GITHUB_API_BASE = os.getenv("GITHUB_API_BASE")


def get_recent_commits() -> list[dict]:
    url = f"{GITHUB_API_BASE}/repos/{GITHUB_OWNER_REPO}/commits"
    headers = {
        "X-GitHub-Api-Version": "2022-11-28",
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }
    params = {
        "per_page": 5
    }

    response = requests.get(url, headers=headers, params=params)

    response.raise_for_status()

    return response.json()


def parse_commit(commit: dict) -> dict:
    sha = commit["sha"]
    author = commit["commit"]["author"]["name"]
    date = commit["commit"]["author"]["date"]
    message = commit["commit"]["message"]
    url = commit["html_url"]

    name = f"{message.splitlines()[0]}"

    desc = (
        f"🧑 **Author**: {author}\n"
        f"📅 **Date**: {date}\n"
        f"🔤 **SHA**: `{sha}`\n"
        f"🔗 [View Commit]({url})"
    )

    return {
        "sha": sha,
        "name": name,
        "desc": desc
    }
