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
        f'<li class="step reveal">'
        f'<div class="step-num">{n}</div>'
        f'<h3>{t}</h3><p>{d}</p>'
        f'</li>'
        for n, t, d in steps
    )
    return f'<section class="steps-section"><div class="wrap"><h2>How Access Mediation works</h2><ol class="steps-grid">{items}</ol></div></section>'


def who_for_section():
    """Who it's for (left) + inaccessible-assets card (right)."""
    return f"""<section class="who-section reveal">
  <div class="wrap">
    <div class="who-grid">
      <div class="who-main">
        <h2>Who is Access Mediation for?</h2>
        <p>Access Mediation may be suitable if you can contribute toward private mediation but paying the standard fee would cause genuine financial difficulty.</p>
        <p>We consider your circumstances individually, including:</p>
        <ul class="check-grid">
          <li>your personal income;</li>
          <li>financial dependants;</li>
          <li>accessible savings and investments;</li>
          <li>exceptional financial hardship.</li>
        </ul>
        <p class="who-key"><strong>Your former partner&#8217;s income does not determine whether you qualify.</strong></p>
        <p>The calculator provides an indicative contribution. We confirm your contribution before an Access appointment is booked.</p>
      </div>
      <aside class="who-side">
        <div class="asset-callout">
          <h3>What if I have assets but cannot access them?</h3>
          <p>We look at financial capacity, not simply what you own on paper.</p>
          <p>Ordinary family home and superannuation are not treated as readily accessible resources. If funds or assets are currently inaccessible — for example, because they are disputed, frozen, or tied up in a property — you can ask us to review your circumstances individually.</p>
        </div>
        <div class="who-note">
          <p>Access Mediation is <strong>not available</strong> for purely commercial, employment, or neighbourhood disputes. Matters involving family violence or safety concerns are carefully screened — call us on <a href="{PHONE_HREF}">{PHONE}</a> before applying.</p>
        </div>
      </aside>
    </div>
  </div>
</section>"""


def inaccessible_assets_section():
    """Merged into who_for_section (two-column layout)."""
    return ""


def privacy_note():
    """Privacy panel: statement left, protected items right."""
    return """<section class="privacy-section reveal">
  <div class="wrap">
    <div class="privacy-panel">
      <div class="privacy-intro">
        <h2>Your financial assessment is private.</h2>
        <p>Each participant is assessed separately. We do not tell the other participant your:</p>
        <p class="privacy-foot">Participants may pay different amounts.</p>
        <p class="privacy-foot"><strong>The amount either participant pays does not affect the mediator&#8217;s independence, neutrality or professional obligations.</strong></p>
      </div>
      <ul class="privacy-list">
        <li>income;</li>
        <li>accessible asset information;</li>
        <li>concession status;</li>
        <li>hardship information;</li>
        <li>reasons for your contribution;</li>
        <li>Access assistance amount.</li>
      </ul>
    </div>
  </div>
</section>"""

