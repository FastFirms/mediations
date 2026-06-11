#!/usr/bin/env python3
"""Blog/guides index page."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, cta_band,
                       org_schema, breadcrumb_schema, BOOK_URL, PHONE_HREF, PHONE, DOMAIN)
OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Published posts: (slug, category, title, blurb)
POSTS = [
 ("cost-of-divorce-in-australia","Costs &amp; fees","How Much Does Divorce Cost in Australia? (2026)","A clear breakdown of court fees, lawyer costs, and how mediation saves tens of thousands."),
 ("mediation-with-a-narcissist","High-conflict","Mediation With a Narcissist: Does It Work?","Yes — often better than court. Proven strategies for high-conflict and controlling exes."),
 ("what-am-i-entitled-to-in-a-separation-in-australia","Property &amp; finances","What Am I Entitled To in a Separation?","How property, super and support are divided — and how to reach a fair split without court."),
 ("how-long-does-mediation-take","The process","How Long Does Mediation Take?","Most disputes resolve in one or two sessions — compared with years in court."),
 ("consent-orders-explained","Consent orders","Consent Orders Explained","How to make your agreement legally binding without going to court — cost, timing, and how to change them."),
  ("property-settlement-after-separation","Property &amp; finances","Property Settlement After Separation","The four-step process, asset pool, time limits and how to settle without a court battle."),
 ("how-to-get-a-divorce-in-australia-a-step-by-step-guide","Divorce","How to Get a Divorce in Australia","Step-by-step: eligibility, the 12-month rule, applying online, cost, and serving papers."),
 ("binding-financial-agreements-guide","Property &amp; finances","Binding Financial Agreements Guide","Prenups and postnups explained — what makes them valid, the risks, and BFA vs consent orders."),
  ("parenting-plans-guide","Parenting","Parenting Plans in Australia","What to include, whether it's binding, plan vs order, and how to agree one through mediation."),
 ("what-is-mediation-in-family-law","The process","What Is Mediation in Family Law?","How the process works, the mediator's role, why it succeeds, cost and time."),
 ("mediate-or-litigate","The process","Mediate or Litigate? How to Choose","An honest comparison of cost, time, control and outcomes — and when court is genuinely needed."),
 ("child-custody-mediation","Parenting","Child Custody Mediation","What the law really says about custody, 50/50 care, and how parents agree without court."),
  ("domestic-violence-and-family-law","Safety","Domestic Violence & Family Law","Protection orders, safety during separation, mediation exemptions, and where to get help."),
 ("separation-guide","Separation","Separation in Australia: Complete Guide","First steps, the date of separation, who pays the bills, who stays in the house, and protecting yourself."),
 ("de-facto-relationships-guide","De facto","De Facto Relationships & Separation","What counts as de facto, how assets are split, the two-year limit, and how it compares to marriage."),
 ("spousal-maintenance-guide","Property &amp; finances","Spousal Maintenance in Australia","Who pays, how much, how long it lasts, and how it differs from child support."),
  ("child-support-guide","Parenting","Child Support in Australia","The formula, how care affects payments, when it stops, and resolving disputes."),
 ("is-family-law-mediation-compulsory","The process","Is Family Law Mediation Compulsory?","When mediation and a Section 60I certificate are required, the exemptions, and what if your ex refuses."),
 ("fathers-rights","Parenting","Fathers' Rights After Separation","The truth about 50/50 care, parental responsibility, and how dads secure meaningful time."),
 ("superannuation-and-divorce","Property &amp; finances","Superannuation and Divorce","How super splitting works, valuation, and why it matters — especially for carers."),
  ("high-conflict-mediation","High-conflict","High-Conflict Family Law Mediation","How shuttle mediation and skilled techniques resolve even bitter disputes without court."),
 ("mothers-rights","Parenting","Mothers' Rights in Family Law","Parental responsibility, the best-interests test, and the myth of automatic mother preference."),
 ("grandparents-rights","Parenting","Grandparents' Rights in Australia","How grandparents can seek time with grandchildren, and why mediation comes first."),
 ("shuttle-mediation-guide","The process","Shuttle Mediation Explained","How keeping parties apart resolves high-conflict disputes safely — pros, cons and when to use it."),
 ("conciliation-vs-mediation","The process","Conciliation vs Mediation","What each is, how the third party's role differs, and which suits your dispute."),
  ("workplace-mediation-guide","Workplace","Workplace Mediation in Australia","How it resolves workplace conflict, the Fair Work Commission's role, and the benefits."),
 ("property-settlement-mediation-guide","Property &amp; finances","Property Settlement Mediation Guide","How to prepare, what to bring, what to expect on the day, and reaching a fair agreement."),
 ("business-in-divorce","Property &amp; finances","Business in Divorce","How businesses, companies and trusts are valued and divided — and how to protect yours."),
 ("family-court-process","The process","The Family Court Process","From pre-action steps to final hearing, timeframes, and why mediation comes first."),
 ("divorce-without-a-lawyer","Divorce","Divorce Without a Lawyer","How to DIY the application, where to be careful, and the cost-effective middle path."),
  ("how-long-does-a-divorce-take","Divorce","How Long Does a Divorce Take?","The 12-month rule, processing times, when it's final, and avoiding delays."),
 ("how-much-does-mediation-cost","Costs &amp; fees","How Much Does Mediation Cost?","Family mediation fees, who pays, free options, and why it's far cheaper than court."),
 ("arbitration-in-family-law","The process","Arbitration in Family Law","How a binding decision on financial matters is reached privately, faster than court."),
 ("pets-and-family-law","Property &amp; finances","Pets and Family Law","Who gets the pet after separation, the 2025 law changes, and resolving pet disputes."),
 ("same-sex-family-law","Divorce","Same-Sex Separation & Divorce","Equal rights for LGBTQ+ couples in divorce, property, parenting and de facto matters."),
 ("changes-to-family-law-act-2025","Legal updates","Changes to the Family Law Act 2025","The new property framework, family violence, pets, and what the reforms mean for you."),
 ("stepparent-rights","Parenting","Step-Parent Rights in Australia","Parental responsibility, contact after separation, child support, and staying in a child's life."),
 ("surrogacy-laws","Legal updates","Surrogacy Laws in Australia","Altruistic vs commercial surrogacy, legal parentage, and the state-by-state rules."),
 ("can-you-record-your-ex","Legal updates","Can You Record Your Ex?","Surveillance laws, whether recordings can be used in court, and what to do instead."),
 ("best-divorce-lawyers-sydney","Divorce","Best Divorce Lawyers in Sydney","When you need a lawyer, when mediation is better, and how to choose the right help."),
 ("parental-alienation-australia","Parenting","Parental Alienation in Australia","What it is, how the law treats it, telling it apart from justified reluctance, and rebuilding the relationship without court."),
 ("who-pays-for-mediation","Costs &amp; fees","Who Pays for Mediation?","How the fee is usually split, when one party pays, free options, and the comparison with court."),
 ("private-vs-free-mediation","Costs &amp; fees","Private vs Free Mediation","Wait times, cost, complexity and outcomes — how to choose between free FDR and private mediation."),
 ("divorce-mediator-vs-divorce-lawyer","Divorce","Divorce Mediator vs Divorce Lawyer","What each does, what they cost, and why most people benefit from both in the right order."),
 ("mediation-before-divorce","Divorce","Mediation Before Divorce","Why resolving parenting and property during separation — before you file — saves time and money."),
 ("what-happens-if-mediation-fails","Family law mediation","What If Mediation Fails?","Section 60I certificates, going to court, and why a 'failed' mediation usually still helps."),
 ("what-is-in-the-property-pool","Property &amp; finances","What's in the Property Pool?","Assets, super, businesses, debts and inheritances — what counts in a property settlement."),
 ("delaying-property-settlement","Property &amp; finances","Can My Ex Delay Settlement?","Stalling tactics, time limits, disclosure duties, and how mediation forces progress."),
 ("co-parenting-mediation","Parenting","Co-Parenting Mediation","Resolving ongoing disputes over schedules, decisions and communication — and keeping kids first."),
]

CATS = ["All","Costs &amp; fees","The process","Property &amp; finances","High-conflict","Parenting"]

schema=[org_schema(),breadcrumb_schema([("Home",""),("Guides","guides")]),
        {"@type":"CollectionPage","name":"Mediation & Family Law Guides",
         "url":f"{DOMAIN}/guides/","isPartOf":{"@id":f"{DOMAIN}/#website"}}]
d=head("Family Law &amp; Mediation Guides | Mediations Australia",
 "Practical, expert guides on mediation, divorce, property settlement, parenting and more — helping you resolve disputes without court. Free consultation.",
 "guides",extra_schema=schema)+nav()

cards=""
for slug,cat,title,blurb in POSTS:
    cards+=f"""<article class="card reveal">
  <span class="cat-tag">{cat}</span>
  <h3><a href="/{slug}/">{esc(title)}</a></h3>
  <p>{esc(blurb)}</p>
  <a class="more" href="/{slug}/">Read guide <span class="arr">→</span></a>
