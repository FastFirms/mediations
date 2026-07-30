# SEO & AEO audit checklist

Work through this against **two things at once**: the current built page
(`<slug>/index.html`) to see what is shipping, and the generator that produces it (to see
where each value comes from, so you fix the source, not the output). Record a concrete
finding and a specific fix for every item. Present a before→after summary to the user before
applying changes.

Each page already passes the structural baseline (one keyword-first H1, unique title/desc,
canonical, OG/Twitter, JSON-LD `@graph`) because `head()` emits it — so this audit is about
*quality and coverage*, not whether the tags exist.

## A. The title tag — earns the click (≤60 chars, rule R8)
The single biggest CTR lever. Check the built `<title>`.
- **Length:** ≤60 chars or Google truncates. Count the rendered characters.
- **Keyword-first:** the primary keyword should appear at or near the front, naturally.
- **Distinct + compelling:** says what the page is and gives a reason to click (specific,
  Australian, trustworthy). Avoid keyword-stuffing and avoid pure brand-first.
- **Brand suffix:** the site uses ` | …` suffixes on some pages; keep the keyword ahead of it.
- Fix in the generator's `title=` argument. The matching OG/Twitter titles regenerate from it.

## B. The meta description — supports the click (≤160 chars, rule R8)
Not a ranking factor, but a major CTR factor and often the snippet an answer engine shows.
- **Length:** ≤160 chars (count rendered chars, entities like `&amp;` count as shown).
- **Includes the primary keyword** and a secondary query if it fits naturally.
- **Has a soft, specific value proposition and an implicit CTA** — on-brand (calm, no
  pressure, no "act now"). One clear sentence usually beats two vague ones.
- Fix in the generator's `desc=` argument (OG/Twitter descriptions regenerate from it).

## C. The H1 — keyword-first (rule R1, non-negotiable)
Exactly one `<h1>`, and it **starts with the keyword**, not brand language.
- Right: *"Melbourne Mediation — resolve disputes without court"*.
- Wrong: *"Resolve disputes without court in Melbourne"* / *"Welcome to …"*.
- The house pattern italicises the emotional/wedge half with `<em>` — keep it.
- The homepage is the one place a brand-positioning H1 may be defensible; if it is not
  keyword-first, **flag it and recommend** options rather than silently rewriting a signature
  brand line — let the user choose. Elsewhere, fix it.

## D. Heading & content coverage — does the page answer the query and its neighbours
- **H2/H3 outline:** scan the headings. Do they cover the primary query *and* the obvious
  follow-on questions a searcher has (cost, time, process, eligibility, "is it right for me")?
  Gaps are ranking and AEO opportunities — add a section.
- **Query/entity coverage:** the page should mention the keyword's natural variants and
  related entities (e.g. for "consent orders": court, parenting, property, FCFCOA, application)
  without stuffing. Thin coverage loses to deeper competitors.
- **Word depth:** blog cornerstones target ≥1,000 body words (R3); service/location pages are
  substantial too. If a striking-distance page is thin versus what ranks above it, depth is
  often the fix.
- **Freshness:** dates, fee figures, and the 2025 Family Law Act reforms should be current.

## E. AEO answer box — the sentence answer engines quote
Answer-engine citation depends on a **direct, self-contained answer to the page's core
question, high on the page, in plain prose.**
- Blog pages have a `key_takeaway(...)` box; service pages have an `answer(...)` "In short:"
  block. Confirm it exists and that its **first sentence fully answers the query on its own**
  (no "it depends" hedging, no unresolved pronouns) — that is what gets lifted into an AI
  answer. Make it quotable: one or two crisp sentences, specific, Australian.
- If the page has no answer block, add one (the generator helper for that page type).
- Numbers and named facts in the answer should be defensible and, ideally, cited nearby.

## F. FAQ + FAQPage schema — structured answers to real questions
- The page should carry an FAQ block that becomes `FAQPage` JSON-LD (`faq_schema`/`faq_html`).
- **Questions should be the actual ones people search** (use the rankings file and the
  "People also ask" style: "How long does …", "How much does …", "Do I need a lawyer for …").
  Replace generic Qs with high-intent ones.
- **Answers are self-contained and concise** (2–4 sentences) — each is independently quotable.
- Verify the `FAQPage` block is present in the JSON-LD `@graph` and that the on-page Q&A text
  matches the schema text (Google requires parity).

## G. JSON-LD schema completeness & validity
- **Right types for the page:** `LegalService`/`Organization` site-wide, plus the page-type
  schema — `Service` for service pages, `Article` for blog/resource pages, `FAQPage` where
  there are FAQs, `BreadcrumbList` everywhere with a trail. Locations carry a per-city
  `LegalService`. Confirm the expected types are in the `@graph`.
- **Completeness:** the entity has name, description, URL; Service has `serviceType`/provider;
  Article has headline matching the H1 intent. Fill obvious gaps.
- **Validity:** exactly one `application/ld+json` block, it parses, and no broken strings from
  the `cite()` double-quote trap (see the blog skill). The one-liner counts the blocks; eyeball
  the JSON for stray quotes.

## H. Internal linking — flow equity to and within the page
- **Links out:** the page should link to its natural neighbours (related services, locations,
  guides) with **descriptive keyword anchor text**, not "click here". Blog pages have a
  "Related" grid; make sure the slugs are real and relevant.
- **Links in:** identify 2–3 strong existing pages that *should* link to this one for the
  target keyword and add a contextual link from them (this is often the highest-leverage,
  most-overlooked fix for a striking-distance page). Each is a small generator edit on the
  linking page.
- **No broken internal links:** the validation one-liner reports `broken` — must be NONE.

## I. Canonical, indexability & technical
- **Canonical** points to the page's own clean URL (`head()` sets this from the slug).
- **Indexability:** the page is `index, follow` — **except the homepage**, which is
  intentionally `noindex, nofollow` on staging (do not change; see generator-map.md).
- **URL/slug** is clean, lowercase, hyphenated, keyword-bearing (already true for new slugs).
- **Trailing-slash** internal links (`/slug/`) — keep the house convention.

## Output of the audit
A compact before→after table the user can approve, e.g.:

| Item | Now | Proposed | Why |
|---|---|---|---|
| Title (chars) | "…" (54) | "…" (58) | keyword-first, adds Australian specificity |
| Meta desc (chars) | "…" (171 ✗) | "…" (156) | within 160, adds soft CTA |
| H1 | "…" | "…" | keyword-first per R1 |
| Answer box | hedged | crisp 1-sentence answer | AEO citation |
| FAQ | 3 generic | 5 high-intent | matches search demand |
| Schema | Service+FAQ | +BreadcrumbList | completeness |
| Internal links in | 1 | 3 (from X, Y, Z) | flow equity for the keyword |

Then apply, build, validate, preview.