def extra_css():
    return """<style>
/* ── Access Mediation page-specific styles ── */
.calc-section{background:var(--sage-pale,#ffffff);padding:52px 0}
.lede-sm{color:var(--ink-soft,#4a4f5a);margin-bottom:24px;font-size:.97rem;line-height:1.6;max-width:62ch}
#access-calc-root{min-height:160px}
.notice{padding:16px 20px;background:#fff3cd;border-left:4px solid #f0a500;border-radius:6px;font-size:.9rem}

/* key takeaway */
.access-kt{margin:32px 0 8px}
.access-kt .kt-label{margin:0 0 6px;font-size:.78rem;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--sage-deep,#294b8e)}
/* related cards */
.access-related{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:16px;list-style:none;padding:0;margin:0}
.access-related a{display:flex;flex-direction:column;gap:6px;height:100%;padding:18px 20px;background:#fff;border:1px solid var(--line,#e0ddd8);border-radius:10px;text-decoration:none;color:inherit;transition:border-color .15s,box-shadow .15s,transform .15s}
.access-related a:hover{border-color:var(--sage-deep,#294b8e);box-shadow:0 6px 18px rgba(27,49,94,.08);transform:translateY(-2px)}
.access-related strong{color:var(--sage-deep,#294b8e)}
.access-related span{color:var(--ink-soft,#666);font-size:.9rem;line-height:1.5}

/* band accordion */
.band-accordion{margin-top:28px;border:1px solid var(--line,rgba(27,49,94,.14));border-radius:10px;overflow:hidden;background:#fff}
.band-accordion-toggle{list-style:none;padding:14px 18px;font-size:.93rem;font-weight:600;color:var(--sage-deep,#294b8e);cursor:pointer;display:flex;justify-content:space-between;align-items:center}
.band-accordion-toggle::-webkit-details-marker{display:none}
details[open] .band-acc-arr{transform:rotate(180deg)}
.band-acc-arr{display:inline-block;transition:transform .2s;font-size:.8rem}
.band-accordion-body{padding:0 18px 18px}

/* steps */
.steps-section{padding:64px 0}
.steps-section h2{margin-bottom:28px}
.steps-grid{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:20px;counter-reset:none}
.step{position:relative;background:#fff;border:1px solid var(--line,rgba(27,49,94,.14));border-radius:14px;padding:24px 22px;display:flex;flex-direction:column;gap:10px}
.step-num{width:40px;height:40px;border-radius:50%;background:var(--sage-deep,#294b8e);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:1rem}
.step h3{margin:4px 0 0;font-size:1.02rem;line-height:1.35}
.step p{margin:0;color:var(--ink-soft,#4a4f5a);font-size:.9rem;line-height:1.6}

/* who + assets */
.who-section{padding:64px 0;background:var(--sand,#f5f9ff)}
.who-grid{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(0,1fr);gap:40px;align-items:start}
.who-main h2{margin-bottom:14px}
.who-main p{line-height:1.65}
.check-grid{list-style:none;padding:0;margin:14px 0 20px;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.check-grid li{background:#fff;border:1px solid var(--line,rgba(27,49,94,.14));border-radius:10px;padding:12px 14px 12px 42px;position:relative;font-size:.93rem;line-height:1.4}
.check-grid li::before{content:"\\2713";position:absolute;left:14px;top:11px;width:18px;height:18px;border-radius:50%;background:var(--sage-deep,#294b8e);color:#fff;font-size:.7rem;font-weight:700;display:flex;align-items:center;justify-content:center}
.who-key{padding:12px 16px;border-left:4px solid var(--sage-deep,#294b8e);background:#fff;border-radius:0 8px 8px 0}
.who-side{display:flex;flex-direction:column;gap:16px}
.asset-callout{background:#fff;border:1.5px solid var(--sage-deep,#294b8e);border-radius:14px;padding:24px}
.asset-callout h3{margin:0 0 10px;font-size:1.05rem;color:var(--sage-deep,#294b8e)}
.asset-callout p{margin:0 0 10px;font-size:.92rem;color:var(--ink-soft,#4a4f5a);line-height:1.6}
.asset-callout p:last-child{margin:0}
.who-note{background:#fff;border:1px solid var(--line,rgba(27,49,94,.14));border-radius:14px;padding:18px 22px}
.who-note p{margin:0;font-size:.88rem;color:var(--ink-soft,#4a4f5a);line-height:1.6}
.who-note a{color:var(--sage-deep,#294b8e);font-weight:600}

/* privacy */
.privacy-section{padding:64px 0}
.privacy-panel{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:40px;align-items:center;background:var(--sage-deep,#294b8e);color:#fff;border-radius:18px;padding:40px}
.privacy-panel h2{color:#fff;margin-bottom:12px}
.privacy-intro p{color:rgba(255,255,255,.88);line-height:1.6}
.privacy-intro p{margin:0 0 12px}
.privacy-foot{font-size:.93rem}
.privacy-intro strong{color:#fff}
.privacy-list{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
.privacy-list li{background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);border-radius:10px;padding:12px 14px 12px 40px;position:relative;font-size:.92rem;line-height:1.35;color:#fff}
.privacy-list li::before{content:"";position:absolute;left:14px;top:50%;width:14px;height:14px;transform:translateY(-50%);background:no-repeat center/contain url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='2.4' stroke-linecap='round' stroke-linejoin='round'%3E%3Crect x='4' y='11' width='16' height='10' rx='2'/%3E%3Cpath d='M8 11V7a4 4 0 0 1 8 0v4'/%3E%3C/svg%3E")}

/* shared data-table */
.data-table{width:100%;border-collapse:collapse;font-size:.9rem}
.data-table th{background:var(--sage-deep,#294b8e);color:#fff;padding:10px 14px;text-align:left}
.data-table td{padding:10px 14px;border-bottom:1px solid rgba(27,49,94,.1);vertical-align:top}
.data-table tfoot td{font-size:.8rem;color:var(--ink-soft,#4a4f5a);padding:10px 14px;border-bottom:none;font-style:italic}
.data-table tbody tr:nth-child(even) td{background:#f8fbf8}
.table-scroll{overflow-x:auto;margin:12px 0 0}

@media(max-width:960px){
  .steps-grid{grid-template-columns:repeat(2,minmax(0,1fr))}
  .who-grid,.privacy-panel{grid-template-columns:1fr;gap:28px}
}
@media(max-width:600px){
  .calc-section,.steps-section,.who-section,.privacy-section{padding:40px 0}
  .steps-grid,.check-grid,.privacy-list{grid-template-columns:1fr}
  .privacy-panel{padding:28px 22px}
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
<section class="phero" style="background-color:var(--sand);background-image:linear-gradient(to right,rgba(245,249,255,1) 0%,rgba(245,249,255,.95) 45%,rgba(245,249,255,.8) 100%),url('/assets/images/hero-our-fees.jpg');background-size:cover;background-position:center 40%">
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
                 f'<div class="answer access-kt reveal"><p class="kt-label">Key takeaway</p><p>{ANSWER}</p></div>'
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

    # Related guides — Access Mediation SEO cluster
    html_doc += """
