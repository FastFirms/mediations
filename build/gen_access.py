#!/usr/bin/env python3
"""
Generate /access-mediation/ — the Access Mediation landing page.

Access Mediation is a limited reduced-contribution pathway for eligible
participants who cannot afford the standard mediation contribution.

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
     "calculator above — it takes about two minutes."),

    ("How are the contributions calculated?",
     "Your contribution is based on your personal income band, adjusted for assets, dependants "
     "(3 or more), concession status, or material hardship. The maximum automatic reduction is "
     "one band. Any adjustment is applied to your contribution only — your partner's assessment "
     "is completely separate and private."),

    ("Will my partner know my contribution or financial details?",
     "No. Each participant's financial assessment is entirely private. Your income band, assets, "
     "hardship circumstances and contribution are never shared with the other participant, their "
     "lawyer, or anyone outside authorised staff. Participants may have different contributions — "
     "but neither party is told the financial basis for the other's contribution."),

    ("Does financial eligibility guarantee a booking?",
     "No. Access appointments are limited and allocated on a first-come, first-served basis "
     "within monthly capacity. Financial eligibility confirms your indicative contribution only — "
     "mediation suitability (including any family safety screening) is assessed separately by our "
     "staff before a booking is confirmed."),

    ("What is the standard contribution and what does Access Mediation save me?",
     "The standard individual contribution for a 3-hour mediation session is $1,500 + GST. "
     "Access contributions range from $495 to $1,295 + GST per person. At Band 1, Access "
     "Mediation provides $1,005 in assistance per participant (the gap between $495 and the "
     "$1,500 standard). This assistance is funded by Mediations Australia and is not a "
     "government subsidy."),

    ("What if I need a Section 60I Certificate?",
     "Section 60I certificates are issued following a recognised Family Dispute Resolution (FDR) "
     "process. If you indicate that you require one, our team will discuss whether your matter "
     "is eligible for FDR and explain the process. We cannot issue a certificate in advance or "
     "guarantee one will be issued — it depends on the conduct of the process."),

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


def band_table():
    rows = [
        ("Band 1", "$0 – $50,000",        "$495",   "$1,005"),
        ("Band 2", "$50,001 – $75,000",   "$695",   "$805"),
        ("Band 3", "$75,001 – $100,000",  "$895",   "$605"),
        ("Band 4", "$100,001 – $125,000", "$1,095", "$405"),
        ("Band 5", "$125,001 – $150,000", "$1,295", "$205"),
        ("Standard", "Above $150,000",    "$1,500", "—"),
    ]
    row_html = "".join(
        f'<tr><td><strong>{b}</strong></td><td>{i}</td>'
        f'<td><strong>{c} + GST</strong></td><td>{a}</td></tr>'
        for b, i, c, a in rows
    )
    return f"""<div class="table-scroll">
<table class="data-table">
  <caption>Access Mediation — indicative contributions per participant (3-hour session)</caption>
  <thead>
    <tr>
      <th>Band</th>
      <th>Personal gross annual income</th>
      <th>Your contribution (ex GST)</th>
      <th>Access assistance</th>
    </tr>
  </thead>
  <tbody>{row_html}</tbody>
  <tfoot>
    <tr><td colspan="4">Contributions are per participant for a 3-hour session. Assets, dependants, concession status and hardship may adjust your band. All figures exclude GST.</td></tr>
  </tfoot>
</table>
</div>"""


def how_it_works():
    steps = [
        ("1", "Check your eligibility",
         "Use our two-minute calculator to receive your indicative contribution based on your "
         "personal financial circumstances. Your partner is not involved in this step."),
        ("2", "Submit your application",
         "Complete the short application form. We ask for your contact details, a brief description "
         "of your matter, and the other participant's contact details so we can send an invitation. "
         "No financial documents are required at this stage."),
        ("3", "We confirm and schedule",
         "Our team reviews your application within 1–2 business days, confirms your contribution "
         "and checks mediation suitability. We then contact both participants to arrange a session."),
        ("4", "Mediation session",
         "Your Access session runs for up to 3 hours with an accredited family mediator. A "
         "50% deposit secures your booking; the balance is due at the session. If you reach "
         "agreement, we can assist with documentation of parenting plans or consent orders."),
    ]
    items = "".join(
        f'<div class="step reveal">'
        f'<div class="step-num">{n}</div>'
        f'<div class="step-body"><h3>{t}</h3><p>{d}</p></div>'
        f'</div>'
        for n, t, d in steps
    )
    return f'<section class="steps-section"><div class="wrap"><h2>How Access Mediation works</h2>{items}</div></section>'


def calculator_section():
    """Placeholder div that access-calc.js mounts the multi-step calculator into."""
    return f"""<section class="calc-section" id="check-eligibility">
  <div class="wrap-narrow">
    <h2>Check your indicative contribution</h2>
    <p class="lede-sm">Answer a few questions about your personal financial circumstances. Takes about two minutes. Your answers are not shared with the other participant.</p>
    <div id="access-calc-root" data-calc="access">
      <!-- Access Mediation calculator mounts here (access-calc.js) -->
      <noscript>
        <div class="notice">
          Please enable JavaScript to use the eligibility calculator, or call us on
          <a href="{PHONE_HREF}">{PHONE}</a> and we will assess your eligibility over the phone.
        </div>
      </noscript>
    </div>
  </div>
