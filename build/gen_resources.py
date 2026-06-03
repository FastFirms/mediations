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
<div class="phero-cta"><a href="{BOOK_URL}" class="btn btn-primary">Book a free consultation <span class="arr">→</span></a>
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
 "Parenting Plan Template Australia | What to Include (Free Guide)",
 "A free guide to what belongs in a parenting plan in Australia — living arrangements, time, decisions and more. Build a workable plan with accredited mediators. Free consultation.",
 "Resource",
 "Parenting Plan Template — <em>what to include</em>, explained.",
 "A good parenting plan covers far more than just who the children live with. This guide walks through everything a thorough parenting plan should address — so you can build arrangements that actually work, and avoid the gaps that cause disputes later.",
 "A parenting plan should cover living arrangements, how time is shared, communication between parents, how major decisions are made, holidays and special occasions, and how future disagreements will be resolved. A mediator can help you turn this into a complete, workable plan.",
 """
 <h2>What should a parenting plan include?</h2>
 <p>A thorough parenting plan addresses the practical realities of raising children across two households. At a minimum, consider covering:</p>
 <ul>
   <li><strong>Living arrangements</strong> — where the children live and the day-to-day routine.</li>
   <li><strong>Time with each parent</strong> — weekdays, weekends, and how transitions happen.</li>
   <li><strong>Holidays and special days</strong> — school holidays, birthdays, Christmas and other significant occasions.</li>
   <li><strong>Decision-making</strong> — how major long-term decisions about schooling, health and religion are made.</li>
   <li><strong>Communication</strong> — how parents will communicate with each other and with the children.</li>
   <li><strong>Travel</strong> — arrangements for holidays away, including interstate or overseas.</li>
   <li><strong>Changing the plan</strong> — how you'll handle adjustments as children grow and circumstances change.</li>
   <li><strong>Resolving disputes</strong> — agreeing to return to mediation before court if disagreements arise.</li>
 </ul>
 <div class="callout"><h3>A template is a starting point — not a substitute for thought</h3>
 <p>Templates help you remember what to cover, but the value is in the conversation. A mediator helps you work through each element so your plan reflects your children's real needs. <a href="/parenting-plan-mediation/">See parenting plan mediation →</a></p></div>
 <h2>Is a parenting plan legally binding?</h2>
 <p>A parenting plan is not directly enforceable, but a court will consider it in any later dispute. To make arrangements legally binding, they can be formalised as <a href="/consent-orders/">consent orders</a>. Many families start with a plan and convert it once arrangements have settled.</p>
 <h2>How a mediator helps</h2>
 <p>Working through a parenting plan with an accredited mediator ensures nothing important is missed and that both parents genuinely agree — which is what makes a plan last. It keeps the focus on the children rather than on conflict.</p>
 """,
 [("What should be included in a parenting plan?",
   "Living arrangements, time with each parent, holidays and special occasions, how major decisions are made, communication, travel, and how to handle future changes and disputes."),
  ("Is a parenting plan legally binding in Australia?",
   "Not directly, but a court will consider it in any later dispute. To make it binding, arrangements can be formalised as consent orders."),
  ("Do I need a lawyer to make a parenting plan?",
   "No. A parenting plan can be made by agreement, and a mediator can help you cover everything thoroughly. Legal advice is useful if you later formalise it as consent orders."),
  ("Can a parenting plan be changed later?",
   "Yes. Parenting plans are flexible and can be updated by agreement as children grow and circumstances change — ideally through mediation if you can't agree directly.")],
 "Parenting Plan Template",
 "Build a parenting plan that <em>actually works</em>.",
 "Book a fixed-fee consultation and let an accredited mediator help you create a complete, child-focused parenting plan.")

