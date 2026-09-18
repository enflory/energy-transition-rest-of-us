#!/usr/bin/env python3
"""
Task runner for this repository.

    python run.py                     what needs doing right now
    python run.py brief    [show]     print the note-writing brief to paste
    python run.py fetch     <show>    scrape episodes that are not saved yet
    python run.py refetch   <show>    re-scrape everything, including saved
    python run.py validate [show]     structural check on every note
    python run.py dedupe   [show]     find republished episodes
    python run.py stats    [show]     archive size and coverage
    python run.py shows               list configured podcasts

`show` is a directory name under podcasts/, e.g. catalyst.

There is deliberately no Makefile: make is not installed by default on
Windows, and this repository is maintained from a Windows machine. Python is
the one interpreter guaranteed to be present, since the pipeline is written
in it.
"""

import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
PY = sys.executable or "python"


def script(name, *args):
    return subprocess.call([PY, os.path.join(ROOT, "scripts", name), *args])


def shows():
    base = os.path.join(ROOT, "podcasts")
    if not os.path.isdir(base):
        return []
    return sorted(d for d in os.listdir(base)
                  if os.path.isfile(os.path.join(base, d, "podcast.json")))


def need_show(args, command):
    if not args:
        sys.exit(f"'{command}' needs a show. Configured: {', '.join(shows())}")
    return args[0]


def main(argv):
    command = argv[0] if argv else "new"
    args = argv[1:]

    if command in ("-h", "--help", "help"):
        print(__doc__)
        return 0

    if command == "shows":
        for s in shows():
            print(s)
        return 0

    if command in ("new", "check", "status"):
        return script("new_episodes.py", *args)

    if command == "brief":
        return script("new_episodes.py", *args, "--brief")

    if command == "fetch":
        return script("scrape.py", need_show(args, "fetch"), "--all")

    if command == "refetch":
        return script("scrape.py", need_show(args, "refetch"), "--all",
                      "--force")

    if command == "validate":
        return script("validate_notes.py", *args)

    if command == "dedupe":
        return script("dedupe_check.py", *args)

    if command == "stats":
        return script("stats.py", *args)

    print(__doc__)
    return sys.exit(f"unknown command: {command}")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
