"""Regression tests for the manifest merge in scrape.py.

    python3 scripts/test_manifest.py        (add -v for each test's name)

write_manifest has lost data twice. An early version rewrote the file
wholesale and a partial run cut it from 146 rows to 48. Later, a blocked
fetch rewrote 20 dated "no transcript" rows as undated errors, which also
made them look like pending work to the status check. These tests pin the
merge order that prevents both, without touching the network or any file in
the repository: every manifest they write lives in a temporary directory.

They reach into scrape.py's module globals (OUT_ROOT, MANIFEST) and replace
load_config, fetch and parse for the end-to-end case. A refactor of those
names needs this file updated with it.
"""
import csv
import email.message
import errno
import os
import shutil
import socket
import ssl
import sys
import tempfile
import unittest
import urllib.error

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(SCRIPTS)
sys.path.insert(0, SCRIPTS)
import scrape  # noqa: E402

HEADER = ["published", "title", "status", "words", "folder", "url"]
U = "https://example.com/a"
NT = ["2023-11-03", "slug-a", "no transcript", "", "", U]
NT2 = ["2023-11-04", "slug-a", "no transcript", "", "", U]
ERR = ["", "slug-a", "error: HTTPError", "", "", U]
ERR2 = ["", "slug-a", "error: URLError", "", "", U]
PERR = ["", "slug-a", "error: IndexError", "", "", U]
SAVED = ["2024-01-01", "T", "saved", "10", "2024-01-01-t", U]


def http_error(code):
    return urllib.error.HTTPError("https://example.com/", code, "msg",
                                  email.message.Message(), None)


def read(path):
    with open(path, encoding="utf-8", newline="") as f:
        return {r[5]: r for r in csv.reader(f)
                if len(r) == 6 and r[0] != "published"}


class ScrapeTestCase(unittest.TestCase):
    """Points scrape.py at a temp directory and restores it afterwards."""

    PATCHED = ("OUT_ROOT", "MANIFEST", "load_config", "fetch", "parse")

    def setUp(self):
        self.saved_attrs = {a: getattr(scrape, a) for a in self.PATCHED}
        self.saved_sleep = scrape.time.sleep
        scrape.time.sleep = lambda seconds: None
        scrape.load_config("catalyst")  # a podcast source: "no transcript"
        self.tmp = tempfile.mkdtemp(prefix="test-manifest-")
        scrape.OUT_ROOT = os.path.join(self.tmp, "episodes")
        scrape.MANIFEST = os.path.join(self.tmp, "manifest.csv")
        os.makedirs(scrape.OUT_ROOT)

    def tearDown(self):
        for a, v in self.saved_attrs.items():
            setattr(scrape, a, v)
        scrape.time.sleep = self.saved_sleep
        shutil.rmtree(self.tmp, ignore_errors=True)

    def write_prior(self, rows):
        with open(scrape.MANIFEST, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, lineterminator="\n")
            w.writerow(HEADER)
            w.writerows(rows)

    def save_document(self, folder, url):
        d = os.path.join(scrape.OUT_ROOT, folder)
        os.makedirs(d)
        with open(os.path.join(d, scrape.KIND["source_file"]), "w",
                  encoding="utf-8") as f:
            f.write(f'---\ntitle: "T"\nurl: "{url}"\n'
                    f'published: "2024-01-01T00:00:00"\nword_count: 10\n---\n')

    def merged(self, prior, rows, unreached=(), saved=()):
        self.write_prior(prior)
        for folder, url in saved:
            self.save_document(folder, url)
        self.kept = scrape.write_manifest(rows, set(unreached))
        return read(scrape.MANIFEST)


class Unreachable(unittest.TestCase):
    """Which fetch failures say nothing about the item itself."""

    def test_blocks_rate_limits_and_server_errors(self):
        for code in (403, 408, 429, 500, 503):
            with self.subTest(code=code):
                self.assertTrue(scrape.unreachable(http_error(code)))

    def test_client_errors_are_news_about_the_page(self):
        for code in (400, 404, 410):
            with self.subTest(code=code):
                self.assertFalse(scrape.unreachable(http_error(code)))

    def test_network_level_failures(self):
        for exc in (urllib.error.URLError("dns"), socket.timeout(),
                    ConnectionResetError(), ssl.SSLEOFError(),
                    OSError(errno.EHOSTUNREACH, "no route")):
            with self.subTest(exc=type(exc).__name__):
                self.assertTrue(scrape.unreachable(exc))

    def test_failures_that_are_not_about_the_network(self):
        for exc in (IndexError(), ValueError(),
                    UnicodeDecodeError("utf-8", b"\xff", 0, 1, "bad")):
            with self.subTest(exc=type(exc).__name__):
                self.assertFalse(scrape.unreachable(exc))


