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
      <a href="{BOOK_URL}" class="btn btn-primary">Book a Free Consultation <span class="arr">→</span></a>
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
      <a href="{BOOK_URL}" class="btn btn-primary">Book a Free Consultation <span class="arr">→</span></a>
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
 "Property Settlement Mediation",
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
 "Book a free initial consultation and get a clear, honest view of how mediation can divide your assets fairly — without the cost and delay of court.")

build(
 "divorce-mediation",
 "Divorce Mediation Australia | Divorce Mediators",
 "Resolve property, parenting and financial matters with experienced divorce mediators — faster and cheaper than court. Fixed-fee, confidential, Australia-wide.",
 "Divorce &amp; separation",
 "Divorce Mediation",
 "Ending a marriage means untangling parenting, property and finances at the hardest possible time. Divorce mediation gives you a calm, structured way to agree on all of it — guided by a neutral divorce mediator, in weeks rather than years, and on terms you decide together instead of ones a judge imposes.",
 "Divorce mediation is a confidential process where a neutral divorce mediator helps separating couples reach agreement on parenting, property and financial matters without going to court. It usually resolves in one or two sessions, costs a fraction of litigation, and the agreement can be made legally binding through consent orders or a binding financial agreement.",
 """
 <h2>What is divorce mediation?</h2>
 <p>Divorce mediation is a form of <a href="/family-law-mediation/">family law mediation</a> focused on the issues that arise when a marriage ends — how you'll co-parent, how you'll divide property and superannuation, and how you'll handle ongoing financial support. A neutral, accredited mediator guides the conversation, keeps it constructive, and helps you reach a workable agreement. The mediator doesn't take sides or decide the outcome; they help <em>you</em> decide it. It's worth being clear about one thing up front: the legal divorce itself — formally ending the marriage — is a separate administrative step you apply for through the court. Mediation resolves the disputes that come <em>with</em> the divorce. Many couples handle both at once: they <a href="/online-divorce/">apply for divorce online</a> while resolving parenting and property through mediation.</p>

 <h2>What does a divorce mediator do?</h2>
 <p>A divorce mediator is a neutral third party trained to help two people in conflict reach agreement. A good mediator for divorce will set a clear agenda, make sure both people are heard, test proposals against what's realistic and fair, and keep the focus on solutions rather than blame. Many of our divorce mediators are also experienced family lawyers, so they can give you a grounded sense of where a matter would likely land in court — which often makes agreement easier, because both sides can see the realistic range. What a mediator will not do is give either party legal advice or impose a decision; you remain free to get your own advice alongside the process.</p>

 <h2>How divorce mediation works, step by step</h2>
 <ol>
   <li><strong>Free consultation</strong> — you tell us what you're facing and we give an honest view of whether mediation can help, and how it sits alongside any legal advice you have.</li>
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
 <p>You begin with a free initial consultation, so there are no billing surprises. From there, divorce mediation typically costs a small fraction of a contested court case, and the fee is usually shared between the parties — unlike two sets of lawyers billing by the hour. <a href="/how-much-does-mediation-cost/">See a full breakdown of what mediation costs →</a></p>

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
 "Book a free initial consultation and get an honest view of how divorce mediation can resolve parenting, property and finances — without an unnecessary court fight.")

build(
 "parenting-plan-mediation",
 "Parenting Plan Mediation | Custody Agreements, No Court",
 "Parenting plan mediation helps separated parents agree on living arrangements, time and decisions for the children — calmer than a custody court case.",
 "Parenting &amp; children's arrangements",
 "Parenting Plan Mediation",
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
 "Book a free initial consultation and let an accredited family mediator help you build a parenting plan that works for everyone who matters most.")

build(
 "section-60i-certificates",
 "Section 60I Certificates | Family Dispute Resolution",
 "Need a Section 60I certificate before family court? Accredited practitioners issue certificates through mediation to meet your legal obligations.",
 "Required before parenting court action",
 "Section 60I Certificates",
 "Before you can apply to court for parenting orders, the law requires you to attempt family dispute resolution first — and prove it with a Section 60I certificate. We conduct the mediation and issue the certificate, so you meet your obligations and genuinely try to resolve things at once.",
 "A Section 60I certificate is a document issued by an accredited Family Dispute Resolution Practitioner confirming you attempted mediation before applying to court for parenting orders. Under the Family Law Act 1975 it is generally required to file a parenting application, unless an exemption (such as family violence or urgency) applies.",
 """
 <h2>When do you need a Section 60I certificate?</h2>
 <p>Before you can file an application for parenting orders in the <a href="https://www.fcfcoa.gov.au/fl/fdr" target="_blank" rel="noopener">Federal Circuit and Family Court of Australia</a>, you must make a genuine attempt at family dispute resolution — and prove it with a Section 60I certificate. This is a legal requirement under section 60I of the <a href="https://www.austlii.edu.au/cgi-bin/viewdb/au/legis/cth/consol_act/fla1975114/" target="_blank" rel="noopener">Family Law Act 1975</a>. Without the certificate, the court will not accept your application unless an exemption applies.</p>

 <h2>What are the five types of Section 60I certificate?</h2>
 <p>An accredited Family Dispute Resolution Practitioner (FDRP) issues a certificate that describes what happened when family dispute resolution was attempted. There are five possible outcomes:</p>
 <figure class="tbl"><table><caption>The five Section 60I certificate types</caption>
 <thead><tr><th>Type</th><th>What it means</th><th>Effect on your court application</th></tr></thead>
 <tbody>
 <tr><td>Type 1</td><td>The other party was invited but didn't attend</td><td>Allows you to file in court</td></tr>
 <tr><td>Type 2</td><td>Both attended and genuinely tried to resolve the dispute</td><td>Allows you to file in court</td></tr>
 <tr><td>Type 3</td><td>Both attended, but one or both didn't make a genuine effort</td><td>Allows you to file; effort is on record</td></tr>
 <tr><td>Type 4</td><td>The practitioner assessed it as inappropriate to conduct FDR</td><td>Allows you to file — treated as exempt</td></tr>
 <tr><td>Type 5</td><td>Mediation started but the practitioner determined it should not continue</td><td>Allows you to file — treated as exempt</td></tr>
 </tbody></table></figure>
 <p>A Type 2 outcome — where both parties genuinely tried — is the one you're aiming for, because it often means you've reached agreement and may not need to file at all.</p>

 <h2>When is a certificate not required — the exemptions</h2>
 <p>Not every parenting dispute requires family dispute resolution first. Exemptions apply in specific circumstances:</p>
 <ul>
   <li><strong>Family violence or risk of abuse</strong> — where there is a family violence order or a genuine safety risk to a party or child</li>
   <li><strong>Urgent situations</strong> — where a child is at immediate risk and urgent orders are needed</li>
   <li><strong>Inability to participate</strong> — where one party is incapable of effectively participating (for example, through serious illness)</li>
   <li><strong>Geographical or other impracticability</strong> — where it would be impractical to attend</li>
 </ul>
 <p>If an exemption may apply to your situation, discuss it in your consultation. We'll advise the correct path — including whether a Type 4 certificate is more appropriate. Your safety and your children's safety always come first. Call <strong>000</strong> in an emergency; <strong>1800RESPECT (1800 737 732)</strong> for confidential support. See <a href="/domestic-violence-and-family-law/">family violence and family law</a>.</p>

 <div class="callout">
   <h3>You may not need to file at all</h3>
   <p>Many families attend FDR, reach agreement through mediation, and never go to court. The certificate is there if you need it — but most disputes resolve before it's used.</p>
 </div>

 <h2>How do you get a Section 60I certificate?</h2>
 <ol>
   <li><strong>Engage an accredited FDRP</strong> — only a practitioner accredited under the <a href="https://www.legislation.gov.au/Series/F2008L02247" target="_blank" rel="noopener">Family Law (Family Dispute Resolution Practitioners) Regulations 2008</a> can issue a valid certificate.</li>
   <li><strong>Intake and assessment</strong> — the practitioner meets with each party separately to understand the issues and check suitability.</li>
   <li><strong>Attend family dispute resolution</strong> — you participate in mediation, either jointly or (where appropriate) by shuttle.</li>
   <li><strong>Reach agreement or receive your certificate</strong> — if you resolve the matter, you may formalise it as <a href="/consent-orders-explained/">consent orders</a>. If not, the practitioner issues the appropriate certificate.</li>
 </ol>

 <h2>What does the process cost and how long does it take?</h2>
 <p>Our initial consultation is free and the FDR process itself is conducted at fixed, known cost — far less than a contested parenting hearing, which can run for a year or more. Most families complete intake and the mediation session within a few weeks. Even if agreement isn't reached, having the certificate means you've done everything the law requires and you can move to court without further delay. <a href="/how-much-does-mediation-cost/">See what mediation costs →</a></p>

 <h2>Can a certificate be used by the other party against you?</h2>
 <p>What is said and disclosed in FDR is confidential and cannot generally be used in court proceedings — with limited exceptions for risk to a child or another person. The certificate records the outcome (attended, genuine effort, etc.) — not what was said. The <a href="https://www.fcfcoa.gov.au/fl/fdr" target="_blank" rel="noopener">FCFCOA's family dispute resolution guidance</a> explains the confidentiality framework in full.</p>

 <h2>What if the other parent won't attend?</h2>
 <p>If you invite the other parent and they don't attend, the practitioner can issue a Type 1 certificate — confirming you tried and they refused — and you can proceed to file. Refusal to attend doesn't block your access to the court; it is recorded on the certificate. <a href="/parenting-plan-mediation/">See parenting plan mediation →</a></p>
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
 "Binding Financial Agreements Mediation | Protect Assets",
 "Negotiate a binding financial agreement through mediation — before, during or after a relationship. Protect assets with accredited mediators.",
 "Binding financial agreements",
 "Financial Agreement Mediation",
 "A binding financial agreement sets out how assets and finances are handled if a relationship ends. Mediation is the calm way to negotiate one — whether you're entering a relationship, already in one, or separating — so the terms are genuinely agreed rather than fought over.",
 "A binding financial agreement (BFA) is a private contract between partners that sets out how property, finances and support will be divided if they separate. Mediation helps couples negotiate fair terms, which are then formalised with independent legal advice to make the agreement binding under the Family Law Act.",
 """
 <h2>When can you make a binding financial agreement?</h2>
 <p>Under the <a href="https://www.austlii.edu.au/cgi-bin/viewdb/au/legis/cth/consol_act/fla1975114/" target="_blank" rel="noopener">Family Law Act 1975</a>, BFAs can be made at three stages:</p>
 <ul>
   <li><strong>Before</strong> a marriage or de facto relationship — what people commonly call a prenuptial agreement or prenup</li>
   <li><strong>During</strong> the relationship — to clarify how finances work or protect assets acquired since the relationship began</li>
   <li><strong>After</strong> separation — to finalise property division and support without going to court</li>
 </ul>
 <p>The same framework applies to married and de facto couples, including same-sex partners. The timing affects which section of the Family Law Act applies, but the core requirements are the same.</p>

 <h2>What must a BFA contain to be legally binding?</h2>
 <p>A BFA is more than a piece of paper — strict requirements must be met before it is enforceable. The critical ones:</p>
 <ul>
   <li>It must be in writing and signed by both parties</li>
   <li><strong>Each party must receive independent legal advice</strong> from a different lawyer, covering the agreement's effect on their rights and whether it is to their advantage</li>
   <li>Each lawyer must sign a statement confirming that advice was given</li>
   <li>A copy of both statements must be provided to both parties</li>
 </ul>
 <p>Mediation handles the hardest part — reaching terms both parties genuinely accept. The formal legal steps then make those terms enforceable. We coordinate both so nothing falls through the gaps.</p>

 <h2>BFA vs consent orders — which is right for you?</h2>
 <figure class="tbl"><table><caption>Binding financial agreement vs consent orders — key differences</caption>
 <thead><tr><th></th><th>Binding financial agreement (BFA)</th><th>Consent orders</th></tr></thead>
 <tbody>
 <tr><td>Court approval required</td><td>No — private contract</td><td>Yes — court approves it</td></tr>
 <tr><td>Independent legal advice</td><td>Required for each party</td><td>Not required (but recommended)</td></tr>
 <tr><td>When it can be made</td><td>Before, during or after the relationship</td><td>Only after separation</td></tr>
 <tr><td>Flexibility</td><td>Higher — can exclude some assets</td><td>Court applies just and equitable test</td></tr>
 <tr><td>Typical cost</td><td>Higher — two lawyers required</td><td>Lower — one court filing fee</td></tr>
 <tr><td>Best suited to</td><td>Pre-relationship protection; maximum flexibility after separation</td><td>Most separating couples formalising an agreement</td></tr>
 </tbody></table></figure>
 <p>For most separating couples, <a href="/consent-orders-explained/">consent orders</a> are simpler and cheaper. A BFA is the right choice when you need flexibility a court wouldn't grant, or when you're protecting pre-relationship assets. We help you choose. <a href="/bfa-or-consent-orders/">Compare both in detail →</a></p>

 <h2>What can a BFA cover?</h2>
 <ul>
   <li>The family home and all real property</li>
   <li>Superannuation — splitting or quarantining it</li>
   <li>Savings, investments, shares and businesses</li>
   <li>Debts, mortgages and liabilities</li>
   <li>Spousal maintenance — ongoing financial support</li>
   <li>Pre-relationship and inherited assets</li>
 </ul>
 <p>Note that BFAs cannot deal with parenting arrangements — those must be resolved separately through a <a href="/parenting-plan-mediation/">parenting plan</a> or consent orders.</p>

 <h2>Can a BFA be challenged or overturned?</h2>
 <p>Yes, in limited circumstances. A court can set aside a BFA if there was fraud or non-disclosure, if one party was under duress or couldn't understand it, if proper legal advice wasn't obtained, or if circumstances have changed dramatically (such as a child being born after the agreement). Agreements reached fairly through mediation — where both parties had full disclosure, proper legal advice, and genuine input into the terms — are far less likely to be challenged. That's exactly why mediation is the smarter way to reach the terms first.</p>

 <h2>Why negotiate a BFA through mediation?</h2>
 <p>Because agreements reached adversarially are more likely to breed resentment and face legal challenge later. When both parties understand and genuinely accept the terms — because they negotiated them in a structured, fair process — those terms stick. A mediator also helps both sides avoid common mistakes: overlooking assets, misunderstanding superannuation splits, or agreeing to maintenance terms that won't work in practice. The lawyers then make it binding. <a href="/spousal-support-mediation/">See spousal maintenance mediation →</a> or <a href="/property-settlement-mediation/">property settlement mediation →</a></p>
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
 "Book a free initial consultation to negotiate a fair financial agreement through mediation — with the legal formalisation that makes it binding.")

build(
 "spousal-support-mediation",
 "Spousal Maintenance Mediation | Fair Support, No Court",
 "Resolve spousal maintenance through mediation. Agree on fair, sustainable support without court — accredited mediators, fixed-fee, formalised properly.",
 "Spousal &amp; partner maintenance",
 "Spousal Maintenance Mediation",
 "When one partner can't adequately support themselves after separation, the other may be required to help. Mediation lets you agree on fair, realistic maintenance — based on genuine need and capacity to pay — without a draining court fight.",
 "Spousal maintenance is financial support one partner pays the other after separation when that partner cannot reasonably meet their own needs. Mediation helps couples agree on the amount and duration based on need and capacity to pay, then formalise it in consent orders or a financial agreement.",
 """
 <h2>What is spousal maintenance — and who qualifies?</h2>
 <p>Spousal maintenance is financial support paid by one former partner to the other after separation, where that person cannot adequately meet their own reasonable needs. It is not automatic — entitlement depends on genuine need on one side and genuine capacity to pay on the other. Under the <a href="https://www.austlii.edu.au/cgi-bin/viewdb/au/legis/cth/consol_act/fla1975114/" target="_blank" rel="noopener">Family Law Act 1975</a>, a court (or your mediator) weighs a specific list of factors:</p>
 <ul>
   <li>Age, health and earning capacity of each party</li>
   <li>Whether one party cares for children, and how that affects their ability to work</li>
   <li>Commitments of each party to support themselves and any dependants</li>
   <li>The standard of living that was reasonable during the relationship</li>
   <li>The duration of the marriage or de facto relationship and its financial impact</li>
   <li>Whether either party's earning capacity was impaired by the relationship (for example, a parent who stepped back from their career)</li>
 </ul>

 <h2>Spousal maintenance vs child support — the key difference</h2>
 <p>They are entirely separate. Child support is assessed by <a href="https://www.servicesaustralia.gov.au/child-support" target="_blank" rel="noopener">Services Australia</a> using a formula based on incomes and the care arrangement — it covers the costs of raising children. Spousal maintenance supports the former partner directly. You may be entitled to, or obligated to pay, both at the same time. <a href="/child-support-mediation/">See child support mediation →</a></p>

 <h2>What forms can spousal maintenance take?</h2>
 <figure class="tbl"><table><caption>Types of spousal maintenance arrangements</caption>
 <thead><tr><th>Type</th><th>How it works</th><th>Best suited to</th></tr></thead>
 <tbody>
 <tr><td>Lump sum</td><td>A one-off payment that finalises all maintenance obligations</td><td>Where the payer has capital but limited ongoing income, or where a clean break is preferred</td></tr>
 <tr><td>Periodic payments</td><td>Regular payments (weekly, fortnightly or monthly) for a fixed period</td><td>Where the receiving party needs time to retrain, return to work, or rebuild earning capacity</td></tr>
 <tr><td>Periodic (indefinite)</td><td>Regular payments continuing until further order or specific event</td><td>Age, illness or disability that genuinely limits earning capacity long-term</td></tr>
 <tr><td>Urgent maintenance</td><td>Immediate short-term support while longer-term arrangements are sorted</td><td>Where one party has immediate need before a settlement is finalised</td></tr>
 </tbody></table></figure>
 <p>Mediation lets you design the arrangement that genuinely fits both parties' realities — a court is more constrained in what it can order and less able to tailor payments to individual circumstances.</p>

 <h2>Time limits — urgent maintenance and final applications</h2>
 <p>Spousal maintenance has time limits you cannot ignore:</p>
 <ul>
   <li><strong>Married parties</strong> — you must apply for spousal maintenance within <strong>12 months of the divorce order</strong> becoming final. After that, you generally need the court's permission.</li>
   <li><strong>De facto partners</strong> — you must apply within <strong>24 months of separation</strong>.</li>
   <li><strong>Urgent maintenance</strong> — can be sought at any time while you're still within the time limit, including before a final settlement is reached.</li>
 </ul>
 <p>Mediation is the fastest way to reach an agreed, binding arrangement well inside these windows. <a href="/de-facto-mediation/">See de facto mediation →</a></p>

 <div class="callout">
   <h3>Often resolved alongside property settlement</h3>
   <p>Spousal maintenance and property settlement are separate legal questions, but most couples address them together in a single mediation — which avoids separate proceedings and produces a more coherent overall outcome.</p>
 </div>

 <h2>Can a spousal maintenance agreement be made binding?</h2>
 <p>Yes. Once you reach agreement through mediation, the arrangement can be formalised as <a href="/consent-orders-explained/">consent orders</a> approved by the court, or as a binding financial agreement. Either makes it enforceable — important because it protects both the receiving party (who needs certainty of payment) and the paying party (who needs certainty of their obligation). We handle the formalisation step. <a href="/property-settlement-mediation/">See property settlement mediation →</a></p>

 <h2>What happens if circumstances change — can maintenance be varied?</h2>
 <p>Periodic maintenance orders can be varied or discharged by the court if circumstances change significantly — for example if the receiving party remarries or begins earning a sufficient income, or if the paying party's circumstances change dramatically. Lump-sum arrangements, once paid, generally cannot be clawed back. Mediation can also be used to renegotiate maintenance arrangements, often avoiding a return to court.</p>
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
 "Book a free initial consultation to resolve spousal maintenance through mediation — fairly, sustainably and without court.")

