#!/usr/bin/env python3
"""
Auto-pulling repo server with public tunnel.

Edit the CONFIG section below, then run:

    brew install cloudflared        # macOS
    python serve_repo.py

The script will:
  1. Clone REPO_URL into LOCAL_DIR (or reuse an existing checkout).
  2. Install requirements.txt if present.
  3. Launch ENTRY_FILE as a subprocess with --host, --port, --foreground,
     and --no-iframe CLI flags (matches minesweeper_server.py).
  4. Start a cloudflared quick tunnel  ->  prints a public *.trycloudflare.com URL.
  5. Every POLL_INTERVAL_SEC, check origin/BRANCH for new commits.
     On change: git pull, reinstall requirements, restart the app.
Stop with Ctrl-C.
"""

import os
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path

# ---------- CONFIG ----------
REPO_URL = "https://github.com/KKallas/minesweepers.git"
BRANCH = "master"
LOCAL_DIR = Path("./repo_checkout")
ENTRY_FILE = "minesweeper_server.py"
HOST = "127.0.0.1"
PORT = 8765                      # minesweeper_server.py default
POLL_INTERVAL_SEC = 60
USE_TUNNEL = True                # set False to skip cloudflared and only serve locally
EXTRA_ARGS = ["--foreground", "--no-iframe"]   # passed to ENTRY_FILE; --foreground keeps
                                               # the process attached so we can manage it
# ----------------------------


def run(cmd, cwd=None, check=True, capture=False):
    return subprocess.run(cmd, cwd=cwd, check=check, capture_output=capture, text=True)


def clone_or_open():
    if not LOCAL_DIR.exists():
        print(f"[git] cloning {REPO_URL} -> {LOCAL_DIR}")
        run(["git", "clone", "--branch", BRANCH, REPO_URL, str(LOCAL_DIR)])
    else:
        print(f"[git] using existing checkout at {LOCAL_DIR}")


def remote_sha():
    r = run(["git", "ls-remote", REPO_URL, BRANCH], capture=True)
    return r.stdout.split()[0] if r.stdout.strip() else None


def local_sha():
    r = run(["git", "rev-parse", "HEAD"], cwd=LOCAL_DIR, capture=True)
    return r.stdout.strip()


def pull():
    print("[git] pulling latest...")
    run(["git", "pull", "--ff-only", "origin", BRANCH], cwd=LOCAL_DIR)


def install_requirements():
    req = LOCAL_DIR / "requirements.txt"
    if req.exists():
        print("[pip] installing requirements.txt")
        run([sys.executable, "-m", "pip", "install", "-q", "-r", str(req)])


def start_app():
    print(f"[app] running {ENTRY_FILE} on http://{HOST}:{PORT}")
    cmd = [sys.executable, ENTRY_FILE,
           "--host", HOST, "--port", str(PORT), *EXTRA_ARGS]
    return subprocess.Popen(cmd, cwd=LOCAL_DIR)


def start_tunnel():
    if not shutil.which("cloudflared"):
        print("[cloudflared] not found on PATH.")
        print("  macOS:   brew install cloudflared")
        print("  Linux:   https://github.com/cloudflare/cloudflared/releases/latest")
        print("  ...or set USE_TUNNEL = False to disable.")
        sys.exit(1)
    print("[cloudflared] starting quick tunnel (public URL will appear below)")
    return subprocess.Popen(
        ["cloudflared", "tunnel", "--url", f"http://{HOST}:{PORT}"],
    )


def main():
    clone_or_open()
    install_requirements()
    server = start_app()
    tunnel = start_tunnel() if USE_TUNNEL else None

    stopping = False

    def cleanup(*_):
        nonlocal stopping
        if stopping:
            return
        stopping = True
        print("\n[shutdown] stopping...")
        for p in (tunnel, server):
            if p and p.poll() is None:
                p.terminate()
                try:
                    p.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    p.kill()
        sys.exit(0)

    signal.signal(signal.SIGINT, cleanup)
    signal.signal(signal.SIGTERM, cleanup)

    try:
        while True:
            time.sleep(POLL_INTERVAL_SEC)
            try:
                if remote_sha() != local_sha():
                    print("[git] new commit on remote, updating")
                    pull()
                    install_requirements()
                    print("[app] restarting")
                    server.terminate()
                    try:
                        server.wait(timeout=10)
                    except subprocess.TimeoutExpired:
                        server.kill()
                    server = start_app()
                else:
                    print("[git] up to date")
            except subprocess.CalledProcessError as e:
                print(f"[git] error: {e}")
    finally:
        cleanup()


if __name__ == "__main__":
    main()