# ---- BFA OR CONSENT ORDERS ----
build("bfa-or-consent-orders",
 "BFA or Consent Orders? | Which Is Right for You (2026 Guide)",
 "Binding financial agreement or consent orders? Compare the two ways to formalise a property settlement in Australia — cost, finality and flexibility. Free consultation.",
 "Resource",
 "BFA or Consent Orders — <em>which is right for you</em>?",
 "Once you've agreed how to divide property, you need to make it legally binding — and there are two main routes: consent orders or a binding financial agreement. This guide explains the difference, so you can choose the one that fits your situation.",
 "Consent orders are approved by a court and are generally simpler and cheaper, while a binding financial agreement (BFA) is a private contract that offers more flexibility but requires each party to get independent legal advice. Which is right depends on your circumstances.",
 """
 <h2>What's the difference between a BFA and consent orders?</h2>
 <p>Both make a property settlement legally binding, but they work differently:</p>
 <ul>
   <li><strong><a href="/consent-orders/">Consent orders</a></strong> are an agreement approved by the Federal Circuit and Family Court. A registrar checks the division is just and equitable, then makes binding orders — without a hearing. They're generally simpler and lower-cost. See our <a href="/consent-orders-explained/">full guide to consent orders</a>.</li>
   <li><strong><a href="/financial-agreements-mediation/">Binding financial agreements (BFAs)</a></strong> are private contracts between the parties. They offer more flexibility and privacy and can be made before, during or after a relationship — but each party must receive independent legal advice for the agreement to be binding.</li>
 </ul>
 <h2>Which should you choose?</h2>
 <p>Consent orders suit most separating couples finalising a property split, especially where the division is straightforward and you want the certainty of court approval. A BFA can be preferable where you want maximum flexibility, privacy, or an agreement made before or during a relationship (a "prenup"). Both are far better than leaving things informal.</p>
 <div class="callout"><h3>The hard part is the agreement itself</h3>
 <p>Whichever instrument you choose, the real work is reaching a fair agreement — which is exactly what mediation does efficiently. We then help you formalise it the right way. <a href="/property-settlement-mediation/">See property settlement mediation →</a></p></div>
 <h2>Comparing the two at a glance</h2>
 <ul>
   <li><strong>Cost:</strong> Consent orders are usually cheaper; BFAs require independent legal advice for each party.</li>
   <li><strong>Court involvement:</strong> Consent orders are court-approved; BFAs are private.</li>
   <li><strong>Timing:</strong> BFAs can be made before, during or after a relationship; consent orders are made on or after separation.</li>
   <li><strong>Finality:</strong> Both are binding, though the grounds to challenge each differ.</li>
 </ul>
 """,
 [("Is a BFA or consent orders cheaper?",
   "Consent orders are generally cheaper, as a BFA requires each party to obtain independent legal advice. But the right choice depends on your circumstances, not just cost."),
  ("Can a BFA be made before marriage?",
   "Yes. A binding financial agreement can be made before, during or after a marriage or de facto relationship. One made beforehand is often called a prenup."),
  ("Are consent orders harder to overturn than a BFA?",
   "Both are binding, but the grounds for setting them aside differ. Consent orders are court-approved; BFAs can be challenged on contract-related grounds such as non-disclosure. Independent advice protects a BFA."),
  ("Do I need to go to court for either?",
   "No. Consent orders are reviewed on the papers without a hearing, and a BFA is a private contract. Neither requires you to attend court.")],
 "BFA or Consent Orders",
 "Choose the <em>right</em> way to make it binding.",
 "Book a consultation and we'll help you reach agreement and formalise it through whichever instrument fits your situation best.")

