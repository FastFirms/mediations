#!/usr/bin/env python3
"""Blog system: UX-optimised post template with CTAs punctuating content,
blog index, full Article+FAQ schema. Phase 1 cornerstone posts."""
import os, sys, re
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, faq_html,
                       org_schema, faq_schema, breadcrumb_schema, article_schema,
                       BOOK_URL, PHONE, PHONE_HREF, DOMAIN)
OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---- Inline CTA components that punctuate blog content ----
def inline_cta(text, btn="Book a free consultation"):
    """A soft, persuasive CTA band placed mid-article."""
    return f"""<div class="post-cta reveal">
  <div class="post-cta-inner">
    <p>{text}</p>
    <a href="{BOOK_URL}" class="btn btn-primary">{btn} <span class="arr">→</span></a>
  </div>
</div>"""

def callout(h, p):
    return f'<div class="callout"><h3>{h}</h3><p>{p}</p></div>'

def key_takeaway(text):
    return f'<div class="answer reveal"><p><strong>Key takeaway:</strong> {text}</p></div>'

POST_CSS = """
<style>
.post-hero{padding:36px 0 8px}
.post-meta{display:flex;gap:16px;align-items:center;font-size:.9rem;color:var(--ink-soft);margin-bottom:18px;flex-wrap:wrap}
.post-meta .cat{background:var(--sage-light);color:var(--sage-deep);padding:5px 14px;border-radius:100px;font-weight:600;font-size:.82rem}
.post-body{padding:30px 0 60px}
.post-body h2{font-size:clamp(1.5rem,3vw,2.1rem);margin:42px 0 14px}
.post-body h2:first-child{margin-top:0}
.post-body h3{font-size:1.25rem;margin:30px 0 10px}
.post-body p{font-size:1.07rem;color:var(--ink-soft);margin-bottom:18px;max-width:70ch}
.post-body ul,.post-body ol{margin:0 0 22px;padding-left:0;list-style:none;display:flex;flex-direction:column;gap:11px}
.post-body ul li{position:relative;padding-left:30px;color:var(--ink-soft);font-size:1.05rem;max-width:66ch}
.post-body ul li::before{content:"";position:absolute;left:0;top:8px;width:16px;height:16px;background:var(--sage-light);border-radius:50%}
.post-body ul li::after{content:"";position:absolute;left:4px;top:11px;width:8px;height:5px;border-left:2px solid var(--sage-deep);border-bottom:2px solid var(--sage-deep);transform:rotate(-45deg)}
.post-body ol{counter-reset:li}
.post-body ol li{position:relative;padding-left:42px;color:var(--ink-soft);font-size:1.05rem;max-width:66ch;counter-increment:li}
.post-body ol li::before{content:counter(li);position:absolute;left:0;top:0;width:26px;height:26px;background:var(--sage);color:var(--cream);border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:.85rem;font-weight:600}
.post-body a{color:var(--sage-deep);text-decoration:underline;text-underline-offset:2px}
.post-body a:hover{color:var(--terra)}
.post-cta{margin:36px 0}
.post-cta-inner{background:linear-gradient(135deg,var(--sage-deep),var(--sage));color:var(--cream);border-radius:20px;padding:30px 34px;display:flex;align-items:center;justify-content:space-between;gap:24px;flex-wrap:wrap}
.post-cta-inner p{color:var(--cream);font-family:var(--serif);font-size:1.2rem;font-style:italic;margin:0;flex:1;min-width:240px}
.post-cta-inner .btn{flex-shrink:0}
.post-toc{background:var(--cream);border:1px solid var(--line);border-radius:14px;padding:22px 26px;margin-bottom:30px}
.post-toc h2{font-size:1rem!important;margin:0 0 12px!important;text-transform:uppercase;letter-spacing:.08em;font-family:var(--sans);font-weight:600;color:var(--ink-soft)}
.post-toc ul{list-style:none;display:flex;flex-direction:column;gap:8px;margin:0;padding:0}
.post-toc ul li{padding:0}
.post-toc ul li::before,.post-toc ul li::after{display:none}
.post-toc a{font-size:.96rem;color:var(--sage-deep);text-decoration:none}
.post-toc a:hover{color:var(--terra);text-decoration:underline}
.related{background:var(--sand-deep);border-radius:24px;padding:40px;margin-top:20px}
.related h2{font-size:1.4rem;margin-bottom:20px}
.related-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:14px}
.related a{background:var(--cream);border:1px solid var(--line);border-radius:12px;padding:18px 20px;font-weight:600;color:var(--ink);font-size:.98rem;transition:transform .3s,box-shadow .3s}
.related a:hover{transform:translateY(-3px);box-shadow:var(--shadow)}
.post-body table{width:100%;border-collapse:collapse;margin:20px 0 28px;font-size:.98rem;background:var(--cream);border-radius:12px;overflow:hidden;box-shadow:var(--shadow)}
.post-body table caption{caption-side:top;text-align:left;font-size:.9rem;color:var(--ink-soft);margin-bottom:8px;font-style:italic}
.post-body th{background:var(--sage-deep);color:var(--cream);text-align:left;padding:13px 16px;font-weight:600;font-family:var(--sans)}
.post-body td{padding:12px 16px;border-bottom:1px solid var(--line);color:var(--ink-soft)}
.post-body tr:last-child td{border-bottom:none}
.post-body tr:nth-child(even) td{background:rgba(90,113,89,.04)}
.post-body figure.tbl{margin:0 0 28px;overflow-x:auto}
.source-note{font-size:.85rem;color:var(--ink-soft);font-style:italic;margin:-12px 0 24px}
@media(max-width:600px){.post-cta-inner{flex-direction:column;align-items:stretch}.post-cta-inner .btn{width:100%;justify-content:center}}
</style>
"""