class MergeOrder(ScrapeTestCase):

    def test_unreached_keeps_the_no_document_row(self):
        self.assertEqual(self.merged([NT], [ERR], unreached=[U])[U], NT)
        self.assertEqual(self.kept, 1)

    def test_other_errors_replace_the_no_document_row(self):
        self.assertEqual(self.merged([NT], [PERR])[U], PERR)
        self.assertEqual(self.kept, 0)

    def test_new_url_records_its_error(self):
        self.assertEqual(self.merged([], [ERR], unreached=[U])[U], ERR)

    def test_newer_error_replaces_earlier_error(self):
        self.assertEqual(self.merged([ERR], [ERR2], unreached=[U])[U], ERR2)

    def test_outcome_replaces_earlier_error(self):
        self.assertEqual(self.merged([ERR], [NT2])[U], NT2)

    def test_outcome_replaces_earlier_outcome(self):
        self.assertEqual(self.merged([NT], [NT2])[U], NT2)

    def test_saved_on_disk_survives_an_unreached_error(self):
        got = self.merged([SAVED], [ERR], unreached=[U],
                          saved=[("2024-01-01-t", U)])
        self.assertEqual(got[U], SAVED)

    def test_stale_saved_row_gives_way_to_the_error(self):
        # The manifest says saved, but the document is not on disk.
        self.assertEqual(self.merged([SAVED], [ERR], unreached=[U])[U], ERR)

    def test_untouched_rows_are_never_dropped(self):
        other = ["2022-01-01", "slug-b", "no transcript", "", "",
                 "https://example.com/b"]
        got = self.merged([NT, other], [NT2])
        self.assertEqual(got[other[5]], other)


class ReplayOnTheRealManifest(ScrapeTestCase):
    """Every "no transcript" URL in the real Catalyst manifest comes back
    403, which is what happened on 2026-11-11. Each row must survive.

    The committed manifest is copied, never written. The real episodes
    directory is only read; the transcripts in it are gitignored, so on a
    fresh checkout it holds notes only and contributes no saved rows.
    """

    def test_blocked_retry_keeps_every_no_transcript_row(self):
        shutil.copy(os.path.join(REPO, "sources", "catalyst", "manifest.csv"),
                    scrape.MANIFEST)
        scrape.OUT_ROOT = os.path.join(REPO, "sources", "catalyst", "episodes")
        before = read(scrape.MANIFEST)
        urls = [u for u, r in before.items() if r[2] == "no transcript"]
        self.assertTrue(urls, "the Catalyst manifest has no rows to replay")
        rows = [["", u.rstrip("/").rsplit("/", 1)[-1], "error: HTTPError",
                 "", "", u] for u in urls]
        scrape.write_manifest(rows, set(urls))
        after = read(scrape.MANIFEST)
        self.assertEqual([after.get(u) for u in urls],
                         [before[u] for u in urls])


class FetchLoop(ScrapeTestCase):
    """main() marks a URL unreached only when fetch() never got the page."""

    BLOCKED = "https://example.com/blocked"
    GONE = "https://example.com/gone"
    CRASH = "https://example.com/crash"
    NEW = "https://example.com/new"

    def test_only_unreached_pages_keep_their_rows(self):
        prior = [["2023-01-01", s, "no transcript", "", "", u]
                 for s, u in [("blocked", self.BLOCKED), ("gone", self.GONE),
                              ("crash", self.CRASH)]]
        self.write_prior(prior)
        paths = (scrape.OUT_ROOT, scrape.MANIFEST)
        real_load = self.saved_attrs["load_config"]

        def load_config(source):
            real_load(source)
            scrape.OUT_ROOT, scrape.MANIFEST = paths
            return scrape.CFG

        def fetch(url):
            if url in (self.BLOCKED, self.NEW):
                raise http_error(403)
            if url == self.GONE:
                raise http_error(404)
            return "<html>a page that arrived</html>"

        def parse(page, url):
            raise IndexError("a layout the parser has not seen")

        scrape.load_config, scrape.fetch, scrape.parse = load_config, fetch, parse
        with open(os.devnull, "w") as quiet:
            stdout, sys.stdout = sys.stdout, quiet
            try:
                scrape.main(["catalyst", self.BLOCKED, self.GONE, self.CRASH,
                             self.NEW])
            finally:
                sys.stdout = stdout

        got = read(scrape.MANIFEST)
        self.assertEqual(got[self.BLOCKED], prior[0])
        self.assertEqual(got[self.GONE][2], "error: HTTPError")
        self.assertEqual(got[self.CRASH][2], "error: IndexError")
        self.assertEqual(got[self.NEW][2], "error: HTTPError")


if __name__ == "__main__":
    unittest.main()
