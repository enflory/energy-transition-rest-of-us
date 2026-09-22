#!/usr/bin/env python3
"""
Task runner for this repository.

    python run.py                       what needs doing right now
    python run.py brief    [source]     print the note-writing brief to paste
    python run.py fetch     <source>    scrape items that are not saved yet
    python run.py refetch   <source>    re-scrape everything, including saved
    python run.py validate [source]     structural check on every note
    python run.py dedupe   [source]     find republished items
    python run.py stats    [source]     archive size and coverage
    python run.py sources               list configured sources

`source` is a directory name under sources/, e.g. catalyst or steel-for-fuel.
A source is a podcast or a newsletter; `content_type` in its source.json says
which, and everything downstream follows from that.

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
    sys.path.insert(0, os.path.join(ROOT, "scripts"))
    import archive
    return archive.source_names()


def need_show(args, command):
    if not args:
        sys.exit(f"'{command}' needs a source. "
                 f"Configured: {', '.join(shows())}")
    return args[0]


def main(argv):
    command = argv[0] if argv else "new"
    args = argv[1:]

    if command in ("-h", "--help", "help"):
        print(__doc__)
        return 0

    if command in ("sources", "shows"):
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
