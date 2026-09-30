# SEO Change Log — Mediations Australia

## Deployment A — 2026-10-01

### P0 — Redirect Fixes

#### Perth keyword redirect
- **Files:** `vercel.json`, `redirects.htaccess`
- **Change:** Added redirects for the correctly-spelled (previously uncovered) URL `/perth-family-law-mediation/` → `/perth-mediation/` (permanent 301). Also covers no-trailing-slash variant in vercel.json.
- **Reason:** The typo variant `/perth-family-law-medi*tion*/` was already covered; the correct spelling was not, causing a 404 for any inbound links using the correct URL.

#### Redirect chain elimination
- **Files:** `vercel.json`, `redirects.htaccess`
- **Three chains fixed:**
  - `/accredited-family-law-mediators/` → was → `/our-mediators/` → `/our-team/` — now direct to `/our-team/`
  - `/family-law-practitioners/` → was → `/our-mediators/` → `/our-team/` — now direct to `/our-team/`
  - `/team-single/` → was → `/our-mediators/` → `/our-team/` — now direct to `/our-team/`
- **Kept intact:** `/our-mediators/` → `/our-team/` redirect (not removed — still needed for inbound links)
- **Reason:** Redirect chains dilute link equity and slow page resolution. Each hop was a wasted 301.

### P1 — Metadata Fix

#### /conflict-resolution-in-the-workplace/ title and description
- **File:** `build/gen_imported_posts.py` (META_OVERRIDES dict)
- **Before title:** `Conflict Resolution in the Workplace | Strategies That…` (truncated, from original import)
- **After title:** `Conflict Resolution in the Workplace | Strategy & Mediation`
- **Before desc:** Original imported description (unverified "$6–12 billion" claim)
- **After desc:** `Workplace conflict can be costly. Learn practical resolution strategies, key considerations for Australian workplaces, and when mediation may help.`
- **Reason:** Title was a truncation artefact from the import pipeline. Description contained an unverified statistic. Both were non-competitive.
- **Note:** `$6–12 billion` claim deliberately excluded — not verified.

---

## Sprint 1 Audit — 2026-10-01

Full technical audit findings documented in `seo/technical-recovery-audit.md`.
