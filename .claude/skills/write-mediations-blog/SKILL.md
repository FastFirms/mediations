---
name: write-mediations-blog
description: >-
  Write and publish a new blog cornerstone for the Mediations Australia website
  (mediationsaustralia.com.au) using its Python build system. Use this skill
  whenever the user wants to add, draft, write, generate, or publish a blog post,
  guide, or article for the Mediations Australia / mediations site — even if they
  only say "write a blog", "add a guide", "new article about X", or name a family-law
  topic to cover. Also use when asked to pick a topic from content gaps, or to wire a
  post into the guides index, sitemap, and authority check. This skill knows the
  house brand voice, the strict SEO/AEO content standards, the post() generator API,
  and the safe branch-and-preview deploy flow. Do NOT use it for editing service or
  location pages, the homepage, or non-blog content.
---

# Write a Mediations Australia blog post

This skill creates a new blog cornerstone for the Mediations Australia static site and
publishes it the safe way: written through the project's Python generator, wired into
the index/sitemap, validated, and pushed to a **branch** for a Vercel preview — never
straight to production.

Read `../../../CLAUDE.md` (the project bible) if you have not already this session. It
is the source of truth for brand, voice, and the non-negotiable rules. This skill
operationalises it for blog writing; where they ever disagree, CLAUDE.md wins.

## The brand voice (get this right — it is the whole point)

