#!/usr/bin/env python3
"""Build-time check: HARD RULE — blog H1s are short, single-phrase titles.

Fails (exit 1) if a blog post's H1 is over 60 visible characters, has a
subtitle after ':' / ' — ' / ' – ' / ' - ', or a second sentence after '?'.
LEGACY lists posts published before the rule; they warn until shortened.
"""
import os, re, sys, html
sys.path.insert(0, os.path.dirname(__file__))
SITE = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX = 60

src = open(os.path.join(os.path.dirname(__file__), "check_authority.py")).read()
BLOG = re.findall(r"'([a-z0-9-]+)'", src[src.index("BLOG="):src.index("def content_only")])

LEGACY = set()


def problems(t):
    out = []
    if len(t) > MAX:
        out.append(f"{len(t)} chars (max {MAX})")
    if re.search(r":\s| [—–-] ", t):
        out.append("has a subtitle")
    if re.search(r"\?\s+\S", t):
        out.append("second sentence after '?'")
    return out


fails, legacy = [], []
for slug in BLOG:
    p = os.path.join(SITE, slug, "index.html")
    if not os.path.exists(p):
        continue
    m = re.search(r"<h1[^>]*>(.*?)</h1>", open(p).read(), re.S)
    if not m:
        fails.append((slug, "no H1", ""))
        continue
    t = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()
    pr = problems(t)
    if pr:
        (legacy if slug in LEGACY else fails).append((slug, "; ".join(pr), t))

print(f"=== BLOG TITLE RULE (≤{MAX} chars, one phrase) ===")
for s, why, t in legacy:
    print(f"  [LEGACY] {s}: {why}")
for s, why, t in fails:
    print(f"  [FAIL] {s}: {why}\n         \"{t}\"")
if fails:
    print("TITLE RULE FAILED — shorten the H1 (put the extra angle in the dek)")
    sys.exit(1)
print(f"ALL NEW TITLES PASS ({len(legacy)} legacy titles still to shorten)")
