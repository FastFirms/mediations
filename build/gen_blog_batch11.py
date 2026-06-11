#!/usr/bin/env python3
"""Batch 11 — supporting-cluster articles that feed the commercial hubs.
Each targets a specific informational query from the SEO deployment plan and
links back into its money page with exact/partial-match anchors."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, inline_cta, key_takeaway
from authority_sources import cite

# ============================================================
# COST CLUSTER
# ============================================================
post("who-pays-for-mediation",
 "Who Pays for Mediation in Australia? (2026 Guide)",
 "Who pays for mediation in family law? How the fee is usually split, when one party pays, free options, and how mediation costs compare with court. 2026 guide.",
 "Costs &amp; fees",
 "Who Pays for Mediation in Australia? <em>How the Fee Is Split</em>",
 "In most family mediations the fee is shared between the two parties — but it isn't a hard rule. This guide explains how mediation costs are usually divided, when one person pays, what free options exist, and how it all compares with the cost of court.",
 [("default","The usual rule: shared equally"),
  ("when-one-pays","When one party pays more (or all)"),
  ("free","Free and subsidised mediation"),
  ("what-included","What the fee actually covers"),
  ("vs-court","Why sharing a mediation fee beats funding a court fight"),
  ("agreeing","Agreeing who pays — before you start")],
 key_takeaway("In Australian family mediation the fee is usually split equally between the parties, because both share the benefit of resolving the dispute. There are exceptions — one party may agree to pay more, or government-funded Family Relationship Centres offer free or low-cost family dispute resolution based on income. Either way, a shared mediation fee is a fraction of funding two lawyers through court.")
 + f"""
<h2 id="default">The usual rule: the fee is shared equally</h2>
<p>Mediation is a joint process that both people benefit from, so the standard arrangement is that the two parties split the mediator's fee 50/50. This reflects the spirit of mediation itself — it isn't one side hiring a champion against the other; it's both sides paying a neutral professional to help them reach an agreement they can both live with. Because most providers, including us, charge a <strong>fixed fee</strong> rather than billing by the hour, each party knows their share up front with no surprises. See a full breakdown on our <a href="/how-much-does-mediation-cost/">what mediation costs</a> page.</p>

<h2 id="when-one-pays">When one party pays more — or all of it</h2>
<p>The 50/50 split is a convention, not a law, and couples often vary it to fit their circumstances:</p>
<ul>
  <li><strong>Income imbalance</strong> — where one partner earns substantially more, they may agree to cover a larger share, or all, of the fee.</li>
  <li><strong>Access to funds</strong> — sometimes the cost is paid from a joint account or from the asset pool being divided, so neither party is out of pocket personally.</li>
  <li><strong>Goodwill</strong> — one party simply offers to pay to get the process moving, particularly where they're keen to resolve things quickly.</li>
</ul>
<p>None of this affects the mediator's neutrality. Who pays the bill has no bearing on the process — the mediator does not act for whoever pays.</p>
"""
 + inline_cta("Want a clear, fixed quote before you commit? Book a consultation and we'll set out exactly what your mediation will cost.")
 + f"""
<h2 id="free">Free and subsidised mediation</h2>
<p>Not everyone has to pay privately. The government funds a national network of Family Relationship Centres that provide family dispute resolution, with the first hours often free and further sessions charged on a sliding scale based on income. You can find them through {cite("frc")}, and the {cite("ag_fdr")} explains how the publicly funded system works. These services are an excellent option for many families, though wait times can be longer and complex financial matters are often better suited to private mediation, where sessions are scheduled quickly and a property settlement can be drafted and formalised in one place.</p>

<h2 id="what-included">What the mediation fee actually covers</h2>
<p>When you pay for private mediation, you're generally paying for more than the session itself. A typical fixed fee covers intake meetings with each party, the mediator's preparation, the mediation session or sessions, and a written record of what's agreed. For parenting matters, an accredited practitioner can also issue the <a href="/section-60i-certificates/">Section 60I certificate</a> you need before applying to court. Formalising the agreement into <a href="/consent-orders/">consent orders</a> may be a separate, modest cost.</p>

<h2 id="vs-court">Why sharing a mediation fee beats funding a court fight</h2>
<p>Here's the comparison that matters. A shared mediation fee usually runs to a few thousand dollars between you. A contested court case means each side funding their own lawyer — often tens of thousands of dollars each, sometimes far more — with no guarantee of the outcome you want. The {cite("fcfcoa_fees")} also adds court filing fees on top. Put simply, the question 'who pays for mediation?' is a much smaller question than 'who pays for court?', and resolving by agreement keeps the money with your family rather than spending it on the dispute.</p>

