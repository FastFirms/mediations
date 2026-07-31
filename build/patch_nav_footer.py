#!/usr/bin/env python3
"""Patch all imported-post index.html files with the current nav() and footer()."""
import os, sys, re

sys.path.insert(0, os.path.dirname(__file__))
from templates import nav, footer

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NEW_NAV = nav()
NEW_FOOTER = footer()

NAV_RE = re.compile(r'<a href="#main" class="skip">.*?</header>', re.DOTALL)
FOOTER_RE = re.compile(r'</main><footer>.*?</footer>', re.DOTALL)

updated = 0
skipped = 0

for slug in sorted(os.listdir(OUT)):
    path = os.path.join(OUT, slug, "index.html")
    if not os.path.isfile(path):
        continue
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # Skip pages already on the current nav (has SVG logo)
    if 'MA.svg' in html:
        skipped += 1
        continue
    if '<a href="#main" class="skip">' not in html:
        skipped += 1
        continue

    new_html = NAV_RE.sub(
        '<a href="#main" class="skip">Skip to main content</a>' + NEW_NAV,
        html, count=1
    )
    new_html = FOOTER_RE.sub('</main>' + NEW_FOOTER, new_html, count=1)

    if new_html != html:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_html)
        updated += 1
        print(f"  patched: {slug}")
    else:
        skipped += 1

print(f"\nDone — {updated} pages patched, {skipped} skipped.")
