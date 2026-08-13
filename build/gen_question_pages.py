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


# ─────────────────────────────────────────────
# Build runner
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print(f"\nBuilding {len(QUESTION_REGISTRY)} Q&A page(s)...")
    print(f"Output: {OUT}/questions/")
    print(f"Review date: {REVIEW_DATE}")
    print(f"\nDone. {len(QUESTION_REGISTRY)} page(s) written.\n")