<h2 id="agreeing">Agreeing who pays before you start</h2>
<p>The simplest approach is to settle the question of who pays at the very start, often in the initial consultation, so it never becomes a sticking point. If you can't agree, that's worth knowing too — it can be a useful early signal of where the bigger negotiation may need the most help. Either way, our team sets out the fee and the options clearly before anything begins. Explore the process on our <a href="/family-law-mediation/">family law mediation</a> page.</p>
"""
 ,
 [("Is mediation cheaper than going to court?",
   "Almost always. A shared mediation fee is typically a few thousand dollars between both parties, while a contested court case can cost each side tens of thousands of dollars, plus court filing fees."),
  ("Do both parties have to pay for mediation?",
   "Usually the fee is split equally, but couples can agree any arrangement — one party paying more, paying from a joint account, or paying from the asset pool. The mediator stays neutral regardless of who pays."),
  ("Is there any free family mediation in Australia?",
   "Yes. Government-funded Family Relationship Centres offer family dispute resolution with initial hours often free and later sessions on an income-based sliding scale."),
  ("Does paying for the mediator mean they're on my side?",
   "No. The mediator is neutral and does not act for either party, regardless of who pays the fee. Their role is to help you both reach an agreement.")],
 [("how-much-does-mediation-cost","How Much Does Mediation Cost?"),
  ("private-vs-free-mediation","Private vs Free Mediation"),
  ("family-law-mediation","Family Law Mediation"),
  ("mediate-or-litigate","Mediate or Litigate?"),
  ("our-fee-structure","Our Fee Structure")],
 read_min=8)


post("private-vs-free-mediation",
 "Private vs Free Mediation in Australia: Which Is Right?",
 "Private mediation vs free family dispute resolution in Australia — the real differences in wait times, cost, complexity and outcomes, and how to choose.",
 "Costs &amp; fees",
 "Private vs Free Mediation: <em>Which Is Right for You?</em>",
 "Australia has both free, government-funded family dispute resolution and private mediation. Both are valuable — they just suit different situations. This guide compares them honestly on cost, wait times, complexity and outcomes so you can choose well.",
 [("two-systems","Two systems, both legitimate"),
  ("free","Free and subsidised mediation: how it works"),
  ("private","Private mediation: how it differs"),
  ("compare","Side-by-side comparison"),
  ("choose","How to choose between them")],
 key_takeaway("Free family dispute resolution, funded through Family Relationship Centres, is an excellent, low-cost option — especially for parenting matters. Private mediation costs more but typically offers shorter wait times, longer and more flexible sessions, and is better suited to complex property and financial settlements that need to be drafted and formalised quickly. Many families use the free system first and turn to private mediation when matters are complex or urgent.")
 + f"""
<h2 id="two-systems">Two systems, both legitimate</h2>
<p>When people search for 'free mediation' they sometimes assume private mediation is just the same thing with a price tag. It isn't quite. Australia deliberately runs two complementary systems: a publicly funded network designed to make family dispute resolution accessible to everyone, and a private profession that offers more capacity and flexibility for those who need it. Neither is 'better' in the abstract — the right choice depends on your matter.</p>

<h2 id="free">Free and subsidised mediation: how it works</h2>
<p>The government funds Family Relationship Centres across the country, which you can find through {cite("frc")}. They provide family dispute resolution for parenting matters, with the first hours often free and further sessions charged on a sliding scale based on income. The {cite("ag_fdr")} oversees this system. It's a genuinely good option: the practitioners are accredited, and for many separating parents it resolves things well. The trade-offs are practical — demand is high, so wait times for an appointment can be weeks or months, sessions can be shorter, and the centres focus primarily on parenting rather than complex property and financial settlements.</p>
"""
 + inline_cta("Not sure which path fits your situation? Book a consultation and we'll give you an honest steer — even if that's towards a free service.")
 + f"""
<h2 id="private">Private mediation: how it differs</h2>
<p>Private mediation is the same core process — a neutral, accredited mediator helping you reach agreement — but delivered with more capacity and flexibility. In practice that usually means you're seen within days rather than months, sessions are as long as the matter needs (often a full day, which can resolve everything in one sitting), and the service handles complex <a href="/property-settlement-mediation/">property settlements</a> involving businesses, trusts and superannuation, then drafts the agreement and helps formalise it into <a href="/consent-orders/">consent orders</a>. You pay for that — typically a fixed fee shared between the parties — but for many people the speed and the one-stop handling are worth it.</p>

<h2 id="compare">Private vs free mediation, side by side</h2>
<figure class="tbl"><table><caption>Comparing free family dispute resolution with private mediation</caption>
<thead><tr><th></th><th>Free / subsidised FDR</th><th>Private mediation</th></tr></thead>
<tbody>
<tr><td>Cost</td><td>Free to low (income-based)</td><td>Fixed fee, usually shared</td></tr>
<tr><td>Wait time</td><td>Weeks to months</td><td>Often days</td></tr>
<tr><td>Best for</td><td>Parenting matters</td><td>Complex property &amp; financial settlements</td></tr>
<tr><td>Session length</td><td>Often shorter</td><td>As long as needed (full-day common)</td></tr>
<tr><td>Drafts &amp; formalises agreement</td><td>Limited</td><td>Yes, in one place</td></tr>
</tbody></table></figure>

