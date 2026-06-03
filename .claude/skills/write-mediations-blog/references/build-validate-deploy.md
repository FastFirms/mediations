# Build, validate, and deploy a new post

All commands run from `build/` unless noted. The blog generators auto-detect the repo root
as their output directory (they write pages to `/<slug>/index.html` at the repo top level).
If you ever need to redirect output for a dry run, set `MED_SITE_OUT=/some/dir` in the
environment and the generators will write there instead.

## Build commands (blog-only — this is all you run for a new post)

```bash
cd build
python3 gen_blog_batchN.py     # N = the new batch file you created (writes the new post)
python3 gen_blog_index.py      # rebuilds /guides/ with the new card
python3 gen_meta.py            # rebuilds sitemap.xml + robots.txt with the new URL
```

That writes only: the new post page, `guides/index.html`, `sitemap.xml`, `robots.txt`.
(Importing `gen_blog` also rebuilds the 4 flagship posts — identical output, harmless.)

## ⚠️ The never-run list

These generators must **not** be run as part of blog work. They manage other pages and
running them would overwrite or damage production state:

- `gen_migration.py` — **STALE and destructive.** It emits only 33 of the 245 live redirect
  rules; running it deletes 212 redirects and breaks `url-migration-map.csv` (violates R7).
  Edit `redirects.htaccess` / `url-migration-map.csv` **by hand** instead.
- `gen_home.py` — the live homepage carries a deliberate `noindex, nofollow`; the generator
  would flip it to `index, follow`. Leave it to a separate, intentional decision.
- `gen_booking.py` — the live booking page differs from the generator (markup refactor).
- `gen_core.py`, `gen_services*.py`, `gen_locations.py`, `gen_resources.py`,
  `gen_missing_pages.py` — not blog files; out of scope for this skill.

If you think one of these genuinely needs running, stop and ask the user first.

## Validate (both must pass before committing)

```bash
python3 check_authority.py     # must end with: ALL POSTS MEET STANDARD
```

Then the site-health one-liner (run from the repo root, NOT build/):

```bash
cd ..
python3 - <<'PY'
import re, glob, os
root="."
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

Expect `H1:0 | schema:0 | broken:NONE`, all H1s unique, and the page count up by one from
the previous total (the repo baseline was **94 pages** when this skill was written — that is
the canonical 90 plus `books`, `memberships`, `mediation-podcast`, `our-mediators`).

If `broken` lists a slug, a `related`/internal link points at a page that does not exist —
fix the link or the slug. If `H1` or `schema` is non-zero, the new post is malformed.

## Choosing a topic from gaps (when the user did not specify)

1. Read `blog-content-manifest.csv` (repo root) — the planning inventory of topics.
2. The 42 published cornerstones are the `BLOG` list in `build/check_authority.py`.
3. `build/blog_inventory.py` holds ~201 legacy WordPress slugs (`SITEMAP1`/`SITEMAP2`) —
   evidence of what drew traffic on the old site.
4. Pick a high-intent, searchable topic **not already covered** by an existing cornerstone
   (e.g. a distinct question, not a near-duplicate of an existing guide). State your pick
   and the reasoning to the user before writing, so they can redirect if they prefer.

## Commit, push, and preview

```bash
# from repo root, on your blog/<slug> branch (never main)
git add <slug>/ guides/index.html sitemap.xml robots.txt \
        build/gen_blog_batchN.py build/gen_blog_index.py build/gen_meta.py build/check_authority.py
git commit -m "Add blog: <human title>"
git push -u origin blog/<slug>
```

Then surface the **Vercel preview URL** for the branch so the user can read the post live
but private. Production publishes only when the user merges `blog/<slug>` into `main`.

Never force-push, never push to `main` without the user explicitly asking, and never run the
never-run generators above.