<section class="blog-related" style="background:var(--cream,#faf8f5);padding:3rem 0">
<div class="wrap">
<h2 style="margin-bottom:1.5rem">Related guides</h2>
<ul class="access-related">
<li><a href="/cant-afford-mediation/"><strong>Can't afford mediation?</strong><br><span>All your options in Australia — FRC, community FDR, Legal Aid, and reduced-fee private</span></a></li>
<li><a href="/is-family-mediation-free-australia/"><strong>Is family mediation free?</strong><br><span>When it can be free, when it's subsidised, and what to do if neither applies</span></a></li>
<li><a href="/who-pays-mediation-one-person-earns-more/"><strong>Who pays when one person earns more?</strong><br><span>How individual assessment works — your partner's income doesn't set your fee</span></a></li>
<li><a href="/does-mediation-have-to-be-paid-50-50/"><strong>Does mediation have to be paid 50/50?</strong><br><span>No — here's how fee arrangements actually work</span></a></li>
<li><a href="/asset-rich-cash-poor-mediation/"><strong>Asset rich, cash poor</strong><br><span>Owning a home doesn't mean you have accessible cash — how the assessment handles this</span></a></li>
<li><a href="/family-relationship-centre-vs-private-mediation/"><strong>FRC vs private mediation</strong><br><span>An honest side-by-side comparison</span></a></li>
<li><a href="/legal-aid-vs-private-mediation/"><strong>Legal Aid vs private mediation</strong><br><span>What Legal Aid covers — and what to do if you don't qualify</span></a></li>
<li><a href="/low-cost-family-mediation-australia/"><strong>Low-cost family mediation</strong><br><span>All lower-cost options compared on cost, wait time, and complexity</span></a></li>
</ul>
</div>
</section>
"""

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
