#!/usr/bin/env python3
"""Blog/guides index page."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, cta_band,
                       org_schema, breadcrumb_schema, BOOK_URL, PHONE_HREF, PHONE, DOMAIN)
OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Cornerstone posts: (slug, category, title, blurb)
POSTS = [
 ("cost-of-divorce-in-australia","Costs & fees","How Much Does Divorce Cost in Australia? (2026)","A clear breakdown of court fees, lawyer costs, and how mediation saves tens of thousands."),
 ("mediation-with-a-narcissist","High-conflict","Mediation With a Narcissist: Does It Work?","Yes — often better than court. Proven strategies for high-conflict and controlling exes."),
 ("what-am-i-entitled-to-in-a-separation-in-australia","Property & finances","What Am I Entitled To in a Separation?","How property, super and support are divided — and how to reach a fair split without court."),
 ("how-long-does-mediation-take","The process","How Long Does Mediation Take?","Most disputes resolve in one or two sessions — compared with years in court."),
 ("consent-orders-explained","Consent orders","Consent Orders Explained","How to make your agreement legally binding without going to court — cost, timing, and how to change them."),
 ("property-settlement-after-separation","Property & finances","Property Settlement After Separation","The four-step process, asset pool, time limits and how to settle without a court battle."),
 ("how-to-get-a-divorce-in-australia-a-step-by-step-guide","Divorce","How to Get a Divorce in Australia","Step-by-step: eligibility, the 12-month rule, applying online, cost, and serving papers."),
 ("binding-financial-agreements-guide","Property & finances","Binding Financial Agreements Guide","Prenups and postnups explained — what makes them valid, the risks, and BFA vs consent orders."),
 ("parenting-plans-guide","Parenting","Parenting Plans in Australia","What to include, whether it's binding, plan vs order, and how to agree one through mediation."),
 ("what-is-mediation-in-family-law","The process","What Is Mediation in Family Law?","How the process works, the mediator's role, why it succeeds, cost and time."),
 ("mediate-or-litigate","The process","Mediate or Litigate? How to Choose","An honest comparison of cost, time, control and outcomes — and when court is genuinely needed."),
 ("child-custody-mediation","Parenting","Child Custody Mediation","What the law really says about custody, 50/50 care, and how parents agree without court."),
 ("domestic-violence-and-family-law","Safety","Domestic Violence & Family Law","Protection orders, safety during separation, mediation exemptions, and where to get help."),
 ("separation-guide","Separation","Separation in Australia: Complete Guide","First steps, the date of separation, who pays the bills, who stays in the house, and protecting yourself."),
 ("de-facto-relationships-guide","De facto","De Facto Relationships & Separation","What counts as de facto, how assets are split, the two-year limit, and how it compares to marriage."),
 ("spousal-maintenance-guide","Property & finances","Spousal Maintenance in Australia","Who pays, how much, how long it lasts, and how it differs from child support."),
 ("child-support-guide","Parenting","Child Support in Australia","The formula, how care affects payments, when it stops, and resolving disputes."),
 ("is-family-law-mediation-compulsory","The process","Is Family Law Mediation Compulsory?","When mediation and a Section 60I certificate are required, the exemptions, and what if your ex refuses."),
 ("fathers-rights","Parenting","Fathers' Rights After Separation","The truth about 50/50 care, parental responsibility, and how dads secure meaningful time."),
 ("superannuation-and-divorce","Property & finances","Superannuation and Divorce","How super splitting works, valuation, and why it matters — especially for carers."),
 ("high-conflict-mediation","High-conflict","High-Conflict Family Law Mediation","How shuttle mediation and skilled techniques resolve even bitter disputes without court."),
 ("mothers-rights","Parenting","Mothers' Rights in Family Law","Parental responsibility, the best-interests test, and the myth of automatic mother preference."),
 ("grandparents-rights","Parenting","Grandparents' Rights in Australia","How grandparents can seek time with grandchildren, and why mediation comes first."),
 ("shuttle-mediation-guide","The process","Shuttle Mediation Explained","How keeping parties apart resolves high-conflict disputes safely — pros, cons and when to use it."),
 ("conciliation-vs-mediation","The process","Conciliation vs Mediation","What each is, how the third party's role differs, and which suits your dispute."),
 ("workplace-mediation-guide","Workplace","Workplace Mediation in Australia","How it resolves workplace conflict, the Fair Work Commission's role, and the benefits."),
 ("property-settlement-mediation-guide","Property & finances","Property Settlement Mediation Guide","How to prepare, what to bring, what to expect on the day, and reaching a fair agreement."),
 ("business-in-divorce","Property & finances","Business in Divorce","How businesses, companies and trusts are valued and divided — and how to protect yours."),
 ("family-court-process","The process","The Family Court Process","From pre-action steps to final hearing, timeframes, and why mediation comes first."),
 ("divorce-without-a-lawyer","Divorce","Divorce Without a Lawyer","How to DIY the application, where to be careful, and the cost-effective middle path."),
 ("how-long-does-a-divorce-take","Divorce","How Long Does a Divorce Take?","The 12-month rule, processing times, when it's final, and avoiding delays."),
 ("how-much-does-mediation-cost","Costs & fees","How Much Does Mediation Cost?","Family mediation fees, who pays, free options, and why it's far cheaper than court."),
 ("arbitration-in-family-law","The process","Arbitration in Family Law","How a binding decision on financial matters is reached privately, faster than court."),
 ("pets-and-family-law","Property & finances","Pets and Family Law","Who gets the pet after separation, the 2025 law changes, and resolving pet disputes."),
 ("same-sex-family-law","Divorce","Same-Sex Separation & Divorce","Equal rights for LGBTQ+ couples in divorce, property, parenting and de facto matters."),
 ("changes-to-family-law-act-2025","Legal updates","Changes to the Family Law Act 2025","The new property framework, family violence, pets, and what the reforms mean for you."),
 ("stepparent-rights","Parenting","Step-Parent Rights in Australia","Parental responsibility, contact after separation, child support, and staying in a child's life."),
 ("surrogacy-laws","Legal updates","Surrogacy Laws in Australia","Altruistic vs commercial surrogacy, legal parentage, and the state-by-state rules."),
 ("can-you-record-your-ex","Legal updates","Can You Record Your Ex?","Surveillance laws, whether recordings can be used in court, and what to do instead."),
 ("best-divorce-lawyers-sydney","Divorce","Best Divorce Lawyers in Sydney","When you need a lawyer, when mediation is better, and how to choose the right help."),
 ("parental-alienation-australia","Parenting","Parental Alienation in Australia","What it is, how the law treats it, telling it apart from justified reluctance, and rebuilding the relationship without court."),
 ("who-pays-for-mediation","Costs & fees","Who Pays for Mediation?","How the fee is usually split, when one party pays, free options, and the comparison with court."),
 ("private-vs-free-mediation","Costs & fees","Private vs Free Mediation","Wait times, cost, complexity and outcomes — how to choose between free FDR and private mediation."),
 ("divorce-mediator-vs-divorce-lawyer","Divorce","Divorce Mediator vs Divorce Lawyer","What each does, what they cost, and why most people benefit from both in the right order."),
 ("mediation-before-divorce","Divorce","Mediation Before Divorce","Why resolving parenting and property during separation — before you file — saves time and money."),
 ("what-happens-if-mediation-fails","The process","What If Mediation Fails?","Section 60I certificates, going to court, and why a failed mediation usually still helps."),
 ("what-is-in-the-property-pool","Property & finances","What's in the Property Pool?","Assets, super, businesses, debts and inheritances — what counts in a property settlement."),
 ("delaying-property-settlement","Property & finances","Can My Ex Delay Settlement?","Stalling tactics, time limits, disclosure duties, and how mediation forces progress."),
 ("co-parenting-mediation","Parenting","Co-Parenting Mediation","Resolving ongoing disputes over schedules, decisions and communication — and keeping kids first."),
]

ALL_CATS = ["All"] + sorted({cat for _,cat,_,_ in POSTS})

schema=[org_schema(),breadcrumb_schema([("Home",""),("Guides","guides")]),
        {"@type":"CollectionPage","name":"Mediation & Family Law Guides",
         "url":f"{DOMAIN}/guides/","isPartOf":{"@id":f"{DOMAIN}/#website"}}]
d=head("Family Law &amp; Mediation Guides | Mediations Australia",
 "Practical, expert guides on mediation, divorce, property settlement, parenting and more — helping you resolve disputes without court. Free consultation.",
 "guides",extra_schema=schema)+nav()

import re as _re

cornerstone_slugs = {s for s,_,_,_ in POSTS}

# Cornerstone cards (with data-cat for JS filter)
cards=""
for slug,cat,title,blurb in POSTS:
    cards+=f'<article class="card reveal" data-cat="{esc(cat)}"><span class="cat-tag">{esc(cat)}</span><h3><a href="/{slug}/">{esc(title)}</a></h3><p>{esc(blurb)}</p><a class="more" href="/{slug}/">Read guide <span class="arr">→</span></a></article>'

# Category filter buttons
def _cat_btn(cat):
    active = ' class="active"' if cat == "All" else ''
    return f'<button{active} data-filter="{esc(cat)}">{esc(cat)}</button>'
cat_buttons = "".join(_cat_btn(c) for c in ALL_CATS)

# Auto-discover imported posts
SKIP_SLUGS = {
    "guides","about-mediations-australia","contact-us","book-a-consultation",
    "how-mediation-works","preparing-for-mediation","our-fee-structure",
    "family-law-mediation","divorce-mediation","property-settlement-mediation",
    "parenting-plan-mediation","section-60i-certificates","financial-agreements-mediation",
    "spousal-support-mediation","child-support-mediation","de-facto-mediation",
    "grandparents-mediation","consent-orders","online-divorce","workplace-mediation",
    "estate-dispute-mediation","collaborative-family-lawyers","family-law-arbitration",
    "divorce-counselling","memberships","our-mediators",
    "sydney-mediation","melbourne-mediation","brisbane-mediation","perth-mediation",
    "adelaide-mediation","canberra-mediation","gold-coast-mediation","newcastle-mediation",
    "wollongong-mediation","geelong-mediation","hobart-mediation","townsville-mediation",
    "cairns-mediation","toowoomba-mediation","ballarat-mediation","bendigo-mediation",
    "launceston-mediation","mackay-mediation","rockhampton-mediation","sunshine-coast-mediation",
    "bundaberg-mediation",
    "parenting-plan-template","bfa-or-consent-orders","getting-ready-for-separation",
    "family-law-cost-estimator","separation-under-one-roof-assessment",
}

def _read_title(path):
    s = open(path, encoding="utf-8", errors="ignore").read()
    m = _re.search(r"<title>(.*?)</title>", s, _re.I | _re.S)
    if not m: return None
    t = _re.sub(r"<[^>]+>","",m.group(1)).strip()
    t = _re.sub(r"\s*\|.*$","",t).strip()
    return t if t else None

imported_items = []
for slug in sorted(
    dd for dd in os.listdir(OUT)
    if os.path.isdir(os.path.join(OUT, dd))
    and dd not in cornerstone_slugs
    and dd not in SKIP_SLUGS
    and os.path.exists(os.path.join(OUT, dd, "index.html"))
    and open(os.path.join(OUT, dd, "index.html"), encoding="utf-8", errors="ignore").read().count("body-import") > 0
):
    title = _read_title(os.path.join(OUT, slug, "index.html"))
    if title:
        imported_items.append((slug, title))

imported_list = "".join(
    f'<li data-title="{esc(t.lower())}"><a href="/{s}/">{esc(t)}</a></li>'
    for s,t in imported_items
)

n_imp = len(imported_items)

d += f"""<main id="main">
{crumb_html([("Home",""),("Guides",None)])}

