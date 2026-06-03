# Page → generator map, build, and safety

Every page is build output. To change a page's SEO, edit the generator that owns it, then
rebuild only that generator. All generators auto-detect the repo root as their output
directory (`OUT = os.environ.get("MED_SITE_OUT") or <repo root>`), so running them from
`build/` writes to the live `<slug>/index.html` files. Set `MED_SITE_OUT=/tmp/dryrun` to
build to a throwaway dir first if you want to diff before touching the repo.

## The map

| Page(s) | Slug(s) | Generator | Notes |
|---|---|---|---|
| Homepage | `` (root) | `gen_home.py` | **Guarded: stays `noindex` on staging.** See below. |
| Family Law Mediation | `family-law-mediation` | `gen_home.py` | built alongside the homepage |
| Core pages | `how-mediation-works`, `about-mediations-australia`, `preparing-for-mediation`, `contact-us` | `gen_core.py` | |
| Services (most) | the 12 service slugs in `SERVICES` (templates.py) | `gen_services.py` | uses `build(slug,title,desc,eyebrow,h1,lede,ans,blocks,qa,crumb,cta_h,cta_p)` |
| Services (extra + fees) | the additional service/fee slugs | `gen_services2.py` | same `build(...)` shape |
| Locations | the 21 `*-mediation` city slugs in `LOCATIONS` | `gen_locations.py` | per-city data in `location_data.py`; emits a per-city `LegalService` |
| Resources | the 5 resource/guide slugs | `gen_resources.py` | `build(...)` with `is_article` |
| Booking | `book-a-consultation` | `gen_booking.py` | **NEVER RUN — out of sync** (see below) |
| Blog cornerstones | the ~43 slugs in `check_authority.py` `BLOG` | `gen_blog.py`, `gen_blog_batch2..10.py` | author via `post()`; see the write-mediations-blog skill |
| Guides index | `guides` | `gen_blog_index.py` | rebuild only if a blog title/card changes |
| sitemap + robots | — | `gen_meta.py` | rebuild only if the set of URLs changes |

To find which generator literally writes a slug, grep for it:
```bash
cd build && grep -rln "\"<slug>\"\|'<slug>'" gen_*.py location_data.py
```

## How each page type sets its SEO fields
- **head(title, desc, slug, extra_schema=[...])** (in `templates.py`) emits `<title>`, the
  meta description, the canonical, the robots tag (`index, follow, max-image-preview:large`),
  Open Graph + Twitter tags (derived from title/desc), and the JSON-LD `@graph` from
  `extra_schema`. So **title and description are fixed by the `title=`/`desc=` arguments** to
  the generator's build call, and **schema by the `extra_schema=[...]` list**.
- **H1** is a string inside the generator's body assembly (the `h1` argument to `build(...)`
  / `post(...)`, or an inline `<h1>` in `gen_home.py` / `gen_core.py`).
- **Answer box:** services use `answer("In short: …")`; blogs use `key_takeaway("…")`.
- **FAQ:** the `qa` list of `(question, answer)` tuples drives both `faq_html()` (visible)
  and `faq_schema()` (`FAQPage` JSON-LD) — edit the tuples and both update in parity.
- **Schema builders** available: `org_schema()`, `service_schema(name,desc,slug)`,
  `article_schema(headline,desc)`, `faq_schema(qa)`, `breadcrumb_schema(trail)`, and the
  per-city `localservice_schema()` in `gen_locations.py`.

## Safety: the full build reproduces every page byte-for-byte
This was verified: running every generator into the repo leaves `git status` clean for all
HTML **except** the booking page (intentionally hand-edited). That means re-running the one
generator that owns your page only changes that page — siblings regenerate identically. After
any build, `git diff --stat` must show only the page(s) you meant to change. If a sibling
shows up, stop and investigate before committing.

## Build commands
From `build/`, run only what you need:
```bash
python3 gen_services.py        # or gen_services2 / gen_core / gen_locations / gen_resources / gen_home
python3 gen_blog_batchN.py     # for a blog page (also rebuilds the 4 flagships, identical output)
python3 gen_blog_index.py      # only if a blog card/title changed
python3 gen_meta.py            # only if the set of URLs changed
```

## ⚠️ The never-run list
- **`gen_migration.py`** — STALE and destructive: emits only 33 of 245 live redirect rules;
  running it deletes 212 redirects and breaks `url-migration-map.csv` (violates R7). Edit
  `redirects.htaccess` / `url-migration-map.csv` **by hand**.
- **`gen_booking.py`** — the live booking page was hand-wired (Formspree action
  `formspree.io/f/mredjobj`, a refactored `book-grid` class). The generator emits the
  pre-wiring version and would revert the live form. Do not run it; edit the booking page's
  SEO by hand if ever needed, then re-test the form.
- **`gen_missing_pages.py`, `gen_services_v2/v3/v4.py`** — superseded scratch generators; not
  the source of any live page. Ignore them.

## The homepage noindex guard
The staging homepage is deliberately `noindex, nofollow` (kept out of search until launch).
`head()` always emits `index, follow`, so `gen_home.py` now **forces the homepage back to
`noindex, nofollow` on every build** via `HOMEPAGE_NOINDEX` (set from the env var
`MED_HOMEPAGE_INDEX`). This makes `gen_home.py` safe to re-run for SEO edits — the homepage's
title/desc/H1/schema/body all rebuild normally while the noindex is preserved.

- To optimise the homepage: edit `gen_home.py`, run `python3 gen_home.py`, and confirm the
  built `index.html` still shows `noindex, nofollow`. `family-law-mediation` rebuilds normally
  (it is and stays indexable).
- **At launch only**, when the homepage should be indexable on the production domain, build
  with `MED_HOMEPAGE_INDEX=1 python3 gen_home.py` (or set `HOMEPAGE_NOINDEX=False`). That is a
  deliberate launch decision — never flip it as part of a routine SEO edit.

## Validation one-liner (run from the repo root, not build/)
```bash
cd ..
python3 - <<'PY'
import re, glob, os
pages = sorted(glob.glob('*/index.html')) + ['index.html']
built = {d for d in os.listdir('.') if os.path.isdir(d) and not d.startswith('.') and d!='build'}
built.add('')
h1bad = ld = 0; links=set()
for p in pages:
    s=open(p).read()
    if s.count('<h1')!=1: h1bad+=1
    if s.count('application/ld+json')!=1: ld+=1
    for m in re.findall(r'href="/([a-z0-9-]+)/"', s): links.add(m)
broken=[l for l in links if l not in built]
h1s=[re.sub(r'\s+',' ', re.sub(r'<[^>]+>','', re.search(r'<h1[^>]*>(.*?)</h1>', open(p).read(), re.S).group(1))).strip() for p in pages]
print(f'{len(pages)} pages | H1:{h1bad} | schema:{ld} | uniqueH1:{len(set(h1s))}/{len(h1s)} | broken:{broken or "NONE"}')
PY
```
Expect `H1:0 | schema:0 | broken:NONE`, all H1s unique, and the page count **unchanged** (an
SEO edit must not add or remove pages — the baseline is 94). If you touched a blog page, also
run `python3 check_authority.py` → `ALL POSTS MEET STANDARD`.

## Quick char-count check for title/description (rule R8)
```bash
python3 - <<'PY'
import re
s=open('<slug>/index.html').read()
t=re.search(r'<title>(.*?)</title>', s).group(1)
d=re.search(r'<meta name="description" content="(.*?)">', s).group(1)
print(f'title {len(t)}/60: {t}')
print(f'desc  {len(d)}/160: {d}')
PY
```