def post(slug, title, desc, category, h1, dek, toc, body, qa, related, read_min=7):
    """related = list of (slug, label). body already includes inline CTAs."""
    schema=[org_schema(),
            breadcrumb_schema([("Home",""),("Guides","guides"),(h1[:60],slug)]),
            article_schema(title.split(" | ")[0], desc)]
    if qa: schema.append(faq_schema(qa))
    d=head(title,desc,slug,og_type="article",extra_schema=schema)
    d=d.replace("</head>", POST_CSS+"</head>")
    d+=nav()
    toc_html=""
    if toc:
        items="".join(f'<li><a href="#{i}">{esc(t)}</a></li>' for i,t in toc)
        toc_html=f'<nav class="post-toc reveal" aria-label="Contents"><h2>In this guide</h2><ul>{items}</ul></nav>'
    rel_html=""
    if related:
        cards="".join(f'<a href="/{s}/">{esc(l)} →</a>' for s,l in related)
        rel_html=f'<section class="related reveal"><h2>Related guides &amp; services</h2><div class="related-grid">{cards}</div></section>'
    d+=f"""<main id="main">
{crumb_html([("Home",""),("Guides","guides"),(h1[:48]+("…" if len(h1)>48 else ""),None)])}
<article>
<header class="post-hero"><div class="wrap-narrow">
  <div class="post-meta"><span class="cat">{esc(category)}</span><span>{read_min} min read</span><span>Reviewed by Mediations Australia</span></div>
  <h1>{h1}</h1>
  <p class="lede" style="margin-top:16px">{dek}</p>
</div></header>
<div class="post-body"><div class="wrap-narrow">
{toc_html}
{body}
</div></div>
</article>"""
    if qa: d+=faq_html(qa, heading="Frequently asked questions")
    d+=f"""<div class="wrap" style="padding-bottom:40px">{rel_html}</div>"""
    # final strong CTA band
    d+=f"""<section class="cta-band" id="book"><div class="phero-blob"></div><div class="wrap"><div class="reveal">
<h2>Ready to resolve it <em>without court</em>?</h2>
<p>Book a fixed-fee consultation and get honest, expert advice on your situation — with no obligation.</p>
<a href="{BOOK_URL}" class="btn btn-primary" style="font-size:1.1rem;padding:18px 38px">Book your free consultation <span class="arr">→</span></a>
</div></div></section>"""
    d+="</main>"+page_end()
    p=os.path.join(OUT,slug); os.makedirs(p,exist_ok=True)
    open(os.path.join(p,"index.html"),"w").write(d)
    return slug, len(re.sub(r'<[^>]+>',' ',d).split())

print("blog engine ready")

