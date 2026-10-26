#!/usr/bin/env python3
"""Shared GitHub token loader for brain scripts.

Zero dependencies: Python 3 stdlib only (matches transcript_memory.py's
convention). Any script in this repo that needs to call the GitHub API
should import github_token() from here instead of reading .env itself or
hardcoding a value.

  from gh_env import github_token
  token = github_token()
  if not token:
      sys.exit("GITHUB_TOKEN not set - see .env.example")

Precedence: a real environment variable (e.g. exported in your shell,
or injected by CI as a secret) always wins. The repo-root .env file
(git-ignored, never committed) only fills the gap for local dev.

This module never prints or logs the token value.
"""

import os
from pathlib import Path


def _repo_root() -> Path:
    """Walk up from this file to the nearest ancestor containing .git."""
    here = Path(__file__).resolve()
    for parent in (here, *here.parents):
        if (parent / ".git").exists():
            return parent
    # Fallback: plugins/brain/scripts/gh_env.py -> repo root is 3 levels up.
    return here.parents[3]


def load_dotenv(path: Path | None = None) -> None:
    """Parse a KEY=VALUE .env file into os.environ (existing env vars win)."""
    env_path = path or (_repo_root() / ".env")
    if not env_path.is_file():
        return
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key:
            os.environ.setdefault(key, value)


def github_token() -> str | None:
    """Return the GitHub token from the environment or repo-root .env, or None."""
    load_dotenv()
    return os.environ.get("GITHUB_TOKEN") or None
