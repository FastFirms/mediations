# The post() API and how to author a cornerstone

Everything here lives in `build/`. A blog post is a single `post(...)` call placed in a
new `build/gen_blog_batchN.py` file. Importing from `gen_blog` also rebuilds the 4
flagship posts defined in that module — that is expected and harmless (identical output).

## Signature

```python
from gen_blog import post, inline_cta, callout, key_takeaway
from authority_sources import cite

post(slug, title, desc, category, h1, dek, toc, body, qa, related, read_min=7)
```

| Arg | Type | What it is | Rules |
|---|---|---|---|
| `slug` | str | URL slug → page is served at `/<slug>/` | lowercase-hyphen, keyword-first, unique |
| `title` | str | `<title>` + OG/Twitter title | **≤ 60 chars** (R8) |
| `desc` | str | meta description + OG/Twitter desc | **≤ 160 chars** (R8) |
| `category` | str | the pill/tag label | HTML-escape `&` as `&amp;` (e.g. `"Costs &amp; fees"`) |
| `h1` | str | the on-page H1 | **keyword-first** (R1), wrap the emotional/wedge part in `<em>…</em>` |
| `dek` | str | the lede paragraph under the H1 | 1–3 sentences, sets up the answer |
| `toc` | list[tuple] | `[(anchor_id, label), …]` | one entry per H2; `anchor_id` must match each H2's `id` |
| `body` | str | the full article HTML | see "Assembling the body" below |
| `qa` | list[tuple] | `[(question, answer), …]` | becomes the on-page FAQ **and** `FAQPage` schema; 4–6 pairs |
| `related` | list[tuple] | `[(slug, label), …]` | 5–6 **real existing** slugs; renders the related grid |
| `read_min` | int | estimated read time shown in meta | optional, default 7 |

`post()` returns `(slug, word_count)`.

## The helper functions

```python
key_takeaway(text)            # the AEO answer box. Put it FIRST in body. Make it quotable.
inline_cta(text, btn="Book a free consultation")  # soft CTA band, placed between sections
callout(heading, paragraph)   # a boxed aside (e.g. "Consent orders vs a BFA")
cite(key)                     # an <a> to an authority source from authority_sources.py
```

`cite('key')` returns `<a href="URL" target="_blank" rel="noopener">Label</a>`. Valid keys
live in `build/authority_sources.py` (e.g. `family_law_act`, `fcfcoa_fees`, `abs_divorce`,
`services_australia_cs`, `fair_work`, `respect_1800`). `TOPIC_SOURCES` in that file suggests
which keys fit which topic. If you need a source that is not in the library, add it to the
`AUTHORITY` dict first (a `.gov.au` / `.edu` / peak-body URL), then `cite()` it.

## Assembling the body (and the cite() quoting trap — R4)

`body` is one big string built by concatenating pieces with `+`. Pattern:

```python
body = (
  key_takeaway("Direct 1–2 sentence answer to the page's core question.")
  + f"""
<h2 id="what-is">What is X?</h2>
<p>Plain-English explanation. Cite authority like this: {cite('family_law_act')}.
   Internal links use normal double quotes: <a href="/family-law-mediation/">mediation</a>.</p>
"""
  + inline_cta("Contextual nudge worded to the section just read.")
  + f"""
<h2 id="how-it-works">How it works</h2>
<p>… {cite('fcfcoa_fees')} …</p>
<figure class="tbl"><table><caption>Typical costs</caption>
  <thead><tr><th>Item</th><th>Cost</th></tr></thead>
  <tbody><tr><td>Filing fee</td><td>~$1,100</td></tr></tbody>
</table></figure>
"""
  + callout("A useful aside", "One or two sentences.")
  + # … more sections, ~7–8 H2 total, 7–8 inline_cta total …
)
```

**The trap:** `cite()` emits `href="..."` with *double* quotes. This is fine inside
**triple-quoted** f-strings (`f"""…"""`) — you can freely mix `cite()` and double-quoted
internal `<a href="...">` links, as the existing posts do. The collision only happens in
*single*-quoted f-strings. So: **always use triple-quoted f-strings for sections that call
`cite()`.** For a section that is a plain (non-f) string and still needs an authority link,
write the link literally with **single quotes**: `<a href='https://…' target='_blank'
rel='noopener'>…</a>`. `check_authority.py` accepts both quote styles.

## HTML conventions inside the body

- Each `<h2>` needs an `id` that exactly matches its `toc` entry, so the jump menu works.
- Lists: plain `<ul>`/`<ol>` — the stylesheet handles the custom bullets/numbers.
- Tables: wrap in `<figure class="tbl">…</figure>`; use `<caption>` for the table title;
  add a `<p class="source-note">` after it citing the data source where relevant.
- Internal links: relative, e.g. `<a href="/parenting-plan-mediation/">…</a>`. Verify the
  target slug exists (validation will flag broken internal links).
- `BOOK_URL` is handled for you by `inline_cta()` and the closing band — never hard-code the
  booking URL (R5).

## Worked checklist before you build

- [ ] H1 keyword-first with an `<em>` emphasis
- [ ] `title` ≤ 60, `desc` ≤ 160
- [ ] `key_takeaway()` is the first thing in `body` and directly answers the question
- [ ] 7–8 `<h2>` sections, each `id` present in `toc`
- [ ] ≥ 1 data table where the topic supports it
- [ ] 7–8 `inline_cta()` interleaved, each contextual
- [ ] ≥ 2–3 `cite()` / authority links
- [ ] 4–6 FAQ pairs in `qa`
- [ ] 5–6 real existing slugs in `related`
- [ ] ≥ 1,000 body words (the return value's word count is the whole page; aim high)
- [ ] Voice: calm, lawyer-friendly, villain = unnecessary litigation
- [ ] Safety content rules applied if the topic touches violence/abuse/crisis (R6)

After writing, do the 3 wiring edits (index, meta, check_authority) and follow
`build-validate-deploy.md`.