<h2 id="choose">How to choose between them</h2>
<p>A simple rule of thumb: if your matter is mainly about parenting, you're not in a hurry, and finances are straightforward, the free system is well worth trying first. If you have a complex property pool, you need to move quickly (for example to meet a <a href="/property-settlement-after-separation/">settlement time limit</a>), or you want everything resolved and formalised in one process, private mediation usually earns its fee. There's no shame in starting free and switching — and we'll tell you honestly which we think fits. See what private mediation costs on our <a href="/how-much-does-mediation-cost/">mediation costs</a> page.</p>
"""
 ,
 [("Is free mediation as good as private mediation?",
   "For straightforward parenting matters, free family dispute resolution is excellent and the practitioners are accredited. Private mediation tends to suit complex property settlements and situations needing fast, flexible scheduling."),
  ("How long do you wait for free mediation in Australia?",
   "Because demand is high, waits for a Family Relationship Centre appointment can run from a few weeks to a few months. Private mediation can usually be arranged within days."),
  ("Can free mediation handle property settlements?",
   "Family Relationship Centres focus mainly on parenting. Complex property and financial settlements — involving businesses, trusts or superannuation — are generally better suited to private mediation that can draft and formalise the agreement."),
  ("Can I start with free mediation and switch to private?",
   "Yes. Many families try the free system first and move to private mediation if matters are complex, urgent, or need to be formalised quickly.")],
 [("who-pays-for-mediation","Who Pays for Mediation?"),
  ("how-much-does-mediation-cost","How Much Does Mediation Cost?"),
  ("family-law-mediation","Family Law Mediation"),
  ("property-settlement-mediation","Property Settlement Mediation"),
  ("how-mediation-works","How Mediation Works")],
 read_min=8)


# ============================================================
# DIVORCE CLUSTER
# ============================================================
post("divorce-mediator-vs-divorce-lawyer",
 "Divorce Mediator vs Divorce Lawyer: What's the Difference?",
 "Divorce mediator vs divorce lawyer — what each does, what they cost, and why most people benefit from both in the right order. A clear 2026 guide.",
 "Divorce",
 "Divorce Mediator vs Divorce Lawyer: <em>What's the Difference?</em>",
 "A divorce mediator and a divorce lawyer do very different jobs — and the smartest approach usually uses both, in the right order. This guide explains what each does, what they cost, and how to combine them to resolve your separation for less.",
 [("roles","Two different roles"),
  ("mediator","What a divorce mediator does"),
  ("lawyer","What a divorce lawyer does"),
  ("compare","Side-by-side comparison"),
  ("both","Why you usually want both"),
  ("order","The order that saves you money")],
 key_takeaway("A divorce mediator is neutral and helps both parties reach a shared agreement on parenting, property and finances. A divorce lawyer acts for one party, giving advice and advocating for their interests. They're not rivals — most people get the best result by mediating first to reach agreement, then having a lawyer review it before it's made binding. That order keeps legal costs down.")
 + f"""
<h2 id="roles">Two different roles, often confused</h2>
<p>People sometimes treat 'divorce mediator' and 'divorce lawyer' as competing options — as if you pick one. In reality they do different jobs, and the question isn't which to choose but how to use each. Getting this right is one of the biggest levers you have over what your separation costs.</p>

<h2 id="mediator">What a divorce mediator does</h2>
<p>A divorce mediator is a neutral, accredited professional who helps you and your former partner reach agreement on the issues that come with separating — parenting, property, superannuation and support. The mediator doesn't take a side or decide the outcome; they run a fair process, keep it constructive, and help you both find common ground. Many of our mediators are also experienced family lawyers, so they understand the legal framework under the {cite("family_law_act")} and can keep proposals realistic — but in the mediation room they stay neutral. Learn more on our <a href="/divorce-mediation/">divorce mediation</a> page.</p>

<h2 id="lawyer">What a divorce lawyer does</h2>
<p>A divorce lawyer acts <em>for you</em>. They advise you on your rights and likely entitlements, draft and review documents, and — if it comes to it — advocate for you in negotiations or in the {cite("fcfcoa")}. That partisan role is exactly what you want when you need advice tailored to your interests or representation in a contested matter. What a lawyer cannot do is be neutral between you and your ex, which is why a lawyer-led process can sometimes harden positions rather than resolve them.</p>
"""
 + inline_cta("Want to resolve your divorce for less? Start with mediation — book a consultation and see how far agreement can take you.")
 + f"""
<h2 id="compare">Divorce mediator vs divorce lawyer, side by side</h2>
<figure class="tbl"><table><caption>How a divorce mediator and a divorce lawyer differ</caption>
<thead><tr><th></th><th>Divorce mediator</th><th>Divorce lawyer</th></tr></thead>
<tbody>
<tr><td>Acts for</td><td>Both parties, neutrally</td><td>You alone</td></tr>
<tr><td>Main goal</td><td>A shared, workable agreement</td><td>The best outcome for you</td></tr>
<tr><td>Gives legal advice?</td><td>No</td><td>Yes</td></tr>
<tr><td>Typical cost</td><td>Fixed fee, usually shared</td><td>Hourly, you pay your own</td></tr>
<tr><td>Decides outcome?</td><td>No — you do</td><td>No — but advocates a position</td></tr>
</tbody></table></figure>

<h2 id="both">Why you usually want both</h2>
<p>The best results typically come from using both. Mediation gets you to an agreement quickly and cheaply; independent legal advice makes sure that agreement is sound before you commit to it. This is especially important before signing a binding financial agreement, where each party is required to have their own lawyer. Far from competing, the two roles complement each other — the mediator builds the deal, the lawyer pressure-tests it.</p>