build(
 "child-support-mediation",
 "Child Support Mediation Australia | Resolve It Privately",
 "Resolve child support disputes through mediation — private arrangements, departures from assessment and special expenses, without court.",
 "Child support arrangements",
 "Child Support Mediation",
 "Child support disagreements can poison co-parenting. Mediation gives you a private, practical way to agree on arrangements — including private agreements that go beyond the standard formula — so your children are properly supported and the conflict ends.",
 "Child support mediation helps separated parents resolve disagreements about supporting their children — including private child support agreements, departures from the standard assessment, and how special expenses are shared. It keeps decisions private and cooperative rather than adversarial.",
 """
 <h2>How is child support normally calculated in Australia?</h2>
 <p><a href="https://www.servicesaustralia.gov.au/child-support" target="_blank" rel="noopener">Services Australia</a> administers a formula-based assessment that uses both parents' incomes, the percentage of care each parent provides, and a cost-of-children table based on the number of children and their ages. The formula is designed to be fair in the average case — but most families aren't average, and the standard assessment leaves significant gaps.</p>
 <p>Common things the assessment does <em>not</em> cover:</p>
 <ul>
   <li>Private school fees and uniforms</li>
   <li>Significant medical, dental or therapy costs</li>
   <li>Extracurricular activities (sport, music, tutoring)</li>
   <li>Travel costs for contact arrangements</li>
   <li>Higher costs in the child's early years</li>
 </ul>
 <p>This is the gap mediation fills — building a complete, child-specific arrangement that works alongside the assessment.</p>

 <h2>Private vs binding child support agreements</h2>
 <figure class="tbl"><table><caption>Types of child support agreement</caption>
 <thead><tr><th></th><th>Limited agreement</th><th>Binding agreement</th></tr></thead>
 <tbody>
 <tr><td>Requires independent legal advice</td><td>No</td><td>Yes — each parent must have their own lawyer</td></tr>
 <tr><td>Can depart from the assessment</td><td>Only if the amount equals or exceeds the assessment</td><td>Yes — can be above or below the assessment</td></tr>
 <tr><td>How it's changed</td><td>Either party can end it with 3 months' notice</td><td>Only by court order or a new binding agreement</td></tr>
 <tr><td>Best for</td><td>Topping up the assessment for special expenses</td><td>Comprehensive private arrangements departing from the formula</td></tr>
 </tbody></table></figure>
 <p>For most families, a limited agreement (covering the formula plus agreed special expenses) is the simplest path. A binding agreement suits families with complex or high-cost arrangements. Mediation helps you choose the right structure and agree the terms. <a href="/financial-agreements-mediation/">See financial agreements →</a></p>

 <h2>What can child support mediation actually resolve?</h2>
 <ul>
   <li><strong>Special expenses</strong> — how private school fees, medical costs, and activity expenses are split</li>
   <li><strong>Departures from the assessment</strong> — where the standard formula doesn't reflect the family's actual arrangements</li>
   <li><strong>Changes in circumstances</strong> — loss of employment, relocation, change in care percentage</li>
   <li><strong>Disputes about care percentages</strong> — the assessment depends on how much time each parent has the children</li>
   <li><strong>International arrangements</strong> — where one parent moves overseas</li>
   <li><strong>Enforcement concerns</strong> — addressing recurring non-payment before it becomes entrenched</li>
 </ul>

 <h2>A worked example: where the formula falls short</h2>
 <p>Consider a family with two children at a private school where fees are $15,000 per year per child. The Services Australia assessment covers ordinary costs of children based on a generic table — it doesn't know about private school fees, and won't automatically divide them. Without a separate agreement, one parent typically ends up carrying the entire fee while the other relies on the formula payment.</p>
 <p>In mediation, the parents agree to split school fees 60/40 (reflecting their incomes), add a shared medical account for unplanned health costs, and increase the base payment modestly for the years of highest activity costs. That complete arrangement is formalised as a limited child support agreement and registered with Services Australia. Both parents know exactly where they stand — and the argument over the fee account ends.</p>

 <div class="callout">
   <h3>Pairs naturally with your parenting plan</h3>
   <p>Financial and parenting arrangements are deeply connected — child support depends on the care percentage, which is what the parenting plan sets. Mediating both together in one session produces a consistent, coherent outcome for your children. <a href="/parenting-plan-mediation/">See parenting plan mediation →</a></p>
 </div>

 <h2>What if the other parent won't pay what's owed?</h2>
 <p>Services Australia has collection and enforcement powers for registered assessments — including intercepting tax refunds, registering charges on property, and suspending driver's licences in serious cases. Mediation is most valuable before enforcement becomes necessary: resolving the underlying dispute (often a disagreement about the care percentage or special expenses, not unwillingness to support the children) prevents the conflict recurring. Where enforcement is already underway, mediation can help recalibrate the arrangement so it actually works.</p>
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
 "Book a free initial consultation to resolve child support through mediation, with arrangements that genuinely fit your family.")

build(
 "de-facto-mediation",
 "De Facto Relationship Mediation Australia | Same Rights",
 "Resolve de facto relationship disputes through mediation — property, finances and parenting. De facto partners have similar rights to married couples.",
 "De facto &amp; same-sex relationships",
 "De Facto Mediation",
 "De facto and same-sex partners have substantially the same rights as married couples when a relationship ends. Mediation resolves property, financial and parenting matters the same way — quickly, privately and without court — once your relationship qualifies under the law.",
 "De facto relationship mediation resolves property, financial and parenting disputes for unmarried couples, including same-sex partners. De facto partners have similar rights to married couples under the Family Law Act, and mediation offers the same fast, private, out-of-court path to resolution.",
 """
 <h2>What counts as a de facto relationship under Australian law?</h2>
 <p>You are generally in a de facto relationship if you live with another person on a genuine domestic basis, but are not married to them. Under the <a href="https://www.austlii.edu.au/cgi-bin/viewdb/au/legis/cth/consol_act/fla1975114/" target="_blank" rel="noopener">Family Law Act 1975</a>, a court determines whether a de facto relationship exists by weighing:</p>
 <ul>
   <li>The duration of the relationship</li>
   <li>Whether you lived together and for how long</li>
   <li>The nature and degree of financial dependence or interdependence</li>
   <li>Whether you owned property together</li>
   <li>The degree of commitment to a shared life</li>
   <li>Whether you have children together</li>
   <li>Whether the relationship was registered under a state or territory law</li>
 </ul>
 <p>Same-sex de facto relationships have exactly the same status under Australian federal family law. A minimum period of two years together is generally required to access property rights under the Family Law Act, unless there is a child of the relationship or a party has made significant contributions.</p>

 <h2>De facto vs married — what's actually different?</h2>
 <figure class="tbl"><table><caption>Key differences: de facto vs married separating couples</caption>
 <thead><tr><th></th><th>De facto partners</th><th>Married couples</th></tr></thead>
 <tbody>
 <tr><td>Access to property settlement</td><td>Yes — if relationship qualifies</td><td>Yes</td></tr>
 <tr><td>Superannuation splitting</td><td>Yes</td><td>Yes</td></tr>
 <tr><td>Spousal maintenance</td><td>Yes</td><td>Yes</td></tr>
 <tr><td>Time limit to claim</td><td><strong>2 years from separation</strong></td><td>12 months from divorce order</td></tr>
 <tr><td>Need to prove relationship</td><td>Yes — if disputed</td><td>No — marriage certificate is proof</td></tr>
 <tr><td>Parenting orders</td><td>Yes — same as married</td><td>Yes</td></tr>
 </tbody></table></figure>
 <p>The two-year time limit for de facto property claims is the most important practical difference — it runs from the date of separation, not from any court order. Missing it can mean losing the right to a settlement entirely.</p>

 <h2>Property settlement for de facto couples</h2>
 <p>The same four-step framework used for married couples applies: identify the asset pool, assess contributions (financial and non-financial), consider future needs, and check the outcome is just and equitable. De facto separations often involve untangling finances that were never formally combined — joint accounts, a home owned by one but paid for together, businesses built during the relationship — which can generate real disagreement about what's in the pool and what each party contributed.</p>
 <p>Mediation resolves this without the cost of first proving the relationship's existence in contested court proceedings — because both parties attending mediation are implicitly acknowledging the relationship. <a href="/property-settlement-mediation/">See property settlement mediation →</a></p>

 <h2>What if one partner disputes that a de facto relationship existed?</h2>
 <p>It happens. If the other party claims there was no qualifying relationship, the matter may need to be determined by a court before property rights can be established. Mediation can still help — sometimes an honest conversation with a mediator resolves the dispute about the relationship's nature before it escalates to litigation. Where court proceedings are unavoidable, the property mediation can follow once the relationship question is settled.</p>

 <div class="callout">
   <h3>Protecting your assets before or during a relationship</h3>
   <p>If you want to protect pre-relationship assets or clarify financial arrangements before they become complicated, a <a href="/financial-agreements-mediation/">binding financial agreement (de facto BFA)</a> can be made before, during or after the relationship. It's significantly cheaper to negotiate one now than to fight over assets later.</p>
 </div>

 <h2>De facto parenting arrangements</h2>
 <p>Parenting rights and responsibilities are identical for de facto and married couples — the law focuses on the children, not the parents' relationship status. If you have children and can't agree on arrangements, the same requirement to attempt <a href="/section-60i-certificates/">family dispute resolution</a> before applying to court applies. <a href="/parenting-plan-mediation/">See parenting plan mediation →</a></p>

 <h2>How long does de facto mediation take, and what does it cost?</h2>
 <p>Most de facto property matters resolve in one or two mediation sessions over a few weeks — far faster than a contested court case, which can run for years and cost tens of thousands in legal fees for each party. Mediation is fixed-fee and typically shared, so you know what you're committing to before you start. <a href="/how-much-does-mediation-cost/">See our fee structure →</a></p>
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
 "Book a free initial consultation to resolve your de facto dispute through mediation — property, finances and parenting, all without court.")

