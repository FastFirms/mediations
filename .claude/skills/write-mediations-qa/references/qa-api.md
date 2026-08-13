# Q&A Page API reference

## `qa_page()` — full annotated signature

```python
qa_page(
    slug,           # str  — URL segment under /questions/
                    #        e.g. "what-is-a-section-60i-certificate"
                    #        Do NOT include /questions/ prefix.

    question,       # str  — The full question, becomes the <h1>.
                    #        Write it as the user would type it.
                    #        e.g. "What is a Section 60I certificate?"

    title,          # str  — <title> tag. ≤60 chars. Must include the
                    #        question or core keyword. Append " | Mediations Australia"
                    #        only if it fits within 60 chars.

    desc,           # str  — meta description. ≤160 chars. Must directly
                    #        answer the question in plain language.

    category,       # str  — one of:
                    #        "family"            — parenting, property, FDR, s60I
                    #        "workplace"         — employees, employers, HR, Fair Work
                    #        "commercial"        — business, partnership, contracts
                    #        "estates"           — wills, inheritance, family provision
                    #        "mediation-process" — costs, confidentiality, preparation

    direct_answer,  # str  — PLAIN TEXT (no HTML). 1–3 sentences that fully
                    #        answer the question. Renders in the answer box at
                    #        the top of the page. This is what AI overviews cite.
                    #        Be precise. No hedging padding. No "it depends"
                    #        without immediately saying what it depends on.

    body,           # str  — HTML string. Expanded answer below the answer box.
                    #        Use <h2>, <p>, <ul>, <table> as needed.
                    #        Use callout() for warnings. Use cite() for sources.
                    #        Keep information density high. Avoid padding.

    sources,        # list of (label, url) tuples.
                    #        Minimum 2. Prefer primary Australian authority URLs.
                    #        e.g. [
                    #          ("Family Law Act 1975 (Cth) s.60I",
                    #           "https://www.legislation.gov.au/Series/C2004A00275"),
                    #          ("Federal Circuit and Family Court of Australia — FDR",
                    #           "https://www.fcfcoa.gov.au/fl/fdr"),
                    #        ]

    reviewer,       # str  — Full name of the reviewing practitioner.
                    #        "Dan Toombs" or "Prav Singh Pillay"

    reviewer_slug,  # str  — slug for their profile link.
                    #        "dan-toombs" or "prav-singh-pillay"

    related,        # list of str — 3–5 slug strings relative to /questions/.
                    #        Only link to pages that exist or are being built
                    #        in the same sprint.

    read_min,       # int  — estimated read time in minutes.
)
```

## Helper functions

### `cite('key')`
Returns an inline hyperlinked citation. Keys defined in `build/authority_sources.py`.

Common keys:

| Key | Source |
|-----|--------|
| `fcfcoa` | Federal Circuit and Family Court of Australia |
| `agd_fdr` | Attorney-General's Department — Family Dispute Resolution |
| `fla` | Family Law Act 1975 (Cth) |
| `fwo` | Fair Work Ombudsman |
| `fwc` | Fair Work Commission |
| `amdras` | AMDRAS (mediator accreditation body) |

**The cite() quoting trap:** do NOT put `cite()` inside an f-string using the
same quote character. Use the opposite quote inside the call:

```python
# WRONG — breaks the f-string
body = f"...as required by {cite("fcfcoa")}..."

# CORRECT
body = f"...as required by {cite('fcfcoa')}..."
```

### `callout(text, type='info')`
Renders a coloured callout box. Types:
- `'info'` — blue, neutral context or definitions
- `'warning'` — amber, important qualifications or state differences
- `'alert'` — red, safety-critical (family violence, urgent orders)

```python
callout(
    "If there is family violence or safety risk, mediation may not be appropriate. "
    "Call <strong>1800RESPECT on 1800&nbsp;737&nbsp;732</strong> or <strong>000</strong> "
    "in an emergency. See our guide to <a href='/domestic-violence-and-family-law/'>"
    "family violence and family law</a>.",
    type='alert'
)
```