<h2 id="order">The order that saves you money</h2>
<p>Sequence matters. If you start with two lawyers firing letters at each other, costs climb before you've made any progress. If you start with mediation, you arrive at a draft agreement and only then pay a lawyer to review it — a much smaller, more focused job. So the cost-effective order is usually: mediate first, get advice alongside or just after, then formalise through <a href="/consent-orders-explained/">consent orders</a> or a binding financial agreement. The point was never to avoid lawyers — it's to avoid an unnecessary, expensive fight. Compare the paths in our <a href="/mediate-or-litigate/">mediate or litigate</a> guide.</p>
"""
 ,
 [("Is a divorce mediator cheaper than a divorce lawyer?",
   "Generally yes. A mediator charges a fixed fee usually shared between both parties, while two lawyers each bill hourly. Mediating first and using a lawyer only to review the agreement keeps total costs down."),
  ("Can a divorce mediator give me legal advice?",
   "No. A mediator is neutral and cannot advise either party. Even where the mediator is also a qualified lawyer, in the mediation they do not act for you — you should get your own independent legal advice."),
  ("Do I need a lawyer if I use a divorce mediator?",
   "You don't need one to mediate, but independent legal advice is wise before signing a binding agreement, and is legally required for a binding financial agreement. Mediation usually makes that advice cheaper and more focused."),
  ("Should I see a mediator or a lawyer first?",
   "For most separations, mediating first is the cost-effective order: you reach a draft agreement, then have a lawyer review it. Where you need urgent protection or advice on rights first, see a lawyer.")],
 [("divorce-mediation","Divorce Mediation"),
  ("divorce-without-a-lawyer","Divorce Without a Lawyer"),
  ("mediate-or-litigate","Mediate or Litigate?"),
  ("family-law-mediation","Family Law Mediation"),
  ("how-much-does-mediation-cost","How Much Does Mediation Cost?")],
 read_min=8)


post("mediation-before-divorce",
 "Can Mediation Help Before You File for Divorce?",
 "Can mediation help before filing for divorce? How resolving parenting and property early — even during separation — saves time, money and stress. 2026 guide.",
 "Divorce",
 "Can Mediation Help <em>Before</em> You File for Divorce?",
 "You don't have to wait for a divorce to be final — or even filed — to start resolving the things that matter. Mediation during separation lets you settle parenting and property early, so the legal divorce becomes a formality rather than a fight.",
 [("timing","Divorce and the disputes are separate"),
  ("during-separation","Mediating during the 12-month separation"),
  ("parenting","Sorting parenting early"),
  ("property","Sorting property early — and the time limit"),
  ("benefits","Why earlier is almost always better"),
  ("how","How to start before you file")],
 key_takeaway("Yes — and often it's the best time. In Australia you must be separated for 12 months before you can apply for divorce, and the divorce itself doesn't resolve parenting or property at all. Mediation during separation lets you settle those issues early, so when you do file, the legal divorce is a simple administrative step. Resolving early protects the asset pool, stabilises arrangements for the children, and reduces conflict.")
 + f"""
<h2 id="timing">The divorce and the disputes are separate things</h2>
<p>This trips a lot of people up. The legal divorce simply ends the marriage; it does not divide property, settle finances, or determine parenting arrangements. Those are separate matters you resolve by agreement or, failing that, in court. And here's the key point: you don't have to wait for the divorce — or even file for it — to start resolving them. Many couples sort out parenting and property well before the divorce paperwork is lodged.</p>

<h2 id="during-separation">Mediating during the 12-month separation</h2>
<p>Australia requires you to be separated for at least 12 months before you can apply for divorce, as set out by the {cite("fcfcoa")}. That waiting period is not dead time — it's the ideal window to mediate. You can use those months to reach a clear, workable agreement on the children and the finances, so that by the time you're eligible to file, the hard parts are already settled. You can even <a href="/online-divorce/">apply for the divorce online</a> later while the agreement sits ready to be formalised.</p>
"""
 + inline_cta("Separated and want to get ahead of it? Book a consultation and start resolving parenting and property now, not later.")
 + f"""
<h2 id="parenting">Sorting parenting early</h2>
<p>Children benefit enormously from early, stable arrangements. Mediating a <a href="/parenting-plan-mediation/">parenting plan</a> soon after separation means the kids settle into a predictable routine rather than living through months of uncertainty and conflict. Under the {cite("family_law_act")}, arrangements must be in the children's best interests — and stability is a big part of that. Early agreement also avoids positions hardening, which is what makes later disputes so bitter.</p>

<h2 id="property">Sorting property early — and watching the time limit</h2>
<p>There's a practical reason not to wait, too. Once a divorce is finalised, you generally have only <strong>12 months</strong> to finalise property and financial matters. Couples who leave everything until after the divorce sometimes find themselves rushing against that clock. Resolving <a href="/property-settlement-mediation/">property settlement</a> through mediation during separation takes the time pressure off entirely and protects the asset pool from being eroded by prolonged conflict.</p>

<h2 id="benefits">Why earlier is almost always better</h2>
<ul>
  <li><strong>Lower conflict</strong> — you negotiate before resentment calcifies into entrenched positions.</li>
  <li><strong>Protected finances</strong> — less time for the asset pool to be run down by legal fees or poor decisions.</li>
  <li><strong>Stability for children</strong> — predictable arrangements from early on.</li>
  <li><strong>A smoother divorce</strong> — when you file, there's nothing left to fight about.</li>
</ul>

