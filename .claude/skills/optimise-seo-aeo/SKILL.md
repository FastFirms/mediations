---
name: optimise-seo-aeo
description: >-
  Audit and optimise an existing page on the Mediations Australia website
  (mediationsaustralia.com.au) for SEO and AEO (answer-engine optimisation),
  applying the fixes through its Python build system. Use this skill whenever the
  user wants to improve, audit, optimise, or fix the SEO/AEO of a page; raise a
  keyword's ranking; tighten a title or meta description; fix an H1; add or complete
  JSON-LD schema; add an AEO "answer box"; improve internal linking; or asks "why
  isn't this page ranking" or "make this page rank better for X". Also use when given
  a target keyword and asked which page should win it, or when handed a rankings export.
  This skill knows the page-type → generator map, the meta/schema system, the rankings
  data, and the safe branch-and-preview deploy flow. Do NOT use it to write new blog
  posts (use write-mediations-blog) or to create brand-new pages.
---

# Optimise a Mediations Australia page for SEO & AEO

This skill takes one existing page (and a target keyword) and makes it rank and get
cited better — auditing it against on-page SEO and answer-engine standards, then applying
the fixes **through the page's Python generator**, validating, and pushing to a **branch**
for a Vercel preview. Never edit the built `*/index.html` files by hand and never push to
`main` (Vercel deploys `main` to the staging site).

Read `../../../CLAUDE.md` first if you have not this session — it is the source of truth for
brand, voice, and the non-negotiable rules R1–R8. This skill operationalises the SEO/AEO
parts; where they ever disagree, CLAUDE.md wins.

## The one rule that shapes everything: edit the generator, not the HTML

Every page on this site is **generated** by a Python script in `build/` that calls
`head(title, desc, slug, extra_schema=[...])` and assembles the body (with the H1, answer
box, sections, FAQ, schema). The committed `*/index.html` files are build output. If you
hand-edit the HTML, the next build silently overwrites it. So every fix in this skill is a
change to a generator's `title=`, `desc=`, H1 string, schema list, or body content,
followed by a rebuild.

The full build reproduces every committed page **byte-for-byte** (verified), so re-running
the one generator that owns your page changes only that page and leaves its siblings
identical. Two exceptions are guarded — see the never-run list in
`references/generator-map.md`.

**Which generator owns your page?** Look it up in `references/generator-map.md`. In short:
home + `family-law-mediation` → `gen_home.py`; the four core pages → `gen_core.py`; the 12
services → `gen_services.py` / `gen_services2.py`; the 21 locations → `gen_locations.py`
(+ `location_data.py`); resources → `gen_resources.py`; blog cornerstones → `gen_blog*.py`.

## What we are optimising for

**SEO** — winning the organic click: a keyword-first H1 (rule R1), a compelling title ≤60
chars and meta description ≤160 chars (rule R8) that earn the click, headings and body that
actually cover the query and its sub-questions, complete and valid JSON-LD, a clean
canonical, and strong internal links in (anchor text) and out.

**AEO** — getting quoted by ChatGPT, Perplexity, Google AI overviews and the like: a direct,
self-contained answer to the page's core question in the first sentence of a visible "answer
box", `FAQPage` schema with real questions people ask, and factual claims that are cited to
authority sources so an answer engine trusts and attributes the page.

The full audit checklist, with the specific thresholds and how to verify each item against
the rendered HTML, is in **`references/audit-checklist.md`**. Read it before auditing.

## Let the rankings drive the priority

The current keyword positions live at **`build/seo/rankings_2026-06-03.csv`**. This export is
from the **old live WordPress site**, so its `URL` column holds *old* URLs — map them to the
new slug for the same topic (e.g. old `/consent-orders-2025-update/` → new
`consent-orders-explained`). It tells you which keywords matter (volume), where the firm
already ranks (equity to protect at launch), and which pages are in "striking distance"
(positions ~4–20) where small on-page gains move the needle most. How to read it and pick a
target is in **`references/rankings.md`**.

When the user has not named a page, propose the highest-leverage target from the rankings
(high volume × striking distance × a page you can safely edit) and say why before editing.

## The workflow — follow in order

### 1. Get on a safe branch
Never work on `main`. From the repo root: `git switch -c seo/<slug>` (or reuse a working
branch). Confirm with `git branch --show-current` that you are not on `main`.

### 2. Identify the page, its generator, and the target keyword(s)
Resolve the slug → generator from `references/generator-map.md`. Confirm the primary keyword
(from the user or the rankings) and 1–3 secondary/related queries the page should also cover.

### 3. Audit
Open the **current built HTML** for the page (`<slug>/index.html`) and the generator that
produces it. Work through `references/audit-checklist.md`, recording concrete findings:
what the current title/desc/H1/schema/answer-box/internal-links are, which fail a threshold,
and the specific fix for each. Present this audit to the user as a short before→after table
before applying changes (these are real edits to a real site).

### 4. Apply the fixes in the generator
Edit the owning generator: tighten `title=` / `desc=` (respect 60/160 and keep brand voice),
make the H1 keyword-first if it is not, add or complete the answer box and `FAQPage` schema,
strengthen headings/body coverage, and improve internal links. Keep changes surgical and
on-brand — soft persuasion, never pressure (CLAUDE.md §2). For blog pages the body is a
`post()` call; see the `write-mediations-blog` skill's `post-api.md` for that API.

### 5. Build only the owning generator
From `build/`, run just the generator(s) that own the page (e.g. `python3 gen_services.py`).
The generators auto-detect the repo root as output. Then run any index/sitemap rebuild only
if the page's title or set of pages changed. Commands and the **never-run list** are in
`references/generator-map.md`.

### 6. Validate (must pass before going further)
- `git diff --stat` should show **only** the page(s) you intended to change (plus the
  generator). If a sibling page changed, something is wrong — investigate before continuing.
- Run the site-health one-liner (in `references/generator-map.md`): expect
  `H1:0 | schema:0 | broken:NONE`, all H1s unique, and the page count unchanged.
- If you touched a blog page, also run `python3 check_authority.py` → `ALL POSTS MEET STANDARD`.
- Sanity-check the new `<title>` and meta description char counts (≤60 / ≤160), and that the
  JSON-LD still parses (no stray quotes from the `cite()` trap — see the blog skill).

### 7. Commit, push, preview
Commit on the branch, push, and report the Vercel **preview URL** so the user can review the
optimised page live but private. The staging site updates only when the user merges to `main`.
Never force-push and never push to `main` without the user explicitly asking.

## Guarded cases (do not get surprised by these)
- **The homepage is deliberately `noindex, nofollow` on staging.** `gen_home.py` now preserves
  that on every build via a staging guard; do not undo it. Making the homepage indexable is a
  launch decision, not an SEO edit — see `references/generator-map.md`.
- **`gen_migration.py` is stale and destructive** (emits 33 of 245 redirects). Never run it;
  edit `redirects.htaccess` / `url-migration-map.csv` by hand (rule R7).
- **`gen_booking.py` is out of sync** with the hand-wired live booking page (Formspree action);
  do not run it.

## Reference files
- `references/audit-checklist.md` — the full SEO + AEO audit, thresholds, and how to verify
  each item against the rendered HTML. **Read before auditing.**
- `references/generator-map.md` — the slug → generator map, how each page type sets its
  title/desc/H1/schema, the byte-identical safety proof, the never-run list, the homepage
  noindex guard, the build commands, and the validation one-liner.
- `references/rankings.md` — how to read `build/seo/rankings_2026-06-03.csv` (old-site URLs,
  volume, positions, striking distance) and pick the highest-leverage target.
