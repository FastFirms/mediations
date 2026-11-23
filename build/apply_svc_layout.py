#!/usr/bin/env python3
"""Post-build: move remaining old single-column pages onto the service-page layout
(hero image, key takeaway, contents menu, sticky assessment sidebar).
Idempotent: skips pages that already have svc-layout. Re-run after rebuilding any
listed page's generator."""
import os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import quiz_card
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CITIES = ["sydney", "melbourne", "brisbane", "perth", "adelaide", "canberra", "gold-coast"]
FL = ["adelaide", "ballarat", "bendigo", "campbelltown", "canberra", "central-coast", "darwin", "geelong",
      "gold-coast", "hobart", "ipswich", "launceston", "mandurah", "melbourne", "newcastle", "penrith",
      "perth", "rockhampton", "toowoomba", "townsville", "wollongong"]
PAGES = {}
for c in CITIES:
    PAGES[f"parenting-mediation-{c}"] = "hero-parenting-plan-mediation.jpg"
    PAGES[f"property-settlement-mediation-{c}"] = "hero-property-settlement-mediation.jpg"
    PAGES[f"workplace-mediation-{c}"] = "hero-workplace-mediation.jpg"
    PAGES[f"divorce-mediation-{c}"] = "hero-divorce-counselling.jpg"
for c in FL:
    PAGES[f"{c}-family-lawyers"] = "hero-family-law-mediation.jpg"
PAGES.update({
    "family-law-mediation": "hero-family-law-mediation.jpg",
    "divorce-mediation": "hero-divorce-counselling.jpg",
    "employment-dispute-mediation": "hero-unfair-dismissal-mediation.jpg",
    "workplace-mediation-cost": "hero-workplace-mediation.jpg",
    "team-conflict-facilitation": "hero-workplace-mediation.jpg",
    "family-law-cost-estimator": "hero-our-fees.jpg",
    "divorce-mediation": "hero-divorce-counselling.jpg",
})

def transform(d, img):
    if "background-image" in d[d.find('<section class="phero"'):d.find('<section class="phero"') + 600]:
        return None
    hm = re.search(r'<section class="phero">\s*(<div class="phero-blob"></div>)?', d)
    if not hm:
        return None
    style = (' style="background-image:linear-gradient(to right,rgba(245,249,255,1) 0%,rgba(245,249,255,.95) 38%,'
             'rgba(245,249,255,.7) 55%,rgba(245,249,255,.2) 75%,rgba(245,249,255,0) 82%),'
             f"url('/assets/images/{img}');background-size:cover;background-position:center 50%;position:relative\"")
    d = d[:hm.start()] + '<section class="phero"' + style + '><div class="phero-blob" style="opacity:.2"></div>' + d[hm.end():]
    if "svc-layout" in d:
        return d  # already on the service layout: hero image only
    hero_end = d.index("</section>", d.index('<section class="phero"')) + len("</section>")
    a0 = d.find('<article class="body">', hero_end)
    if a0 < 0:
        return d  # page has its own section layout: hero image only
    between = d[hero_end:a0]
    takeaway = ""
    am = re.search(r'<div class="answer[^"]*"[^>]*>\s*<p>(.*?)</p>', between, re.S)
    if am:
        txt = re.sub(r'^\s*<strong>In short:</strong>\s*', '', am.group(1))
        takeaway = ('<div class="answer reveal"><h2 style="margin-bottom:8px;font-size:1.05rem;text-transform:uppercase;'
                    'letter-spacing:.08em;color:var(--sage-deep)">Key takeaway</h2><p>' + txt + '</p></div>')
        between = between[:between.find('<div class="wrap-narrow"', 0) if '<div class="wrap-narrow"' in between else am.start()] \
                  if False else re.sub(r'(<!--[^>]*-->\s*)?<div class="wrap-narrow"[^>]*>\s*<div class="answer.*?</div>\s*</div>', '', between, count=1, flags=re.S)
    a1 = d.index("</article>", a0)
    inner = d[a0 + len('<article class="body">'):a1]
    om = re.match(r'\s*<div class="wrap-narrow[^"]*"[^>]*>', inner)
    if not om:
        return None
    inner = inner[om.end():]
    inner = inner[:inner.rstrip().rfind("</div>")]
    items = []
    def _id(mm):
        attrs, body = mm.group(1), mm.group(2)
        label = re.sub(r'<[^>]+>', '', body).strip()
        idm = re.search(r'id="([^"]+)"', attrs)
        if idm:
            i = idm.group(1)
        else:
            i = re.sub(r'[^a-z0-9]+', '-', label.lower()).strip('-')[:40].strip('-') or f"s{len(items)}"
            while any(i == x for x, _ in items):
                i += "-2"
            attrs += f' id="{i}"'
        items.append((i, label))
        return f'<h2{attrs}>{body}</h2>'
    inner = re.sub(r'<h2([^>]*)>(.*?)</h2>', _id, inner, flags=re.S)
    toc = ""
    if len(items) >= 3:
        toc = ('<nav class="toc" aria-label="On this page"><h2>On this page</h2><ul>'
               + "".join(f'<li><a href="#{i}">{l}</a></li>' for i, l in items) + '</ul></nav>')
    layout = ('<div class="wrap svc-layout" style="display:grid;grid-template-columns:1fr 340px;gap:clamp(32px,4vw,56px);'
              'align-items:start;padding-top:clamp(40px,5vw,64px);padding-bottom:clamp(40px,5vw,64px)">\n<div class="svc-body">\n'
              + takeaway + toc + inner + '\n</div>\n<aside style="position:sticky;top:24px">' + quiz_card() + '</aside>\n</div>')
    return d[:hero_end] + between + layout + d[a1 + len("</article>"):]

if __name__ == "__main__":
    done = skipped = 0
    for slug, img in PAGES.items():
        p = os.path.join(ROOT, slug, "index.html")
        if not os.path.exists(p):
            continue
        out = transform(open(p).read(), img)
        if out is None:
            skipped += 1; print("skip", slug); continue
        open(p, "w").write(out); done += 1
    print(f"svc layout applied: {done}, skipped: {skipped}")
