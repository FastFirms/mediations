#!/usr/bin/env python3
"""
Generate /access-mediation/ — the Access Mediation landing page.

Revised per UX brief: calculator first, band table in accordion,
no public Band 1-5 labels, simplified eligibility language.

Build: python3 build/gen_access.py
Output: access-mediation/index.html
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, faq_html, cta_band,
                       org_schema, faq_schema, breadcrumb_schema, service_schema,
                       BOOK_URL, PHONE, PHONE_HREF)

OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLUG = "access-mediation"

# ── Page content ──────────────────────────────────────────────────────────────
TITLE   = "Access Mediation | Reduced-Fee Family Mediation for Eligible Participants"
DESC    = ("Access Mediation is a reduced-contribution family mediation pathway for eligible "
           "participants. Check your indicative contribution and apply in minutes.")
H1      = "Access Mediation — Reduced Contributions for Eligible Participants"
EYEBROW = "Reduced-fee mediation pathway"
LEDE    = ("If the standard mediation contribution is genuinely out of reach, you may qualify "
           "for Access Mediation — a limited pathway where contributions are assessed individually, "
           "based on your income, assets and circumstances, not your partner's.")

ANSWER  = ("Access Mediation offers reduced individual contributions from $495 + GST for a "
           "3-hour session, assessed on your personal financial circumstances. Places are "
           "limited. Financial eligibility does not guarantee a booking — mediation suitability "
           "is assessed separately.")

QA = [
    ("What is Access Mediation?",
     "Access Mediation is a limited reduced-contribution pathway for family mediation. "
     "Each participant's contribution is assessed individually based on their own income, "
     "assets, dependants, and hardship circumstances — not their partner's. Contributions "
     "range from $495 + GST to $1,295 + GST per person for a 3-hour session."),

    ("Am I eligible for Access Mediation?",
     "Eligibility is assessed on your personal gross annual income (generally below $150,000), "
     "accessible assets, number of dependants, any concession card status, and genuine hardship. "
     "Each case is reviewed individually. You can check your indicative contribution using our "
     "calculator above — it takes about 60 seconds."),

    ("How are contributions calculated?",
     "Your contribution is based on your personal income, adjusted for accessible assets, dependants "
     "(3 or more), concession status, or material hardship. The maximum automatic reduction is "
     "one band. Any adjustment is applied to your contribution only — your partner's assessment "
     "is completely separate and private."),

    ("Will my partner know my contribution or financial details?",
     "No. Each participant's financial assessment is entirely private. Your income, assets, "
     "hardship circumstances and contribution are never shared with the other participant, their "
     "lawyer, or anyone outside authorised staff. Participants may have different contributions — "
     "but neither party is told the financial basis for the other's contribution."),

    ("Does financial eligibility guarantee a booking?",
     "No. Access appointments are limited and allocated on a first-come, first-served basis "
     "within monthly capacity. Financial eligibility confirms your indicative contribution only — "
     "mediation suitability (including any family safety screening) is assessed separately by our "
     "staff before a booking is confirmed."),

    ("What is Access assistance?",
     "Access assistance is the difference between the standard individual contribution ($1,500 + GST "
     "for a 3-hour session) and your assessed Access contribution. For example, at the lowest band "
     "the Access assistance is $1,005 — reducing your contribution from $1,500 to $495 + GST. "
     "This assistance is funded by Mediations Australia and is not a government subsidy."),

    ("What if I need a Section 60I certificate?",
     "Section 60I certificates are issued following a recognised Family Dispute Resolution (FDR) "
     "process. If obtaining a certificate may be important in your circumstances, please tell us "
     "before booking so we can help identify the appropriate service and practitioner. "
     "If you are unsure whether you require one, speak with our team or obtain independent legal advice. "
     "We cannot issue a certificate in advance or guarantee one will be issued."),

    ("Can I apply if my income is above $150,000?",
     "Generally, income above $150,000 per year attracts the standard contribution. However, if "
     "you have significant material hardship despite a higher income, our team will review your "
     "circumstances individually. Use the calculator to check, or call us on "
     f"{PHONE} to discuss."),

    ("What happens after I apply?",
     "Our team reviews your application (usually within 1–2 business days), confirms your "
     "contribution and mediation suitability, and contacts you to arrange scheduling. If Access "
     "capacity is full for the current month, you will be placed on a waitlist and contacted as "
     "soon as a place becomes available."),

    ("What mediation matters does Access cover?",
     "Access Mediation is available for family law matters — parenting arrangements, property "
     "settlement, or both. It is not available for purely commercial or employment disputes. "
     "Matters involving family violence are carefully screened; contact us to discuss safety "
     "and suitability before applying."),
]


def band_table_accordion():
    """Band table inside a <details> accordion — no Band 1-5 labels."""
    rows = [
        ("Up to $50,000",          "$495"),
        ("$50,001 – $75,000",      "$695"),
        ("$75,001 – $100,000",     "$895"),
        ("$100,001 – $125,000",    "$1,095"),
        ("$125,001 – $150,000",    "$1,295"),
        ("More than $150,000",     "Standard contribution, subject to exceptional hardship review"),
    ]
    row_html = "".join(
        f'<tr><td>{i}</td><td><strong>{c} + GST</strong></td></tr>'
        for i, c in rows
    )
    return f"""<details class="band-accordion">
  <summary class="band-accordion-toggle">Prefer to see the contribution bands? <span class="band-acc-arr">&#8595;</span></summary>
  <div class="band-accordion-body">
    <div class="table-scroll">
    <table class="data-table">
      <caption>Access Mediation — indicative contributions per participant (3-hour session)</caption>
      <thead>
        <tr>
          <th>Personal gross annual income</th>
          <th>Indicative contribution</th>
        </tr>
      </thead>
      <tbody>{row_html}</tbody>
      <tfoot>
        <tr><td colspan="2">These amounts are indicative. Accessible financial resources, dependants and exceptional hardship may affect the final contribution. All figures exclude GST.</td></tr>
      </tfoot>
    </table>
    </div>
  </div>
