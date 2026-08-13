#!/usr/bin/env python3
"""Generate the /questions/ hub page — the Q&A knowledge hub index.

Imports QUESTION_REGISTRY from gen_question_pages.py to build the grid automatically.
Run after gen_question_pages.py so the registry is populated.

Usage (from build/ directory):
    python3 gen_question_pages.py && python3 gen_questions_hub.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html,
                       cta_band, org_schema, breadcrumb_schema, faq_schema,
                       BOOK_URL, PHONE, PHONE_HREF)
from gen_question_pages import QUESTION_REGISTRY

OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CATEGORIES = [
    ("family",            "Family Mediation",
     "Parenting, property, separation, FDR and Section 60I certificates."),
    ("workplace",         "Workplace Mediation",
     "Employees, employers, HR teams and workplace conflict."),
    ("commercial",        "Commercial Mediation",
     "Business, partnership, shareholder and contractual disputes."),
    ("estates",           "Estate Mediation",
     "Wills, estates, inheritance and family provision disputes."),
    ("mediation-process", "About Mediation",
     "Costs, confidentiality, lawyers, preparation and what to expect."),
]

CATEGORY_ICONS = {
    "family":            "&#x1F46A;",
    "workplace":         "&#x1F3E2;",
    "commercial":        "&#x1F91D;",
    "estates":           "&#x2696;&#xFE0F;",
    "mediation-process": "&#x1F4AC;",
}


def build():
    slug  = "questions"
    title = "Mediation Questions & Answers | Mediations Australia"
    desc  = ("Clear answers to common questions about mediation, family dispute "
             "resolution, workplace disputes and commercial mediation in Australia. "
             "Written by accredited Australian mediators.")

    by_cat = {cat: [] for cat, _, _ in CATEGORIES}
    for q in QUESTION_REGISTRY:
        cat = q.get("category", "mediation-process")
        if cat in by_cat:
            by_cat[cat].append(q)

    # Category cards
    cat_cards = ""
    for cat_key, cat_label, cat_desc in CATEGORIES:
        count = len(by_cat.get(cat_key, []))
        icon  = CATEGORY_ICONS.get(cat_key, "&#x1F4CB;")
        cat_cards += (
            f'<a href="#cat-{cat_key}" class="card" style="text-decoration:none;display:block">'
            f'<div style="font-size:2rem;margin-bottom:.5rem">{icon}</div>'
            f'<h3 style="margin:.25rem 0 .5rem">{esc(cat_label)}</h3>'
            f'<p style="font-size:.9rem;color:var(--muted,#6b7280);margin:0">{esc(cat_desc)}</p>'
            f'<span style="display:inline-block;margin-top:.75rem;font-size:.85rem;'
            f'color:var(--accent,#2d6be4)">{count} question{"s" if count != 1 else ""} &#x2192;</span>'
            f'</a>'
        )

    # Question grid grouped by category
    grid_sections = ""
    for cat_key, cat_label, _ in CATEGORIES:
        questions = by_cat.get(cat_key, [])
        if not questions:
            continue
        cards = ""
        for q in questions:
            preview = q["desc"][:120] + ("&#x2026;" if len(q["desc"]) > 120 else "")
            cards += (
                f'<article class="card" style="display:flex;flex-direction:column">'
                f'<h3 style="font-size:1rem;margin:.25rem 0 .5rem">'
                f'<a href="/questions/{q["slug"]}/" style="color:inherit;text-decoration:none">'
                f'{esc(q["question"])}</a></h3>'
                f'<p style="font-size:.88rem;color:var(--muted,#6b7280);flex:1;margin:0 0 .75rem">'
                f'{preview}</p>'
                f'<a href="/questions/{q["slug"]}/" class="more" style="font-size:.875rem;margin-top:auto">'
                f'Read the answer <span class="arr">&#x2192;</span></a>'
                f'</article>'
            )
        grid_sections += (
            f'<div id="cat-{cat_key}" style="margin-top:3rem">'
            f'<h2 style="margin-bottom:1.25rem">{esc(cat_label)}</h2>'
            f'<div class="cards reveal">{cards}</div>'
            f'</div>'
        )

    # Can't find your question? box
    submission = (
        f'<div style="background:var(--surf,#f7f8fa);border-radius:12px;'
        f'padding:2rem;text-align:center;margin-top:3rem">'
        f'<p style="font-weight:600;font-size:1.1rem;margin-bottom:.5rem">'
        f"Can&#x27;t find your question?</p>"
        f'<p style="color:var(--muted,#6b7280);margin-bottom:1.25rem">'
        f'Call us and we&#x27;ll answer it &#x2014; or send it below and we&#x27;ll '
        f'add it to the library.</p>'
        f'<a href="/contact-us/" class="btn btn-primary">'
        f'Ask a question <span class="arr">&#x2192;</span></a>'
        f'</div>'
    )

    qa_pairs = [(q["question"], q["desc"]) for q in QUESTION_REGISTRY[:10]]

    schema = [
        org_schema(),
        breadcrumb_schema([("Home", ""), ("Questions &amp; Answers", None)]),
        faq_schema(qa_pairs),
    ]

    doc = head(title, desc, slug, extra_schema=schema)
    doc += nav()
    doc += f"""<main id="main">
{crumb_html([("Home",""),("Questions &amp; Answers",None)])}
<section class="phero" style="padding-bottom:2.5rem">
  <div class="phero-blob"></div>
  <div class="wrap">
    <span class="eyebrow"><span class="pulse"></span>Knowledge hub</span>
    <h1>Your Mediation Questions, <em>Answered</em></h1>
    <p class="lede">Clear answers to common questions about mediation, family dispute
    resolution, workplace disputes and commercial mediation in Australia.
    Written and reviewed by accredited Australian mediators and Family Dispute
    Resolution Practitioners.</p>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="reveal">
      <p class="sec-tag">Browse by topic</p>
      <h2 class="sec-title">What do you need help with?</h2>
    </div>
    <div class="cards reveal" style="margin-top:2rem">{cat_cards}</div>
  </div>
</section>

<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="reveal">
      <p class="sec-tag">All questions</p>
      <h2 class="sec-title">Browse the full library</h2>
      <p style="max-width:54ch;color:var(--muted,#6b7280)">
        {len(QUESTION_REGISTRY)} answered question{"s" if len(QUESTION_REGISTRY) != 1 else ""},
        each with primary Australian sources and expert review.</p>
    </div>
    {grid_sections}
    {submission}
  </div>
</section>
</main>"""
    doc += cta_band(
        "Need to speak with a mediator?",
        "Our accredited practitioners are available for a free initial consultation "
        "&#x2014; by phone, video or in person across Australia."
    )
    doc += page_end()

    path = os.path.join(OUT, "questions")
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "index.html"), "w") as f:
        f.write(doc)
    print(f"  ✓ /questions/ hub ({len(QUESTION_REGISTRY)} questions listed)")


if __name__ == "__main__":
    print("\nBuilding /questions/ hub...")
    build()
    print()
