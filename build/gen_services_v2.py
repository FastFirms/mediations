#!/usr/bin/env python3
"""Cornerstone-depth service pages.

Each page follows the exact same conventions as the 42 blog cornerstones:
- Keyword-first H1
- Hero with lede
- Key-takeaway answer box (AEO)
- TOC with jump anchors
- 6-8 substantive sections with H2s
- 1+ data table where the topic supports it
- 6-8 inline CTAs woven through the body
- FAQ block with FAQPage schema
- Related guides/services grid
- Closing CTA band
- ≥2 authoritative external citations (.gov.au / .edu / peak-body)
- ~1,400-1,800 words of substantive, query-satisfying content

Built carefully — quality not speed. Three pages this batch for review.
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, faq_html, cta_band,
                       org_schema, faq_schema, breadcrumb_schema, service_schema,
                       BOOK_URL, PHONE, PHONE_HREF, DOMAIN)
from authority_sources import cite

OUT = "/home/claude/mediations/site"

# ---- Reusable component helpers ----

def inline_cta(text):
    """Punctuating CTA between sections."""
    return f'''<aside class="inline-cta"><p>{text}</p><a href="{BOOK_URL}" class="btn btn-primary">Book a free consultation <span class="arr">→</span></a></aside>'''

def key_takeaway(text):
    """AEO answer box — direct answer to the page's question in 1-2 sentences."""
    return f'''<div class="answer reveal"><h2 style="margin-bottom:8px;font-size:1.05rem;text-transform:uppercase;letter-spacing:.08em;color:var(--sage-deep)">Key takeaway</h2><p>{text}</p></div>'''

def callout(heading, body):
    """Editorial callout box."""
    return f'''<div class="callout"><h3>{heading}</h3><p>{body}</p></div>'''

def toc(items):
    """Jump-anchor table of contents."""
    lis = "\n".join(f'<li><a href="#{anchor}">{label}</a></li>' for anchor, label in items)
    return f'''<nav class="toc" aria-label="On this page"><h2>On this page</h2><ul>{lis}</ul></nav>'''

def related_grid(items):
    """Bottom-of-page related links grid."""
    cards = "\n".join(
        f'<a href="/{slug}/" class="related-card"><h3>{title}</h3></a>'
        for slug, title in items
    )
    return f'''<section class="sec-tint"><div class="wrap-narrow"><h2>Related guides &amp; services</h2><div class="related-grid">{cards}</div></div></section>'''

def service_page(slug, title, desc, breadcrumb_label, eyebrow, h1_html, lede, toc_items,
                 takeaway, body_html, faq_items, related_items, schema_extra=None):
    """Generate one cornerstone-depth service page."""
    schema = [org_schema(), breadcrumb_schema([("Home",""),(breadcrumb_label,slug)]),
              service_schema(title, desc, slug), faq_schema(faq_items)]
    if schema_extra: schema.extend(schema_extra)

    d = head(title, desc, slug, extra_schema=schema) + nav()
    d += f'''<main id="main">
{crumb_html([("Home",""),(breadcrumb_label,None)])}
<section class="phero"><div class="phero-blob"></div><div class="wrap">
<span class="eyebrow"><span class="pulse"></span>{eyebrow}</span>
<h1>{h1_html}</h1>
<p class="lede">{lede}</p>
<div class="phero-cta">
<a href="{BOOK_URL}" class="btn btn-primary">Book a free consultation <span class="arr">→</span></a>
<a href="{PHONE_HREF}" class="btn btn-ghost">Call {PHONE}</a>
</div></div></section>

<section class="sec"><div class="wrap-narrow">
{takeaway}
{toc(toc_items)}
{body_html}
</div></section>

<section class="sec-tint"><div class="wrap-narrow">
{faq_html(faq_items, heading=f"{breadcrumb_label} \u2014 frequently asked")}
</div></section>

{related_grid(related_items)}
'''
    d += cta_band(f"Ready to <em>resolve this</em>?",
                  "Book a fixed-fee consultation and we'll explain how mediation applies to your situation.")
    d += "</main>" + page_end()

    os.makedirs(os.path.join(OUT, slug), exist_ok=True)
    open(os.path.join(OUT, slug, "index.html"), "w").write(d)
    print(f"  built {slug}")