build(
 "grandparents-mediation",
 "Grandparents' Rights Mediation | See Your Grandchildren",
 "Grandparents can use mediation to maintain contact with grandchildren after family breakdown. Resolve arrangements respectfully, without court.",
 "Grandparents &amp; extended family",
 "Grandparents' Rights Mediation",
 "When families break down, grandparents can lose contact with grandchildren they love. Australian law recognises children's right to a relationship with people significant to their care — including grandparents — and mediation is the gentlest way to restore and protect that bond.",
 "Grandparents' mediation helps grandparents reach agreement about spending time with their grandchildren after a separation or family conflict. The Family Law Act recognises children's right to maintain relationships with grandparents and other significant people, and mediation resolves this without a contested court case.",
 """
 <h2>Do grandparents have legal rights to see their grandchildren?</h2>
 <p>Australian family law doesn't use the language of "grandparent rights" — instead, it focuses on what is in the best interests of the child. The <a href="https://www.austlii.edu.au/cgi-bin/viewdb/au/legis/cth/consol_act/fla1975114/" target="_blank" rel="noopener">Family Law Act 1975</a> specifically recognises children's right to maintain a relationship with "significant people" in their lives — which expressly includes grandparents and other relatives. Grandparents can apply to the court for parenting orders, and their relationship with the child is a factor the court must consider.</p>
 <p>In practice, the most important thing grandparents can do is attempt mediation before any court action. Litigation against your own children or their ex-partners tends to permanently poison relationships — the one thing grandparents can least afford to lose.</p>

 <h2>When does grandparent contact mediation help?</h2>
 <ul>
   <li>After a parental separation that has cut off contact with one side of the family</li>
   <li>Where a parent has died and the surviving parent is restricting contact</li>
   <li>When a family conflict or estrangement has damaged the relationship</li>
   <li>Where grandparents have been a primary carer and need formal recognition</li>
   <li>When parents are relocating interstate or overseas and ongoing contact needs to be formalised</li>
   <li>Where one grandparent has remarried and step-family dynamics have created barriers</li>
 </ul>

 <h2>How does grandparent mediation work?</h2>
 <p>A neutral, accredited mediator facilitates a conversation between the grandparents and the parent or parents involved, with the focus kept entirely on what is best for the children. The mediator does not take sides — they help everyone move past the grievances and establish a practical arrangement the family can actually maintain.</p>
 <p>Sessions can be face-to-face or online. Where the relationship between grandparents and parents is very strained, shuttle mediation — where the mediator moves between separate rooms — is often the best approach. Many mediations in these situations result in a written contact agreement that can be included in a <a href="/parenting-plan-mediation/">parenting plan</a> or, if needed, formalised as <a href="/consent-orders-explained/">consent orders</a>.</p>

 <figure class="tbl"><table><caption>Grandparent contact mediation vs applying to court</caption>
 <thead><tr><th></th><th>Mediation first</th><th>Straight to court</th></tr></thead>
 <tbody>
 <tr><td>Effect on family relationships</td><td>Rebuilds communication — less adversarial</td><td>Highly adversarial — typically damages relationships permanently</td></tr>
 <tr><td>Cost</td><td>Fixed fee, low — often shared</td><td>High — legal fees on both sides</td></tr>
 <tr><td>Time to outcome</td><td>Weeks</td><td>Months to years</td></tr>
 <tr><td>Focus</td><td>The children's best interests</td><td>Legal arguments and evidence</td></tr>
 <tr><td>Result</td><td>Flexible, agreed arrangement</td><td>Rigid court order</td></tr>
 </tbody></table></figure>

 <div class="callout">
   <h3>The court strongly encourages mediation first</h3>
   <p>Grandparents who apply for parenting orders must (like parents) generally attempt family dispute resolution before the court will accept their application. Mediating first is not just the gentler path — it's usually required.</p>
 </div>

 <h2>What if a parent refuses all contact?</h2>
 <p>This is the hardest situation. Mediation depends on the parent being willing to participate — you cannot force someone to come. If a parent refuses all contact and won't engage in mediation, the grandparent may need to apply to court, but the court will still want evidence that other avenues were tried first.</p>
 <p>Often, though, a parent's refusal reflects fear or grievance rather than an absolute position. A skilled mediator, approaching the situation without pressure or blame, achieves contact arrangements in many cases where the grandparent had been told "there's no hope." The mediator's job is to create a safe space where the parent can say what they actually need — which is rarely "no contact forever."</p>

 <h2>What arrangements can be reached?</h2>
 <p>The arrangements that work best are built around the children's ages, school schedules, and the geography involved. Common outcomes from grandparent mediation include:</p>
 <ul>
   <li>Regular scheduled contact (every fortnight, school holidays, birthdays)</li>
   <li>Video calls where distance is a factor</li>
   <li>Transition arrangements (grandparents collecting children from school)</li>
   <li>Overnight stays for older children</li>
   <li>Inclusion in significant events (Christmas, milestones)</li>
 </ul>
 <p>These arrangements can be written into a <a href="/parenting-plan-mediation/">parenting plan</a> alongside the parents' own arrangements, or formalised separately as consent orders if the relationship requires that level of certainty.</p>
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
 "Book a free initial consultation to restore contact with your grandchildren through respectful, child-focused mediation.")

build(
 "consent-orders",
 "Consent Orders Australia | Legally Binding Agreements",
 "Turn your mediated agreement into legally binding consent orders. We prepare and lodge consent orders for parenting and property — no court hearing required.",
 "Formalising your agreement",
 "Consent Orders",
 "Reaching agreement is the hard part — consent orders make it stick. They turn what you've agreed into legally enforceable court orders, usually without anyone setting foot in a courtroom. We prepare and lodge them for you.",
 "Consent orders are written agreements approved by the Federal Circuit and Family Court of Australia that make your parenting or property arrangements legally binding. You don't attend a hearing — the court reviews your agreement on the papers and, if it's fair, makes it into enforceable orders.",
 """
 <h2>What can consent orders cover?</h2>
 <p>Consent orders are approved by the <a href="https://www.fcfcoa.gov.au/" target="_blank" rel="noopener">Federal Circuit and Family Court of Australia</a> and can cover three broad areas of family law:</p>
 <ul>
   <li><strong>Parenting arrangements</strong> — where children live, time with each parent, decision-making about education, health and religion, handover arrangements, travel and overseas access</li>
   <li><strong>Property and financial matters</strong> — division of real property, superannuation splitting, savings and investments, businesses, debts, and any other assets or liabilities</li>
   <li><strong>Spousal maintenance</strong> — ongoing financial support, whether as periodic payments or a lump sum</li>
 </ul>
 <p>You can apply for consent orders covering some or all of these in a single application. Most separating couples address both parenting and property in the one set of orders. For a complete guide, see <a href="/consent-orders-explained/">consent orders explained →</a></p>

 <h2>How the consent orders process works, step by step</h2>
 <ol>
   <li><strong>Reach agreement</strong> — usually through mediation, though some couples agree directly</li>
   <li><strong>Prepare the application</strong> — the terms of your agreement are drafted into the correct legal form (an Application for Consent Orders and a Minute of Proposed Orders)</li>
   <li><strong>Lodge with the court</strong> — filed through the <a href="https://www.comcourts.gov.au/" target="_blank" rel="noopener">Commonwealth Courts Portal</a>, online, with the relevant filing fee</li>
   <li><strong>Court review</strong> — a registrar reviews the application on the papers (no hearing required in most cases) to check that parenting arrangements are in the children's best interests and that property division is just and equitable</li>
   <li><strong>Orders made</strong> — if satisfied, the court makes the orders; you receive a sealed copy, which is enforceable from that date</li>
 </ol>
 <p>The typical turnaround for uncontested consent order applications ranges from a few weeks to a few months, depending on the court's workload — far faster than a contested hearing, which can take a year or more.</p>

 <h2>Consent orders vs a parenting plan vs a binding financial agreement</h2>
 <figure class="tbl"><table><caption>Choosing the right legal instrument for your agreement</caption>
 <thead><tr><th></th><th>Consent orders</th><th>Parenting plan</th><th>Binding financial agreement (BFA)</th></tr></thead>
 <tbody>
 <tr><td>Legally enforceable</td><td>Yes — court order</td><td>No — but courts consider it</td><td>Yes — private contract</td></tr>
 <tr><td>Court approval required</td><td>Yes</td><td>No</td><td>No</td></tr>
 <tr><td>Independent legal advice required</td><td>Not required (recommended)</td><td>Not required</td><td>Yes — each party must have their own lawyer</td></tr>
 <tr><td>Covers parenting</td><td>Yes</td><td>Yes</td><td>No</td></tr>
 <tr><td>Covers property/finance</td><td>Yes</td><td>No</td><td>Yes</td></tr>
 <tr><td>Flexibility after agreement</td><td>Parenting: can vary if circumstances change; Property: generally final</td><td>High — flexible by agreement</td><td>Can be varied only by a new BFA or court order</td></tr>
 <tr><td>Best for</td><td>Most separating couples</td><td>Flexible parenting co-management</td><td>Pre-relationship protection or maximum financial flexibility</td></tr>
 </tbody></table></figure>
 <p>For the majority of separating couples, consent orders are the right instrument — they combine court-backed enforceability with a straightforward process and no need for each party to retain separate lawyers. <a href="/bfa-or-consent-orders/">Compare BFAs and consent orders in detail →</a></p>

 <h2>What does the court check before making consent orders?</h2>
 <p>The registrar does not rubber-stamp whatever you've agreed. For <strong>parenting orders</strong>, they must be satisfied the arrangements are in the best interests of the children. For <strong>property orders</strong>, the division must be just and equitable. Agreements that appear grossly unfair, involve inadequate disclosure, or don't properly protect the children's interests may be returned for revision. Mediation produces agreements that are inherently more likely to pass this test — because the mediator has already tested their fairness and practicality in the process.</p>

 <div class="callout">
   <h3>What happens if consent orders are breached?</h3>
   <p>Consent orders are enforceable court orders. If parenting orders are breached without reasonable excuse, the aggrieved party can apply to the court for a contravention order — which can result in penalties, make-up time, or changed orders. Property orders are enforceable through the court's execution powers. This is the practical difference between a consent order and a parenting plan.</p>
 </div>

 <h2>Can consent orders be changed after they're made?</h2>
 <p>Property consent orders are generally final — the principle of finality in property settlement means they're difficult to change without showing fraud, non-disclosure, or a significant change in circumstances. Parenting consent orders can be varied if circumstances have changed significantly since they were made (for example, one parent relocating, a child's needs changing, or the existing arrangement breaking down). In both cases, mediation is the first step — most variations are agreed rather than litigated. <a href="/parenting-plan-mediation/">See parenting plan mediation →</a> or <a href="/property-settlement-mediation/">property settlement mediation →</a></p>
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
 "Online Divorce Mediation",
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
 "Book a free initial online consultation and resolve your separation by secure video, with the same accredited mediators and binding outcomes as in person.")

