# SEO/AEO Handoff — for the Claude Code session building this site

**Date:** 2026-07-04
**Purpose:** Everything the build session needs to make this rebuild launch-ready for SEO/AEO. Self-contained — read this first, then execute Part A (in-repo tasks) and honour Part B (strategy) as you build.

A fuller strategy report sits one level up (outside this repo) if you want the full audit reasoning:
`../mediations-australia-newsite-strategy.md`.

---

## Context in one paragraph

This repo is the **rebuild**. It is **not yet deployed** — the live `mediationsaustralia.com.au` is still the old WordPress site. A full six-dimension SEO/AEO audit + a 533-keyword rank analysis was run. Good news: the rebuild already passes almost every structural gate the live site fails (single keyword-first H1s, unique H1s/titles, valid schema incl. LegalService/LocalBusiness on all 21 location pages, breadcrumbs, OG/Twitter, `en-AU`, zero broken internal links, answer boxes on all content pages, booking links everywhere, alt text everywhere). The remaining work is one systematic fix (meta lengths) plus honouring the launch/migration strategy in Part B.

---

## Part A — Concrete in-repo tasks

### A1. Finish the meta-length fixes (R8) — ✅ DONE (2026-07-06: gate passes, 0 violations)

A build gate now enforces this: **`build/check_meta_lengths.py`** (titles ≤60, descriptions ≤160).

- ✅ **Location pages already fixed** — `gen_locations.py` template was shortened (dropped the duplicated city in the title; removed "Free consultation." from the description). All 21 location pages pass.
- ⏳ **~81 violations remain** on individually-authored service/guide/blog/core pages (~24 titles >60, ~57 descriptions >160). Most are marginal (titles 61–69, descriptions 161–200).

**Do this:**
```bash
cd build && python3 check_meta_lengths.py        # prints every failing page + its current length
```
For each flagged page, edit the `title=` / `desc=` string **in its generator** (not the built HTML — it's regenerated):
- Which generator sets them → `gen_core.py`, `gen_services.py` / `gen_services2.py` / `gen_services_v*.py`, `gen_resources.py`, `gen_blog*.py`, `gen_home.py`, `gen_booking.py`. All flow through `templates.head(title, desc, slug, ...)` in `templates.py`.
- **Trim, don't gut.** Keep keyword-first (R1) and meaning. The overage is usually trailing filler — drop `" (2026)"`, `" Complete 2026 guide."`, `" Free consultation."`, `" Step by step."`, `" Call 1800 952 380."` (on non-conversion pages), or tighten one clause.
- Titles: consider dropping the ` | Mediations Australia` / brand suffix on long ones, or a redundant word.

Then rebuild and re-check until clean:
```bash
# full rebuild per README/CLAUDE.md section 5, then:
python3 build/check_meta_lengths.py      # must end: "ALL PAGES MEET META STANDARD"
python3 build/check_authority.py         # must end: "ALL POSTS MEET STANDARD"
```

### A2. Wire both gates into the build

Add `check_meta_lengths.py` next to `check_authority.py` in the build script / CI so neither can regress. A build that fails either gate should not ship.

### A3. Keep these validators in mind (nice-to-have, not blocking)

- A location-page **body-text similarity** check (the current validator checks H1/schema uniqueness but not prose) — guards the 21 location pages against doorway-page duplication as they grow.
- A **contextual-internal-link** check — every blog cornerstone should link in-body to ≥1 service pillar + `/book-a-consultation/`.

---

## Part B — Strategy the build must honour (from the audit)

### B1. Migration & cutover is the highest-risk moment — do NOT skip
The live WordPress site is **~337 URLs** (incl. TWO overlapping location clusters: `/[city]-mediation/` **and** `/[city]-family-lawyers/`). This rebuild is ~104 pages and **renames some top-ranking pages** (e.g. live `/costs-of-mediation/` [ranks for 14 kw] → `/how-much-does-mediation-cost/`; live `/what-is-child-custody-mediation/` [18 kw] → `/child-custody-mediation/`).
- **Every live URL that ranks needs a 301** in `redirects.htaccess`. The existing 218-entry map was built against a different corpus — **reconcile it against the live sitemaps + Google Search Console "Pages" report before cutover.** Do not deploy until every live URL maps to a new page or an explicit 301.
- Consolidate the live site's dual `[city]-family-lawyers` cluster into the `[city]-mediation` pages via 301 (don't recreate two clusters).
- Keep the old sitemap live-but-redirecting through a transition window.

