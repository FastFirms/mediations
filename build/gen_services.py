#!/usr/bin/env python3
"""Generate all service pages with unique, substantive, AEO-optimised content."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, faq_html, cta_band,
                       org_schema, faq_schema, breadcrumb_schema, service_schema,
                       BOOK_URL, PHONE, PHONE_HREF)

OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def phero(eyebrow, h1, lede):
    return f"""<main id="main">
{crumb_html([("Home",""),(h1.split(" that ")[0].split(",")[0],None)])}
<section class="phero">
  <div class="phero-blob"></div>
  <div class="wrap">
    <span class="eyebrow"><span class="pulse"></span>{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
    <div class="phero-cta">
      <a href="{BOOK_URL}" class="btn btn-primary">Book a free consultation <span class="arr">→</span></a>
      <a href="{PHONE_HREF}" class="btn btn-ghost">Call {PHONE}</a>
    </div>
  </div>
</section>"""

def answer(text):
    return f'<div class="wrap-narrow"><div class="answer reveal"><p><strong>In short:</strong> {text}</p></div></div>'

def body(blocks):
    return f'<article class="body"><div class="wrap-narrow reveal">{blocks}</div></article>'

def build(slug, title, desc, eyebrow, h1, lede, ans, blocks, qa, crumb_name, cta_h, cta_p):
    schema = [org_schema(),
              breadcrumb_schema([("Home",""),(crumb_name,slug)]),
              service_schema(crumb_name, desc, slug),
              faq_schema(qa)]
    html_doc = head(title, desc, slug, extra_schema=schema)
    html_doc += nav()
    # rebuild phero with correct crumb
    phero_html = f"""<main id="main">
{crumb_html([("Home",""),(crumb_name,None)])}
<section class="phero">
  <div class="phero-blob"></div>
  <div class="wrap">
    <span class="eyebrow"><span class="pulse"></span>{eyebrow}</span>
    <h1>{h1}</h1>
    <p class="lede">{lede}</p>
    <div class="phero-cta">
      <a href="{BOOK_URL}" class="btn btn-primary">Book a free consultation <span class="arr">→</span></a>
      <a href="{PHONE_HREF}" class="btn btn-ghost">Call {PHONE}</a>
    </div>
  </div>
</section>"""
    html_doc += phero_html
    html_doc += answer(ans)
    html_doc += body(blocks)
    html_doc += faq_html(qa, heading=f"{crumb_name} FAQs")
    html_doc += cta_band(cta_h, cta_p)
    html_doc += "</main>" + page_end()
    path = os.path.join(OUT, slug)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "index.html"), "w") as f:
        f.write(html_doc)
    return slug

# ============================================================
# SERVICE PAGE CONTENT — unique, substantive, answer-first
# ============================================================

build(
 "property-settlement-mediation",
 "Property Settlement Mediation | Divide Assets, No Court",
 "Resolve your property settlement through mediation — divide assets, debts and super fairly, then formalise it in consent orders. Fixed-fee, no court.",
 "Property &amp; financial settlements",
 "Property Settlement Mediation — divide assets <em>fairly and finally</em>.",
 "Separating means untangling a shared financial life — the home, savings, super, debts and businesses. Mediation lets you divide it all by agreement, quickly and privately, instead of handing the decision to a court after years of legal fees.",
 "Property settlement mediation is a process where separating partners agree on how to divide assets, debts and superannuation with the help of a neutral mediator, then formalise it through consent orders or a binding financial agreement. It typically resolves in one or two sessions and costs a fraction of litigation.",
 """
 <h2>How is a property settlement <em>actually</em> decided?</h2>
 <p>Australian family law follows a four-step approach to dividing property, and mediation works within exactly the same framework — so your agreement reflects what a court would likely consider fair:</p>
 <ol>
   <li><strong>Identify the asset pool</strong> — everything you own and owe, together and separately: property, savings, superannuation, vehicles, businesses and debts.</li>
   <li><strong>Assess contributions</strong> — financial contributions (income, assets brought in) and non-financial ones (homemaking, parenting, renovations).</li>
   <li><strong>Consider future needs</strong> — earning capacity, age, health, and who cares for the children.</li>
   <li><strong>Check it's just and equitable</strong> — that the overall split is fair in the circumstances.</li>
 </ol>
 <p>In mediation, your mediator helps you work through each step openly, so the outcome is grounded in the same principles a judge would apply — but reached in days, not years. The same four-step approach is set out in the <a href="https://www.austlii.edu.au/cgi-bin/viewdb/au/legis/cth/consol_act/fla1975114/" target="_blank" rel="noopener">Family Law Act 1975</a>.</p>

 <h2>Full and frank disclosure comes first</h2>
 <p>A fair settlement depends on both people putting all their cards on the table. Each of you has a <a href="https://www.fcfcoa.gov.au/fl/duty-disclosure" target="_blank" rel="noopener">duty of full and frank financial disclosure</a> — bank statements, payslips, tax returns, superannuation statements, and details of any businesses or trusts. Mediation actually makes this easier: instead of months of lawyers' letters chasing documents, the mediator sets a clear, shared list up front so you both arrive with the same picture. Without honest disclosure, any agreement can later be set aside, so getting it right protects you.</p>

 <h2>What can be included in a property settlement?</h2>
 <ul>
   <li>The family home and any investment properties</li>
   <li>Superannuation (which can be split between partners)</li>
   <li>Savings, shares and investments</li>
   <li>Vehicles, furniture and personal property</li>
   <li>Business interests and trusts</li>
   <li>Debts, mortgages and liabilities</li>
 </ul>

 <h2>How superannuation, businesses and trusts are treated</h2>
 <p>A property settlement is rarely just the house and the savings. The trickier assets are exactly where mediation earns its keep, because you can agree a sensible approach instead of paying lawyers to fight over valuations:</p>
 <ul>
   <li><strong>Superannuation</strong> — treated as property and able to be split between partners, which often unlocks a fairer division without anyone having to sell the family home.</li>
   <li><strong>Businesses and company interests</strong> — a business one or both of you built forms part of the pool; the question is its value and how to deal with it without crippling the business that pays the bills.</li>
   <li><strong>Trusts and inheritances</strong> — these can be in or out of the pool depending on timing, control and how they were used during the relationship. They need careful, honest handling.</li>
   <li><strong>Debts and liabilities</strong> — mortgages, loans and tax debts are shared too, and a good settlement allocates them as deliberately as it does the assets.</li>
 </ul>

 <h2>Contributions and future needs — the part people miss</h2>
 <p>A fair split isn't simply 50/50. The law weighs both what each of you <em>put in</em> — financial contributions, plus the non-financial ones like homemaking and parenting — and what each of you will <em>need going forward</em>: earning capacity, age, health, and who has the day-to-day care of the children. Two couples with identical asset pools can fairly settle on very different splits because of these factors. In mediation, your mediator helps you weigh them honestly, so the outcome reflects the same considerations a court would apply.</p>

 <h2>Property settlement time limits</h2>
 <p>There are deadlines, and missing them can cost you the right to a settlement — so this is one area where acting early genuinely matters. Mediation is the fastest route to a binding agreement inside these windows:</p>
 <figure class="tbl"><table><caption>Time limits to finalise a property settlement</caption>
 <thead><tr><th>Your situation</th><th>Time limit to apply</th><th>From when</th></tr></thead>
 <tbody>
 <tr><td>Married then divorced</td><td>12 months</td><td>The date your divorce becomes final</td></tr>
 <tr><td>De facto relationship</td><td>24 months</td><td>The date of separation</td></tr>
 </tbody></table></figure>
 <p>You can settle before a divorce is even finalised — many couples do. If you're past a limit, a court's permission is sometimes possible but not guaranteed, so don't bank on it. <a href="/de-facto-mediation/">See de facto property disputes →</a> or <a href="/property-settlement-after-separation/">read the full guide to property settlement after separation →</a></p>

 <h2>What if you can't agree on a value — or your ex stalls?</h2>
 <p>Disagreement over what something is worth is normal, and it doesn't derail mediation: you simply agree on an independent valuer for the home, business or super and work from their figure. Delay is the bigger risk — sometimes one party drags things out hoping the other gives up. Mediation counters that by setting a clear timetable and a shared disclosure list up front, so there's nowhere to hide and far less room to stall than in slow-moving litigation.</p>

 <h2>Making your settlement binding: consent orders or a BFA</h2>
 <p>A handshake agreement isn't enough — to be safe and final, a property settlement should be formalised. There are two routes, and your mediator helps you choose:</p>
 <figure class="tbl"><table><caption>Two ways to make a property settlement legally binding</caption>
 <thead><tr><th></th><th>Consent orders</th><th>Binding financial agreement (BFA)</th></tr></thead>
 <tbody>
 <tr><td>Approved by a court</td><td>Yes — a registrar checks it's just and equitable</td><td>No — a private contract between you</td></tr>
 <tr><td>Independent legal advice</td><td>Not required</td><td>Required for each party</td></tr>
 <tr><td>Typical cost</td><td>Lower (one court filing fee)</td><td>Higher (two sets of legal advice)</td></tr>
 <tr><td>Best for</td><td>Most separating couples</td><td>Maximum flexibility or pre/during relationship</td></tr>
 </tbody></table></figure>
 <p>For most couples, <a href="/consent-orders-explained/">consent orders</a> are the simpler, lower-cost route. Where you want more flexibility, a <a href="/financial-agreements-mediation/">binding financial agreement</a> may suit. <a href="/bfa-or-consent-orders/">Compare the two in detail →</a></p>

 <h2>Why mediate rather than go to court over your settlement?</h2>
 <p>Because a contested property case can consume a meaningful share of the very asset pool you're dividing. Mediation keeps the money where it belongs — with you and your family — and lets you craft creative solutions a court can't, like staggered payouts or keeping the home until children finish school. Many family lawyers recommend it as the sensible first step, then we help you formalise the agreement in <a href="/consent-orders-explained/">consent orders</a>.</p>

 <h2>How long does it take, and what does it cost?</h2>
 <p>Most property matters settle in one or two mediation sessions over a few weeks, compared with the one to three years a contested case can take — and at a fraction of the cost. Because the fee is fixed and shared, you know what you're committing to up front. <a href="/how-much-does-mediation-cost/">See what mediation costs →</a></p>
 """,
 [("How long do I have to finalise a property settlement?",
   "After divorce you generally have 12 months to apply for property orders; de facto couples have two years from the date of separation. Mediation is the fastest way to reach a binding agreement inside these limits."),
  ("Can superannuation be divided in mediation?",
   "Yes. Superannuation is treated as property under Australian family law and can be split between partners. Your mediation agreement can include a superannuation split, formalised through consent orders."),
  ("Is a mediated property agreement legally binding?",
   "It becomes binding once formalised — either as consent orders approved by the court or as a binding financial agreement. We handle that step so your settlement is enforceable."),
  ("What if we can't agree on the value of an asset?",
   "Independent valuations (for property, businesses or super) are commonly used. The mediator helps you agree on a valuation process so the division is based on fair, agreed figures.")],
 "Property Settlement Mediation",
 "Settle your property matters <em>this month</em>, not next year.",
 "Book a fixed-fee consultation and get a clear, honest view of how mediation can divide your assets fairly — without the cost and delay of court.")

build(
 "divorce-mediation",
 "Divorce Mediation Australia | Divorce Mediators",
 "Resolve property, parenting and financial matters with experienced divorce mediators — faster and cheaper than court. Fixed-fee, confidential, Australia-wide.",
 "Divorce &amp; separation",
 "Divorce Mediation — settle the terms <em>without court</em>.",
 "Ending a marriage means untangling parenting, property and finances at the hardest possible time. Divorce mediation gives you a calm, structured way to agree on all of it — guided by a neutral divorce mediator, in weeks rather than years, and on terms you decide together instead of ones a judge imposes.",
 "Divorce mediation is a confidential process where a neutral divorce mediator helps separating couples reach agreement on parenting, property and financial matters without going to court. It usually resolves in one or two sessions, costs a fraction of litigation, and the agreement can be made legally binding through consent orders or a binding financial agreement.",
 """
 <h2>What is divorce mediation?</h2>
 <p>Divorce mediation is a form of <a href="/family-law-mediation/">family law mediation</a> focused on the issues that arise when a marriage ends — how you'll co-parent, how you'll divide property and superannuation, and how you'll handle ongoing financial support. A neutral, accredited mediator guides the conversation, keeps it constructive, and helps you reach a workable agreement. The mediator doesn't take sides or decide the outcome; they help <em>you</em> decide it. It's worth being clear about one thing up front: the legal divorce itself — formally ending the marriage — is a separate administrative step you apply for through the court. Mediation resolves the disputes that come <em>with</em> the divorce. Many couples handle both at once: they <a href="/online-divorce/">apply for divorce online</a> while resolving parenting and property through mediation.</p>

 <h2>What does a divorce mediator do?</h2>
 <p>A divorce mediator is a neutral third party trained to help two people in conflict reach agreement. A good mediator for divorce will set a clear agenda, make sure both people are heard, test proposals against what's realistic and fair, and keep the focus on solutions rather than blame. Many of our divorce mediators are also experienced family lawyers, so they can give you a grounded sense of where a matter would likely land in court — which often makes agreement easier, because both sides can see the realistic range. What a mediator will not do is give either party legal advice or impose a decision; you remain free to get your own advice alongside the process.</p>

 <h2>How divorce mediation works, step by step</h2>
 <ol>
   <li><strong>Fixed-fee consultation</strong> — you tell us what you're facing and we give an honest view of whether mediation can help, and how it sits alongside any legal advice you have.</li>
   <li><strong>Intake and preparation</strong> — each of you meets the mediator separately, financial disclosure is gathered, and the issues are mapped out.</li>
   <li><strong>The mediation session</strong> — guided by the mediator, you work through parenting, property and finances, in the same room or in separate rooms ('shuttle' mediation) where there's conflict or a safety concern.</li>
   <li><strong>Reaching agreement</strong> — points of agreement are recorded in a Heads of Agreement as you go.</li>
   <li><strong>Formalising it</strong> — we turn the agreement into consent orders or a binding financial agreement so it's enforceable.</li>
 </ol>

 <h2>Divorce mediator vs divorce lawyer: what's the difference?</h2>
 <p>They're not rivals — most people benefit from both, in the right order. A divorce lawyer advises and advocates for one side; a divorce mediator stays neutral and helps both sides reach a shared agreement. Starting with mediation usually means any legal advice is cheaper and more focused, because you're paying a lawyer to check an agreement rather than fight for one.</p>
 <figure class="tbl"><table><caption>Divorce mediator vs divorce lawyer — how they differ</caption>
 <thead><tr><th></th><th>Divorce mediator</th><th>Divorce lawyer</th></tr></thead>
 <tbody>
 <tr><td>Acts for</td><td>Both parties, neutrally</td><td>One party</td></tr>
 <tr><td>Goal</td><td>A shared, workable agreement</td><td>The best outcome for their client</td></tr>
 <tr><td>Typical cost</td><td>Fixed fee, usually shared</td><td>Hourly, each side pays their own</td></tr>
 <tr><td>Speed</td><td>Weeks — often one or two sessions</td><td>Months to years if contested</td></tr>
 <tr><td>Decides the outcome?</td><td>No — you do</td><td>No — but pushes a position; a judge decides if it goes to court</td></tr>
 </tbody></table></figure>
 <p>The point isn't to avoid lawyers — it's to avoid an unnecessary court fight. Mediation first, advice alongside, court only if you truly need it.</p>

 <h2>What can divorce mediation resolve?</h2>
 <ul>
   <li><strong>Parenting</strong> — living arrangements, time with each parent and decision-making, formalised in a <a href="/parenting-plan-mediation/">parenting plan</a> or consent orders</li>
   <li><strong>Property and finances</strong> — dividing the home, savings, superannuation, debts and businesses through <a href="/property-settlement-mediation/">property settlement mediation</a></li>
   <li><strong>Spousal maintenance</strong> — ongoing financial support where one partner needs it, via <a href="/spousal-support-mediation/">spousal maintenance mediation</a></li>
   <li><strong>Child support</strong> — private arrangements that depart from or sit alongside the formula</li>
 </ul>
 <p>You can resolve all of these together in one mediation, or just the issues you're stuck on. The framework mediators apply mirrors the <a href="https://www.austlii.edu.au/cgi-bin/viewdb/au/legis/cth/consol_act/fla1975114/" target="_blank" rel="noopener">Family Law Act 1975</a>, so your agreement reflects what a court would consider fair.</p>

 <h2>Divorce mediation vs going to court</h2>
 <p>A contested divorce can run one to three years and cost tens of thousands of dollars per side — money that comes straight out of the asset pool you're trying to divide. Mediation keeps that money with your family. It's also private: court is a public process on the court's timetable, while mediation happens when and how it suits you. And because you craft the agreement yourselves, arrangements tend to last — which matters most when there are children and you'll be co-parenting for years. The <a href="https://www.fcfcoa.gov.au/fl/divorce" target="_blank" rel="noopener">Federal Circuit and Family Court of Australia</a> itself expects parties to make a genuine effort to resolve matters before litigating.</p>

 <h2>How much does divorce mediation cost?</h2>
 <p>You begin with a fixed-fee consultation, so there are no billing surprises. From there, divorce mediation typically costs a small fraction of a contested court case, and the fee is usually shared between the parties — unlike two sets of lawyers billing by the hour. <a href="/how-much-does-mediation-cost/">See a full breakdown of what mediation costs →</a></p>

 <h2>How to prepare for divorce mediation</h2>
 <ol>
   <li><strong>Get your financial picture together</strong> — recent bank, loan and superannuation statements, tax returns and a list of assets and debts. Both parties owe a <a href="https://www.fcfcoa.gov.au/fl/duty-disclosure" target="_blank" rel="noopener">duty of full and frank disclosure</a>.</li>
   <li><strong>Think about the children first</strong> — what arrangement genuinely works for them, not just what feels fair to you.</li>
   <li><strong>Separate needs from wants</strong> — know what you truly need to walk away with, and where you have room to move.</li>
   <li><strong>Come willing to listen</strong> — the couples who resolve fastest are the ones who arrive ready to problem-solve, not re-argue the relationship.</li>
 </ol>

 <h2>When divorce mediation may not be suitable</h2>
 <p>We're honest about the limits. Mediation isn't appropriate in every case — particularly where there is family violence, a serious safety risk, or where one party won't participate or disclose honestly. If that's your situation, you may be exempt from the usual requirement to attempt mediation, and court protection may be the right first step. If you're in immediate danger, call <strong>000</strong>; for confidential support, <strong>1800RESPECT (1800 737 732)</strong> is available 24/7. See our guidance on <a href="/domestic-violence-and-family-law/">family violence and family law</a>.</p>

 <h2>Making your agreement legally binding</h2>
 <p>Reaching agreement is the hard part — we make the rest simple. Once you've settled, we help formalise it so it's enforceable: <a href="/consent-orders-explained/">consent orders</a> approved by the court for parenting and property, or a binding financial agreement where that suits better. You walk away with certainty, not just a handshake. Wherever you are in Australia — from <a href="/sydney-mediation/">Sydney</a> to Perth — you can do the whole thing in person or by secure video.</p>
 """,
 [("What is the difference between divorce and divorce mediation?",
   "Divorce is the legal end of the marriage, which you apply for through the court. Divorce mediation is the process of agreeing on parenting, property and financial arrangements — the issues that come with separating. Most people handle both at the same time."),
  ("Do I still need a lawyer if I use a divorce mediator?",
   "You don't need one to mediate, but it's wise to get independent legal advice alongside the process, especially before signing a binding agreement. Mediation usually makes that advice cheaper and more focused, because the lawyer is checking an agreement rather than fighting for one."),
  ("How long does divorce mediation take?",
   "Most matters resolve in one or two sessions over a few weeks, compared with the one to three years a contested court case can take. Complex financial matters may need more time."),
  ("Is divorce mediation legally binding?",
   "The mediated agreement becomes binding once it's formalised — as consent orders approved by the court, or as a binding financial agreement. We handle that step so your outcome is enforceable."),
  ("Can we mediate if we don't agree on anything yet?",
   "Yes. Starting far apart is normal — that's exactly what mediation is for. A skilled divorce mediator helps you find common ground issue by issue, and you don't have to resolve everything in one sitting.")],
 "Divorce Mediation",
 "Start your divorce the <em>calmer</em> way.",
 "Book a fixed-fee consultation and get an honest view of how divorce mediation can resolve parenting, property and finances — without an unnecessary court fight.")

build(
 "parenting-plan-mediation",
 "Parenting Plan Mediation | Custody Agreements, No Court",
 "Parenting plan mediation helps separated parents agree on living arrangements, time and decisions for the children — calmer than a custody court case.",
 "Parenting &amp; children's arrangements",
 "Parenting Plan Mediation — built around <em>your children</em>.",
 "The hardest part of separating is working out arrangements for the kids. Mediation gives you a calm, structured way to agree on living arrangements, time with each parent and how decisions get made — putting your children first and keeping the choice in your hands.",
 "Parenting plan mediation helps separated parents agree on living arrangements, time-sharing and decision-making for their children, guided by a neutral mediator. It is child-focused, faster and far less costly than a contested parenting case, and for most families it is a required step before court.",
 """
 <h2>What does a parenting plan cover?</h2>
 <p>A parenting plan is a written agreement that sets out the practical arrangements for raising your children after separation. A thorough plan usually covers:</p>
 <ul>
   <li>Where the children live and how time is shared between parents</li>
   <li>How handovers, holidays and special occasions work</li>
   <li>How major long-term decisions (school, health, religion) are made</li>
   <li>How parents will communicate and resolve future disagreements</li>
   <li>Arrangements for travel, including overseas</li>
 </ul>
 <p>For a full checklist of what to include, see our <a href="/parenting-plan-template/">parenting plan template guide</a>.</p>

 <h2>How does parenting plan mediation work?</h2>
 <p>Mediation is a structured conversation guided by a neutral, accredited practitioner. It usually runs in a few stages:</p>
 <ul>
   <li><strong>Intake</strong> — each parent meets the mediator separately so the issues, and any safety concerns, are understood before you begin.</li>
   <li><strong>Joint sessions</strong> — you work through each part of the plan with the mediator keeping the focus on the children, not the past.</li>
   <li><strong>Drafting</strong> — the agreement is written up as a clear parenting plan both parents sign.</li>
   <li><strong>Formalising (optional)</strong> — if you want it enforceable, the plan is converted into <a href="/consent-orders-explained/">consent orders</a>.</li>
 </ul>
 <p>If being in the same room is difficult, sessions can run in separate rooms ('shuttle' mediation) or <a href="/online-divorce/">online by video</a>.</p>

 <figure class="tbl"><table><caption>Parenting plan vs consent orders vs a contested court case</caption>
 <thead><tr><th></th><th>Parenting plan</th><th>Consent orders</th><th>Contested court case</th></tr></thead>
 <tbody>
 <tr><td>Legally enforceable</td><td>No, but courts consider it</td><td>Yes</td><td>Yes</td></tr>
 <tr><td>Who decides</td><td>The parents</td><td>The parents (court approves)</td><td>A judge</td></tr>
 <tr><td>Typical timeframe</td><td>One or two sessions</td><td>Weeks once agreed</td><td>One to three years</td></tr>
 <tr><td>Flexibility to change</td><td>High — by agreement</td><td>Needs a new application</td><td>Needs a new application</td></tr>
 </tbody></table></figure>

 <h2>Is a parenting plan legally binding?</h2>
 <p>A parenting plan itself is not legally enforceable, but it carries real weight — a court will consider it if a dispute later arises. If you want a binding outcome, your agreement can be turned into <a href="/consent-orders-explained/">consent orders</a>, which are enforceable. Many families start with a parenting plan and formalise it once arrangements have settled.</p>

 <h2>The children's best interests come first</h2>
 <p>Whatever you agree, the <a href="https://www.austlii.edu.au/cgi-bin/viewdb/au/legis/cth/consol_act/fla1975114/" target="_blank" rel="noopener">Family Law Act 1975</a> requires arrangements to be made in the best interests of the child. Reforms that took effect in 2024 simplified the factors a court weighs and put the safety and developmental needs of children at the centre. A good plan reflects each child's age and stage — younger children usually need shorter, more frequent contact, while teenagers need arrangements that respect school, friends and activities. The <a href="https://www.familyrelationships.gov.au/" target="_blank" rel="noopener">Family Relationships Online</a> service and <a href="https://aifs.gov.au/" target="_blank" rel="noopener">Australian Institute of Family Studies</a> are useful starting points for the evidence on what helps children adjust.</p>

 <h2>Common care arrangements parents agree in mediation</h2>
 <p>There's no single 'right' arrangement — the best one fits your children's ages, your work, and how far apart you live. These are the patterns separated parents most often land on, and mediation helps you choose or tailor one rather than have a court impose it:</p>
 <figure class="tbl"><table><caption>Common shared-care patterns after separation</caption>
 <thead><tr><th>Arrangement</th><th>How it works</th><th>Often suits</th></tr></thead>
 <tbody>
 <tr><td>Week about</td><td>Alternating weeks with each parent</td><td>School-age children; parents living close</td></tr>
 <tr><td>5-2-2-5</td><td>Fixed weekdays with each parent, alternating weekends</td><td>Families wanting predictable routine</td></tr>
 <tr><td>Alternate weekends</td><td>Primary home with one parent, every second weekend (plus a weeknight) with the other</td><td>Younger children; longer distances</td></tr>
 <tr><td>Tailored</td><td>Built around shift work, travel or a child's needs</td><td>Any family that doesn't fit a template</td></tr>
 </tbody></table></figure>
 <p>Research consistently shows children adjust best when conflict is low and both parents stay involved — which is exactly what mediation is designed to protect.</p>

 <h2>Is this the same as child custody mediation?</h2>
 <p>In practice, yes. 'Custody' is an older word that Australian family law no longer uses — today the focus is on parental responsibility and the time children spend with each parent. So if you're searching for <a href="/child-custody-mediation/">child custody mediation</a>, parenting plan mediation is the process you're after. It's also where ongoing <strong>co-parenting</strong> gets easier: a clear plan removes the weekly friction over handovers, holidays and decisions, so you spend less energy negotiating and more parenting.</p>

 <h2>When parenting mediation isn't appropriate</h2>
 <p>Mediation depends on both parents being able to negotiate safely. Where there is family violence, a child-safety concern or a serious power imbalance, it may not be suitable — and you may be exempt from the requirement to attempt it. Your safety and your children's safety come first. If you're in immediate danger call <strong>000</strong>; for confidential support, <strong>1800RESPECT (1800 737 732)</strong> is available 24/7. See <a href="/domestic-violence-and-family-law/">family violence and family law</a>.</p>

 <h2>Do we have to mediate before going to court?</h2>
 <p>For most parenting matters, yes. Under the Family Law Act you must make a genuine attempt at <a href="https://www.fcfcoa.gov.au/fl/fdr" target="_blank" rel="noopener">family dispute resolution</a> before applying for parenting orders, unless an exemption applies. You'll need a <a href="/section-60i-certificates/">Section 60I certificate</a> to file — which we can issue as part of your mediation.</p>

 <h2>How long does it take, and what does it cost?</h2>
 <p>Most families reach a workable parenting plan in one or two sessions over a few weeks — a fraction of the time and cost of a contested parenting case, which can run for one to three years. Keeping the matter out of court also keeps the decisions with the people who know the children best. <a href="/how-much-does-mediation-cost/">See what mediation costs →</a> or read more on <a href="/child-custody-mediation/">child custody mediation</a>.</p>
 """,
 [("Is a parenting plan legally enforceable?",
   "A parenting plan is not directly enforceable, but a court will take it into account in any later dispute. To make arrangements binding, they can be formalised as consent orders, which are enforceable."),
  ("What's the difference between a parenting plan and consent orders?",
   "A parenting plan is a flexible written agreement signed by both parents. Consent orders are approved by the court and legally binding. Many parents start with a plan and convert it to consent orders later."),
  ("Do both parents have to agree to mediation?",
   "Mediation is voluntary, but both parents are strongly encouraged to attend, and a genuine attempt is generally required before court. If one parent refuses, the other can still obtain a Section 60I certificate."),
  ("Can children have a say in the parenting plan?",
   "Where appropriate, child-inclusive practices can ensure children's views are heard in an age-appropriate way, without putting them in the middle of the dispute."),
  ("How long does parenting mediation take?",
   "Most families reach a workable parenting plan in one or two sessions over a few weeks — far faster than a contested parenting case, which can take one to three years."),
  ("What happens in parenting mediation?",
   "Each parent first meets the mediator separately, then joint sessions work through living arrangements, time-sharing and decision-making with the focus kept on the children. The agreement is written up as a parenting plan you both sign.")],
 "Parenting Plan Mediation",
 "Put your children first — <em>starting today</em>.",
 "Book a fixed-fee consultation and let an accredited family mediator help you build a parenting plan that works for everyone who matters most.")

build(
 "section-60i-certificates",
 "Section 60I Certificate | Family Dispute Resolution Australia",
 "Need a Section 60I certificate before family court? Our accredited practitioners conduct mediation and issue Section 60I certificates so you can meet your legal obligations.",
 "Required before parenting court action",
 "Section 60I Certificates — issued by <em>accredited practitioners</em>.",
 "Before you can apply to court for parenting orders, the law requires you to attempt family dispute resolution first — and prove it with a Section 60I certificate. We conduct the mediation and issue the certificate, so you meet your obligations and genuinely try to resolve things at once.",
 "A Section 60I certificate is a document issued by an accredited Family Dispute Resolution Practitioner confirming you attempted mediation before applying to court for parenting orders. Under the Family Law Act 1975 it is generally required to file a parenting application, unless an exemption (such as family violence or urgency) applies.",
 """
 <h2>When do you need a Section 60I certificate?</h2>
 <p>You generally need one before filing any application for parenting orders in the Federal Circuit and Family Court of Australia. It proves you made a genuine effort to resolve the dispute through family dispute resolution before asking a court to decide.</p>

 <h2>What are the five types of Section 60I certificate?</h2>
 <p>An accredited practitioner can issue a certificate stating that:</p>
 <ul>
   <li>The other party did not attend, despite being invited</li>
   <li>Both parties attended and made a genuine effort to resolve the dispute</li>
   <li>Both parties attended but one or both did not make a genuine effort</li>
   <li>The practitioner decided the matter was not appropriate for mediation</li>
   <li>Mediation started but the practitioner decided it was not appropriate to continue</li>
 </ul>

 <div class="callout">
   <h3>When a certificate isn't required</h3>
   <p>Exemptions apply in cases of family violence, child abuse risk, genuine urgency, or where a party is unable to participate. If this is your situation, tell us in your consultation and we'll advise the safest, correct path.</p>
 </div>

 <h2>How do you get a Section 60I certificate?</h2>
 <p>You attend family dispute resolution with an accredited practitioner. If the matter resolves, you may not need to go to court at all. If it doesn't, the practitioner issues the certificate so you can file. Either way you've moved forward. <a href="/parenting-plan-mediation/">See parenting plan mediation →</a></p>
 """,
 [("How long is a Section 60I certificate valid?",
   "A Section 60I certificate is generally valid for 12 months from the date of issue. If you don't file within that time, you may need to attend family dispute resolution again."),
  ("Who can issue a Section 60I certificate?",
   "Only an accredited Family Dispute Resolution Practitioner can issue one. Our practitioners are accredited and issue certificates as part of the mediation process."),
  ("Do I need a certificate for property matters?",
   "No. Section 60I certificates relate to parenting matters. Property and financial disputes don't require one, though mediation is still strongly encouraged."),
  ("What if the other parent won't attend?",
   "If the other parent is invited but doesn't attend, the practitioner can issue a certificate to that effect, allowing you to proceed to court.")],
 "Section 60I Certificates",
 "Meet your obligations — and maybe avoid court <em>entirely</em>.",
 "Book a consultation with an accredited Family Dispute Resolution Practitioner. We'll conduct your mediation and issue your Section 60I certificate if you need it.")

build(
 "financial-agreements-mediation",
 "Binding Financial Agreements (BFA) Mediation | Protect Assets",
 "Negotiate a binding financial agreement (BFA) through mediation — before, during or after a relationship. Protect assets with accredited mediators and proper legal advice.",
 "Binding financial agreements",
 "Financial Agreement Mediation — <em>protect what matters</em>.",
 "A binding financial agreement sets out how assets and finances are handled if a relationship ends. Mediation is the calm way to negotiate one — whether you're entering a relationship, already in one, or separating — so the terms are genuinely agreed rather than fought over.",
 "A binding financial agreement (BFA) is a private contract between partners that sets out how property, finances and support will be divided if they separate. Mediation helps couples negotiate fair terms, which are then formalised with independent legal advice to make the agreement binding under the Family Law Act.",
 """
 <h2>When can you make a binding financial agreement?</h2>
 <p>BFAs can be made at any stage of a relationship:</p>
 <ul>
   <li><strong>Before</strong> a marriage or de facto relationship (sometimes called a prenup)</li>
   <li><strong>During</strong> the relationship, to clarify financial arrangements</li>
   <li><strong>After</strong> separation, to finalise property and support</li>
 </ul>

 <h2>What makes a financial agreement legally binding?</h2>
 <p>For a BFA to be binding under Australian law, strict requirements must be met — most importantly, each party must receive independent legal advice before signing. Mediation handles the hard part (reaching fair terms everyone accepts); the formal legal steps then make it enforceable. We guide you through both.</p>

 <div class="callout">
   <h3>BFA or consent orders — which is right for you?</h3>
   <p>Both can finalise property matters, but they work differently. Consent orders are approved by a court; BFAs are private contracts. We'll help you choose. <a href="/consent-orders/">Compare consent orders →</a></p>
 </div>

 <h2>Why mediate a financial agreement?</h2>
 <p>Because financial agreements negotiated adversarially breed resentment and are more likely to be challenged later. Terms reached through mediation tend to be fairer, better understood by both parties, and more durable. <a href="/spousal-support-mediation/">See spousal maintenance →</a></p>
 """,
 [("What is a binding financial agreement?",
   "A BFA is a private contract between partners setting out how assets, finances and support are handled if they separate. It can be made before, during or after a relationship."),
  ("Do both people need their own lawyer for a BFA?",
   "Yes. For a BFA to be binding, each party must receive independent legal advice before signing. Mediation reaches the agreed terms; independent advice makes it enforceable."),
  ("Can a binding financial agreement be overturned?",
   "A BFA can be set aside in limited circumstances — for example fraud, non-disclosure, or if proper procedures weren't followed. Agreements reached fairly through mediation are far less likely to be challenged."),
  ("Is a BFA the same as a prenup?",
   "A prenup is simply a BFA made before marriage or a de facto relationship. The same legal framework applies.")],
 "Binding Financial Agreements",
 "Protect your future, <em>without the conflict</em>.",
 "Book a fixed-fee consultation to negotiate a fair financial agreement through mediation — with the legal formalisation that makes it binding.")

build(
 "spousal-support-mediation",
 "Spousal Maintenance Mediation | Fair Support, No Court",
 "Resolve spousal maintenance through mediation. Agree on fair, sustainable support without court — accredited mediators, fixed-fee, formalised properly.",
 "Spousal &amp; partner maintenance",
 "Spousal Maintenance Mediation, settled <em>fairly and respectfully</em>.",
 "When one partner can't adequately support themselves after separation, the other may be required to help. Mediation lets you agree on fair, realistic maintenance — based on genuine need and capacity to pay — without a draining court fight.",
 "Spousal maintenance is financial support one partner pays the other after separation when that partner cannot reasonably meet their own needs. Mediation helps couples agree on the amount and duration based on need and capacity to pay, then formalise it in consent orders or a financial agreement.",
 """
 <h2>Who is entitled to spousal maintenance?</h2>
 <p>Spousal maintenance isn't automatic. It depends on two things: one partner's genuine need for support, and the other partner's capacity to pay. A court (or your mediation) weighs factors such as:</p>
 <ul>
   <li>Age, health and ability to earn an income</li>
   <li>Care of children and its effect on earning capacity</li>
   <li>The standard of living that's reasonable in the circumstances</li>
   <li>The length of the relationship and its financial impact</li>
 </ul>

 <h2>How is spousal maintenance different from child support?</h2>
 <p>Child support is for the costs of raising children and is usually assessed by Services Australia. Spousal maintenance supports a former partner directly. They're separate — and you may deal with both. <a href="/child-support-mediation/">See child support mediation →</a></p>

 <div class="callout">
   <h3>Maintenance can be a lump sum or periodic</h3>
   <p>Mediation lets you design arrangements that genuinely fit — a one-off lump sum, periodic payments for a fixed time, or support while a partner retrains. A court order is often more rigid.</p>
 </div>

 <h2>Why mediate spousal maintenance?</h2>
 <p>Because these arrangements work best when both people understand and accept them. Mediation produces sustainable agreements rather than imposed obligations that breed missed payments and return trips to court. <a href="/property-settlement-mediation/">Often it's resolved alongside your property settlement.</a></p>
 """,
 [("Am I automatically entitled to spousal maintenance?",
   "No. Entitlement depends on one partner's genuine need and the other's capacity to pay. Mediation helps you assess both fairly and agree on a realistic arrangement."),
  ("How long does spousal maintenance last?",
   "It varies. Maintenance can be a lump sum, or periodic payments for a fixed period — for example while a partner retrains or returns to work. Mediation lets you tailor the duration."),
  ("Is spousal maintenance the same as child support?",
   "No. Child support covers the costs of raising children; spousal maintenance supports a former partner. They are assessed separately and you may address both."),
  ("Can a spousal maintenance agreement be made binding?",
   "Yes, through consent orders or a binding financial agreement. We help you formalise whatever you agree in mediation.")],
 "Spousal Maintenance Mediation",
 "Reach a fair arrangement, <em>without the fight</em>.",
 "Book a fixed-fee consultation to resolve spousal maintenance through mediation — fairly, sustainably and without court.")

build(
 "child-support-mediation",
 "Child Support Mediation Australia | Resolve It Privately",
 "Resolve child support disputes through mediation. Agree on private arrangements, departures from assessment and special expenses — without court, with accredited mediators.",
 "Child support arrangements",
 "Child Support Mediation — resolved <em>privately and fairly</em>.",
 "Child support disagreements can poison co-parenting. Mediation gives you a private, practical way to agree on arrangements — including private agreements that go beyond the standard formula — so your children are properly supported and the conflict ends.",
 "Child support mediation helps separated parents resolve disagreements about supporting their children — including private child support agreements, departures from the standard assessment, and how special expenses are shared. It keeps decisions private and cooperative rather than adversarial.",
 """
 <h2>How is child support normally calculated?</h2>
 <p>In Australia, child support is usually assessed by Services Australia using a formula based on both parents' incomes, the care arrangements, and the costs of children. But the formula doesn't fit every family — and that's where mediation helps.</p>

 <h2>What can child support mediation resolve?</h2>
 <ul>
   <li>Private child support agreements that suit your circumstances</li>
   <li>How school fees, medical costs and extracurricular expenses are shared</li>
   <li>Disagreements about the assessment or a change in circumstances</li>
   <li>Arrangements that work alongside your parenting plan</li>
 </ul>

 <div class="callout">
   <h3>A binding child support agreement</h3>
   <p>Parents can make a binding child support agreement that departs from the formula — for example covering private school fees directly. As with a BFA, each parent needs independent legal advice. We guide you through it.</p>
 </div>

 <h2>Why not just rely on the assessment?</h2>
 <p>The formula is a starting point, not a complete solution — it rarely addresses big-ticket items like private schooling or significant medical needs. Mediation lets you build a complete, tailored arrangement that actually reflects your children's lives. <a href="/parenting-plan-mediation/">Pairs naturally with a parenting plan.</a></p>
 """,
 [("Can we agree on child support privately instead of using the formula?",
   "Yes. Parents can make a private or binding child support agreement that departs from the standard assessment. Mediation helps you negotiate fair terms; a binding agreement requires independent legal advice."),
  ("Does child support mediation replace Services Australia?",
   "Not entirely — Services Australia still administers assessments. Mediation helps you resolve disputes and reach agreements that can sit alongside or depart from the assessment."),
  ("Can mediation cover school fees and medical costs?",
   "Yes. These 'special expenses' are a common focus of child support mediation, since the standard formula often doesn't address them adequately."),
  ("What if the other parent won't pay what was assessed?",
   "Mediation can address the underlying disagreement and create a workable plan. Enforcement remains available through Services Australia, but resolving the conflict often prevents the problem recurring.")],
 "Child Support Mediation",
 "Support your children — <em>without the standoff</em>.",
 "Book a fixed-fee consultation to resolve child support through mediation, with arrangements that genuinely fit your family.")

build(
 "de-facto-mediation",
 "De Facto Relationship Mediation Australia | Same Rights",
 "Resolve de facto relationship disputes through mediation — property, finances and parenting. De facto partners have similar rights to married couples. No court required.",
 "De facto &amp; same-sex relationships",
 "De Facto Mediation — <em>same rights, same clarity</em>.",
 "De facto and same-sex partners have substantially the same rights as married couples when a relationship ends. Mediation resolves property, financial and parenting matters the same way — quickly, privately and without court — once your relationship qualifies under the law.",
 "De facto relationship mediation resolves property, financial and parenting disputes for unmarried couples, including same-sex partners. De facto partners have similar rights to married couples under the Family Law Act, and mediation offers the same fast, private, out-of-court path to resolution.",
 """
 <h2>What counts as a de facto relationship?</h2>
 <p>You're generally considered de facto if you've lived together on a genuine domestic basis. Courts look at factors including the length of the relationship, whether you lived together, financial interdependence, a shared residence, and whether you have children together. Same-sex relationships are treated identically.</p>

 <h2>Do de facto partners have the same rights as married couples?</h2>
 <p>Largely, yes. When a qualifying de facto relationship ends, partners can seek property settlements, superannuation splits and spousal maintenance — much like divorcing couples. The main differences are in time limits and the threshold of proving the relationship existed.</p>

 <div class="callout">
   <h3>Time limit: two years</h3>
   <p>De facto partners generally have two years from separation to apply for property or maintenance orders. Mediation is the fastest way to reach a binding agreement within that window. <a href="/property-settlement-mediation/">See property settlement →</a></p>
 </div>

 <h2>Why mediation suits de facto disputes</h2>
 <p>De facto separations often involve disentangling finances that were never formally combined, which can get contentious fast. Mediation provides the neutral structure to sort it out fairly — and avoids the added cost of first proving the relationship's existence in court. <a href="/financial-agreements-mediation/">A financial agreement can also protect both partners.</a></p>
 """,
 [("Do de facto couples have the same rights as married couples?",
   "Largely yes. Qualifying de facto partners can seek property settlements, superannuation splits and maintenance under the Family Law Act, similar to married couples, with some differences in time limits and proving the relationship."),
  ("How long do de facto partners have to make a claim?",
   "Generally two years from the date of separation. Mediation is the fastest way to reach a binding agreement within that limit."),
  ("Are same-sex relationships treated the same?",
   "Yes. Same-sex de facto relationships have the same status and rights under Australian family law."),
  ("How do we prove we were in a de facto relationship?",
   "Courts consider factors like living together, the length of the relationship, financial interdependence and shared children. Mediation can proceed by agreement without a contested court finding.")],
 "De Facto Relationship Mediation",
 "Same rights. Same fairness. <em>Far less stress.</em>",
 "Book a fixed-fee consultation to resolve your de facto dispute through mediation — property, finances and parenting, all without court.")

build(
 "grandparents-mediation",
 "Grandparents' Rights Mediation | See Your Grandchildren",
 "Grandparents can use mediation to keep seeing grandchildren after family breakdown. Resolve contact arrangements respectfully, without court. Accredited mediators.",
 "Grandparents &amp; extended family",
 "Grandparents' Rights Mediation — <em>stay part of the family</em>.",
 "When families break down, grandparents can lose contact with grandchildren they love. Australian law recognises children's right to a relationship with people significant to their care — including grandparents — and mediation is the gentlest way to restore and protect that bond.",
 "Grandparents' mediation helps grandparents reach agreement about spending time with their grandchildren after a separation or family conflict. The Family Law Act recognises children's right to maintain relationships with grandparents and other significant people, and mediation resolves this without a contested court case.",
 """
 <h2>Do grandparents have legal rights to see grandchildren?</h2>
 <p>The law focuses on the child's right to maintain meaningful relationships with people significant to their welfare — which expressly includes grandparents. Grandparents can apply for orders to spend time with grandchildren, but mediation is almost always the better first step: it's less adversarial and far easier on the children.</p>

 <h2>When does grandparent mediation help?</h2>
 <ul>
   <li>After a parental separation that has cut off contact</li>
   <li>When a family conflict has damaged relationships</li>
   <li>Where a parent has passed away and contact is at risk</li>
   <li>When grandparents are providing significant care and need certainty</li>
 </ul>

 <div class="callout">
   <h3>The children come first — always</h3>
   <p>Mediation keeps the focus where it belongs: on what's best for the children, not on adult grievances. That child-centred approach is exactly why it works where confrontation fails.</p>
 </div>

 <h2>Why mediate rather than litigate?</h2>
 <p>Court action against your own children or their former partners can permanently fracture a family. Mediation rebuilds communication instead of destroying it — giving you the best chance of a lasting relationship with your grandchildren. <a href="/parenting-plan-mediation/">Arrangements can be included in a parenting plan.</a></p>
 """,
 [("Do grandparents have a legal right to see their grandchildren?",
   "The law recognises a child's right to maintain relationships with significant people including grandparents. Grandparents can apply for time with grandchildren, but mediation is usually the better first step."),
  ("Can grandparents apply for parenting orders?",
   "Yes. Grandparents can apply for orders about spending time with or caring for grandchildren, though mediation is encouraged before court."),
  ("Do grandparents need a Section 60I certificate?",
   "If applying for parenting orders, grandparents generally need to attempt family dispute resolution first, the same as parents. We can conduct this and issue the certificate."),
  ("What if a parent refuses any contact?",
   "Mediation provides a neutral space to address the parent's concerns and rebuild trust. It succeeds in many cases where direct conversations have broken down.")],
 "Grandparents' Mediation",
 "Don't lose the bond — <em>rebuild it</em>.",
 "Book a fixed-fee consultation to restore contact with your grandchildren through respectful, child-focused mediation.")

build(
 "consent-orders",
 "Consent Orders Australia | Make Your Agreement Legally Binding",
 "Turn your mediated agreement into legally binding consent orders. We prepare and lodge consent orders for parenting and property — no court hearing required.",
 "Formalising your agreement",
 "Consent Orders — make your agreement <em>legally binding</em>.",
 "Reaching agreement is the hard part — consent orders make it stick. They turn what you've agreed into legally enforceable court orders, usually without anyone setting foot in a courtroom. We prepare and lodge them for you.",
 "Consent orders are written agreements approved by the Federal Circuit and Family Court of Australia that make your parenting or property arrangements legally binding. You don't attend a hearing — the court reviews your agreement on the papers and, if it's fair, makes it into enforceable orders.",
 """
 <h2>What can consent orders cover?</h2>
 <ul>
   <li><strong>Parenting</strong> — living arrangements, time with each parent, decision-making</li>
   <li><strong>Property</strong> — division of assets, debts and superannuation</li>
   <li><strong>Spousal maintenance</strong> — ongoing financial support</li>
 </ul>

 <h2>How do consent orders work?</h2>
 <p>Once you reach agreement (often through mediation), an application for consent orders is prepared and lodged with the court. A registrar reviews it to ensure parenting arrangements are in the children's best interests and property division is just and equitable. If satisfied, the court makes the orders — no hearing, no appearance. For a step-by-step walkthrough of the process, costs and timeframes, see our <a href="/consent-orders-explained/">consent orders explained guide</a>.</p>

 <div class="callout">
   <h3>Consent orders vs a parenting plan vs a BFA</h3>
   <p>Consent orders are court-approved and enforceable. A <a href="/parenting-plan-mediation/">parenting plan</a> is flexible but not directly enforceable. A <a href="/financial-agreements-mediation/">binding financial agreement</a> is a private contract for financial matters. We help you choose the right instrument.</p>
 </div>

 <h2>Why mediate first, then formalise?</h2>
 <p>Because consent orders only work when you actually agree — the court won't impose terms in a consent application. Mediation gets you to that agreement efficiently; consent orders lock it in. It's the complete path from dispute to durable resolution. <a href="/property-settlement-mediation/">Start with property settlement →</a></p>
 """,
 [("Do I have to go to court for consent orders?",
   "No. Consent orders are reviewed by the court on the papers. If your agreement is fair, the court makes the orders without anyone attending a hearing."),
  ("Are consent orders legally binding?",
   "Yes. Once approved, consent orders are enforceable court orders, the same as if a judge had made them after a hearing."),
  ("How long do consent orders take?",
   "Once lodged, processing times vary, but it's far faster than contested litigation. The slow part is reaching agreement — which mediation accelerates."),
  ("Can consent orders be changed later?",
   "Property orders are generally final. Parenting orders can be changed if circumstances significantly change and it's in the children's best interests, ideally by agreement through mediation.")],
 "Consent Orders",
 "Lock in your agreement — the <em>right way</em>.",
 "Book a consultation. We'll help you reach agreement through mediation and prepare the consent orders that make it legally binding.")

build(
 "online-divorce",
 "Online Divorce in Australia | Apply &amp; Mediate by Video",
 "Apply for divorce online through the courts, and resolve parenting, property and finances by secure video with accredited mediators — anywhere in Australia.",
 "Online &amp; remote mediation",
 "Online Divorce Mediation — <em>wherever you are in Australia</em>.",
 "You don't need to be in the same room — or even the same state — to resolve a separation. Our secure online mediation handles parenting, property and financial matters by video, making expert dispute resolution available across all of Australia, including regional and remote areas.",
 "Online divorce mediation lets separating couples resolve parenting, property and financial matters by secure video conference with an accredited mediator. It offers the same structured process and binding outcomes as in-person mediation, available anywhere in Australia.",
 """
 <h2>What does "online divorce" actually mean?</h2>
 <p>"Online divorce" covers two different things, and it helps to separate them. The first is the <strong>divorce application itself</strong> — the legal step that formally ends a marriage — which in Australia is now filed entirely online through the courts. The second is resolving the <strong>issues that come with separation</strong> — parenting, property and finances — which a divorce order does not deal with at all. Those are settled by agreement (ideally through mediation) or, failing that, by the court.</p>
 <p>Most people who search for "online divorce" want help with both: getting the paperwork through, and sorting out the children and the assets without a courtroom fight. This page explains how each part works online.</p>

 <h2>How to apply for a divorce online in Australia</h2>
 <p>You apply for divorce through the <a href="https://www.comcourts.gov.au/" target="_blank" rel="noopener">Commonwealth Courts Portal</a>, the online filing system of the <a href="https://www.fcfcoa.gov.au/fl/divorce" target="_blank" rel="noopener">Federal Circuit and Family Court of Australia</a>. There is no need to attend a registry in person to lodge it. In outline:</p>
 <ul>
   <li><strong>Check you're eligible</strong> — you (or your spouse) must regard Australia as home, and you must have been separated for at least 12 months and one day.</li>
   <li><strong>Create a portal account</strong> and complete the online Application for Divorce.</li>
   <li><strong>Pay the filing fee</strong> (a reduced fee applies if you hold a concession card or would suffer financial hardship).</li>
   <li><strong>Serve a sole application</strong> on your spouse, or file jointly so service isn't required.</li>
   <li><strong>Attend the hearing if needed</strong> — often you don't have to, particularly for a joint application or where there are no children under 18.</li>
 </ul>
 <p>A divorce order takes effect one month and one day after it is granted. Remember it ends the marriage only — it does not divide property or settle parenting. That second half is where <a href="/divorce-mediation/">divorce mediation</a> does the real work. <a href="/how-to-get-a-divorce-in-australia-a-step-by-step-guide/">See our full step-by-step divorce guide →</a></p>

 <figure class="tbl"><table><caption>The two halves of an online divorce</caption>
 <thead><tr><th></th><th>The divorce application</th><th>Resolving parenting &amp; property</th></tr></thead>
 <tbody>
 <tr><td>What it does</td><td>Legally ends the marriage</td><td>Settles children, property, finances</td></tr>
 <tr><td>How it's done online</td><td>Commonwealth Courts Portal</td><td>Online mediation by secure video</td></tr>
 <tr><td>Time limit</td><td>After 12 months' separation</td><td>Property: within 12 months of divorce</td></tr>
 <tr><td>Outcome</td><td>Divorce order</td><td>Parenting plan, consent orders or BFA</td></tr>
 </tbody></table></figure>

 <h2>How does online mediation work?</h2>
 <p>Online mediation mirrors in-person mediation, conducted over secure video. You can be in the same virtual room, or in separate virtual rooms with the mediator moving between you ('shuttle' mediation) — useful where there's high conflict or a safety concern. Documents are shared and signed electronically, and sessions are scheduled around work and childcare.</p>

 <h2>Is online mediation as effective as in person?</h2>
 <p>Yes — and often more convenient. Online mediation removes travel, reduces cost, and lets people participate from a place where they feel safe and comfortable. Outcomes are just as binding once formalised in <a href="/consent-orders-explained/">consent orders</a> or a financial agreement. For parenting matters, an accredited practitioner can also issue the <a href="/section-60i-certificates/">Section 60I certificate</a> you need before applying to court.</p>

 <div class="callout">
   <h3>Built for regional and remote Australia</h3>
   <p>If you're far from a capital city, online mediation gives you access to the same nationally accredited mediators as anyone in Sydney or Melbourne — no long drives, no relocating.</p>
 </div>

 <h2>What can be resolved online?</h2>
 <ul>
   <li>Parenting arrangements and <a href="/parenting-plan-mediation/">parenting plans</a></li>
   <li><a href="/property-settlement-mediation/">Property settlements</a> and superannuation splits</li>
   <li>Spousal maintenance and child support</li>
   <li>Section 60I certificates for parenting matters</li>
 </ul>

 <h2>Sole or joint application — and what if your spouse won't cooperate?</h2>
 <p>You can apply for divorce <strong>jointly</strong> with your spouse, or on your own as a <strong>sole</strong> applicant. A joint application is simplest: there's nothing to serve, and neither of you usually needs to attend court. With a sole application you must arrange for your spouse to be served with the documents, and prove that service to the court.</p>
 <p>You do <em>not</em> need your spouse's consent to get divorced. If they won't participate, a sole application still proceeds — the court only needs to be satisfied you've been separated for 12 months and that proper service was attempted. Mediation can't force a divorce, but it can resolve the parenting and property questions that are usually the real source of conflict, so the divorce itself becomes a formality.</p>

 <h2>Is an online divorce cheaper?</h2>
 <p>Usually, yes. Filing online avoids registry trips, and resolving the surrounding issues by mediation rather than litigation is dramatically cheaper than a contested case — a settled matter is often resolved in one or two sessions instead of the one to three years a defended court case can take. The court's filing fee is set by the FCFCOA and reduced fees apply on hardship grounds. <a href="/how-much-does-mediation-cost/">See what mediation costs →</a></p>
 <p><a href="/family-law-mediation/">See our full family law mediation service →</a></p>
 """,
 [("Can you get a divorce online in Australia?",
   "Yes. You apply through the Commonwealth Courts Portal, the online filing system of the Federal Circuit and Family Court — there's no need to attend a registry in person. You must have been separated for at least 12 months."),
  ("Does an online divorce also sort out property and parenting?",
   "No. A divorce order only ends the marriage. Property, finances and parenting are resolved separately — by agreement (ideally through mediation) or by the court — and have their own time limits."),
  ("Do both people have to agree to divorce online?",
   "No. You can apply jointly or as a sole applicant. You don't need your spouse's consent; a sole application proceeds provided you've been separated 12 months and your spouse has been properly served."),
  ("Is online mediation legally valid?",
   "Yes. Agreements reached through online mediation are just as valid as in-person ones and can be formalised into binding consent orders or financial agreements."),
  ("What technology do I need?",
   "A device with a camera and microphone, and an internet connection. We use secure video conferencing and guide you through the setup beforehand."),
  ("Can we do online mediation if there's conflict or safety concerns?",
   "Yes. Online 'shuttle' mediation keeps parties in separate virtual rooms with the mediator moving between them, which can feel safer and less confronting."),
  ("Is online mediation available in regional areas?",
   "Yes. Online mediation is available anywhere in Australia with an internet connection, giving regional and remote clients the same access as those in capital cities.")],
 "Online Divorce Mediation",
 "Resolve it from home — <em>anywhere in Australia</em>.",
 "Book a fixed-fee online consultation and resolve your separation by secure video, with the same accredited mediators and binding outcomes as in person.")

build(
 "workplace-mediation",
 "Workplace Mediation Australia | Resolve Disputes Fast",
 "Resolve workplace disputes through mediation — unfair dismissal, bullying, contracts and conflict. Faster and cheaper than the Fair Work Commission. Accredited mediators.",
 "Workplace &amp; employment disputes",
 "Workplace Mediation — <em>resolve disputes before they escalate</em>.",
 "Workplace conflict is costly, stressful and contagious. Mediation resolves disputes — from unfair dismissal claims to bullying complaints — early and confidentially, before they become expensive battles at the Fair Work Commission, so everyone can get back to work.",
 "Workplace mediation is a confidential process where a neutral mediator helps employers and employees resolve disputes — such as unfair dismissal, bullying, harassment or contract disagreements — without proceeding to the Fair Work Commission or court. It's faster, cheaper and helps preserve working relationships.",
 """
 <h2>What workplace disputes can be mediated?</h2>
 <ul>
   <li>Unfair dismissal and termination disputes</li>
   <li>Bullying, harassment and discrimination complaints</li>
   <li>Employment contract and entitlement disagreements</li>
   <li>Interpersonal conflict between colleagues or with management</li>
   <li>Restructure, redundancy and return-to-work disputes</li>
 </ul>

 <h2>Why mediate workplace disputes early?</h2>
 <p>Because unresolved conflict spreads — it damages morale, productivity and reputation, and can end up at the Fair Work Commission or in court. Early mediation contains the cost and keeps the matter private. For businesses, it's risk management; for employees, it's a fair hearing without a drawn-out fight.</p>

 <div class="callout">
   <h3>Good for business, good for people</h3>
   <p>Mediation delivers neutral, safe conversations where both sides are heard, structured discussion focused on solutions rather than blame, and practical agreements that get workplaces back on track.</p>
 </div>

 <h2>How does workplace mediation work?</h2>
 <p>A neutral mediator meets with the parties (together or separately), helps each side be heard, identifies the real issues, and guides everyone toward a practical agreement. It's confidential and 'without prejudice', so people can speak openly. Where useful, the outcome can be documented in a binding agreement.</p>
 """,
 [("Is workplace mediation confidential?",
   "Yes. Workplace mediation is conducted on a 'without prejudice' basis, meaning discussions generally can't be used later in legal proceedings, which lets both sides speak openly."),
  ("Can mediation prevent a Fair Work claim?",
   "Often, yes. Resolving a dispute early through mediation can prevent it escalating to the Fair Work Commission, saving both time and significant cost."),
  ("Who pays for workplace mediation?",
   "Arrangements vary. Employers often cover the cost as part of resolving a dispute, though it can be shared. You'll have fee clarity from the outset."),
  ("Is the outcome of workplace mediation binding?",
   "The mediation itself is voluntary, but any agreement reached can be documented and made binding, for example as a deed of settlement.")],
 "Workplace Mediation",
 "Resolve it early — <em>before it costs more</em>.",
 "Book a fixed-fee consultation to resolve a workplace dispute through confidential mediation, before it reaches the Fair Work Commission.")

print("\nService pages built.")
import subprocess
print(subprocess.run(["ls","/home/claude/mediations/site"],capture_output=True,text=True).stdout)