build(
 "workplace-mediation",
 "Workplace Mediation Australia | Resolve Disputes Fast",
 "Nationally accredited mediators resolving workplace disputes — unfair dismissal, bullying, harassment, partnership and executive conflicts. Faster, private and above 90% resolution rate.",
 "Workplace &amp; employment disputes",
 "Workplace Mediation — <em>Resolve It Before It Costs More</em>",
 "A dispute at work rarely stays contained. What begins as one difficult conversation can quickly consume a team, damage a reputation and end up in front of the Fair Work Commission or a court. Our nationally accredited mediators resolve workplace and employment disputes across Australia — often in a single day, with a resolution rate above 90%.",
 "Workplace mediation is a voluntary, confidential process in which a neutral third party — the mediator — helps people in an employment relationship resolve a dispute without going to court or a tribunal. The mediator does not take sides, give evidence or impose a decision. They create a structured, safe conversation that helps each person be heard and guides everyone toward a workable, mutually agreed outcome.",
 """
 <h2>Why workplace disputes are worth resolving early</h2>
 <p>Australian workplaces are heavily regulated, and the systems that deal with employment disputes are designed to encourage resolution before a formal hearing. The <a href="https://www.fwc.gov.au/" target="_blank" rel="noopener">Fair Work Commission</a> reports that around three in four unfair dismissal cases settle at conciliation — well before any hearing. The reasons to resolve early are practical:</p>

 <figure class="tbl"><table><caption>Workplace mediation vs the Fair Work Commission process</caption>
 <thead><tr><th></th><th>Workplace mediation</th><th>Fair Work Commission</th></tr></thead>
 <tbody>
 <tr><td>Timing</td><td>Immediately — at any point in the dispute</td><td>After dismissal or formal complaint; strict time limits apply</td></tr>
 <tr><td>Confidential</td><td>Yes — without prejudice</td><td>Generally no — decisions are published and searchable</td></tr>
 <tr><td>Who controls the outcome</td><td>The parties</td><td>A commissioner or arbitrator</td></tr>
 <tr><td>Preserves working relationships</td><td>Yes — built for this</td><td>Rarely — adversarial by design</td></tr>
 <tr><td>Typical timeframe</td><td>Weeks — often a single session</td><td>Many months, sometimes over a year</td></tr>
 <tr><td>Typical cost per party</td><td>Fixed, transparent, shared</td><td>Legal fees + management time + disruption</td></tr>
 </tbody></table></figure>

 <h2>Types of workplace and employment disputes we mediate</h2>
 <p>Workplace conflict takes many forms, and each has its own legal context and emotional weight. Choose the area closest to your situation for a detailed guide.</p>

 <div class="cards">
   <div class="card">
     <h3><a href="/unfair-dismissal-termination-mediation/" style="color:inherit;text-decoration:none">Unfair Dismissal &amp; Termination Disputes</a></h3>
     <p>Dismissals, forced resignations and redundancy disagreements. How the 21-day Fair Work deadline works and how mediation resolves these claims without a hearing.</p>
     <a href="/unfair-dismissal-termination-mediation/" class="more">Read the guide <span class="arr">→</span></a>
   </div>
   <div class="card">
     <h3><a href="/workplace-bullying-harassment-mediation/" style="color:inherit;text-decoration:none">Workplace Bullying &amp; Harassment</a></h3>
     <p>When repeated unreasonable behaviour creates a health and safety risk. Where mediation helps, when it does not, and how it sits alongside stop-bullying applications.</p>
     <a href="/workplace-bullying-harassment-mediation/" class="more">Read the guide <span class="arr">→</span></a>
   </div>
   <div class="card">
     <h3><a href="/general-protections-discrimination-mediation/" style="color:inherit;text-decoration:none">General Protections &amp; Discrimination Claims</a></h3>
     <p>Adverse action, workplace rights and protected attributes. Tight time limits apply — 21 days in dismissal cases. How conciliation and private mediation can resolve these.</p>
     <a href="/general-protections-discrimination-mediation/" class="more">Read the guide <span class="arr">→</span></a>
   </div>
   <div class="card">
     <h3><a href="/partnership-executive-exit-mediation/" style="color:inherit;text-decoration:none">Partnership &amp; Executive Exit Disputes</a></h3>
     <p>Business partners falling out, directors leaving under strain, senior executives negotiating a dignified exit. Resolving high-stakes separations privately.</p>
     <a href="/partnership-executive-exit-mediation/" class="more">Read the guide <span class="arr">→</span></a>
   </div>
 </div>

 <h2>How workplace mediation works, step by step</h2>
 <ol>
   <li><strong>Book a consultation.</strong> You start with a fixed-fee conversation so you understand your position, your options and whether mediation is the right path. There are no surprises on cost.</li>
   <li><strong>We match you with the right mediator.</strong> Workplace disputes need a mediator who understands employment law and workplace dynamics. Many of our mediators are also experienced lawyers.</li>
   <li><strong>Preparation.</strong> The mediator speaks with each party privately to understand the issues, the interests behind them, and any safety or power-imbalance concerns that need managing.</li>
   <li><strong>The session.</strong> Mediation can run with everyone in the room, or in a shuttle format where the mediator moves between separate rooms. It can be held in person or online.</li>
   <li><strong>Agreement.</strong> In around 90% of our matters, the parties reach agreement in the session itself.</li>
   <li><strong>Making it binding.</strong> We guide you on turning the agreement into an enforceable outcome — a deed of settlement or a formal terms-of-settlement document.</li>
 </ol>
 <p>All discussions are conducted on a without-prejudice basis — what is said in mediation generally cannot be used in later legal proceedings. This confidentiality is what allows people to speak openly and explore settlement.</p>

 <h2>How mediation fits alongside the Fair Work system</h2>
 <p>Private mediation and the Fair Work system work together — they are not alternatives that cancel each other out. Several types of workplace claim must be lodged with the <a href="https://www.fwc.gov.au/" target="_blank" rel="noopener">Fair Work Commission</a> within strict time limits, and the Commission itself offers conciliation. Private mediation can be used:</p>
 <ul>
   <li><strong>Before you lodge</strong> — to try to resolve things directly and avoid the formal process entirely</li>
   <li><strong>Alongside a lodged claim</strong> — to reach a settlement faster and on your own terms</li>
   <li><strong>In situations the Commission does not cover</strong> — interpersonal conflict, team dynamics, executive exits and commercial partnership disputes</li>
 </ul>
 <p>Because deadlines are short — as little as 21 days for an unfair dismissal claim — it is important to get advice quickly so you do not lose a right by waiting. For general information about workplace rights, the <a href="https://www.fairwork.gov.au/" target="_blank" rel="noopener">Fair Work Ombudsman</a> is the primary government source. For work health and safety guidance, see <a href="https://www.safeworkaustralia.gov.au/" target="_blank" rel="noopener">Safe Work Australia</a>.</p>

 <h2>When workplace mediation may not be appropriate</h2>
 <p>We believe strongly in mediation, but we are honest about its limits. Mediation depends on both people being able to participate freely and safely. It may not be the right first step where:</p>
 <ul>
   <li>there is a serious power imbalance that cannot be managed within the process</li>
   <li>there has been violence, serious sexual harassment, or threats that make a safe conversation impossible</li>
   <li>a party is not able to negotiate freely — for example because of intimidation or fear of reprisal</li>
   <li>an urgent legal deadline or a safety risk means a formal application (such as a stop-bullying order) needs to be made first</li>
 </ul>
 <p>In these situations, safety and proper advice come before process. A good mediator will tell you honestly if mediation is not suitable for your matter. If you need support: <strong>1800RESPECT</strong> 1800 737 732 &middot; <strong>Lifeline</strong> 13 11 14 &middot; <strong>Beyond Blue</strong> 1300 22 4636.</p>

 <h2>Can the outcome be made legally binding?</h2>
 <p>Yes. Any agreement reached in workplace mediation can be documented as a deed of settlement — a legally binding contract. The deed records what was agreed, which might include an apology, a change in working arrangements, a payment, a reference, or a commitment to a working protocol. The terms are confidential (unlike a court order or FWC determination) and tailored to what actually resolves the dispute. <a href="/our-fee-structure/">See what mediation costs →</a></p>

 <p style="font-size:.9rem;color:var(--ink-soft);margin-top:32px;font-style:italic">This page is for general information only and does not constitute legal advice. For personalised guidance, please consult a qualified legal professional or accredited mediator.</p>
 """,
 [("What is workplace mediation?",
   "Workplace mediation is a voluntary, confidential process in which a neutral mediator helps people in an employment relationship resolve a dispute without going to court or a tribunal. The mediator does not impose a decision — they help the parties reach their own workable agreement."),
  ("Is workplace mediation legally required in Australia?",
   "Not across the board. Unlike parenting matters, there is no general legal requirement to mediate a workplace dispute. However, the Fair Work Commission actively encourages conciliation and mediation, and courts expect parties to have made genuine attempts to resolve matters before litigating."),
  ("How long does workplace mediation take?",
   "Most workplace mediations are completed in a single session, often within a day. A matter can usually be booked within a few weeks — compared with many months, sometimes over a year, for a contested tribunal or court outcome."),
  ("Is what I say in mediation confidential?",
   "Yes. Mediation is conducted on a without-prejudice basis, meaning offers and admissions made during the process usually cannot be used later in court. This confidentiality is what allows people to speak openly and explore settlement."),
  ("Do I need a lawyer to attend workplace mediation?",
   "No, it is not mandatory. Many people mediate without a lawyer present. That said, getting legal advice before or after mediation is sensible — especially where the amounts or legal rights involved are significant — so you understand the implications of any agreement before signing."),
  ("What does workplace mediation cost?",
   "We use transparent, fixed-fee pricing so you know the cost up front. Fees depend on the complexity and length of the matter, and are typically shared between the parties or as otherwise agreed. See our fee structure page for details.")],
 "Workplace Mediation",
 "Resolve it early — <em>before it costs more</em>.",
 "Book a free initial consultation to resolve a workplace dispute through confidential mediation, before it reaches the Fair Work Commission.")

print("\nService pages built.")
import subprocess
print(subprocess.run(["ls","/home/claude/mediations/site"],capture_output=True,text=True).stdout)