## Review date
The generator inserts today's date as "Last reviewed" in DD Month YYYY format
automatically at build time. Do not pass it.

## Meta limits
- `title` **≤60 chars** — generator warns if exceeded
- `desc` **≤160 chars** — generator warns if exceeded

Count carefully. The question itself is often 50+ chars. Drop
" | Mediations Australia" from `title` if the question alone fills 50+ chars.

## Worked example — "What is a Section 60I certificate?"

```python
qa_page(
    slug="what-is-a-section-60i-certificate",
    question="What is a Section 60I certificate?",
    title="What Is a Section 60I Certificate? | Mediations Australia",
    desc="A Section 60I certificate is issued by an accredited FDR Practitioner after family mediation is attempted or cannot proceed. Required before most parenting court applications.",
    category="family",
    direct_answer=(
        "A Section 60I certificate is a document issued by an accredited Family Dispute "
        "Resolution Practitioner (FDRP) after family mediation has been attempted, completed, "
        "or assessed as unsuitable. In most cases, you must hold a current Section 60I "
        "certificate before filing a parenting application in the Federal Circuit and "
        "Family Court of Australia."
    ),
    body=(
        f"<h2>What does a Section 60I certificate say?</h2>"
        f"<p>There are five certificate types an FDRP can issue:</p>"
        f"<table><thead><tr><th>Certificate type</th><th>Meaning</th></tr></thead>"
        f"<tbody>"
        f"<tr><td>s60I(8)(aa)</td><td>Mediation attended, genuine effort by all parties</td></tr>"
        f"<tr><td>s60I(8)(a)</td><td>Other party did not attend</td></tr>"
        f"<tr><td>s60I(8)(b)</td><td>FDR assessed as not appropriate (e.g. family violence)</td></tr>"
        f"<tr><td>s60I(8)(c)</td><td>One party did not make a genuine effort</td></tr>"
        f"<tr><td>s60I(8)(d)</td><td>FDR started but not completed</td></tr>"
        f"</tbody></table>"
        f"<h2>When do you need one?</h2>"
        f"<p>Under {cite('fla')} section 60I, most parenting applications to the "
        f"{cite('fcfcoa')} require a certificate unless an exemption applies — including "
        f"genuine family violence risk, urgency, or where the other party cannot be located.</p>"
        f"<h2>Western Australia</h2>"
        f"{callout('In Western Australia, parenting matters may be filed in the Family Court of Western Australia under section 66H of the Family Court Act 1997 (WA), which has its own FDR certificate requirements.', type='warning')}"
        f"<h2>How long is a Section 60I certificate valid?</h2>"
        f"<p>There is no legislated expiry date, but courts may question a certificate "
        f"that is several years old if circumstances have significantly changed.</p>"
    ),
    sources=[
        ("Family Law Act 1975 (Cth) s.60I",
         "https://www.legislation.gov.au/Series/C2004A00275"),
        ("Federal Circuit and Family Court of Australia — Family Dispute Resolution",
         "https://www.fcfcoa.gov.au/fl/fdr"),
        ("Attorney-General's Department — Family Dispute Resolution",
         "https://www.ag.gov.au/families-and-marriage/families/family-dispute-resolution"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "who-can-issue-a-section-60i-certificate",
        "do-i-need-mediation-before-family-court",
        "what-if-my-ex-refuses-mediation",
        "what-happens-if-family-mediation-fails",
        "is-family-mediation-confidential",
    ],
    read_min=3,
)
```

## Checklist before building

- [ ] `direct_answer` reads naturally as a standalone paragraph
- [ ] `title` ≤60 chars (count it)
- [ ] `desc` ≤160 chars (count it)
- [ ] At least 2 `sources` entries, both primary authority URLs
- [ ] `related` slugs all exist or are being built in the same sprint
- [ ] Family violence callout present if topic touches DV or coercive control
- [ ] WA callout present if topic involves s.60I / FDR / de facto property
- [ ] `reviewer` is a real named practitioner, not "Editorial Team"
- [ ] `category` matches one of the five valid values exactly