The wedge: **"Court has its place — but rarely the best place to start."** The villain
is **unnecessary litigation and the adversarial process — never lawyers** (many of the
firm's own mediators are lawyers, and lawyers are a key referral channel).

- Calm, considered, persuasive without pressure. Not corporate-legal, not salesy.
- Honest about limits. Where mediation is not appropriate (family violence, safety
  risk, urgent orders, refusal to disclose), say so plainly.
- Lawyer-friendly framing: "family lawyers *and* mediators", never "vs".
- Avoid: "battle", "fight", "win", "destroy", heroic "litigate", "act now".
- Prefer: "resolve", "agreement", "early resolution", "without court", "smarter first step".

If a draft reads like aggressive personal-injury advertising, rewrite it. See the voice
samples in CLAUDE.md §13 to calibrate.

## What "good" looks like (the depth standard — rule R3)

Every cornerstone targets **≥1,000 body words** and includes, in this order:

1. Keyword-first `<h1>` with an italic `<em>` emphasis on the emotional/wedge part.
2. A **Key takeaway** answer box that directly answers the page's question in 1–2
   sentences (this is the AEO signal answer engines cite — make it quotable).
3. A table-of-contents jump menu.
4. **7–8 H2 sections**, each with a stable `id` matching the ToC.
5. **At least one data table** where the topic supports it (costs, timeframes, comparisons).
6. **7–8 inline CTAs** interleaved between sections, each worded to the section just read.
7. An FAQ block (becomes `FAQPage` schema).
8. A "Related guides & services" grid.
9. The closing CTA band (added automatically by the generator).

The flagship to match or beat is `cost-of-divorce-in-australia` (1,183 body words, 5
tables, 7 authority links). Aim there.

**Authority citations (rule R2 — enforced by the build):** every post needs **≥2–3
links** to `.gov.au` / `.edu` / peak-body sources. Pull them from
`build/authority_sources.py` via `cite('key')`. `check_authority.py` fails the build if
a post has fewer than two — do not relax it; it is the E-E-A-T signal.

**Meta limits (rule R8):** `title` ≤ 60 chars, `desc` ≤ 160 chars. The generator emits the
matching Open Graph + Twitter tags from these, so getting them right covers all three.

## How the post() generator works

You author a post by calling `post(...)` from `build/gen_blog.py`. Full annotated API,
the helper functions, the cite() quoting trap, and a copy-paste skeleton are in
**`references/post-api.md`** — read it before writing your first post.

In short: a post is one `post(slug, title, desc, category, h1, dek, toc, body, qa,
related, read_min)` call inside a new `build/gen_blog_batchN.py` file. The `body` is an
HTML string assembled from `key_takeaway(...)`, triple-quoted f-string sections (which
may call `cite(...)` and contain internal `<a href="/slug/">` links), `inline_cta(...)`,
and `callout(...)`.

## The workflow — follow in order

### 1. Get on a safe branch
Never write on `main` (Vercel auto-deploys `main` to production). From the repo root:
`git switch -c blog/<slug>` (or reuse an existing working branch). Confirm with
`git branch --show-current` that you are not on `main`.

### 2. Choose the topic
- If the user named a topic/keyword, use it.
- If not, **auto-pick from content gaps**: read `blog-content-manifest.csv` at the repo
  root and the existing slugs (the `BLOG` list in `build/check_authority.py` is the
  canonical list of the 42 published cornerstones). The old-site inventory in
  `build/blog_inventory.py` (~201 legacy slugs) shows demand. Pick a high-intent topic
  that is **not already covered** by an existing cornerstone, and tell the user what you
  picked and why before writing.

### 3. Research for accuracy
Family-law facts must be correct and current (Australian jurisdiction; note WA differs).
Verify figures (fees, time limits, thresholds) against the authority sources. Where the
2025 Family Law Act reforms are relevant, reflect them. If you assert a statistic, cite it.

### 4. Write the post
Create `build/gen_blog_batchN.py` (next unused N) and write one `post(...)` call to the
full standard above. Decide the `category` tag, the ToC ids, the FAQ pairs, and a
`related` grid of 5–6 real existing slugs. See `references/post-api.md`.

### 5. Wire it in (3 small edits)
- `build/gen_blog_index.py` → add a card tuple to `POSTS` (slug, category, title, blurb).
- `build/gen_meta.py` → add the slug to the `core` list (so it enters `sitemap.xml`).
- `build/check_authority.py` → add the slug to the `BLOG` list (so it is validated).

### 6. Build
From `build/`: `python3 gen_blog_batchN.py && python3 gen_blog_index.py && python3 gen_meta.py`.
The generators auto-detect the repo root as the output directory. Exact commands and the
**never-run list** of generators that must NOT be run are in
`references/build-validate-deploy.md`.

### 7. Validate (must pass before you go further)
- `python3 check_authority.py` → must end with `ALL POSTS MEET STANDARD`.
- Run the validation one-liner (in the deploy reference) → expect `H1:0 | schema:0 |
  broken:NONE` and the page count incremented by one.

### 8. Redirects (only if consolidating old URLs)
If this post replaces legacy WordPress URLs, add `301` lines to `redirects.htaccess` and a
row to `url-migration-map.csv` **by hand**. Never regenerate these with
`gen_migration.py` — it is stale and would delete entries (violates rule R7).

### 9. Commit, push, preview
Commit on the branch, push, and report the Vercel preview URL. Production updates only
when the user merges to `main`. Details in `references/build-validate-deploy.md`.

## Safety content rules (rule R6 — non-negotiable)

If the topic touches family violence, abuse, child welfare, or crisis:
- Surface **000** and **1800RESPECT (1800 737 732 / 1800respect.org.au)** clearly.
- State plainly that mediation may not be appropriate where there is family violence, and
  that exemptions apply — link to `domestic-violence-and-family-law/`.
- Never name suicide/self-harm methods. Direct distressed readers to professional help,
  not to mediation.
- Never produce content that could sexualise, groom, or endanger a minor. Refuse and
  explain if a request heads there.

## Reference files
- `references/post-api.md` — the `post()` API, helpers, cite() trap, meta limits, a full
  annotated skeleton, and a worked checklist. **Read before writing.**
- `references/build-validate-deploy.md` — build commands, the never-run generator list,
  the validation one-liner, gap-picking detail, and the git branch/push/preview flow.