<section class="phero"><div class="phero-blob"></div><div class="wrap">
<span class="eyebrow"><span class="pulse"></span>Free expert guides</span>
<h1>Family law &amp; mediation <em>guides</em>.</h1>
<p class="lede">Clear, practical answers on separation, property settlement, parenting and more — written by accredited mediators.</p>
<div class="phero-cta">
  <a href="{BOOK_URL}" class="btn btn-primary">Book a free consultation <span class="arr">→</span></a>
  <a href="{PHONE_HREF}" class="btn btn-ghost">Call {PHONE}</a>
</div>
</div></section>

<section class="sec" style="padding-top:40px" id="featured">
<div class="wrap">
  <p class="sec-tag">Featured guides</p>
  <h2 class="sec-title" style="margin-bottom:28px">In-depth guides by <em>our mediators</em>.</h2>
  <div class="filter-bar" role="group" aria-label="Filter by topic">{cat_buttons}</div>
  <div class="cards" id="cstone-grid">{cards}</div>
  <p id="no-cat" style="display:none;color:var(--ink-soft);padding:32px 0;text-align:center">No guides in that category yet.</p>
</div>
</section>

<section class="sec" style="background:var(--cream)" id="all-articles">
<div class="wrap">
  <p class="sec-tag">Full library</p>
  <h2 class="sec-title">Everything we've <em>written</em>.</h2>
  <p style="color:var(--ink-soft);max-width:56ch;margin:0 0 28px">{n_imp} articles covering every aspect of family law, mediation, separation and dispute resolution in Australia.</p>
  <div class="search-wrap">
    <svg class="si" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
    <input type="search" id="asearch" placeholder="Search {n_imp} articles…" aria-label="Search all articles" autocomplete="off">
    <span id="scount" aria-live="polite"></span>
  </div>
  <ul class="alist" id="alist">{imported_list}</ul>
  <p id="no-search" style="display:none;color:var(--ink-soft);padding:24px 0">No articles match your search. Try different keywords.</p>
