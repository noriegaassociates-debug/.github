#!/usr/bin/env python3
"""Deterministically extract NMG Glassbox history events from browser-history Markdown exports.

This script creates event rows only from the supplied working files. It does not infer
missing events, validate visited sources, or promote history rows into evidentiary authority.
"""

import argparse
import csv
import hashlib
import re
import urllib.parse
from datetime import datetime
from pathlib import Path

DATE_RE = re.compile(r'^\*\*(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday), ([A-Za-z]+ \d{1,2}, \d{4})\*\*$')
TIME_RE = re.compile(r'^(\d{1,2}:\d{2})\s*([AP])M$', re.I)
LINK_RE = re.compile(r'^\[\*\*(.*?)\*\*\]\((\S+?)(?:\s+"(.*?)")?\)(.*)$')


def norm_line(value: str) -> str:
    return value.replace("\u202f", " ").replace("\xa0", " ").strip()


def normalize_markdown_url(value: str) -> str:
    for old, new in [("\\&", "&"), ("\\_", "_"), ("\\(", "("), ("\\)", ")"), ("\\;", ";"), ("\\=", "=")]:
        value = value.replace(old, new)
    return value


def hostname_family(hostname: str) -> str:
    h = (hostname or "").lower()
    if h.endswith("chatgpt.com"):
        return "ENGINE_INTERACTION_OPENAI"
    if h.endswith("gemini.google.com") or h.endswith("notebook.google.com"):
        return "ENGINE_INTERACTION_GOOGLE"
    if h.endswith("claude.ai"):
        return "ENGINE_INTERACTION_ANTHROPIC"
    if h.endswith("github.com") or h.endswith("githubusercontent.com"):
        return "REPOSITORY_OR_CODE_HOST"
    if h.endswith("patents.google.com") or h.endswith("patentimages.storage.googleapis.com"):
        return "PATENT_DISCOVERY_OR_DOCUMENT"
    if h.endswith(".gov") or ".gov" in h:
        return "GOVERNMENT_WEB_SOURCE"
    if h.endswith("archive.org"):
        return "ARCHIVE_SOURCE"
    if h.endswith("google.com"):
        return "SEARCH_OR_GOOGLE_SERVICE"
    return "WEB_SOURCE_OTHER" if h else "UNRESOLVED_HOST"


def extract(path: Path):
    raw = path.read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    lines = raw.decode("utf-8").splitlines()
    current_date = None
    rows = []
    i = 0
    while i < len(lines):
        text = norm_line(lines[i])
        dm = DATE_RE.match(text)
        if dm:
            current_date = datetime.strptime(dm.group(1), "%B %d, %Y").date()
            i += 1
            continue
        tm = TIME_RE.match(text)
        if tm and current_date:
            time_value = datetime.strptime(f"{tm.group(1)} {tm.group(2).upper()}M", "%I:%M %p").time()
            j = i + 1
            found = None
            while j < min(i + 10, len(lines)):
                candidate = norm_line(lines[j])
                if DATE_RE.match(candidate) or TIME_RE.match(candidate):
                    break
                lm = LINK_RE.match(candidate)
                if lm:
                    found = (j, lm)
                    break
                j += 1
            if found:
                j, lm = found
                title, raw_url, tooltip, trailer = lm.groups()
                normalized_url = normalize_markdown_url(raw_url)
                hostname = urllib.parse.urlparse(normalized_url).hostname or ""
                rows.append({
                    "source_file": path.name,
                    "source_file_sha256": sha,
                    "source_line_time": i + 1,
                    "source_line_link": j + 1,
                    "date": current_date.isoformat(),
                    "time_local": time_value.strftime("%H:%M"),
                    "timestamp_local": datetime.combine(current_date, time_value).isoformat(timespec="minutes"),
                    "title_exact": title,
                    "url_exact_markdown": raw_url,
                    "url_normalized_markdown_escapes_only": normalized_url,
                    "displayed_domain_exact": trailer.strip(),
                    "hostname_derived": hostname,
                    "source_kind_derived": hostname_family(hostname),
                    "tooltip_exact": tooltip or "",
                    "raw_link_line_exact": lines[j],
                    "validation_state": "HISTORY_EVENT_UNVALIDATED",
                    "promotion_state": "NOT_PROMOTED",
                })
                i = j + 1
                continue
        i += 1
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inputs", nargs="+", type=Path)
    ap.add_argument("-o", "--output", required=True, type=Path)
    args = ap.parse_args()

    rows = []
    for path in args.inputs:
        rows.extend(extract(path))
    rows.sort(key=lambda r: (r["timestamp_local"], r["source_file"], r["source_line_time"], r["source_line_link"]))
    for idx, row in enumerate(rows, 1):
        row["event_id"] = f"NMG-HIST-EVT-{idx:06d}"

    fields = ["event_id"] + [k for k in rows[0].keys() if k != "event_id"]
    with args.output.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {len(rows)} rows to {args.output}")


if __name__ == "__main__":
    main()
