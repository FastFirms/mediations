# `build/` — Site Generators

This folder builds the Mediations Australia static site from Python templates.
No build script writes `styles.css` — that's hand-maintained in `site/styles.css`.

---

## Quick start

```bash
# Run a full rebuild (output goes to ../site/)
python3 gen_home.py
python3 gen_core.py
python3 gen_services.py          # initial thin service pages (overwritten by v2-v4)
python3 gen_services2.py
python3 gen_services_v2.py       # 3 flagship cornerstone services
python3 gen_services_v3.py       # 5 more cornerstone services
python3 gen_services_v4.py       # 9 more cornerstone services
python3 gen_locations.py
python3 gen_resources.py
python3 gen_booking.py
python3 gen_blog.py              # 4 flagship blog posts
python3 gen_blog_batch2.py       # batches 2-9 = 38 more posts
python3 gen_blog_batch3.py
python3 gen_blog_batch4.py
python3 gen_blog_batch5.py
python3 gen_blog_batch6.py
python3 gen_blog_batch7.py
python3 gen_blog_batch8.py
python3 gen_blog_batch9.py
python3 gen_blog_index.py        # /guides/ index page
python3 gen_missing_pages.py     # 4 placeholder pages
python3 gen_meta.py              # sitemap.xml + robots.txt
python3 gen_migration.py         # 301 redirect map

# Then validate
python3 check_authority.py        # must end "ALL POSTS MEET STANDARD"
```

The one-liner validator (run from `site/`, not `build/`):

```bash
cd ../site && python3 -c "
import re,glob,os
pages=sorted(glob.glob('*/index.html'))+['index.html']
built={d for d in os.listdir('.') if os.path.isdir(d)};built.add('')
h1bad=ld=0;links=set()
for p in pages:
    s=open(p).read()
    if s.count('<h1')!=1:h1bad+=1
    if s.count('application/ld+json')<1:ld+=1
    for m in re.findall(r'href=\"/([a-z0-9-]+)/\"',s):links.add(m)
broken=[l for l in links if l not in built]
print(f'{len(pages)} pages | H1:{h1bad} | schema:{ld} | broken:{broken or \"NONE\"}')
"
# Healthy output: "95 pages | H1:0 | schema:0 | broken:NONE"
```

---

## What each file does

### Shared building blocks

| File | Purpose |
|---|---|
| `templates.py` | Shared head/meta/JSON-LD, nav (megamenu), footer, helper functions. **Most-imported file.** Edit cautiously — every page depends on it. |
| `authority_sources.py` | Curated `.gov.au` / `.edu` / peak-body citation sources. Use `cite("key")` to insert one. Min-2-links-per-blog rule enforced via `check_authority.py`. |
| `slugmap_data.py` | The 220+ entry old-URL → new-URL mapping used by `gen_migration.py`. |
| `blog_inventory.py` | List of 211 legacy blog URLs and their consolidation/redirect target. |
| `location_data.py` | Per-location data (court registries, suburb lists, etc.) used by `gen_locations.py`. |

### Page generators (each writes one or more pages into `../site/`)

| File | Output |
|---|---|
| `gen_home.py` | `/` (homepage) + early variant of `/family-law-mediation/` |
| `gen_core.py` | about, contact, fee-structure, how-mediation-works, preparing-for-mediation |
| `gen_services.py` + `gen_services2.py` | **Initial thin** 18 service pages. Overwritten by v2/v3/v4 below. |
| `gen_services_v2.py` | **Cornerstone-depth** rebuilds of `family-law-mediation`, `property-settlement-mediation`, `child-custody-mediation`. Also defines shared component helpers (`inline_cta`, `key_takeaway`, `callout`, `toc`, `related_grid`, `service_page`) imported by v3 and v4. |
| `gen_services_v3.py` | Cornerstone rebuilds: parenting-plan, consent-orders, financial-agreements, section-60i, workplace, online-divorce |
| `gen_services_v4.py` | Cornerstone rebuilds: spousal-support, child-support, de-facto, grandparents, arbitration, estate-dispute, accredited-mediators, collaborative-lawyers, divorce-counselling |
| `gen_locations.py` | 21 deep location pages (~1,850 words each) |
| `gen_resources.py` | 6 resource pages (preparing-for-mediation, cost-estimator, etc.) |
| `gen_booking.py` | `/book-a-consultation/` — Formspree-wired form |
| `gen_blog.py` | 4 flagship blog cornerstones |
| `gen_blog_batch2.py` … `gen_blog_batch9.py` | 38 more blog cornerstones (42 total) |
| `gen_blog_index.py` | `/guides/` index page listing all blog posts |
| `gen_missing_pages.py` | 4 placeholder pages (our-mediators, memberships, podcast, books) |
| `gen_meta.py` | `sitemap.xml` + `robots.txt` |
| `gen_migration.py` | `redirects.htaccess` (220+ x 301s) + `url-migration-map.csv` |