### B2. One canonical owner per head term (fixes the cannibalization the live site suffers)
The live site's head terms ("family law mediation", "mediators", "[city] mediation") underperform because the homepage, `/family-law-mediation/`, an orphan `/mediation/` page, and every city page all target the same terms. In this rebuild, enforce:
- **Homepage** = brand/hub. Keyword-first H1, but do **not** re-explain "family law mediation" in depth — link to the pillar.
- **`/family-law-mediation/`** = the single deepest page for that term; the city pages link **up** to it.
- **`/[city]-mediation/`** = local pages (they already have LegalService/LocalBusiness schema — good). Keep local blurbs short and link up to the national service pages rather than duplicating them.
- Do not resurrect a standalone `/mediation/` page competing for the bare term.
- Give **workplace/commercial** mediation its own hub (the ~30% business audience), not just a subsection of family pages.

### B3. Internal linking = hub-and-spoke
The winning informational cornerstones (e.g. `/application-for-divorce/`, `/what-is-mediation-in-family-law/`) should link **up** to the relevant service pillar + `/book-a-consultation/` with descriptive anchors. Homepage should feature the pillar + the 4 office cities prominently rather than all 21 cities as flat peers.

### B4. Launch-blockers (YMYL trust) — verify before deploy
- **`/domestic-violence-and-family-law/`** must surface **000 and 1800RESPECT** prominently and be linked from every family/parenting/location page (footer + inline disclaimer), per R6. (It exists in the repo — confirm the safety content is prominent, not buried.)
- **`/our-mediators/`** must show real, named, credentialed mediators (AMDRAS accreditation + register link; note who is also a lawyer). Confirm it isn't a stub — the live site's version repeats one bio 4×.
- **Replace any placeholder authors** with real credentialed `Person` bylines linked to `/our-mediators/`.

### B5. Protect the winners
The informational long-tail already ranks (#1s). **Do not restructure those pages** — only add an author/reviewer byline. Put the largest content effort into the **commercial/service pages** (that's where rankings lag): add named-mediator credibility, a cost/timeline table, a mediation-vs-litigation comparison, and question-form H2s with 40–60-word answer blocks.

### B6. Facts to verify before launch (do not ship placeholders)
The "90% success rate" (verify or soften + date it), AMDRAS accreditation numbers, the 4 office addresses + geo-coords (for LocalBusiness schema), mediator credentials, and phone-number/NAP consistency.

### B7. AEO
`gen_llms.py` exists — confirm `/llms.txt` ships and lists the key pages. Confirm robots.txt keeps the explicit AI-crawler allowlist. Keep the "Key takeaway" answer boxes to a 40–60-word self-contained lead answer.

---

## Current pass/fail snapshot (this repo, 104 pages)

| Check | Status |
|---|---|
| Single keyword-first H1 / unique H1s & titles | pass (0 dupes) |
| Canonical / JSON-LD present & valid / OG / Twitter / en-AU | pass |
| Broken internal links | 0 |
| Location pages: LegalService/LocalBusiness + Breadcrumb | all 21 |
| Answer boxes on content pages | 96/104 (rest are non-content) |
| Authority citations (`check_authority.py`) | governs — keep passing |
| **Meta lengths (`check_meta_lengths.py`)** | ✅ pass — 0 violations (fixed 2026-07-06) |