# =====================================================================
# 1. FAMILY LAW MEDIATION — the flagship service page
# =====================================================================
service_page(
    slug="family-law-mediation",
    title="Family Law Mediation in Australia | Mediations Australia",
    desc="Family law mediation in Australia explained: how it works, what it covers, costs, and how to resolve parenting and property matters without court. Free consultation.",
    breadcrumb_label="Family Law Mediation",
    eyebrow="Our core service",
    h1_html='Family Law Mediation \u2014 <em>resolve it without court</em>.',
    lede="Family law mediation is how most separating Australians resolve parenting, property and financial matters \u2014 without years in court, without crushing legal fees, and with the agreement in their own hands. Our nationally accredited mediators have helped thousands of families do exactly that.",
    toc_items=[
        ("what-is","What is family law mediation?"),
        ("when","When is mediation appropriate?"),
        ("how","How the process works"),
        ("issues","Issues we can resolve"),
        ("costs","What it costs"),
        ("vs-court","Mediation vs court"),
        ("binding","Making the agreement binding"),
        ("get-started","How to get started"),
    ],
    takeaway=key_takeaway(
        "Family law mediation is a confidential, structured process where a nationally accredited mediator helps separating partners reach agreement on parenting, property and financial matters. It's required before most parenting court applications under the Family Law Act, resolves around 90% of matters in one to two sessions, and costs a small fraction of going to court \u2014 typically a few thousand dollars total rather than tens of thousands per side."
    ),
    body_html=f"""
<h2 id="what-is">What is family law mediation?</h2>
<p>Family law mediation is a confidential process led by a neutral, accredited mediator \u2014 a trained professional who is not a judge and not your lawyer. Their job is to help you and your former partner work through the issues that come with separation: where the children will live, how time will be shared, how property and superannuation will be divided, and any ongoing financial support. The mediator doesn't impose a decision. <strong>You design the outcome you can both live with.</strong></p>

<p>It's recognised across the Australian system as the default path for separating families. Under the {cite("family_law_act")}, you must generally attempt family dispute resolution before applying to court for a parenting order \u2014 and the courts strongly expect genuine pre-action efforts on property matters too. The {cite("ag_fdr")} sets the framework, and accredited mediators issue the {esc("Section 60I certificate")} the court requires.</p>

<p>Critically, mediation isn't a soft, talk-it-out exercise. It's a structured process with phases, ground rules, and a clear path to a written agreement \u2014 conducted by professionals who understand both the law and the human dynamics of separation.</p>
""" + inline_cta("Wondering if mediation fits your situation? Book a fixed-fee consultation \u2014 we'll give you an honest assessment.") + """

<h2 id="when">When is mediation appropriate?</h2>
<p>For the vast majority of separating couples, mediation is the right first step \u2014 even when conflict feels high. It works particularly well when:</p>
<ul>
  <li>You both genuinely want to resolve things rather than fight</li>
  <li>There are children, and protecting the co-parenting relationship matters</li>
  <li>There are assets to divide and you'd rather they go to your family than to lawyers</li>
  <li>You want to keep your business private and out of public court records</li>
  <li>You want to move forward with your life sooner rather than later</li>
</ul>

<p><strong>Mediation may not be appropriate</strong> where there is family violence or a serious safety risk, where one party refuses to participate genuinely or to disclose financial information, or where urgent court orders are needed. We assess this honestly at the consultation \u2014 if mediation isn't the right path for you, we'll tell you. <a href="/domestic-violence-and-family-law/">See family violence and family law \u2192</a></p>
""" + callout("High conflict doesn't rule out mediation",
   "Counter-intuitively, mediation often works better than court for high-conflict separations \u2014 the structure and shuttle techniques contain conflict more effectively than an adversarial hearing. See our high-conflict mediation guide.") + """

<h2 id="how">How the process works</h2>
<p>The process is more structured than people expect. Here's what actually happens:</p>

<ol>
  <li><strong>Initial consultation</strong> \u2014 a fixed-fee call to understand your situation, confirm mediation is appropriate, and outline how it would work for you.</li>
  <li><strong>Intake assessment</strong> \u2014 each party meets separately with the mediator to discuss the issues, identify any safety concerns, and prepare for the session.</li>
  <li><strong>Pre-session preparation</strong> \u2014 you gather the relevant information (financial disclosure, what you want for the children, any documents that matter) so the session is productive.</li>
  <li><strong>The mediation session</strong> \u2014 the substantive day. You work through the issues with the mediator's guidance \u2014 in the same room, or in <a href="/shuttle-mediation-guide/">separate rooms ("shuttle mediation")</a> if that's preferable.</li>
  <li><strong>Heads of Agreement</strong> \u2014 the resolution is documented while it's fresh, so nothing is left to memory.</li>
  <li><strong>Formalisation</strong> \u2014 the agreement is made legally binding through <a href="/consent-orders/">consent orders</a> or a <a href="/financial-agreements-mediation/">binding financial agreement</a>.</li>
</ol>

<p>The session itself typically runs for half a day to a full day. Around 90% of family matters resolve in one or two sessions, with the rest needing a follow-up.</p>

<h2 id="issues">Issues we can resolve</h2>
<p>Family law mediation covers the full range of matters that arise when a relationship ends:</p>
<ul>
  <li><strong>Parenting arrangements</strong> \u2014 where the children live, how time is shared, decision-making for major issues</li>
  <li><strong>Property settlement</strong> \u2014 dividing assets, debts, the family home, vehicles, and investments</li>
  <li><strong>Superannuation splitting</strong> \u2014 often one of the largest assets and most-overlooked in informal arrangements</li>
  <li><strong>Spousal maintenance</strong> \u2014 financial support where one partner can't adequately support themselves</li>
  <li><strong>Child support</strong> \u2014 private agreements that work alongside or instead of the standard formula</li>
  <li><strong>Business and trust interests</strong> \u2014 sensitive financial matters resolved privately, not in public court records</li>
  <li><strong>De facto separations</strong> \u2014 the same property rights as married couples, with the same need for fair resolution</li>
</ul>
""" + inline_cta("Got more than one issue to resolve? Mediation handles them together in a single coherent process.") + f"""

<h2 id="costs">What it costs</h2>
<p>This is the question everyone asks, and the news is good. Private family mediation is dramatically cheaper than court \u2014 and the savings stay with your family.</p>

<figure class="tbl"><table><caption>Mediation vs court \u2014 typical costs</caption>
<thead><tr><th>Path</th><th>Typical total cost</th><th>Time to resolution</th></tr></thead>
<tbody>
<tr><td><strong>Mediation</strong> (full process, shared)</td><td>$3,000\u2013$7,000</td><td>1\u20133 sessions over weeks</td></tr>
<tr><td>Mediation + consent orders</td><td>$5,000\u2013$9,000</td><td>Add 2\u20136 weeks for filing</td></tr>
<tr><td>Contested litigation (each party)</td><td>$50,000\u2013$200,000+</td><td>1\u20133 years</td></tr>
</tbody></table></figure>

<p>Mediation costs are usually shared between the parties, so your share is roughly half the headline figure. Our consultations are <strong>fixed-fee</strong>, so you'll know what you're committing to before you commit. <a href="/our-fee-structure/">See our fee structure \u2192</a></p>

<p>Government-funded <a href="https://www.familyrelationships.gov.au/" target="_blank" rel="noopener">Family Relationship Centres</a> offer mediation at free or low cost for parenting matters \u2014 valuable, but typically with longer wait times and more limited capacity for complex financial matters.</p>

<h2 id="vs-court">Mediation vs court</h2>
<p>The comparison isn't really about which is "better" \u2014 they're tools for different situations. But for the vast majority of separating families, mediation is the smarter first move. Here's why:</p>

<ul>
  <li><strong>You stay in control of the outcome.</strong> In court, a judge decides. In mediation, you and your former partner decide.</li>
  <li><strong>It's far cheaper.</strong> Often by a factor of 10\u201320x compared to a contested matter.</li>
  <li><strong>It's faster.</strong> Weeks rather than years.</li>
  <li><strong>It's private.</strong> Court files become public record; mediation is confidential.</li>
  <li><strong>It protects co-parenting.</strong> Adversarial litigation damages the relationship you need to keep functioning for years to come.</li>
  <li><strong>Outcomes hold better.</strong> Agreements people design themselves are more likely to be followed than orders imposed on them.</li>
</ul>

<p>Court has a legitimate place \u2014 where there's family violence, urgent safety concerns, refusal to participate or disclose, or genuinely intractable legal questions. The point isn't to avoid court at all costs; it's to avoid <em>unnecessary</em> court. <a href="/mediate-or-litigate/">See the full comparison \u2192</a></p>
""" + inline_cta("Most families never need a courtroom. Find out if yours is one of them \u2014 book a free consultation.") + """

<h2 id="binding">Making the agreement binding</h2>
<p>An agreement reached in mediation isn't automatically legally binding \u2014 and this is the step many people overlook. To give the agreement the force of a court order (and to close off future claims), it needs to be formalised through one of two paths:</p>

<ul>
  <li><strong>Consent orders</strong> \u2014 filed with the Federal Circuit and Family Court, which reviews and approves the agreement, giving it the same status as if a judge had ordered it. The standard path for both parenting and property matters. <a href="/consent-orders/">See consent orders \u2192</a></li>
  <li><strong>Binding financial agreement (BFA)</strong> \u2014 a private contract between the parties, requiring independent legal advice for each party. Useful particularly for property and financial matters where parties want to avoid court involvement entirely. <a href="/financial-agreements-mediation/">See financial agreements \u2192</a></li>
</ul>

<p>We handle the formalisation step as part of the mediation process \u2014 you don't reach an agreement and then have to find separate lawyers to make it stick. <a href="/bfa-or-consent-orders/">See which option suits you \u2192</a></p>

<h2 id="get-started">How to get started</h2>
<p>The first step is a fixed-fee consultation. We'll listen to your situation, explain how mediation would apply, give you an honest assessment of whether it's the right path, and \u2014 if you proceed \u2014 schedule the intake and mediation session. There's no obligation and no surprises. Many of the people we help are referred by their own family lawyers, who know what court costs in money and wellbeing.</p>
""",
    faq_items=[
        ("Is family law mediation compulsory in Australia?",
         "For most parenting matters, yes \u2014 you must attempt family dispute resolution and obtain a Section 60I certificate before applying to court, unless an exemption applies. For property matters, mediation isn't strictly compulsory but the courts expect genuine pre-action efforts to resolve."),
        ("How much does family law mediation cost?",
         "Private mediation typically costs $3,000\u2013$7,000 total, usually shared between the parties \u2014 so each person's share is around half that. Free and low-cost options are available through Family Relationship Centres for parenting matters."),
        ("How long does the mediation process take?",
         "The mediation session itself typically runs half a day to a full day. Around 90% of family matters resolve in one or two sessions \u2014 a matter of weeks rather than the one to three years a contested court case can take."),
        ("Do I need a lawyer to attend mediation?",
         "No. Lawyers aren't required, though legal advice before or after can be wise for complex matters. Many of our mediators are also experienced family lawyers, so legal awareness is in the room either way."),
        ("Is everything said in mediation confidential?",
         "Yes. Mediation is conducted on a 'without prejudice' basis, meaning what's said generally can't be used later in court. That confidentiality is exactly what lets everyone speak openly and reach agreement."),
        ("What happens if mediation doesn't work?",
         "You can still proceed to court \u2014 the mediator will issue a Section 60I certificate confirming you attempted mediation, and any partial agreements reached can still be honoured. Mediation isn't an all-or-nothing risk."),
        ("Can family violence rule out mediation?",
         "Where there's family violence or a serious safety risk, mediation may not be appropriate \u2014 and the law recognises this with exemptions from the compulsory mediation requirement. We assess this honestly at the initial consultation."),
    ],
    related_items=[
        ("property-settlement-mediation","Property Settlement Mediation"),
        ("parenting-plan-mediation","Parenting Plan Mediation"),
        ("section-60i-certificates","Section 60I Certificates"),
        ("consent-orders","Consent Orders"),
        ("how-mediation-works","How Mediation Works"),
        ("preparing-for-mediation","Preparing for Mediation"),
        ("mediate-or-litigate","Mediate or Litigate?"),
        ("high-conflict-mediation","High-Conflict Mediation"),
    ],
)

