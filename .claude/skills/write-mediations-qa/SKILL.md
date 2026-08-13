---
name: write-mediations-qa
description: Write and publish a new Q&A page for the Mediations Australia /questions/ knowledge hub. Use whenever the user wants to add, draft, or publish a question-and-answer page. Knows the qa_page() generator API, editorial rules, source hierarchy, expert attribution, and the safe branch-and-preview deploy flow. Do NOT use for blog cornerstones (use write-mediations-blog) or service/location pages.
---

# Write a Mediations Australia Q&A page

This skill creates a new question-and-answer page under `/questions/` for the
Mediations Australia static site, using the `gen_question_pages.py` generator.

Read `../../../CLAUDE.md` (the project bible) if you have not already this session.
Where CLAUDE.md and this skill ever disagree, CLAUDE.md wins.

## How Q&A pages differ from blog cornerstones

| Blog cornerstone | Q&A page |
|---|---|
| ≥1,000 words, depth standard | No arbitrary word count — use the length the question needs |
| Thought-leadership tone | Information-density tone: answer first, context second |
| 7–8 H2 sections | Flexible structure driven by the question |
| Inline CTAs every section | One restrained CTA, clearly separated from the answer |
| City/location variants acceptable | One canonical national answer — no city variants unless law genuinely differs |
| Topical authority piece | Specific user intent answered precisely |

## The brand voice — Q&A edition

Same house style as the blog, with one additional rule: **answer the question
in the first sentence.** No "Navigating the complexities of..." openings. No
table-of-contents padding when the answer is short. Get to the point.

- Calm, considered, precise. Not corporate-legal, not salesy.
- Honest about limits: where the answer differs by state, say so. Where a
  question is out of scope for mediation, say so.
- Lawyer-friendly: never "vs lawyers" framing.
- Avoid: "battle", "fight", "win", "act now", heroic litigation language.
- Prefer: "resolve", "agree", "by agreement", "without court".

## What "good" looks like

A good Q&A page:

1. Opens with a **direct answer box** — 1–3 sentences that fully answer the
   question. This is what an AI overview or voice assistant will cite.
2. Has a **keyword-first H1** — the question itself, verbatim or lightly
   edited for naturalness.
3. Contains a **named expert attribution** — the FDRP or mediator who wrote or
   reviewed the answer. Link to their profile page.
4. Cites **primary Australian sources** — legislation, court websites, AGD,
   Fair Work, AMDRAS. Minimum 2 authority citations per page.
5. Includes **related questions** — 3–5 manually curated links to other
   `/questions/` pages in the same cluster.
6. Has one **restrained conversion CTA** — clearly separated from the answer
   body. Not a hard sell; an invitation.
7. Has a **"Last reviewed" date** in DD Month YYYY format.

## Safety content rules (rule R6 — non-negotiable)

If the topic touches family violence, abuse, or coercive control:
- State plainly that mediation may not be appropriate and that exemptions apply.
- Link to `/domestic-violence-and-family-law/`.
- Surface **1800RESPECT (1800 737 732)** and **000** in an emergency.
- Never minimise or qualify safety concerns for brevity.

## Source hierarchy

Use sources from `build/authority_sources.py` via `cite('key')` where available.
For Q&A pages the primary hierarchy is:

**Family/FDR topics:** Federal Circuit and Family Court of Australia → Australian
Attorney-General's Department → relevant legislation (Family Law Act 1975,
Family Court Act 1997 WA) → AMDRAS.

**Workplace topics:** Fair Work Ombudsman → Fair Work Commission → Safe Work
Australia → relevant legislation (Fair Work Act 2009).

**Commercial/estate topics:** Attorney-General's Department → AMDRAS → relevant
state legislation.

Secondary commentary may supplement but must not replace primary authority citations.

## Expert attribution

Assign a real named reviewer from the Mediations Australia team. Current
practitioners: Dan Toombs (FDRP, mediator), Prav Singh Pillay (FDRP, mediator).
Link to `/our-mediators/` or the individual profile page.

Do **not** use "Mediations Australia Editorial Team" for flagship Q&A pages.

## The `qa_page()` API

Full annotated API is in **`references/qa-api.md`** — read it before writing
your first page. In short:

```python
qa_page(
    slug,           # URL slug under /questions/ — e.g. "what-is-a-section-60i-certificate"
    question,       # The full question string — becomes the H1
    title,          # <title> tag ≤60 chars
    desc,           # meta description ≤160 chars
    category,       # "family" | "workplace" | "commercial" | "estates" | "mediation-process"
    direct_answer,  # Plain text — 1–3 sentence direct answer shown in the answer box
    body,           # HTML string — expanded answer, context, tables, worked examples
    sources,        # list of (label, url) tuples for the sources section
    reviewer,       # Name string — "Dan Toombs" or "Prav Singh Pillay"
    reviewer_slug,  # Profile page slug — "dan-toombs" or "prav-singh-pillay"
    related,        # list of /questions/ slugs — 3–5 related questions
    read_min,       # int — estimated read time in minutes
)
```

Helper functions available inside `body`:
- `cite('key')` — inline authority citation link (same as blog skill)
- `callout(text, type='info'|'warning'|'alert')` — coloured callout box

## The workflow — follow in order

### 1. Get on a safe branch
Never work on `main`. From the repo root:
`git switch -c qa/<slug>` or reuse an existing working branch.
Confirm with `git branch --show-current` that you are not on `main`.

### 2. Choose the question
If the user named a question, use it. If not, pick from the Tier 1 blueprint
list, starting with the five first-sprint questions:
1. do-i-need-mediation-before-family-court
2. what-if-my-ex-refuses-mediation
3. what-is-a-section-60i-certificate
4. who-can-issue-a-section-60i-certificate
5. how-much-does-family-mediation-cost

### 3. Research for accuracy
Family-law facts must be current and correct (Australian jurisdiction; note WA
differs: s.66H Family Court Act 1997 WA vs s.60I Family Law Act 1975 Cth).
Reflect 2025 Family Law Act reforms where relevant.

### 4. Write the page
Add a `qa_page(...)` call to `build/gen_question_pages.py`. Follow the API in
`references/qa-api.md`. Keep `direct_answer` tight — it is what AI overviews quote.

### 5. Wire it in (2 small edits)
- `build/gen_questions_hub.py` → add the question to the relevant `QUESTIONS`
  list so it appears in the hub grid.
- `build/gen_meta.py` → add `questions/<slug>` to the `core` list.

### 6. Build
From `build/`:
```
python3 gen_question_pages.py
python3 gen_questions_hub.py
python3 gen_meta.py
```

### 7. Validate
- `git diff --stat` — only intended pages should change.
- Run the site-health one-liner (in `references/build-validate-deploy.md`):
  expect `H1:0 | schema:0 | broken:NONE`.
- Check `<title>` ≤60 chars, meta description ≤160 chars.
- Check the named reviewer and review date render in the built HTML.

### 8. Commit, push, preview
Commit on the branch, push, and report the Vercel preview URL.

## Reference files
- `references/qa-api.md` — the `qa_page()` API, helpers, skeleton, worked example.
- `references/build-validate-deploy.md` — build commands, never-run list, validation one-liner.