# ============================================================
# CORNERSTONE POST 1 — Cost of divorce in Australia
# ============================================================
post("cost-of-divorce-in-australia",
 "How Much Does Divorce Cost in Australia? (2026 Guide)",
 "How much does divorce cost in Australia in 2026? A full breakdown of court filing fees, lawyer hourly rates, expert reports, property settlement and mediation costs — with how to save tens of thousands.",
 "Costs &amp; fees",
 "How Much Does Divorce Cost in Australia? <em>(2026 Guide)</em>",
 "A divorce in Australia can cost anywhere from around $1,100 for a straightforward application to well over $100,000 for a contested case involving property and children. This guide breaks down every cost you may face — filing fees, lawyer rates, expert reports and property settlement — and shows exactly how mediation keeps the total down.",
 [("understanding-divorce","Understanding divorce in Australia"),
  ("filing-fees","Filing fees and fee reductions"),
  ("lawyer-costs","Legal representation costs"),
  ("court-costs","Court and expert report costs"),
  ("property-settlement","Property settlement and financial agreements"),
  ("mediation-cost","Mediation: the cost-effective alternative"),
  ("managing-costs","How to manage your divorce costs")],
 key_takeaway("The divorce application itself is a fixed government fee of around $1,100 (or about $375 with a concession). The costs that vary enormously are legal representation, expert reports and property disputes — where a contested case can exceed $100,000 per side. Mediation typically resolves matters for $3,500–$4,500 in total, shared between parties.")
 + """
<p>Some marriages break down beyond repair, and divorce brings both emotional and financial strain. To put it in context, the <a href="https://www.abs.gov.au/statistics/people/people-and-communities/marriages-and-divorces-australia/latest-release" target="_blank" rel="noopener">Australian Bureau of Statistics</a> recorded roughly 48,000–49,000 divorces granted in a recent year, and independent reporting has put the cost of a typical divorce somewhere between $10,000 and $20,000 — though once property and parenting disputes are added, the total can climb past $100,000. Understanding where the money actually goes is the first step to keeping your own costs under control.</p>
<p class="source-note">Sources: <a href="https://www.abs.gov.au/statistics/people/people-and-communities/marriages-and-divorces-australia/latest-release" target="_blank" rel="noopener">ABS Marriages and Divorces, Australia</a>; <a href="https://www.fcfcoa.gov.au/fl/fees/fl-fees" target="_blank" rel="noopener">FCFCOA fee schedule</a>.</p>

<h2 id="understanding-divorce">Understanding divorce in Australia</h2>
<p>Divorce is the legal process of formally ending a marriage under the <a href="https://www.austlii.edu.au/cgi-bin/viewdb/au/legis/cth/consol_act/fla1975114/" target="_blank" rel="noopener">Family Law Act 1975</a>. Australia operates a no-fault system, which means the court doesn't examine why the marriage ended — only that it has broken down irretrievably, demonstrated by 12 months of separation.</p>
<h3>Who can apply for divorce?</h3>
<p>To be eligible, you must:</p>
<ul>
  <li>Be an Australian citizen, a permanent resident, or have lived in Australia for at least 12 months;</li>
  <li>Have been separated for at least 12 months; and</li>
  <li>Show there is no reasonable likelihood of reconciliation.</li>
</ul>
<p>You can file a <strong>joint application</strong> (both parties agree) or a <strong>sole application</strong> (one spouse applies and serves the other). Where there are children under 18, the court must also be satisfied that proper arrangements are in place for their care — which is where <a href="/parenting-plan-mediation/">a parenting plan</a> becomes important.</p>
"""
 + inline_cta("Not sure what your separation will actually cost? Get a clear, honest estimate in a fixed-fee consultation.")
 + """
<h2 id="filing-fees">Filing fees and fee reductions</h2>
<p>Every divorce begins with the application fee. As set by federal regulations, the <a href="https://www.fcfcoa.gov.au/fl/fees/fl-fees" target="_blank" rel="noopener">standard divorce filing fee</a> is approximately $1,100, with a reduced fee of around $375 for eligible applicants. The fee is fixed — it's the same regardless of how complex your circumstances are.</p>
<h3>Who qualifies for a reduced fee?</h3>
<ul>
  <li>Healthcare card holders</li>
  <li>Pension concession card holders</li>
  <li>Commonwealth Seniors Health Card holders</li>
  <li>Youth Allowance or Austudy recipients</li>
  <li>People in prison or under 18</li>
  <li>Legal aid recipients</li>
</ul>
<p>People experiencing genuine financial hardship may also qualify through an assessment of income, assets and living expenses.</p>

<h2 id="lawyer-costs">Legal representation costs</h2>
<p>Professional legal fees are usually the largest single cost in a divorce. Family lawyer rates vary widely with seniority:</p>
<figure class="tbl"><table><caption>Indicative family lawyer hourly rates (AUD)</caption>
<thead><tr><th>Position</th><th>Hourly rate (AUD)</th></tr></thead>
<tbody>
<tr><td>Junior solicitor</td><td>$250 – $450</td></tr>
<tr><td>Mid-level solicitor</td><td>$400 – $550</td></tr>
<tr><td>Senior solicitor / partner</td><td>$500 – $800</td></tr>
</tbody></table></figure>
<p>For straightforward, uncontested divorces, many firms offer fixed-fee packages, commonly in the $2,000–$5,000 range depending on complexity. Fixed fees give you cost certainty — but they usually assume the matter stays uncontested.</p>
"""
 + callout("The hidden cost most people miss",
   "It isn't only money. Research consistently shows that after a drawn-out court battle, neither party tends to be satisfied with the result — and the damage to co-parenting relationships can last for years. Mediation protects both your finances and your family.")
 + """
<h2 id="court-costs">Court and expert report costs</h2>
<p>If a matter is contested and proceeds through the courts, additional fees apply across the life of the case:</p>
<figure class="tbl"><table><caption>Indicative court-related fees (AUD)</caption>
<thead><tr><th>Court process</th><th>Estimated cost (AUD)</th></tr></thead>
<tbody>
<tr><td>Daily hearing fee</td><td>$770 (before a Registrar) – $1,045 (before a Judge)</td></tr>
<tr><td>Setting-down fee</td><td>$770 – $1,045</td></tr>
<tr><td>Conciliation conference</td><td>~$480</td></tr>
</tbody></table></figure>
<p>Complex matters often require expert assessments, which add further cost:</p>
<figure class="tbl"><table><caption>Indicative expert report costs (AUD)</caption>
<thead><tr><th>Service</th><th>Estimated cost (AUD)</th></tr></thead>
<tbody>
<tr><td>House valuation</td><td>$400 – $800</td></tr>
<tr><td>Business valuation</td><td>$3,000 – $10,000</td></tr>
<tr><td>Family report</td><td>~$3,300 per parent</td></tr>
<tr><td>Financial assessment</td><td>Varies with complexity</td></tr>
</tbody></table></figure>
<p>Uncontested divorces are far cheaper; contested matters — especially those involving financial disputes or parenting battles — escalate quickly as court appearances and expert reports accumulate.</p>
"""
 + inline_cta("Every dollar spent fighting in court is a dollar out of your settlement. See how mediation protects the pool — book a consultation.")
 + """
<h2 id="property-settlement">Property settlement and financial agreements</h2>
<p>Although legally separate from the divorce, the property settlement is often the largest part of the overall cost. Typical expenses include:</p>
<figure class="tbl"><table><caption>Indicative property settlement costs (AUD)</caption>
<thead><tr><th>Service</th><th>Estimated cost (AUD)</th></tr></thead>
<tbody>
<tr><td>Consent orders (court filing fee)</td><td>~$200</td></tr>
<tr><td>Legal documentation</td><td>$3,000 – $4,500</td></tr>
<tr><td>Binding financial agreement</td><td>$4,500 – $10,000</td></tr>
<tr><td>Mediation sessions</td><td>$150 – $300 per hour</td></tr>
</tbody></table></figure>
<p>A legally binding settlement — through <a href="/consent-orders/">consent orders</a> or a <a href="/financial-agreements-mediation/">binding financial agreement</a> — is essential. Without one, a former spouse can later claim financial entitlements even after the divorce is finalised. <a href="/what-am-i-entitled-to-in-a-separation-in-australia/">Learn what you're entitled to in a separation →</a></p>
<h3>Family Dispute Resolution for matters involving children</h3>
<p>For divorces involving children, Family Dispute Resolution is generally a mandatory step before court. Costs vary — government-funded services may be free or low-cost, while private mediation costs more but typically moves faster. <a href="/section-60i-certificates/">You'll need a Section 60I certificate to proceed to court →</a></p>

<h2 id="mediation-cost">Mediation: the cost-effective alternative</h2>
<p>Here's the comparison that matters most. Before heading to court, most couples are expected to attempt <a href="https://www.ag.gov.au/families-and-marriage/families/family-dispute-resolution" target="_blank" rel="noopener">family dispute resolution</a> — and private mediation commonly costs in the range of $5,000–$7,000 in total, shared between the parties. Many providers, including focused mediation practices, resolve matters for less. The point is the scale of the saving: a contested court case can cost <em>each</em> party tens of thousands of dollars, while mediation resolves the same dispute for a few thousand in total.</p>
<p>For context, here is an indicative fixed-fee mediation structure:</p>
<figure class="tbl"><table><caption>Indicative mediation fees (AUD)</caption>
<thead><tr><th>Service</th><th>Cost (AUD)</th></tr></thead>
<tbody>
<tr><td>Invitation to mediation &amp; certificates</td><td>$350 + GST</td></tr>
<tr><td>Full day of mediation &amp; Heads of Agreement</td><td>$3,500 – $4,500 + GST</td></tr>
</tbody></table></figure>
<p>Beyond cost, mediation is faster, private, and keeps the decision in your hands rather than a judge's. <a href="/how-mediation-works/">See exactly how mediation works →</a></p>
"""
 + inline_cta("Most disputes resolve in one or two mediation sessions — for a fraction of court costs. Find out if yours can too.")
 + """
<h2 id="managing-costs">How to manage your divorce costs</h2>
<ol>
  <li><strong>Try mediation before litigation.</strong> It's the single most effective way to control costs — and for parenting matters, <a href="https://www.fcfcoa.gov.au/fl/fdr" target="_blank" rel="noopener">family dispute resolution is generally required</a> anyway.</li>
  <li><strong>Gather documentation early.</strong> Having paperwork ready reduces back-and-forth (and billable hours) with your lawyer. <a href="/getting-ready-for-separation/">See our separation checklist →</a></li>
  <li><strong>Communicate efficiently with your lawyer.</strong> Be concise and prepared for every meeting.</li>
  <li><strong>Explore fixed-fee arrangements.</strong> They remove the fear of an open-ended bill. <a href="/our-fee-structure/">See our transparent fees →</a></li>
  <li><strong>Check your eligibility for reduced fees.</strong> Concession holders and those in hardship may qualify.</li>
  <li><strong>Stay organised.</strong> Missing deadlines and court dates causes delays that add cost.</li>
</ol>
<p>The bottom line: the cost of divorce in Australia is largely within your control. Choosing resolution over litigation protects both your finances and your wellbeing — and for most families, mediation is the smartest first step.</p>
"""
 ,
 [("Is divorce expensive if both parties agree?",
   "No. An uncontested divorce is far cheaper — the main cost is the court filing fee of around $1,100 (or about $375 if eligible for a reduced fee). Legal costs are lower because there are no disputes to resolve."),
  ("How much does an uncontested divorce cost?",
   "Typically between $1,100 and $5,000, depending on whether you use a lawyer or handle it yourself. Fixed-fee services help manage the expense."),
  ("Is a divorce with children more expensive?",
   "It can be, due to potential disputes over parenting arrangements. The filing fee is the same, but legal and mediation costs may rise if disagreements arise. Family Dispute Resolution is generally required first."),
  ("Do I have to pay my spouse's divorce costs?",
   "Usually each party pays their own legal costs. In certain circumstances a court may order one party to contribute to the other's costs, but this is the exception rather than the rule."),
  ("How much does mediation cost compared to court?",
   "Mediation typically costs $3,500–$4,500 for a full day, shared between parties, versus tens of thousands per side for a contested court case. It's also far faster.")],
 [("what-am-i-entitled-to-in-a-separation-in-australia","What Am I Entitled To?"),
  ("property-settlement-mediation","Property Settlement Mediation"),
  ("our-fee-structure","Our Fee Structure"),
  ("consent-orders","Consent Orders"),
  ("how-mediation-works","How Mediation Works"),
  ("getting-ready-for-separation","Getting Ready for Separation")],
 read_min=11)