# =====================================================================
# 2. PROPERTY SETTLEMENT MEDIATION
# =====================================================================
service_page(
    slug="property-settlement-mediation",
    title="Property Settlement Mediation in Australia | Mediations Australia",
    desc="Resolve your property settlement through accredited mediation \u2014 divide assets, super and debts fairly without court. Fixed-fee consultations, nationally available.",
    breadcrumb_label="Property Settlement Mediation",
    eyebrow="Service",
    h1_html='Property Settlement Mediation \u2014 <em>divide it fairly, finally</em>.',
    lede="Property settlement is the financial settlement of separation \u2014 dividing the assets, debts, superannuation and businesses you've built. Mediation resolves it faster, far more cheaply, and with the agreement in your hands rather than a judge's. The savings stay with your family, not your lawyers.",
    toc_items=[
        ("what-is","What is property settlement mediation?"),
        ("when","When should you mediate?"),
        ("how","How the process works"),
        ("framework","The four-step framework"),
        ("what-included","What's included in the pool"),
        ("super","Superannuation and complex assets"),
        ("costs","Costs and timeframes"),
        ("binding","Making it binding"),
    ],
    takeaway=key_takeaway(
        "Property settlement mediation resolves the financial side of separation \u2014 dividing assets, superannuation, debts and businesses \u2014 through structured negotiation with an accredited mediator. It applies the same four-step framework a court would use (asset pool \u2192 contributions \u2192 future needs \u2192 just and equitable), but in weeks rather than years and at a fraction of the cost. The mediated agreement is then formalised through consent orders or a binding financial agreement."
    ),
    body_html=f"""
<h2 id="what-is">What is property settlement mediation?</h2>
<p>Property settlement mediation is a focused form of <a href="/family-law-mediation/">family law mediation</a> dealing specifically with the financial division of separation \u2014 the assets, debts, superannuation, and any business or trust interests. A nationally accredited mediator helps you and your former partner work through the asset pool, assess contributions and future needs, and reach a settlement that's fair, durable, and legally binding.</p>

<p>It's the path that the {cite("fcfcoa")} actively encourages, and that most experienced family lawyers will recommend as the first move. The reason is simple: contested property litigation can eat 10\u201340% of the asset pool it's fighting over, while mediation typically costs a few thousand dollars. The asset pool you're protecting is exactly the asset pool that gets eroded by going to court.</p>
""" + inline_cta("Want to know what's actually in your asset pool \u2014 and what a fair split looks like? Start with a consultation.") + """

<h2 id="when">When should you mediate?</h2>
<p>The best time to start property mediation is once you both genuinely accept the relationship is over and have a reasonable picture of the asset pool \u2014 but <em>before</em> positions harden, before legal costs mount, and before the asset pool itself starts shrinking through prolonged conflict. Earlier is almost always better. <a href="/property-settlement-after-separation/">See the time limits that apply \u2192</a></p>

<p>It's particularly well-suited when:</p>
<ul>
  <li>There's a meaningful asset pool worth protecting from legal fees</li>
  <li>One or both parties has a business or trust interest (privacy matters)</li>
  <li>Superannuation is a significant asset and needs careful handling</li>
  <li>You want certainty and finality without years of court delays</li>
  <li>You want to preserve a working relationship for any ongoing co-parenting</li>
</ul>

<h2 id="how">How the process works</h2>
<ol>
  <li><strong>Initial consultation</strong> \u2014 we listen, explain the process, and give you a clear picture of how mediation applies to your specific assets.</li>
  <li><strong>Disclosure preparation</strong> \u2014 both parties prepare full financial disclosure: bank statements, super, valuations, business records. This is non-negotiable.</li>
  <li><strong>Pre-mediation intake</strong> \u2014 each party meets separately with the mediator to set expectations and identify priorities.</li>
  <li><strong>The mediation session</strong> \u2014 typically a full day, working through the asset pool and reaching agreement on division.</li>
  <li><strong>Heads of Agreement</strong> \u2014 the deal is documented while it's fresh.</li>
  <li><strong>Formalisation</strong> \u2014 consent orders or binding financial agreement, making it enforceable.</li>
</ol>
""" + callout("Disclosure is non-negotiable",
   "Both parties have a duty of full and frank financial disclosure. Hiding assets doesn't just sink the mediation \u2014 it can lead to a settlement being overturned by a court even years later. Go in transparent and the process works.") + """

<h2 id="framework">The four-step framework</h2>
<p>Mediation isn't a free-for-all \u2014 it applies exactly the same framework a court would use. Understanding this is what stops negotiations becoming a tug-of-war.</p>

<ol>
  <li><strong>Identify the asset pool.</strong> Everything in either name, jointly or individually, including super.</li>
  <li><strong>Assess contributions.</strong> Financial (income, savings, inheritance) and non-financial (homemaking, child-rearing, supporting a partner's career) \u2014 both counted.</li>
  <li><strong>Consider future needs.</strong> Earning capacity, age, health, care of children \u2014 adjusting for the future, not just looking backward.</li>
  <li><strong>Check it's just and equitable.</strong> The final test \u2014 does the overall division feel fair to both, in all the circumstances?</li>
</ol>

<p>There's no automatic 50/50. The result reflects the specifics of your relationship and circumstances. <a href="/what-am-i-entitled-to-in-a-separation-in-australia/">See the four-step framework in detail \u2192</a></p>
""" + inline_cta("Curious what your share would actually look like? Book a consultation \u2014 we'll talk you through it.") + """

<h2 id="what-included">What's included in the asset pool</h2>
<p>The asset pool is everything of value, including:</p>
<ul>
  <li>Real estate \u2014 the family home, investment properties</li>
  <li>Bank accounts, savings, term deposits</li>
  <li>Superannuation balances (yes, super is property under the Family Law Act)</li>
  <li>Investments \u2014 shares, managed funds, cryptocurrency</li>
  <li>Vehicles, boats, valuable personal items</li>
  <li>Business interests, partnership shares, trust entitlements</li>
  <li>Debts and liabilities (these come off the pool, not just the assets)</li>
  <li>Inheritances and gifts received during the relationship (treatment varies under the <a href='https://www.austlii.edu.au/cgi-bin/viewdb/au/legis/cth/consol_act/fla1975114/' target='_blank' rel='noopener'>Family Law Act 1975</a>)</li>
</ul>

<h2 id="super">Superannuation and complex assets</h2>
<p>Superannuation is often the most overlooked major asset. Under the Family Law Act, super can be <strong>split</strong> between partners in a property settlement \u2014 the split amount stays in super (subject to preservation rules) but rebalances retirement security, particularly important where one partner reduced paid work to raise children. <a href="/superannuation-and-divorce/">See superannuation and divorce \u2192</a></p>

<p>For more complex matters \u2014 businesses, family trusts, defined-benefit super, cryptocurrency holdings \u2014 mediation works well because it's <em>flexible</em>. A court has a limited set of orders it can make; in mediation you can craft creative solutions (offsets, staged payouts, retained interests) that a judge wouldn't impose. <a href="/business-in-divorce/">See business in divorce \u2192</a></p>

<h2 id="costs">Costs and timeframes</h2>
<p>Property settlement mediation typically costs $3,000\u2013$7,000 total, usually shared between the parties. The mediation session itself is usually a full day, with most matters resolving in that single day or, sometimes, with a follow-up half-day. The full process from initial consultation to filed consent orders typically takes 4\u201310 weeks. Compare that to one to three years for a contested matter, with each party paying $50,000\u2013$200,000+ in legal fees.</p>
""" + inline_cta("Time is money in property settlement \u2014 both literally. The sooner you start, the more there is to share.") + """

<h2 id="binding">Making the agreement binding</h2>
<p>The agreement reached in mediation isn't automatically enforceable. To give it the force of law (and to close off future claims), it needs to be formalised through either:</p>

<ul>
  <li><strong>Consent orders</strong> \u2014 lodged with the Federal Circuit and Family Court, which reviews and approves the agreement. The standard path; gives the same effect as a judge's order. <a href="/consent-orders/">See consent orders \u2192</a></li>
  <li><strong>Binding financial agreement (BFA)</strong> \u2014 a private contract requiring independent legal advice for each party. Avoids court involvement entirely. <a href="/financial-agreements-mediation/">See financial agreements \u2192</a></li>
</ul>

<p>We manage this step as part of the process \u2014 the agreement you reach is the agreement that gets formalised. <a href="/bfa-or-consent-orders/">Which is right for you? \u2192</a></p>
""",
    faq_items=[
        ("How much does property settlement mediation cost?",
         "Private property settlement mediation typically costs $3,000\u2013$7,000 total, usually shared between the parties. Compare that to $50,000\u2013$200,000+ per side for contested litigation."),
        ("How long does the process take?",
         "Most property matters resolve in a single full-day mediation session, sometimes with a follow-up. The full process from consultation to filed consent orders is typically 4\u201310 weeks."),
        ("Do we have to disclose all our finances?",
         "Yes. Both parties have a legal duty of full and frank financial disclosure. Hiding assets can derail the mediation and lead to a settlement being overturned even years later."),
        ("Is there an automatic 50/50 split?",
         "No. The Family Law Act uses a four-step framework \u2014 asset pool, contributions, future needs, just and equitable \u2014 which produces different results depending on circumstances."),
        ("Can superannuation be split in mediation?",
         "Yes. Super is property under the Family Law Act and can be split through the mediation process, with the split formalised in consent orders or a binding financial agreement."),
        ("What if my ex hides assets?",
         "The disclosure obligation is enforceable. If hidden assets emerge later, a settlement can be set aside. In practice, mediators are alert to inconsistencies and will pause the process where disclosure is incomplete."),
        ("Is the mediated agreement legally binding?",
         "Not automatically. It's made binding through consent orders (court-approved) or a binding financial agreement (private, with independent legal advice). We handle this step for you."),
    ],
    related_items=[
        ("family-law-mediation","Family Law Mediation"),
        ("property-settlement-after-separation","Property Settlement: Complete Guide"),
        ("what-am-i-entitled-to-in-a-separation-in-australia","What Am I Entitled To?"),
        ("consent-orders","Consent Orders"),
        ("financial-agreements-mediation","Financial Agreements"),
        ("superannuation-and-divorce","Superannuation & Divorce"),
        ("business-in-divorce","Business in Divorce"),
        ("preparing-for-mediation","Preparing for Mediation"),
    ],
)

