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

print("Resource pages built.")
