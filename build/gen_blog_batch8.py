#!/usr/bin/env python3
"""Batch 8: property-settlement-mediation guide, business in divorce, family court process, divorce-without-a-lawyer, how-long-does-a-divorce-take."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, inline_cta, callout, key_takeaway
from authority_sources import cite

# ---- PROPERTY SETTLEMENT MEDIATION GUIDE (absorbs 8) ----
post("property-settlement-mediation-guide",
 "Property Settlement Mediation: How to Prepare & What to Expect (2026)",
 "Property settlement mediation explained: how to prepare, what to expect on the day, what to bring, and how to reach a fair financial agreement without court. 2026 guide.",
 "Property &amp; finances",
 "Property Settlement Mediation: <em>How to Prepare &amp; What to Expect</em>",
 "Property settlement mediation is how most separating couples divide their assets without a court battle. Knowing how to prepare \u2014 and what actually happens on the day \u2014 makes all the difference to the outcome. This guide walks you through it step by step.",
 [("what-is","What is property settlement mediation?"),
  ("when","When should you mediate?"),
  ("prepare","How to prepare"),
  ("bring","What to bring"),
  ("on-the-day","What to expect on the day"),
  ("strategies","Strategies for a fair outcome"),
  ("after","Making the agreement binding")],
 key_takeaway("Property settlement mediation is a structured process where a neutral mediator helps separating partners divide assets, debts and superannuation by agreement. Preparation is everything: gather full financial disclosure, know your asset pool, and decide your priorities in advance. Most matters resolve in one session, and the agreement is then made binding through consent orders or a financial agreement.")
 + """
<h2 id="what-is">What is property settlement mediation?</h2>
<p>Property settlement mediation is a focused form of <a href="/family-law-mediation/">mediation</a> dealing specifically with the financial side of separation \u2014 dividing the property, assets, debts and superannuation. A neutral mediator guides you and your former partner through the issues and helps you reach a fair, workable agreement, applying the same <a href="/what-am-i-entitled-to-in-a-separation-in-australia/">four-step framework</a> under the <a href='https://www.austlii.edu.au/cgi-bin/viewdb/au/legis/cth/consol_act/fla1975114/' target='_blank' rel='noopener'>Family Law Act 1975</a> a court would use, but in a fraction of the time and cost.</p>
"""
 + inline_cta("Ready to divide assets fairly without a court fight? Book a property settlement mediation consultation.")
 + """
<h2 id="when">When should you mediate?</h2>
<p>The best time is once you both accept the relationship is over and you have a reasonable picture of the asset pool \u2014 but before positions harden or legal costs mount. You don't need to have everything figured out; that's what the process is for. Earlier is almost always better: it protects the asset pool from being eroded by prolonged conflict and legal fees. <a href="/property-settlement-after-separation/">See the time limits that apply \u2192</a></p>

<h2 id="prepare">How to prepare</h2>
<ol>
  <li><strong>Gather full financial disclosure</strong> \u2014 both parties have a <a href='https://www.fcfcoa.gov.au/fl/duty-disclosure' target='_blank' rel='noopener'>duty of full and frank financial disclosure</a>, so disclose everything. Hiding assets doesn't just derail the mediation; it can see a later settlement overturned.</li>
  <li><strong>Build the asset pool picture</strong> \u2014 list all assets, debts and superannuation, joint and individual.</li>
  <li><strong>Get valuations where needed</strong> \u2014 for property, businesses, or defined-benefit super.</li>
  <li><strong>Know your priorities</strong> \u2014 separate what you genuinely need from what you'd prefer.</li>
  <li><strong>Consider your future needs</strong> \u2014 housing, earning capacity, care of children.</li>
</ol>
"""
 + callout("Disclosure is non-negotiable",
   "Both parties have a <a href='https://www.fcfcoa.gov.au/fl/duty-disclosure' target='_blank' rel='noopener'>duty of full and frank financial disclosure</a>. Hiding assets doesn't just sink the mediation \u2014 it can lead to a later settlement being overturned. Go in transparent.")
 + """