# =====================================================================
# 3. CHILD CUSTODY MEDIATION
# =====================================================================
service_page(
    slug="child-custody-mediation",
    title="Child Custody Mediation in Australia | Mediations Australia",
    desc="Resolve parenting arrangements through accredited mediation \u2014 best-interests focused, court-required for parenting orders. Free consultation, nationally available.",
    breadcrumb_label="Child Custody Mediation",
    eyebrow="Service",
    h1_html='Child Custody Mediation \u2014 <em>child-focused, court-ready</em>.',
    lede="Mediation is the path Australian family law takes by default for parenting matters \u2014 required before court, focused on the child's best interests, and far better at producing arrangements that actually work in everyday life. Our accredited Family Dispute Resolution Practitioners help parents reach durable, child-focused agreements.",
    toc_items=[
        ("what-is","What is child custody mediation?"),
        ("required","Why it's required before court"),
        ("best-interests","The best-interests test"),
        ("how","How the process works"),
        ("what-covered","What gets agreed"),
        ("5050","The truth about 50/50"),
        ("section-60i","Section 60I certificates"),
        ("get-started","Getting started"),
    ],
    takeaway=key_takeaway(
        "Child custody mediation \u2014 properly called Family Dispute Resolution \u2014 is the required first step before parents can apply to court for a parenting order in Australia. An accredited Family Dispute Resolution Practitioner helps parents agree workable arrangements focused on the children's best interests, covering where the children live, time with each parent, decision-making and communication. Most parents resolve matters at mediation; for those who can't, a Section 60I certificate allows the matter to proceed to court."
    ),
    body_html=f"""
<h2 id="what-is">What is child custody mediation?</h2>
<p>Despite the everyday term "custody", Australian family law no longer uses that word \u2014 it talks about "parental responsibility" and "spending time with" each parent. What people search for as <em>child custody mediation</em> is, technically, <strong>Family Dispute Resolution (FDR)</strong>: a structured process where parents work through parenting arrangements with the help of an accredited Family Dispute Resolution Practitioner.</p>

<p>The process is recognised across the {cite("ag_fdr")} framework. It's confidential, structured, and focused entirely on what's in the children's best interests \u2014 not on what either parent feels they "deserve". For the vast majority of separating parents, it's both the legally required path and the one that produces arrangements children actually thrive under.</p>
""" + inline_cta("Want a workable parenting arrangement \u2014 not a court fight? Book a consultation with an accredited practitioner.") + """

<h2 id="required">Why it's required before court</h2>
<p>Under the Family Law Act, you must generally attempt Family Dispute Resolution and obtain a Section 60I certificate before you can file a parenting application in court \u2014 unless an exemption applies. This isn't bureaucracy. It reflects a deliberate policy: children's matters should be resolved cooperatively wherever safe, because litigation damages the co-parenting relationship the children depend on long after the case ends.</p>

<p>Exemptions apply where there is family violence or risk of it, child abuse or risk of it, urgency, or where a party can't participate effectively. <a href="/is-family-law-mediation-compulsory/">See the exemptions in detail \u2192</a></p>
""" + callout("Genuine attempt matters",
   "Turning up isn't enough. The law requires a genuine attempt at resolution \u2014 listening, considering options, trying to reach agreement. Counter-intuitively, this is also what makes mediation succeed, so the requirement points the same way as your interests.") + f"""

<h2 id="best-interests">The best-interests test</h2>
<p>Every decision in parenting matters \u2014 in mediation or in court \u2014 is governed by what's in the children's best interests. The {cite("fcfcoa")} weighs several factors:</p>

<ul>
  <li>The benefit of a meaningful relationship with both parents</li>
  <li>The need to protect the child from physical or psychological harm</li>
  <li>The child's views (in an age-appropriate way)</li>
  <li>Each parent's capacity to provide for the child's needs</li>
  <li>The practical effects of any proposed arrangement</li>
  <li>The nature of the child's relationship with parents and other significant people</li>
</ul>

<p><strong>Where these factors conflict, safety always takes priority.</strong> A parent's right to spend time with a child does not override a real risk of harm. <a href="/domestic-violence-and-family-law/">See domestic violence and family law \u2192</a></p>

<h2 id="how">How the process works</h2>
<ol>
  <li><strong>Initial intake</strong> \u2014 each parent meets separately with the practitioner to discuss the situation, identify safety concerns, and assess suitability for mediation.</li>
  <li><strong>Pre-session preparation</strong> \u2014 thinking through what arrangement you'd like, what the children need, what's practical.</li>
  <li><strong>The mediation session</strong> \u2014 the parents work through the arrangement with the practitioner's guidance. Joint session or <a href="/shuttle-mediation-guide/">shuttle mediation</a> (separate rooms) depending on the dynamics.</li>
  <li><strong>Parenting plan or consent orders</strong> \u2014 the agreement is documented. A parenting plan is informal; consent orders make it legally binding. <a href="/parenting-plans-guide/">See parenting plans \u2192</a></li>
  <li><strong>Section 60I certificate</strong> \u2014 if matters don't fully resolve, the practitioner issues the certificate that allows court application.</li>
</ol>

<h2 id="what-covered">What gets agreed</h2>
<p>A parenting agreement typically covers:</p>
<ul>
  <li><strong>Living arrangements</strong> \u2014 where the children primarily live, time with the other parent</li>
  <li><strong>Holidays and special occasions</strong> \u2014 school holidays, birthdays, Christmas, family events</li>
  <li><strong>Major decisions</strong> \u2014 schooling, healthcare, religion, travel</li>
  <li><strong>Day-to-day communication</strong> \u2014 how parents communicate, how children stay in touch with the absent parent</li>
  <li><strong>Changeover</strong> \u2014 logistics, location, who does drop-off and pick-up</li>
  <li><strong>Changes and disputes</strong> \u2014 how future disagreements get resolved</li>
</ul>
""" + inline_cta("Want a parenting arrangement that actually works in real life? An accredited practitioner can help you build one.") + """

<h2 id="5050">The truth about 50/50 care</h2>
<p>There is no automatic right to equal time \u2014 not for either parent. The law supports children maintaining a meaningful relationship with both parents where safe, but the actual split depends on the child's best interests and practical realities: work schedules, distance between homes, the child's age, school routines, sibling arrangements. Equal time is one possible outcome, not a starting assumption.</p>

<p>Fixating on a "magic number" often distracts from what matters: stable, meaningful relationships with both parents in an arrangement the child can live with. Sometimes that's 50/50; sometimes it's 60/40; sometimes it's something more creative that suits a specific family's circumstances. <a href="/fathers-rights/">See fathers' rights \u2192</a> and <a href="/mothers-rights/">mothers' rights \u2192</a></p>

<h2 id="section-60i">Section 60I certificates</h2>
<p>If mediation doesn't fully resolve parenting matters, the practitioner can issue a Section 60I certificate \u2014 the document that allows you to file a parenting application in court. The certificate doesn't say who's "right"; it simply records that the required FDR step was attempted. Several certificate types exist (the other party didn't attend, mediation wasn't appropriate, both parties attended in good faith, etc.). <a href="/section-60i-certificates/">See Section 60I certificates \u2192</a></p>

<h2 id="get-started">Getting started</h2>
<p>The first step is a fixed-fee consultation. We'll explain the FDR process, assess suitability honestly (including any safety concerns), and outline a clear path forward. If mediation is right for your family, we'll schedule the intake and mediation session. If it isn't \u2014 we'll tell you and help you understand the alternatives. There's no obligation and no surprises.</p>
""",
    faq_items=[
        ("Is mediation compulsory before going to court for custody?",
         "For most parenting matters, yes \u2014 you must attempt Family Dispute Resolution and obtain a Section 60I certificate before applying to court, unless an exemption applies (family violence, urgency, child abuse risk, inability to participate)."),
        ("Is there an automatic right to 50/50 care in Australia?",
         "No. There's no automatic equal-time right for either parent. The arrangement depends on the child's best interests and practical realities like work, distance and the child's age."),
        ("What does the best-interests test consider?",
         "Whether a meaningful relationship with both parents is beneficial, the need to protect from harm, the child's views (age-appropriate), each parent's capacity, and practical circumstances. Safety always takes priority where it conflicts with contact."),
        ("How long does child custody mediation take?",
         "Most parenting matters resolve in one or two sessions over a few weeks. Compare that to the one to three years a contested court matter typically takes."),
        ("What's the difference between a parenting plan and consent orders?",
         "A parenting plan is a written, signed agreement but not directly enforceable by the court. Consent orders are filed and approved, giving the same effect as a judge's orders."),
        ("Does the child get a say in the arrangement?",
         "Children's views are considered in an age-appropriate way, but they're not the sole determinant. Older children's views carry more weight, but the overall best-interests test is what governs the decision."),
        ("What if there's family violence?",
         "Family violence is a recognised exemption from compulsory mediation, and protective orders take priority. We assess this honestly at intake \u2014 if mediation isn't safe for you, we'll tell you and help you understand the protective alternatives."),
    ],
    related_items=[
        ("family-law-mediation","Family Law Mediation"),
        ("parenting-plan-mediation","Parenting Plan Mediation"),
        ("section-60i-certificates","Section 60I Certificates"),
        ("parenting-plans-guide","Parenting Plans: Complete Guide"),
        ("is-family-law-mediation-compulsory","Is Mediation Compulsory?"),
        ("fathers-rights","Fathers' Rights"),
        ("mothers-rights","Mothers' Rights"),
        ("domestic-violence-and-family-law","Domestic Violence & Family Law"),
    ],
)

print("\nBatch 1 complete: 3 cornerstone-depth service pages built.")