</details>"""


def calculator_section():
    """Calculator first — the primary conversion element."""
    return f"""<section class="calc-section" id="check-contribution">
  <div class="wrap-narrow">
    <h2>Check your indicative contribution</h2>
    <p class="lede-sm">Answer a few questions about your own financial circumstances. Takes about 60 seconds. No documents are required to check. Your answers are private and are not shared with the other participant.</p>
    <div id="access-calc-root" data-calc="access">
      <!-- Access Mediation calculator mounts here (access-calc.js) -->
      <noscript>
        <div class="notice">
          Please enable JavaScript to use the contribution calculator, or call us on
          <a href="{PHONE_HREF}">{PHONE}</a> and we will assess your contribution over the phone.
        </div>
      </noscript>
    </div>
    {band_table_accordion()}
  </div>
</section>"""


def how_it_works():
    """Simplified 4-step process per UX brief §10."""
    steps = [
        ("1", "Check your indicative contribution",
         "Answer a few questions about your own financial circumstances. "
         "Takes about 60 seconds. You do not need to upload documents to check."),
        ("2", "Submit an application if you want to proceed",
         "We confirm your contribution before an appointment is booked. "
         "No financial documents are required at the application stage."),
        ("3", "The other participant is contacted separately",
         "Their financial circumstances are assessed privately and independently. "
         "One participant&#8217;s income does not affect what the other pays."),
        ("4", "Mediation is arranged if appropriate and available",
         "Normal intake, safety, suitability and availability requirements still apply. "
         "Access places are limited and allocated within monthly capacity."),
    ]
    items = "".join(
        f'<div class="step reveal">'
        f'<div class="step-num">{n}</div>'
        f'<div class="step-body"><h3>{t}</h3><p>{d}</p></div>'
        f'</div>'
        for n, t, d in steps
    )
    return f'<section class="steps-section"><div class="wrap"><h2>How Access Mediation works</h2>{items}</div></section>'


def who_for_section():
    """Simplified 'who is this for' section per UX brief §11."""
    return f"""<section class="who-section reveal">
  <div class="wrap-narrow">
    <h2>Who is Access Mediation for?</h2>
    <p>Access Mediation may be suitable if you can contribute toward private mediation but paying the standard fee would cause genuine financial difficulty.</p>
    <p>We consider your circumstances individually, including:</p>
    <ul class="check-list">
      <li>your personal income;</li>
      <li>financial dependants;</li>
      <li>accessible savings and investments;</li>
      <li>exceptional financial hardship.</li>
    </ul>
    <p><strong>Your former partner&#8217;s income does not determine whether you qualify.</strong></p>
    <p>The calculator provides an indicative contribution. We confirm your contribution before an Access appointment is booked.</p>
    <p style="font-size:.88rem;color:var(--ink-soft,#3d5248)">Access Mediation is <strong>not available</strong> for purely commercial, employment, or neighbourhood disputes. Matters involving family violence or safety concerns are carefully screened — call us on <a href="{PHONE_HREF}" style="color:var(--sage-deep,#1e6040)">{PHONE}</a> before applying.</p>
  </div>