<h2 id="how">How to start before you file</h2>
<p>You simply book a consultation — there's no need to have filed anything first. We'll help you map the issues, gather what's needed, and work through parenting and property at a pace that suits you. When the agreement is reached, we help formalise it through <a href="/consent-orders-explained/">consent orders</a> so it's binding and ready. Then the divorce, when its time comes, is the easy part. Start on our <a href="/divorce-mediation/">divorce mediation</a> page.</p>
"""
 ,
 [("Can I mediate before applying for divorce?",
   "Yes. You don't need to have filed for divorce — or even be eligible yet — to mediate parenting and property. Many couples resolve these during the 12-month separation period."),
  ("Do I have to be divorced to settle property?",
   "No. You can reach and formalise a property settlement during separation, before a divorce is filed or finalised. After divorce, a 12-month time limit applies to finalise property, so earlier is safer."),
  ("Does mediation speed up the divorce?",
   "It doesn't change the legal requirements, but it removes the disputes that make divorces drawn-out. With parenting and property already agreed, the divorce application itself is straightforward."),
  ("Is it better to mediate before or after divorce?",
   "Usually before or during separation. Resolving early protects the asset pool, stabilises arrangements for children, and avoids the post-divorce 12-month property time limit becoming a rush.")],
 [("divorce-mediation","Divorce Mediation"),
  ("online-divorce","Online Divorce"),
  ("how-to-get-a-divorce-in-australia-a-step-by-step-guide","How to Get a Divorce"),
  ("property-settlement-mediation","Property Settlement Mediation"),
  ("parenting-plan-mediation","Parenting Plan Mediation")],
 read_min=8)


# ============================================================
# FAMILY CLUSTER
# ============================================================
post("what-happens-if-mediation-fails",
 "What Happens If Mediation Fails? (Australia, 2026)",
 "What happens if family mediation fails or one party won't attend? Section 60I certificates, going to court, and why a 'failed' mediation often still helps.",
 "Family law mediation",
 "What Happens If Mediation Fails? <em>Your Next Steps</em>",
 "Most family mediations succeed — but not all, and that's not the end of the road. This guide explains what happens if mediation doesn't resolve everything: Section 60I certificates, the path to court, and why even a 'failed' mediation usually leaves you better off.",
 [("how-often","How often does mediation fail?"),
  ("partial","Partial agreement is still progress"),
  ("certificate","The Section 60I certificate"),
  ("court","Going to court after mediation"),
  ("wont-attend","If the other party won't attend"),
  ("still-helps","Why 'failed' mediation still helps")],
 key_takeaway("If family mediation doesn't resolve your dispute, you're not stuck. For parenting matters, the mediator issues a Section 60I certificate, which lets you apply to court. Often mediation resolves some issues even if not all, narrowing what's left to decide. And the disclosure and clarity gained in mediation usually make any later court process faster and cheaper — so it's rarely wasted.")
 + f"""
<h2 id="how-often">How often does mediation actually fail?</h2>
<p>Less often than people fear. The large majority of family matters that go to mediation reach agreement, because the process is designed to find common ground that adversarial positions obscure. But mediation is voluntary and not every matter resolves — sometimes the gap is too wide, sometimes new information emerges, and sometimes one party simply isn't ready. When that happens, there's a clear and orderly path forward.</p>

<h2 id="partial">Partial agreement is still real progress</h2>
<p>'Failure' is rarely all-or-nothing. Couples frequently agree on most issues and get stuck on one — say they settle parenting but not the family home, or agree the split but not the timing. That's a good outcome, not a bad one: every issue resolved in mediation is one fewer to argue (and pay for) later, and the remaining question is sharply defined. You can formalise what you agreed and deal only with the rest.</p>

<h2 id="certificate">The Section 60I certificate</h2>
<p>For parenting disputes, the law generally requires you to attempt family dispute resolution before you can apply to court. If mediation doesn't resolve the matter, the accredited practitioner issues a {cite("fcfcoa_fdr")} certificate — a Section 60I certificate — confirming you made a genuine effort. That certificate is your key to filing. We can issue it as part of the process; read more on our <a href="/section-60i-certificates/">Section 60I certificates</a> page.</p>
"""
 + inline_cta("Worried mediation might not resolve everything? Book a consultation — even partial agreement saves you time and money.")
 + f"""
<h2 id="court">Going to court after mediation</h2>
<p>If you do need to apply to court, the matter proceeds through the {cite("fcfcoa")}, which actively encourages parties to keep negotiating — most cases still settle before a final hearing. Anything you resolved in mediation can be formalised into <a href="/consent-orders-explained/">consent orders</a>, so the court only has to deal with what's genuinely in dispute. Our <a href="/family-court-process/">family court process</a> guide explains what to expect.</p>

<h2 id="wont-attend">If the other party won't attend</h2>
<p>Mediation needs both people, but one party's refusal doesn't trap you. Where the other side won't participate, the mediator can issue a Section 60I certificate on the basis that the other party did not attend — which lets you proceed to court for parenting matters. For property, there's no certificate requirement, so you can move forward through legal channels. Either way, an unwilling ex slows you down but doesn't stop you.</p>

