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
    return (
        f'<aside style="margin-top:3rem;padding:1.5rem;background:var(--surf,#f7f8fa);'
        f'border-radius:10px;border:1px solid var(--border,#e5e7eb)">'
        f'<p style="font-size:.75rem;text-transform:uppercase;letter-spacing:.08em;'
        f'color:var(--muted,#6b7280);margin:0 0 1rem">About the expert</p>'
        f'<div style="display:flex;gap:1.25rem;align-items:flex-start">'
        f'<img src="/images/Dan-Bio.png" alt="Dan Toombs — Founder, Mediations Australia" '
        f'width="80" height="80" loading="lazy" '
        f'style="border-radius:50%;flex-shrink:0;object-fit:cover;width:80px;height:80px">'
        f'<div>'
        f'<p style="font-weight:700;margin:0 0 .15rem;font-size:1rem">Dan Toombs</p>'
        f'<p style="margin:0 0 .75rem;color:var(--muted,#6b7280);font-size:.875rem">'
        f'Founder, Mediations Australia</p>'
        f'<p style="margin:0 0 .75rem;font-size:.9rem;line-height:1.6">'
        f'Dan Toombs is the Founder of Mediations Australia, an award-winning lawyer, '
        f'former Tribunal Member and nationally accredited mediator (AMDRAS). His career '
        f'spans law, adjudication and organisational leadership, giving him particular '
        f'insight into the systemic, structural and human dynamics that drive complex '
        f'disputes. A recipient of the National Human Rights Law Award and a Winston '
        f'Churchill Fellow, Dan brings legal expertise, strategic insight and practical '
        f'judgment to dispute resolution.</p>'
        f'<a href="https://www.mediationsaustralia.com.au/our-team/dan-toombs/" '
        f'style="font-size:.875rem;font-weight:600">View Dan Toombs’ profile &rarr;</a>'
        f'</div></div>'
        f'<p style="margin:1rem 0 0;font-size:.8rem;color:var(--muted,#6b7280)">'
        f'Last reviewed {REVIEW_DATE}</p>'
        f'</aside>'
    )


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
# ── TIER 2 · PAGES 21–35 ────────────────────────────────────────────────────

qa_page(
    slug="what-is-family-dispute-resolution",
    question="What is Family Dispute Resolution?",
    title="What Is Family Dispute Resolution (FDR)?",
    desc="FDR is a structured mediation process for separating parents. Most parents must attempt FDR before filing parenting matters in the Family Court.",
    category="family",
    direct_answer=(
        "Family Dispute Resolution (FDR) is a structured, confidential mediation process "
        "designed to help separating parents resolve disputes about their children without "
        "going to court. Under the Family Law Act 1975, most parents must attempt FDR "
        "before they can apply to the Family Court for parenting orders."
    ),
    body=(
        f"<h2>What happens in FDR?</h2>"
        f"<p>FDR is facilitated by an accredited Family Dispute Resolution Practitioner (FDRP). "
        f"The FDRP does not take sides or make decisions — they help the parties communicate, "
        f"identify what each person needs, and work toward an agreement about parenting "
        f"arrangements. FDR sessions are confidential and what is said cannot generally "
        f"be used in court proceedings.</p>"
        f"<p>FDR can be conducted with both parties in the same room (joint session) or in "
        f"separate rooms with the FDRP moving between them "
        f"(<a href='/questions/what-is-shuttle-mediation/'>shuttle mediation</a>). "
        f"It is also available online.</p>"
        f"<h2>FDR vs ordinary mediation</h2>"
        f"<p>FDR is a specific type of mediation defined by the {cite('family_law_act')} and "
        f"regulated by the {cite('fcfcoa_fdr')} accreditation scheme. The key difference is "
        f"that <strong>only an accredited FDRP can issue a Section 60I certificate</strong> — "
        f"the document required to file a parenting application in the Family Court. A general "
        f"mediator, lawyer, or counsellor cannot issue this certificate. See our separate guide: "
        f"<a href='/questions/whats-the-difference-between-mediation-and-family-dispute-resolution/'>"
        f"mediation vs FDR</a>.</p>"
        f"<h2>What FDR covers</h2>"
        f"<p>FDR addresses parenting and children's matters — where children live, time spent "
        f"with each parent, communication, schooling, and similar arrangements. It does not "
        f"cover property or financial matters, which are dealt with through separate "
        f"mediation or court proceedings.</p>"
        f"<h2>Who provides FDR?</h2>"
        f"<p>FDR is provided by:</p>"
        f"<ul>"
        f"<li><strong>Family Relationships Centres</strong> — government-funded, subsidised "
        f"or free for eligible families. Wait times can be longer.</li>"
        f"<li><strong>Private FDRPs</strong> — faster access, typically at cost. The fee is "
        f"usually shared between the parties.</li>"
        f"<li><strong>The {cite('fcfcoa')}</strong> — provides FDR as part of its dispute "
        f"resolution services.</li>"
        f"</ul>"
        f"<h2>What if FDR doesn't resolve the dispute?</h2>"
        f"<p>If FDR is unsuccessful, the FDRP issues a "
        f"<a href='/questions/what-is-a-section-60i-certificate/'>Section 60I certificate</a> "
        f"recording the outcome. That certificate is then filed with the court to show the "
        f"FDR requirement has been satisfied. Any partial agreement reached during FDR can "
        f"be documented and formalised as consent orders or a parenting plan.</p>"
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
        "whats-the-difference-between-mediation-and-family-dispute-resolution",
        "what-is-a-section-60i-certificate",
        "do-i-need-mediation-before-family-court",
        "who-can-issue-a-section-60i-certificate",
        "is-family-mediation-confidential",
    ],
    read_min=3,
)

