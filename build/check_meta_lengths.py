#!/usr/bin/env python3
"""Build-time check: every page's <title> must be <=60 chars and its meta
description <=160 chars (project rule R8). Mirrors check_authority.py style."""
import re, os
from html import unescape

SITE = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TITLE_MAX = 60
DESC_MAX = 160

def strip_tags(x): return re.sub(r"<[^>]+>", "", x)

pages = []
root_index = os.path.join(SITE, "index.html")
if os.path.exists(root_index):
    pages.append(("/", root_index))
for d in sorted(os.listdir(SITE)):
    p = os.path.join(SITE, d, "index.html")
    if os.path.isdir(os.path.join(SITE, d)) and os.path.exists(p):
        pages.append((f"/{d}/", p))

print("=== META LENGTH STANDARD CHECK (title <=60, description <=160) ===")
allpass = True
fails = []
for slug, p in pages:
    s = open(p, encoding="utf-8", errors="ignore").read()
    mt = re.search(r"<title>(.*?)</title>", s, re.S | re.I)
    md = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', s, re.S | re.I)
    title = unescape(strip_tags(mt.group(1)).strip()) if mt else ""
    desc = unescape(md.group(1).strip()) if md else ""
    tl, dl = len(title), len(desc)
    if not title:
        fails.append(f"  [FAIL] {slug}: MISSING <title>"); allpass = False
    elif tl > TITLE_MAX:
        fails.append(f"  [FAIL] {slug}: title {tl} chars (>{TITLE_MAX})"); allpass = False
    if not desc:
        fails.append(f"  [FAIL] {slug}: MISSING meta description"); allpass = False
    elif dl > DESC_MAX:
        fails.append(f"  [FAIL] {slug}: description {dl} chars (>{DESC_MAX})"); allpass = False

for line in fails:
    print(line)
print()
print(f"Checked {len(pages)} pages.")
print("ALL PAGES MEET META STANDARD" if allpass else f"{len(fails)} META VIOLATIONS — tighten titles/descriptions")
