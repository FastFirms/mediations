#!/usr/bin/env python3
"""Generate individual Q&A pages under /questions/{slug}/.

Each page is authored via qa_page() calls at the bottom of this file.
Never edit the built questions/*/index.html files directly — edit here and rebuild.

Usage (from build/ directory):
    python3 gen_question_pages.py
"""
import os, sys
from datetime import date
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html,
                       cta_band, org_schema, faq_schema, breadcrumb_schema,
                       BOOK_URL, PHONE, PHONE_HREF)
from authority_sources import cite

OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REVIEW_DATE = date.today().strftime("%-d %B %Y")

CATEGORY_LABELS = {
    "family":            "Family Mediation",
    "workplace":         "Workplace Mediation",
    "commercial":        "Commercial Mediation",
    "estates":           "Estate Mediation",
    "mediation-process": "About Mediation",
}

# Registry: populated by qa_page() calls; imported by gen_questions_hub.py
QUESTION_REGISTRY = []

# Slug → question text map (for related-links rendering)
SLUG_TO_QUESTION = {}


# ─────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────

def callout(text, type="info"):
    """Render a coloured callout box. type: 'info' | 'warning' | 'alert'"""
    colours = {
        "info":    "background:#eef4fb;border-left:4px solid #2d6be4;",
        "warning": "background:#fffbea;border-left:4px solid #f5a623;",
        "alert":   "background:#fff0f0;border-left:4px solid #d0021b;",
    }
    style = colours.get(type, colours["info"])
    return (f'<div class="callout" style="{style}padding:1rem 1.25rem;'
            f'border-radius:0 6px 6px 0;margin:1.5rem 0">{text}</div>')


def related_links(slugs):
    if not slugs:
        return ""
    items = "".join(
        f'<li><a href="/questions/{s}/">{esc(SLUG_TO_QUESTION.get(s, s.replace("-", " ").capitalize()))}</a></li>'
        for s in slugs
    )
    return (f'<aside style="background:var(--surf,#f7f8fa);border-radius:8px;'
            f'padding:1.5rem 1.75rem;margin:2.5rem 0">'
            f'<p style="font-weight:600;margin-bottom:.75rem">Related questions</p>'
            f'<ul style="margin:0;padding-left:1.25rem">{items}</ul></aside>')


def sources_block(sources):
    if not sources:
        return ""
    items = "".join(
        f'<li><a href="{url}" target="_blank" rel="noopener">{esc(label)}</a></li>'
        for label, url in sources
    )
    return (f'<section style="border-top:1px solid var(--border,#e5e7eb);'
            f'margin-top:2.5rem;padding-top:1.5rem">'
            f'<p style="font-size:.85rem;font-weight:600;color:var(--muted,#6b7280);'
            f'text-transform:uppercase;letter-spacing:.05em;margin-bottom:.5rem">Sources</p>'
            f'<ul style="font-size:.88rem;margin:0;padding-left:1.25rem">{items}</ul></section>')


def reviewer_block(reviewer, reviewer_slug):
    return (f'<div style="display:flex;align-items:center;gap:.75rem;'
            f'margin-top:2.5rem;padding:.75rem 1rem;background:var(--surf,#f7f8fa);'
            f'border-radius:8px;font-size:.9rem">'
            f'<span style="color:var(--muted,#6b7280)">Reviewed by</span>'
            f'<a href="/our-mediators/" style="font-weight:600">{esc(reviewer)}</a>'
            f'<span style="color:var(--muted,#6b7280)">·</span>'
            f'<span style="color:var(--muted,#6b7280)">Last reviewed {REVIEW_DATE}</span></div>')


# ─────────────────────────────────────────────
# Core builder
# ─────────────────────────────────────────────

def qa_page(slug, question, title, desc, category,
            direct_answer, body, sources, reviewer, reviewer_slug,
            related, read_min):
    """Build one Q&A page and register it for the hub."""

    if len(title) > 60:
        print(f"  WARN [{slug}] title {len(title)} chars > 60")
    if len(desc) > 160:
        print(f"  WARN [{slug}] desc {len(desc)} chars > 160")

    SLUG_TO_QUESTION[slug] = question
    QUESTION_REGISTRY.append({
        "slug": slug, "question": question, "desc": desc,
        "category": category, "read_min": read_min,
    })

    cat_label = CATEGORY_LABELS.get(category, "Mediation")
    full_slug = f"questions/{slug}"

    schema = [
        org_schema(),
        breadcrumb_schema([
            ("Home", ""),
            ("Questions &amp; Answers", "questions"),
            (question, None),
        ]),
        faq_schema([(question, direct_answer)]),
    ]

    doc = head(title, desc, full_slug, extra_schema=schema)
    doc += nav()
    doc += f"""<main id="main">
{crumb_html([("Home",""),("Questions &amp; Answers","questions"),(esc(question),None)])}
<section class="phero" style="padding-bottom:2rem">
  <div class="phero-blob"></div>
  <div class="wrap">
    <span class="eyebrow"><span class="pulse"></span>{esc(cat_label)}</span>
    <h1>{esc(question)}</h1>
  </div>
</section>
<div class="wrap-narrow" style="padding-top:0">
  <div class="answer reveal" style="margin-bottom:2rem">
    <p><strong>In short:</strong> {esc(direct_answer)}</p>
  </div>
  <article class="body reveal">
    {body}
    {related_links(related)}
    {sources_block(sources)}
    {reviewer_block(reviewer, reviewer_slug)}
  </article>
  <div style="margin:3rem 0 1rem;text-align:center">
    <a href="/questions/" style="font-size:.9rem;color:var(--muted,#6b7280)">&larr; All questions</a>
  </div>
</div>"""
    doc += cta_band(
        "Ready to resolve your dispute?",
        "Our accredited mediators help Australians reach agreements without court. "
        "Book a free consultation to discuss your situation."
    )
    doc += "</main>" + page_end()

    path = os.path.join(OUT, "questions", slug)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "index.html"), "w") as f:
        f.write(doc)
    print(f"  ✓ /questions/{slug}/")


# ═══════════════════════════════════════════════════════════════
# Q&A PAGES — add new qa_page() calls here
# ═══════════════════════════════════════════════════════════════

# ── TIER 1 · SPRINT 1 ────────────────────────────────────────

qa_page(
    slug="do-i-need-mediation-before-family-court",
    question="Do I need mediation before going to Family Court?",
    title="Do I Need Mediation Before Family Court?",
    desc="In most cases yes — Australian law requires FDR before filing parenting orders. Exceptions apply for urgency and family violence.",
    category="family",
    direct_answer=(
        "In most cases, yes. Before filing a parenting application in the Federal Circuit "
        "and Family Court of Australia, the law requires you to attempt family dispute "
        "resolution with an accredited practitioner and obtain a Section 60I certificate. "
        "Exceptions apply where there is family violence, urgency, or child abuse concerns."
    ),
    body=(
        f"<h2>What the law requires</h2>"
        f"<p>Section 60I of the {cite('family_law_act')} makes family dispute resolution "
        f"a prerequisite to most parenting applications in the {cite('fcfcoa')}. Before "
        f"a court will accept your filing, you must produce a Section 60I certificate "
        f"issued by an accredited Family Dispute Resolution Practitioner (FDRP).</p>"
        f"<p>This applies whether you are seeking orders about where a child lives, "
        f"time with a parent, or other parenting arrangements.</p>"
        f"<h2>When mediation is <em>not</em> required</h2>"
        f"<p>You can bypass the FDR requirement if:</p>"
        f"<ul>"
        f"<li>There is a risk of family violence or child abuse</li>"
        f"<li>The matter is urgent — for example, a child needs immediate protection</li>"
        f"<li>The other party cannot be located or contacted</li>"
        f"<li>Either party is unable to participate effectively due to incapacity</li>"
        f"</ul>"
        + callout('If there is family violence or a risk to a child, you may apply directly to the court without FDR. Contact <strong>1800RESPECT on 1800 737 732</strong> or <strong>000</strong> in an emergency. See our guide to <a href="/domestic-violence-and-family-law/">family violence and family law</a>.', type='alert') +
        f"<h2>Does mediation apply to property matters?</h2>"
        f"<p>The FDR certificate requirement applies specifically to <em>parenting</em> "
        f"applications. For property settlement and financial matters there is no strict "
        f"legal precondition to filing — but courts expect parties to have made genuine "
        f"attempts to settle before a hearing is allocated. Mediation remains the most "
        f"efficient path to a property agreement.</p>"
        f"<h2>Western Australia</h2>"
        + callout('In Western Australia, parenting matters may be filed in the Family Court of Western Australia under section 66H of the <em>Family Court Act 1997 (WA)</em>, which carries equivalent FDR requirements. Contact us to confirm which framework applies to your circumstances.', type='warning') +
        f"<h2>What happens at family dispute resolution?</h2>"
        f"<p>At FDR, a neutral accredited practitioner helps both parties discuss "
        f"parenting arrangements in a structured, confidential setting. If agreement is "
        f"reached, it can be formalised in a parenting plan or consent orders. If not, "
        f"the FDRP issues a certificate allowing you to proceed to court. Most FDR "
        f"sessions are completed in a single day. Learn more: "
        f"<a href='/how-mediation-works/'>How mediation works</a>.</p>"
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
        "what-if-my-ex-refuses-mediation",
        "what-is-a-section-60i-certificate",
        "who-can-issue-a-section-60i-certificate",
        "what-happens-if-family-mediation-fails",
        "is-family-mediation-confidential",
    ],
    read_min=3,
)