# ============================================================
# CORNERSTONE POST 2 — Mediation with a narcissist
# ============================================================
post("mediation-with-a-narcissist",
 "Mediation With a Narcissist: Does It Work? (Expert Guide 2026)",
 "Can mediation work with a narcissistic or highly controlling ex? Yes — and often better than court. The tactics to expect, proven strategies, how to prepare, and when mediation isn't safe.",
 "High-conflict",
 "Mediation With a Narcissist: <em>Does It Actually Work?</em>",
 "It's one of the most common questions we're asked — and the answer surprises people. Mediation with a narcissistic or highly controlling ex can absolutely work, and often delivers better outcomes than court. But it must be done the right way, with the right mediator and the right preparation. Here's everything you need to know.",
 [("can-it-work","Can mediation work with a narcissist?"),
  ("tactics","Tactics a narcissist may use in mediation"),
  ("why-court-worse","Why court is often worse"),
  ("strategies","Strategies that make it work"),
  ("prepare","How to prepare emotionally"),
  ("children","Protecting the children"),
  ("when-not","When mediation isn't appropriate")],
 key_takeaway("Mediation can work well with a narcissistic ex — sometimes better than court — because skilled mediators use structure, firm boundaries and 'shuttle' techniques to neutralise manipulation, and signed agreements become enforceable. But success depends on preparation and the circumstances; where there's family violence or genuine safety risk, other steps may be needed first.")
 + """
<h2 id="can-it-work">Can mediation work with a narcissist?</h2>
<p>Many people assume that if their former partner is narcissistic, manipulative or controlling, mediation is doomed — that the other party will dominate the room and "win." In practice, the opposite is frequently true. A skilled, accredited mediator is specifically trained to manage these dynamics, and the structure of mediation can actually work against a manipulative party rather than for them.</p>
<p>Here's the counterintuitive part: people with strong narcissistic traits — a pattern clinically described in the <a href="https://www.psychiatry.org/patients-families/personality-disorders/what-are-personality-disorders" target="_blank" rel="noopener">DSM-5 framework for personality disorders</a> — are often highly motivated by how they appear to others. In a structured, witnessed setting, that desire to look reasonable can make them more cooperative — and any commitments they make become enforceable once the agreement is signed. The process can effectively hold them to their word in a way an informal conversation never could.</p>
"""
 + inline_cta("Worried about facing a controlling ex? Talk to a mediator experienced in high-conflict matters — confidentially.")
 + """
<h2 id="tactics">Tactics a narcissist may use in mediation</h2>
<p>Knowing what to expect removes much of its power. Common tactics include:</p>
<ul>
  <li><strong>Charm offensive</strong> — trying to win the mediator over and present as the reasonable victim.</li>
  <li><strong>Intimidation</strong> — using tone, body language or veiled threats to unsettle you.</li>
  <li><strong>Gaslighting</strong> — distorting facts to make you doubt your own recollection.</li>
  <li><strong>Projection and blame-shifting</strong> — recasting their conduct as yours.</li>
  <li><strong>Delay and obstruction</strong> — dragging things out to assert control or wear you down.</li>
  <li><strong>Refusing to compromise</strong> — treating every concession as a loss.</li>
</ul>
<p>A skilled mediator recognises these patterns and manages them — redirecting to facts, enforcing ground rules, and refusing to let the process be hijacked.</p>
"""
 + callout("Shuttle mediation: never in the same room",
   "Where there's high conflict, mediation can be run 'shuttle' style — you and your ex stay in separate rooms (or separate video calls) and the mediator moves between you. You never have to face them directly, which removes a key tool of intimidation.")
 + """
<h2 id="why-court-worse">Why court is often worse</h2>
<p>It's tempting to believe a judge will "see through" a manipulative ex and deliver justice. But court is adversarial by design — it can actually reward the party willing to fight longest and hardest, and it hands a controlling person a public stage and years of opportunity to prolong the conflict. For someone who thrives on control and attention, litigation can become the perfect weapon.</p>
<p>Mediation, by contrast, is private, structured and focused on resolution rather than performance. With the right approach it removes much of the oxygen that high-conflict behaviour feeds on, and it gets you to a binding outcome far faster. <a href="/cost-of-divorce-in-australia/">It also costs a fraction of a drawn-out court battle →</a></p>
"""
 + inline_cta("Preparation is everything with a high-conflict ex. We'll help you go in ready — book a confidential consultation.")
 + """
<h2 id="strategies">Strategies that make it work</h2>
<p>Mediating with a high-conflict personality works best when you go in prepared and disciplined:</p>
<ol>
  <li><strong>Set clear goals beforehand.</strong> Know what you genuinely need versus what you'd merely prefer, so provocation can't knock you off course.</li>
  <li><strong>Stay factual.</strong> Skilled mediators use reality-checking — referring to documents, statements and timelines — to counter attempts to rewrite the narrative.</li>
  <li><strong>Choose an experienced mediator.</strong> High-conflict matters are not the place for an inexperienced practitioner.</li>
  <li><strong>Get everything in writing.</strong> Documented agreements prevent later misrepresentation and become enforceable.</li>
  <li><strong>Use shuttle mediation</strong> if being in the same room is intimidating.</li>
  <li><strong>Keep emotion out of the exchange.</strong> A narcissist often seeks an emotional reaction; staying calm and businesslike denies them that.</li>
</ol>

<h2 id="prepare">How to prepare emotionally</h2>
<p>The practical preparation matters, but so does the emotional side. Going in, it helps to: accept that the session may be uncomfortable; rehearse staying calm under provocation, perhaps with a counsellor; lean on a support person before and after; and remind yourself that the goal is a workable future arrangement, not winning an argument about the past. <a href="/divorce-counselling/">Counselling can help you build that resilience →</a></p>
"""
 + inline_cta("You don't have to face this alone or unprepared. Speak with a mediator who understands high-conflict dynamics.")
 + """
<h2 id="children">Protecting the children</h2>
<p>Where children are involved, mediation's child-focused approach is a major advantage. Rather than a courtroom fight that can drag children into the conflict, mediation keeps the focus on practical, future-facing arrangements. A well-drafted <a href="/parenting-plan-mediation/">parenting plan</a> can also reduce future flashpoints by setting clear expectations — which is particularly valuable when one parent tends toward control or unpredictability.</p>

<h2 id="when-not">When mediation isn't appropriate</h2>
<p>Honesty matters here. Mediation is not suitable in every situation. Where there is family violence, a power imbalance that cannot be safely managed, or a genuine safety risk, mediation may not be appropriate — and exemptions exist precisely for these circumstances under the <a href="https://www.fcfcoa.gov.au/fl/fdr" target="_blank" rel="noopener">family dispute resolution requirements</a>. If you are in immediate danger, contact emergency services or <a href="https://www.1800respect.org.au/" target="_blank" rel="noopener">1800RESPECT</a>.</p>
<p>If you're unsure whether your situation is safe for mediation, tell us. We'll give you an honest assessment and, if mediation isn't right, help you find the appropriate path. Your safety always comes first. <a href="/contact-us/">Talk to us confidentially →</a></p>
"""
 ,
 [("Can you really mediate with a narcissist?",
   "Often, yes. Skilled mediators use structure, boundaries and shuttle techniques to manage manipulation, and the enforceability of signed agreements can hold a controlling party to their commitments. Success depends on preparation and circumstances."),
  ("Isn't court better for dealing with a manipulative ex?",
   "Usually not. Court is adversarial and public, which can reward prolonged conflict and give a controlling person a stage. Mediation is private and resolution-focused, removing much of what high-conflict behaviour feeds on, and it's faster and cheaper."),
  ("What is shuttle mediation?",
   "Shuttle mediation keeps you and your ex in separate rooms (or separate video calls), with the mediator moving between you. You never have to face them directly — useful in high-conflict or safety-sensitive situations."),
  ("How do I prepare for mediation with a narcissist?",
   "Set clear goals, stay factual, document everything, choose an experienced mediator, consider shuttle mediation, and prepare emotionally — ideally with support from a counsellor."),
  ("When is mediation not appropriate?",
   "Where there is family violence, an unmanageable power imbalance, or a genuine safety risk, mediation may not be suitable, and exemptions apply. If you're in immediate danger, contact emergency services.")],
 [("family-law-mediation","Family Law Mediation"),
  ("parenting-plan-mediation","Parenting Plan Mediation"),
  ("divorce-counselling","Divorce Counselling"),
  ("how-mediation-works","How Mediation Works"),
  ("what-am-i-entitled-to-in-a-separation-in-australia","What Am I Entitled To?"),
  ("cost-of-divorce-in-australia","Cost of Divorce")],
 read_min=10)