<h2 id="bring">What to bring</h2>
<ul>
  <li>Recent bank, loan and credit card statements</li>
  <li>Superannuation statements for both parties</li>
  <li>Property valuations or appraisals</li>
  <li>Tax returns and payslips</li>
  <li>Details of any businesses, trusts or investments</li>
  <li>A list of significant assets and debts, with rough values</li>
</ul>

<h2 id="on-the-day">What to expect on the day</h2>
<p>After an initial intake, the mediator will usually open jointly (or keep you in separate rooms if you prefer \u2014 see <a href="/shuttle-mediation-guide/">shuttle mediation</a>), confirm the issues, and work methodically through the asset pool and how to divide it. Expect to negotiate, to hear the other perspective, and to focus on options rather than blame. Most property matters resolve in a single full-day session, ending with a documented Heads of Agreement. <a href="/preparing-for-mediation/">See how to prepare \u2192</a></p>
"""
 + inline_cta("Walk in prepared and walk out with an agreement. We'll get you ready \u2014 book a consultation today.")
 + """
<h2 id="strategies">Strategies for a fair outcome</h2>
<ul>
  <li><strong>Stay focused on the future</strong>, not on re-fighting the relationship.</li>
  <li><strong>Be realistic</strong> \u2014 anchor to the four-step framework, not to what you wish you were owed.</li>
  <li><strong>Think in terms of the whole pool</strong>, not winning individual items.</li>
  <li><strong>Weigh super properly</strong> against other assets \u2014 don't trade it away cheaply.</li>
  <li><strong>Keep emotion in check</strong> \u2014 calm, factual negotiation gets better results.</li>
</ul>

<h2 id="after">Making the agreement binding</h2>
<p>An agreement reached in mediation isn't automatically binding \u2014 you formalise it afterwards through <a href="/consent-orders-explained/">consent orders</a> (court-approved) or a <a href="/binding-financial-agreements-guide/">binding financial agreement</a>. This step closes off future claims and gives both parties certainty. We help you take the agreement through to a binding outcome. <a href="/property-settlement-mediation/">See our property settlement mediation service \u2192</a></p>
"""
 ,
 [("How do I prepare for property settlement mediation?",
   "Gather full financial disclosure, build a clear picture of the asset pool, get valuations where needed, know your priorities, and consider your future needs."),
  ("What should I bring to property mediation?",
   "Bank and loan statements, superannuation statements, property valuations, tax returns and payslips, details of businesses or trusts, and a list of assets and debts with values."),
  ("How long does property settlement mediation take?",
   "Most property matters resolve in a single full-day session, ending with a documented Heads of Agreement, though complex pools may need more time."),
  ("Is the mediated property agreement legally binding?",
   "Not automatically. You formalise it afterwards through consent orders or a binding financial agreement to make it binding and close off future claims."),
  ("What happens if my ex hides assets in mediation?",
   "Both parties have a duty of full disclosure. Hiding assets can derail the mediation and can lead to a later settlement being overturned by a court.")],
 [("property-settlement-mediation","Property Settlement Mediation"),
  ("property-settlement-after-separation","Property Settlement After Separation"),
  ("what-am-i-entitled-to-in-a-separation-in-australia","What Am I Entitled To?"),
  ("consent-orders-explained","Consent Orders Explained"),
  ("superannuation-and-divorce","Superannuation & Divorce"),
  ("preparing-for-mediation","Preparing for Mediation")],
 read_min=10)
print("property-settlement-mediation-guide built")

# ---- BUSINESS IN DIVORCE (absorbs 3) ----
post("business-in-divorce",
 "What Happens to a Business in a Divorce in Australia? (2026)",
 "What happens to a business in a divorce in Australia? How businesses, companies and trusts are valued and divided in a property settlement \u2014 and how to protect yours.",
 "Property &amp; finances",
 "What Happens to a Business in a Divorce in Australia?",
 "A business is often the most valuable \u2014 and most complex \u2014 asset in a separation. It forms part of the property pool, must be valued, and can be divided in various ways. This guide explains how businesses, companies and trusts are treated in a divorce, and how to protect a business you've built.",
 [("part-of-pool","Is a business part of the property pool?"),
  ("valuation","How is a business valued?"),
  ("divided","How is a business divided?"),
  ("trusts","Companies and trusts"),
  ("protect","How to protect your business"),
  ("mediation","Why mediation suits business matters")],
 key_takeaway("A business is treated as property in a divorce and forms part of the asset pool. It must be valued (often by an expert), and the value is then factored into the overall division \u2014 usually by one party retaining the business and offsetting its value against other assets, rather than splitting the business itself. Companies and trusts add complexity. Mediation is well suited to keeping a business intact.")
 + f"""
