#!/usr/bin/env python3
"""Resource/guide pages + booking form. Keyword-first H1s, full schema."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, faq_html, cta_band,
                       org_schema, faq_schema, breadcrumb_schema, article_schema,
                       BOOK_URL, PHONE, PHONE_HREF)
OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def build(slug,title,desc,eyebrow,h1,lede,ans,blocks,qa,crumb,cta_h,cta_p,is_article=True):
    extra=article_schema(crumb,desc) if is_article else None
    schema=[org_schema(),breadcrumb_schema([("Home",""),("Resources",None if False else "preparing-for-mediation"),(crumb,slug)])]
    if extra: schema.append(extra)
    if qa: schema.append(faq_schema(qa))
    d=head(title,desc,slug,extra_schema=schema)+nav()
    d+=f"""<main id="main">
{crumb_html([("Home",""),("Resources",None),(crumb,None)])}
<section class="phero"><div class="phero-blob"></div><div class="wrap">
<span class="eyebrow"><span class="pulse"></span>{eyebrow}</span>
<h1>{h1}</h1><p class="lede">{lede}</p>
<div class="phero-cta"><a href="{BOOK_URL}" class="btn btn-primary">Book a Free Consultation <span class="arr">→</span></a>
<a href="{PHONE_HREF}" class="btn btn-ghost">Call {PHONE}</a></div>
</div></section>
<div class="wrap-narrow"><div class="answer reveal"><p><strong>In short:</strong> {ans}</p></div></div>
<article class="body"><div class="wrap-narrow reveal">{blocks}</div></article>"""
    if qa: d+=faq_html(qa,heading=f"{crumb} — FAQs")
    d+=cta_band(cta_h,cta_p)+"</main>"+page_end()
    p=os.path.join(OUT,slug); os.makedirs(p,exist_ok=True)
    open(os.path.join(p,"index.html"),"w").write(d)
    import re; return slug,len(re.sub(r'<[^>]+>',' ',d).split())

# ---- PARENTING PLAN TEMPLATE ----
build("parenting-plan-template",
 "Parenting Plan Template Australia | What to Include (2026)",
 "A complete guide to what belongs in a parenting plan in Australia — living arrangements, time, decisions, holidays and dispute resolution. Build yours with accredited mediators.",
 "A practical guide for separated parents",
 "Parenting Plan Template",
 "A parenting plan is the practical backbone of co-parenting after separation. This guide walks through every section a thorough Australian parenting plan should cover — with worked examples, common mistakes to avoid, and how to turn a draft into an arrangement that actually holds.",
 "A parenting plan should cover where the children live, how time is shared week to week, holidays and special occasions, how major decisions are made, communication between parents, travel arrangements, and how disputes will be handled. A mediator helps parents negotiate each section so the plan reflects the children's real needs rather than what either parent prefers.",
 """
 <h2>What is a parenting plan?</h2>
 <p>A parenting plan is a written agreement between separated parents that sets out how their children will be raised across two households. Under the <a href="https://www.legislation.gov.au/Details/C2021C00095" target="_blank" rel="noopener">Family Law Act 1975</a>, a parenting plan must be in writing and signed and dated by both parents. It is not a court order, but a court will consider it in any later dispute — and it is far more useful than an oral agreement that each party later remembers differently.</p>
 <p>A parenting plan is different from <a href="/consent-orders/">consent orders</a>, which are court-approved and directly enforceable. Many families use a parenting plan as a starting point and later formalise it as consent orders once arrangements have settled.</p>

 <h2>The full template: what to cover section by section</h2>

 <h3>1. Living arrangements</h3>
 <p>Specify where the children primarily live and describe the week-to-week routine clearly enough that there's no room for argument. Include:</p>
 <ul>
   <li>Which parent the child lives with during the school week</li>
   <li>Which parent has time at weekends and when</li>
   <li>How transitions happen — who drops off, who collects, at what time and where</li>
   <li>What happens if one parent is late or unavailable</li>
 </ul>
 <div class="callout"><h3>Worked example: week on / week off</h3>
 <p>"[Child] will live with Parent A Sunday evening to Sunday evening in alternating weeks. Parent B will collect from school on the first day of their week and Parent A will collect at the end. If either parent is unable to collect, they will notify the other by 2pm that day and the other parent will collect instead."</p></div>

 <h3>2. Time with each parent</h3>
 <p>Detail regular time arrangements with enough specificity that both parents can follow the plan without needing to negotiate each week. Consider:</p>
 <ul>
   <li>Weekday and weekend routine during term time</li>
   <li>Before and after school arrangements</li>
   <li>How overnight stays are scheduled</li>
   <li>What happens when the child is sick</li>
 </ul>

 <h3>3. School holidays</h3>
 <p>School holidays are a common flashpoint. Set out exactly how each holiday period is divided — don't leave it as "to be agreed each time".</p>
 <figure class="tbl"><table>
 <caption>Common holiday allocation approaches</caption>
 <thead><tr><th>Holiday period</th><th>Approach A (split evenly)</th><th>Approach B (alternating years)</th></tr></thead>
 <tbody>
 <tr><td>Christmas</td><td>First half / second half alternating years</td><td>Parent A odd years, Parent B even years</td></tr>
 <tr><td>Easter</td><td>Good Friday weekend / Easter Monday weekend alternating</td><td>Opposite to Christmas allocation</td></tr>
 <tr><td>School term breaks</td><td>First week / second week each break</td><td>Alternating school holiday periods</td></tr>
 <tr><td>Winter holidays</td><td>Split evenly, parents choose halves</td><td>Alternating years</td></tr>
 </tbody></table></figure>

 <h3>4. Special occasions</h3>
 <p>Specify what happens on birthdays, Mother's Day, Father's Day, and significant cultural or religious occasions. These are predictable pressure points — plan for them in advance.</p>

 <h3>5. Major decision-making</h3>
 <p>The <a href="https://www.legislation.gov.au/Details/C2021C00095" target="_blank" rel="noopener">Family Law Act</a> distinguishes between day-to-day decisions (each parent makes these during their time) and long-term decisions about the child's welfare. Specify how you'll handle:</p>
 <ul>
   <li><strong>Education</strong> — which school, subject choices, tutoring, extracurriculars</li>
   <li><strong>Health</strong> — routine medical appointments, elective procedures, choice of doctor or dentist</li>
   <li><strong>Religion and culture</strong> — religious upbringing and cultural practices</li>
   <li><strong>Travel</strong> — interstate and overseas holidays, passport applications</li>
   <li><strong>Name changes</strong></li>
 </ul>
 <p>Most plans provide for joint decision-making on major issues, with a process for resolving disagreement — such as mediation — before either parent can act unilaterally.</p>

 <h3>6. Communication between parents</h3>
 <p>Agree on how you'll communicate — about the children, not about each other. Many plans specify:</p>
 <ul>
   <li>Preferred channel (email, a co-parenting app, text)</li>
   <li>Expected response times for non-urgent matters</li>
   <li>How to handle urgent or emergency communication</li>
   <li>Whether a parent can contact the children during the other's time, and how</li>
 </ul>

 <h3>7. Travel and relocation</h3>
 <p>Address domestic and international travel separately. For overseas travel, specify notice periods, passport arrangements, and what documentation the travelling parent will carry. Relocation — one parent moving significantly further away — is one of the most contested issues in family law. Even if it seems unlikely now, consider including a process for how it would be handled.</p>

 <h3>8. Changeover arrangements</h3>
 <p>Specify exactly where and when changeovers happen. "At school" is clearer and lower-conflict than "at the front door". Include a fallback: what happens if a parent is more than 30 minutes late?</p>

 <h3>9. Dispute resolution</h3>
 <p>Include a clause committing both parents to return to mediation before escalating any dispute to court. This is one of the most valuable provisions in any parenting plan — it keeps minor disagreements from becoming expensive litigation.</p>

 <h3>10. Review and variation</h3>
 <p>Children's needs change. Build in a scheduled review — annually, or when a child changes school — and agree on a process for proposing changes. A plan that can be updated by agreement is far more durable than one that can only be changed through court.</p>

 <h2>Parenting plan vs consent orders: which do you need?</h2>
 <figure class="tbl"><table>
 <thead><tr><th></th><th>Parenting plan</th><th>Consent orders</th></tr></thead>
 <tbody>
 <tr><td>Legally binding</td><td>No — but courts consider it</td><td>Yes — directly enforceable</td></tr>
 <tr><td>Court involvement</td><td>None</td><td>Registered with court (no hearing)</td></tr>
 <tr><td>Flexibility to vary</td><td>High — by agreement</td><td>Lower — requires consent or court order</td></tr>
 <tr><td>Cost</td><td>Lower</td><td>Slightly higher (court filing fee)</td></tr>
 <tr><td>Best for</td><td>Early-stage, cooperative arrangements</td><td>Where you want certainty and enforceability</td></tr>
 </tbody></table></figure>

 <h2>Common mistakes in parenting plans</h2>
 <ul>
   <li><strong>Too vague</strong> — "reasonable time with each parent" sounds flexible but causes constant negotiation and disputes.</li>
   <li><strong>No holiday detail</strong> — leaving holidays as "to be agreed" is the most common source of conflict.</li>
   <li><strong>No changeover specifics</strong> — ambiguity about time and place breeds conflict at handover.</li>
   <li><strong>Forgetting the children's activities</strong> — who drives to sport, who pays for extracurriculars, what happens when activities conflict with changeover?</li>
   <li><strong>No review mechanism</strong> — a plan written when a child is 4 won't suit a teenager.</li>
 </ul>

 <h2>How mediation helps you build a better plan</h2>
 <p>A mediator doesn't draft the plan for you — they help you and the other parent work through each section together, drawing out the details that matter, surfacing disagreements early, and finding workable solutions. The result is a plan both parents have genuinely agreed to, which is what makes it last. <a href="/parenting-plan-mediation/">See parenting plan mediation →</a></p>
 """,
 [("What should be included in a parenting plan in Australia?",
   "Living arrangements, weekly time with each parent, school holiday allocation, special occasions, major decision-making, communication between parents, travel, changeover arrangements, dispute resolution, and how the plan will be reviewed. The more specific it is, the fewer disputes arise."),
  ("Is a parenting plan legally binding in Australia?",
   "No. A parenting plan is not a court order and cannot be directly enforced. However, a court will consider it in any later dispute, and it is far more useful than a verbal agreement. To make arrangements directly enforceable, formalise them as consent orders."),
  ("Do I need a lawyer to make a parenting plan?",
   "No. A parenting plan can be made directly between parents, and a mediator can help you cover everything thoroughly. Independent legal advice is recommended before formalising anything as consent orders."),
  ("Can a parenting plan be changed later?",
   "Yes — by written agreement between both parents. The Family Law Act allows parenting plans to be varied or replaced by a later signed agreement. Build a review process into the plan itself so changes happen constructively."),
  ("What is the difference between a parenting plan and consent orders?",
   "A parenting plan is a private written agreement — flexible but not directly enforceable. Consent orders are court-approved and enforceable. Many families start with a parenting plan and convert to consent orders once arrangements are settled."),
  ("How specific should a parenting plan be?",
   "Specific enough that neither parent has to negotiate week by week. Vague terms like 'reasonable time' cause disputes. Specify days, times, locations, and fallback arrangements for common scenarios like illness or late pick-up.")],
 "Parenting Plan Template",
 "Build a parenting plan that <em>actually works</em>.",
 "Book a free initial consultation and let an accredited mediator help you create a complete, child-focused parenting plan.")

# ---- BFA OR CONSENT ORDERS ----
build("bfa-or-consent-orders",
 "BFA or Consent Orders? Which Is Right for You (2026 Guide)",
 "BFA or consent orders? Compare the two ways to formalise a property settlement in Australia — cost, finality, flexibility and when each applies. Free consultation.",
 "Know which one to choose before you sign",
 "BFA or Consent Orders",
 "Once you've reached an agreement on property, you need to make it legally binding. There are two main routes: consent orders and binding financial agreements. They work differently, cost differently, and suit different situations. This guide explains which is right for you.",
 "Consent orders are approved by the Federal Circuit and Family Court — simpler, cheaper, and suitable for most separating couples. A binding financial agreement (BFA) is a private contract that offers more flexibility, can be made before or during a relationship, but requires independent legal advice from a lawyer for each party. For most people finalising a separation, consent orders are the better starting point.",
 """
 <h2>What are consent orders?</h2>
 <p><a href="/consent-orders/">Consent orders</a> are orders made by the Federal Circuit and Family Court of Australia that reflect an agreement the parties have already reached. You don't attend court — a registrar reviews the proposed orders on the papers and, if satisfied they are just and equitable, approves them. Once approved, they are binding court orders with the full force of law behind them.</p>
 <p>Consent orders can cover property (real estate, superannuation, savings, debts), parenting arrangements, and spousal maintenance. They are the most common way to formalise a property settlement after separation.</p>

 <h2>What is a binding financial agreement (BFA)?</h2>
 <p>A <a href="/financial-agreements-mediation/">binding financial agreement</a> is a private contract between two people that sets out how assets, finances and (in some cases) maintenance will be handled. Unlike consent orders, a BFA is never reviewed or approved by a court — it takes effect as a private contract once each party has received independent legal advice from a lawyer and both lawyers have signed a statement confirming that advice was given.</p>
 <p>BFAs can be made at three stages: before a marriage or de facto relationship begins (a "prenup"), during the relationship, or after separation. This flexibility is their main advantage.</p>

 <h2>Side-by-side comparison</h2>
 <figure class="tbl"><table>
 <thead><tr><th></th><th>Consent orders</th><th>Binding financial agreement</th></tr></thead>
 <tbody>
 <tr><td>Court involvement</td><td>Yes — court reviews and approves</td><td>No — private contract</td></tr>
 <tr><td>When it can be made</td><td>On or after separation</td><td>Before, during or after the relationship</td></tr>
 <tr><td>Independent legal advice required</td><td>Not mandatory, but recommended</td><td>Mandatory for both parties — agreement is void without it</td></tr>
 <tr><td>Typical cost (legal fees)</td><td>$1,500–$3,500 combined</td><td>$3,000–$8,000+ combined (each party needs own lawyer)</td></tr>
 <tr><td>What it can cover</td><td>Property, super, parenting, maintenance</td><td>Property, super, maintenance (not parenting)</td></tr>
 <tr><td>Grounds to challenge</td><td>Fraud, non-disclosure, impracticable</td><td>Non-disclosure, undue influence, no legal advice</td></tr>
 <tr><td>Suitable for prenup</td><td>No</td><td>Yes</td></tr>
 </tbody></table></figure>

 <h2>Which should you choose?</h2>
 <p>For most separating couples finalising a property split, <strong>consent orders are the better default</strong>. They are cheaper, faster, cover parenting as well as property, and carry the weight of court approval — which makes them harder to challenge. The court's "just and equitable" check is a feature, not a bureaucratic hurdle: it protects both parties.</p>
 <p>A BFA makes more sense when:</p>
 <ul>
   <li>You want to make arrangements before or during a relationship (a prenup or mid-relationship agreement)</li>
   <li>You have strong privacy reasons to keep the agreement entirely off court records</li>
   <li>Your situation is genuinely unusual in a way consent orders can't accommodate</li>
   <li>You are de facto and separated more than two years ago (outside the window for court property orders)</li>
 </ul>

 <h2>What happens if you do nothing?</h2>
 <p>Not formalising your settlement is the most common — and most costly — mistake. Without consent orders or a BFA:</p>
 <ul>
   <li>Either party can return to court to claim a share of assets years later</li>
   <li>The other person's future spouse, creditors or estate may have a claim over assets you thought were yours</li>
   <li>Time limits apply: married couples have 12 months from the date of divorce; de facto couples have 24 months from separation</li>
 </ul>
 <div class="callout"><h3>The hard part is reaching the agreement</h3>
 <p>Whichever instrument you use, the real work is negotiating a fair outcome — which is exactly what <a href="/property-settlement-mediation/">property settlement mediation</a> does in a single day. Once agreement is reached, your lawyers can draft and formalise it. <a href="/property-settlement-mediation/">See property settlement mediation →</a></p></div>

 <h2>Cost comparison: a worked example</h2>
 <p>For a typical couple with a house, super, and one shared car:</p>
 <figure class="tbl"><table>
 <thead><tr><th>Step</th><th>Via consent orders</th><th>Via BFA</th></tr></thead>
 <tbody>
 <tr><td>Mediation (property settlement)</td><td>~$3,000–$5,000 shared</td><td>~$3,000–$5,000 shared</td></tr>
 <tr><td>Legal drafting</td><td>~$1,500–$3,000 combined</td><td>~$3,000–$8,000 combined</td></tr>
 <tr><td>Court filing fee</td><td>$175 (2026)</td><td>Nil</td></tr>
 <tr><td>Total (approximate)</td><td><strong>$5,000–$8,000</strong></td><td><strong>$6,000–$13,000</strong></td></tr>
 </tbody></table></figure>
 <p>Both paths cost a fraction of contested litigation, which typically runs $30,000–$150,000 per side. <a href="/family-law-cost-estimator/">See the full cost comparison →</a></p>
 """,
 [("Is a BFA or consent orders cheaper?",
   "Consent orders are generally cheaper. A BFA requires mandatory independent legal advice from a separate lawyer for each party, which adds cost. For most separating couples, consent orders are the more cost-effective route."),
  ("Can a BFA be made before marriage?",
   "Yes. A binding financial agreement can be made before, during or after a marriage or de facto relationship. One made before is often called a prenup. Consent orders can only be made on or after separation."),
  ("Do I have to go to court for consent orders?",
   "No. Consent orders are reviewed on the papers by a registrar — there is no hearing. You submit the application and draft orders, pay the filing fee, and the court approves them without anyone attending."),
  ("Are consent orders harder to overturn than a BFA?",
   "Generally yes, because they carry court approval. A BFA can be set aside on contract-related grounds like non-disclosure or failure to obtain independent legal advice. Both are binding when properly made."),
  ("What if I miss the time limit?",
   "Married couples must apply for property orders within 12 months of their divorce becoming final. De facto couples have 24 months from the date of separation. After these deadlines, you need court permission to proceed, which adds cost and uncertainty."),
  ("Can consent orders cover both property and parenting?",
   "Yes — consent orders are the only instrument that can cover both in the same document. A BFA cannot include parenting arrangements.")],
 "BFA or Consent Orders",
 "Choose the right way to make it binding.",
 "Book a consultation and we'll help you reach agreement and formalise it the right way for your situation.")

# ---- GETTING READY FOR SEPARATION ----
build("getting-ready-for-separation",
 "Getting Ready for Separation | Practical Checklist 2026",
 "A practical guide to preparing for separation in Australia — finances, documents, children, legal steps and wellbeing. What to do first, what to avoid, and how mediation helps.",
 "The first steps you take matter most",
 "Getting Ready for Separation",
 "The decisions you make in the first weeks of separation have a disproportionate effect on the months that follow. This practical guide covers every step — financial, legal, parenting and personal — so you're prepared rather than reactive, and so the process ahead is as straightforward as it can be.",
 "To get ready for separation, record your separation date, gather all financial documents, understand the full asset pool, think carefully about parenting arrangements, and get an early understanding of your legal options. Acting early and systematically protects your interests and makes mediation — the fastest path to resolution — far more productive.",
 """
 <h2>Step 1: Record your separation date</h2>
 <p>Your separation date is more important than most people realise. It starts the clock on time limits for property applications — 12 months from divorce for married couples, 24 months from separation for de facto couples. It also affects Centrelink entitlements, tax, and how assets are valued in a property settlement.</p>
 <p>Write down the date, note it in a message to yourself, or send a brief email — something dated and retrievable. If you're separating under one roof, see our guide to <a href="/separation-under-one-roof/">separation under one roof</a> for what else you'll need to document.</p>

 <h2>Step 2: Gather your financial documents</h2>
 <p>A property settlement requires a complete and honest picture of everything you own and owe, together and separately. Start collecting:</p>
 <figure class="tbl"><table>
 <caption>Financial documents to gather</caption>
 <thead><tr><th>Category</th><th>What to collect</th></tr></thead>
 <tbody>
 <tr><td>Property</td><td>Recent valuations or sales data, mortgage statements, council rates notices</td></tr>
 <tr><td>Superannuation</td><td>Latest statements for all super funds — both yours and your partner's</td></tr>
 <tr><td>Bank accounts</td><td>Statements for all accounts — joint and individual — for the past 12–24 months</td></tr>
 <tr><td>Income</td><td>Payslips, tax returns, business financials if self-employed</td></tr>
 <tr><td>Investments</td><td>Share portfolios, managed funds, cryptocurrency holdings</td></tr>
 <tr><td>Vehicles</td><td>Registration documents, finance contracts</td></tr>
 <tr><td>Debts</td><td>Credit card statements, personal loan balances, HECS, any guarantees</td></tr>
 <tr><td>Business interests</td><td>Trust deeds, company documents, accountant valuations</td></tr>
 </tbody></table></figure>
 <p>Both parties are legally required to make full financial disclosure in any property settlement. Gathering your own documents early means you're not dependent on your former partner's cooperation later.</p>

 <h2>Step 3: Understand the full asset pool</h2>
 <p>The "asset pool" in a property settlement includes everything owned by either of you — jointly or individually — minus all liabilities. Under the <a href="https://www.legislation.gov.au/Details/C2021C00095" target="_blank" rel="noopener">Family Law Act 1975</a>, assets acquired before the relationship, during it, and after separation may all be relevant. Make a list:</p>
 <ul>
   <li>The family home and any investment properties</li>
   <li>Superannuation for both parties (treated as a separate asset class)</li>
   <li>Bank savings and term deposits</li>
   <li>Shares, managed funds, cryptocurrency</li>
   <li>Vehicles, boats, caravans</li>
   <li>Businesses, trust interests, partnership shares</li>
   <li>Inheritances received (timing and use matters)</li>
   <li>All debts: mortgage, car loans, credit cards, personal loans</li>
 </ul>

 <h2>Step 4: Think clearly about the children</h2>
 <p>If you have children, their arrangements are the most important thing to get right — and the most emotionally charged. Before any conversations with your former partner, think through:</p>
 <ul>
   <li>Where the children would live day-to-day and who would do school drop-off and pick-up</li>
   <li>How time would be divided week to week, and over school holidays</li>
   <li>How major decisions — schooling, health, travel — would be made</li>
   <li>What the children's routines, friendships and activities are, and how to protect them</li>
 </ul>
 <p>The <a href="https://www.legislation.gov.au/Details/C2021C00095" target="_blank" rel="noopener">Family Law Act</a> requires that the best interests of the child are the paramount consideration in any parenting arrangement. Keeping that principle front of mind — rather than what feels fair to you as a parent — produces better outcomes and reduces conflict. See our <a href="/parenting-plan-template/">parenting plan template</a> for what a thorough arrangement covers.</p>

 <h2>Step 5: Protect your immediate financial position</h2>
 <p>While you're getting organised:</p>
 <ul>
   <li><strong>Open a personal bank account</strong> in your own name if you don't already have one, and redirect your income to it</li>
   <li><strong>Don't drain joint accounts</strong> — this is treated seriously by courts and will be held against you in a property settlement</li>
   <li><strong>Update your will and superannuation beneficiary nominations</strong> — these don't change automatically on separation</li>
   <li><strong>Notify Centrelink</strong> if you receive family payments — your entitlements change from the date of separation</li>
   <li><strong>Review any joint insurances</strong> — home, contents, health — and consider your coverage going forward</li>
 </ul>

 <h2>Step 6: Understand your legal options early</h2>
 <p>Many people assume separation means lawyers and court. In most cases it doesn't have to. The options, roughly in order of cost and conflict:</p>
 <figure class="tbl"><table>
 <thead><tr><th>Option</th><th>Best for</th><th>Typical cost</th></tr></thead>
 <tbody>
 <tr><td><a href="/family-law-mediation/">Mediation</a></td><td>Most separating couples — property and parenting</td><td>$3,000–$8,000 total shared</td></tr>
 <tr><td>Collaborative law</td><td>Where both parties have lawyers but want to avoid court</td><td>$10,000–$30,000</td></tr>
 <tr><td>Negotiation via lawyers</td><td>Complex matters or where one party won't engage</td><td>$15,000–$60,000+</td></tr>
 <tr><td>Contested court proceedings</td><td>Last resort — when nothing else works</td><td>$30,000–$150,000+ per side</td></tr>
 </tbody></table></figure>
 <p>Mediation resolves over 90% of matters. Most people who try it avoid court entirely. <a href="/family-law-mediation/">Read more about family law mediation →</a></p>

 <h2>A note on safety</h2>
 <p>If your situation involves family violence or you feel unsafe, your safety comes first. Call 000 in an emergency. The <a href="https://1800respect.org.au" target="_blank" rel="noopener">1800RESPECT helpline (1800 737 732)</a> provides confidential support 24 hours a day. Mediation may not be appropriate where there is family violence — tell us about any safety concerns and we will advise the safest options, including arrangements where you and your former partner are never in the same room.</p>

 <div class="callout"><h3>You don't need to have it all sorted before you call us</h3>
 <p>Most people contact us before they've gathered everything. A free initial consultation helps you understand what comes next, what to prioritise, and what mediation can realistically achieve in your situation — no obligation.</p></div>
 """,
 [("What should I do first when separating?",
   "Record your separation date, open a personal bank account, gather your financial documents, and get an early understanding of your options. Acting early and systematically protects your interests and makes the process ahead much smoother."),
  ("What financial documents do I need for separation?",
   "Property valuations and mortgage statements, superannuation statements for both parties, bank statements for all accounts, payslips and tax returns, and details of all debts. Both parties must make full financial disclosure in any property settlement."),
  ("How do I protect my children during separation?",
   "Keep conflict away from them, maintain their routines, and focus on what works for them rather than what feels fair to you. A parenting plan negotiated through mediation gives children stability and keeps arrangements off the court's docket."),
  ("When should I update my will after separation?",
   "Immediately. Your will does not automatically change on separation, and your former partner may remain a beneficiary until it is updated. Also update your superannuation beneficiary nominations, which are separate from your will."),
  ("Do I have to go to court when I separate?",
   "No. Most separating couples resolve property and parenting matters through mediation, then formalise the agreement as consent orders. Court is a last resort, usually only needed when one party refuses to engage or there is a serious safety issue."),
  ("What happens if I miss the time limits for property settlement?",
   "Married couples have 12 months from the date of divorce to apply for property orders; de facto couples have 24 months from separation. After those dates you need the court's permission, which adds cost and uncertainty. Act before the deadline.")],
 "Getting Ready for Separation",
 "Face it prepared, not overwhelmed.",
 "Book a free initial consultation and we'll help you understand exactly what to do next — with no obligation.")

# ---- FAMILY LAW COST ESTIMATOR ----
build("family-law-cost-estimator",
 "Family Law Cost Estimator | Mediation vs Court Costs 2026",
 "How much does a family law matter cost in Australia? Real figures for mediation, lawyers and court — by dispute type. See why mediation saves tens of thousands.",
 "Know the real numbers before you decide",
 "Family Law Cost Estimator",
 "The cost of resolving a family law matter in Australia varies enormously — from a few thousand dollars through mediation to six figures in contested litigation. This guide gives you real cost figures by dispute type, explains what drives costs up, and shows how to estimate your own situation.",
 "Mediation typically costs $3,000–$8,000 total shared between the parties, regardless of complexity. A contested family law matter through court typically costs each party $30,000–$150,000+ in legal fees and takes one to three years. The path you choose — not the complexity of your matter — is the single biggest driver of cost.",
 """
 <h2>The single biggest cost driver: path choice</h2>
 <p>Most people assume family law cost is determined by how complex their matter is. It isn't. The single biggest driver is whether you resolve through mediation or through contested court proceedings. A highly complex property matter resolved through mediation costs a small fraction of a simple matter fought through court.</p>
 <p>The reason: court runs on hourly legal fees, accumulated over months or years. Mediation runs on a fixed session fee, resolved in a day.</p>

 <h2>Cost by dispute type: mediation vs court</h2>
 <figure class="tbl"><table>
 <caption>Approximate costs by dispute type (2026, Australia)</caption>
 <thead><tr><th>Dispute type</th><th>Mediation (total, shared)</th><th>Contested court (per party)</th></tr></thead>
 <tbody>
 <tr><td>Parenting arrangements</td><td>$2,500–$5,000</td><td>$25,000–$80,000</td></tr>
 <tr><td>Property settlement (straightforward)</td><td>$3,000–$6,000</td><td>$30,000–$80,000</td></tr>
 <tr><td>Property settlement (complex — business, trust)</td><td>$5,000–$10,000</td><td>$60,000–$200,000+</td></tr>
 <tr><td>Parenting + property combined</td><td>$4,000–$8,000</td><td>$40,000–$150,000+</td></tr>
 <tr><td>Spousal maintenance</td><td>$2,500–$5,000</td><td>$20,000–$60,000</td></tr>
 <tr><td>Estate dispute</td><td>$3,000–$7,000</td><td>$30,000–$120,000+</td></tr>
 <tr><td>Workplace dispute</td><td>$2,000–$5,000</td><td>$15,000–$80,000</td></tr>
 </tbody></table></figure>
 <p><em>Figures are estimates only. Actual costs depend on the number of sessions required, complexity, and whether legal advice is sought alongside mediation. Court costs include solicitor fees, barrister fees for hearings, and filing costs — and do not include the value of your own time over one to three years.</em></p>

 <h2>What's included in mediation costs</h2>
 <p>At Mediations Australia, mediation fees are fixed and transparent. They cover:</p>
 <ul>
   <li>A free initial consultation</li>
   <li>Mediator preparation and intake</li>
   <li>The mediation session (typically a full day)</li>
   <li>A written record of outcomes or heads of agreement</li>
 </ul>
 <p>Mediation fees are typically shared equally between the parties. See our <a href="/our-fee-structure/">full fee structure →</a></p>

 <h2>What's not included — and what you might also need</h2>
 <p>Mediation reaches agreement. Formalising that agreement is a separate step:</p>
 <figure class="tbl"><table>
 <thead><tr><th>Formalisation step</th><th>Approximate cost</th></tr></thead>
 <tbody>
 <tr><td>Consent orders (property + parenting)</td><td>$1,500–$3,000 combined legal drafting + $175 court fee</td></tr>
 <tr><td>Binding financial agreement (BFA)</td><td>$3,000–$8,000 combined (each party needs own lawyer)</td></tr>
 <tr><td>Section 60I certificate (parenting)</td><td>Included in mediation fee</td></tr>
 </tbody></table></figure>

 <h2>What drives costs up in court</h2>
 <p>Court costs compound over time. The typical escalation path:</p>
 <ol>
   <li><strong>Initial legal advice and letters</strong> — $3,000–$8,000</li>
   <li><strong>Interim hearings</strong> (urgent orders for parenting or property) — $5,000–$20,000 per hearing</li>
   <li><strong>Disclosure and subpoenas</strong> — $5,000–$15,000</li>
   <li><strong>Expert reports</strong> (valuations, family reports) — $3,000–$10,000</li>
   <li><strong>Final hearing preparation</strong> — $15,000–$40,000</li>
   <li><strong>Final hearing</strong> (barrister, solicitor, 2–5 days) — $20,000–$80,000</li>
 </ol>
 <p>These amounts apply to <em>each party</em>. In family law, costs are rarely awarded — meaning each side almost always bears their own legal bill regardless of outcome.</p>

 <h2>The hidden costs of litigation</h2>
 <p>The financial cost is only part of it. Contested court proceedings also cost:</p>
 <ul>
   <li><strong>Time</strong> — one to three years to a final hearing, during which nothing is resolved</li>
   <li><strong>The asset pool itself</strong> — legal fees are paid from the assets being divided. A couple with a $600,000 property can spend $150,000 in combined legal fees fighting over how to split it.</li>
   <li><strong>The co-parenting relationship</strong> — adversarial proceedings make it harder to cooperate on parenting for the years ahead</li>
   <li><strong>Wellbeing</strong> — the stress of protracted litigation has measurable effects on health and work performance</li>
 </ul>

 <h2>Worked example: the same matter, two paths</h2>
 <p>A Sydney couple separating with a $950,000 home, $280,000 combined super, and two children aged 8 and 11:</p>
 <figure class="tbl"><table>
 <thead><tr><th></th><th>Via mediation</th><th>Via contested court</th></tr></thead>
 <tbody>
 <tr><td>Time to resolution</td><td>1 day</td><td>18–30 months</td></tr>
 <tr><td>Mediation / legal fees (combined)</td><td>$7,000</td><td>$120,000–$200,000</td></tr>
 <tr><td>Asset pool preserved</td><td>~$1,223,000</td><td>~$1,023,000–$1,103,000</td></tr>
 <tr><td>Ongoing co-parenting relationship</td><td>Intact</td><td>Damaged</td></tr>
 </tbody></table></figure>

 <div class="callout"><h3>Early resolution saves the most</h3>
 <p>Costs in family law compound with time. The earlier you resolve — ideally through mediation before lawyers are deeply involved — the more of the asset pool stays with your family. <a href="/family-law-mediation/">See what mediation involves →</a></p></div>
 """,
 [("How much does family law mediation cost in Australia?",
   "Mediation typically costs $3,000–$8,000 total, shared between the parties. This covers the mediator's preparation, the session (usually a full day), and a written record of outcomes. Formalising the agreement as consent orders adds approximately $1,500–$3,000 in legal fees."),
  ("How much does a contested family law case cost?",
   "A contested family law matter typically costs each party $30,000–$150,000 in legal fees, depending on complexity and how far it runs. In most cases each side bears their own costs regardless of outcome."),
  ("Why is mediation so much cheaper than court?",
   "Mediation resolves in a single day on a fixed fee. Court runs on hourly legal billing accumulated over one to three years, with multiple hearings, disclosure processes, and expert reports — all of which compound costs significantly."),
  ("Are mediation costs split between the parties?",
   "Usually yes. Mediation fees are typically shared equally, which halves the effective cost for each party. Each party pays their own lawyers if they choose to have legal advice alongside the process."),
  ("What happens to legal costs in court — does the winner get them paid?",
   "Generally no. Family law courts rarely award costs, meaning each party almost always pays their own legal fees regardless of outcome. This is one reason mediation — where costs are low and shared — is the better financial choice for most families."),
  ("How can I get an accurate cost estimate for my situation?",
   "Book a free initial consultation. Costs depend on the specific issues in dispute, the asset pool, and the level of cooperation between parties — a short conversation gives a far more accurate picture than a generic guide.")],
 "Family Law Cost Estimator",
 "See what you could save.",
 "Book a free initial consultation for an honest estimate of what resolving your matter will cost — and how much mediation can save you.")

# ---- SEPARATION UNDER ONE ROOF ----
build("separation-under-one-roof",
 "Separation Under One Roof | How It Works in Australia",
 "Separated but still living together? Learn how separation under one roof works in Australia, what you need to show, and how mediation helps. Free consultation.",
 "Managing together until you can live apart",
 "Separation Under One Roof",
 "Many couples separate while still living in the same home — for financial reasons, for the children, or while they sort out next steps. This guide explains how 'separation under one roof' is recognised in Australia and how to handle it.",
 "Separation under one roof means a couple has separated but continues to live in the same home. It is recognised in Australia, but you may need to show that the relationship has genuinely ended — through changes in finances, sleeping arrangements, and how you present to others.",
 """
 <h2>What is separation under one roof?</h2>
 <p>"Separation under one roof" describes a couple who have decided their relationship is over but continue, at least for a time, to live in the same home. It is common and entirely valid. People stay under one roof for financial reasons — running two households is expensive — for the stability of the children, while a property settlement is sorted out, or simply because finding somewhere else to live takes time.</p>
 <p>What matters legally is not whether you share an address, but whether the relationship has genuinely ended. In Australia you can be separated for every legal purpose — divorce, property settlement, Centrelink — while still sleeping under the same roof, provided you can show the marriage or de facto relationship is over in substance.</p>

 <h2>Is separation under one roof legally recognised in Australia?</h2>
 <p>Yes. Under the <a href="https://www.austlii.edu.au/cgi-bin/viewdb/au/legis/cth/consol_act/fla1975114/" target="_blank" rel="noopener">Family Law Act 1975</a>, separation happens when at least one person forms the intention to end the relationship, communicates that to the other, and acts on it. Nothing in the law requires you to live at different addresses. The courts have long accepted that a couple can be "separated but living under the same roof", and the <a href="https://www.fcfcoa.gov.au/fl/divorce" target="_blank" rel="noopener">Federal Circuit and Family Court of Australia</a> has a specific process for proving it when you apply for a divorce.</p>
 <p>This matters because a divorce in Australia requires you to be separated for at least <strong>12 months and one day</strong> before you can apply. Time spent separated under one roof counts towards that 12 months — you just need to be able to evidence it.</p>

 <h2>How do you show you've genuinely separated?</h2>
 <p>Because you're still living together, you may need to demonstrate that the relationship has actually ended rather than merely become strained. No single factor is decisive; a court or agency looks at the overall picture across several areas of life.</p>
 <figure class="tbl"><table><caption>What changes when a couple separates under one roof</caption>
 <thead><tr><th>Area of life</th><th>What genuine separation can look like</th></tr></thead>
 <tbody>
 <tr><td>Sleeping arrangements</td><td>Separate bedrooms, or one partner moving to another part of the home</td></tr>
 <tr><td>Finances</td><td>Separate bank accounts, divided bills, no longer pooling income</td></tr>
 <tr><td>Household tasks</td><td>Each person cooks, cleans and shops for themselves rather than for the couple</td></tr>
 <tr><td>Social life</td><td>Attending events separately; no longer presenting as a couple</td></tr>
 <tr><td>Others' knowledge</td><td>Family, friends and agencies such as Centrelink have been told you've separated</td></tr>
 </tbody></table></figure>
 <p>You don't need every box ticked. The point is to show a consistent pattern that the relationship has ended, not just a rough patch. Keeping a brief note of when things changed — when you moved to a separate room, when you split the accounts — makes this far easier to evidence later.</p>
 <div class="callout"><h3>The date of separation matters</h3>
 <p>Your date of separation sets the clock running on time limits for both divorce and property. It can also affect Centrelink entitlements and how assets are valued. If you're separated under one roof, pin the date down early so you understand exactly where you stand.</p></div>

 <h2>The affidavit you'll need when you apply for divorce</h2>
 <p>When you have lived under the same roof during the 12-month separation period, the court won't simply take your word for it. You will usually need to file an <strong>affidavit</strong> setting out the changes in your relationship — sleeping arrangements, finances, household duties and social life — together with a <strong>corroborating affidavit from an independent person</strong>, such as a friend or family member, who can confirm they understood you to be separated. The <a href="https://www.fcfcoa.gov.au/fl/divorce" target="_blank" rel="noopener">FCFCOA divorce process</a> sets out exactly what these affidavits should cover.</p>
 <p>It sounds onerous, but in practice it is a short, factual statement. The earlier you have clarity on your separation date and the changes that followed, the simpler this step becomes.</p>

 <h2>How your separation date affects time limits</h2>
 <p>Separation isn't only about divorce. It also starts the clock on the deadlines for finalising a property settlement, and those deadlines differ for married and de facto couples.</p>
 <figure class="tbl"><table><caption>Key time limits that run from your separation or divorce date</caption>
 <thead><tr><th>Step</th><th>Married couples</th><th>De facto couples</th></tr></thead>
 <tbody>
 <tr><td>Apply for divorce</td><td>After 12 months' separation</td><td>Not applicable</td></tr>
 <tr><td>Apply for a property settlement</td><td>Within 12 months of divorce becoming final</td><td>Within 24 months of separation</td></tr>
 <tr><td>Parenting arrangements</td><td>No time limit</td><td>No time limit</td></tr>
 </tbody></table></figure>
 <p>Applying after a deadline isn't impossible, but you need the court's permission, which adds cost and uncertainty. If a deadline is approaching, it is worth formalising arrangements while everyone is still cooperating. <a href="/property-settlement-after-separation/">Read our property settlement guide →</a></p>

 <h2>Centrelink, tax and finances while under one roof</h2>
 <p>Once you separate, you may be assessed as a single person for some payments even if you still share an address. <a href="https://www.servicesaustralia.gov.au/separating" target="_blank" rel="noopener">Services Australia</a> can recognise you as separated under one roof and may ask for a separation form and supporting details. Being upfront and consistent — the same separation date you'd give the court — keeps things clean across the board and avoids problems down the track.</p>

 <h2>Living together while separated: practical tips</h2>
 <p>The arrangement works best when expectations are clear. A few things make a real difference:</p>
 <ul>
   <li><strong>Agree on space and schedules</strong> — who uses common areas when, and how you'll handle meals, laundry and the bathroom.</li>
   <li><strong>Separate your money early</strong> — open individual accounts and divide responsibility for bills so nothing falls through the cracks.</li>
   <li><strong>Keep the children's routine steady</strong> — shield them from conflict and present a united, calm front about the practical changes.</li>
   <li><strong>Document the change</strong> — note your separation date and the adjustments that followed, which helps with both divorce and Centrelink later.</li>
   <li><strong>Plan the exit</strong> — treat the shared-roof period as temporary and agree a rough timeline for one person to move on.</li>
 </ul>

 <h2>How mediation helps when you're still living together</h2>
 <p>Living together while separated can be tense, and small frictions — bills, the school run, who uses the kitchen when — can escalate quickly. <a href="/family-law-mediation/">Mediation</a> provides a structured, neutral way to agree on living arrangements, finances and parenting while you remain under the same roof, and to plan an orderly transition out of it.</p>
 <p>A mediator can help you set practical ground rules for the household, work towards a <a href="/property-settlement-mediation/">property settlement</a> and <a href="/parenting-plan-mediation/">parenting arrangements</a>, and reach agreements you can later formalise as <a href="/consent-orders-explained/">consent orders</a>. If being in the same room is difficult, mediation can be conducted in separate rooms (shuttle mediation) or online. <a href="/getting-ready-for-separation/">See getting ready for separation →</a></p>
 """,
 [("Can you be separated while living together?",
   "Yes. 'Separation under one roof' is recognised in Australia under the Family Law Act 1975. You may need to show the relationship has genuinely ended despite living in the same home."),
  ("How do you prove separation under one roof?",
   "Through factors like separate sleeping arrangements, separated finances, reduced shared activities, and informing family, friends and relevant agencies that you've separated. When applying for divorce you'll usually file an affidavit, plus a corroborating affidavit from an independent person."),
  ("Does time separated under one roof count towards the 12 months for divorce?",
   "Yes. A divorce requires 12 months and one day of separation, and time spent separated under the same roof counts — provided you can evidence that the relationship had genuinely ended."),
  ("Why does the date of separation matter?",
   "It can affect time limits for divorce and property applications, Centrelink entitlements, and how assets are valued. Getting clarity on your separation date early helps you understand your legal position."),
  ("Can you still claim Centrelink as separated if you live together?",
   "You may be assessed as single even while sharing an address. Services Australia can recognise separation under one roof and may ask for a separation form and supporting details."),
  ("Can we mediate while still living together?",
   "Yes. Mediation can help you agree on living arrangements, finances and parenting while under one roof, and can be conducted in separate rooms or online if being together is difficult.")],
 "Separation Under One Roof",
 "Living together, living apart — <em>we can help</em>.",
 "Book a free initial consultation to work out living, financial and parenting arrangements while you're separated under one roof.")

# ---- UNFAIR DISMISSAL: 21-DAY RULE ----
build("unfair-dismissal-21-day-rule",
 "Unfair Dismissal: The 21-Day Rule Explained",
 "Missed the 21-day unfair dismissal deadline and your claim is gone. This guide explains who can claim, what happens after you lodge, and how mediation resolves most cases without a hearing.",
 "Know your deadline — and your options",
 "Unfair Dismissal: <em>The 21-Day Rule Explained</em>",
 "If you have just lost your job and something feels wrong, the 21-day deadline is the single most important fact you need to know. This guide explains who can claim, what happens after lodging, what a realistic outcome looks like, and how most unfair dismissal cases resolve without a hearing.",
 "An unfair dismissal application must be lodged with the Fair Work Commission within 21 calendar days of the dismissal taking effect — not 21 business days. The deadline is unforgiving: extensions are only granted in exceptional circumstances like serious illness or being actively misled. If you have recently lost your job, treat it as urgent.",
 """
 <h2>Why 21 days is the number that matters most</h2>
 <p><strong>An unfair dismissal application must be lodged with the <a href="https://www.fwc.gov.au/" target="_blank" rel="noopener">Fair Work Commission</a> within 21 calendar days after the dismissal takes effect</strong> — not 21 business days. Weekends and public holidays count. The clock starts on your last day of employment, not the day you were told or the day your final pay landed.</p>
 <p>The Commission can extend this deadline only in "exceptional circumstances." Being upset, unsure of your rights, or not getting around to it are not exceptional. Serious illness or being actively misled might be — but you cannot count on it. <strong>Once 21 days pass, the door generally closes.</strong></p>

 <h2>Are you eligible to claim?</h2>
 <p>Not everyone dismissed can bring an unfair dismissal claim. You generally need to pass all of these:</p>
 <ul>
   <li><strong>You were dismissed</strong> — including constructive dismissal, where your employer's conduct left you no real choice but to resign.</li>
   <li><strong>You served the minimum employment period</strong> — 6 months of continuous service, or 12 months for a small business employer (fewer than 15 employees).</li>
   <li><strong>You are award-covered, agreement-covered, or earn under the high-income threshold</strong> — above the threshold without award or agreement coverage, unfair dismissal is not available.</li>
   <li><strong>It was not a genuine redundancy</strong> — a genuine redundancy is a complete defence. See our <a href="/redundancy-was-it-genuine/">redundancy guide</a> for the legal test.</li>
 </ul>
 <p>If you do not qualify for unfair dismissal, a <strong>general protections claim</strong> may be open to you — and that also runs on a 21-day deadline in dismissal cases.</p>

 <h2>What "unfair" actually means</h2>
 <p>The Commission asks whether your dismissal was <strong>"harsh, unjust or unreasonable."</strong> It weighs: was there a valid reason connected to your capacity or conduct? Were you told that reason and given a chance to respond? Were you warned before being dismissed for performance? A dismissal can be substantively justified but still unfair if the process was botched — and equally, a clumsy-feeling dismissal might be lawful if the reason was sound and the process fair.</p>

 <h2>What happens after you lodge</h2>
 <p>The overwhelming majority of unfair dismissal claims never reach a hearing. After lodging (Form F2), the Commission offers <strong>conciliation</strong> — an informal, private, without-prejudice discussion typically held about five weeks after lodging, usually by phone or video, running up to 90 minutes.</p>
 <p>Around <strong>three in four cases settle at or before conciliation.</strong> If not settled, the matter moves to a Commission Member who makes a binding decision — slower, more stressful, and riskier for everyone.</p>

 <h2>What a realistic outcome looks like</h2>
 <p>Because conciliation lets parties agree to almost anything, settlements are flexible. Common elements include: a payment (often measured in weeks of pay, not a windfall); an agreed statement of service or reference; a non-disparagement clause; and a mutual release with confidentiality. Compensation, if a matter runs to a Member's decision, is capped and indexed annually.</p>
 <p>Private mediation with an accredited mediator can run <em>before</em> you lodge — sometimes resolving things without a formal claim — or alongside a lodged claim for a more tailored process. See our <a href="/unfair-dismissal-termination-mediation/">unfair dismissal mediation page</a> for how we approach it.</p>
 """,
 [("Does the 21 days include weekends?",
   "Yes. It is 21 calendar days from when the dismissal takes effect, not 21 business days."),
  ("What if I have already missed the 21-day deadline?",
   "You can apply for an extension, but it is only granted in exceptional circumstances such as serious illness or being actively misled. Get advice immediately."),
  ("What does unfair dismissal actually mean?",
   "The Fair Work Commission asks whether your dismissal was 'harsh, unjust or unreasonable.' This looks at both the reason for dismissal and the fairness of the process — including whether you were warned, consulted, and given a chance to respond."),
  ("Do I need a lawyer at conciliation?",
   "No. Many people are unrepresented, and the process is designed to be accessible. But advice beforehand on what your claim is realistically worth can significantly change the outcome."),
  ("Can private mediation help with an unfair dismissal?",
   "Yes. Private mediation can run before you lodge, to try to resolve directly with your employer, or alongside a lodged claim for a more tailored process than the Commission's 90-minute conciliation call allows.")],
 "Unfair Dismissal: The 21-Day Rule",
 "Act before the clock runs out — <em>we can help</em>.",
 "Book a free consultation to understand your rights and deadlines before the 21-day window closes.")

# ---- IS MEDIATION RIGHT FOR YOUR WORKPLACE DISPUTE? ----
build("is-mediation-right-for-workplace-dispute",
 "Is Mediation Right for Your Workplace Dispute?",
 "Mediation resolves most workplace disputes faster and more privately than a tribunal — but not every situation. This honest guide helps you decide whether mediation fits your dispute.",
 "An honest guide to help you decide",
 "Is Mediation Right for Your Workplace Dispute?",
 "We believe deeply in mediation for workplace disputes — and we are going to be honest about when it is not the right answer, because that honesty is part of taking your situation seriously. This guide helps you make a clear-eyed judgement about your own circumstances.",
 "Mediation works best when both people can come to the table able to speak freely and safely, with a genuine aim of finding a workable outcome. It may not be the right first step where there has been violence, serious harassment, severe power imbalance, or where serious allegations need to be independently established first. An honest first conversation will tell you which path fits.",
 """
 <h2>What mediation actually is — and is not</h2>
 <p>A mediator is a neutral third party who helps people in a dispute have a structured, confidential conversation and reach their own agreement. The mediator does not judge, does not take sides, and cannot impose a decision. <strong>Mediation is not a watered-down court.</strong> Nobody "wins" and nobody is "found" to have done anything. Its power comes entirely from the fact that the parties themselves control the outcome.</p>

 <h2>When mediation works well</h2>
 <p>Mediation tends to be the best available option where several of these are true:</p>
 <ul>
   <li><strong>The relationship needs to continue, or ending it well matters.</strong> Colleagues who will keep working together, or business partners who share an industry. Mediation is built to preserve working relationships; litigation is built to end them.</li>
   <li><strong>Both people can participate freely and safely.</strong> This is the single most important condition.</li>
   <li><strong>The dispute is about interests, not just proving fault.</strong> Pay, conditions, workload, recognition, communication breakdown — these are exactly the problems mediation excels at.</li>
   <li><strong>Speed and privacy matter.</strong> Most workplace mediations resolve in a single session and stay completely confidential.</li>
 </ul>
 <p>This covers many disputes: <a href="/unfair-dismissal-termination-mediation/">unfair dismissal</a>, <a href="/redundancy-restructure-mediation/">redundancy</a>, <a href="/general-protections-discrimination-mediation/">general protections matters</a>, <a href="/partnership-executive-exit-mediation/">partnership exits</a>, and most everyday <a href="/workplace-investigations-grievance-mediation/">grievances</a>.</p>

 <h2>When mediation may not be the right first step</h2>
 <p>Mediation depends on both people being able to negotiate safely. When that condition is absent, mediation can be ineffective at best and harmful at worst. It may not be the right first step where:</p>
 <ul>
   <li><strong>There has been violence, serious sexual harassment, or threats.</strong> Safety comes before process.</li>
   <li><strong>There is a severe power imbalance that cannot be managed.</strong> A skilled mediator manages routine imbalance through shuttle mediation and careful process design — but extreme imbalance may prevent a fair outcome.</li>
   <li><strong>A party fears reprisal or cannot speak honestly.</strong> If fear prevents real negotiation, the conversation is not genuine.</li>
   <li><strong>The behaviour is ongoing and needs to be stopped urgently.</strong> A stop-bullying application or WHS report may need to come first. See our <a href="/workplace-bullying-harassment-mediation/">bullying and harassment guide</a>.</li>
   <li><strong>Serious allegations need to be independently established.</strong> Where serious misconduct needs to be factually determined, a proper investigation usually comes first. See our <a href="/workplace-investigations-grievance-mediation/">investigations guide</a>.</li>
 </ul>
 <p>Importantly, "not the right first step" does not mean "never." Mediation frequently has a role <em>later</em> — after facts are established, safety is assured, or a situation is de-escalated — to repair the workplace and agree a way forward.</p>

 <h2>How a responsible mediator handles the risky cases</h2>
 <p>Before any workplace mediation, there should be a <strong>screening and preparation stage</strong>: the mediator speaks privately with each party, listens for safety concerns and power imbalances, and forms a judgement about whether mediation is appropriate. That might mean a shuttle format, allowing support people, setting clear ground rules, or — where it is the right call — advising that mediation should not proceed yet. Screening is a genuine safeguard, not a formality.</p>
 """,
 [("Can my employer force me to mediate?",
   "No. Mediation is voluntary. You should never be pressured into a process that does not feel safe, and you can raise safety or power-imbalance concerns at any point."),
  ("If mediation is not right now, is it ruled out forever?",
   "No. It often becomes appropriate later — after an investigation, once a situation is de-escalated, or once safety is assured — to repair the workplace."),
  ("Will the mediator decide who is right?",
   "No. A mediator never judges or imposes a decision. If you want a binding ruling on the facts, mediation is not that process."),
  ("Is workplace mediation confidential?",
   "Yes. Mediation is confidential and conducted on a without-prejudice basis, which means what is said generally cannot be used against you later."),
  ("How do I know if mediation fits my specific situation?",
   "The honest test is one question: can both people come to the table able to speak freely and safely, with a genuine aim of finding a workable outcome? If you are unsure, an initial no-obligation conversation will give you a straight assessment.")],
 "Is Mediation Right for Your Workplace Dispute?",
 "Get an honest assessment — <em>not a sales pitch</em>.",
 "Book a free consultation and we will tell you honestly whether mediation fits your situation — including when it does not.")

# ---- REDUNDANCY: WAS IT GENUINE? ----
build("redundancy-was-it-genuine",
 "Redundancy: Was It Genuine? The Legal Test Explained",
 "A genuine redundancy is a complete defence to unfair dismissal. This guide explains the three-part legal test, the consultation mistake that ends most claims, and how to assess your situation.",
 "Know the three-part test before accepting it",
 "Redundancy: <em>Was It Genuine?</em>",
 "Being made redundant is one of the stranger kinds of job loss — supposedly about the role, not the person, yet it can feel intensely personal. This guide explains what 'genuine redundancy' actually means under Australian law, the part employers get wrong most often, and how to assess whether your situation holds up.",
 "Under section 389 of the Fair Work Act, a dismissal is only a genuine redundancy if all three conditions are met: the job is no longer required by anyone; the employer complied with any applicable consultation obligation; and redeployment was not reasonable. Miss any one element and the redundancy may not be genuine — opening the door to an unfair dismissal claim.",
 """
 <h2>Why "genuine" is the whole ballgame</h2>
 <p>A genuine redundancy is a complete <strong>defence</strong> to an unfair dismissal claim. If your redundancy was genuine, you generally cannot bring an unfair dismissal case no matter how upsetting it was. But if your redundancy was <em>not</em> genuine — even where there was a real business reason — that defence falls away.</p>
 <p>The question is not just "did the business have a reason?" It is "did this dismissal meet every element of the legal test?" That gap is where many valid claims live.</p>

 <h2>The three-part test under section 389</h2>
 <p>Under section 389 of the <em>Fair Work Act 2009</em> (Cth), a dismissal is only a genuine redundancy if <strong>all three</strong> of the following are satisfied:</p>
 <ol>
   <li><strong>The job is no longer required by anyone.</strong> The role must have genuinely ceased to be needed because of changes in operational requirements — a downturn, restructure, automation, merger or site closure. If your duties were handed to someone else or a near-identical role was created under a new title, the job arguably still exists.</li>
   <li><strong>The employer complied with any consultation obligation.</strong> This is the most commonly missed element — see below.</li>
   <li><strong>Redeployment was not reasonable.</strong> The employer must show there was no other reasonable role you could have been redeployed into within the business or an associated entity.</li>
 </ol>

 <h2>The part employers most often get wrong: consultation</h2>
 <p>The consultation obligation usually comes not from the <em>Fair Work Act</em> itself, but from the <strong>modern award or enterprise agreement</strong> that covers the employee. Almost every modern award contains a consultation clause triggered by "major workplace change" — and because most employees are covered by an award, the obligation applies far more often than employers assume.</p>
 <p>When it applies, consultation must be <strong>genuine and prior to the decision</strong>. The Fair Work Commission has confirmed repeatedly: <strong>even if consultation would not have changed the outcome, failing to consult means the redundancy is not genuine.</strong> A phone call announcing a decision already made is notification — not consultation.</p>

 <h2>Signs your redundancy may not be genuine</h2>
 <ul>
   <li>Your duties are still being done by other people or under a different job title</li>
   <li>You were told the decision was final before anyone consulted you</li>
   <li>There were other roles you could have filled, and you were not offered them</li>
   <li>You were the only person selected and the basis for choosing you is unclear</li>
   <li>Your award or agreement contains a consultation clause that was not followed</li>
 </ul>
 <p>Remember the <strong>21-day deadline</strong>: if you want to challenge a redundancy as unfair dismissal, lodge with the Fair Work Commission within 21 days of the dismissal taking effect. See our <a href="/unfair-dismissal-21-day-rule/">unfair dismissal 21-day rule guide</a>.</p>

 <h2>How mediation resolves redundancy disputes</h2>
 <p>Redundancy disputes are often as much about process, communication and dignity as they are about money — which makes them well suited to mediation. Rather than fighting over whether the technical test was met in a public hearing, mediation lets both sides craft a practical resolution: an agreed payment, a reference, outplacement support, confidentiality, and a mutual release. See our <a href="/redundancy-restructure-mediation/">redundancy and restructure mediation page</a> for how we approach it.</p>
 """,
 [("Is redundancy pay compulsory?",
   "Minimum redundancy pay and notice are set by the National Employment Standards and any applicable award, based on length of service. Small businesses may be exempt from redundancy pay in some cases."),
  ("Can I be made redundant while on leave?",
   "Being on leave does not protect a genuinely redundant role, but it does not remove the consultation and process obligations either. Selecting someone because they are on certain protected leave can raise general protections issues."),
  ("My employer says it is a genuine redundancy. Can I still challenge it?",
   "Yes. Genuine redundancy is a legal test, not just the employer's label. If the role still exists, consultation was skipped, or redeployment was reasonable and not offered, the redundancy may not be genuine."),
  ("How long do I have to challenge a redundancy?",
   "If challenging as an unfair dismissal, 21 calendar days from the dismissal taking effect. Act quickly."),
  ("Does the size of my employer matter?",
   "Yes. Small businesses (fewer than 15 employees) have a longer minimum employment period and some redundancy-pay exemptions — but they still must consult where an award or agreement requires it.")],
 "Redundancy: Was It Genuine?",
 "Know where you stand — <em>before you accept it</em>.",
 "Book a free consultation to find out whether your redundancy meets the legal test — and what your realistic options are.")

# ---- CONTESTING A WILL: YOUR OPTIONS ----
build("contesting-a-will",
 "Contesting a Will in Australia: Your Options",
 "There are two different ways to challenge a will in Australia, with strict and varying state-by-state deadlines. This guide explains both, the time limits, and why mediation resolves most estate disputes.",
 "Know your options — and your deadlines",
 "Contesting a Will in Australia: <em>Your Options</em>",
 "When someone close to you dies and the will leaves you out — or leaves you far less than you needed — the hurt is real, and it is rarely only about money. This guide explains the two very different ways a will can be challenged, the strict time limits that differ by state, what the process looks like, and why mediation resolves most of these disputes without a court battle.",
 "There are two distinct challenges: a family provision claim (arguing the will fails to make adequate provision for you, not that it is invalid) and a validity challenge (arguing the will should not stand at all — on grounds like lack of testamentary capacity, undue influence, or fraud). Most disputes are family provision claims. Time limits are strict, vary by state, and missing one usually ends your claim permanently.",
 """
 <h2>Two very different challenges</h2>
 <p><strong>A family provision claim</strong> — by far the most common. You are not arguing the will is invalid. You accept it is a real, properly made will — but you say it fails to make adequate provision for you, someone the deceased had a responsibility to provide for. The court can redistribute part of the estate to correct that inadequate provision.</p>
 <p><strong>A challenge to the will's validity</strong> — here you are arguing the will itself should not stand at all. Grounds include: <em>testamentary capacity</em> (the deceased was not of sound mind); <em>undue influence</em> (someone pressured them); <em>fraud or forgery</em>; or improper <em>execution</em>.</p>

 <h2>Time limits: strict and different by state</h2>
 <p>This is the most important practical point. <strong>There is no national deadline. Time limits differ across every state and territory, and missing one usually ends your claim permanently.</strong></p>
 <figure><table>
 <thead><tr><th>State / Territory</th><th>Deadline</th><th>Starts from</th></tr></thead>
 <tbody>
 <tr><td>New South Wales</td><td>12 months</td><td>Date of death</td></tr>
 <tr><td>Victoria</td><td>6 months</td><td>Grant of probate</td></tr>
 <tr><td>Queensland</td><td>6 months (notify); 9 months (file)</td><td>Date of death</td></tr>
 <tr><td>South Australia</td><td>6 months</td><td>Grant of probate</td></tr>
 <tr><td>Western Australia</td><td>6 months</td><td>Grant of probate</td></tr>
 <tr><td>Tasmania</td><td>3 months — the shortest in Australia</td><td>Grant of probate</td></tr>
 <tr><td>ACT / NT</td><td>Approximately 6 months</td><td>Grant of probate / date of death</td></tr>
 </tbody></table></figure>
 <p>Courts have only limited discretion to allow a late claim. If you think you may have a claim, get advice immediately — do not wait until you feel emotionally ready. The clock does not.</p>

 <h2>What the process looks like</h2>
 <p>A family provision claim follows a fairly predictable path, and mediation is built into it. The claim is filed in the relevant Supreme Court; a first directions hearing orders an exchange of financial information; then <strong>mediation is held — in many states, effectively a compulsory step before a final hearing.</strong> If mediation settles the matter, agreed terms go before the court for orders. If not, a judge decides — slower, costlier, and public.</p>

 <h2>Why mediation, not a court battle</h2>
 <p>Estate disputes are uniquely destructive when litigated — the legal costs come out of the very estate everyone is fighting over, and these disputes happen at the rawest possible time, when grief is fresh and old family tensions resurface sharpened by loss.</p>
 <p>Mediation protects the estate (a fraction of the cost of litigation), is private, is faster (most resolve in a single session versus 12-18 months in court), and preserves relationships. In mediation, the family decides. At a hearing, a judge who never knew the deceased decides for everyone. Our <a href="/estate-dispute-mediation/">estate and inheritance dispute mediation page</a> explains how we approach these sensitive matters.</p>
 """,
 [("Can I contest a will if I was left something, just not enough?",
   "Yes. A family provision claim is about whether provision was adequate for your proper maintenance and support — you can be a beneficiary and still claim."),
  ("Does estrangement stop me claiming?",
   "No, though it is a factor the court weighs. Courts have made provision for estranged adult children in genuine financial need."),
  ("What if the estate has already been distributed?",
   "This makes a claim much harder, and in some states impossible — which is another reason to act before the deadline."),
  ("Do I need a lawyer to contest a will?",
   "Family provision claims are legally technical and most participants are represented. But the resolution itself — mediation — is where matters are usually settled, and that is a process built around agreement, not argument."),
  ("Is mediation mandatory in estate disputes?",
   "In many states, attempting mediation is effectively a compulsory component of a family provision claim before it can go to a final hearing.")],
 "Contesting a Will",
 "Talk to us before the deadline passes — <em>time matters here</em>.",
 "Book a free consultation before the deadline in your state — missing it usually ends your options permanently.")

# ---- COMMERCIAL DISPUTE GUIDE ----
build("commercial-dispute-guide",
 "Commercial Dispute Guide: Resolve Without Court",
 "Business disputes resolved by mediation are faster, cheaper, and more private than litigation. This guide covers the main types of commercial dispute and why litigation is usually the wrong first move.",
 "Resolve business conflict without litigation",
 "Commercial Dispute Guide: <em>Resolve Business Conflict Without Court</em>",
 "Every business dispute arrives at the worst possible time. Left to escalate, any of them can swallow months of management time, tens of thousands in legal fees, and a good deal of the goodwill your business runs on. This guide explains the main types of commercial dispute, why litigation is so often the wrong first move, and how mediation resolves these matters faster, more cheaply, and more privately.",
 "Commercial disputes — contract fights, partnership breakdowns, lease disputes, franchise conflicts — are resolved far faster and more cheaply through mediation than litigation. Most commercial mediations resolve in a single session. Litigation routinely takes one to three years, costs substantial money on both sides, and exposes sensitive commercial information to the public record. Many commercial contracts already require mediation before you can litigate.",
 """
 <h2>The common types of commercial dispute</h2>
 <ul>
   <li><strong>Contract disputes.</strong> Non-payment, defective or late supply, disagreement over what the contract requires, or one party walking away. Most begin as a difference of interpretation that hardens into a standoff.</li>
   <li><strong>Partnership and shareholder disputes.</strong> Often the most damaging, because they are personal as well as commercial — deadlock over strategy, disagreements about drawings, or a fundamental falling-out. Where a partner or director is leaving, see our <a href="/partnership-executive-exit-mediation/">partnership and executive exit guidance</a>.</li>
   <li><strong>Commercial and retail lease disputes.</strong> Rent reviews, outgoings, make-good obligations, renewal and assignment. These have their own special rules — see below.</li>
   <li><strong>Franchise, supply, and distribution disputes.</strong> Disagreements between franchisors and franchisees, or along a supply chain, often governed by the Franchising Code of Conduct.</li>
   <li><strong>Business sale and purchase disputes.</strong> Earn-outs, warranties, and disagreements about what was promised during a sale.</li>
 </ul>

 <h2>Why litigation is usually the wrong first move</h2>
 <ul>
   <li><strong>It destroys value.</strong> Public conflict unsettles customers, staff, suppliers and lenders.</li>
   <li><strong>It is slow.</strong> Commercial litigation routinely takes one to three years to reach a final hearing.</li>
   <li><strong>It is expensive.</strong> Legal costs on both sides can run into serious money, and even the "winner" may be out of pocket.</li>
   <li><strong>It is public.</strong> Sensitive commercial information — your margins, contracts, internal emails — can end up on the public record.</li>
   <li><strong>It burns relationships.</strong> You often still have to deal with the other side, or share an industry with them.</li>
 </ul>

 <h2>A special case: retail and commercial leases</h2>
 <p>Retail lease disputes deserve their own mention because in most of Australia, <strong>mediation is a mandatory step before a tribunal will hear the matter.</strong> In NSW, disputes must go to the <a href="https://www.smallbusiness.nsw.gov.au/" target="_blank" rel="noopener">NSW Small Business Commissioner</a> before NCAT. Victoria uses the Victorian Small Business Commission before VCAT. Queensland, South Australia, Western Australia, the ACT and NT operate similar pathways.</p>
 <p>Many commercial contracts also contain <strong>dispute-resolution clauses</strong> requiring mediation before litigating. If your contract has one, mediation is not just sensible — it may be a contractual precondition to going to court at all. Check your agreement early.</p>

 <h2>What a commercial mediation looks like</h2>
 <p>A typical commercial mediation is a structured, confidential session run by a neutral mediator who understands both the legal framework and commercial realities. Many of our mediators are also experienced lawyers, which matters in complex matters. The mediator meets each side privately and together, helps identify real interests beneath stated positions, and guides the conversation toward a deal. Once agreement is reached, it is captured in a binding deed of settlement — enforceable and final.</p>
 """,
 [("Is mediation binding in a commercial dispute?",
   "The mediation process is voluntary, but once you sign a settlement agreement or deed, that becomes an enforceable contract. You are not bound until you agree."),
  ("What if the other side refuses to mediate?",
   "Many contracts require mediation, and for retail leases it is generally mandatory. A refusal to mediate can also be viewed poorly by a court later."),
  ("Can mediation handle a dispute that is both commercial and personal, like a partnership breakup?",
   "Yes. A single settlement can resolve the money, the ownership, the restraints, and how the split is communicated, all at once."),
  ("How long does commercial mediation take?",
   "Most commercial mediations resolve in a single session. Compare that with one to three years for litigation."),
  ("Is commercial mediation confidential?",
   "Yes. Mediation is private and without prejudice — a major advantage over public court proceedings.")],
 "Commercial Dispute Guide",
 "Resolve it faster — <em>and keep it private</em>.",
 "Before committing your business to a slow, costly and public legal fight, talk to us about resolving it faster, more privately, and with a commercial outcome that actually works.")

# ---- REAL ESTATE & CONSTRUCTION DISPUTES ----
build("real-estate-construction-disputes",
 "Real Estate &amp; Construction Disputes: Resolve Without Tribunal",
 "Property disputes escalate fast. This guide covers building defects, boundary fights, co-ownership deadlocks, and why mediation resolves most in a single session instead of months at tribunal.",
 "Resolve property disputes without the tribunal fight",
 "Real Estate &amp; Construction Disputes: <em>Resolving Them Without a Tribunal</em>",
 "Property disputes have a particular way of escalating. What starts as a crack in a new wall, a fence in the wrong spot, or a disagreement over a final invoice can quickly become a matter of principle — and then a matter for lawyers. This guide explains the common types of property dispute, the formal pathways that apply, and why mediation is so often the faster, cheaper and less bruising way to resolve them.",
 "Property disputes — building defects, boundary fights, co-ownership deadlocks, strata conflicts — are well suited to mediation because the outcomes people actually want are practical, not just financial. A works schedule, a cost-sharing arrangement, a buy-out. These are things mediation can deliver that a tribunal generally cannot. Most property mediations resolve in a single session.",
 """
 <h2>The common types of property dispute</h2>
 <ul>
   <li><strong>Building and construction disputes.</strong> Between homeowners and builders, builders and subcontractors, developers and contractors. Flashpoints: defective work, delays, cost overruns, disputed variations. These often turn on technical questions that make litigating them extremely costly.</li>
   <li><strong>Boundary and fencing disputes.</strong> Encroachments, dividing-fence cost-sharing, and access disputes between neighbours. Frequently more about relationship and principle than money — which is exactly why a purely legal approach so often fails to actually resolve them.</li>
   <li><strong>Co-ownership disputes.</strong> Siblings who inherited a house, friends who invested together, or a couple who have separated and cannot agree on whether to sell, how to manage the property, or how to divide the proceeds.</li>
   <li><strong>Strata and owners-corporation disputes.</strong> Conflicts between lot owners or between owners and the body corporate. See our <a href="/strata-neighbour-dispute-mediation/">strata and neighbour dispute guidance</a> for detail.</li>
   <li><strong>Off-the-plan and sale disputes.</strong> Disagreements over whether the finished product matches what was promised, delayed settlements, and disputes about deposits.</li>
 </ul>

 <h2>Why property disputes are so well suited to mediation</h2>
 <ul>
   <li><strong>The outcomes people want are practical, not just financial.</strong> What an owner usually wants is the defect fixed, or the fence agreed, or the property sold on sensible terms. Mediation can deliver a works schedule, a cost-sharing arrangement, or a buy-out. A court generally cannot.</li>
   <li><strong>The relationship often continues.</strong> Neighbours remain neighbours. Co-owners may still be family. A negotiated agreement can repair what a judgment never can.</li>
   <li><strong>Speed matters.</strong> Building defects deteriorate while parties argue. A tribunal matter can take many months just to reach a first hearing. Mediation can be arranged and resolved far faster.</li>
 </ul>

 <h2>The formal pathways — and where mediation fits</h2>
 <p>State civil and administrative tribunals — NCAT in NSW, VCAT in Victoria, QCAT in Queensland — handle a large share of building, strata and tenancy disputes, and frequently encourage or require mediation before a final hearing. Building contracts themselves very often contain dispute-resolution clauses requiring mediation or expert determination before litigating.</p>
 <p>Private mediation can run before you engage any of these processes, alongside them, or as the resolution step within them. The advantage of engaging early is that you may resolve the matter before it hardens into a formal proceeding, saving the cost and delay entirely.</p>

 <h2>What a property mediation looks like</h2>
 <p>For a construction dispute, mediation often means working through disputed items methodically — which are agreed, which are contested, and what a realistic resolution looks like. Where technical questions are central, the parties can agree to rely on a single jointly-instructed expert rather than competing ones, which alone can save enormous cost. Once agreement is reached, it is recorded in a binding written settlement so the outcome is enforceable.</p>
 """,
 [("My builder and I are at war over defects. Is it too late to mediate?",
   "Almost never. Even matters already in a tribunal are frequently resolved at mediation. The sooner you mediate, the more cost you save."),
  ("Can mediation force the other side to fix defective work?",
   "Mediation cannot force anything — but a mediated settlement can include a binding, agreed schedule of rectification works with timeframes. That is often exactly what an owner wants, and what a damages award does not deliver."),
  ("We are co-owners who cannot agree whether to sell. Can mediation help?",
   "Yes. Co-ownership deadlocks are well suited to mediation, which can produce a buy-out, an agreed sale process, or a management arrangement — without the cost and finality of a court-ordered sale."),
  ("Is a retail lease dispute different?",
   "Yes. In most states you must attempt mediation through the Small Business Commissioner before going to a tribunal."),
  ("How long does property mediation take?",
   "Most property mediations resolve in a single session, compared with many months for a tribunal or court outcome.")],
 "Real Estate &amp; Construction Disputes",
 "Resolve your property dispute — <em>before it spirals</em>.",
 "Book a free consultation before a property disagreement becomes an expensive, drawn-out tribunal fight.")

# ---- WORKPLACE DISPUTE GUIDE ----
build("workplace-dispute-guide",
 "Workplace Dispute Guide: Your Rights, the FWC &amp; Mediation",
 "A plain-English map of your options in an Australian workplace dispute — FWC, unfair dismissal, general protections, bullying, redundancy, and how mediation resolves most without a hearing.",
 "Your rights, your options, plain English",
 "Workplace Dispute Guide: <em>Your Rights, the FWC &amp; Mediation</em>",
 "Trouble at work has a way of taking over your whole life. Whether you have been dismissed, bullied, made redundant, or are an employer facing a claim, the path forward is rarely obvious. This guide cuts through the acronyms to explain your main options, how the Fair Work system fits together, where the critical deadlines are, and how mediation resolves the large majority of these disputes without a hearing.",
 "Australian workplace disputes divide into several distinct legal shapes — unfair dismissal, redundancy, general protections, bullying, partnership exits, and internal grievances — each with different tests and deadlines. The Fair Work Commission is built to encourage resolution before a hearing; the large majority of matters settle at conciliation. Private mediation works alongside the FWC or in situations the Commission does not cover, and resolves most disputes in a single session.",
 """
 <h2>First: the deadlines, because some are brutally short</h2>
 <p>The most important: if you have been dismissed and want to challenge it as unfair dismissal or a general protections claim, you have just <strong>21 calendar days</strong> from when the dismissal takes effect to lodge with the Fair Work Commission. That is three weeks, weekends included. Extensions are only granted in exceptional circumstances. Treat any recent dismissal as urgent.</p>

 <h2>Your main options, plain English</h2>
 <ul>
   <li><a href="/unfair-dismissal-termination-mediation/"><strong>Unfair dismissal.</strong></a> Was your dismissal "harsh, unjust or unreasonable"? Tight 21-day deadline; eligibility rules apply.</li>
   <li><a href="/redundancy-restructure-mediation/"><strong>Redundancy disputes.</strong></a> Was your redundancy genuine? If the role still exists, consultation was skipped, or redeployment was not offered, it may not be — opening an unfair dismissal claim.</li>
   <li><a href="/general-protections-discrimination-mediation/"><strong>General protections and discrimination.</strong></a> Did you suffer adverse action because you exercised a workplace right or have a protected attribute like age, sex, race, disability, or pregnancy?</li>
   <li><a href="/workplace-bullying-harassment-mediation/"><strong>Bullying and harassment.</strong></a> Repeated unreasonable behaviour creating a risk to health and safety. Specific avenues apply, including applying to the FWC for a stop-bullying order.</li>
   <li><a href="/partnership-executive-exit-mediation/"><strong>Partnership and executive exits.</strong></a> High-stakes separations blending employment, commercial and corporate issues.</li>
   <li><a href="/workplace-investigations-grievance-mediation/"><strong>Workplace investigations and grievances.</strong></a> Knowing when a complaint needs formal investigation, when it is better mediated, and how to handle a grievance without inflaming it.</li>
 </ul>

 <h2>How the Fair Work system actually works</h2>
 <p>The <a href="https://www.fwc.gov.au/" target="_blank" rel="noopener">Fair Work Commission</a> is Australia's national workplace tribunal. Its basic instinct is to encourage resolution, not to run trials. For most claim types, the Commission's first move is to offer <strong>conciliation</strong> — an informal, confidential, without-prejudice discussion designed to help both sides reach their own agreement. The large majority of matters settle at this stage.</p>
 <p>Alongside the Commission: the <a href="https://www.fairwork.gov.au/" target="_blank" rel="noopener">Fair Work Ombudsman</a> handles workplace rights and pay compliance; <a href="https://www.safeworkaustralia.gov.au/" target="_blank" rel="noopener">Safe Work Australia</a> sets the national work health and safety framework, including psychosocial hazards like bullying and role conflict that employers now have a positive duty to manage.</p>

 <h2>Where private mediation fits alongside all of this</h2>
 <p>Private mediation is not an alternative that competes with the Fair Work system — it works with it. Mediation can be used before you lodge (to resolve directly and sometimes avoid a formal claim altogether), alongside a lodged claim (more time and a tailored process), or in situations the Commission does not cover such as partnership disputes or internal grievances.</p>
 <p>The advantages are consistent: faster (usually a single session), private (no public record), cheaper than a contested hearing, and the outcome stays in your hands.</p>

 <h2>Preventing disputes before they start</h2>
 <p>A great deal of workplace conflict traces back to team dynamics that were never properly understood: unclear roles, overlapping responsibilities, and behaviour that gets read as personal when it is really structural. <a href="/belbin-team-roles-training/">Belbin Team Roles training</a> helps organisations build balanced teams and give people a shared, non-personal language for difference — heading off conflict before it ever becomes a grievance or a claim.</p>
 """,
 [("I have been dismissed. What is the first thing I should do?",
   "Check the date your dismissal took effect and count forward 21 days — that is likely your deadline to lodge with the Fair Work Commission. Get advice quickly, well before that date."),
  ("Do I need a lawyer for a workplace dispute?",
   "Not necessarily. Many matters are resolved without one, and Fair Work processes are designed to be accessible. But early advice — even a single consultation — often changes the outcome, especially on which claim applies and what it is worth."),
  ("Is mediation compulsory for workplace disputes?",
   "There is no across-the-board requirement to mediate (unlike family law parenting matters). But the Commission strongly encourages conciliation, many contracts require mediation, and courts expect genuine attempts at resolution."),
  ("Can an employer use mediation too?",
   "Absolutely. Employers facing a claim, or wanting to handle a grievance or restructure correctly, benefit just as much from early advice and mediation as employees do."),
  ("How much does workplace mediation cost?",
   "We use transparent, fixed-fee pricing. Mediation is a fraction of the cost of a contested hearing. See our fee structure page for detail.")],
 "Workplace Dispute Guide",
 "Not sure which option fits? <em>Start here.</em>",
 "Book a free consultation to find out which option fits your situation, what the deadlines are, and whether mediation is the right step.")

print("Resource pages built.")