</div>
</section>
"""
d += cta_band("Got a question we haven't <em>covered</em>?",
 "Book a fixed-fee consultation and get honest, expert answers tailored to your exact situation.")
d += "</main>" + page_end()

d = d.replace("</head>", """<style>
.cat-tag{display:inline-block;background:var(--sage-light);color:var(--sage-deep);padding:5px 13px;border-radius:100px;font-size:.78rem;font-weight:600;margin-bottom:14px}
.card h3 a{color:var(--ink)}.card h3 a:hover{color:var(--sage-deep)}.card h3{margin-bottom:10px;font-size:1.2rem}
/* Filter bar */
.filter-bar{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:36px}
.filter-bar button{padding:8px 18px;border-radius:100px;font-size:.85rem;font-weight:500;border:1.5px solid var(--sage-light);background:transparent;color:var(--ink-soft);cursor:pointer;transition:all .15s;font-family:inherit}
.filter-bar button:hover{border-color:var(--sage);color:var(--sage-deep)}
.filter-bar button.active{background:var(--sage-deep);border-color:var(--sage-deep);color:#fff}
/* Search */
.search-wrap{position:relative;display:flex;align-items:center;max-width:520px;margin-bottom:28px}
.si{position:absolute;left:16px;color:var(--ink-soft);pointer-events:none}
#asearch{width:100%;padding:13px 48px 13px 46px;border:1.5px solid var(--sand-deep,#ebe3d4);border-radius:12px;font-size:1rem;font-family:inherit;color:var(--ink);background:var(--sand);outline:none;transition:border-color .15s}
#asearch:focus{border-color:var(--sage)}
#scount{position:absolute;right:14px;font-size:.82rem;color:var(--ink-soft);white-space:nowrap;pointer-events:none}
/* Article list */
.alist{list-style:none;padding:0;margin:0;columns:3;column-gap:40px}
.alist li{break-inside:avoid;padding:9px 0;border-bottom:1px solid rgba(35,41,31,.07)}
.alist li a{color:var(--ink);text-decoration:none;font-size:.93rem;line-height:1.4;display:block;transition:color .15s}
.alist li a:hover{color:var(--sage-deep)}
@media(max-width:900px){.alist{columns:2}}
@media(max-width:580px){.alist{columns:1}.filter-bar button{font-size:.8rem;padding:7px 14px}}
</style></head>""")

d = d.replace("</body>", """<script>
(function(){
  var btns=document.querySelectorAll('.filter-bar button');
  var cards=document.querySelectorAll('#cstone-grid .card');
  var noCat=document.getElementById('no-cat');
  btns.forEach(function(b){
    b.addEventListener('click',function(){
      btns.forEach(function(x){x.classList.remove('active')});
      b.classList.add('active');
      var f=b.dataset.filter;
      var vis=0;
      cards.forEach(function(c){var s=(f==='All'||c.dataset.cat===f);c.style.display=s?'':'none';if(s)vis++;});
      noCat.style.display=vis?'none':'block';
    });
  });
  var inp=document.getElementById('asearch');
  var items=document.querySelectorAll('#alist li');
  var noS=document.getElementById('no-search');
  var cnt=document.getElementById('scount');
  if(inp){inp.addEventListener('input',function(){
    var q=this.value.trim().toLowerCase();
    var v=0;
    items.forEach(function(li){var m=!q||li.dataset.title.indexOf(q)!==-1;li.hidden=!m;if(m)v++;});
    noS.style.display=(q&&v===0)?'block':'none';
    cnt.textContent=q?(v+' result'+(v===1?'':'s')):'';
  });}
})();
</script>
</body>""")

os.makedirs(os.path.join(OUT, "guides"), exist_ok=True)
open(os.path.join(OUT, "guides", "index.html"), "w").write(d)
print(f"Guides index built — {len(POSTS)} cornerstones + {n_imp} imported | {len(ALL_CATS)-1} filter categories")