### Validation

| File | Purpose |
|---|---|
| `check_authority.py` | Walks every blog post, confirms each has ≥2 external links to authoritative sources. **Must pass before deploy.** |

### Historical (in `_archive/`)

One-shot patches we applied during the rebuild. Already executed — kept for audit
trail and as reference for similar future fixes. Don't re-run unless you understand
why each one was needed. See `_archive/README.md`.

---

## Non-negotiable rules (carried over from CLAUDE.md)

When writing new content via these generators:

1. **H1s must be keyword-first.** "Family Law Mediation — *resolve it without court*" ✓.  Generic openers like "Welcome to..." ✗.
2. **Blog posts must have ≥2 authority external citations.** Use `cite("key")` from `authority_sources.py`. Enforced by `check_authority.py`.
3. **Blog depth ≥1,000 words**, with TOC, key takeaway, FAQ schema, 6+ inline CTAs, related grid.
4. **Use `BOOK_URL` constant from `templates.py`** for every booking CTA — never hardcode the URL.
5. **Children/safety content rules**: include emergency contacts (000, 1800RESPECT) where the topic warrants; never name self-harm methods.
6. **Migration map is a safety net.** When you change a URL, add the old → new mapping to `slugmap_data.py` and rerun `gen_migration.py`.
7. **Meta titles ≤60 chars, descriptions ≤160 chars**, all unique site-wide. OG and Twitter must mirror.

---

## Brand palette (defined in `../site/styles.css`)

```
--sand:#f4efe6      warm sand background
--sand-deep:#ebe3d4 darker sand for soft section bands
--cream:#fbf8f2     card and surface fill
--ink:#23291f       primary text
--ink-soft:#4a5043  secondary text
--sage:#5a7159      brand accent
--sage-deep:#3f5340 strong sage for emphasis bands
--sage-light:#dfe6d8 soft sage for callouts
--cta:#FF6B43       primary CTA colour (coral) — used to be called --teal
--cta-deep:#E85A35  CTA hover state
--err:#c0392b       form validation errors only
--warn:#b07000      placeholder warning boxes only
--terra:#c66a3f     legacy — defined but unused
--line:rgba(35,41,31,.12)  hairline borders
```

---

## Adding a new blog post — the workflow

The cleanest pattern is to add a new entry to one of the existing `gen_blog_batch*.py`
files (whichever has thematically related content), following the existing structure:

```python
# Inside gen_blog_batch9.py or similar:
blog_post(
    slug="your-new-post-slug",
    title="Your Post Title | Mediations Australia",
    desc="Meta description, ≤160 chars, unique site-wide.",
    h1="Your Keyword-First H1 — emotive subordinate clause.",
    lede="Opening paragraph, sets up the answer to the search query.",
    takeaway="One-paragraph direct answer (AEO).",
    toc=[("anchor","Section title"), ...],
    body="""<h2 id="anchor">Section heading</h2>
            <p>Substantive content with """ + cite("ag_fdr") + """ citations woven in...</p>
            """ + inline_cta("Punchy CTA copy") + """
            ...""",
    faq=[("Question?","Answer."), ...],
    related=[("slug","Title"), ...],
)
```

Then:

1. Run `python3 gen_blog_batch9.py` (or whichever batch).
2. Run `python3 gen_blog_index.py` to update `/guides/`.
3. Run `python3 gen_meta.py` to update `sitemap.xml`.
4. Run `python3 check_authority.py` — must say "ALL POSTS MEET STANDARD".
5. Run the validation one-liner — must say "broken:NONE".

If you've changed an existing URL, also:

6. Add the old → new entry to `slugmap_data.py`.
7. Run `python3 gen_migration.py` to rebuild the redirects file.