qa_page(
    slug="what-if-my-ex-refuses-mediation",
    question="What happens if my ex refuses mediation?",
    title="What If My Ex Refuses Mediation?",
    desc="If your ex refuses family mediation, the FDRP issues a Section 60I certificate allowing you to apply to the Family Court. Refusal may also affect costs orders.",
    category="family",
    direct_answer=(
        "If the other party refuses to attend or does not participate genuinely, "
        "the accredited Family Dispute Resolution Practitioner can issue a Section 60I "
        "certificate. This allows you to file a parenting application in the Family Court "
        "without completing FDR. A court may also take the refusal into account when "
        "making costs orders."
    ),
    body=(
        f"<h2>What the FDRP will do</h2>"
        f"<p>When the other party refuses to attend, an accredited FDRP — from a service "
        f"like Mediations Australia or through the {cite('fcfcoa_fdr')} — can issue a "
        f"<a href='/questions/what-is-a-section-60i-certificate/'>Section 60I "
        f"certificate</a> recording that the other party did not attend "
        f"(certificate type s60I(8)(a)) or did not make a genuine effort (s60I(8)(c)).</p>"
        f"<p>That certificate allows you to file a parenting application in the "
        f"{cite('fcfcoa')}.</p>"
        f"<h2>Can refusal affect the outcome in court?</h2>"
        f"<p>Courts have the power to award costs against a party who unreasonably refused "
        f"to participate in dispute resolution. Costs orders are not automatic, but a "
        f"clear refusal without good reason can be raised in proceedings and may influence "
        f"how a judge views that party's reasonableness throughout the matter.</p>"
        f"<h2>What counts as failing to make a 'genuine effort'?</h2>"
        f"<p>Attending but being obstructive, refusing to engage with any compromise, or "
        f"failing to provide required financial disclosure can all constitute a failure to "
        f"make a genuine effort — even if the person technically shows up on the day.</p>"
        f"<h2>When refusal is appropriate</h2>"
        + callout('Refusal is sometimes the right call. If there is family violence, coercive control, or a significant power imbalance, mediation may not be safe or appropriate — and a Section 60I exemption applies. See our guide to <a href="/domestic-violence-and-family-law/">family violence and family law</a> or call <strong>1800RESPECT on 1800 737 732</strong>.', type='alert') +
        f"<h2>What if they agree but then won't engage?</h2>"
        f"<p>Sometimes a party agrees to attend but provides no financial disclosure, "
        f"stonewalls discussion, or walks out. The FDRP assesses whether genuine "
        f"participation occurred and issues the appropriate certificate. "
        f"<a href='/shuttle-mediation-guide/'>Shuttle mediation</a> — where parties "
        f"are in separate rooms — can help in situations where face-to-face contact is "
        f"difficult but both parties are willing to participate.</p>"
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
        "do-i-need-mediation-before-family-court",
        "what-is-a-section-60i-certificate",
        "what-happens-if-family-mediation-fails",
        "is-family-mediation-confidential",
        "can-i-bring-a-lawyer-to-family-mediation",
    ],
    read_min=3,
)