<h2 id="still-helps">Why 'failed' mediation still helps</h2>
<p>Even when it doesn't produce a full agreement, mediation rarely wastes your time. The financial disclosure gathered, the issues clarified, and the realistic range surfaced all make any later process faster and cheaper. Judges also look favourably on parties who genuinely tried to resolve matters. In other words, mediation that 'fails' often still shortens and cheapens what follows — and you can always return to it once positions have shifted. Start, or restart, on our <a href="/family-law-mediation/">family law mediation</a> page.</p>
"""
 ,
 [("What is a Section 60I certificate?",
   "It's a certificate issued by an accredited family dispute resolution practitioner confirming you attempted mediation (or that it wasn't appropriate). For most parenting matters you need one before you can apply to court."),
  ("Can I go to court if mediation fails?",
   "Yes. For parenting matters you'll generally need a Section 60I certificate first, which the mediator issues. For property matters there's no certificate requirement and you can proceed through legal channels."),
  ("What if my ex refuses to attend mediation?",
   "The mediator can issue a Section 60I certificate on the basis the other party didn't attend, allowing you to apply to court for parenting matters. Refusal slows the process but doesn't stop you."),
  ("Is mediation wasted if it doesn't fully work?",
   "Rarely. Partial agreements narrow the dispute, disclosure and clarity gained make any court process faster and cheaper, and courts view a genuine attempt favourably.")],
 [("section-60i-certificates","Section 60I Certificates"),
  ("family-court-process","The Family Court Process"),
  ("is-family-law-mediation-compulsory","Is Mediation Compulsory?"),
  ("family-law-mediation","Family Law Mediation"),
  ("high-conflict-mediation","High-Conflict Mediation")],
 read_min=8)


# ============================================================
# PROPERTY CLUSTER
# ============================================================
post("what-is-in-the-property-pool",
 "What Is Included in the Property Pool? (Australia, 2026)",
 "What's in the property pool in a family law settlement? Assets, super, businesses, debts, inheritances and what counts — a clear guide for separating couples.",
 "Property &amp; finances",
 "What's Included in the Property Pool? <em>The Full Picture</em>",
 "Before you can divide a property settlement fairly, you have to know what's in it. This guide explains exactly what goes into the asset pool under Australian family law — including the assets people forget — and why honest disclosure is the foundation of any fair split.",
 [("what-is-pool","What 'the property pool' means"),
  ("included","What's included"),
  ("super","Superannuation"),
  ("business","Businesses, trusts and inheritances"),
  ("debts","Debts count too"),
  ("disclosure","Why full disclosure is non-negotiable")],
 key_takeaway("The property pool is the total of everything you and your former partner own and owe — together and separately. It includes the family home, savings, investments, vehicles, superannuation, business interests, and sometimes trusts and inheritances, minus all debts and liabilities. Both parties must fully disclose their finances; a settlement built on hidden assets can later be overturned.")
 + f"""
<h2 id="what-is-pool">What 'the property pool' actually means</h2>
<p>In a family law settlement, the first step is always to identify the 'property pool' — the complete picture of what there is to divide. It's not just the things in one person's name, and it's not just the assets acquired during the relationship. The pool is everything of value you both own and owe, wherever it sits. Getting this picture complete and honest is the foundation; everything that follows — contributions, future needs, the final split — is built on it. This mirrors the four-step approach under the {cite("family_law_act")} that mediators and courts alike apply.</p>

<h2 id="included">What's included in the pool</h2>
<ul>
  <li>The family home and any investment or other property</li>
  <li>Cash, savings and term deposits</li>
  <li>Shares, managed funds and other investments</li>
  <li>Vehicles, boats and valuable personal property</li>
  <li>Superannuation (yes, it counts — see below)</li>
  <li>Business interests, company shares and partnership interests</li>
  <li>Sometimes trusts and inheritances</li>
  <li>Minus all debts and liabilities</li>
</ul>
<p>It doesn't matter whose name an asset is in, or whether one partner 'earned' it — if it's part of the relationship's economic picture, it generally goes into the pool to be considered.</p>
"""
 + inline_cta("Not sure what counts in your pool? Book a consultation and we'll help you map it clearly — without the lawyers' letters.")
 + f"""
<h2 id="super">Superannuation is property too</h2>
<p>One of the most common misconceptions is that superannuation sits outside a property settlement. It doesn't. Super is treated as property under Australian family law and can be split between partners, which often makes a fair division possible without anyone having to sell the family home. Defined-benefit and self-managed funds need careful valuation, but the principle is simple: super is part of the pool. See how this works in <a href="/property-settlement-mediation/">property settlement mediation</a>.</p>

<h2 id="business">Businesses, trusts and inheritances</h2>
<p>These are where settlements get genuinely complex. A business one or both of you built forms part of the pool — the question is its value and how to deal with it without destroying the income it produces. Trusts and inheritances are more nuanced: whether they're 'in' or 'out' depends on timing, who controls them, and how they were used during the relationship. These need careful, honest handling, which is exactly the kind of thing mediation is well suited to working through.</p>

<h2 id="debts">Debts count too</h2>
<p>The pool isn't only assets. Mortgages, personal loans, credit card balances, tax debts and business liabilities all reduce the net pool and have to be allocated as deliberately as the assets. A settlement that divides the assets but ignores who carries the debts isn't a fair settlement — it's an unfinished one.</p>

<h2 id="disclosure">Why full disclosure is non-negotiable</h2>
<p>None of this works without honesty. Both parties have a {cite("fcfcoa_disclosure")} — a duty of full and frank financial disclosure. Hiding or understating assets doesn't just poison the process; a settlement reached on incomplete information can be set aside by a court later, unravelling everything. Mediation actually makes disclosure easier, because the mediator sets a clear, shared list of documents up front so you both arrive with the same complete picture. That's the real starting line for a fair <a href="/property-settlement-mediation/">property settlement</a>.</p>
"""
 ,
 [("Is superannuation included in a property settlement?",
   "Yes. Superannuation is treated as property under Australian family law and can be split between partners, often as part of a mediated settlement formalised in consent orders."),
  ("Does it matter whose name an asset is in?",
   "Generally no. The property pool includes assets regardless of which partner's name they're in, if they form part of the relationship's economic picture."),
  ("Are inheritances part of the property pool?",
   "Sometimes. Whether an inheritance is included depends on its timing, who controls it, and how it was used during the relationship. These need careful, case-by-case assessment."),
  ("What happens if my ex hides assets?",
   "Both parties have a duty of full disclosure. Hiding assets can see a later settlement overturned by a court, so non-disclosure is a serious risk for the person doing it.")],
 [("property-settlement-mediation","Property Settlement Mediation"),
  ("property-settlement-after-separation","Property Settlement After Separation"),
  ("superannuation-and-divorce","Superannuation & Divorce"),
  ("delaying-property-settlement","Can My Ex Delay Settlement?"),
  ("what-am-i-entitled-to-in-a-separation-in-australia","What Am I Entitled To?")],
 read_min=8)


post("delaying-property-settlement",
 "Can My Ex Delay the Property Settlement? (Australia, 2026)",
 "Can your ex delay a property settlement — and what can you do? Stalling tactics, time limits, disclosure duties and how mediation forces progress. 2026 guide.",
 "Property &amp; finances",
 "Can My Ex Delay the Property Settlement? <em>What You Can Do</em>",
 "A former partner dragging out a property settlement is one of the most common — and most frustrating — situations after separation. Here's why it happens, what limits the stalling, and how mediation and the law combine to force progress.",
 [("why-stall","Why an ex stalls"),
  ("can-they","How long can they really delay?"),
  ("disclosure","Disclosure duties cut both ways"),
  ("time-limits","Time limits work in your favour"),
  ("mediation","How mediation forces momentum"),
  ("court","When you may need the court")],
 key_takeaway("An ex can slow a property settlement, but they can't stall forever. Both parties have a legal duty to disclose their finances, strict time limits apply, and mediation imposes a clear timetable that makes drift far harder than in slow-moving litigation. If stalling continues, a court can be asked to step in — and judges take a dim view of deliberate delay.")
 + f"""