# ---- GETTING READY FOR SEPARATION ----
build("getting-ready-for-separation",
 "Getting Ready for Separation | A Practical Checklist (Australia)",
 "A practical guide to preparing for separation in Australia — finances, children, documents and your wellbeing. Steps to take before you separate. Free consultation.",
 "Resource",
 "Getting Ready for Separation — a <em>practical guide</em>.",
 "Separation is overwhelming, but preparation makes it manageable. This practical guide covers the key things to think about before and during separation — from gathering financial documents to protecting your children's wellbeing — so you can move forward with clarity.",
 "To get ready for separation, gather your financial documents, understand your assets and debts, think about parenting arrangements, prioritise your wellbeing and your children's, and get clear on your goals. Early preparation makes mediation and the decisions ahead far smoother.",
 """
 <h2>Practical steps to take</h2>
 <ol>
   <li><strong>Gather your financial information.</strong> Collect records of income, assets, debts, superannuation and joint accounts. A clear financial picture is essential for any property settlement.</li>
   <li><strong>Understand the full asset pool.</strong> List what you own and owe, together and separately — property, savings, super, vehicles, businesses and liabilities.</li>
   <li><strong>Think about the children.</strong> Consider what living and time arrangements would genuinely work for them. Their stability matters most.</li>
   <li><strong>Protect your wellbeing.</strong> Separation is emotionally demanding. Lean on support — friends, family, or <a href="/divorce-counselling/">counselling</a>.</li>
   <li><strong>Get clear on your goals.</strong> Separate what you truly need from what you'd prefer. This clarity is invaluable in mediation.</li>
   <li><strong>Seek early guidance.</strong> Understanding your options early — including mediation — helps you avoid costly missteps.</li>
 </ol>
 <div class="callout"><h3>You don't have to have it all figured out</h3>
 <p>Many people come to us before they've sorted any of this. A fixed-fee consultation is a good first step — we'll help you understand what to do next, with no obligation.</p></div>
 <h2>A note on safety</h2>
 <p>If your situation involves family violence or you feel unsafe, your safety comes first. Contact emergency services if you're in immediate danger, and tell us about any concerns so we can advise the safest path — including arrangements that mean you never have to be in the same room as the other person.</p>
 <h2>How mediation fits in</h2>
 <p>Once you're prepared, <a href="/family-law-mediation/">mediation</a> is usually the fastest, least stressful way to resolve the practical questions — parenting, property and finances — without court. <a href="/preparing-for-mediation/">See how to prepare for mediation →</a></p>
 """,
 [("What should I do before separating?",
   "Gather financial documents, understand your assets and debts, think about parenting arrangements, prioritise wellbeing, and get clear on your goals. Early guidance on your options helps too."),
  ("What financial documents do I need?",
   "Records of income, assets, debts, superannuation, bank accounts and any business interests — anything that helps build a complete picture of the asset pool for a property settlement."),
  ("How do I protect my children during separation?",
   "Focus on stability and keeping conflict away from them. Child-focused parenting arrangements and, where helpful, counselling support children through the transition."),
  ("When should I get advice?",
   "As early as possible. Understanding your options early — including mediation — helps you avoid costly missteps and reduces stress.")],
 "Getting Ready for Separation",
 "Face it <em>prepared</em>, not overwhelmed.",
 "Book a fixed-fee consultation and we'll help you understand exactly what to do next — with no obligation.")

# ---- FAMILY LAW COST ESTIMATOR (content page for now) ----
build("family-law-cost-estimator",
 "Family Law Cost Estimator | Mediation vs Court Costs (Australia)",
 "Understand and estimate the cost of resolving a family law matter — mediation versus court. See why mediation costs a fraction of litigation. Free consultation.",
 "Resource",
 "Family Law Cost Estimator — <em>mediation vs court</em>.",
 "Worried about what resolving your family law matter will cost? This guide explains the real cost difference between mediation and court — so you can estimate your situation and understand why mediation typically saves tens of thousands of dollars.",
 "Mediation typically costs from a few hundred to a few thousand dollars, usually shared between parties, while a contested family law court case can cost tens of thousands per side and take one to three years. The exact cost depends on complexity, but mediation is almost always far cheaper.",
 """
 <h2>What drives the cost of a family law matter?</h2>
 <ul>
   <li><strong>The path you choose</strong> — mediation versus litigation is the single biggest factor.</li>
   <li><strong>Complexity</strong> — the size of the asset pool, business interests and the number of issues in dispute.</li>
   <li><strong>The level of conflict</strong> — the more entrenched the dispute, the longer (and costlier) it takes.</li>
   <li><strong>How quickly you resolve it</strong> — early resolution saves the most.</li>
 </ul>
 <h2>Mediation vs court: the cost difference</h2>
 <p>A contested family law case can cost tens or even hundreds of thousands of dollars per side once two sets of lawyers bill by the hour over one to three years. Mediation, by contrast, typically resolves in one or two sessions, with a fixed fee usually shared between the parties — frequently the difference between a few thousand dollars total and a six-figure litigation bill. The money you save is money that stays with your family. <a href="/our-fee-structure/">See our transparent fee structure →</a></p>
 <div class="callout"><h3>Get a real estimate for your situation</h3>
 <p>Every matter is different. The most accurate way to understand your likely cost is a fixed-fee consultation, where we assess your circumstances and explain the options clearly — with no obligation. An interactive estimator is coming soon; for now, a quick call gives you a far more accurate picture.</p></div>
 <h2>Why early resolution saves the most</h2>
 <p>Costs in family law compound over time — the longer a dispute runs, the more it costs emotionally and financially. Resolving early through <a href="/family-law-mediation/">mediation</a> is the most reliable way to keep costs down and protect the asset pool you're dividing.</p>
 """,
 [("How much does a family law matter cost?",
   "It varies with complexity, but mediation typically costs from a few hundred to a few thousand dollars shared between parties, while contested court cases can cost tens of thousands per side."),
  ("Why is mediation cheaper than court?",
   "Mediation resolves matters in one or two sessions rather than one to three years of hourly legal fees, so it avoids the compounding cost of litigation."),
  ("Is the cost shared between parties?",
   "Mediation fees are usually shared, making the process more affordable for everyone. Litigation, by contrast, means each side carries its own substantial legal bill."),
  ("How can I get an accurate cost estimate?",
   "Book a fixed-fee consultation. Because every matter differs, a short conversation gives a far more accurate estimate than any generic calculator.")],
 "Family Law Cost Estimator",
 "See what you could <em>save</em>.",
 "Book a fixed-fee consultation for an honest estimate of what resolving your matter will cost — and how much mediation can save you.")

