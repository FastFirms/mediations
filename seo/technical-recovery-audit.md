# Technical Recovery Audit — Mediations Australia

**Audit date:** 2026-10-01  
**Context:** Site traffic dropped 59% (May 2026: 4,979 sessions → Sep 2026: 2,024 sessions). Sprint 1 audit run to identify technical friction. Deployment A implements confirmed P0/P1 fixes only.

---

## Sprint 1 Findings Summary

### Phase A — Canonical & Domain

| Item | Status | Notes |
|---|---|---|
| Canonical domain redirect (non-www → www) | **PASS** | 308 permanent, verified in Vercel dashboard |
| HTTPS enforcement | PASS | Vercel handles |
| Sitemap hostname | PASS | `www.mediationsaustralia.com.au` |

### Phase B — Redirect Audit

| Item | Status | Action |
|---|---|---|
| `/perth-family-law-mediation/` → 404 | **FIXED (Dep A)** | Added → `/perth-mediation/` in vercel.json + htaccess |
| `/accredited-family-law-mediators/` chains through `/our-mediators/` | **FIXED (Dep A)** | Now direct to `/our-team/` |
| `/family-law-practitioners/` chains through `/our-mediators/` | **FIXED (Dep A)** | Now direct to `/our-team/` |
| `/team-single/` chains through `/our-mediators/` | **FIXED (Dep A)** | Now direct to `/our-team/` |
| Perth typo `/perth-family-law-medi*tion*/` | PASS | Already covered |
| Duplicate redirect entries (minor) | LOW | Not actioned in Dep A |

### Phase C — Metadata Audit

| Page | Item | Status | Action |
|---|---|---|---|
| `/conflict-resolution-in-the-workplace/` | Title truncation artefact | **FIXED (Dep A)** | New title via META_OVERRIDES |
| `/conflict-resolution-in-the-workplace/` | Description with unverified claim | **FIXED (Dep A)** | Clean desc, no $6–12B claim |
| `/workplace-mediation/` | Title / H1 | NOT ACTIONED | Held — not in Dep A scope |

### Phase D — Schema Audit

| Item | Status | Notes |
|---|---|---|
| FAQPage schema on conflict-resolution | HELD | Not approved for Dep A |
| Organisation schema | PASS | Present sitewide |
| BreadcrumbList | PASS | Present on all generated pages |

### Phase E — IntersectionObserver `.reveal` Pattern

**REPORT ONLY — no changes made**

- The site uses an IntersectionObserver pattern with `.reveal` class for scroll-triggered fade-in
- **Risk identified:** If primary page content (H1, lede, above-fold sections) carries `.reveal`, Googlebot may not render it — Googlebot does not scroll and WRS (Web Rendering Service) may not fire the observer
- **Verified:** Homepage hero and above-fold lede elements do NOT appear to carry `.reveal` in the initial HTML — the class is applied to lower-section elements
- **Recommendation:** Audit all generator templates to confirm `.reveal` is never added to H1, answer box, or first body section. Treat this as a standing guardrail.
- **Status:** Monitoring only. No page-level content changes made.

### Phase F — Vercel Alias Audit (mediations-seven.vercel.app)

**REPORT ONLY — no changes made**

- `mediations-seven.vercel.app` is the Vercel preview/staging alias
- It carries the site-wide `X-Robots-Tag: noindex, nofollow` header set in vercel.json `headers` block — this is the intentional staging noindex
- Internal pages checked: same header present on all paths
- No sitemap exposed at `/sitemap.xml` on this alias (expected — staging)
- **Verdict:** Alias behaves correctly. No leak risk.

### Phase G — Traffic Drop Root Cause Hypotheses

Based on audit findings, probable contributing factors to the 59% traffic drop:

1. **AI Overview cannibalisation** — High-volume informational queries (best co-parenting apps, separation expenses, divorce papers) lost impressions to Google AI Overviews. These pages rank but generate fewer clicks.
2. **Redirect chains** — Three chains diluting equity on team/mediator pages (fixed Dep A)
3. **Missing Perth redirect** — Any inbound links to correct `/perth-family-law-mediation/` were 404ing (fixed Dep A)
4. **Import page metadata quality** — Truncated titles and unverified claims reducing CTR on imported posts

---

## Deployment A — Changes Made (2026-10-01)

| File | Change |
|---|---|
| `vercel.json` | Added `/perth-family-law-mediation/` + no-slash variant → `/perth-mediation/`; fixed 3 chain destinations to `/our-team/` |
| `redirects.htaccess` | Fixed `/team-single/`, `/accredited-family-law-mediators/`, `/family-law-practitioners/` to → `/our-team/`; added `/perth-family-law-mediation/` → `/perth-mediation/` |
| `build/gen_imported_posts.py` | Added `conflict-resolution-in-the-workplace` to META_OVERRIDES with clean title + desc |
| `conflict-resolution-in-the-workplace/index.html` | Rebuilt output (via generator) |

**Status:** Local only. Not deployed. Awaiting operator authorisation.

---

## Next — Deployment B (HOLD)

Not actioned. Awaiting operator review of Deployment A results and explicit authorisation.