<h2 id="why-stall">Why an ex drags it out</h2>
<p>Understanding the motive helps you respond. Stalling is usually about one of a few things: an emotional reluctance to let go, a belief that delay improves their position, a hope you'll give up and accept less, or simply avoidance. Occasionally it's strategic — for instance, hoping an asset's value will move. Whatever the reason, the law and a good process are designed to limit how much delay actually achieves.</p>

<h2 id="can-they">How long can they really delay?</h2>
<p>Less than they might think. While a determined party can introduce friction — being slow with documents, cancelling sessions, raising endless queries — the system has guardrails. Disclosure is compulsory, mediation sets deadlines, and ultimately a court can impose a timetable and make orders even if one party drags their feet. Delay is a tactic with a shelf life, not an indefinite veto.</p>

<h2 id="disclosure">Disclosure duties cut both ways</h2>
<p>One of the strongest tools against stalling is the {cite("fcfcoa_disclosure")} — the duty of full and frank financial disclosure that binds both parties. An ex who 'can't find' documents or is mysteriously slow to produce them is not just being difficult; they may be breaching a legal obligation. Persistent non-disclosure can be raised with a court, which can draw adverse inferences and even set aside a later settlement built on hidden information. Honesty isn't optional, and that protects the party who wants to get on with it.</p>
"""
 + inline_cta("Tired of waiting on a stalling ex? Book a consultation — mediation sets a clear timetable that's hard to dodge.")
 + f"""
<h2 id="time-limits">Time limits work in your favour</h2>
<p>The clock can be an ally. After a divorce, you generally have 12 months to finalise property; for de facto couples it's 24 months from separation. These limits create pressure to act — and they apply to your ex as much as to you. Far from being only a risk, the deadline is also leverage: drift has consequences for both sides, which often concentrates a reluctant party's mind. See the detail in our <a href="/property-settlement-after-separation/">property settlement after separation</a> guide.</p>

<h2 id="mediation">How mediation forces momentum</h2>
<p>This is where mediation genuinely outperforms a lawyer-led back-and-forth. A mediation sets a date, a shared disclosure list and an agenda up front — so instead of open-ended letter-writing that a staller can spin out for months, there's a structured process with a clear destination. It's much harder to 'go quiet' on a scheduled full-day session with everything on the table. For many couples, simply booking <a href="/property-settlement-mediation/">property settlement mediation</a> is what finally breaks the logjam.</p>

<h2 id="court">When you may need the court</h2>
<p>If an ex refuses to engage at all, the {cite("family_law_act")} lets you apply to court for property orders, and the court can set a binding timetable and ultimately decide the matter. It's the slower, costlier path — which is exactly why most people prefer mediation — but it exists as a backstop precisely so that one party cannot hold the other hostage indefinitely. Knowing the backstop is there often makes mediation more productive.</p>
"""
 ,
 [("How long can my ex delay a property settlement?",
   "They can slow it but not stall indefinitely. Disclosure is compulsory, time limits apply, mediation imposes a timetable, and a court can ultimately set deadlines and make orders even if one party drags their feet."),
  ("Is there a time limit to settle property after divorce?",
   "Yes. After a divorce you generally have 12 months to finalise property matters; de facto couples have 24 months from separation. These limits apply to both parties."),
  ("What if my ex won't disclose their finances?",
   "Both parties have a legal duty of full and frank disclosure. Persistent non-disclosure can be raised with a court, which can draw adverse inferences and set aside a settlement based on hidden assets."),
  ("Can mediation stop my ex stalling?",
   "It makes stalling much harder. Mediation sets a date, a shared disclosure list and an agenda, replacing open-ended negotiation with a structured process that's difficult to spin out.")],
 [("property-settlement-mediation","Property Settlement Mediation"),
  ("property-settlement-after-separation","Property Settlement After Separation"),
  ("what-is-in-the-property-pool","What's in the Property Pool?"),
  ("high-conflict-mediation","High-Conflict Mediation"),
  ("how-long-does-a-divorce-take","How Long Does Divorce Take?")],
 read_min=8)


# ============================================================
# PARENTING CLUSTER
# ============================================================
post("co-parenting-mediation",
 "Co-Parenting Mediation: Making Shared Parenting Work",
 "Co-parenting mediation helps separated parents resolve ongoing disputes over schedules, decisions and communication — keeping the focus on the children.",
 "Parenting &amp; children",
 "Co-Parenting Mediation: <em>Making Shared Parenting Work</em>",
 "Reaching a parenting plan is one thing; living it for years is another. Co-parenting mediation helps separated parents resolve the ongoing friction — schedules, decisions, new partners, changing needs — so shared parenting actually works long term.",
 [("what-is","What co-parenting mediation is"),
  ("when","When to use it"),
  ("issues","Common issues it resolves"),
  ("best-interests","Keeping the children at the centre"),
  ("changing","Changing arrangements as kids grow"),
  ("how","How to start")],
 key_takeaway("Co-parenting mediation is family dispute resolution focused on the ongoing relationship between separated parents — not just the initial parenting plan, but the day-to-day disputes that come up for years afterward. A neutral mediator helps you resolve conflicts over schedules, decisions and communication, and update arrangements as children grow, keeping the focus on the children rather than the conflict.")
 + f"""