</article>"""

d+=f"""<main id="main">
{crumb_html([("Home",""),("Guides",None)])}
<section class="phero"><div class="phero-blob"></div><div class="wrap">
<span class="eyebrow"><span class="pulse"></span>Free expert guides</span>
<h1>Family law &amp; mediation <em>guides</em>.</h1>
<p class="lede">Clear, practical answers to the questions people actually ask when facing separation, property settlement or a dispute — written by accredited mediators to help you make confident decisions.</p>
<div class="phero-cta"><a href="{BOOK_URL}" class="btn btn-primary">Book a free consultation <span class="arr">→</span></a>
<a href="{PHONE_HREF}" class="btn btn-ghost">Call {PHONE}</a></div>
</div></section>
<section class="sec" style="padding-top:30px"><div class="wrap">
<div class="cards">{cards}</div>
<p style="margin-top:36px;color:var(--ink-soft);text-align:center">More guides are being added regularly. <a href="{BOOK_URL}" style="color:var(--sage-deep);text-decoration:underline">Have a specific question? Ask us directly →</a></p>
</div></section>
"""
d+=cta_band("Got a question we haven't <em>covered</em>?",
 "Book a fixed-fee consultation and get honest, expert answers tailored to your exact situation.")
d+="</main>"+page_end()

# small style addition for cat tags
d=d.replace("</head>","""<style>
.cat-tag{display:inline-block;background:var(--sage-light);color:var(--sage-deep);padding:5px 13px;border-radius:100px;font-size:.78rem;font-weight:600;margin-bottom:14px}
.card h3 a{color:var(--ink)}.card h3 a:hover{color:var(--sage-deep)}
.card h3{margin-bottom:10px;font-size:1.2rem}
</style></head>""")

os.makedirs(os.path.join(OUT,"guides"),exist_ok=True)
open(os.path.join(OUT,"guides","index.html"),"w").write(d)
print("Blog index (/guides/) built with",len(POSTS),"posts")