qa_page(
    slug="what-is-a-section-60i-certificate",
    question="What is a Section 60I certificate?",
    title="What Is a Section 60I Certificate? | Mediations Australia",
    desc="A Section 60I certificate is issued by an accredited FDRP after family mediation is attempted or unsuitable. Required before most parenting court applications.",
    category="family",
    direct_answer=(
        "A Section 60I certificate is a document issued by an accredited Family Dispute "
        "Resolution Practitioner (FDRP) after family mediation has been attempted, "
        "completed, or assessed as unsuitable. In most cases, you must hold one before "
        "you can file a parenting application in the Federal Circuit and Family Court "
        "of Australia."
    ),
    body=(
        f"<h2>Why it exists</h2>"
        f"<p>The {cite('family_law_act')} requires most separating parents to attempt "
        f"family dispute resolution before asking a court to make parenting orders. The "
        f"Section 60I certificate is the FDRP's record of what happened — whether "
        f"mediation was completed, why it was not, or why it was assessed as inappropriate.</p>"
        f"<h2>The five certificate types</h2>"
        f"<table style='width:100%;border-collapse:collapse;margin:1rem 0'>"
        f"<thead><tr style='background:var(--surf,#f7f8fa)'>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Certificate</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Meaning</th>"
        f"</tr></thead><tbody>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>s60I(8)(aa)</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Mediation attended and a genuine effort was made by all parties</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>s60I(8)(a)</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>The other party did not attend</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>s60I(8)(b)</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>FDR assessed as not appropriate (e.g. family violence or safety concern)</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>s60I(8)(c)</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>One party did not make a genuine effort</td></tr>"
        f"<tr><td style='padding:.6rem .8rem'>s60I(8)(d)</td>"
        f"<td style='padding:.6rem .8rem'>FDR commenced but was not completed</td></tr>"
        f"</tbody></table>"
        f"<h2>Does the certificate type affect my court application?</h2>"
        f"<p>Any of these certificate types allows you to file a parenting application. "
        f"However, the type may be relevant to how a court views the parties' conduct — "
        f"particularly whether someone failed to make a genuine effort.</p>"
        f"<h2>How long is a Section 60I certificate valid?</h2>"
        f"<p>There is no legislated expiry date. However, if significant time has passed "
        f"or circumstances have materially changed, a court may question whether an older "
        f"certificate reflects the current situation. Fresh FDR may be advisable.</p>"
        f"<h2>Western Australia</h2>"
        + callout('If you are in Western Australia, parenting matters may proceed under the Family Court of Western Australia and section 66H of the <em>Family Court Act 1997 (WA)</em>, which has its own equivalent certificate requirement.', type='warning') +
        f"<h2>Who can issue one?</h2>"
        f"<p>Only an <a href='/questions/who-can-issue-a-section-60i-certificate/'>"
        f"accredited FDRP</a> registered with the {cite('amdras')} can issue a Section "
        f"60I certificate. Confirm accreditation before booking — a session with a "
        f"non-accredited mediator will not produce a valid certificate.</p>"
    ),
    sources=[
        ("Family Law Act 1975 (Cth) s.60I",
         "https://www.legislation.gov.au/Series/C2004A00275"),
        ("Federal Circuit and Family Court of Australia — Family Dispute Resolution",
         "https://www.fcfcoa.gov.au/fl/fdr"),
        ("Attorney-General's Department — Family Dispute Resolution",
         "https://www.ag.gov.au/families-and-marriage/families/family-dispute-resolution"),
        ("Mediator Standards Board (AMDRAS) — FDRP accreditation",
         "https://msb.org.au/"),
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

qa_page(
    slug="who-can-issue-a-section-60i-certificate",
    question="Who can issue a Section 60I certificate?",
    title="Who Can Issue a Section 60I Certificate?",
    desc="Only an accredited Family Dispute Resolution Practitioner (FDRP) registered with the Mediator Standards Board can issue a Section 60I certificate in Australia.",
    category="family",
    direct_answer=(
        "Only an accredited Family Dispute Resolution Practitioner (FDRP) registered "
        "with the Mediator Standards Board (AMDRAS) can issue a Section 60I certificate. "
        "Not all mediators hold FDRP accreditation — confirm this before booking if you "
        "need a certificate for a court application."
    ),
    body=(
        f"<h2>What is an accredited FDRP?</h2>"
        f"<p>A Family Dispute Resolution Practitioner is a mediator who has completed "
        f"specialist training and been assessed as competent to conduct family dispute "
        f"resolution under the {cite('family_law_act')}. FDRPs are registered by the "
        f"{cite('amdras')} and must meet ongoing professional development requirements.</p>"
        f"<h2>General mediators vs FDRPs</h2>"
        f"<table style='width:100%;border-collapse:collapse;margin:1rem 0'>"
        f"<thead><tr style='background:var(--surf,#f7f8fa)'>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Practitioner type</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Can issue s60I certificate?</th>"
        f"</tr></thead><tbody>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Accredited FDRP (AMDRAS registered)</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Yes</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>General mediator (not FDRP accredited)</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>No</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Family lawyer (not also an FDRP)</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>No</td></tr>"
        f"<tr><td style='padding:.6rem .8rem'>Counsellor or psychologist (not also an FDRP)</td>"
        f"<td style='padding:.6rem .8rem'>No</td></tr>"
        f"</tbody></table>"
        f"<h2>Government FDR services</h2>"
        f"<p>The {cite('fcfcoa_fdr')} operates a dispute resolution service staffed by "
        f"accredited FDRPs. Family Relationships Centres funded by the "
        f"{cite('ag_fdr')} also provide FDR with accredited practitioners — often "
        f"subsidised or free for eligible families.</p>"
        f"<h2>Private FDRPs</h2>"
        f"<p>Private accredited FDRPs — including our practitioners at Mediations "
        f"Australia — offer greater scheduling flexibility and can often see parties "
        f"sooner than subsidised services. All our mediators conducting family dispute "
        f"resolution hold current FDRP accreditation with the {cite('amdras')}.</p>"
        f"<h2>How to verify accreditation</h2>"
        f"<p>You can verify a practitioner's FDRP status through the AMDRAS register at "
        f"msb.org.au. Always confirm before booking if you need a certificate for a "
        f"court application.</p>"
    ),
    sources=[
        ("Family Law Act 1975 (Cth) s.60I",
         "https://www.legislation.gov.au/Series/C2004A00275"),
        ("Mediator Standards Board (AMDRAS) — FDRP accreditation",
         "https://msb.org.au/"),
        ("Federal Circuit and Family Court of Australia — Family Dispute Resolution",
         "https://www.fcfcoa.gov.au/fl/fdr"),
        ("Attorney-General's Department — Family Dispute Resolution",
         "https://www.ag.gov.au/families-and-marriage/families/family-dispute-resolution"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "what-is-a-section-60i-certificate",
        "do-i-need-mediation-before-family-court",
        "what-if-my-ex-refuses-mediation",
        "how-much-does-family-mediation-cost",
        "is-family-mediation-confidential",
    ],
    read_min=3,
)

qa_page(
    slug="how-much-does-family-mediation-cost",
    question="How much does family mediation cost in Australia?",
    title="How Much Does Family Mediation Cost in Australia?",
    desc="Family mediation costs $2,000–$5,000 for a full-day private session. Free options exist through government services. Far less than contested court proceedings.",
    category="family",
    direct_answer=(
        "A private family mediation session in Australia typically costs between $2,000 "
        "and $5,000 for a full day, depending on the provider and complexity. Subsidised "
        "and free options are available through Family Relationships Centres and the "
        "Federal Circuit and Family Court's dispute resolution service for eligible families."
    ),
    body=(
        f"<h2>What the cost covers</h2>"
        f"<p>The fee for a full-day family mediation session with a private accredited "
        f"FDRP typically includes the mediator's preparation, the session itself (usually "
        f"four to six hours), and a summary of any agreement reached. Legal advice, "
        f"consent orders, and separate lawyer attendance are additional.</p>"
        f"<h2>Typical cost ranges</h2>"
        f"<table style='width:100%;border-collapse:collapse;margin:1rem 0'>"
        f"<thead><tr style='background:var(--surf,#f7f8fa)'>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Service type</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Typical cost</th>"
        f"</tr></thead><tbody>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Government-subsidised FDR (Family Relationships Centre)</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Free to low-cost (income tested)</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>FCFCOA Dispute Resolution service</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Free for parties already in the court system</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Private FDRP — half day</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>$1,000–$2,500</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Private FDRP — full day</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>$2,000–$5,000</td></tr>"
        f"<tr><td style='padding:.6rem .8rem'>Contested court proceedings (per party)</td>"
        f"<td style='padding:.6rem .8rem'>$20,000–$100,000+</td></tr>"
        f"</tbody></table>"
        f"<h2>How costs are usually split</h2>"
        f"<p>Mediation costs are generally shared equally between the parties, though this "
        f"is negotiable. In court proceedings, each party typically bears their own legal "
        f"costs — one reason mediation is substantially cheaper overall even at private rates.</p>"
        f"<h2>Free and subsidised options</h2>"
        f"<p>Family Relationships Centres funded by the {cite('ag_fdr')} provide "
        f"subsidised FDR for eligible families. The {cite('fcfcoa_fdr')} also operates "
        f"a dispute resolution service for parties already in the court system. "
        f"Wait times for subsidised services can be considerably longer than private "
        f"providers.</p>"
        + callout('Our fee structure is transparent and fixed. See our <a href="/our-fee-structure/">fee page</a> for current rates, or call us to discuss your situation before committing.', type='info') +
        f"<h2>Is mediation worth it?</h2>"
        f"<p>Even at private rates, a resolved mediation costs a fraction of a contested "
        f"hearing — and most matters resolve in a single session. See our full guide: "
        f"<a href='/how-much-does-mediation-cost/'>How much does mediation cost in Australia?</a></p>"
    ),
    sources=[
        ("Federal Circuit and Family Court of Australia — filing fees",
         "https://www.fcfcoa.gov.au/fl/fees/fl-fees"),
        ("Attorney-General's Department — Family Dispute Resolution",
         "https://www.ag.gov.au/families-and-marriage/families/family-dispute-resolution"),
        ("Family Relationships Online",
         "https://www.familyrelationships.gov.au/"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "do-i-need-mediation-before-family-court",
        "what-is-a-section-60i-certificate",
        "who-can-issue-a-section-60i-certificate",
        "what-if-my-ex-refuses-mediation",
        "is-family-mediation-confidential",
    ],
    read_min=3,
)


# ── TIER 1 · PAGES 6–20 ─────────────────────────────────────

qa_page(
    slug="how-long-does-family-mediation-take",
    question="How long does family mediation take?",
    title="How Long Does Family Mediation Take?",
    desc="Most family mediation sessions are completed in a single day of four to six hours. Complex property and parenting matters may need a second session.",
    category="family",
    direct_answer=(
        "Most family mediation sessions are completed in a single day — typically four "
        "to six hours. Complex matters involving both parenting and property may require "
        "a second session, but most disputes are resolved in one appointment."
    ),
    body=(
        f"<h2>Typical session length</h2>"
        f"<p>A standard family mediation day runs from around 9 am to 3 or 4 pm, "
        f"with breaks. The first hour is usually spent on introductions and ground "
        f"rules; the remaining time is focused negotiation. Most families reach a "
        f"workable agreement before the end of the day.</p>"
        f"<h2>What affects the time?</h2>"
        f"<table style='width:100%;border-collapse:collapse;margin:1rem 0'>"
        f"<thead><tr style='background:var(--surf,#f7f8fa)'>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Factor</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Typical impact</th>"
        f"</tr></thead><tbody>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Parenting arrangements only</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Half day to full day</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Property settlement only</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Full day</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Parenting and property combined</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>One to two full days</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>High conflict or complex assets</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>May require a second session</td></tr>"
        f"<tr><td style='padding:.6rem .8rem'>Shuttle mediation (separate rooms)</td>"
        f"<td style='padding:.6rem .8rem'>Often slightly longer than joint sessions</td></tr>"
        f"</tbody></table>"
        f"<h2>How does this compare to court?</h2>"
        f"<p>A contested parenting or property matter in the {cite('fcfcoa')} typically "
        f"takes one to three years from filing to final hearing, with multiple interim "
        f"appearances along the way. Mediation resolves most matters in a single day — "
        f"and the agreement reached is binding once formalised.</p>"
        f"<h2>Preparation speeds things up</h2>"
        f"<p>Parties who arrive with a clear sense of their priorities, a completed "
        f"financial statement (for property matters), and relevant documents typically "
        f"reach agreement faster. See our "
        f"<a href='/preparing-for-mediation/'>mediation preparation tool</a> to get "
        f"ready before your session.</p>"
    ),
    sources=[
        ("Federal Circuit and Family Court of Australia — Family Dispute Resolution",
         "https://www.fcfcoa.gov.au/fl/fdr"),
        ("Attorney-General's Department — Family Dispute Resolution",
         "https://www.ag.gov.au/families-and-marriage/families/family-dispute-resolution"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "how-much-does-family-mediation-cost",
        "what-happens-during-mediation",
        "is-family-mediation-confidential",
        "do-i-need-mediation-before-family-court",
        "can-i-bring-a-lawyer-to-family-mediation",
    ],
    read_min=2,
)

qa_page(
    slug="what-happens-if-family-mediation-fails",
    question="What happens if family mediation fails?",
    title="What Happens If Family Mediation Fails?",
    desc="If family mediation fails, the FDRP issues a Section 60I certificate allowing you to apply to the Family Court. Partial agreements can still be formalised.",
    category="family",
    direct_answer=(
        "If family mediation does not result in a full agreement, the accredited FDRP "
        "issues a Section 60I certificate. This allows you to file a parenting "
        "application in the Family Court. Any partial agreements reached during "
        "mediation can still be documented and formalised."
    ),
    body=(
        f"<h2>What the FDRP does when mediation ends without agreement</h2>"
        f"<p>The {cite('fcfcoa_fdr')} requires the FDRP to issue a Section 60I "
        f"certificate recording what happened. The certificate type reflects the "
        f"reason — whether mediation was genuinely attempted, whether one party "
        f"failed to participate, or whether FDR was assessed as inappropriate.</p>"
        f"<p>That certificate is the document you file with the court to show you "
        f"have satisfied the FDR requirement under the {cite('family_law_act')}.</p>"
        f"<h2>Partial agreements still have value</h2>"
        f"<p>It is common for mediation to resolve some issues but not others — for "
        f"example, agreeing on a parenting schedule but not on the school holiday "
        f"split. Partial agreements can be documented in a <a href='/parenting-plans-guide/'>"
        f"parenting plan</a> or formalised as consent orders, reducing the number of "
        f"issues the court needs to decide.</p>"
        f"<h2>Going to court after mediation</h2>"
        f"<p>Court proceedings after a failed mediation do not start from scratch. "
        f"The issues identified during mediation often help both parties and their "
        f"lawyers understand where genuine dispute remains, which can narrow the "
        f"scope and cost of litigation.</p>"
        f"<h2>Is there anything to try before court?</h2>"
        f"<p>Yes. If mediation broke down due to communication difficulties, "
        f"<a href='/shuttle-mediation-guide/'>shuttle mediation</a> (where parties "
        f"are in separate rooms) may be worth attempting. Some matters that fail in "
        f"traditional FDR are resolved through collaborative law or with lawyers "
        f"present. We are happy to advise on next steps after an unsuccessful session.</p>"
        + callout('If mediation failed because of family violence or safety concerns, do not feel obligated to try again without appropriate safeguards. A Section 60I(8)(b) certificate can be issued where FDR is assessed as not appropriate. See our guide to <a href="/domestic-violence-and-family-law/">family violence and family law</a>.', type='alert') +
        f""
    ),
    sources=[
        ("Family Law Act 1975 (Cth) s.60I",
         "https://www.legislation.gov.au/Series/C2004A00275"),
        ("Federal Circuit and Family Court of Australia — Family Dispute Resolution",
         "https://www.fcfcoa.gov.au/fl/fdr"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "what-is-a-section-60i-certificate",
        "what-if-my-ex-refuses-mediation",
        "do-i-need-mediation-before-family-court",
        "is-family-mediation-confidential",
        "how-much-does-family-mediation-cost",
    ],
    read_min=3,
)

qa_page(
    slug="is-family-mediation-confidential",
    question="Is family mediation confidential?",
    title="Is Family Mediation Confidential?",
    desc="Yes — family mediation is confidential. What is said during FDR cannot be used as evidence in court proceedings, with narrow exceptions for safety disclosures.",
    category="family",
    direct_answer=(
        "Yes. Family mediation is confidential. Under the Family Law Act, statements "
        "made during family dispute resolution are protected — they cannot be used as "
        "evidence in court proceedings. Narrow exceptions exist for disclosures about "
        "risk of harm to a child or another person."
    ),
    body=(
        f"<h2>The legal basis for confidentiality</h2>"
        f"<p>Section 10H of the {cite('family_law_act')} provides that communications "
        f"made during FDR are inadmissible in court. This protection exists so parties "
        f"can speak candidly without fear that concessions or compromises made during "
        f"negotiation will be used against them later.</p>"
        f"<h2>What the protection covers</h2>"
        f"<ul>"
        f"<li>Statements made by either party during the mediation session</li>"
        f"<li>Documents prepared specifically for use in mediation</li>"
        f"<li>Proposals and counter-proposals exchanged during FDR</li>"
        f"<li>Admissions made in the course of negotiation</li>"
        f"</ul>"
        f"<h2>Exceptions to confidentiality</h2>"
        f"<p>The protection does not apply to:</p>"
        f"<ul>"
        f"<li>Disclosures about a risk of harm to a child</li>"
        f"<li>Disclosures about a risk of harm to another person</li>"
        f"<li>Any agreement reached in writing during or following the session</li>"
        f"<li>Information that would otherwise be admissible — confidentiality does "
        f"not protect pre-existing documents simply because they were brought to mediation</li>"
        f"</ul>"
        f"<h2>Does the mediator keep notes?</h2>"
        f"<p>The FDRP keeps session notes for their own records but these are not "
        f"disclosed to the court. The only document provided to the court is the "
        f"Section 60I certificate, which records the outcome category — not what "
        f"was said during the session.</p>"
        f"<h2>What about agreements reached in mediation?</h2>"
        f"<p>Any written agreement signed by both parties at the conclusion of "
        f"mediation is not subject to the confidentiality protection — it can be "
        f"filed as a <a href='/bfa-or-consent-orders/'>consent order</a> or "
        f"<a href='/parenting-plans-guide/'>parenting plan</a>. The confidentiality "
        f"shield protects the negotiation process, not the outcome.</p>"
    ),
    sources=[
        ("Family Law Act 1975 (Cth) s.10H — confidentiality of FDR",
         "https://www.legislation.gov.au/Series/C2004A00275"),
        ("Federal Circuit and Family Court of Australia — Family Dispute Resolution",
         "https://www.fcfcoa.gov.au/fl/fdr"),
        ("Attorney-General's Department — Family Dispute Resolution",
         "https://www.ag.gov.au/families-and-marriage/families/family-dispute-resolution"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "do-i-need-mediation-before-family-court",
        "what-happens-during-mediation",
        "is-mediation-legally-binding",
        "can-i-bring-a-lawyer-to-family-mediation",
        "what-happens-if-family-mediation-fails",
    ],
    read_min=3,
)

qa_page(
    slug="can-mediation-cover-parenting-and-property",
    question="Can mediation deal with parenting and property at the same time?",
    title="Can Mediation Cover Parenting and Property?",
    desc="Yes — mediation can resolve parenting and property settlement in one process, usually more efficient than running two separate proceedings.",
    category="family",
    direct_answer=(
        "Yes. Mediation can address both parenting arrangements and property settlement "
        "in a single process. Resolving both together is often more efficient and leads "
        "to more durable agreements, because each issue can be considered alongside "
        "the other."
    ),
    body=(
        f"<h2>Why deal with both together?</h2>"
        f"<p>Parenting and property are often interconnected. Who keeps the family "
        f"home may affect where the children live. Child support interacts with "
        f"property division. Addressing both in mediation lets parties see the full "
        f"picture and make trade-offs — something courts can struggle to facilitate "
        f"across separate proceedings.</p>"
        f"<h2>How a combined session works</h2>"
        f"<p>Our mediators structure combined sessions so that parenting is typically "
        f"addressed first — most separating parents find it easier to negotiate "
        f"finances once they have a clear picture of the co-parenting arrangement. "
        f"The session then moves to property, superannuation and any other financial "
        f"matters.</p>"
        f"<h2>Does combining them take longer?</h2>"
        f"<p>Yes — a combined parenting and property mediation typically takes a full "
        f"day and may occasionally require a second session for complex matters. "
        f"This is still considerably faster and cheaper than running two separate "
        f"court proceedings.</p>"
        f"<h2>What about the FDR certificate?</h2>"
        f"<p>The <a href='/questions/what-is-a-section-60i-certificate/'>Section 60I "
        f"certificate</a> requirement applies to parenting matters only. There is no "
        f"equivalent legal precondition for property matters — but courts expect "
        f"parties to have made genuine resolution attempts before listing a "
        f"property hearing.</p>"
        f"<h2>Formalising the agreement</h2>"
        f"<p>A parenting agreement reached in mediation can be recorded as a "
        f"<a href='/parenting-plans-guide/'>parenting plan</a> or filed as consent "
        f"orders. Property agreements are typically formalised through "
        f"<a href='/bfa-or-consent-orders/'>consent orders or a binding financial "
        f"agreement</a>. Both can be prepared after the mediation session with the "
        f"assistance of a family lawyer.</p>"
    ),
    sources=[
        ("Family Law Act 1975 (Cth)",
         "https://www.legislation.gov.au/Series/C2004A00275"),
        ("Federal Circuit and Family Court of Australia — Family Dispute Resolution",
         "https://www.fcfcoa.gov.au/fl/fdr"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "do-i-need-mediation-before-family-court",
        "how-long-does-family-mediation-take",
        "is-family-mediation-confidential",
        "how-much-does-family-mediation-cost",
        "can-i-bring-a-lawyer-to-family-mediation",
    ],
    read_min=3,
)

qa_page(
    slug="can-i-bring-a-lawyer-to-family-mediation",
    question="Can I bring a lawyer to family mediation?",
    title="Can I Bring a Lawyer to Family Mediation?",
    desc="Yes — you can bring a lawyer to family mediation as a support person or adviser. Their role is to advise you, not to advocate or negotiate on your behalf.",
    category="family",
    direct_answer=(
        "Yes, you can bring a lawyer to family mediation. Their role is to support and "
        "advise you, not to advocate or run arguments. Most FDRPs welcome lawyers who "
        "understand the mediation process and can help their client participate "
        "constructively."
    ),
    body=(
        f"<h2>What a lawyer can do in mediation</h2>"
        f"<ul>"
        f"<li>Advise you privately during breaks on the legal implications of proposed "
        f"agreements</li>"
        f"<li>Help you understand your rights and entitlements before and after the session</li>"
        f"<li>Review any draft agreement at the end of the day before you sign</li>"
        f"<li>Assist with formalising the agreement into consent orders or a binding "
        f"financial agreement after the session</li>"
        f"</ul>"
        f"<h2>What a lawyer should not do in mediation</h2>"
        f"<p>Mediation is a facilitated negotiation, not a court hearing. A lawyer who "
        f"interrupts, advocates aggressively, or turns the session into a legal argument "
        f"can undermine the process. Good mediation lawyers understand the difference "
        f"between advising a client and running a case.</p>"
        f"<h2>Does the other party need to agree?</h2>"
        f"<p>Typically, both parties should be informed if a lawyer is attending so "
        f"neither side feels ambushed. If one party has a lawyer, the other may also "
        f"wish to bring one or take independent legal advice before the session.</p>"
        f"<h2>Getting legal advice before you mediate</h2>"
        f"<p>Even if you do not bring a lawyer to the session itself, we recommend "
        f"getting independent legal advice before mediation on property matters — "
        f"particularly superannuation splitting and the range of outcomes a court "
        f"might award. This helps you negotiate from an informed position.</p>"
        f"<p>See our <a href='/family-lawyers/'>family lawyers directory</a> if you "
        f"need a referral.</p>"
    ),
    sources=[
        ("Federal Circuit and Family Court of Australia — Family Dispute Resolution",
         "https://www.fcfcoa.gov.au/fl/fdr"),
        ("Attorney-General's Department — Family Dispute Resolution",
         "https://www.ag.gov.au/families-and-marriage/families/family-dispute-resolution"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "is-family-mediation-confidential",
        "do-i-need-a-lawyer-for-mediation",
        "what-happens-during-mediation",
        "how-much-does-family-mediation-cost",
        "can-mediation-cover-parenting-and-property",
    ],
    read_min=2,
)

qa_page(
    slug="mediation-family-violence-coercive-control",
    question="Is mediation suitable where there is family violence or coercive control?",
    title="Mediation and Family Violence: Is It Suitable?",
    desc="Mediation is often not appropriate where there is family violence or coercive control. Exemptions from FDR apply, and safety must come first.",
    category="family",
    direct_answer=(
        "Mediation is often not appropriate where there is family violence or coercive "
        "control. The law recognises this: an accredited FDRP can assess FDR as "
        "unsuitable and issue a Section 60I certificate allowing court access without "
        "mediation. Safety must come first — please seek appropriate support before "
        "considering mediation."
    ),
    body=(
        callout('If you are in immediate danger, call <strong>000</strong>. For support with family violence, call <strong>1800RESPECT on 1800 737 732</strong> (24/7, free, confidential). See also our guide to <a href="/domestic-violence-and-family-law/">family violence and family law</a>.', type='alert') +
        f"<h2>Why family violence affects mediation</h2>"
        f"<p>Mediation works best when both parties can participate freely and on "
        f"reasonably equal terms. Where there is family violence or coercive control, "
        f"one party may be unable to negotiate safely or freely — meaning any agreement "
        f"reached may not reflect genuine consent.</p>"
        f"<h2>The legal exemption</h2>"
        f"<p>Under section 60I of the {cite('family_law_act')}, you are not required "
        f"to attempt FDR if there is a risk of family violence. An accredited FDRP can "
        f"issue a s60I(8)(b) certificate — which allows you to apply to the "
        f"{cite('fcfcoa')} directly without mediation — if FDR is assessed as not "
        f"appropriate in the circumstances.</p>"
        f"<h2>Can mediation ever be appropriate with DV history?</h2>"
        f"<p>In some situations — where violence is historical rather than ongoing, "
        f"safety plans are in place, and both parties genuinely consent — carefully "
        f"managed mediation with appropriate safeguards (such as "
        f"<a href='/shuttle-mediation-guide/'>shuttle mediation</a>, where parties "
        f"are in separate rooms and never meet face-to-face) may be considered. "
        f"This is a decision made carefully by the FDRP in consultation with both "
        f"parties and relevant support services — never assumed.</p>"
        f"<h2>Protective orders and mediation</h2>"
        f"<p>If an Apprehended Violence Order (AVO) or Family Violence Intervention "
        f"Order is in place, mediation may need to be conducted in a way that complies "
        f"with the order's conditions. Always disclose any existing orders to the FDRP "
        f"before a session is scheduled.</p>"
        f"<h2>Where to get help</h2>"
        f"<p>1800RESPECT (1800 737 732) offers free, confidential support 24 hours "
        f"a day. They can also help you access legal services and safety planning. "
        f"Legal Aid in your state can provide advice on your options when family "
        f"violence is present.</p>"
    ),
    sources=[
        ("Family Law Act 1975 (Cth) s.60I",
         "https://www.legislation.gov.au/Series/C2004A00275"),
        ("1800RESPECT — family and domestic violence support",
         "https://www.1800respect.org.au/"),
        ("Federal Circuit and Family Court of Australia — Family Dispute Resolution",
         "https://www.fcfcoa.gov.au/fl/fdr"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "do-i-need-mediation-before-family-court",
        "what-is-a-section-60i-certificate",
        "what-is-shuttle-mediation",
        "what-happens-if-family-mediation-fails",
        "is-family-mediation-confidential",
    ],
    read_min=3,
)

qa_page(
    slug="what-is-shuttle-mediation",
    question="What is shuttle mediation?",
    title="What Is Shuttle Mediation? | Mediations Australia",
    desc="Shuttle mediation is where parties stay in separate rooms and the mediator moves between them. It is used where face-to-face contact is difficult or unsafe.",
    category="mediation-process",
    direct_answer=(
        "Shuttle mediation is a format where the parties remain in separate rooms "
        "throughout the session and the mediator moves between them, relaying "
        "proposals and facilitating negotiation. It is used where face-to-face "
        "contact is difficult, uncomfortable, or inappropriate."
    ),
    body=(
        f"<h2>How shuttle mediation works</h2>"
        f"<p>At the start of a shuttle session, the mediator meets with each party "
        f"separately to understand their position and priorities. The mediator then "
        f"moves between the rooms, conveying offers and responses, identifying common "
        f"ground, and working toward an agreement — without the parties ever being "
        f"in the same space.</p>"
        f"<h2>When shuttle mediation is used</h2>"
        f"<ul>"
        f"<li>Where there is a history of family violence or coercive control</li>"
        f"<li>Where high conflict makes joint sessions unproductive</li>"
        f"<li>Where one or both parties find face-to-face contact distressing</li>"
        f"<li>Where a power imbalance exists between the parties</li>"
        f"<li>Online mediation — which is inherently shuttle-style by default</li>"
        f"</ul>"
        f"<h2>Shuttle vs joint mediation — which is better?</h2>"
        f"<p>Joint sessions (where both parties are in the same room) can be more "
        f"efficient and allow direct communication, which sometimes helps parties "
        f"reach more nuanced agreements. Shuttle mediation takes longer and relies "
        f"heavily on the mediator's skill in conveying proposals accurately. "
        f"The right format depends on the circumstances — your FDRP will discuss "
        f"this with you before the session.</p>"
        f"<h2>Is shuttle mediation still family dispute resolution?</h2>"
        f"<p>Yes. Shuttle mediation conducted by an accredited FDRP counts as family "
        f"dispute resolution under the {cite('family_law_act')}. A Section 60I "
        f"certificate can be issued following a shuttle session in the same way as "
        f"a joint session.</p>"
        f"<h2>Online shuttle mediation</h2>"
        f"<p>Online mediation via secure video platform is increasingly common and "
        f"offers a built-in shuttle format — each party joins from a separate "
        f"location and the mediator manages separate video calls. See our guide to "
        f"<a href='/online-mediation-australia/'>online mediation in Australia</a>.</p>"
    ),
    sources=[
        ("Family Law Act 1975 (Cth)",
         "https://www.legislation.gov.au/Series/C2004A00275"),
        ("Attorney-General's Department — Family Dispute Resolution",
         "https://www.ag.gov.au/families-and-marriage/families/family-dispute-resolution"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "mediation-family-violence-coercive-control",
        "what-happens-during-mediation",
        "is-family-mediation-confidential",
        "how-long-does-family-mediation-take",
        "do-i-need-mediation-before-family-court",
    ],
    read_min=2,
)

qa_page(
    slug="how-much-does-mediation-cost",
    question="How much does mediation cost in Australia?",
    title="How Much Does Mediation Cost in Australia?",
    desc="Mediation costs $1,500–$5,000 per session in Australia, varying by dispute type. Government subsidies apply for family matters. Court costs far more.",
    category="mediation-process",
    direct_answer=(
        "Mediation costs in Australia range from free (through government-subsidised "
        "family services) to $1,500–$5,000 for a private session, depending on the "
        "dispute type and provider. Family mediation, workplace mediation, and "
        "commercial mediation each have different typical costs."
    ),
    body=(
        f"<h2>Cost by dispute type</h2>"
        f"<table style='width:100%;border-collapse:collapse;margin:1rem 0'>"
        f"<thead><tr style='background:var(--surf,#f7f8fa)'>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Dispute type</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Private cost (approx)</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Subsidised options?</th>"
        f"</tr></thead><tbody>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Family / parenting (private FDRP)</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>$2,000–$5,000 per day</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Yes — Family Relationships Centres, FCFCOA</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Property settlement</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>$2,500–$5,000 per day</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Limited</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Workplace (employment disputes)</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>$1,500–$4,000 per day</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Fair Work Commission (conciliation)</td></tr>"
        f"<tr><td style='padding:.6rem .8rem'>Commercial / business</td>"
        f"<td style='padding:.6rem .8rem'>$3,000–$8,000+ per day</td>"
        f"<td style='padding:.6rem .8rem'>No</td></tr>"
        f"</tbody></table>"
        f"<h2>What the fee includes</h2>"
        f"<p>A private mediation fee typically covers the mediator's preparation "
        f"(reviewing documents and financial information in advance), the session "
        f"itself, and an agreement summary if the matter resolves. Legal advice, "
        f"consent orders, and lawyer attendance are separate.</p>"
        f"<h2>How costs are split</h2>"
        f"<p>Mediation costs are generally shared equally between the parties. This "
        f"is negotiable — in some commercial matters, the party that initiated the "
        f"dispute bears a larger share. In workplace matters, an employer often "
        f"covers the full cost as part of a workplace investigation or HR response.</p>"
        f"<h2>The cost of not mediating</h2>"
        f"<p>A contested family court matter typically costs $20,000–$100,000 per "
        f"party. A commercial litigation matter can run well beyond that. Mediation "
        f"resolves most matters in one day at a fraction of that cost. See our "
        f"<a href='/our-fee-structure/'>fee structure</a> for current rates.</p>"
    ),
    sources=[
        ("Federal Circuit and Family Court of Australia — filing fees",
         "https://www.fcfcoa.gov.au/fl/fees/fl-fees"),
        ("Attorney-General's Department — Family Dispute Resolution",
         "https://www.ag.gov.au/families-and-marriage/families/family-dispute-resolution"),
        ("Fair Work Commission — unfair dismissal conciliation",
         "https://www.fwc.gov.au/disputes-at-work/unfair-dismissals"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "how-much-does-family-mediation-cost",
        "how-long-does-mediation-take",
        "what-happens-during-mediation",
        "is-mediation-legally-binding",
        "do-i-need-a-lawyer-for-mediation",
    ],
    read_min=3,
)

qa_page(
    slug="how-long-does-mediation-take",
    question="How long does mediation take?",
    title="How Long Does Mediation Take? | Mediations Australia",
    desc="Most mediation sessions take four to six hours in a single day. Complex disputes may need a second session. Court proceedings take months or years.",
    category="mediation-process",
    direct_answer=(
        "Most mediation sessions are completed in a single day — typically four to "
        "six hours. Complex disputes or those involving multiple parties may need a "
        "second session. Either way, mediation resolves most disputes in days, not "
        "the months or years a court hearing can take."
    ),
    body=(
        f"<h2>Typical durations by dispute type</h2>"
        f"<table style='width:100%;border-collapse:collapse;margin:1rem 0'>"
        f"<thead><tr style='background:var(--surf,#f7f8fa)'>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Dispute type</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Typical session length</th>"
        f"</tr></thead><tbody>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Parenting arrangements</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Half day to full day</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Property settlement</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Full day</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Parenting and property combined</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>One to two full days</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Workplace dispute</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Half day to full day</td></tr>"
        f"<tr><td style='padding:.6rem .8rem'>Commercial or estate dispute</td>"
        f"<td style='padding:.6rem .8rem'>Full day, sometimes two</td></tr>"
        f"</tbody></table>"
        f"<h2>Time from booking to resolution</h2>"
        f"<p>With a private mediator, most parties can schedule a session within "
        f"one to three weeks. Government-subsidised services can have longer wait "
        f"times. Compare this to a contested family court matter, which typically "
        f"takes one to three years from filing to final hearing — and a commercial "
        f"dispute that can run longer still.</p>"
        f"<h2>What can slow mediation down?</h2>"
        f"<ul>"
        f"<li>Incomplete financial disclosure before the session</li>"
        f"<li>A party who has not received independent legal advice on their options</li>"
        f"<li>Complex asset structures or business valuations needing expert input</li>"
        f"<li>High conflict requiring shuttle format rather than joint sessions</li>"
        f"</ul>"
        f"<p>Good preparation is the single biggest factor in reducing session time. "
        f"Use our <a href='/preparing-for-mediation/'>free preparation tool</a> "
        f"before your session.</p>"
    ),
    sources=[
        ("Federal Circuit and Family Court of Australia",
         "https://www.fcfcoa.gov.au/"),
        ("Attorney-General's Department — Family Dispute Resolution",
         "https://www.ag.gov.au/families-and-marriage/families/family-dispute-resolution"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "how-much-does-mediation-cost",
        "what-happens-during-mediation",
        "how-long-does-family-mediation-take",
        "do-i-need-a-lawyer-for-mediation",
        "is-mediation-legally-binding",
    ],
    read_min=2,
)

qa_page(
    slug="what-happens-during-mediation",
    question="What happens during mediation?",
    title="What Happens During Mediation? | Mediations Australia",
    desc="During mediation a neutral mediator helps parties reach a voluntary agreement. Sessions follow four stages: opening, exploration, negotiation, and agreement.",
    category="mediation-process",
    direct_answer=(
        "During mediation, a neutral accredited mediator facilitates a structured "
        "conversation between the parties to help them reach a voluntary agreement. "
        "A typical session moves through four stages: opening and ground rules, "
        "exploration of each party's concerns, negotiation of options, and "
        "formalising any agreement reached."
    ),
    body=(
        f"<h2>The four stages of a mediation session</h2>"
        f"<p><strong>1. Opening</strong> — The mediator introduces themselves, "
        f"explains the process and ground rules, and confirms that participation is "
        f"voluntary and confidential. Each party has an opportunity to briefly "
        f"describe their situation without interruption.</p>"
        f"<p><strong>2. Exploration</strong> — The mediator helps both parties "
        f"identify the key issues, understand each other's concerns, and separate "
        f"positions (what people say they want) from interests (why they want it). "
        f"This stage often reveals unexpected common ground.</p>"
        f"<p><strong>3. Negotiation</strong> — Parties generate options and work "
        f"toward solutions. The mediator does not make decisions or take sides — "
        f"they ask questions, reality-test proposals, and help keep the conversation "
        f"productive. Private meetings (caucuses) with each party may occur.</p>"
        f"<p><strong>4. Agreement</strong> — If the parties reach agreement, the "
        f"key terms are summarised in writing before everyone leaves. This document "
        f"is then used to prepare a formal agreement (consent orders, parenting plan, "
        f"or settlement deed) after the session.</p>"
        f"<h2>What the mediator does not do</h2>"
        f"<ul>"
        f"<li>Give legal advice to either party</li>"
        f"<li>Make decisions or impose outcomes</li>"
        f"<li>Take sides or express opinions on who is right</li>"
        f"<li>Disclose what one party said to the other (in shuttle format)</li>"
        f"</ul>"
        f"<h2>Joint vs shuttle format</h2>"
        f"<p>In a joint session, both parties are in the same room throughout. In "
        f"<a href='/questions/what-is-shuttle-mediation/'>shuttle mediation</a>, "
        f"parties remain in separate rooms and the mediator moves between them. "
        f"The process is the same — only the format differs.</p>"
        f"<h2>What to bring</h2>"
        f"<p>For family and property matters, bring financial documents, a list of "
        f"assets and debts, and any relevant correspondence. Use our "
        f"<a href='/preparing-for-mediation/'>free preparation tool</a> to organise "
        f"what you need before the session.</p>"
    ),
    sources=[
        ("Federal Circuit and Family Court of Australia — Family Dispute Resolution",
         "https://www.fcfcoa.gov.au/fl/fdr"),
        ("Mediator Standards Board (AMDRAS)",
         "https://msb.org.au/"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "how-long-does-mediation-take",
        "is-family-mediation-confidential",
        "what-is-shuttle-mediation",
        "do-i-need-a-lawyer-for-mediation",
        "is-mediation-legally-binding",
    ],
    read_min=3,
)

qa_page(
    slug="do-i-need-a-lawyer-for-mediation",
    question="Do I need a lawyer for mediation?",
    title="Do I Need a Lawyer for Mediation?",
    desc="You do not need a lawyer for mediation, but independent legal advice before and after is strongly recommended for property and parenting matters.",
    category="mediation-process",
    direct_answer=(
        "You do not need a lawyer to participate in mediation — and many people "
        "mediate successfully without one present. However, independent legal advice "
        "before the session (to understand your rights) and after (to review any "
        "agreement) is strongly recommended, particularly for property and "
        "financial matters."
    ),
    body=(
        f"<h2>What a mediator cannot do</h2>"
        f"<p>The mediator is neutral and cannot give legal advice to either party. "
        f"They help facilitate the conversation — they cannot tell you whether a "
        f"proposed property split is fair, what a court would likely award, or "
        f"whether an agreement protects your interests. Only a lawyer advising you "
        f"independently can do that.</p>"
        f"<h2>Why legal advice before mediation matters</h2>"
        f"<p>Knowing your legal entitlements before you mediate helps you negotiate "
        f"from an informed position. For property matters, this includes understanding "
        f"the range of outcomes a court might order, how superannuation is split, and "
        f"whether any time limits apply. For parenting, it means understanding the "
        f"best-interests framework and what the court considers.</p>"
        f"<h2>Why legal review after mediation matters</h2>"
        f"<p>An agreement reached at mediation is not legally binding until it is "
        f"formalised — typically as <a href='/bfa-or-consent-orders/'>consent orders "
        f"or a binding financial agreement</a>. A lawyer should review the terms "
        f"before you sign, and help prepare the formal documents. Some agreements "
        f"that seem fair on the day have unintended tax, superannuation, or "
        f"enforcement consequences that a lawyer will identify.</p>"
        f"<h2>Bringing a lawyer to the session</h2>"
        f"<p>You can <a href='/questions/can-i-bring-a-lawyer-to-family-mediation/'>"
        f"bring a lawyer to mediation</a> as a support person and adviser. This is "
        f"more common in property and commercial mediations than in parenting "
        f"sessions. If one party has a lawyer present, the other may wish to "
        f"arrange the same.</p>"
        f"<h2>Where to find a family lawyer</h2>"
        f"<p>Our <a href='/family-lawyers/'>family lawyers directory</a> lists "
        f"practitioners in major Australian cities who work alongside mediators "
        f"and understand the process.</p>"
    ),
    sources=[
        ("Federal Circuit and Family Court of Australia",
         "https://www.fcfcoa.gov.au/"),
        ("Attorney-General's Department — Family Dispute Resolution",
         "https://www.ag.gov.au/families-and-marriage/families/family-dispute-resolution"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "can-i-bring-a-lawyer-to-family-mediation",
        "is-mediation-legally-binding",
        "what-happens-during-mediation",
        "is-family-mediation-confidential",
        "how-much-does-mediation-cost",
    ],
    read_min=3,
)

qa_page(
    slug="is-mediation-legally-binding",
    question="Is mediation legally binding?",
    title="Is Mediation Legally Binding? | Mediations Australia",
    desc="Mediation is not legally binding itself, but agreements can be formalised as consent orders or a binding financial agreement to become enforceable.",
    category="mediation-process",
    direct_answer=(
        "Mediation itself is not legally binding — it is a voluntary process. However, "
        "agreements reached in mediation can be made legally binding by formalising "
        "them as consent orders (filed with the court) or a binding financial "
        "agreement (signed by both parties with independent legal advice)."
    ),
    body=(
        f"<h2>The difference between the process and the outcome</h2>"
        f"<p>The mediation session is voluntary and confidential — neither party is "
        f"compelled to agree to anything. But once an agreement is reached and "
        f"properly formalised, it becomes as enforceable as any other court order "
        f"or contract.</p>"
        f"<h2>How to make a family agreement legally binding</h2>"
        f"<table style='width:100%;border-collapse:collapse;margin:1rem 0'>"
        f"<thead><tr style='background:var(--surf,#f7f8fa)'>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Agreement type</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>How it is formalised</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Legally binding?</th>"
        f"</tr></thead><tbody>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Parenting plan</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Written and signed by both parents</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Not a court order — good faith agreement</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Consent orders</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Filed with and approved by the court</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Yes — enforceable as a court order</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Binding financial agreement (BFA)</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Signed by both parties with independent legal advice</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Yes — binding contract</td></tr>"
        f"<tr><td style='padding:.6rem .8rem'>Workplace or commercial settlement deed</td>"
        f"<td style='padding:.6rem .8rem'>Signed written agreement</td>"
        f"<td style='padding:.6rem .8rem'>Yes — enforceable contract</td></tr>"
        f"</tbody></table>"
        f"<h2>What happens if someone breaks the agreement?</h2>"
        f"<p>A consent order can be enforced through the {cite('fcfcoa')} — "
        f"breach can result in fines, community service, or imprisonment for "
        f"serious contraventions. A binding financial agreement or settlement deed "
        f"can be enforced through the courts as a breach of contract.</p>"
        f"<h2>Should I get legal advice before signing?</h2>"
        f"<p>Yes — always. A lawyer should review any draft agreement before you "
        f"formalise it. For binding financial agreements, independent legal advice "
        f"is a legal requirement — without it the agreement can be set aside. "
        f"See <a href='/bfa-or-consent-orders/'>consent orders vs BFAs explained</a>.</p>"
    ),
    sources=[
        ("Family Law Act 1975 (Cth)",
         "https://www.legislation.gov.au/Series/C2004A00275"),
        ("Federal Circuit and Family Court of Australia — consent orders",
         "https://www.fcfcoa.gov.au/fl/consent-orders"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "what-happens-during-mediation",
        "do-i-need-a-lawyer-for-mediation",
        "is-family-mediation-confidential",
        "how-long-does-mediation-take",
        "how-much-does-mediation-cost",
    ],
    read_min=3,
)

qa_page(
    slug="when-should-hr-use-an-external-mediator",
    question="When should HR use an external mediator?",
    title="When Should HR Use an External Mediator?",
    desc="Use an external mediator when internal resolution fails, a conflict of interest exists, or the allegations are serious enough to require independent handling.",
    category="workplace",
    direct_answer=(
        "HR should consider an external mediator when internal resolution attempts "
        "have failed, where there is a real or perceived conflict of interest in "
        "handling the dispute internally, where the allegations are serious, or where "
        "the parties have lost confidence in the organisation's ability to resolve "
        "the matter fairly."
    ),
    body=(
        f"<h2>Signs that internal resolution is insufficient</h2>"
        f"<ul>"
        f"<li>The conflict has persisted despite informal management intervention</li>"
        f"<li>One or both parties have raised a formal grievance</li>"
        f"<li>The dispute involves a manager and a direct report (inherent power imbalance)</li>"
        f"<li>HR or a manager is named as a party or witness in the dispute</li>"
        f"<li>The matter involves bullying, harassment, or discrimination allegations</li>"
        f"<li>There is legal risk — an unfair dismissal, general protections, or "
        f"workers compensation claim has been filed or is threatened</li>"
        f"</ul>"
        f"<h2>Why external mediation helps</h2>"
        f"<p>An external mediator has no stake in the organisation's culture, "
        f"management relationships, or the outcome. Parties are more likely to speak "
        f"candidly and engage genuinely when they trust the process is independent. "
        f"External mediation also protects the employer from later claims that the "
        f"resolution process was biased.</p>"
        f"<h2>Timing matters</h2>"
        f"<p>The sooner mediation is initiated, the better. Unresolved workplace "
        f"conflict tends to escalate — affecting team morale, productivity, and "
        f"ultimately exposing the employer to {cite('fair_work')} applications, "
        f"workers compensation claims for psychological injury, and WHS regulator "
        f"scrutiny. Early mediation is almost always cheaper than late mediation.</p>"
        f"<h2>Before a Fair Work application is filed</h2>"
        f"<p>If an employee is considering an unfair dismissal or general protections "
        f"application, external mediation before the filing deadline can resolve the "
        f"matter without litigation. Once an application is filed, the "
        f"{cite('fair_work')} conducts its own conciliation — but the parties have "
        f"less control over the process and timing.</p>"
        f"<h2>Confidentiality in workplace mediation</h2>"
        f"<p>External mediators are bound by confidentiality. What is said in the "
        f"mediation session cannot be used in subsequent proceedings — this allows "
        f"frank discussion and genuine compromise without the risk of admissions "
        f"being used against either party.</p>"
    ),
    sources=[
        ("Fair Work Commission — unfair dismissal and dispute resolution",
         "https://www.fwc.gov.au/disputes-at-work/unfair-dismissals"),
        ("Safe Work Australia — managing psychosocial hazards",
         "https://www.safeworkaustralia.gov.au/safety-topic/hazards/mental-health"),
        ("Fair Work Ombudsman",
         "https://www.fairwork.gov.au/"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "workplace-investigation-vs-mediation",
        "is-workplace-mediation-confidential",
        "how-much-does-mediation-cost",
        "what-happens-during-mediation",
        "is-mediation-legally-binding",
    ],
    read_min=3,
)

qa_page(
    slug="workplace-investigation-vs-mediation",
    question="Workplace investigation vs mediation: what's the difference?",
    title="Workplace Investigation vs Mediation: The Difference",
    desc="A workplace investigation determines facts. Mediation helps parties reach a voluntary resolution. They serve different purposes and are not interchangeable.",
    category="workplace",
    direct_answer=(
        "A workplace investigation is a formal fact-finding process that produces "
        "findings and recommendations — it determines what happened. Mediation is a "
        "facilitated negotiation that helps parties reach a voluntary agreement — it "
        "resolves the relationship going forward. They serve different purposes and "
        "are sometimes used together."
    ),
    body=(
        f"<h2>Key differences</h2>"
        f"<table style='width:100%;border-collapse:collapse;margin:1rem 0'>"
        f"<thead><tr style='background:var(--surf,#f7f8fa)'>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'></th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Investigation</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Mediation</th>"
        f"</tr></thead><tbody>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb);font-weight:600'>Purpose</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Determine facts</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Resolve the dispute</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb);font-weight:600'>Process</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Investigator interviews witnesses, reviews evidence</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Mediator facilitates negotiation between parties</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb);font-weight:600'>Outcome</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Findings of fact, recommendations</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Voluntary agreement between parties</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb);font-weight:600'>Confidential?</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Report may be disclosed to parties</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Fully confidential</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;font-weight:600'>Voluntary?</td>"
        f"<td style='padding:.6rem .8rem'>Employer-directed; parties must participate</td>"
        f"<td style='padding:.6rem .8rem'>Voluntary — both parties must agree to participate</td></tr>"
        f"</tbody></table>"
        f"<h2>When to investigate vs when to mediate</h2>"
        f"<p>An investigation is appropriate where there are serious allegations "
        f"that need to be established as fact before any action is taken — for "
        f"example, allegations of serious misconduct, harassment, or fraud that "
        f"may lead to disciplinary action or termination.</p>"
        f"<p>Mediation is appropriate where the primary goal is to repair a "
        f"working relationship, resolve an ongoing conflict, or reach a settlement "
        f"— even where some fault is acknowledged. It is also useful where an "
        f"investigation would be disproportionate to the seriousness of the issue.</p>"
        f"<h2>Can you do both?</h2>"
        f"<p>Yes — and sometimes it is the right sequence. An investigation may "
        f"establish findings that then provide the basis for a mediated resolution "
        f"of the employment relationship. Alternatively, mediation may be attempted "
        f"first, and an investigation initiated only if mediation does not resolve "
        f"the matter. The right sequence depends on the nature and seriousness of "
        f"the allegations.</p>"
        f"<p>Our <a href='/workplace-mediation/'>workplace mediation service</a> "
        f"includes advice on which process is appropriate for your situation.</p>"
    ),
    sources=[
        ("Fair Work Commission — dispute resolution",
         "https://www.fwc.gov.au/disputes-at-work"),
        ("Safe Work Australia — managing psychosocial hazards",
         "https://www.safeworkaustralia.gov.au/safety-topic/hazards/mental-health"),
        ("Fair Work Ombudsman",
         "https://www.fairwork.gov.au/"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "when-should-hr-use-an-external-mediator",
        "is-workplace-mediation-confidential",
        "is-mediation-legally-binding",
        "what-happens-during-mediation",
        "how-much-does-mediation-cost",
    ],
    read_min=3,
)

qa_page(
    slug="is-workplace-mediation-confidential",
    question="Is workplace mediation confidential?",
    title="Is Workplace Mediation Confidential?",
    desc="Yes. Workplace mediation is confidential. What is said in the session cannot be used in subsequent proceedings, with narrow safety exceptions.",
    category="workplace",
    direct_answer=(
        "Yes. Workplace mediation is confidential. What is said during the session "
        "cannot be used as evidence in subsequent legal proceedings. Both parties "
        "and the mediator are bound by confidentiality, which allows frank "
        "discussion and genuine compromise without risk of admissions being used "
        "against either party."
    ),
    body=(
        f"<h2>What confidentiality covers</h2>"
        f"<ul>"
        f"<li>Statements made by either party during the session</li>"
        f"<li>Documents shared specifically for use in mediation</li>"
        f"<li>Offers and counter-offers exchanged during negotiation</li>"
        f"<li>The mediator's own notes from the session</li>"
        f"</ul>"
        f"<h2>What it does not cover</h2>"
        f"<ul>"
        f"<li>The fact that mediation occurred (though parties can agree to keep "
        f"this confidential too)</li>"
        f"<li>Pre-existing documents — bringing a document to mediation does not "
        f"make it confidential if it was already discoverable</li>"
        f"<li>Any written settlement agreement — this is the exception. The agreement "
        f"itself is not confidential and can be enforced as a contract</li>"
        f"</ul>"
        f"<h2>Why confidentiality matters in workplace disputes</h2>"
        f"<p>Employees are more likely to speak candidly about workplace grievances "
        f"if they know their words cannot be quoted in a {cite('fair_work')} "
        f"proceeding or used in a subsequent unfair dismissal application. Employers "
        f"are more willing to explore flexible settlements when they know a concession "
        f"in mediation cannot be used as an admission in litigation.</p>"
        f"<h2>Can the employer share the outcome?</h2>"
        f"<p>Parties can agree to keep the outcome confidential as part of the "
        f"settlement — this is common where the resolution involves a financial "
        f"payment or agreed separation. The settlement agreement typically includes "
        f"a confidentiality clause binding both parties.</p>"
        f"<h2>What about workplace investigations?</h2>"
        f"<p>A workplace investigation is not confidential in the same way — the "
        f"employer directs the process and the findings are reported. If you are "
        f"unsure whether an investigation or mediation is more appropriate, see our "
        f"comparison: <a href='/questions/workplace-investigation-vs-mediation/'>"
        f"workplace investigation vs mediation</a>.</p>"
    ),
    sources=[
        ("Fair Work Commission — dispute resolution",
         "https://www.fwc.gov.au/disputes-at-work"),
        ("Fair Work Ombudsman",
         "https://www.fairwork.gov.au/"),
        ("Mediator Standards Board (AMDRAS)",
         "https://msb.org.au/"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "when-should-hr-use-an-external-mediator",
        "workplace-investigation-vs-mediation",
        "is-mediation-legally-binding",
        "is-family-mediation-confidential",
        "what-happens-during-mediation",
    ],
    read_min=3,
)


# ─────────────────────────────────────────────
# Build runner
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print(f"\nBuilding {len(QUESTION_REGISTRY)} Q&A page(s)...")
    print(f"Output: {OUT}/questions/")
    print(f"Review date: {REVIEW_DATE}")
    print(f"\nDone. {len(QUESTION_REGISTRY)} page(s) written.\n")