# ============================================================
# POST 3 — What am I entitled to in a separation
# ============================================================
post("what-am-i-entitled-to-in-a-separation-in-australia",
 "What Am I Entitled To in a Separation in Australia? (2026)",
 "What are you entitled to when you separate in Australia? A full guide to how property, superannuation and support are divided under the four-step process — and how to reach a fair split without court.",
 "Property &amp; finances",
 "What Am I Entitled To in a Separation in Australia?",
 "There is no fixed formula and no automatic 50/50 split in Australian family law. What you're entitled to depends on the total asset pool, each person's contributions, your future needs, and what's fair overall. This guide explains exactly how entitlements are worked out — and how to reach a fair outcome without a court battle.",
 [("no-formula","Why there's no automatic 50/50"),
  ("four-steps","The four-step process explained"),
  ("contributions","How contributions are assessed"),
  ("future-needs","How future needs are weighed"),
  ("whats-included","What's included in the asset pool"),
  ("super","Superannuation and entitlements"),
  ("time-limits","Time limits you need to know"),
  ("reaching-fair","Reaching a fair split without court")],
 key_takeaway("Australian law applies no fixed split. Courts and mediators follow a four-step process: identify the asset pool, assess contributions (financial and non-financial), consider future needs, and confirm the result is just and equitable. The outcome could be 50/50, 60/40, 70/30 or otherwise — it depends entirely on your circumstances.")
 + """
<h2 id="no-formula">Why there's no automatic 50/50</h2>
<p>One of the most persistent myths about separation is that assets are simply halved. They are not. Australian family law, under the <a href="https://www.austlii.edu.au/cgi-bin/viewdb/au/legis/cth/consol_act/fla1975114/" target="_blank" rel="noopener">Family Law Act 1975</a>, doesn't apply a fixed percentage. Instead it asks a broader question: what division is just and equitable given everything about this particular relationship? Depending on the facts, a fair result might be an even split, or it might be weighted 60/40 or 70/30 toward one party.</p>
<p>This is actually good news. It means your individual circumstances — what you contributed, what you'll need going forward — genuinely matter, rather than being flattened into a mechanical formula.</p>
"""
 + inline_cta("Want to know what a fair split looks like in your situation? Get a clear picture in a fixed-fee consultation.")
 + """
<h2 id="four-steps">The four-step process explained</h2>
<p>Both courts and mediators work through the same four-step framework to determine entitlements:</p>
<figure class="tbl"><table><caption>The four-step property settlement process</caption>
<thead><tr><th>Step</th><th>What happens</th></tr></thead>
<tbody>
<tr><td>1. Identify the asset pool</td><td>Establish everything owned and owed — jointly and individually.</td></tr>
<tr><td>2. Assess contributions</td><td>Weigh financial and non-financial contributions by each party.</td></tr>
<tr><td>3. Consider future needs</td><td>Account for earning capacity, age, health and care of children.</td></tr>
<tr><td>4. Check it's just and equitable</td><td>Stand back and confirm the overall outcome is genuinely fair.</td></tr>
</tbody></table></figure>
<p>In <a href="/property-settlement-mediation/">property settlement mediation</a>, you work through each step openly with a neutral mediator — so your agreement reflects the very principles a court would apply, but is reached in weeks rather than years.</p>

<h2 id="contributions">How contributions are assessed</h2>
<p>Contributions fall into two categories, and crucially, both count:</p>
<ul>
  <li><strong>Financial contributions</strong> — income earned, assets brought into the relationship, inheritances, and money spent on property or improvements.</li>
  <li><strong>Non-financial contributions</strong> — raising children, homemaking, renovations and unpaid work that supported the family or a partner's career.</li>
</ul>
<p>A frequent worry is: "I earned less, so will I get less?" Not necessarily. The law expressly recognises that a parent who stayed home or worked part-time to raise children contributed just as meaningfully as the higher earner. Contributions are also assessed across the whole relationship, including the period since separation.</p>
"""
 + callout("Initial contributions matter — but they fade over time",
   "Assets one partner brought into the relationship are considered, but in a long relationship their significance is usually diluted by years of joint contributions. In a short relationship, they tend to carry more weight.")
 + """
<h2 id="future-needs">How future needs are weighed</h2>
<p>After contributions, the law looks forward. Two people who contributed equally may still receive different shares if their future circumstances differ. Factors include:</p>
<ul>
  <li>Age and the state of each person's health</li>
  <li>Income and earning capacity, and the difference between them</li>
  <li>Who has the primary care of the children</li>
  <li>The length of the relationship and its effect on earning ability</li>
</ul>
<p>For example, a parent who will care for young children and has reduced earning capacity may receive an adjustment in their favour to reflect that future need.</p>
"""
 + inline_cta("Future needs can shift the outcome significantly. Talk to a mediator about how they apply to you.")
 + """
<h2 id="whats-included">What's included in the asset pool</h2>
<p>The asset pool is broader than many people expect. It typically includes:</p>
<ul>
  <li>The family home and any other real estate</li>
  <li>Superannuation (which can be split between partners)</li>
  <li>Savings, shares and investments</li>
  <li>Vehicles, furniture and personal property</li>
  <li>Business interests, companies and trusts</li>
  <li>Debts, mortgages and other liabilities (which reduce the pool)</li>
</ul>
<p>Both parties have a <a href="https://www.fcfcoa.gov.au/fl/duty-disclosure" target="_blank" rel="noopener">duty of full and frank financial disclosure</a> — hiding assets is taken very seriously by the courts. <a href="/property-settlement-mediation/">See how property settlement mediation handles disclosure →</a></p>

<h2 id="super">Superannuation and entitlements</h2>
<p>Superannuation is treated as property under family law and can be split between partners as part of a settlement. This often surprises people, but it's an important entitlement — particularly where one partner has a much larger balance because the other took time out of the workforce to raise children. A superannuation split can be formalised through consent orders or a financial agreement.</p>

<h2 id="time-limits">Time limits you need to know</h2>
<p>Entitlements don't stay open indefinitely. Key time limits:</p>
<ul>
  <li><strong>Married couples:</strong> generally 12 months from the date the divorce becomes final to apply for property orders.</li>
  <li><strong>De facto couples:</strong> generally two years from the date of separation.</li>
</ul>
<p>Mediation is the fastest way to reach a binding agreement inside these windows. <a href="/de-facto-mediation/">See de facto entitlements and time limits →</a></p>
"""
 + inline_cta("Time limits apply to property settlements. Don't leave it too late — book a consultation today.")
 + """
<h2 id="reaching-fair">Reaching a fair split without court</h2>
<p>You don't need a judge to divide your property — and in most cases, you shouldn't want one. Mediation lets you and your former partner reach a fair agreement based on the same four-step legal framework, then formalise it through <a href="/consent-orders/">consent orders</a> or a <a href="/financial-agreements-mediation/">binding financial agreement</a> so it's legally enforceable. It's faster, cheaper, private, and keeps the decision where it belongs — with the two of you. <a href="/how-mediation-works/">See how the process works →</a></p>
"""
 ,
 [("Is everything split 50/50 in an Australian separation?",
   "No. There's no automatic 50/50 split. The division depends on the asset pool, each party's financial and non-financial contributions, future needs, and what's just and equitable overall — it could be 50/50, 60/40, 70/30 or otherwise."),
  ("Do non-financial contributions count?",
   "Yes. Raising children, homemaking and supporting a partner's career are weighed alongside financial contributions. A lower earner is not automatically entitled to less."),
  ("Is superannuation included in a property settlement?",
   "Yes. Superannuation is treated as property and can be split between partners, formalised through consent orders or a financial agreement."),
  ("How long do I have to claim a property settlement?",
   "Generally 12 months after a divorce is finalised, or two years from separation for de facto couples. Mediation is the fastest way to reach a binding agreement within these limits."),
  ("What if my ex is hiding assets?",
   "Both parties have a duty of full financial disclosure. Hiding assets is treated seriously by the courts and can lead to penalties or a settlement being set aside.")],
 [("property-settlement-mediation","Property Settlement Mediation"),
  ("financial-agreements-mediation","Binding Financial Agreements"),
  ("consent-orders","Consent Orders"),
  ("de-facto-mediation","De Facto Mediation"),
  ("cost-of-divorce-in-australia","Cost of Divorce"),
  ("how-mediation-works","How Mediation Works")],
 read_min=9)