<h2 id="what-is">What co-parenting mediation is</h2>
<p>Most people think of mediation as a one-off — you separate, you agree a parenting plan, done. But co-parenting is a relationship that continues for years, and disputes don't politely stop once the ink dries. Co-parenting mediation is family dispute resolution aimed squarely at that ongoing relationship: a neutral, accredited mediator helping two parents work through the recurring friction of raising children across two homes. It uses the same principles as any <a href="/parenting-plan-mediation/">parenting plan mediation</a>, applied to live, day-to-day issues.</p>

<h2 id="when">When to use it</h2>
<p>Co-parenting mediation is useful whenever the existing arrangement is creating conflict — even if you already have a parenting plan or court orders. Common triggers include a parent wanting to change the schedule, a new partner entering the picture, a planned relocation, disagreements about schooling or health, or simply communication breaking down into constant arguments. Rather than heading back to court every time something shifts, mediation gives you a faster, calmer way to recalibrate.</p>
"""
 + inline_cta("Co-parenting friction wearing you down? Book a consultation and reset the arrangement calmly — without going back to court.")
 + f"""
<h2 id="issues">Common issues co-parenting mediation resolves</h2>
<ul>
  <li><strong>Schedule disputes</strong> — handovers, holidays, special occasions and last-minute changes</li>
  <li><strong>Decision-making</strong> — school choice, medical decisions, extracurricular activities and religion</li>
  <li><strong>Communication</strong> — how and how often you talk, and keeping it child-focused</li>
  <li><strong>New partners</strong> — introducing them and managing blended-family dynamics</li>
  <li><strong>Relocation</strong> — one parent wanting to move, and what that means for time</li>
  <li><strong>Money around the kids</strong> — activities, school fees and shared costs</li>
</ul>

<h2 id="best-interests">Keeping the children at the centre</h2>
<p>The anchor through all of this is the children's best interests, which the {cite("family_law_act")} places at the centre of every parenting decision. Co-parenting mediation works because it pulls the focus away from the parents' grievances and back to a practical question: what actually works for these children, at this age, right now? Research collected by the {cite("aifs")} consistently shows children adjust best to separation when parental conflict is low and both parents stay meaningfully involved — which is exactly what good co-parenting mediation protects.</p>

<h2 id="changing">Changing arrangements as children grow</h2>
<p>An arrangement that suited a four-year-old rarely suits a fourteen-year-old. Children's needs, schools, friendships and activities change, and a co-parenting relationship has to flex with them. Mediation is the natural place to do that — instead of treating every change as a fresh battle, you have a low-conflict forum to update the plan by agreement. Where you want the updated arrangement to be enforceable, it can be formalised into <a href="/consent-orders-explained/">consent orders</a>.</p>

<h2 id="how">How to start</h2>
<p>You don't need a lawyer or a court application to begin — just book a consultation. If parenting orders are involved and you're heading toward court, the mediator can also issue a {cite("fcfcoa_fdr")} Section 60I certificate where required. Most families, though, find that a session or two resets the relationship enough to get co-parenting back on track. Start on our <a href="/parenting-plan-mediation/">parenting mediation</a> page, or read more on <a href="/child-custody-mediation/">child custody mediation</a>.</p>
"""
 ,
 [("What is co-parenting mediation?",
   "It's family dispute resolution focused on the ongoing relationship between separated parents — resolving recurring disputes over schedules, decisions and communication, and updating arrangements as children grow."),
  ("Can I use mediation if we already have a parenting plan?",
   "Yes. Co-parenting mediation is ideal when an existing plan or court order is causing conflict or needs updating. It's faster and calmer than returning to court each time something changes."),
  ("Do I need to go back to court to change parenting arrangements?",
   "Often no. Parents can agree changes through mediation and, if they want them enforceable, formalise the updated arrangement as consent orders without a contested hearing."),
  ("How does co-parenting mediation help the children?",
   "By lowering conflict and keeping the focus on the children's needs. Research shows children adjust best when parental conflict is low and both parents stay involved.")],
 [("parenting-plan-mediation","Parenting Plan Mediation"),
  ("child-custody-mediation","Child Custody Mediation"),
  ("parenting-plans-guide","Parenting Plans Guide"),
  ("section-60i-certificates","Section 60I Certificates"),
  ("family-law-mediation","Family Law Mediation")],
 read_min=8)


print("batch 11 (supporting-cluster articles) built")
