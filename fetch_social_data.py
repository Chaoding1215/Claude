#!/usr/bin/env python3
"""
SocialFetch — fetch_social_data.py

A lightweight data collection script that fetches the latest public social/data
posts from public APIs and structures them as clean JSON. Part of the SocialFetch
team's service offering.

Supports multiple public data sources:
  - jsonplaceholder : Fake posts from JSONPlaceholder (great for testing/demo)
  - hackernews      : Top stories from Hacker News (real social data, no auth)

Usage:
    python3 fetch_social_data.py --source hackernews --output data.json
    python3 fetch_social_data.py --source jsonplaceholder --output posts.json
    python3 fetch_social_data.py --count 10 --source hackernews

Requires: Python 3.8+ (stdlib only — no external dependencies)
"""

import json
import sys
import time
import urllib.error
import urllib.request
from argparse import ArgumentParser, Namespace
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


# ─── API Configuration ───────────────────────────────────────────────────────

API_SOURCES: Dict[str, Dict[str, Any]] = {
    "jsonplaceholder": {
        "url": "https://jsonplaceholder.typicode.com/posts",
        "description": "Fake posts from JSONPlaceholder (testing/demo API)",
        "parser": "jsonplaceholder",
    },
    "hackernews": {
        "url": "https://hacker-news.firebaseio.com/v0/topstories.json",
        "description": "Real top stories from Hacker News (public API, no auth)",
        "parser": "hackernews",
    },
}

REQUEST_TIMEOUT: int = 15  # seconds
DEFAULT_COUNT: int = 5


# ─── HTTP Helpers ────────────────────────────────────────────────────────────