</section>"""


def eligibility_section():
    return f"""<section class="elig-section reveal">
  <div class="wrap">
    <h2>Who can apply for Access Mediation?</h2>
    <p>Access Mediation is a limited pathway — not a universal right. Each application is reviewed individually. You may be eligible if:</p>
    <ul class="check-list">
      <li>Your personal gross annual income is below $150,000</li>
      <li>Your accessible assets do not substantially exceed your income-band contribution</li>
      <li>Your matter involves family law — parenting arrangements, property settlement, or both</li>
      <li>You do not already have a funded FDR pathway (e.g. Legal Aid) available to you</li>
    </ul>
    <p>Your contribution may be reduced by one band if you have three or more dependants, hold a current concession card, or face genuine material hardship. Both adjustments cannot stack — the maximum automatic reduction is one band.</p>
    <p>Access Mediation is <strong>not available</strong> for purely commercial, employment, or neighbourhood disputes, or where a participant has accessible assets well above $150,000.</p>
    <div class="elig-note">
      <strong>Family violence and safety.</strong> If there are safety concerns, family violence, or a significant power imbalance, call us on
      <a href="{PHONE_HREF}">{PHONE}</a> before applying. We will discuss safety screening, whether mediation is appropriate, and what protections can be put in place.
    </div>
  </div>
</section>"""


def privacy_note():
    return """<section class="privacy-section reveal">
  <div class="wrap-narrow">
    <h2>Your financial information stays private</h2>
    <p>Each participant&#8217;s financial assessment is completely separate and confidential. Your income band, assets, hardship circumstances, concession status, and contribution are never shared with:</p>
    <ul>
      <li>The other participant or their legal representative</li>
      <li>Anyone outside authorised Mediations Australia staff</li>
      <li>Any third-party service, analytics platform, or advertising system</li>
    </ul>
    <p>Participants may have different contributions. Neither party is told the financial basis for the other&#8217;s assessment. Your application is held securely and used only to assess eligibility and arrange your session.</p>
  </div>
</section>"""


def extra_css():
    return """<style>
/* ── Access Mediation page-specific styles ── */
.calc-section{background:var(--sage-pale,#f1f5f1);padding:60px 0}
.lede-sm{color:var(--muted);margin-bottom:28px;font-size:.97rem}
#access-calc-root{min-height:200px}
.notice{padding:16px 20px;background:#fff3cd;border-left:4px solid #f0a500;border-radius:6px;font-size:.9rem}
.steps-section{padding:60px 0}
.steps-section h2{margin-bottom:32px}
.step{display:flex;gap:20px;align-items:flex-start;margin-bottom:28px}
.step-num{width:40px;height:40px;border-radius:50%;background:var(--green,#1e6040);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:1rem;flex-shrink:0;margin-top:2px}
.step-body h3{margin:0 0 6px;font-size:1.05rem}
.step-body p{margin:0;color:var(--muted);font-size:.93rem;line-height:1.6}
.elig-section{padding:60px 0;background:var(--sage-pale,#f1f5f1)}
.elig-section h2{margin-bottom:16px}
.elig-section>div>p{font-size:.95rem;line-height:1.6}
.check-list{list-style:none;padding:0;margin:16px 0}
.check-list li{padding-left:28px;position:relative;margin-bottom:10px;font-size:.95rem;line-height:1.5}
.check-list li::before{content:"✓";position:absolute;left:0;color:var(--green,#1e6040);font-weight:700}
.elig-note{margin-top:24px;padding:16px 20px;background:#fff;border-left:4px solid var(--green,#1e6040);border-radius:0 8px 8px 0;font-size:.9rem;line-height:1.6}
.privacy-section{padding:50px 0}
.privacy-section h2{margin-bottom:12px}
.privacy-section ul{margin:16px 0;padding-left:24px}
.privacy-section li{margin-bottom:8px;font-size:.95rem;line-height:1.5}
.data-table{width:100%;border-collapse:collapse;font-size:.9rem}
.data-table th{background:var(--green,#1e6040);color:#fff;padding:10px 14px;text-align:left}
.data-table td{padding:10px 14px;border-bottom:1px solid #e8efe9;vertical-align:top}
.data-table tfoot td{font-size:.8rem;color:var(--muted);padding:10px 14px;border-bottom:none}
.data-table tbody tr:nth-child(even) td{background:#f8fbf8}
.table-scroll{overflow-x:auto;margin:24px 0 32px}
.body-section{padding:50px 0}
.body-section h2{margin-bottom:8px}
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
      <a href="#check-eligibility" class="btn btn-primary">Check My Eligibility <span class="arr">&#8595;</span></a>
      <a href="{PHONE_HREF}" class="btn btn-ghost">Call {PHONE}</a>
    </div>
  </div>
</section>"""

    html_doc += (f'<div class="wrap-narrow">'
                 f'<div class="answer reveal"><p><strong>In short:</strong> {ANSWER}</p></div>'
                 f'</div>')

    html_doc += f'<section class="body-section reveal"><div class="wrap"><h2>Access contribution bands</h2>{band_table()}</div></section>'
    html_doc += calculator_section()
    html_doc += how_it_works()
    html_doc += eligibility_section()
    html_doc += privacy_note()
    html_doc += faq_html(QA, heading="Access Mediation FAQs")
    html_doc += cta_band(
        "Ready to check your eligibility?",
        "Use our two-minute calculator above, or call us to discuss your situation confidentially. "
        "Access places are limited — check early.",
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