# ---- SEPARATION UNDER ONE ROOF ----
build("separation-under-one-roof",
 "Separation Under One Roof | How It Works in Australia",
 "Separated but still living together? Learn how separation under one roof works in Australia, what you need to show, and how mediation helps. Free consultation.",
 "Resource",
 "Separation Under One Roof — <em>how it works</em>.",
 "Many couples separate while still living in the same home — for financial reasons, for the children, or while they sort out next steps. This guide explains how 'separation under one roof' is recognised in Australia and how to handle it.",
 "Separation under one roof means a couple has separated but continues to live in the same home. It is recognised in Australia, but you may need to show that the relationship has genuinely ended — through changes in finances, sleeping arrangements, and how you present to others.",
 """
 <h2>What is separation under one roof?</h2>
 <p>It's when a couple decides their relationship is over but continues, at least for a time, to live in the same house. This is common and entirely valid — people stay under one roof for financial reasons, for stability for the children, or simply while they work out what comes next.</p>
 <h2>How do you show you've genuinely separated?</h2>
 <p>Because you're still living together, you may need to demonstrate the relationship has actually ended. Factors that help show genuine separation include:</p>
 <ul>
   <li>Separate sleeping arrangements</li>
   <li>Changes to how finances are handled — separate accounts, divided expenses</li>
   <li>A reduction in shared activities and domestic tasks done for each other</li>
   <li>Telling family and friends, and relevant government agencies, that you've separated</li>
   <li>Each person living a more independent life within the home</li>
 </ul>
 <div class="callout"><h3>The date of separation matters</h3>
 <p>Your date of separation can affect time limits for property and divorce applications. If you're separated under one roof, it's worth getting clarity early so you understand your position.</p></div>
 <h2>How mediation helps when you're still living together</h2>
 <p>Living together while separated can be tense. <a href="/family-law-mediation/">Mediation</a> provides a structured, neutral way to agree on living arrangements, finances and parenting while you remain under the same roof — and to plan the transition out of it. If being in the same room is difficult, mediation can be conducted in separate rooms or online. <a href="/getting-ready-for-separation/">See getting ready for separation →</a></p>
 """,
 [("Can you be separated while living together?",
   "Yes. 'Separation under one roof' is recognised in Australia. You may need to show the relationship has genuinely ended despite living in the same home."),
  ("How do you prove separation under one roof?",
   "Through factors like separate sleeping arrangements, separated finances, reduced shared activities, and informing family, friends and relevant agencies that you've separated."),
  ("Why does the date of separation matter?",
   "It can affect time limits for divorce and property applications. Getting clarity on your separation date early helps you understand your legal position."),
  ("Can we mediate while still living together?",
   "Yes. Mediation can help you agree on arrangements while under one roof, and can be conducted in separate rooms or online if being together is difficult.")],
 "Separation Under One Roof",
 "Living together, living apart — <em>we can help</em>.",
 "Book a fixed-fee consultation to work out living, financial and parenting arrangements while you're separated under one roof.")

print("Resource pages built.")