def fetch_json(url: str) -> Any:
    """Fetch a URL and parse the response as JSON.

    Args:
        url: The URL to fetch.

    Returns:
        Parsed JSON data (dict or list).

    Raises:
        SystemExit: On network failure, HTTP error, or bad JSON.
    """
    req = urllib.request.Request(url, headers={"User-Agent": "SocialFetch/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=REQUEST_TIMEOUT) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw)
    except urllib.error.HTTPError as e:
        print(f"HTTP error {e.code} fetching {url}: {e.reason}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Network error fetching {url}: {e.reason}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON from {url}: {e}", file=sys.stderr)
        sys.exit(1)
    except TimeoutError:
        print(f"Request timed out after {REQUEST_TIMEOUT}s: {url}", file=sys.stderr)
        sys.exit(1)


# ─── Parsers ─────────────────────────────────────────────────────────────────

def parse_jsonplaceholder(raw: List[Dict[str, Any]], count: int) -> List[Dict[str, Any]]:
    """Parse JSONPlaceholder posts into structured SocialFetch format.

    Args:
        raw: Raw list of post dicts from the API.
        count: Maximum number of posts to return.

    Returns:
        List of structured post dicts.
    """
    posts = []
    for item in raw[:count]:
        posts.append({
            "id": item["id"],
            "source": "jsonplaceholder",
            "title": item.get("title", ""),
            "body": item.get("body", ""),
            "author_id": item.get("userId"),
            "url": f"https://jsonplaceholder.typicode.com/posts/{item['id']}",
            "fetched_at": datetime.now(timezone.utc).isoformat(),
        })
    return posts


def parse_hackernews(raw_ids: List[int], count: int) -> List[Dict[str, Any]]:
    """Parse Hacker News top stories into structured SocialFetch format.

    HN topstories.json returns a list of item IDs. We fetch each item's
    details individually (up to ``count`` items).

    Args:
        raw_ids: List of story IDs from /v0/topstories.json.
        count: Maximum number of stories to return.

    Returns:
        List of structured story dicts.
    """
    stories = []
    for story_id in raw_ids[:count]:
        item_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        try:
            item = fetch_json(item_url)
        except SystemExit:
            # Log the failure but continue with remaining stories
            print(f"Warning: failed to fetch story {story_id}", file=sys.stderr)
            continue

        if item is None or item.get("deleted") or item.get("dead"):
            continue

        stories.append({
            "id": item["id"],
            "source": "hackernews",
            "title": item.get("title", ""),
            "body": item.get("text", ""),
            "author": item.get("by", "unknown"),
            "score": item.get("score", 0),
            "comments": item.get("descendants", 0),
            "url": item.get("url", f"https://news.ycombinator.com/item?id={item['id']}"),
            "type": item.get("type", "story"),
            "fetched_at": datetime.now(timezone.utc).isoformat(),
        })
    return stories


PARSERS: Dict[str, Any] = {
    "jsonplaceholder": parse_jsonplaceholder,
    "hackernews": parse_hackernews,
}


# ─── Output ──────────────────────────────────────────────────────────────────

def build_output(
    source: str,
    posts: List[Dict[str, Any]],
    elapsed_ms: float,
) -> Dict[str, Any]:
    """Wrap the fetched posts into a structured output envelope.

    Args:
        source: API source name.
        posts: Parsed list of post dicts.
        elapsed_ms: Time taken for the fetch in milliseconds.

    Returns:
        A dict with metadata and results.
    """
    return {
        "meta": {
            "source": source,
            "count": len(posts),
            "fetched_at": datetime.now(timezone.utc).isoformat(),
            "elapsed_ms": round(elapsed_ms, 2),
            "version": "1.0.0",
        },
        "posts": posts,
    }


def save_json(data: Dict[str, Any], path: Optional[Path]) -> None:
    """Write data as pretty-printed JSON to a file or stdout.

    Args:
        data: The data to write.
        path: File path, or None to write to stdout.
    """
    output = json.dumps(data, indent=2, ensure_ascii=False)
    if path:
        path.write_text(output, encoding="utf-8")
        print(f"Saved {len(data['posts'])} posts to {path}", file=sys.stderr)
    else:
        print(output)


# ─── CLI ─────────────────────────────────────────────────────────────────────

def build_parser() -> ArgumentParser:
    parser = ArgumentParser(
        prog="fetch_social_data.py",
        description=(
            "Fetch the latest public social/data posts from a public API "
            "and save them as structured JSON."
        ),
    )
    parser.add_argument(
        "--source",
        "-s",
        choices=list(API_SOURCES.keys()),
        default="hackernews",
        help=f"Data source to fetch from (default: hackernews). "
             f"Available: {', '.join(API_SOURCES.keys())}",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=None,
        help="Output file path. If omitted, prints to stdout.",
    )
    parser.add_argument(
        "--count",
        "-c",
        type=int,
        default=DEFAULT_COUNT,
        help=f"Number of posts to fetch (default: {DEFAULT_COUNT}).",
    )
    parser.add_argument(
        "--list-sources",
        action="store_true",
        help="List available data sources and exit.",
    )
    return parser


def list_sources() -> None:
    """Print available data sources and their descriptions."""
    print("Available data sources:\n")
    for name, cfg in API_SOURCES.items():
        print(f"  {name:<20} {cfg['description']}")
    print()


def validate_args(args: Namespace) -> None:
    """Validate parsed arguments.

    Args:
        args: Parsed CLI arguments.

    Raises:
        SystemExit: If validation fails.
    """
    if args.count < 1:
        print("Error: --count must be at least 1", file=sys.stderr)
        sys.exit(1)
    if args.count > 100:
        print("Error: --count cannot exceed 100", file=sys.stderr)
        sys.exit(1)


# ─── Main ────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.list_sources:
        list_sources()
        return

    validate_args(args)

    source_cfg = API_SOURCES[args.source]
    parser_fn = PARSERS[args.source]

    print(
        f"Fetching {args.count} posts from '{args.source}'...",
        file=sys.stderr,
    )

    start = time.perf_counter()
    raw_data = fetch_json(source_cfg["url"])
    posts = parser_fn(raw_data, args.count)
    elapsed = (time.perf_counter() - start) * 1000  # ms

    output = build_output(source=args.source, posts=posts, elapsed_ms=elapsed)
    save_json(output, path=args.output)


if __name__ == "__main__":
    main()