<h2 id="part-of-pool">Is a business part of the property pool?</h2>
<p>Yes. Under the {cite("family_law_act")}, a business \u2014 whether a sole trader operation, a company, or an interest in a partnership \u2014 forms part of the asset pool to be divided, just like the family home or superannuation. This is true even if only one partner runs it, and even if it was started before the relationship (though the timing and contributions affect how it's treated). <a href="/property-settlement-after-separation/">See how the asset pool works \u2192</a></p>
"""
 + inline_cta("Worried about what happens to the business you've built? Get clear, practical advice in a consultation.")
 + """
<h2 id="valuation">How is a business valued?</h2>
<p>Valuing a business is rarely as simple as looking at its bank balance. Depending on the business, valuation may consider net assets, future earning capacity, goodwill, and comparable sales. For anything beyond the simplest operation, an independent expert valuation is usually needed (the <a href='https://www.fcfcoa.gov.au/' target='_blank' rel='noopener'>Federal Circuit and Family Court</a> deals with complex business valuations regularly) \u2014 and the parties may need to agree on a single expert to avoid duelling valuations. Getting the value right matters enormously, because it drives the whole settlement.</p>

<h2 id="divided">How is a business divided?</h2>
<p>Contrary to what many fear, the business itself usually isn't carved up or sold. The far more common outcome is that one partner <strong>retains the business</strong> and its value is <strong>offset</strong> against other assets \u2014 for example, the business-owning partner keeps the company while the other receives a larger share of the home or superannuation. This keeps the business intact and operating. Where that's not possible, options include a payout over time or, as a last resort, sale.</p>
"""
 + callout("Keeping the business running matters",
   "Courts and mediators generally try to avoid killing the goose that lays the golden egg. An outcome that destroys a viable business usually serves no one \u2014 so offsetting its value is almost always preferred to splitting or selling it.")
 + """
<h2 id="trusts">Companies and trusts</h2>
<p>Where assets are held in a company or family trust, things get more complex \u2014 but they're not out of reach. The court can look behind these structures to determine who really controls and benefits from the assets, and can treat them as part of the pool or as a financial resource. Structures set up to shield assets from a settlement rarely work as intended. <a href="/property-settlement-after-separation/">See the duty of disclosure \u2192</a></p>

<h2 id="protect">How to protect your business</h2>
<ul>
  <li><strong>A binding financial agreement</strong> \u2014 a <a href="/binding-financial-agreements-guide/">BFA</a> (prenup or during the relationship) can quarantine a business.</li>
  <li><strong>Clear records</strong> \u2014 keep business and personal finances separate and well documented.</li>
  <li><strong>Realistic valuation</strong> \u2014 engage early with a credible expert.</li>
  <li><strong>Mediate, don't litigate</strong> \u2014 a court fight can damage the very business you're trying to protect.</li>
</ul>
"""
 + inline_cta("Protect the business you've worked for. We'll help you reach a fair outcome that keeps it intact.")
 + """
<h2 id="mediation">Why mediation suits business matters</h2>
<p>Business-related settlements are exactly where <a href="/property-settlement-mediation/">mediation</a> shines. It's confidential \u2014 so sensitive financial details stay private rather than entering the public court record. It's faster \u2014 so the business isn't left in limbo for years. And it's flexible \u2014 letting you craft creative solutions (offsets, staged payouts, ongoing arrangements) that a court might not order. For business owners, mediation is almost always the smarter path. <a href="/mediate-or-litigate/">Compare mediation and court \u2192</a></p>
"""
 ,
 [("Is my business part of the property pool in a divorce?",
   "Yes. A business \u2014 sole trader, company or partnership interest \u2014 forms part of the asset pool, even if only one partner runs it or it started before the relationship."),
  ("How is a business valued in a divorce?",
   "Through factors like net assets, future earning capacity and goodwill, usually requiring an independent expert valuation for anything beyond the simplest operation."),
  ("Will my business be sold or split in a divorce?",
   "Usually not. The common outcome is one partner retaining the business and offsetting its value against other assets, keeping the business intact and operating."),
  ("Can assets held in a trust or company be divided?",
   "Often yes. Courts can look behind company and trust structures to determine real control and benefit, and treat the assets as part of the pool or a financial resource."),
  ("How can I protect my business from a divorce?",
   "A binding financial agreement can quarantine a business, alongside clear separate record-keeping, credible early valuation, and resolving matters through mediation rather than court.")],
 [("property-settlement-after-separation","Property Settlement"),
  ("property-settlement-mediation","Property Settlement Mediation"),
  ("binding-financial-agreements-guide","Binding Financial Agreements"),
  ("what-am-i-entitled-to-in-a-separation-in-australia","What Am I Entitled To?"),
  ("superannuation-and-divorce","Superannuation & Divorce"),
  ("mediate-or-litigate","Mediate or Litigate?")],
 read_min=9)
print("business-in-divorce built")

# ---- FAMILY COURT PROCESS (absorbs 8) ----
post("family-court-process",
 "The Family Court Process in Australia: What to Expect (2026)",
 "How the family court process works in Australia: from pre-action steps to final hearing, the role of the Federal Circuit and Family Court, timeframes, and why mediation comes first.",
 "The process",
 "The Family Court Process in Australia: <em>What to Expect</em>",
 "If your matter can't be resolved by agreement, understanding the court process removes some of the fear. This guide walks through the family court system in Australia \u2014 the pre-action steps, what happens at each stage, how long it takes, and why mediation is required first and remains the better option throughout.",
 [("court","The Federal Circuit and Family Court"),
  ("pre-action","Pre-action procedures come first"),
  ("stages","The stages of a court case"),
  ("how-long","How long does it take?"),
  ("final-hearing","The final hearing"),
  ("orders","Procedural and final orders"),
  ("mediation-throughout","Mediation throughout the process")],
 key_takeaway("Family law matters are handled by the Federal Circuit and Family Court of Australia. Before filing, you must complete pre-action procedures \u2014 including attempting dispute resolution. A contested case moves through interim hearings and procedural steps to a final hearing, often taking one to three years. Mediation is required before parenting applications and can resolve matters at any stage, even after proceedings begin.")
 + f"""
<h2 id="court">The Federal Circuit and Family Court</h2>
<p>Since 2021, family law matters in Australia (outside Western Australia) are handled by the {cite("fcfcoa")} \u2014 a single court with a streamlined structure designed to resolve matters faster and encourage settlement. Western Australia has its own {cite("family_court_wa")}. The court deals with parenting, property and financial disputes that can't be resolved by agreement.</p>
"""
 + inline_cta("Facing the prospect of court? Mediation can often resolve things first \u2014 and faster. Talk to us.")
 + f"""
<h2 id="pre-action">Pre-action procedures come first</h2>
<p>You can't simply file and head to a hearing. The court requires <strong>pre-action procedures</strong>: genuine attempts to resolve the dispute first, exchanging relevant documents, and \u2014 for parenting matters \u2014 attempting family dispute resolution and obtaining a <a href="/section-60i-certificates/">Section 60I certificate</a>. Skipping these steps without an exemption can have consequences, including costs orders. <a href="/is-family-law-mediation-compulsory/">See the pre-court mediation requirement \u2192</a></p>

<h2 id="stages">The stages of a court case</h2>
<ol>
  <li><strong>Filing</strong> \u2014 the application and supporting documents are lodged.</li>
  <li><strong>First court date</strong> \u2014 the matter is assessed and directions are given.</li>
  <li><strong>Interim hearings</strong> \u2014 temporary orders may be made for urgent issues.</li>
  <li><strong>Procedural steps</strong> \u2014 disclosure, valuations, family reports, and further dispute resolution.</li>
  <li><strong>Final hearing</strong> \u2014 if still unresolved, a judge hears the evidence and decides.</li>
</ol>
<p>Notably, the court actively pushes parties toward settlement at every stage \u2014 most matters resolve before a final hearing.</p>
"""
 + callout("Most cases settle before final hearing",
   "Even once proceedings start, the overwhelming majority of family law matters settle by agreement before a judge ever decides. That's why resolving early \u2014 ideally through mediation \u2014 saves enormous time and cost.")
 + """
<h2 id="how-long">How long does it take?</h2>
<p>A contested family law matter commonly takes one to three years from filing to a final hearing, depending on complexity and court workload. Interim issues may be dealt with sooner, but the full process is slow \u2014 one of the strongest arguments for resolving by agreement. <a href="/how-long-does-mediation-take/">Compare that to weeks for mediation \u2192</a></p>

<h2 id="final-hearing">The final hearing</h2>
<p>If a matter reaches a final hearing, both parties present evidence and are cross-examined, and the judge makes binding orders. It's the most expensive, stressful and uncertain stage \u2014 and you hand the decision entirely to the judge. Very few matters reach this point, and for good reason. <a href="/mediate-or-litigate/">See why mediation is the smarter path \u2192</a></p>
"""
 + inline_cta("Don't let your matter drag through years of court. Most disputes can resolve far sooner. Book a consultation.")
 + """
<h2 id="orders">Procedural and final orders</h2>
<p>Throughout a case the court makes <strong>procedural orders</strong> (directions managing the case \u2014 timetables, disclosure, reports) and ultimately <strong>final orders</strong> (the binding decision resolving the dispute). Interim orders can also be made along the way for urgent matters. Breaching court orders has real consequences \u2014 see <a href="/consent-orders-explained/">our guide on orders and breaches</a>.</p>

<h2 id="mediation-throughout">Mediation throughout the process</h2>
<p>Here's the key point: mediation isn't only a pre-court step \u2014 it remains available, and valuable, at every stage. Many matters that begin in court are resolved through mediation partway through, ending the litigation early and saving the parties from a final hearing. It's never too late to step off the court path and resolve by agreement. <a href="/family-law-mediation/">See how mediation works \u2192</a></p>
"""
 ,
 [("Which court handles family law in Australia?",
   "The Federal Circuit and Family Court of Australia handles family law matters outside WA, which has its own Family Court of Western Australia."),
  ("What are pre-action procedures?",
   "Steps required before filing: genuinely attempting to resolve the dispute, exchanging documents, and \u2014 for parenting matters \u2014 attempting family dispute resolution and getting a Section 60I certificate."),
  ("How long does a family court case take?",
   "A contested matter commonly takes one to three years from filing to final hearing, depending on complexity and court workload. Most settle before then."),
  ("Do most family law cases go to a final hearing?",
   "No. The overwhelming majority settle by agreement before a judge decides, which is why resolving early through mediation saves significant time and cost."),
  ("Can I use mediation after court proceedings have started?",
   "Yes. Mediation remains available at every stage and frequently resolves matters partway through, ending the litigation before a final hearing.")],
 [("mediate-or-litigate","Mediate or Litigate?"),
  ("is-family-law-mediation-compulsory","Is Mediation Compulsory?"),
  ("section-60i-certificates","Section 60I Certificates"),
  ("how-long-does-mediation-take","How Long Does Mediation Take?"),
  ("consent-orders-explained","Consent Orders Explained"),
  ("family-law-mediation","Family Law Mediation")],
 read_min=10)
print("family-court-process built")

# ---- DIVORCE WITHOUT A LAWYER (absorbs 2) ----
post("divorce-without-a-lawyer",
 "Divorce Without a Lawyer in Australia: Is It Possible? (2026)",
 "Can you get divorced without a lawyer in Australia? Yes \u2014 here's how to do the divorce application yourself, when you still need help, and how mediation replaces costly litigation.",
 "Divorce",
 "Divorce Without a Lawyer in Australia: <em>Is It Possible?</em>",
 "Yes \u2014 you can get divorced without a lawyer in Australia, and many people do. The divorce application is designed to be done yourself. But 'divorce' and 'sorting out property and children' are different things, and knowing where you can DIY and where you shouldn't will save you money and mistakes.",
 [("can-you","Can you really DIY a divorce?"),
  ("application","Doing the divorce application yourself"),
  ("where-careful","Where you need to be careful"),
  ("property","Property and parenting are different"),
  ("mediation","Mediation: the middle path"),
  ("when-lawyer","When you should get advice")],
 key_takeaway("You can do the divorce application yourself in Australia \u2014 it's lodged online and designed for self-representation. But ending the marriage is separate from dividing property and sorting parenting, which carry real risk if you DIY badly. Mediation is the cost-effective middle path: it resolves the substantive issues without each side running up large legal bills.")
 + """
<h2 id="can-you">Can you really DIY a divorce?</h2>
<p>For the divorce itself \u2014 the legal ending of the marriage \u2014 yes, absolutely. The application is designed to be completed by ordinary people without legal training, and a large share of divorces are done without a lawyer, using the <a href='https://www.fcfcoa.gov.au/fl/divorce' target='_blank' rel='noopener'>court's divorce resources</a>. Where people get into trouble is assuming the same applies to property and parenting, which are separate and far higher-stakes. <a href="/how-to-get-a-divorce-in-australia-a-step-by-step-guide/">See the step-by-step divorce guide \u2192</a></p>
"""
 + inline_cta("Want to keep costs down but get it right? Mediation handles the hard part affordably. Book a consultation.")
 + f"""
<h2 id="application">Doing the divorce application yourself</h2>
<p>The {cite("fcfcoa")} provides the Application for Divorce through the Commonwealth Courts Portal, with guidance on each step. If you meet the eligibility criteria (12 months' separation, residency) and your situation is straightforward, you can complete it, pay the fee, and \u2014 for joint applications with no children under 18 \u2014 often avoid attending court entirely. <a href="/cost-of-divorce-in-australia/">See what it costs \u2192</a></p>

<h2 id="where-careful">Where you need to be careful</h2>
<p>DIY is fine for a clean, agreed divorce. Be more cautious if: there are children under 18 (the court must be satisfied about their care); you can't locate your spouse; service is contested; or there's any complexity. In those cases a little guidance prevents costly delays and rejected applications.</p>
"""
 + callout("Divorce \u2260 settlement",
   "The single biggest mistake is thinking the divorce sorts everything out. It doesn't. It only ends the marriage \u2014 and it actually starts a 12-month clock to finalise property. Don't let DIY divorce lull you into missing that.")
 + """
<h2 id="property">Property and parenting are different</h2>
<p>This is where DIY gets risky. Dividing property and agreeing parenting arrangements have lasting financial and personal consequences, and informal "we'll just sort it out ourselves" arrangements often unravel \u2014 leaving you exposed to future claims. You don't necessarily need two lawyers billing by the hour, but you do need the agreement done properly and made binding through <a href="/consent-orders-explained/">consent orders</a>. <a href="/property-settlement-after-separation/">See property settlement \u2192</a></p>

<h2 id="mediation">Mediation: the middle path</h2>
<p>Between expensive lawyer-led litigation and risky DIY sits mediation \u2014 and it's the sweet spot for most people. A neutral mediator helps you reach a fair agreement on property and parenting without each side lawyering up, then you formalise it. You stay in control, keep costs low, and get a binding, proper outcome. It's how you "do it yourself" on the hard parts without doing it blind. <a href="/family-law-mediation/">See family law mediation \u2192</a></p>
"""
 + inline_cta("The smart middle path: resolve property and parenting through mediation, no court war. Book today.")
 + """
<h2 id="when-lawyer">When you should get advice</h2>
<p>Get legal advice where the stakes or complexity are high: significant or complex assets, a business or trust, superannuation splitting, family violence, or where you and your ex are far apart. Even then, advice plus mediation usually beats full litigation on cost. The goal isn't to avoid all professional help \u2014 it's to use it efficiently where it counts. <a href="/collaborative-family-lawyers/">See collaborative family law \u2192</a></p>
"""
 ,
 [("Can I get divorced without a lawyer in Australia?",
   "Yes. The divorce application is designed for self-representation and lodged online. Many people do it themselves, especially for straightforward, agreed divorces."),
  ("Do I need a lawyer to divide property?",
   "Not necessarily two lawyers billing hourly, but property division has lasting consequences and should be done properly and made binding through consent orders. Mediation is the cost-effective path."),
  ("Does a DIY divorce sort out property and children?",
   "No. The divorce only ends the marriage. Property and parenting are separate, and divorce actually starts a 12-month clock to finalise property matters."),
  ("When should I get legal advice for my divorce?",
   "Where stakes or complexity are high \u2014 significant or complex assets, a business or trust, superannuation, family violence, or where you and your ex are far apart."),
  ("What's the cheapest way to handle a separation properly?",
   "Mediation \u2014 it resolves property and parenting without each side running up large legal bills, then the agreement is formalised through consent orders or a financial agreement.")],
 [("how-to-get-a-divorce-in-australia-a-step-by-step-guide","How to Get a Divorce"),
  ("cost-of-divorce-in-australia","Cost of Divorce"),
  ("property-settlement-after-separation","Property Settlement"),
  ("consent-orders-explained","Consent Orders Explained"),
  ("family-law-mediation","Family Law Mediation"),
  ("mediate-or-litigate","Mediate or Litigate?")],
 read_min=9)
print("divorce-without-a-lawyer built")

# ---- HOW LONG DOES A DIVORCE TAKE (absorbs 1) ----
post("how-long-does-a-divorce-take",
 "How Long Does a Divorce Take in Australia? (2026 Guide)",
 "How long does a divorce take in Australia? The 12-month separation rule, processing times, when the divorce is final, and why property and parenting take their own timeline.",
 "Divorce",
 "How Long Does a Divorce Take in Australia?",
 "From the 12-month separation requirement to the month-and-a-day after the order, the divorce itself runs on a fairly predictable timeline. But property and parenting follow their own clock entirely. Here's how long each part really takes \u2014 and how to avoid the delays that catch people out.",
 [("overview","The short answer"),
  ("12-months","The 12-month separation rule"),
  ("processing","Processing and hearing times"),
  ("final","When the divorce becomes final"),
  ("property-timeline","Property and parenting timelines"),
  ("speed-up","How to avoid delays")],
 key_takeaway("Before you can even apply, you must be separated for at least 12 months. Once filed, a divorce is typically processed within a few months, and the divorce order takes effect one month and one day after it's granted. Property and parenting matters run on separate timelines \u2014 quick by agreement through mediation, or one to three years if contested in court.")
 + """
<h2 id="overview">The short answer</h2>
<p>There are really two timelines. The <strong>divorce itself</strong>: 12 months' separation before applying, then a few months to process, then one month and a day until it's final. The <strong>property and parenting side</strong>: as little as a few weeks if you mediate, or one to three years if it's fought in court. Most of the "how long does divorce take" frustration comes from conflating the two.</p>
"""
 + inline_cta("Want the property and parenting side resolved in weeks, not years? Mediation makes it possible. Book now.")
 + """
<h2 id="12-months">The 12-month separation rule</h2>
<p>You can't apply for divorce until you've been separated for at least 12 months and one day, per the <a href='https://www.austlii.edu.au/cgi-bin/viewdb/au/legis/cth/consol_act/fla1975114/' target='_blank' rel='noopener'>Family Law Act 1975</a>. This is the biggest single component of the timeline, and it can't be shortcut. The good news is you don't have to wait for the divorce to sort out property and parenting \u2014 those can (and usually should) be resolved during the separation period. <a href="/separation-guide/">See our separation guide \u2192</a></p>

<h2 id="processing">Processing and hearing times</h2>
<p>Once you file, processing typically takes a few months, depending on <a href='https://www.fcfcoa.gov.au/' target='_blank' rel='noopener'>court</a> workload. Whether you need to attend a hearing depends on your situation \u2014 joint applications with no children under 18 often proceed without anyone attending, while sole applications involving children may require a brief hearing. <a href="/how-to-get-a-divorce-in-australia-a-step-by-step-guide/">See the full application process \u2192</a></p>
"""
 + callout("The one-month-and-a-day rule",
   "After a divorce is granted, it doesn't take effect immediately \u2014 it becomes final one month and one day later. Only then are you legally divorced and free to remarry, so factor this into any plans.")
 + """
<h2 id="final">When the divorce becomes final</h2>
<p>The divorce order takes legal effect one month and one day after it is granted. At that point you'll be able to access the divorce certificate, and you're free to remarry. Remember, too, that this final date starts the <strong>12-month clock</strong> to apply for property orders \u2014 a deadline people frequently overlook. <a href="/property-settlement-after-separation/">See property time limits \u2192</a></p>

<h2 id="property-timeline">Property and parenting timelines</h2>
<p>This is where the timeline varies wildly, and where you have the most control. Resolved by agreement through <a href="/property-settlement-mediation/">mediation</a>, property and parenting can be settled in a matter of weeks. Fought through the <a href="/family-court-process/">court system</a>, the same issues can take one to three years. The choice of path \u2014 far more than the divorce paperwork \u2014 determines how long your separation really takes to finalise. <a href="/how-long-does-mediation-take/">See how long mediation takes \u2192</a></p>
"""
 + inline_cta("The divorce clock you can't change \u2014 but the rest you can. Resolve it fast through mediation. Book today.")
 + """
<h2 id="speed-up">How to avoid delays</h2>
<ol>
  <li><strong>Use the separation period productively</strong> \u2014 resolve property and parenting before the divorce is even granted.</li>
  <li><strong>Apply jointly where possible</strong> \u2014 it avoids service and often avoids a hearing.</li>
  <li><strong>Get the application right</strong> \u2014 errors cause rejections and delays.</li>
  <li><strong>Mediate the substantive issues</strong> \u2014 it's the single biggest time-saver.</li>
  <li><strong>Watch the 12-month property deadline</strong> after the divorce is final.</li>
</ol>
"""
 ,
 [("How long does a divorce take in Australia?",
   "You must be separated 12 months before applying, then processing takes a few months, and the divorce becomes final one month and one day after it's granted."),
  ("Do I have to wait 12 months to get divorced?",
   "Yes. You must be separated for at least 12 months and one day before you can apply. However, you can resolve property and parenting during that time."),
  ("When is a divorce final in Australia?",
   "The divorce order takes effect one month and one day after it's granted. Only then are you legally divorced and free to remarry."),
  ("Why do property matters take longer than the divorce?",
   "Because property and parenting run on a separate timeline. By agreement through mediation they take weeks; contested in court they can take one to three years."),
  ("How can I make my divorce faster?",
   "Resolve property and parenting during the separation period, apply jointly where possible, get the application right, and mediate the substantive issues to avoid court delays.")],
 [("how-to-get-a-divorce-in-australia-a-step-by-step-guide","How to Get a Divorce"),
  ("how-long-does-mediation-take","How Long Does Mediation Take?"),
  ("property-settlement-after-separation","Property Settlement"),
  ("family-court-process","The Family Court Process"),
  ("separation-guide","Separation Guide"),
  ("cost-of-divorce-in-australia","Cost of Divorce")],
 read_min=8)
print("how-long-does-a-divorce-take built")