</section>"""


def inaccessible_assets_section():
    """New section per UX brief §12."""
    return """<section class="assets-section reveal">
  <div class="wrap-narrow">
    <div class="asset-callout">
      <h3>What if I have assets but cannot access them?</h3>
      <p>We look at financial capacity, not simply what you own on paper.</p>
      <p>Ordinary family home and superannuation are not treated as readily accessible resources. If funds or assets are currently inaccessible — for example, because they are disputed, frozen, or tied up in a property — you can ask us to review your circumstances individually.</p>
    </div>
  </div>
</section>"""


def privacy_note():
    """Strengthened privacy section per UX brief §13."""
    return """<section class="privacy-section reveal">
  <div class="wrap-narrow">
    <h2>Your financial assessment is private.</h2>
    <p>Each participant is assessed separately. We do not tell the other participant your:</p>
    <ul class="privacy-list">
      <li>income;</li>
      <li>accessible asset information;</li>
      <li>concession status;</li>
      <li>hardship information;</li>
      <li>reasons for your contribution;</li>
      <li>Access assistance amount.</li>
    </ul>
    <p>Participants may pay different amounts.</p>
    <p><strong>The amount either participant pays does not affect the mediator&#8217;s independence, neutrality or professional obligations.</strong></p>
  </div>
</section>"""


def extra_css():
    return """<style>