qa_page(
    slug="whats-the-difference-between-mediation-and-family-dispute-resolution",
    question="What's the difference between mediation and Family Dispute Resolution?",
    title="Mediation vs Family Dispute Resolution: The Difference",
    desc="FDR is a specific type of mediation under the Family Law Act. Only an accredited FDRP can issue the Section 60I certificate the Family Court requires.",
    category="family",
    direct_answer=(
        "Family Dispute Resolution (FDR) is a specific type of mediation defined by the "
        "Family Law Act 1975. The key practical difference is the certificate: only an "
        "accredited FDRP can issue the Section 60I certificate required to file parenting "
        "proceedings in the Family Court. A general mediator cannot issue this certificate, "
        "even if they conduct an identical process."
    ),
    body=(
        f"<h2>What they have in common</h2>"
        f"<p>Both mediation and FDR are facilitated, confidential processes in which a "
        f"neutral practitioner helps parties communicate and reach agreement. Both are "
        f"voluntary in the sense that neither party is forced to agree to anything. Both "
        f"are generally faster and less expensive than court proceedings.</p>"
        f"<h2>The critical difference: accreditation and the Section 60I certificate</h2>"
        f"<table style='width:100%;border-collapse:collapse;margin:1rem 0'>"
        f"<thead><tr style='background:var(--surf,#f7f8fa)'>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Feature</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>FDR</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>General mediation</th>"
        f"</tr></thead><tbody>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Defined by legislation?</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Yes — Family Law Act 1975</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>No — general practice</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Practitioner must be accredited?</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Yes — FDRP accreditation required</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>No mandatory accreditation</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Can issue Section 60I certificate?</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Yes</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>No</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Required before Family Court parenting application?</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Yes (unless exempt)</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>No</td></tr>"
        f"<tr><td style='padding:.6rem .8rem'>Covers property matters?</td>"
        f"<td style='padding:.6rem .8rem'>No — parenting only</td>"
        f"<td style='padding:.6rem .8rem'>Yes — any type of dispute</td></tr>"
        f"</tbody></table>"
        f"<h2>Does the label matter?</h2>"
        f"<p>In practice, many FDRPs also conduct general mediation — for property, commercial, "
        f"or workplace disputes — and many general mediators are also accredited FDRPs. The "
        f"label matters only when you need a Section 60I certificate for court. Always confirm "
        f"that your practitioner holds current FDRP accreditation if a court certificate "
        f"may be needed. You can verify accreditation through the {cite('amdras')}.</p>"
        f"<h2>When to choose each</h2>"
        f"<ul>"
        f"<li>Use an accredited <strong>FDRP</strong> for parenting and children's matters "
        f"where a Section 60I certificate may be required.</li>"
        f"<li>Use a <strong>mediator</strong> (FDRP or otherwise) for property, financial, "
        f"or other disputes where no certificate is needed.</li>"
        f"<li>For combined parenting and property matters, choose an accredited FDRP who "
        f"also has experience in property mediation — they can cover both.</li>"
        f"</ul>"
    ),
    sources=[
        ("Family Law Act 1975 (Cth) s.60I",
         "https://www.legislation.gov.au/Series/C2004A00275"),
        ("Mediator Standards Board (AMDRAS) — FDRP accreditation",
         "https://msb.org.au/"),
        ("Federal Circuit and Family Court of Australia — Family Dispute Resolution",
         "https://www.fcfcoa.gov.au/fl/fdr"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "what-is-family-dispute-resolution",
        "who-can-issue-a-section-60i-certificate",
        "what-is-a-section-60i-certificate",
        "do-i-need-mediation-before-family-court",
        "what-happens-during-mediation",
    ],
    read_min=3,
)

qa_page(
    slug="when-can-i-be-exempt-from-family-dispute-resolution",
    question="When can I be exempt from Family Dispute Resolution?",
    title="Exemptions From Family Dispute Resolution (FDR)",
    desc="FDR exemptions apply where there is family violence, urgency, the other party cannot be located, or an FDRP assesses FDR as unsuitable.",
    category="family",
    direct_answer=(
        "You are exempt from the FDR requirement under the Family Law Act if there is "
        "a risk of family violence or abuse, the matter is urgent, the other party "
        "cannot be located, or an accredited FDRP assesses FDR as not appropriate in "
        "the circumstances. An exemption means you can file parenting proceedings "
        "without a Section 60I certificate."
    ),
    body=(
        callout('If you are in immediate danger, call <strong>000</strong>. For family violence support call <strong>1800RESPECT on 1800 737 732</strong> (free, 24/7). See also our guide to <a href="/domestic-violence-and-family-law/">family violence and family law</a>.', type='alert') +
        f"<h2>The exemptions under the Family Law Act</h2>"
        f"<p>Section 60I(9) of the {cite('family_law_act')} lists the circumstances in which "
        f"a parenting application can be filed without a Section 60I certificate:</p>"
        f"<table style='width:100%;border-collapse:collapse;margin:1rem 0'>"
        f"<thead><tr style='background:var(--surf,#f7f8fa)'>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Exemption</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>What it covers</th>"
        f"</tr></thead><tbody>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'><strong>Family violence or abuse</strong></td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>A risk of family violence to a party or child, or abuse of a child. No FDR attempt required.</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'><strong>Urgency</strong></td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>The matter is urgent — for example, a child is at immediate risk of harm or removal from Australia.</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'><strong>Other party cannot be located</strong></td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>The other party's whereabouts are unknown and cannot be established.</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'><strong>FDRP assessment as unsuitable</strong></td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>An accredited FDRP has assessed FDR as not appropriate — they issue an s60I(8)(b) certificate.</td></tr>"
        f"<tr><td style='padding:.6rem .8rem'><strong>Contravention proceedings</strong></td>"
        f"<td style='padding:.6rem .8rem'>The application is about a contravention of an existing parenting order.</td></tr>"
        f"</tbody></table>"
        f"<h2>How to use an exemption</h2>"
        f"<p>If an exemption applies, you do not need to attempt FDR or obtain a Section 60I "
        f"certificate before filing. You will typically need to file a supporting document or "
        f"affidavit with the {cite('fcfcoa')} explaining why the exemption applies. The court "
        f"then decides whether the exemption is made out.</p>"
        f"<h2>Family violence: no FDR attempt required</h2>"
        f"<p>The family violence exemption is the most commonly used. You do not need to attempt "
        f"FDR or contact an FDRP before filing — the exemption applies directly. If you are "
        f"unsure whether the circumstances qualify, seek legal advice before filing.</p>"
        f"<h2>FDRP assessment as unsuitable</h2>"
        f"<p>If you contact an accredited FDRP and they assess FDR as not appropriate — for "
        f"example, because of a power imbalance, family violence history, or another party's "
        f"incapacity — they will issue an s60I(8)(b) certificate. This certificate allows "
        f"you to file parenting proceedings without FDR having been attempted.</p>"
        f"<p>See also: <a href='/questions/can-i-get-a-s60i-certificate-without-attending-mediation/'>"
        f"Can I get a Section 60I certificate without attending mediation?</a></p>"
    ),
    sources=[
        ("Family Law Act 1975 (Cth) s.60I(9)",
         "https://www.legislation.gov.au/Series/C2004A00275"),
        ("Federal Circuit and Family Court of Australia — Family Dispute Resolution",
         "https://www.fcfcoa.gov.au/fl/fdr"),
        ("1800RESPECT — family violence support",
         "https://www.1800respect.org.au/"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "do-i-need-mediation-before-family-court",
        "what-is-a-section-60i-certificate",
        "can-i-get-a-s60i-certificate-without-attending-mediation",
        "mediation-family-violence-coercive-control",
        "what-if-my-ex-refuses-mediation",
    ],
    read_min=3,
)

qa_page(
    slug="can-i-get-a-s60i-certificate-without-attending-mediation",
    question="Can I get a Section 60I certificate without attending mediation?",
    title="Section 60I Certificate Without Attending Mediation",
    desc="Yes — a Section 60I certificate can be issued without attending mediation if FDR is assessed as unsuitable, the other party refuses, or an exemption applies.",
    category="family",
    direct_answer=(
        "Yes. A Section 60I certificate can be issued without attending a full mediation "
        "session. An accredited FDRP can issue the certificate if they assess FDR as not "
        "appropriate, if the other party refuses to attend, or if one party does not make "
        "a genuine effort. In family violence or urgency situations, you may not need a "
        "certificate at all."
    ),
    body=(
        f"<h2>Certificate types that don't require completing mediation</h2>"
        f"<p>Under section 60I of the {cite('family_law_act')}, an accredited FDRP can issue "
        f"five different certificate types. Three of them do not require a completed "
        f"mediation session:</p>"
        f"<table style='width:100%;border-collapse:collapse;margin:1rem 0'>"
        f"<thead><tr style='background:var(--surf,#f7f8fa)'>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Certificate type</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>When issued</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Mediation required?</th>"
        f"</tr></thead><tbody>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>s60I(8)(a)</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Other party did not attend</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>No</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>s60I(8)(b)</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>FDRP assessed FDR as not appropriate</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>No</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>s60I(8)(c)</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>One party did not make a genuine effort</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Session started but may not be completed</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>s60I(8)(d)</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>FDR started but not completed</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Partial session only</td></tr>"
        f"<tr><td style='padding:.6rem .8rem'>s60I(8)(aa)</td>"
        f"<td style='padding:.6rem .8rem'>Mediation attended, genuine effort by all parties</td>"
        f"<td style='padding:.6rem .8rem'>Yes — full session</td></tr>"
        f"</tbody></table>"
        f"<h2>What the FDRP intake process involves</h2>"
        f"<p>Before booking a full FDR session, an FDRP conducts an intake assessment — "
        f"separate appointments with each party to assess the suitability of FDR. If at "
        f"this stage the FDRP assesses FDR as not appropriate (for example, due to family "
        f"violence, a significant power imbalance, or one party's incapacity), they can "
        f"issue an s60I(8)(b) certificate without a full session ever taking place.</p>"
        f"<h2>What if the other party simply refuses to come?</h2>"
        f"<p>If you make a genuine effort to initiate FDR and the other party refuses to "
        f"attend, the FDRP can issue an s60I(8)(a) certificate. This certificate satisfies "
        f"the court requirement — you are not penalised for the other party's refusal. "
        f"See also: <a href='/questions/what-if-my-ex-refuses-mediation/'>"
        f"what if my ex refuses mediation?</a></p>"
        f"<h2>When no certificate is needed at all</h2>"
        f"<p>If an exemption applies — family violence, urgency, or the other party cannot "
        f"be located — you may file parenting proceedings without any certificate. See: "
        f"<a href='/questions/when-can-i-be-exempt-from-family-dispute-resolution/'>"
        f"FDR exemptions</a>.</p>"
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
        "who-can-issue-a-section-60i-certificate",
        "when-can-i-be-exempt-from-family-dispute-resolution",
        "what-if-my-ex-refuses-mediation",
        "do-i-need-mediation-before-family-court",
    ],
    read_min=3,
)

qa_page(
    slug="how-long-is-a-s60i-certificate-valid",
    question="How long is a Section 60I certificate valid?",
    title="How Long Is a Section 60I Certificate Valid?",
    desc="The Court states a Section 60I certificate is valid for 12 months. Seek legal advice before filing if your certificate is older than 12 months.",
    category="family",
    direct_answer=(
        "There is no legislated expiry period for a Section 60I certificate — the Family "
        "Law Act 1975 does not set a time limit. The Court currently states a s60I "
        "certificate is valid for 12 months, so use a recent certificate wherever "
        "possible. If significant time has passed, seek legal advice before filing."
    ),
    body=(
        callout('The <a href="https://www.fcfcoa.gov.au">Federal Circuit and Family Court of Australia</a> currently states that a Section 60I certificate is valid for 12 months. If your certificate is older than 12 months, seek legal advice before filing your parenting application.', type='warning') +
        f"<h2>What the legislation says</h2>"
        f"<p>Section 60I of the {cite('family_law_act')} requires a certificate to be filed "
        f"with a parenting application. The legislation itself does not specify an expiry "
        f"date — however, the {cite('fcfcoa')} states that certificates are valid for "
        f"12 months from the date of issue.</p>"
        f"<h2>Practical guidance</h2>"
        f"<p>If you received a Section 60I certificate some time ago and have not yet filed, "
        f"seek legal advice before doing so. Your lawyer can advise whether the court is "
        f"likely to accept the existing certificate or whether a fresh FDR attempt is "
        f"advisable in your circumstances.</p>"
        f"<p>If circumstances have changed significantly since the certificate was issued "
        f"— for example, new family violence concerns, a change in the child's living "
        f"arrangements, or a material change in either party's situation — a fresh FDR "
        f"attempt may be more productive regardless of whether the certificate is still "
        f"within the 12-month window.</p>"
        f"<h2>Certificate types and their context</h2>"
        f"<p>The certificate records the <em>type</em> of outcome from FDR — whether "
        f"mediation was genuinely attempted, whether a party refused, or whether FDR was "
        f"assessed as unsuitable. Courts can and do consider the certificate type when "
        f"dealing with cost applications. A certificate showing one party did not make "
        f"a genuine effort (s60I(8)(c)) can be taken into account in costs orders against "
        f"that party.</p>"
        f"<h2>WA — different rules apply</h2>"
        f"<p>In Western Australia, family law matters involving children are governed by "
        f"the Family Court Act 1997 (WA) and section 66H, not s.60I of the Commonwealth "
        f"Act. The certificate requirements may differ. Always confirm the applicable rules "
        f"with a WA family lawyer if you are filing in the Family Court of Western Australia.</p>"
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
        "who-can-issue-a-section-60i-certificate",
        "can-i-get-a-s60i-certificate-without-attending-mediation",
        "do-i-need-mediation-before-family-court",
        "what-happens-if-family-mediation-fails",
    ],
    read_min=2,
)

qa_page(
    slug="can-grandparents-use-family-mediation",
    question="Can grandparents use family mediation?",
    title="Can Grandparents Use Family Mediation?",
    desc="Yes — grandparents can use family mediation to resolve disputes about time with grandchildren, and usually need FDR before applying to the Family Court.",
    category="family",
    direct_answer=(
        "Yes. Grandparents can use family mediation — and in most cases should, before "
        "applying to the Family Court for contact orders. Mediation gives grandparents "
        "an opportunity to reach an agreed arrangement with the child's parents without "
        "the cost and delay of court proceedings."
    ),
    body=(
        f"<h2>Grandparents' rights and mediation</h2>"
        f"<p>Under the {cite('family_law_act')}, grandparents are among the people who "
        f"can apply to the {cite('fcfcoa')} for parenting orders — including orders about "
        f"the time they spend with their grandchildren. Before making such an application, "
        f"grandparents are generally required to attempt "
        f"<a href='/questions/what-is-family-dispute-resolution/'>Family Dispute "
        f"Resolution (FDR)</a>.</p>"
        f"<h2>Who attends mediation?</h2>"
        f"<p>Typically, the grandparent(s) and the child's parents. In some cases, other "
        f"family members may also be involved. The mediator facilitates discussion about "
        f"what arrangements would be in the child's best interests — which is the paramount "
        f"consideration under the Family Law Act.</p>"
        f"<h2>Is mediation required before grandparents can go to court?</h2>"
        f"<p>Generally yes. The FDR requirement applies to most parenting applications, "
        f"including those made by grandparents. Exemptions exist (family violence, urgency, "
        f"the other party cannot be located) — see our guide to "
        f"<a href='/questions/when-can-i-be-exempt-from-family-dispute-resolution/'>"
        f"FDR exemptions</a>.</p>"
        f"<h2>What mediation can achieve for grandparents</h2>"
        f"<p>Mediation can result in an agreed arrangement for regular contact — specific "
        f"days, school holiday time, phone calls, or video chats. This agreement can be "
        f"documented as a parenting plan or formalised as consent orders, giving it legal "
        f"standing without the cost and adversarial nature of a contested court application.</p>"
        f"<h2>What if a parent refuses to engage?</h2>"
        f"<p>If a parent refuses to attend FDR, the FDRP can issue a Section 60I certificate "
        f"recording the refusal. This satisfies the court requirement and allows the grandparent "
        f"to file a parenting application. See: "
        f"<a href='/questions/can-i-get-a-s60i-certificate-without-attending-mediation/'>"
        f"getting a certificate without completing mediation</a>.</p>"
        f"<h2>Costs</h2>"
        f"<p>Private FDRP fees are usually shared between the parties, but in grandparent "
        f"matters the cost is sometimes borne by the grandparent as the initiating party. "
        f"Subsidised FDR through Family Relationships Centres is available for grandparent "
        f"matters. See our full guide to <a href='/grandparents-rights/'>grandparents' rights</a>.</p>"
    ),
    sources=[
        ("Family Law Act 1975 (Cth)",
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
        "what-is-family-dispute-resolution",
        "when-can-i-be-exempt-from-family-dispute-resolution",
        "can-i-get-a-s60i-certificate-without-attending-mediation",
        "what-is-a-section-60i-certificate",
    ],
    read_min=2,
)

qa_page(
    slug="can-we-make-a-parenting-plan-at-mediation",
    question="Can we make a parenting plan at mediation?",
    title="Can We Make a Parenting Plan at Mediation?",
    desc="Yes — a parenting plan can be drafted and signed at mediation. It is not a court order, but formally records both parents' agreed arrangements.",
    category="family",
    direct_answer=(
        "Yes. A parenting plan can be drafted and signed at the conclusion of a successful "
        "mediation session. A parenting plan is a written agreement between parents — it is "
        "not a court order, but it is a formal document that records both parents' intentions "
        "and can be used as the basis for consent orders if the parties wish to make it "
        "legally enforceable."
    ),
    body=(
        f"<h2>What is a parenting plan?</h2>"
        f"<p>A parenting plan is a written agreement made under the {cite('family_law_act')} "
        f"between the parents of a child. It covers how parenting responsibilities will be "
        f"shared — including where the child lives, time with each parent, education, health, "
        f"and communication. It does not need to be filed with a court.</p>"
        f"<h2>How a parenting plan is made at mediation</h2>"
        f"<p>If parents reach agreement during mediation, the key terms are typically "
        f"summarised in writing before the session ends. Both parents sign the document "
        f"at the conclusion of the session. This summary then becomes the parenting plan "
        f"— or the basis for a more detailed plan prepared by a family lawyer.</p>"
        f"<p>Some FDRPs assist parties in drafting the plan during the session; others "
        f"provide a record of agreement that the parties then take to lawyers to formalise. "
        f"Discuss with your FDRP what documentation they provide at the end of a session.</p>"
        f"<h2>Is a parenting plan legally binding?</h2>"
        f"<p>A parenting plan is not a court order — it cannot be directly enforced through "
        f"the court if one parent breaches it. However:</p>"
        f"<ul>"
        f"<li>If one parent consistently departs from the parenting plan, the court can "
        f"take this into account in subsequent proceedings</li>"
        f"<li>A parenting plan can be used as the basis for consent orders, which are "
        f"legally enforceable</li>"
        f"<li>A later parenting plan supersedes an earlier one under the Family Law Act</li>"
        f"</ul>"
        f"<h2>Parenting plan vs consent orders — which is better?</h2>"
        f"<table style='width:100%;border-collapse:collapse;margin:1rem 0'>"
        f"<thead><tr style='background:var(--surf,#f7f8fa)'>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'></th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Parenting plan</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Consent orders</th>"
        f"</tr></thead><tbody>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Requires court filing?</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>No</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Yes</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Legally enforceable?</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>No — good faith only</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Yes — court order</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Cost to create?</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Low</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Moderate (legal drafting + filing fee ~$195)</td></tr>"
        f"<tr><td style='padding:.6rem .8rem'>Best for?</td>"
        f"<td style='padding:.6rem .8rem'>Cooperative parents; arrangements likely to change</td>"
        f"<td style='padding:.6rem .8rem'>Where certainty and enforceability are needed</td></tr>"
        f"</tbody></table>"
        f"<p>Our guide to <a href='/parenting-plans-guide/'>parenting plans in Australia</a> "
        f"covers what to include and when to upgrade to consent orders.</p>"
    ),
    sources=[
        ("Family Law Act 1975 (Cth) s.63C — parenting plans",
         "https://www.legislation.gov.au/Series/C2004A00275"),
        ("Federal Circuit and Family Court of Australia — parenting plans",
         "https://www.fcfcoa.gov.au/fl/pip"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "what-happens-during-mediation",
        "do-i-need-mediation-before-family-court",
        "is-mediation-legally-binding",
        "can-mediation-cover-parenting-and-property",
        "is-family-mediation-confidential",
    ],
    read_min=3,
)

qa_page(
    slug="can-property-settlement-be-resolved-through-mediation",
    question="Can property settlement be resolved through mediation?",
    title="Can Property Settlement Be Resolved Through Mediation?",
    desc="Yes — property settlement can be resolved through mediation. Most separating couples reach agreement, avoiding contested court proceedings.",
    category="family",
    direct_answer=(
        "Yes. Property settlement can be resolved through mediation, and most separating "
        "couples who attempt it do reach an agreement. An agreement reached at mediation "
        "can then be formalised as consent orders or a binding financial agreement, making "
        "it legally enforceable without a contested court hearing."
    ),
    body=(
        f"<h2>How property mediation works</h2>"
        f"<p>Property mediation follows a similar structure to parenting mediation — a neutral "
        f"mediator helps both parties identify their assets, debts, and superannuation, "
        f"understand their legal entitlements, and negotiate a settlement. Sessions typically "
        f"run for a full day and cover the entire property pool.</p>"
        f"<p>Unlike parenting FDR, there is no mandatory pre-court mediation requirement for "
        f"property matters under the {cite('family_law_act')} — but courts expect parties to "
        f"have made genuine attempts to resolve property before listing for hearing. Parties "
        f"who have not attempted mediation may face adverse cost orders.</p>"
        f"<h2>What property mediation covers</h2>"
        f"<ul>"
        f"<li>The family home and other real estate</li>"
        f"<li>Superannuation splitting</li>"
        f"<li>Savings, investments, and shares</li>"
        f"<li>Business interests</li>"
        f"<li>Debts (mortgage, credit cards, personal loans)</li>"
        f"<li>Spousal maintenance (where applicable)</li>"
        f"</ul>"
        f"<h2>What you need to bring to property mediation</h2>"
        f"<p>Full financial disclosure is required — both parties should have current "
        f"valuations of all assets, statements for all accounts and superannuation funds, "
        f"and a clear picture of all debts. Incomplete disclosure is the most common reason "
        f"property mediation is unsuccessful.</p>"
        f"<p>See: <a href='/questions/what-should-i-bring-to-family-mediation/'>"
        f"what to bring to family mediation</a>.</p>"
        f"<h2>Formalising the agreement</h2>"
        f"<p>An agreement reached at property mediation can be formalised as:</p>"
        f"<ul>"
        f"<li><strong>Consent orders</strong> — filed with the {cite('fcfcoa')} "
        f"and made as orders of the court. Enforceable and stamp-duty exempt in most states.</li>"
        f"<li><strong>Binding financial agreement (BFA)</strong> — a contract signed by both "
        f"parties with independent legal advice. Does not require court filing.</li>"
        f"</ul>"
        f"<p>See our full guide: <a href='/bfa-or-consent-orders/'>"
        f"consent orders vs binding financial agreements</a>.</p>"
        f"<h2>Time limits</h2>"
        f"<p>Property applications must be made within 12 months of divorce being granted, "
        f"or within two years of the end of a de facto relationship. Missing these deadlines "
        f"requires the court's leave. Don't delay — see "
        f"<a href='/delaying-property-settlement/'>the risks of delaying property settlement</a>.</p>"
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
        "can-mediation-cover-parenting-and-property",
        "how-much-does-family-mediation-cost",
        "is-mediation-legally-binding",
        "what-is-in-the-property-pool",
        "bfa-or-consent-orders",
    ],
    read_min=3,
)

qa_page(
    slug="can-mediation-happen-online",
    question="Can mediation happen online?",
    title="Can Mediation Happen Online? | Mediations Australia",
    desc="Yes — online mediation is fully recognised in Australia for family, workplace, and commercial disputes. It counts as FDR for Section 60I certificate purposes.",
    category="family",
    direct_answer=(
        "Yes. Online mediation is fully available in Australia and is legally recognised "
        "for all dispute types, including Family Dispute Resolution (FDR). An online "
        "session conducted by an accredited FDRP carries the same legal weight as an "
        "in-person session and can result in a Section 60I certificate."
    ),
    body=(
        f"<h2>How online mediation works</h2>"
        f"<p>Online mediation is conducted via secure video conferencing. The mediator "
        f"manages separate video calls with each party (shuttle format) or brings both "
        f"parties into the same call (joint session). Most online platforms support "
        f"breakout rooms, which replicate the private meeting structure of in-person sessions.</p>"
        f"<h2>Is online mediation as effective as in-person?</h2>"
        f"<p>For many disputes, yes. Online mediation works particularly well where:</p>"
        f"<ul>"
        f"<li>The parties are in different cities or states</li>"
        f"<li>One or both parties have mobility or health limitations</li>"
        f"<li>High conflict makes sharing a physical space difficult</li>"
        f"<li>Shuttle format is already the preferred approach</li>"
        f"</ul>"
        f"<p>Some complex or high-stakes mediations (large property pools, multi-party "
        f"commercial disputes) may benefit from in-person sessions where non-verbal "
        f"communication and physical presence can aid negotiation. Discuss the format "
        f"with your mediator before the session.</p>"
        f"<h2>Does online FDR count for Section 60I purposes?</h2>"
        f"<p>Yes. An online FDR session conducted by an accredited FDRP under the "
        f"{cite('family_law_act')} is fully recognised. The FDRP can issue a Section 60I "
        f"certificate following an online session in exactly the same way as an in-person "
        f"session. See our full guide to "
        f"<a href='/online-mediation-australia/'>online mediation in Australia</a>.</p>"
        f"<h2>What you need for online mediation</h2>"
        f"<ul>"
        f"<li>A reliable internet connection</li>"
        f"<li>A device with camera and microphone (laptop preferred)</li>"
        f"<li>A private, quiet location where you will not be interrupted</li>"
        f"<li>Any documents or financial information the mediator has asked you to prepare</li>"
        f"</ul>"
        f"<h2>Is online mediation available across Australia?</h2>"
        f"<p>Yes — online mediation removes geographic barriers. Parties in rural and regional "
        f"Australia, and in different states, can participate without travel. We offer online "
        f"mediation for family, workplace, and commercial matters across all Australian "
        f"states and territories.</p>"
    ),
    sources=[
        ("Family Law Act 1975 (Cth)",
         "https://www.legislation.gov.au/Series/C2004A00275"),
        ("Federal Circuit and Family Court of Australia — Family Dispute Resolution",
         "https://www.fcfcoa.gov.au/fl/fdr"),
        ("Attorney-General's Department — Family Dispute Resolution",
         "https://www.ag.gov.au/families-and-marriage/families/family-dispute-resolution"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "what-is-shuttle-mediation",
        "what-happens-during-mediation",
        "do-i-need-mediation-before-family-court",
        "is-family-mediation-confidential",
        "how-long-does-family-mediation-take",
    ],
    read_min=2,
)

qa_page(
    slug="what-should-i-bring-to-family-mediation",
    question="What should I bring to family mediation?",
    title="What to Bring to Family Mediation | Mediations Australia",
    desc="Bring financial documents, asset and debt lists, super statements, and clear priorities. This guide covers what to prepare before your family mediation session.",
    category="family",
    direct_answer=(
        "For family mediation, bring current financial documents for property matters "
        "(bank statements, superannuation, property valuations, debts), and for parenting "
        "matters, a clear picture of your children's current routine and your proposed "
        "arrangements. Arriving prepared reduces session time and increases the chances "
        "of reaching agreement."
    ),
    body=(
        f"<h2>For property and financial mediation</h2>"
        f"<table style='width:100%;border-collapse:collapse;margin:1rem 0'>"
        f"<thead><tr style='background:var(--surf,#f7f8fa)'>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Document type</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>What to bring</th>"
        f"</tr></thead><tbody>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Real estate</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Recent property valuation or agents' appraisals; mortgage statements with current balance</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Superannuation</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Most recent member statement for all funds (both parties)</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Bank accounts</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Statements showing current balances for all joint and individual accounts</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Debts</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Current balances on credit cards, personal loans, car finance</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Income</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Recent pay slips or tax returns for both parties</td></tr>"
        f"<tr><td style='padding:.6rem .8rem'>Business interests</td>"
        f"<td style='padding:.6rem .8rem'>Recent financial statements, tax returns, any valuation</td></tr>"
        f"</tbody></table>"
        f"<h2>For parenting mediation</h2>"
        f"<ul>"
        f"<li>A clear description of the current parenting arrangements (what is actually happening day to day)</li>"
        f"<li>Your proposed arrangements — written out in specific terms (days, times, handover locations)</li>"
        f"<li>A list of your children's activities, school, and commitments</li>"
        f"<li>Any existing court orders or parenting plans that are in place</li>"
        f"<li>Contact details for the children's school and doctors (if relevant to the dispute)</li>"
        f"</ul>"
        f"<h2>Know your priorities before you arrive</h2>"
        f"<p>Before the session, spend time thinking about:</p>"
        f"<ul>"
        f"<li>What outcome matters most to you — your must-haves</li>"
        f"<li>What you would be willing to compromise on</li>"
        f"<li>What you think is important for your children (for parenting matters)</li>"
        f"</ul>"
        f"<p>Parties who arrive with clear priorities tend to reach agreement faster. "
        f"Those who arrive without a clear picture of what they want often spend the "
        f"first half of the session working this out.</p>"
        f"<h2>What not to bring</h2>"
        f"<ul>"
        f"<li>Text messages or social media posts you plan to present as evidence — "
        f"mediation is not a hearing. Bringing a folder of grievances can derail the "
        f"process.</li>"
        f"<li>Your children — children are not present in mediation sessions.</li>"
        f"<li>Unrealistic expectations — knowing the range of outcomes a court might "
        f"order (from legal advice) helps you negotiate from an informed position.</li>"
        f"</ul>"
        f"<p>Use our <a href='/preparing-for-mediation/'>free preparation tool</a> "
        f"to organise everything before your session.</p>"
    ),
    sources=[
        ("Federal Circuit and Family Court of Australia — duty of disclosure",
         "https://www.fcfcoa.gov.au/fl/duty-disclosure"),
        ("Attorney-General's Department — Family Dispute Resolution",
         "https://www.ag.gov.au/families-and-marriage/families/family-dispute-resolution"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "what-happens-during-mediation",
        "how-long-does-family-mediation-take",
        "is-family-mediation-confidential",
        "can-mediation-cover-parenting-and-property",
        "do-i-need-a-lawyer-for-mediation",
    ],
    read_min=3,
)

qa_page(
    slug="how-does-workplace-mediation-work",
    question="How does workplace mediation work?",
    title="How Does Workplace Mediation Work?",
    desc="Workplace mediation is a confidential process where a neutral mediator helps resolve disputes. Most matters resolve in a single day.",
    category="workplace",
    direct_answer=(
        "Workplace mediation is a confidential, facilitated process in which an independent "
        "mediator helps the parties to a workplace dispute communicate and reach a voluntary "
        "resolution. Most workplace mediation sessions are completed in a single day. The "
        "mediator does not take sides, make decisions, or impose outcomes."
    ),
    body=(
        f"<h2>The workplace mediation process</h2>"
        f"<p>A typical workplace mediation session follows four stages:</p>"
        f"<p><strong>1. Introduction</strong> — The mediator explains the process, confirms "
        f"confidentiality, and establishes ground rules. Each party has the opportunity to "
        f"speak without interruption.</p>"
        f"<p><strong>2. Exploration</strong> — The mediator helps each party describe their "
        f"experience, identify what matters most to them, and understand the other party's "
        f"perspective. Private meetings (caucuses) may occur at this stage.</p>"
        f"<p><strong>3. Negotiation</strong> — The mediator facilitates discussion of options "
        f"and helps the parties work toward agreement. The mediator may reality-test "
        f"proposals and help identify common ground.</p>"
        f"<p><strong>4. Agreement</strong> — If the parties reach agreement, the key terms "
        f"are documented in writing and signed by both parties before the session ends. "
        f"The agreement is a binding contract.</p>"
        f"<h2>Who attends?</h2>"
        f"<p>Typically, the two (or more) parties directly in dispute, and the mediator. "
        f"HR representatives may attend in an observer or support capacity, depending on "
        f"the organisation's approach. Legal representatives do not typically participate "
        f"in the session itself, though parties may take legal advice before and after.</p>"
        f"<h2>How long does it take?</h2>"
        f"<p>Most workplace mediation sessions are completed in half a day to a full day. "
        f"Complex matters involving multiple parties may require a second session. "
        f"Scheduling typically takes one to three weeks from agreement to participate.</p>"
        f"<h2>What types of disputes does it cover?</h2>"
        f"<ul>"
        f"<li>Interpersonal conflict between colleagues</li>"
        f"<li>Bullying and harassment disputes (where allegations have been assessed as "
        f"suitable for mediation)</li>"
        f"<li>Manager/employee relationship breakdowns</li>"
        f"<li>Unfair dismissal and general protections matters (pre- or post-application)</li>"
        f"<li>Redundancy and restructure disputes</li>"
        f"<li>Return-to-work arrangements following workplace injury</li>"
        f"</ul>"
        f"<h2>Is the outcome confidential?</h2>"
        f"<p>Yes — see our detailed guide: "
        f"<a href='/questions/is-workplace-mediation-confidential/'>"
        f"is workplace mediation confidential?</a> Both the process and the outcome "
        f"(unless the parties agree otherwise) are confidential.</p>"
        f"<h2>What if the dispute involves a {cite('fair_work')} application?</h2>"
        f"<p>Private workplace mediation can occur before, during, or alongside "
        f"Fair Work Commission proceedings. Resolving a matter through private mediation "
        f"gives the parties more control over the outcome and timeline than waiting for "
        f"a Commission conciliation conference.</p>"
    ),
    sources=[
        ("Fair Work Commission — dispute resolution",
         "https://www.fwc.gov.au/disputes-at-work"),
        ("Fair Work Ombudsman",
         "https://www.fairwork.gov.au/"),
        ("Safe Work Australia — managing psychosocial hazards",
         "https://www.safeworkaustralia.gov.au/safety-topic/hazards/mental-health"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "when-should-hr-use-an-external-mediator",
        "workplace-investigation-vs-mediation",
        "is-workplace-mediation-confidential",
        "can-an-employee-refuse-workplace-mediation",
        "what-happens-if-workplace-mediation-fails",
    ],
    read_min=3,
)

qa_page(
    slug="can-an-employee-refuse-workplace-mediation",
    question="Can an employee refuse workplace mediation?",
    title="Can an Employee Refuse Workplace Mediation?",
    desc="Workplace mediation is voluntary — an employee can refuse. However, refusal may affect ongoing employment and any related Fair Work Commission proceedings.",
    category="workplace",
    direct_answer=(
        "Yes. Workplace mediation is a voluntary process — an employee can refuse to "
        "participate. However, refusal is not without consequences: it may be taken into "
        "account by the Fair Work Commission in related proceedings, and it may affect "
        "how an employer deals with the underlying dispute."
    ),
    body=(
        f"<h2>Mediation is voluntary</h2>"
        f"<p>Unlike a workplace investigation (which an employer can direct an employee "
        f"to participate in), mediation requires both parties to agree to participate. "
        f"An employee cannot be forced to attend or forced to reach agreement at a "
        f"mediation session.</p>"
        f"<h2>Consequences of refusing</h2>"
        f"<p>While an employee cannot be disciplined solely for refusing mediation, "
        f"refusal can have practical consequences:</p>"
        f"<ul>"
        f"<li><strong>Fair Work Commission proceedings.</strong> If a related unfair "
        f"dismissal or general protections application is before the {cite('fair_work')}, "
        f"Commission members may take a dim view of unreasonable refusal to attempt "
        f"resolution — this can affect conciliation outcomes and, in some cases, costs.</li>"
        f"<li><strong>Employer's response to the dispute.</strong> An employer who has "
        f"offered mediation in good faith and been refused may feel more confident "
        f"proceeding with disciplinary action or other steps to manage the situation.</li>"
        f"<li><strong>Missed opportunity.</strong> Many workplace disputes that proceed "
        f"to litigation could have been resolved — at lower cost and stress — through "
        f"mediation. Refusal often prolongs the conflict.</li>"
        f"</ul>"
        f"<h2>When is refusal reasonable?</h2>"
        f"<p>Refusal may be reasonable where:</p>"
        f"<ul>"
        f"<li>The employee has safety concerns about meeting the other party</li>"
        f"<li>The dispute involves allegations so serious that mediation is not an "
        f"appropriate first step (for example, serious misconduct requiring investigation "
        f"and findings before any resolution is possible)</li>"
        f"<li>The employer has not offered adequate support — such as permitting a "
        f"support person to attend</li>"
        f"</ul>"
        f"<h2>Can an employer make mediation a condition of employment?</h2>"
        f"<p>An employment contract or workplace policy may require participation in "
        f"a dispute resolution process. If mediation is included in such a process, "
        f"an employee may be obliged to attend — though they cannot be forced to agree "
        f"to any outcome. Seek legal advice if your employment agreement contains such "
        f"a clause and you are uncertain of your obligations.</p>"
        f"<p>See also: <a href='/questions/workplace-investigation-vs-mediation/'>"
        f"workplace investigation vs mediation</a> — to understand when investigation "
        f"is the more appropriate process.</p>"
    ),
    sources=[
        ("Fair Work Commission — dispute resolution",
         "https://www.fwc.gov.au/disputes-at-work"),
        ("Fair Work Ombudsman",
         "https://www.fairwork.gov.au/"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "how-does-workplace-mediation-work",
        "can-a-support-person-attend-workplace-mediation",
        "workplace-investigation-vs-mediation",
        "when-should-hr-use-an-external-mediator",
        "what-happens-if-workplace-mediation-fails",
    ],
    read_min=2,
)

qa_page(
    slug="can-a-support-person-attend-workplace-mediation",
    question="Can a support person attend workplace mediation?",
    title="Can a Support Person Attend Workplace Mediation?",
    desc="Yes — employees and employers can bring a support person to workplace mediation. Their role is to support, not to advocate or negotiate on behalf of the party.",
    category="workplace",
    direct_answer=(
        "Yes. Both employees and employers can bring a support person to workplace "
        "mediation. A support person is there to support the participant — not to "
        "speak on their behalf, advocate, or run arguments. The mediator will confirm "
        "the role of any support person at the start of the session."
    ),
    body=(
        f"<h2>Who can be a support person?</h2>"
        f"<p>A support person can be:</p>"
        f"<ul>"
        f"<li>A union representative</li>"
        f"<li>A colleague or friend (with the agreement of both parties)</li>"
        f"<li>A HR representative (for the employer side)</li>"
        f"<li>A lawyer or employment law adviser</li>"
        f"<li>A mental health or wellbeing support person</li>"
        f"</ul>"
        f"<h2>What a support person can and cannot do</h2>"
        f"<table style='width:100%;border-collapse:collapse;margin:1rem 0'>"
        f"<thead><tr style='background:var(--surf,#f7f8fa)'>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>A support person can</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>A support person cannot</th>"
        f"</tr></thead><tbody>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Provide emotional support</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Speak on the participant's behalf</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Advise the participant privately during breaks</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Advocate, argue, or cross-examine</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Help the participant understand proposals</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Interrupt or take over the session</td></tr>"
        f"<tr><td style='padding:.6rem .8rem'>Assist with documents and note-taking</td>"
        f"<td style='padding:.6rem .8rem'>Make decisions on the participant's behalf</td></tr>"
        f"</tbody></table>"
        f"<h2>Does the other party need to agree?</h2>"
        f"<p>It is good practice to notify the other party if you intend to bring a support "
        f"person, particularly if that person is a lawyer. Springing a legal representative "
        f"on the other side can create an imbalance — if one party has a lawyer, the other "
        f"may reasonably wish to adjourn and take their own legal advice first.</p>"
        f"<h2>Union representatives</h2>"
        f"<p>Under the Fair Work Act 2009 (Cth) and the {cite('fair_work')}, employees have a general right to be "
        f"represented by a union in workplace matters. A union representative acting as "
        f"a support person in mediation is consistent with this right — though they should "
        f"understand the support-not-advocacy role in a mediation context.</p>"
        f"<h2>Can the mediator exclude a support person?</h2>"
        f"<p>Yes. A mediator may ask a support person to leave if their conduct is "
        f"disruptive or undermines the mediation process. A support person who turns "
        f"the session into a legal argument rather than a facilitated negotiation may "
        f"be asked to step back or leave.</p>"
    ),
    sources=[
        ("Fair Work Commission — unfair dismissal rights",
         "https://www.fwc.gov.au/disputes-at-work/unfair-dismissals"),
        ("Fair Work Ombudsman",
         "https://www.fairwork.gov.au/"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "how-does-workplace-mediation-work",
        "can-an-employee-refuse-workplace-mediation",
        "is-workplace-mediation-confidential",
        "when-should-hr-use-an-external-mediator",
        "workplace-investigation-vs-mediation",
    ],
    read_min=2,
)

qa_page(
    slug="can-workplace-mediation-deal-with-bullying-allegations",
    question="Can workplace mediation deal with bullying allegations?",
    title="Can Workplace Mediation Deal With Bullying Allegations?",
    desc="Workplace mediation can address bullying — best suited to interpersonal conflict rather than serious misconduct requiring formal investigation.",
    category="workplace",
    direct_answer=(
        "Workplace mediation can address some bullying disputes — particularly where the "
        "behaviour is interpersonal and both parties are willing to engage constructively. "
        "It is generally not appropriate as the sole response where allegations are serious, "
        "systematic, or involve a significant power imbalance without appropriate safeguards."
    ),
    body=(
        f"<h2>When mediation is appropriate for bullying</h2>"
        f"<p>Mediation can be an effective response to bullying where:</p>"
        f"<ul>"
        f"<li>The behaviour is interpersonal and involves a breakdown in the working "
        f"relationship (conflict-driven rather than systematic abuse)</li>"
        f"<li>Both parties are willing to participate genuinely and without coercion</li>"
        f"<li>The primary goal is restoring a working relationship, not establishing fault</li>"
        f"<li>No formal investigation is required — or an investigation has been completed "
        f"and findings are established</li>"
        f"</ul>"
        f"<h2>When mediation is not appropriate</h2>"
        f"<ul>"
        f"<li>Where the bullying is serious or systematic and requires an investigation "
        f"to establish facts and accountability</li>"
        f"<li>Where there is a significant power imbalance (manager bullying a direct "
        f"report) without appropriate safeguards — shuttle format may mitigate this</li>"
        f"<li>Where the alleged bully denies any problematic behaviour and is unwilling "
        f"to engage in good faith</li>"
        f"<li>Where the safety of the complainant would be at risk</li>"
        f"</ul>"
        f"<p>See: <a href='/questions/workplace-investigation-vs-mediation/'>"
        f"workplace investigation vs mediation</a> — for guidance on which process "
        f"is more appropriate in your situation.</p>"
        f"<h2>What about Fair Work Commission anti-bullying applications?</h2>"
        f"<p>The {cite('fair_work')} has the power to make orders to stop bullying "
        f"under Part 6-4B of the Fair Work Act 2009 (Cth). Many Fair Work Commission "
        f"anti-bullying applications are resolved through conciliation — which is a "
        f"form of facilitated negotiation similar to mediation. Private mediation before "
        f"filing can resolve matters faster and with more flexibility than Commission "
        f"proceedings.</p>"
        f"<h2>Safe Work Australia and psychosocial hazards</h2>"
        f"<p>Under WHS legislation, employers have a duty to manage psychosocial hazards "
        f"in the workplace, including bullying — see {cite('safework_mental')} for "
        f"guidance. Mediation is one tool in a suite of responses — alongside policies, "
        f"training, and investigation. It should be part of a broader response, not a "
        f"substitute for it where the situation is serious.</p>"
        f"<h2>Confidentiality and bullying mediation</h2>"
        f"<p>Workplace mediation is confidential — what is said in the session cannot "
        f"be used in subsequent proceedings. This can encourage frank discussion but "
        f"also means that admissions made in mediation cannot substitute for a formal "
        f"investigation finding if accountability is the primary concern.</p>"
    ),
    sources=[
        ("Fair Work Commission — anti-bullying applications",
         "https://www.fwc.gov.au/disputes-at-work/bullying-at-work"),
        ("Safe Work Australia — managing psychosocial hazards",
         "https://www.safeworkaustralia.gov.au/safety-topic/hazards/mental-health"),
        ("Fair Work Ombudsman",
         "https://www.fairwork.gov.au/"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "how-does-workplace-mediation-work",
        "workplace-investigation-vs-mediation",
        "when-should-hr-use-an-external-mediator",
        "is-workplace-mediation-confidential",
        "what-happens-if-workplace-mediation-fails",
    ],
    read_min=3,
)

qa_page(
    slug="what-happens-if-workplace-mediation-fails",
    question="What happens if workplace mediation fails?",
    title="What Happens If Workplace Mediation Fails?",
    desc="If workplace mediation fails, the dispute continues via Fair Work conciliation, disciplinary action, or litigation. Partial agreements still have value.",
    category="workplace",
    direct_answer=(
        "If workplace mediation fails, the dispute does not simply disappear — it "
        "continues through other channels. Depending on the nature of the dispute, "
        "this may mean Fair Work Commission conciliation or arbitration, disciplinary "
        "action, litigation, or a formal HR process. Partial agreements reached during "
        "mediation can still have value."
    ),
    body=(
        f"<h2>Partial agreements still have value</h2>"
        f"<p>Even when a full agreement is not reached, mediation often clarifies the "
        f"issues in dispute, identifies areas of common ground, and reduces the number "
        f"of matters that need to be resolved through other means. A partial agreement — "
        f"for example, on a return-to-work arrangement even where compensation is not "
        f"resolved — can significantly reduce the scope and cost of any subsequent "
        f"proceedings.</p>"
        f"<h2>What comes next — by dispute type</h2>"
        f"<table style='width:100%;border-collapse:collapse;margin:1rem 0'>"
        f"<thead><tr style='background:var(--surf,#f7f8fa)'>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Dispute type</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Typical next step after failed mediation</th>"
        f"</tr></thead><tbody>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Unfair dismissal</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>FWC conciliation conference; if unresolved, hearing and arbitration</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>General protections</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>FWC conference; if unresolved, Federal Court proceedings</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Workplace bullying</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>FWC anti-bullying application; investigation; WHS regulator referral</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Interpersonal conflict</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Formal HR process; performance management; redeployment or separation</td></tr>"
        f"<tr><td style='padding:.6rem .8rem'>Discrimination</td>"
        f"<td style='padding:.6rem .8rem'>State or federal anti-discrimination commission; human rights complaint</td></tr>"
        f"</tbody></table>"
        f"<h2>Did the mediation fail — or break down early?</h2>"
        f"<p>It is worth asking whether mediation genuinely failed or simply broke down "
        f"before it had a real chance to work. Common reasons mediation does not succeed "
        f"include: insufficient preparation, one party attending under duress, a "
        f"mediator not suited to the type of dispute, or the format not matching the "
        f"circumstances (for example, a joint session in a situation that needed shuttle "
        f"format). A second attempt with a different mediator or format sometimes resolves "
        f"matters that did not settle the first time.</p>"
        f"<h2>Confidentiality after failed mediation</h2>"
        f"<p>The confidentiality of the mediation process continues after it ends. "
        f"What was said during mediation cannot be used in subsequent {cite('fair_work')} "
        f"proceedings or litigation. The fact that mediation was attempted (and failed) "
        f"may be disclosed, but the content of the discussions may not.</p>"
        f"<h2>Getting advice on next steps</h2>"
        f"<p>We recommend both parties seek independent legal advice after a failed "
        f"mediation before deciding next steps. An employment lawyer can advise on the "
        f"realistic prospects of the available options, the likely costs, and the "
        f"timeframes involved.</p>"
    ),
    sources=[
        ("Fair Work Commission — dispute resolution",
         "https://www.fwc.gov.au/disputes-at-work"),
        ("Fair Work Ombudsman",
         "https://www.fairwork.gov.au/"),
        ("Safe Work Australia",
         "https://www.safeworkaustralia.gov.au/"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "how-does-workplace-mediation-work",
        "workplace-investigation-vs-mediation",
        "when-should-hr-use-an-external-mediator",
        "can-an-employee-refuse-workplace-mediation",
        "is-workplace-mediation-confidential",
    ],
    read_min=3,
)


# ── TIER 3 · PAGES 36–50 ────────────────────────────────────────────────────

qa_page(
    slug="how-much-does-commercial-mediation-cost",
    question="How much does commercial mediation cost in Australia?",
    title="How Much Does Commercial Mediation Cost in Australia?",
    desc="Commercial mediation typically costs $3,000–$8,000 per party per day in Australia. Costs depend on mediator seniority, dispute complexity, and session length.",
    category="commercial",
    direct_answer=(
        "Commercial mediation in Australia typically costs $3,000–$8,000 per party per day, "
        "depending on the mediator's seniority and the complexity of the dispute. This is "
        "significantly less than commercial litigation, which commonly runs to tens of thousands "
        "of dollars and takes years to resolve."
    ),
    body=(
        f"<h2>What drives the cost of commercial mediation?</h2>"
        f"<table style='width:100%;border-collapse:collapse;margin:1rem 0'>"
        f"<thead><tr style='background:var(--surf,#f7f8fa)'>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Cost factor</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Typical range</th>"
        f"</tr></thead><tbody>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Mediator daily rate (experienced)</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>$4,000–$12,000 + GST</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Mediator daily rate (senior barrister/retired judge)</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>$10,000–$25,000 + GST</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Venue (if not included)</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>$500–$2,000 per day</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Your legal representation</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>$3,000–$10,000+ per day (if instructed)</td></tr>"
        f"<tr><td style='padding:.6rem .8rem'>Preparation (briefs, position papers)</td>"
        f"<td style='padding:.6rem .8rem'>$2,000–$5,000 (billed by your lawyers)</td></tr>"
        f"</tbody></table>"
        f"<h2>How costs are split</h2>"
        f"<p>In commercial mediation, the mediator's fee is typically split equally between "
        f"the parties — each pays half. Parties bear their own legal representation costs. "
        f"Where a mediation clause in a contract specifies the cost split, that clause governs.</p>"
        f"<h2>Is commercial mediation cheaper than litigation?</h2>"
        f"<p>Almost always. A commercial dispute that reaches hearing in the Supreme Court "
        f"or Federal Court commonly costs each party $150,000–$500,000+ in legal fees over "
        f"two to four years. A one-day commercial mediation that resolves the matter costs "
        f"a fraction of this — even accounting for preparation time and legal representation "
        f"at the session.</p>"
        f"<h2>Court-ordered mediation</h2>"
        f"<p>Courts in NSW, Victoria, and other states routinely order commercial disputes "
        f"to mediation before hearing. Court-annexed mediation may be provided at a reduced "
        f"cost or no cost through the relevant court's dispute resolution scheme, though "
        f"wait times are generally longer than private mediation.</p>"
        f"<h2>Worked example</h2>"
        f"<p>A contract dispute between two businesses worth $800,000. Both parties instruct "
        f"solicitors. Private commercial mediator at $8,000/day (split equally: $4,000 each). "
        f"Each party's solicitor attends at $3,500. Preparation $1,500. <strong>Total per "
        f"party: approximately $9,000</strong> — compared to $120,000+ each if the matter "
        f"proceeds to a two-day Supreme Court hearing with barristers.</p>"
        f"<h2>When is a more expensive mediator worth it?</h2>"
        f"<p>For large or technically complex disputes, a senior mediator — a retired judge "
        f"or senior commercial barrister — can command $15,000–$25,000 per day. Their "
        f"authority, experience, and commercial judgment often produce better outcomes faster "
        f"in high-stakes matters, making the premium cost-effective overall.</p>"
    ),
    sources=[
        ("Resolution Institute — commercial mediation",
         "https://www.resolution.institute/"),
        ("NSW Civil and Administrative Tribunal — ADR",
         "https://www.ncat.nsw.gov.au/"),
        ("Federal Court of Australia — mediation",
         "https://www.fedcourt.gov.au/law-and-practice/alternative-dispute-resolution"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "how-does-commercial-mediation-work",
        "mediation-vs-arbitration-whats-the-difference",
        "can-mediation-resolve-a-contract-dispute",
        "is-commercial-mediation-confidential",
        "what-happens-if-commercial-mediation-fails",
    ],
    read_min=3,
)

qa_page(
    slug="how-does-commercial-mediation-work",
    question="How does commercial mediation work?",
    title="How Does Commercial Mediation Work?",
    desc="Commercial mediation is a confidential process for business disputes. A neutral mediator facilitates discussion without deciding the outcome.",
    category="commercial",
    direct_answer=(
        "Commercial mediation is a structured, confidential process in which a neutral "
        "mediator helps the parties to a business dispute reach a negotiated resolution. "
        "The mediator does not make decisions or impose outcomes — the parties retain "
        "full control. Most commercial mediations are completed in one to two days."
    ),
    body=(
        f"<h2>Before the session: preparation</h2>"
        f"<p>Effective commercial mediation requires preparation. Each party typically "
        f"prepares a confidential position paper (or mediation brief) setting out their "
        f"case, their key interests, and their settlement parameters. This document is "
        f"provided to the mediator before the session — it may or may not be shared with "
        f"the other party, at the submitting party's election.</p>"
        f"<h2>The mediation session</h2>"
        f"<p>A typical commercial mediation session follows four stages:</p>"
        f"<p><strong>1. Opening joint session</strong> — The mediator explains the process "
        f"and ground rules. Each party (or their legal representative) makes an opening "
        f"statement. The parties hear each other's perspective, often for the first time "
        f"in a controlled setting.</p>"
        f"<p><strong>2. Private meetings (caucus)</strong> — The mediator meets privately "
        f"with each party in turn. These are the most productive part of the process — "
        f"the mediator explores each party's real interests, tests the strength of their "
        f"positions, and begins to identify the parameters of a possible resolution.</p>"
        f"<p><strong>3. Negotiation</strong> — The mediator moves between the parties "
        f"(shuttle mediation) or brings them back together to facilitate joint negotiation. "
        f"The mediator may reality-test proposals, suggest options, and help the parties "
        f"find creative solutions that a court could not order.</p>"
        f"<p><strong>4. Agreement</strong> — If the parties reach agreement, the heads "
        f"of agreement (or a full deed of settlement) are drafted and signed before the "
        f"session ends. This agreement is a binding contract.</p>"
        f"<h2>Who attends?</h2>"
        f"<p>Commercial mediation typically involves: the parties (decision-makers with "
        f"authority to settle), their legal representatives (solicitors, barristers), and "
        f"the mediator. Technical experts or insurers may attend where relevant. It is "
        f"essential that the person attending has genuine authority to settle — sending "
        f"someone without authority is a common cause of failed mediations.</p>"
        f"<h2>Is commercial mediation different from court?</h2>"
        f"<table style='width:100%;border-collapse:collapse;margin:1rem 0'>"
        f"<thead><tr style='background:var(--surf,#f7f8fa)'>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'></th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Commercial mediation</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Court litigation</th>"
        f"</tr></thead><tbody>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Who decides the outcome?</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>The parties</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>The judge</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Confidential?</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Yes</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Generally public</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Timeframe</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Days to weeks</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Months to years</td></tr>"
        f"<tr><td style='padding:.6rem .8rem'>Creative outcomes possible?</td>"
        f"<td style='padding:.6rem .8rem'>Yes — anything the parties agree</td>"
        f"<td style='padding:.6rem .8rem'>Limited to what the court can order</td></tr>"
        f"</tbody></table>"
    ),
    sources=[
        ("Resolution Institute — commercial mediation",
         "https://www.resolution.institute/"),
        ("Federal Court of Australia — mediation",
         "https://www.fedcourt.gov.au/law-and-practice/alternative-dispute-resolution"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "how-much-does-commercial-mediation-cost",
        "mediation-vs-arbitration-whats-the-difference",
        "is-commercial-mediation-confidential",
        "can-lawyers-attend-commercial-mediation",
        "what-happens-if-commercial-mediation-fails",
    ],
    read_min=3,
)

qa_page(
    slug="mediation-vs-arbitration-whats-the-difference",
    question="Mediation vs arbitration: what's the difference?",
    title="Mediation vs Arbitration: What's the Difference?",
    desc="In mediation the parties reach their own agreement. In arbitration the arbitrator decides the outcome like a private judge. Learn which suits your dispute.",
    category="commercial",
    direct_answer=(
        "The key difference is who decides: in mediation, the parties negotiate and reach "
        "their own agreement with a neutral facilitator. In arbitration, the arbitrator "
        "hears the evidence and makes a binding decision — like a private judge. Mediation "
        "preserves control and confidentiality; arbitration produces a binding determination "
        "when the parties cannot agree."
    ),
    body=(
        f"<h2>Side-by-side comparison</h2>"
        f"<table style='width:100%;border-collapse:collapse;margin:1rem 0'>"
        f"<thead><tr style='background:var(--surf,#f7f8fa)'>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Feature</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Mediation</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Arbitration</th>"
        f"</tr></thead><tbody>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Who decides the outcome?</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>The parties — by agreement</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>The arbitrator — by determination</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Process</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Facilitated negotiation</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Adversarial hearing (evidence, submissions)</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Binding?</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Yes — if a settlement agreement is signed</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Yes — the award is binding and enforceable</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Confidential?</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Yes</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Yes (unlike court, which is public)</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Speed</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Days to weeks</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Months to years</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Cost</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Lower</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Higher (closer to litigation)</td></tr>"
        f"<tr><td style='padding:.6rem .8rem'>Voluntary?</td>"
        f"<td style='padding:.6rem .8rem'>Yes — parties can walk away</td>"
        f"<td style='padding:.6rem .8rem'>If agreed or ordered, parties cannot stop the process</td></tr>"
        f"</tbody></table>"
        f"<h2>When mediation is the better choice</h2>"
        f"<p>Mediation is generally preferable when:</p>"
        f"<ul>"
        f"<li>Preserving the business relationship matters</li>"
        f"<li>Both parties are open to compromise</li>"
        f"<li>A creative, tailored outcome is more valuable than a win/lose determination</li>"
        f"<li>Speed and cost are priorities</li>"
        f"</ul>"
        f"<h2>When arbitration is the better choice</h2>"
        f"<p>Arbitration is generally preferable when:</p>"
        f"<ul>"
        f"<li>The parties cannot agree and need a binding determination</li>"
        f"<li>A legal finding of fact or law is required</li>"
        f"<li>One party is unwilling to negotiate in good faith</li>"
        f"<li>The matter involves international parties (the arbitral award is enforceable "
        f"internationally under the New York Convention)</li>"
        f"</ul>"
        f"<h2>Can you do both?</h2>"
        f"<p>Yes — many commercial contracts include a tiered dispute resolution clause: "
        f"negotiation first, then mediation, then arbitration (or litigation). This is "
        f"best practice. Attempting mediation first rarely delays arbitration significantly, "
        f"and frequently avoids it entirely. See also our guide to "
        f"<a href='/arbitration-in-family-law/'>arbitration in family law</a> for the "
        f"family law context.</p>"
    ),
    sources=[
        ("Resolution Institute — commercial mediation and arbitration",
         "https://www.resolution.institute/"),
        ("Federal Court of Australia — alternative dispute resolution",
         "https://www.fedcourt.gov.au/law-and-practice/alternative-dispute-resolution"),
        ("ACICA — Australian Centre for International Commercial Arbitration",
         "https://www.acica.org.au/"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "how-does-commercial-mediation-work",
        "is-commercial-mediation-confidential",
        "can-mediation-resolve-a-contract-dispute",
        "what-happens-if-commercial-mediation-fails",
        "how-much-does-commercial-mediation-cost",
    ],
    read_min=3,
)

qa_page(
    slug="should-i-mediate-a-shareholder-dispute",
    question="Should I mediate a shareholder dispute?",
    title="Should I Mediate a Shareholder Dispute?",
    desc="Yes — mediation suits most shareholder disputes. It is confidential, faster than litigation, and lets the business keep operating during the process.",
    category="commercial",
    direct_answer=(
        "Yes. Mediation is well suited to most shareholder disputes. It is confidential, "
        "significantly faster and cheaper than shareholder litigation, and preserves the "
        "option of keeping the business running while the dispute is resolved. Courts also "
        "expect parties to have attempted mediation before listing a shareholder matter "
        "for hearing."
    ),
    body=(
        f"<h2>Why shareholder disputes are well suited to mediation</h2>"
        f"<p>Shareholder disputes — whether between equal partners, majority and minority "
        f"shareholders, or family shareholders — typically involve long-standing relationships, "
        f"significant assets, and ongoing business operations that would be damaged by "
        f"protracted litigation. Mediation addresses all three concerns:</p>"
        f"<ul>"
        f"<li><strong>Confidentiality</strong> — shareholder disputes often involve "
        f"sensitive financial information. Mediation is confidential; court proceedings "
        f"are generally public.</li>"
        f"<li><strong>Speed</strong> — shareholder litigation commonly takes two to four "
        f"years. Mediation can resolve matters in one to two days.</li>"
        f"<li><strong>Business continuity</strong> — the business can keep operating during "
        f"mediation; protracted litigation typically damages operations and key relationships.</li>"
        f"<li><strong>Creative outcomes</strong> — mediation can produce a buyout at an "
        f"agreed valuation, a restructured shareholders' agreement, a payment plan, or a "
        f"staged exit — none of which a court can impose.</li>"
        f"</ul>"
        f"<h2>What shareholder mediation can cover</h2>"
        f"<table style='width:100%;border-collapse:collapse;margin:1rem 0'>"
        f"<thead><tr style='background:var(--surf,#f7f8fa)'>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Dispute type</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Mediation outcome examples</th>"
        f"</tr></thead><tbody>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Shareholder buyout</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Agreed valuation, staged payment, or external sale</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Profit distribution disputes</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Revised distribution formula; arrears settlement</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Director/shareholder deadlock</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Updated shareholders' agreement; board restructure</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Oppression claims</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Buyout, restructure, or agreed exit before court application</td></tr>"
        f"<tr><td style='padding:.6rem .8rem'>Family shareholder disputes</td>"
        f"<td style='padding:.6rem .8rem'>Succession arrangements, estate carve-out, or agreed sale</td></tr>"
        f"</tbody></table>"
        f"<h2>Does a shareholders' agreement affect the process?</h2>"
        f"<p>Many shareholders' agreements include a dispute resolution clause requiring "
        f"mediation before legal proceedings. If yours does, mediation is not just advisable "
        f"— it may be a contractual precondition to commencing court action. Check your "
        f"agreement before filing any proceedings.</p>"
        f"<h2>When mediation may not be enough</h2>"
        f"<p>Mediation is less suitable where one party has engaged in fraud or serious "
        f"misconduct, where urgent court orders (such as an injunction to stop asset "
        f"dissipation) are needed, or where one party refuses to engage in good faith. "
        f"In those cases, legal proceedings may need to run concurrently with or instead "
        f"of mediation.</p>"
    ),
    sources=[
        ("Corporations Act 2001 (Cth) — shareholder rights",
         "https://www.legislation.gov.au/Series/C2004A00818"),
        ("Resolution Institute — commercial mediation",
         "https://www.resolution.institute/"),
        ("ASIC — resolving business disputes",
         "https://asic.gov.au/"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "how-does-commercial-mediation-work",
        "can-business-partners-use-mediation",
        "is-commercial-mediation-confidential",
        "mediation-vs-arbitration-whats-the-difference",
        "what-happens-if-commercial-mediation-fails",
    ],
    read_min=3,
)

qa_page(
    slug="can-business-partners-use-mediation",
    question="Can business partners use mediation?",
    title="Can Business Partners Use Mediation?",
    desc="Yes — mediation is highly effective for business partnership disputes. It is confidential, fast, and preserves the partnership where possible.",
    category="commercial",
    direct_answer=(
        "Yes. Business partners can use mediation to resolve disputes about profit splits, "
        "decision-making, roles, exit arrangements, and partnership dissolution. Mediation "
        "is confidential, faster than litigation, and often produces outcomes that preserve "
        "the business — or enable a clean exit — without the cost and reputational damage "
        "of court proceedings."
    ),
    body=(
        f"<h2>What types of partnership disputes suit mediation?</h2>"
        f"<ul>"
        f"<li>Profit and loss distribution disputes</li>"
        f"<li>Disputes about decision-making authority and management roles</li>"
        f"<li>One partner wanting to exit and disagreement on the buyout price</li>"
        f"<li>Alleged breach of the partnership agreement</li>"
        f"<li>Disputes over capital contributions or drawings</li>"
        f"<li>Clients, intellectual property, or non-compete obligations on exit</li>"
        f"</ul>"
        f"<h2>Does a partnership agreement affect the mediation process?</h2>"
        f"<p>Most well-drafted partnership agreements include a dispute resolution clause "
        f"requiring the partners to attempt mediation before commencing legal proceedings. "
        f"If yours does, check whether the clause specifies a particular process, mediator "
        f"appointment mechanism, or timeframe — you must follow it, or risk breaching the "
        f"agreement before you have even started.</p>"
        f"<p>If there is no written partnership agreement, state partnership legislation "
        f"(which varies by state) provides default rules on how disputes are resolved and how "
        f"a partnership may be dissolved. Seek legal advice on your state's applicable legislation.</p>"
        f"<h2>Mediation vs dissolution proceedings</h2>"
        f"<p>Partners who cannot resolve a dispute face two broad paths: mediation (aiming "
        f"for an agreed outcome) or court proceedings to dissolve the partnership. Dissolution "
        f"proceedings are expensive, public, and destructive to the business's goodwill. "
        f"Many partnerships that reach mediation avoid dissolution entirely — the parties "
        f"restructure the arrangement, execute a buyout, or agree a clean separation of "
        f"clients and assets.</p>"
        f"<h2>Who should attend the mediation?</h2>"
        f"<p>All partners (or their authorised representatives) should attend with genuine "
        f"authority to settle. Where the partnership has a business manager or accountant "
        f"whose information is material to the dispute, they may also attend. Legal "
        f"representatives often attend commercial partnership mediations but are not "
        f"required — see our guide: "
        f"<a href='/questions/can-lawyers-attend-commercial-mediation/'>"
        f"can lawyers attend commercial mediation?</a></p>"
        f"<h2>What outcomes can mediation produce?</h2>"
        f"<ul>"
        f"<li>A revised partnership agreement with updated terms</li>"
        f"<li>A buyout of one partner's interest at an agreed valuation</li>"
        f"<li>A structured wind-down with agreed client and asset allocation</li>"
        f"<li>A payment plan for arrears or disputed drawings</li>"
        f"<li>A non-compete or client list allocation on exit</li>"
        f"</ul>"
    ),
    sources=[
        ("Resolution Institute — commercial mediation",
         "https://www.resolution.institute/"),
        ("ASIC — resolving business disputes",
         "https://asic.gov.au/"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "should-i-mediate-a-shareholder-dispute",
        "how-does-commercial-mediation-work",
        "can-mediation-resolve-a-contract-dispute",
        "is-commercial-mediation-confidential",
        "what-happens-if-commercial-mediation-fails",
    ],
    read_min=2,
)

qa_page(
    slug="can-mediation-resolve-a-contract-dispute",
    question="Can mediation resolve a contract dispute?",
    title="Can Mediation Resolve a Contract Dispute?",
    desc="Yes — mediation resolves most contract disputes. It is confidential, cheaper than litigation, and produces binding agreements without a court judgment.",
    category="commercial",
    direct_answer=(
        "Yes. Mediation can resolve most commercial contract disputes — including "
        "payment defaults, delivery failures, service disputes, and interpretation "
        "disagreements. A settlement agreement reached at mediation is a binding contract. "
        "Most commercial contracts also include a dispute resolution clause requiring "
        "mediation before court proceedings."
    ),
    body=(
        f"<h2>What types of contract disputes suit mediation?</h2>"
        f"<ul>"
        f"<li>Payment defaults and invoicing disputes</li>"
        f"<li>Breach of contract claims (goods not delivered, services not performed)</li>"
        f"<li>Disputes about the scope or quality of work performed</li>"
        f"<li>Construction and building contract disputes</li>"
        f"<li>Supply chain and distribution agreement disputes</li>"
        f"<li>IT and software contract disputes</li>"
        f"<li>Franchise agreement disputes</li>"
        f"<li>Lease and commercial property disputes</li>"
        f"</ul>"
        f"<h2>Is mediation required before I can sue?</h2>"
        f"<p>Many commercial contracts include a dispute resolution clause requiring the "
        f"parties to attempt mediation (or at least good-faith negotiation) before commencing "
        f"court proceedings. Failing to comply with such a clause before filing can result "
        f"in a stay of proceedings and adverse cost orders. Check your contract before "
        f"filing any claim.</p>"
        f"<h2>How does a settlement agreement work?</h2>"
        f"<p>If the parties reach agreement at mediation, the key terms are recorded in "
        f"a heads of agreement or deed of settlement, signed by both parties before the "
        f"session ends. This document is a binding contract and can be enforced in the "
        f"same way as any other commercial agreement. It is not a court order — it does "
        f"not require filing — but it can be enforced if breached.</p>"
        f"<h2>What mediation can achieve that a court cannot</h2>"
        f"<p>A court can only order money or a specific legal remedy. Mediation can produce "
        f"any outcome the parties agree — including a revised payment schedule, a variation "
        f"to the contract's ongoing terms, a trade of goods or services in lieu of payment, "
        f"a mutual release, or a reference for an independent expert to determine a disputed "
        f"technical question. This flexibility is one of mediation's key advantages for "
        f"commercial disputes.</p>"
        f"<h2>Worked example</h2>"
        f"<p>A builder invoices $280,000 for completed works. The client claims defects "
        f"and refuses to pay. If litigated in the District Court, costs could exceed "
        f"$60,000 each over 18 months. At mediation: both parties agree an independent "
        f"building inspector assesses the defects; the builder agrees to rectify confirmed "
        f"defects; the client pays $240,000 on a staged schedule. Total mediation cost: "
        f"under $10,000 each. Matter resolved in one day.</p>"
    ),
    sources=[
        ("Resolution Institute — commercial mediation",
         "https://www.resolution.institute/"),
        ("Federal Court of Australia — alternative dispute resolution",
         "https://www.fedcourt.gov.au/law-and-practice/alternative-dispute-resolution"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "how-does-commercial-mediation-work",
        "how-much-does-commercial-mediation-cost",
        "is-commercial-mediation-confidential",
        "mediation-vs-arbitration-whats-the-difference",
        "what-happens-if-commercial-mediation-fails",
    ],
    read_min=3,
)

qa_page(
    slug="is-commercial-mediation-confidential",
    question="Is commercial mediation confidential?",
    title="Is Commercial Mediation Confidential?",
    desc="Yes — commercial mediation is confidential. What is said cannot be used in court proceedings or disclosed to third parties without the parties' consent.",
    category="commercial",
    direct_answer=(
        "Yes. Commercial mediation is confidential. What is said during mediation — "
        "including offers, concessions, and admissions — cannot generally be used in "
        "subsequent court or arbitration proceedings. This confidentiality is protected "
        "both by the mediation agreement signed at the start of the session and, in many "
        "Australian jurisdictions, by legislation."
    ),
    body=(
        f"<h2>How confidentiality is protected</h2>"
        f"<p>Commercial mediation confidentiality operates at two levels:</p>"
        f"<p><strong>Contractual protection:</strong> The mediation agreement (signed before "
        f"the session begins) includes a confidentiality clause binding all participants — "
        f"the parties, their legal representatives, and the mediator. Any party who breaches "
        f"this clause may be liable in damages.</p>"
        f"<p><strong>Legislative protection:</strong> In several Australian states, the "
        f"confidentiality of mediation communications is reinforced by legislation — for "
        f"example, under the Evidence Act in NSW and Victoria, mediation communications "
        f"are protected from disclosure in court proceedings. Confirm the applicable "
        f"legislation with your legal adviser.</p>"
        f"<h2>What confidentiality covers</h2>"
        f"<ul>"
        f"<li>All offers and counter-offers made during the session</li>"
        f"<li>Concessions and admissions</li>"
        f"<li>Documents produced specifically for the mediation (such as confidential "
        f"position papers)</li>"
        f"<li>What the mediator says during private meetings (caucus)</li>"
        f"<li>The fact that a particular settlement position was taken</li>"
        f"</ul>"
        f"<h2>What confidentiality does not cover</h2>"
        f"<ul>"
        f"<li>The settlement agreement itself — if the parties intend for the agreement "
        f"to be enforceable, it must be capable of being put before a court if breached. "
        f"The agreement is confidential as a document but not non-existent.</li>"
        f"<li>Pre-existing documents produced in the mediation that were already disclosable "
        f"— producing a document at mediation does not make it privileged if it was not "
        f"already.</li>"
        f"<li>Evidence of criminal conduct or child abuse — confidentiality does not "
        f"protect disclosures that a party is legally required to report.</li>"
        f"</ul>"
        f"<h2>Without prejudice privilege</h2>"
        f"<p>In addition to the mediation agreement, settlement discussions conducted "
        f"in the context of a genuine attempt to resolve a dispute are generally protected "
        f"by without prejudice privilege at common law. This means that even if the "
        f"mediation agreement were silent, the communications would generally not be "
        f"admissible in court. The two protections — contractual and common law — "
        f"reinforce each other.</p>"
        f"<p>For questions about how confidentiality works in family mediation, see: "
        f"<a href='/questions/is-family-mediation-confidential/'>"
        f"is family mediation confidential?</a></p>"
    ),
    sources=[
        ("Resolution Institute — commercial mediation",
         "https://www.resolution.institute/"),
        ("Evidence Act 1995 (NSW)",
         "https://www.legislation.nsw.gov.au/view/html/inforce/current/act-1995-025"),
        ("Federal Court of Australia — alternative dispute resolution",
         "https://www.fedcourt.gov.au/law-and-practice/alternative-dispute-resolution"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "how-does-commercial-mediation-work",
        "can-lawyers-attend-commercial-mediation",
        "mediation-vs-arbitration-whats-the-difference",
        "can-mediation-resolve-a-contract-dispute",
        "what-happens-if-commercial-mediation-fails",
    ],
    read_min=3,
)

qa_page(
    slug="can-lawyers-attend-commercial-mediation",
    question="Can lawyers attend commercial mediation?",
    title="Can Lawyers Attend Commercial Mediation?",
    desc="Yes — lawyers regularly attend commercial mediation as advisers and representatives. Their role is to advise, not to run the session adversarially.",
    category="commercial",
    direct_answer=(
        "Yes. Lawyers regularly attend commercial mediation as advisers and legal "
        "representatives. Unlike court, lawyers do not dominate commercial mediation — "
        "the process is facilitated by a neutral mediator and the business decision-makers "
        "at the table are the ones who settle. Lawyers advise, review documents, and help "
        "formalise any agreement."
    ),
    body=(
        f"<h2>What lawyers do at commercial mediation</h2>"
        f"<p>At commercial mediation, a lawyer typically:</p>"
        f"<ul>"
        f"<li>Prepares the confidential position paper or mediation brief</li>"
        f"<li>Advises the client on the legal merits and realistic settlement range before "
        f"and during the session</li>"
        f"<li>Makes the opening statement on behalf of the client (if a joint session is held)</li>"
        f"<li>Attends private meetings (caucus) with the client and mediator</li>"
        f"<li>Reviews and drafts the settlement agreement or heads of agreement</li>"
        f"<li>Provides real-time advice on whether a proposed settlement is acceptable</li>"
        f"</ul>"
        f"<h2>Should both parties have legal representation?</h2>"
        f"<p>There is no requirement for either party to have legal representation. However, "
        f"where one party has legal representation and the other does not, a significant "
        f"imbalance can arise — particularly in complex commercial disputes. The mediator "
        f"has an obligation to ensure the process is fair, but cannot give legal advice "
        f"to the unrepresented party. If you are the unrepresented party in a matter "
        f"where the other side has lawyers, seek at least a pre-mediation legal consultation "
        f"on your position.</p>"
        f"<h2>The difference between commercial and family mediation</h2>"
        f"<p>Legal representation at commercial mediation is more common and less "
        f"controversial than at family mediation. Commercial disputes typically involve "
        f"larger amounts, more complex legal issues, and business entities rather than "
        f"individuals. In family mediation, lawyers sometimes attend but often provide "
        f"advice only before and after the session. See: "
        f"<a href='/questions/can-i-bring-a-lawyer-to-family-mediation/'>"
        f"can I bring a lawyer to family mediation?</a></p>"
        f"<h2>Barristers at commercial mediation</h2>"
        f"<p>For high-value or legally complex matters, barristers are sometimes retained "
        f"specifically for commercial mediation. A barrister's advocacy skills and "
        f"authoritative assessment of litigation risk can be valuable in persuading the "
        f"other side (through the mediator) to settle. Some mediators are themselves "
        f"senior barristers or retired judges — which often concentrates the minds of "
        f"the parties on the realistic outcomes of litigation.</p>"
    ),
    sources=[
        ("Resolution Institute — commercial mediation",
         "https://www.resolution.institute/"),
        ("Federal Court of Australia — alternative dispute resolution",
         "https://www.fedcourt.gov.au/law-and-practice/alternative-dispute-resolution"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "how-does-commercial-mediation-work",
        "is-commercial-mediation-confidential",
        "can-mediation-resolve-a-contract-dispute",
        "how-much-does-commercial-mediation-cost",
        "what-happens-if-commercial-mediation-fails",
    ],
    read_min=2,
)

qa_page(
    slug="what-happens-if-commercial-mediation-fails",
    question="What happens if commercial mediation fails?",
    title="What Happens If Commercial Mediation Fails?",
    desc="If commercial mediation fails, parties can proceed to arbitration or court. Partial agreements retain value and confidentiality is preserved.",
    category="commercial",
    direct_answer=(
        "If commercial mediation fails, the parties may proceed to arbitration or court "
        "proceedings. The confidentiality of the mediation process is preserved — nothing "
        "said or offered during mediation can be used in the subsequent proceedings. "
        "Any partial agreement reached during mediation can still be documented and "
        "relied upon."
    ),
    body=(
        f"<h2>What 'failed' mediation often produces</h2>"
        f"<p>A mediation that does not produce a full settlement is not necessarily a "
        f"failure. Even unsuccessful mediations typically:</p>"
        f"<ul>"
        f"<li>Narrow the issues in dispute — the parties often agree on facts or "
        f"quantum elements, leaving fewer matters for a court to determine</li>"
        f"<li>Produce a partial settlement — some claims or parties may be resolved "
        f"even if the full matter is not</li>"
        f"<li>Clarify each party's genuine bottom line, reducing wasted time in "
        f"subsequent proceedings</li>"
        f"<li>Demonstrate good faith, which courts take into account in cost orders</li>"
        f"</ul>"
        f"<h2>Next steps by dispute type</h2>"
        f"<table style='width:100%;border-collapse:collapse;margin:1rem 0'>"
        f"<thead><tr style='background:var(--surf,#f7f8fa)'>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Dispute type</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Typical next step</th>"
        f"</tr></thead><tbody>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Contract dispute</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>District or Supreme Court proceedings; or arbitration if the contract requires it</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Shareholder dispute</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Supreme Court oppression proceedings (Corporations Act s.232)</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Building/construction dispute</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>NCAT (NSW), VCAT (Vic), or relevant state tribunal; or expert determination</td></tr>"
        f"<tr><td style='padding:.6rem .8rem'>International commercial dispute</td>"
        f"<td style='padding:.6rem .8rem'>International arbitration under ACICA, ICC, or LCIA rules</td></tr>"
        f"</tbody></table>"
        f"<h2>Does failed mediation affect costs in subsequent proceedings?</h2>"
        f"<p>Yes — and this can cut both ways. If a party attended mediation in bad faith "
        f"(for example, without genuine authority to settle, or with no intention of "
        f"settling), courts may penalise that party in costs. Conversely, a party who "
        f"attended in good faith and made reasonable proposals can use the failed mediation "
        f"to demonstrate reasonableness — which is relevant to cost outcomes in subsequent "
        f"proceedings.</p>"
        f"<h2>Is a second mediation worth trying?</h2>"
        f"<p>Often yes — particularly where the first mediation broke down early, involved "
        f"a mediator not well suited to the dispute type, or used a format (such as a "
        f"joint session) that was inappropriate for the relationship between the parties. "
        f"A second mediation with a different mediator, a different format, or after "
        f"interim steps (such as an expert report) resolves many matters that did not "
        f"settle the first time.</p>"
    ),
    sources=[
        ("Resolution Institute — commercial mediation",
         "https://www.resolution.institute/"),
        ("Federal Court of Australia — alternative dispute resolution",
         "https://www.fedcourt.gov.au/law-and-practice/alternative-dispute-resolution"),
        ("ACICA — Australian Centre for International Commercial Arbitration",
         "https://www.acica.org.au/"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "how-does-commercial-mediation-work",
        "mediation-vs-arbitration-whats-the-difference",
        "is-commercial-mediation-confidential",
        "can-mediation-resolve-a-contract-dispute",
        "how-much-does-commercial-mediation-cost",
    ],
    read_min=3,
)

qa_page(
    slug="can-you-mediate-a-contested-will",
    question="Can you mediate a contested will?",
    title="Can You Mediate a Contested Will?",
    desc="Yes — will and estate disputes can be mediated. Most courts encourage or require mediation before contested probate or family provision matters go to hearing.",
    category="estate",
    direct_answer=(
        "Yes. Contested will and estate disputes can be mediated — and most Australian "
        "courts require or strongly encourage mediation before a contested probate or "
        "family provision matter proceeds to hearing. Mediation is confidential, "
        "significantly cheaper than estate litigation, and preserves family relationships "
        "more effectively than adversarial proceedings."
    ),
    body=(
        f"<h2>What types of will and estate disputes suit mediation?</h2>"
        f"<ul>"
        f"<li>Family provision claims (where a family member believes they were inadequately "
        f"provided for in a will)</li>"
        f"<li>Disputes about the validity of a will (undue influence, testamentary capacity)</li>"
        f"<li>Disputes about the proper construction or interpretation of a will</li>"
        f"<li>Executor disputes — challenges to an executor's conduct or decision-making</li>"
        f"<li>Disputes between beneficiaries about asset distribution or valuation</li>"
        f"</ul>"
        f"<h2>Is mediation required before estate litigation?</h2>"
        f"<p>In New South Wales, Victoria, and Queensland, courts routinely order estate "
        f"disputes to mediation before a contested hearing is listed. In NSW, family provision "
        f"matters filed in the Supreme Court are almost invariably referred to mediation "
        f"at an early stage. Parties who proceed to hearing without attempting mediation "
        f"may face adverse cost orders.</p>"
        f"<h2>Family provision claims</h2>"
        f"<p>Family provision claims — brought under the Succession Act 2006 (NSW), "
        f"Administration and Probate Act 1958 (Vic), or equivalent state legislation — "
        f"are among the most commonly mediated estate disputes. The mediator helps the "
        f"parties (the estate executor or administrator, and the claimant) explore the "
        f"merits of the claim, the assets available, and an appropriate provision without "
        f"a contested hearing.</p>"
        f"<h2>Advantages of mediating estate disputes</h2>"
        f"<ul>"
        f"<li><strong>Cost</strong> — contested estate litigation can cost $100,000–$300,000+ "
        f"in legal fees. These costs are often paid from the estate, reducing what "
        f"beneficiaries receive. Mediation costs a fraction of this.</li>"
        f"<li><strong>Speed</strong> — estate litigation commonly takes two to four years. "
        f"Mediation can resolve matters in one to two sessions.</li>"
        f"<li><strong>Family relationships</strong> — adversarial proceedings permanently "
        f"damage family relationships. Mediation creates space for constructive dialogue.</li>"
        f"<li><strong>Estate preservation</strong> — the longer a contested estate is "
        f"in dispute, the more it costs in ongoing legal and administration fees. "
        f"Resolution through mediation stops the clock.</li>"
        f"</ul>"
    ),
    sources=[
        ("Succession Act 2006 (NSW)",
         "https://www.legislation.nsw.gov.au/view/html/inforce/current/act-2006-080"),
        ("Supreme Court of NSW — estate disputes",
         "https://www.supremecourt.justice.nsw.gov.au/"),
        ("Resolution Institute — estate mediation",
         "https://www.resolution.institute/"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "what-is-estate-mediation",
        "can-mediation-resolve-an-inheritance-dispute",
        "how-much-does-estate-mediation-cost",
        "when-should-an-estate-dispute-go-to-mediation",
        "what-happens-if-estate-mediation-fails",
    ],
    read_min=3,
)

qa_page(
    slug="what-is-estate-mediation",
    question="What is estate mediation?",
    title="What Is Estate Mediation?",
    desc="Estate mediation resolves will and inheritance disputes without court. A neutral mediator helps parties reach a negotiated, confidential settlement.",
    category="estate",
    direct_answer=(
        "Estate mediation is a confidential, facilitated process designed to resolve "
        "disputes about wills, estates, and inheritances. A neutral mediator helps "
        "the parties — beneficiaries, executors, family members — reach a negotiated "
        "settlement without the cost and delay of contested court proceedings."
    ),
    body=(
        f"<h2>What estate mediation covers</h2>"
        f"<p>Estate mediation can address any dispute arising from a will or estate, "
        f"including:</p>"
        f"<ul>"
        f"<li><strong>Family provision claims</strong> — where a family member seeks "
        f"greater provision from the estate than the will allows</li>"
        f"<li><strong>Executor disputes</strong> — challenges to an executor's conduct, "
        f"decisions, or removal</li>"
        f"<li><strong>Beneficiary disputes</strong> — disagreements between beneficiaries "
        f"about asset distribution, property values, or allocation of specific assets</li>"
        f"<li><strong>Will validity disputes</strong> — where the validity of the will "
        f"is questioned on grounds such as testamentary capacity or undue influence</li>"
        f"<li><strong>Trust and estate administration disputes</strong> — disputes about "
        f"how a testamentary trust is being administered</li>"
        f"</ul>"
        f"<h2>How does estate mediation work?</h2>"
        f"<p>Estate mediation follows a similar process to commercial mediation. The "
        f"mediator meets separately with each party (executor/estate, claimants, and "
        f"any other beneficiaries) before or during the session, understands each "
        f"party's position and interests, and facilitates negotiation. Sessions typically "
        f"run for a full day.</p>"
        f"<p>Where the estate includes real property or business assets, current valuations "
        f"are essential — parties should obtain independent valuations before the session "
        f"to avoid valuation disputes becoming the obstacle to settlement.</p>"
        f"<h2>Who attends estate mediation?</h2>"
        f"<p>Typically: the executor (or administrator), the claimant(s), their legal "
        f"representatives, and the mediator. Where there are multiple beneficiaries, "
        f"all may need to attend — or appoint one person with authority to settle on "
        f"behalf of their group. If the estate includes a trustee company or public "
        f"trustee, a representative with genuine settlement authority must attend.</p>"
        f"<h2>Is estate mediation confidential?</h2>"
        f"<p>Yes — estate mediation is confidential. What is said and offered during "
        f"the session cannot be used in subsequent court proceedings. The settlement "
        f"agreement itself is binding and enforceable. See our full guide to "
        f"<a href='/estate-dispute-mediation/'>estate dispute mediation</a>.</p>"
        f"<h2>When do courts refer estate matters to mediation?</h2>"
        f"<p>In New South Wales, most family provision matters filed in the Supreme Court "
        f"are referred to mediation before a hearing is listed. In Victoria and Queensland, "
        f"courts similarly encourage or order mediation in contested estate matters. "
        f"See: <a href='/questions/when-should-an-estate-dispute-go-to-mediation/'>"
        f"when should an estate dispute go to mediation?</a></p>"
    ),
    sources=[
        ("Succession Act 2006 (NSW)",
         "https://www.legislation.nsw.gov.au/view/html/inforce/current/act-2006-080"),
        ("Supreme Court of NSW — estate disputes",
         "https://www.supremecourt.justice.nsw.gov.au/"),
        ("Resolution Institute — estate mediation",
         "https://www.resolution.institute/"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "can-you-mediate-a-contested-will",
        "can-mediation-resolve-an-inheritance-dispute",
        "how-much-does-estate-mediation-cost",
        "when-should-an-estate-dispute-go-to-mediation",
        "what-happens-if-estate-mediation-fails",
    ],
    read_min=3,
)

qa_page(
    slug="can-mediation-resolve-an-inheritance-dispute",
    question="Can mediation resolve an inheritance dispute?",
    title="Can Mediation Resolve an Inheritance Dispute?",
    desc="Yes — mediation resolves most inheritance disputes faster and cheaper than court. Family provision claims and executor disputes all suit mediation.",
    category="estate",
    direct_answer=(
        "Yes. Mediation resolves most inheritance disputes — including family provision "
        "claims, executor disputes, and beneficiary conflicts — faster and at far lower "
        "cost than court proceedings. Most Australian courts require or strongly encourage "
        "mediation before a contested inheritance matter proceeds to hearing."
    ),
    body=(
        f"<h2>What makes inheritance disputes suited to mediation?</h2>"
        f"<p>Inheritance disputes typically involve:</p>"
        f"<ul>"
        f"<li>Family members who will have an ongoing relationship after the dispute resolves</li>"
        f"<li>Finite assets (the estate) that litigation costs diminish for all parties</li>"
        f"<li>Emotional and relational dimensions that a court cannot address</li>"
        f"<li>A desire for privacy — court proceedings are public; mediation is confidential</li>"
        f"</ul>"
        f"<p>All four features make mediation particularly well-suited compared to "
        f"adversarial litigation.</p>"
        f"<h2>Family provision claims</h2>"
        f"<p>The most common inheritance dispute is a family provision claim — where a "
        f"family member believes they were inadequately provided for in the will. These "
        f"claims are brought under state succession legislation (Succession Act 2006 (NSW), "
        f"Administration and Probate Act 1958 (Vic), or equivalent). They are almost always "
        f"resolved through mediation in New South Wales, where the Supreme Court refers "
        f"most claims to mediation before hearing.</p>"
        f"<h2>What outcomes can mediation produce?</h2>"
        f"<ul>"
        f"<li>A lump sum payment to the claimant from the estate</li>"
        f"<li>Transfer of a specific asset (such as a property) in full or partial "
        f"satisfaction of a claim</li>"
        f"<li>A revised distribution of the estate with all parties' agreement</li>"
        f"<li>A payment schedule where the estate does not have liquid assets available</li>"
        f"<li>Resolution of executor conduct complaints alongside distribution</li>"
        f"</ul>"
        f"<h2>Cost comparison</h2>"
        f"<table style='width:100%;border-collapse:collapse;margin:1rem 0'>"
        f"<thead><tr style='background:var(--surf,#f7f8fa)'>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Path</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Typical cost (each party)</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Timeframe</th>"
        f"</tr></thead><tbody>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Mediation</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>$3,000–$10,000</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>1–3 months</td></tr>"
        f"<tr><td style='padding:.6rem .8rem'>Supreme Court hearing</td>"
        f"<td style='padding:.6rem .8rem'>$50,000–$300,000+</td>"
        f"<td style='padding:.6rem .8rem'>2–4 years</td></tr>"
        f"</tbody></table>"
        f"<p>Estate litigation costs are often paid from the estate — reducing what "
        f"all beneficiaries receive, not just the losing party. Mediation protects the "
        f"estate for the family.</p>"
    ),
    sources=[
        ("Succession Act 2006 (NSW)",
         "https://www.legislation.nsw.gov.au/view/html/inforce/current/act-2006-080"),
        ("Supreme Court of NSW — estate disputes",
         "https://www.supremecourt.justice.nsw.gov.au/"),
        ("Resolution Institute — estate mediation",
         "https://www.resolution.institute/"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "can-you-mediate-a-contested-will",
        "what-is-estate-mediation",
        "how-much-does-estate-mediation-cost",
        "when-should-an-estate-dispute-go-to-mediation",
        "what-happens-if-estate-mediation-fails",
    ],
    read_min=3,
)

qa_page(
    slug="how-much-does-estate-mediation-cost",
    question="How much does estate mediation cost?",
    title="How Much Does Estate Mediation Cost?",
    desc="Estate mediation in Australia typically costs $2,000–$6,000 per party — far less than contested estate litigation, which can cost $50,000–$300,000+ per party.",
    category="estate",
    direct_answer=(
        "Estate mediation in Australia typically costs $2,000–$6,000 per party, including "
        "the mediator's fee and legal representation at the session. This is a fraction "
        "of the cost of contested estate litigation, which commonly costs $50,000–$300,000+ "
        "per party — often paid from the estate itself, reducing what all beneficiaries receive."
    ),
    body=(
        f"<h2>What drives estate mediation costs?</h2>"
        f"<table style='width:100%;border-collapse:collapse;margin:1rem 0'>"
        f"<thead><tr style='background:var(--surf,#f7f8fa)'>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Cost component</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Typical range</th>"
        f"</tr></thead><tbody>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Mediator's fee (per party, half-day)</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>$800–$2,000</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Mediator's fee (per party, full day)</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>$1,500–$4,000</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Legal representation at session</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>$1,500–$4,000 (solicitor's day rate)</td></tr>"
        f"<tr><td style='padding:.6rem .8rem'>Preparation (position papers, asset schedules)</td>"
        f"<td style='padding:.6rem .8rem'>$1,000–$3,000 (billed by your lawyers)</td></tr>"
        f"</tbody></table>"
        f"<h2>Who pays for estate mediation?</h2>"
        f"<p>In estate disputes, the mediator's fee is typically split equally between "
        f"the estate (on behalf of the executor) and the claimant(s). Each party bears "
        f"their own legal costs. Where there are multiple claimants, they may share the "
        f"claimant's portion of the mediator's fee.</p>"
        f"<p>In court-ordered mediations, costs are sometimes paid from the estate as "
        f"part of the estate administration costs — subject to the court's orders. "
        f"Confirm the cost allocation with your legal adviser before booking.</p>"
        f"<h2>Why litigation is far more expensive</h2>"
        f"<p>Contested estate matters — particularly family provision claims — are among "
        f"the most expensive civil disputes in Australia. A two-day Supreme Court hearing "
        f"with barristers commonly costs $80,000–$200,000 per party in legal fees. "
        f"These costs are frequently paid from the estate, reducing what all beneficiaries "
        f"ultimately receive. A one-day mediation that resolves the matter costs all "
        f"parties combined what a single day of Supreme Court litigation costs one party.</p>"
        f"<h2>Worked example</h2>"
        f"<p>A family provision claim against a $1.2M estate. Claimant seeks $250,000. "
        f"Estate mediation: mediator $2,500 (split $1,250 each), solicitor for claimant "
        f"$1,800, solicitor for estate $2,000, preparation $1,200 each. "
        f"<strong>Total per party: approximately $3,000–$4,000.</strong> Settlement: "
        f"$180,000 to the claimant. Estate proceeds to distribution. If litigated instead: "
        f"each party spends $80,000–$150,000. Estate is substantially diminished.</p>"
    ),
    sources=[
        ("Succession Act 2006 (NSW)",
         "https://www.legislation.nsw.gov.au/view/html/inforce/current/act-2006-080"),
        ("Supreme Court of NSW — probate and estate",
         "https://www.supremecourt.justice.nsw.gov.au/"),
        ("Resolution Institute — estate mediation",
         "https://www.resolution.institute/"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "what-is-estate-mediation",
        "can-you-mediate-a-contested-will",
        "can-mediation-resolve-an-inheritance-dispute",
        "when-should-an-estate-dispute-go-to-mediation",
        "what-happens-if-estate-mediation-fails",
    ],
    read_min=3,
)

qa_page(
    slug="when-should-an-estate-dispute-go-to-mediation",
    question="When should an estate dispute go to mediation?",
    title="When Should an Estate Dispute Go to Mediation?",
    desc="Mediate an estate dispute as early as possible — before costs escalate. Courts order mediation before contested hearings in most Australian states.",
    category="estate",
    direct_answer=(
        "An estate dispute should go to mediation as early as possible — ideally before "
        "formal legal proceedings are filed and before legal costs escalate significantly. "
        "Courts in NSW, Victoria, and Queensland also order estate and family provision "
        "matters to mediation before a contested hearing is listed."
    ),
    body=(
        f"<h2>The earlier, the better</h2>"
        f"<p>The single most important factor in estate mediation outcomes is timing. "
        f"Disputes resolved early — before proceedings are filed, before positions harden, "
        f"and before significant legal costs have been incurred — settle more easily and "
        f"at better outcomes for all parties. Once Supreme Court proceedings are underway, "
        f"costs escalate rapidly and settlement becomes psychologically harder.</p>"
        f"<h2>Key triggers that indicate it's time for mediation</h2>"
        f"<ul>"
        f"<li>A family member indicates they intend to make a family provision claim</li>"
        f"<li>Beneficiaries are in dispute about asset distribution or property values</li>"
        f"<li>There is a challenge to the executor's conduct or decision-making</li>"
        f"<li>A dispute about will validity is emerging and the parties wish to avoid "
        f"the reputational and relational damage of contested litigation</li>"
        f"<li>The estate is holding assets (such as real property) that cannot be "
        f"distributed until the dispute is resolved — mediation resolves the blockage</li>"
        f"</ul>"
        f"<h2>Court-ordered mediation</h2>"
        f"<p>In New South Wales, the Supreme Court refers most family provision matters "
        f"to mediation within months of filing — often before the first contested hearing. "
        f"In Victoria and Queensland, courts similarly order or encourage mediation. "
        f"Parties who wait for a court order lose the opportunity to resolve the matter "
        f"at lower cost through private mediation first.</p>"
        f"<h2>Time limits for family provision claims</h2>"
        f"<p>Family provision claims must be filed within 12 months of the date of death "
        f"in NSW and most other states. Filing proceedings to protect the limitation period "
        f"does not prevent the parties from mediating — but it is important not to let "
        f"mediation delay result in a claim being time-barred. A potential claimant can "
        f"attempt mediation and file proceedings simultaneously, or file first and then "
        f"mediate.</p>"
        f"<h2>What about disputes that arise during administration?</h2>"
        f"<p>Not all estate disputes are about wills — many arise during the administration "
        f"of an estate (executor decisions, delays, asset valuations, interim distributions). "
        f"These disputes suit mediation at any stage of administration. Resolving "
        f"administration disputes through mediation avoids the cost and delay of beneficiary "
        f"actions in the Supreme Court.</p>"
    ),
    sources=[
        ("Succession Act 2006 (NSW) — time limits",
         "https://www.legislation.nsw.gov.au/view/html/inforce/current/act-2006-080"),
        ("Supreme Court of NSW — estate disputes",
         "https://www.supremecourt.justice.nsw.gov.au/"),
        ("Resolution Institute — estate mediation",
         "https://www.resolution.institute/"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "what-is-estate-mediation",
        "can-you-mediate-a-contested-will",
        "can-mediation-resolve-an-inheritance-dispute",
        "how-much-does-estate-mediation-cost",
        "what-happens-if-estate-mediation-fails",
    ],
    read_min=3,
)

qa_page(
    slug="what-happens-if-estate-mediation-fails",
    question="What happens if estate mediation fails?",
    title="What Happens If Estate Mediation Fails?",
    desc="If estate mediation fails, parties proceed to court. Confidentiality is preserved, partial agreements remain valid, and a second attempt often succeeds.",
    category="estate",
    direct_answer=(
        "If estate mediation fails, the parties may proceed to contested court proceedings "
        "— typically in the Supreme Court. The confidentiality of the mediation process "
        "is preserved; nothing said or offered in mediation can be used in the subsequent "
        "litigation. Any partial agreement reached at mediation remains binding."
    ),
    body=(
        f"<h2>What failed estate mediation often still achieves</h2>"
        f"<p>A mediation that does not produce a full settlement is not necessarily "
        f"a failure. Even unsuccessful estate mediations frequently:</p>"
        f"<ul>"
        f"<li>Narrow the dispute — the parties may agree on asset values or some "
        f"distribution questions, leaving fewer contested issues for the court</li>"
        f"<li>Resolve some claimants while others remain in dispute</li>"
        f"<li>Reveal the other party's real position, helping legal advisers refine "
        f"their approach to subsequent proceedings</li>"
        f"<li>Demonstrate good faith, which courts consider in costs orders</li>"
        f"</ul>"
        f"<h2>Next steps after failed estate mediation</h2>"
        f"<table style='width:100%;border-collapse:collapse;margin:1rem 0'>"
        f"<thead><tr style='background:var(--surf,#f7f8fa)'>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Dispute type</th>"
        f"<th style='padding:.6rem .8rem;text-align:left;border-bottom:2px solid var(--border,#e5e7eb)'>Typical next step</th>"
        f"</tr></thead><tbody>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Family provision claim</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Contested Supreme Court hearing; costs usually from estate</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Will validity dispute</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Probate proceedings; contested hearing with expert evidence</td></tr>"
        f"<tr><td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Executor dispute</td>"
        f"<td style='padding:.6rem .8rem;border-bottom:1px solid var(--border,#e5e7eb)'>Application for removal of executor; court administration order</td></tr>"
        f"<tr><td style='padding:.6rem .8rem'>Beneficiary/distribution dispute</td>"
        f"<td style='padding:.6rem .8rem'>Administration action in Supreme Court; court-directed distribution</td></tr>"
        f"</tbody></table>"
        f"<h2>Costs after failed mediation</h2>"
        f"<p>Estate litigation costs are usually paid from the estate — meaning all "
        f"beneficiaries bear the cost of the dispute, not just the losing party. "
        f"A party who attended mediation in good faith and made reasonable proposals "
        f"can sometimes use this to their advantage in costs arguments at the conclusion "
        f"of the proceedings. A party who refused to mediate, or attended in bad faith, "
        f"may face a personal costs order.</p>"
        f"<h2>Is a second mediation worth trying?</h2>"
        f"<p>Yes — often. Estate disputes where the first mediation broke down over "
        f"asset valuations, executor access to information, or the presence of one "
        f"difficult party sometimes resolve at a second session once these obstacles "
        f"are addressed. An independent expert report on property values, or a change "
        f"in the mediator, sometimes makes the critical difference. Courts support "
        f"parties attempting a second mediation before hearing.</p>"
        f"<p>See our full guide: <a href='/estate-dispute-mediation/'>estate dispute "
        f"mediation in Australia</a>.</p>"
    ),
    sources=[
        ("Succession Act 2006 (NSW)",
         "https://www.legislation.nsw.gov.au/view/html/inforce/current/act-2006-080"),
        ("Supreme Court of NSW — estate disputes",
         "https://www.supremecourt.justice.nsw.gov.au/"),
        ("Resolution Institute — estate mediation",
         "https://www.resolution.institute/"),
    ],
    reviewer="Dan Toombs",
    reviewer_slug="dan-toombs",
    related=[
        "what-is-estate-mediation",
        "can-you-mediate-a-contested-will",
        "can-mediation-resolve-an-inheritance-dispute",
        "how-much-does-estate-mediation-cost",
        "when-should-an-estate-dispute-go-to-mediation",
    ],
    read_min=3,
)


if __name__ == "__main__":
    print(f"\nBuilding {len(QUESTION_REGISTRY)} Q&A page(s)...")
    print(f"Output: {OUT}/questions/")
    print(f"Review date: {REVIEW_DATE}")
    print(f"\nDone. {len(QUESTION_REGISTRY)} page(s) written.\n")