# ============================================================
# POST 4 — How long does mediation take
# ============================================================
post("how-long-does-mediation-take",
 "How Long Does Mediation Take in Australia? (2026 Guide)",
 "How long does mediation take in Australia? Most disputes resolve in one or two sessions within a few weeks — versus one to three years in court. Full timeline, what affects it, and how to speed it up.",
 "The process",
 "How Long Does Mediation Take?",
 "Most family law mediations resolve in just one or two sessions, often within a few weeks of starting. Compare that to the one to three years a contested court case can take, and the appeal is obvious. This guide walks through the realistic timeline, what speeds it up or slows it down, and how it stacks up against litigation.",
 [("typical-timeline","The typical mediation timeline"),
  ("single-session","How long is a single session?"),
  ("what-affects","What affects how long it takes"),
  ("vs-court","How that compares to court"),
  ("complex","What about complex matters?"),
  ("speed-it-up","How to speed things up")],
 key_takeaway("Most mediations resolve in one to two sessions, frequently within a few weeks. A single session runs from a couple of hours to a full day. Complex financial matters may need more time, but even then mediation is dramatically faster than the one to three years a contested court case typically takes.")
 + """
<h2 id="typical-timeline">The typical mediation timeline</h2>
<p>From first contact to a signed, binding agreement, mediation usually moves quickly. Here's the realistic shape of it:</p>
<figure class="tbl"><table><caption>Typical mediation timeline</caption>
<thead><tr><th>Stage</th><th>Typical timeframe</th></tr></thead>
<tbody>
<tr><td>Initial consultation</td><td>Booked within days; a fixed-fee session</td></tr>
<tr><td>Preparation &amp; intake</td><td>1–3 weeks (gathering documents, inviting the other party)</td></tr>
<tr><td>The mediation session</td><td>Usually a single day</td></tr>
<tr><td>Formalising the agreement</td><td>Consent orders prepared and lodged afterwards</td></tr>
</tbody></table></figure>
<p>For many couples the substantive process — from booking to agreement — is complete within a few weeks. <a href="/how-mediation-works/">See the full step-by-step process →</a></p>
"""
 + inline_cta("Ready to resolve things in weeks, not years? Book a consultation and we'll map out your timeline.")
 + """
<h2 id="single-session">How long is a single session?</h2>
<p>A typical mediation session runs anywhere from two or three hours to a full day, depending on the number of issues and the level of agreement going in. Parenting-only matters can sometimes be resolved in a half-day; a full property settlement often uses a full day. Many matters are designed around a single full-day session that produces a Heads of Agreement by the end.</p>

<h2 id="what-affects">What affects how long it takes</h2>
<ul>
  <li><strong>Complexity of the matter</strong> — a straightforward parenting plan is faster than a property pool with businesses, trusts and superannuation.</li>
  <li><strong>Level of conflict</strong> — the more entrenched the dispute, the more sessions may be needed.</li>
  <li><strong>Quality of preparation</strong> — having documents and financial disclosure ready dramatically shortens the process.</li>
  <li><strong>Both parties' willingness</strong> — genuine engagement from both sides is the single biggest accelerator.</li>
  <li><strong>Whether valuations are needed</strong> — waiting on a property or business valuation can add a few weeks.</li>
</ul>
"""
 + callout("Even a partial agreement saves time",
   "If mediation doesn't resolve absolutely everything, it almost always narrows the issues — meaning a faster, cheaper process for anything that does proceed. Nothing invested in mediation is wasted.")
 + """
<h2 id="vs-court">How that compares to court</h2>
<p>The contrast is stark. A contested family law matter can take one to three years to reach a final hearing, with multiple interim court dates, adjournments and long waiting periods in between (see the <a href="https://www.fcfcoa.gov.au/" target="_blank" rel="noopener">Federal Circuit and Family Court of Australia</a>). Court lists in the busier registries are <a href="https://www.fcfcoa.gov.au/" target="_blank" rel="noopener">heavily backed up</a>, which only adds to the delay. Most parenting matters also require <a href="https://www.ag.gov.au/families-and-marriage/families/family-dispute-resolution" target="_blank" rel="noopener">family dispute resolution</a> before filing.</p>
<p>Mediation compresses all of that into a matter of weeks. The time saved isn't just a convenience — it means far less stress, dramatically lower cost, and a faster fresh start for everyone involved, especially the children. <a href="/cost-of-divorce-in-australia/">See how that time saving translates into cost savings →</a></p>
"""
 + inline_cta("Why wait years for a court date? Most mediations finish in weeks. Find out how fast yours could be.")
 + """
<h2 id="complex">What about complex matters?</h2>
<p>Some matters genuinely need more than one session — a large or contested asset pool, a family business requiring valuation, or a high-conflict dynamic. Even then, mediation typically spans a few sessions over a few weeks, not the years a contested trial would consume. Where one issue remains stuck, <a href="/family-law-arbitration/">arbitration</a> can deliver a binding decision on that point quickly, without a full court case.</p>

<h2 id="speed-it-up">How to speed things up</h2>
<ol>
  <li><strong>Come prepared.</strong> Gather financial documents and think through your goals before you start. <a href="/preparing-for-mediation/">See how to prepare →</a></li>
  <li><strong>Choose online mediation.</strong> <a href="/online-divorce/">Online sessions</a> remove travel and are far easier to schedule.</li>
  <li><strong>Complete disclosure early.</strong> Having full financial disclosure ready avoids mid-process delays.</li>
  <li><strong>Focus on outcomes, not blame.</strong> The faster both parties move past grievances, the faster you resolve.</li>
</ol>
<p>Done well, mediation turns what could be years of litigation into a few focused weeks — and leaves you in control of the outcome the whole way through.</p>
"""
 ,
 [("How many mediation sessions are usually needed?",
   "Most matters resolve in one or two sessions. A single session runs from a couple of hours to a full day, depending on complexity."),
  ("How long does a mediation session last?",
   "Typically two or three hours up to a full day. Many matters are designed around a single full-day session that produces a Heads of Agreement."),
  ("Is mediation really faster than court?",
   "Dramatically. Mediation usually resolves within weeks, while a contested court case can take one to three years to reach a final hearing."),
  ("What if we don't finish in one session?",
   "Some matters, especially complex financial ones, need a follow-up session. Even then it's far faster than litigation, and any progress narrows the remaining issues."),
  ("How quickly can I get started?",
   "An initial consultation can usually be booked within days, and the mediation itself scheduled within a few weeks once both parties are ready.")],
 [("how-mediation-works","How Mediation Works"),
  ("preparing-for-mediation","Preparing for Mediation"),
  ("online-divorce","Online Mediation"),
  ("cost-of-divorce-in-australia","Cost of Divorce"),
  ("family-law-arbitration","Family Law Arbitration"),
  ("family-law-mediation","Family Law Mediation")],
 read_min=8)

print("\nCornerstone posts (batch 1) built.")