/* ── Access Mediation page-specific styles ── */
.calc-section{background:var(--sage-pale,#f1f5f1);padding:52px 0}
.lede-sm{color:var(--ink-soft,#3d5248);margin-bottom:24px;font-size:.97rem;line-height:1.6;max-width:62ch}
#access-calc-root{min-height:160px}
.notice{padding:16px 20px;background:#fff3cd;border-left:4px solid #f0a500;border-radius:6px;font-size:.9rem}

/* band accordion */
.band-accordion{margin-top:28px;border:1px solid var(--line,rgba(13,34,24,.14));border-radius:10px;overflow:hidden;background:#fff}
.band-accordion-toggle{list-style:none;padding:14px 18px;font-size:.93rem;font-weight:600;color:var(--sage-deep,#1e6040);cursor:pointer;display:flex;justify-content:space-between;align-items:center}
.band-accordion-toggle::-webkit-details-marker{display:none}
details[open] .band-acc-arr{transform:rotate(180deg)}
.band-acc-arr{display:inline-block;transition:transform .2s;font-size:.8rem}
.band-accordion-body{padding:0 18px 18px}

/* steps */
.steps-section{padding:52px 0}
.steps-section h2{margin-bottom:28px}
.step{display:flex;gap:20px;align-items:flex-start;margin-bottom:24px}
.step-num{width:38px;height:38px;border-radius:50%;background:var(--sage-deep,#1e6040);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.97rem;flex-shrink:0;margin-top:2px}
.step-body h3{margin:0 0 5px;font-size:1rem}
.step-body p{margin:0;color:var(--ink-soft,#3d5248);font-size:.91rem;line-height:1.6}

/* who section */
.who-section{padding:48px 0;background:var(--sage-pale,#f1f5f1)}
.who-section h2{margin-bottom:12px}
.check-list{list-style:none;padding:0;margin:12px 0 16px}
.check-list li{padding-left:26px;position:relative;margin-bottom:9px;font-size:.93rem;line-height:1.5}
.check-list li::before{content:"✓";position:absolute;left:0;color:var(--sage-deep,#1e6040);font-weight:700}

/* assets callout */
.assets-section{padding:36px 0}
.asset-callout{background:#fff;border:1.5px solid var(--sage-deep,#1e6040);border-radius:12px;padding:22px 24px}
.asset-callout h3{margin:0 0 8px;font-size:1rem;color:var(--sage-deep,#1e6040)}
.asset-callout p{margin:0 0 8px;font-size:.91rem;color:var(--ink-soft,#3d5248);line-height:1.6}
.asset-callout p:last-child{margin:0}

/* privacy */
.privacy-section{padding:48px 0;background:var(--sage-pale,#f1f5f1)}
.privacy-section h2{margin-bottom:10px}
.privacy-list{list-style:none;padding:0;margin:12px 0 16px}
.privacy-list li{padding-left:24px;position:relative;margin-bottom:8px;font-size:.91rem;color:var(--ink-soft,#3d5248);line-height:1.45}
.privacy-list li::before{content:"\2717";position:absolute;left:0;color:var(--sage-deep,#1e6040);font-weight:700}

/* shared data-table */
.data-table{width:100%;border-collapse:collapse;font-size:.9rem}
.data-table th{background:var(--sage-deep,#1e6040);color:#fff;padding:10px 14px;text-align:left}
.data-table td{padding:10px 14px;border-bottom:1px solid rgba(13,34,24,.1);vertical-align:top}
.data-table tfoot td{font-size:.8rem;color:var(--ink-soft,#3d5248);padding:10px 14px;border-bottom:none;font-style:italic}
.data-table tbody tr:nth-child(even) td{background:#f8fbf8}
.table-scroll{overflow-x:auto;margin:12px 0 0}

@media(max-width:600px){
  .calc-section,.steps-section,.who-section,.privacy-section,.assets-section{padding:36px 0}
  .band-accordion-toggle{font-size:.88rem}
}
</style>"""


def build():
    schema = [
        org_schema(),
        breadcrumb_schema([("Home", ""), ("Access Mediation", SLUG)]),
        service_schema("Access Mediation", DESC, SLUG),
        faq_schema(QA),
    ]
    html_doc = head(TITLE, DESC, SLUG, extra_schema=schema)
    html_doc = html_doc.replace("</head>", extra_css() + "\n</head>")
    html_doc += nav()
    html_doc += f"""<main id="main">
{crumb_html([("Home",""),("Access Mediation",None)])}
<section class="phero">
  <div class="phero-blob"></div>
  <div class="wrap">
    <span class="eyebrow"><span class="pulse"></span>{EYEBROW}</span>
    <h1>{H1}</h1>
    <p class="lede">{LEDE}</p>
    <div class="phero-cta">
      <a href="#check-contribution" class="btn btn-primary">Check My Indicative Contribution <span class="arr">&#8595;</span></a>
      <a href="{PHONE_HREF}" class="btn btn-ghost">Call {PHONE}</a>
    </div>
  </div>
</section>"""

    html_doc += (f'<div class="wrap-narrow">'
                 f'<div class="answer reveal"><p><strong>In short:</strong> {ANSWER}</p></div>'
                 f'</div>')

    # Calculator FIRST (brief §3)
    html_doc += calculator_section()

    # How it works
    html_doc += how_it_works()

    # Who it's for (simplified)
    html_doc += who_for_section()

    # Inaccessible assets callout
    html_doc += inaccessible_assets_section()

    # Privacy
    html_doc += privacy_note()

    # FAQ (renamed FAQ 6: "What is Access assistance?")
    html_doc += faq_html(QA, heading="Access Mediation FAQs")

    # Final CTA — primary: Check My Access Contribution (brief §16)
    html_doc += cta_band(
        "Find out what your contribution could be.",
        "Use our short calculator for an indicative Access contribution. "
        "It takes about 60 seconds and you do not need to upload financial documents to check.",
    )
    html_doc += "</main>" + page_end()
    html_doc = html_doc.replace("</body>", '<script src="/access-calc.js" defer></script>\n</body>')

    path = os.path.join(OUT, SLUG)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "index.html"), "w") as f:
        f.write(html_doc)
    print(f"Built: /{SLUG}/")


if __name__ == "__main__":
    build()
