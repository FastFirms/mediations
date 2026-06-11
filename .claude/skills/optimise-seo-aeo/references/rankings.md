# Reading the rankings export & picking a target

The keyword positions live at **`build/seo/rankings_2026-06-03.csv`**. Refresh it by dropping
a newer export in `build/seo/` and pointing the skill at the new filename.

## File shape (mind the banner line)
- **Line 1 is a banner** (`"Google Australia (Melbourne, Victoria, Australia)…"`) — skip it.
- **Line 2 is the header:** `Keyword, URL, Tags, "Search vol.", <date1>, <date2>, … <dateN>`.
- Each later date column is the page's **position** for that keyword on that day; the **last
  date column is the most recent** position. A blank/non-numeric cell means **not ranking** in
  the tracked set (treat as unranked).
- `Tags` = `Focus` marks the firm's priority keywords. `Search vol.` is monthly AU volume.
- **Rows can repeat a keyword** with different URLs/positions — the same query ranking via
  different pages. When summarising, keep the best (lowest-number) position per keyword.

Robust parse (skips the banner, handles ragged/blank cells):
```python
import csv
lines=open('build/seo/rankings_2026-06-03.csv',encoding='utf-8-sig').read().splitlines()
rows=list(csv.DictReader(lines[1:]))
LATEST='2026-06-03'   # = the last date column header
def pos(r):
    v=(r.get(LATEST) or '').strip(); return int(v) if v.isdigit() else 999
def vol(r):
    v=(r.get('Search vol.') or '').strip().replace(',',''); return int(v) if v.isdigit() else 0
```

## The URLs are OLD-site URLs — map them to new slugs
This export is from the **current live WordPress site**, which is the *old* site. Its `URL`
column therefore holds old URLs that often differ from the new static-site slugs. Map by
topic before acting, e.g.:
- old `/consent-orders-2025-update/` → new `consent-orders-explained`
- old `/separated-under-one-roof/` → new `separation-under-one-roof`
- old `/family-mediation-process-guide/` → the new mediation hub / `how-mediation-works`

Check `redirects.htaccess` and `url-migration-map.csv` for the authoritative old→new mapping,
or grep the new slugs with the per-topic words. The point: the rankings tell you the **topic's
demand and current standing**; you optimise the **new** page that will own that topic at launch.

## How to prioritise (highest leverage first)
Score candidates by **volume × winnability × your ability to safely edit the page**:
1. **Striking distance (positions ~4–20)** on a **high-volume** keyword — small on-page gains
   here move ranking and traffic the most. This is the sweet spot.
2. **`Focus`-tagged** keywords — the firm's stated priorities; weight them up.
3. **Page-1 but not top-3 (4–10)** — tighten title/answer-box/internal links to climb.
4. **High-volume topics where the new site has a strong page but the old URL ranks mid-page**
   — protect and grow that equity for launch.
5. Deprioritise: already top-3 (little upside), or huge head terms where the homepage is the
   only natural target (the homepage is `noindex` on staging — optimise it for launch readiness,
   but it cannot demonstrate ranking movement on a preview).

Top opportunities visible in the 2026-06-03 export (best row per keyword):

| Vol | Pos | Tag | Keyword | New page to optimise |
|---|---|---|---|---|
| 14,800 | 18 | Focus | Mediators | homepage (guarded noindex — launch target) |
| 9,900 | 16 | | Mediation | homepage / mediation hub |
| 2,400 | 16 | | Consent Orders | `consent-orders-explained` |
| 1,600 | 4 | | separated under one roof | `separation-under-one-roof` |
| 1,300 | 12 | | consent order | `consent-orders-explained` |

When the user has not named a page, propose the best target from a fresh read of the file
(volumes and positions shift), explain the reasoning, and confirm before editing. For a clean
demonstration prefer a striking-distance content/service page you can fully edit and that the
preview can show indexable; reserve the homepage for an explicit launch-readiness pass because
of its noindex guard.
