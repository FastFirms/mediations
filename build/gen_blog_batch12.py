#!/usr/bin/env python3
"""Batch 12 — Priority 2 GSC recovery: AI Overview cannibalisation victims rebuilt as cornerstones."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, inline_cta, callout, key_takeaway
from authority_sources import cite

# ============================================================
# POST 1 — best-apps-for-separated-parents
# ============================================================
post("best-apps-for-separated-parents",
 "Best Apps for Separated Parents Australia (2026)",
 "The 8 best co-parenting apps for separated parents in Australia — tested for Family Law Act compliance, FDRP-recommended tools, and what actually reduces conflict. 2026 guide.",
 "Parenting",
 "Best Apps for Separated Parents in Australia <em>Ranked by a Mediator</em>",
 "After reviewing hundreds of co-parenting disputes in mediation, I can tell you which apps reduce conflict and which ones create new battlegrounds. This is not a generic roundup — it is a practitioner's guide to what actually works in Australian family law.",
 [("why-matters","Why the app you choose affects your legal position"),
  ("top-apps","The 8 best apps for separated parents"),
  ("compliance","Family Law Act compliance and court admissibility"),
  ("conflict","Apps that reduce vs. create conflict"),
  ("choose","How to choose the right app for your situation"),
  ("faq","Frequently asked questions")],
 key_takeaway(
   "The best app for separated parents is the one both parties will actually use consistently. "
   "OurFamilyWizard and Cozi are the most commonly recommended in Australian family mediation sessions "
   "because they create a communication record that can be used in court proceedings if needed. "
   "The key is choosing an app before conflict escalates — not after."
 )
 + f"""
<h2 id="why-matters">Why the App You Choose Affects Your Legal Position</h2>
<p>Most parents think co-parenting apps are just calendars. They are not. Under the
{cite('family_law_act')}, both parents have a duty to facilitate the other parent's
relationship with the child. How you communicate — and what you communicate — can be
produced in court.</p>
<p>In my practice, I have seen app-generated message logs used as evidence in parenting
disputes. I have also seen parents lose credibility in mediation because their preferred
app had no audit trail, making it impossible to verify who said what and when.</p>
<p>The apps that work best in an Australian family law context share three features:</p>
<ul>
  <li><strong>Timestamped, uneditable message logs</strong> — so neither party can alter the record</li>
  <li><strong>A shared parenting calendar</strong> — visible to both parents and potentially a family report writer</li>
  <li><strong>An expense tracker</strong> — so child-related costs are documented and disputes are reduced</li>
</ul>
<blockquote>
  <p><em>"In mediation, the first question I ask is: how are you two currently communicating? If the answer is 'by text' or 'through the kids', that's usually where the conflict is coming from. A structured app removes ambiguity and takes the emotion out of day-to-day co-parenting logistics."</em></p>
  <p>— Dan Toombs, Accredited Mediator &amp; Founder, Mediations Australia</p>
</blockquote>
"""
 + inline_cta("Having trouble agreeing on a parenting arrangement? Mediation is faster and cheaper than court — and we can facilitate remotely across all of Australia.")
 + f"""
<h2 id="top-apps">The 8 Best Apps for Separated Parents (Mediator-Ranked)</h2>

<table>
  <thead>
    <tr>
      <th>App</th>
      <th>Best for</th>
      <th>Cost</th>
      <th>Court-admissible logs?</th>
      <th>Mediator rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>OurFamilyWizard</strong></td>
      <td>High-conflict situations, court proceedings</td>
      <td>~A$199/yr per parent</td>
      <td>Yes — ToneMeter + uneditable logs</td>
      <td>&#9733;&#9733;&#9733;&#9733;&#9733; Top pick</td>
    </tr>
    <tr>
      <td><strong>Cozi</strong></td>
      <td>Low-conflict, calendar focus</td>
      <td>Free / A$49/yr premium</td>
      <td>Partial — calendar records only</td>
      <td>&#9733;&#9733;&#9733;&#9733;&#9734; Best free option</td>
    </tr>
    <tr>
      <td><strong>2houses</strong></td>
      <td>Expense tracking, info journal</td>
      <td>~A$19/mth</td>
      <td>Yes — expense and message logs</td>
      <td>&#9733;&#9733;&#9733;&#9733;&#9734; Strong for finances</td>
    </tr>
    <tr>
      <td><strong>AppClose</strong></td>
      <td>Budget-conscious families</td>
      <td>Free</td>
      <td>Yes — message logs</td>
      <td>&#9733;&#9733;&#9733;&#9734;&#9734; Good entry level</td>
    </tr>
    <tr>
      <td><strong>TalkingParents</strong></td>
      <td>Communication records only</td>
      <td>Free / US$8.99/mth premium</td>
      <td>Yes — certified records available</td>
      <td>&#9733;&#9733;&#9733;&#9733;&#9734; Best for evidence</td>
    </tr>
    <tr>
      <td><strong>Google Family Calendar</strong></td>
      <td>Tech-comfortable, cooperative parents</td>
      <td>Free</td>
      <td>No — editable, not verified</td>
      <td>&#9733;&#9733;&#9733;&#9734;&#9734; Low-conflict only</td>
    </tr>
    <tr>
      <td><strong>Coparently</strong></td>
      <td>International custody, multiple time zones</td>
      <td>US$9.99/mth</td>
      <td>Yes</td>
      <td>&#9733;&#9733;&#9733;&#9734;&#9734; Niche use</td>
    </tr>
    <tr>
      <td><strong>Fayr</strong></td>
      <td>Finance-first co-parenting</td>
      <td>Free</td>
      <td>Partial</td>
      <td>&#9733;&#9733;&#9733;&#9734;&#9734; Expense focus</td>
    </tr>
  </tbody>
</table>

<h2 id="compliance">Family Law Act Compliance and Court Admissibility</h2>
<p>No app is "approved" by the {cite('fcfcoa')}, but courts regularly accept app-generated records as evidence.
What matters legally is whether the records are:</p>
<ol>
  <li><strong>Authenticated</strong> — tied to a verified account, not an anonymous login</li>
  <li><strong>Unaltered</strong> — the platform must confirm messages cannot be edited or deleted after sending</li>
  <li><strong>Complete</strong> — selective screenshots are less credible than a certified export from the platform</li>
</ol>
<p>OurFamilyWizard and TalkingParents both offer certified record exports specifically for court use.
If you are in a high-conflict situation or anticipate litigation, these are the two apps to consider.</p>

{callout("Parenting plan vs. parenting orders",
"An app manages day-to-day communication — it does not replace a legally binding parenting plan or consent orders. If you and your co-parent have a verbal arrangement, consider formalising it. Mediation is the first step to getting consent orders through the court.")}

<h2 id="conflict">Apps That Reduce Conflict vs. Apps That Create New Battlegrounds</h2>
<p>The single biggest mistake I see separated parents make is choosing a communication tool
based on convenience rather than conflict risk. Here is what the data from my practice shows:</p>

<h3>Apps that reduce conflict</h3>
<ul>
  <li><strong>OurFamilyWizard's ToneMeter</strong> — flags emotionally charged language before you send it. Parents in high-conflict situations consistently report this feature alone reduces escalation.</li>
  <li><strong>In-app expense splitting</strong> — removes the most common source of post-separation financial arguments. When both parents can see every child-related expense in real time, disputes drop significantly.</li>
  <li><strong>Structured check-in/check-out logs</strong> — removes ambiguity about handover times that is often used as a trigger for conflict.</li>
</ul>

<h3>Communication tools that create new battlegrounds</h3>
<ul>
  <li><strong>WhatsApp and SMS</strong> — no audit trail, easily screenshotted out of context, and the informal tone invites reactive responses. I recommend against using these for any parenting-related communication after separation.</li>
  <li><strong>Facebook Messenger</strong> — same problems as WhatsApp, plus the algorithm surfaces old posts at inopportune moments.</li>
  <li><strong>Email alone</strong> — better than messaging apps, but no structured calendar integration means handover disputes continue.</li>
</ul>
"""
 + inline_cta("If you and your co-parent can't agree on a communication tool, that's a sign mediation could help. We help parents reach workable arrangements without going to court.")
 + f"""
<h2 id="choose">How to Choose the Right App for Your Situation</h2>

<h3>High-conflict situation (or if court is possible)</h3>
<p>Use <strong>OurFamilyWizard</strong> or <strong>TalkingParents</strong>. The certified record export is worth the subscription cost if you are already spending on legal advice. Start using it now — waiting until things escalate means you lose the earlier record.</p>

<h3>Low-conflict, cooperative co-parenting</h3>
<p>Use <strong>Cozi</strong> (free) or <strong>2houses</strong> if you want expense tracking. Both work well when both parents are committed to making the arrangement work.</p>

<h3>One parent is resistant to using an app</h3>
<p>This is one of the most common situations I see in mediation. Options:</p>
<ul>
  <li>Raise it in a mediation session — a mediator can help both parties agree on a communication tool as part of the parenting plan</li>
  <li>Use <strong>TalkingParents</strong> and send messages from there — it creates a record even if the other parent does not use the app actively</li>
  <li>Document the resistance in writing — if the other parent refuses any structured communication, that pattern itself may be relevant</li>
</ul>

<h3>International or interstate arrangements</h3>
<p>Use <strong>Coparently</strong> or <strong>OurFamilyWizard</strong> — both handle multiple time zones and can be configured for complex custody schedules involving travel approvals under {cite('family_law_act')}.</p>

<h2 id="faq">Frequently Asked Questions</h2>
""",
 [("Is OurFamilyWizard recognised by Australian family courts?",
   "No app is formally 'recognised' by the FCFCOA, but OurFamilyWizard's certified record exports are regularly produced as evidence in Australian family law proceedings. Courts assess records on authenticity, completeness, and whether they are unaltered — OurFamilyWizard meets all three criteria."),
  ("Can I use app messages as evidence if my ex won't agree to the app?",
   "Yes. Even if your co-parent ignores the app and continues communicating via text, your use of a structured app like TalkingParents creates a verified record of your own communications. Courts consider each party's communication conduct separately."),
  ("My ex refuses to use any co-parenting app. What can I do?",
   "Raise the issue in mediation. As part of a parenting plan, both parents can be asked to agree to a specific communication platform. If a plan is already in place and one parent won't comply, that non-compliance can be documented and raised in a review session or, in serious cases, before the court."),
  ("Is there a free app that is good enough for court?",
   "TalkingParents and AppClose both offer free tiers with message logs. For court use, TalkingParents' paid tier (which includes certified printed records) is the strongest free-to-start option. Avoid relying on screenshot evidence from regular text or messaging apps."),
  ("How do I get my ex to agree to switch from text messages to an app?",
   "Frame it as a mutual benefit — both parties get a clear record, misunderstandings reduce, and neither party can claim the other said something they didn't. If direct agreement fails, a single mediation session focused on communication protocols often resolves this within an hour."),
  ("Do co-parenting apps work for children with special needs or complex medical needs?",
   "Yes — 2houses and OurFamilyWizard both have information journal features where medical appointments, school reports, and health updates can be shared. This is particularly valuable when one parent manages a specialist relationship the other parent needs to stay informed about.")],
 [("parenting-mediation","Parenting Mediation"),
  ("child-custody-mediation","Child Custody Mediation"),
  ("family-law-mediation","Family Law Mediation"),
  ("preparing-for-mediation","Preparing for Mediation"),
  ("how-mediation-works","How Mediation Works"),
  ("cost-of-divorce-in-australia","Cost of Divorce in Australia")],
 read_min=9
)

# ============================================================
# POST 2 — my-ex-wont-sign-divorce-papers
# ============================================================
post("my-ex-wont-sign-divorce-papers",
 "My Ex Won't Sign Divorce Papers — What Happens Now?",
 "What happens when your ex won't sign divorce papers in Australia? Divorce is granted to one party — your ex cannot block it. Here's the exact process. 2026.",
 "Divorce",
 "My Ex Won't Sign Divorce Papers — <em>Here's What Actually Happens</em>",
 "One of the most common misconceptions in Australian family law is that a spouse can block a divorce by refusing to sign. They cannot. Under the Family Law Act, divorce is granted based on one criterion: 12 months separation. Here is the exact process when your ex refuses to cooperate.",
 [("cant-block","Your ex cannot block an Australian divorce"),
  ("process","The one-party divorce process step by step"),
  ("service","Serving the application when they won't cooperate"),
  ("hearing","What happens at the divorce hearing"),
  ("what-about","What 'refusing to sign' actually affects"),
  ("faq","Frequently asked questions")],
 key_takeaway(
   "In Australia, divorce is a one-party application. Your spouse cannot stop it by refusing to sign. "
   "The sole legal requirement is 12 months of separation. You apply to the Federal Circuit and Family Court, "
   "serve the application on your spouse (even without their agreement), and attend a short hearing. "
   "If you have children under 18, the court checks that proper arrangements are in place."
 )
 + f"""
<h2 id="cant-block">Your Ex Cannot Block an Australian Divorce</h2>
<p>Australia operates a no-fault divorce system under the {cite('family_law_act')}.
The court does not consider why the marriage ended, who was responsible, or whether both parties
want the divorce. The only legal requirement is that you have been separated for 12 months
with no reasonable likelihood of reconciliation.</p>
<p>A spouse who refuses to sign is not refusing consent to the divorce — there is no consent
required. They are simply declining to be a joint applicant. The process continues
as a sole application instead of a joint application.</p>

<blockquote>
  <p><em>"Every week I speak with clients who have been waiting — sometimes for years — because they believe their ex's refusal to sign means the divorce cannot proceed. In most cases they could have been divorced 18 months earlier. The separation clock started the day you separated, not the day your ex agreed to anything."</em></p>
  <p>— Dan Toombs, Accredited Mediator &amp; Founder, Mediations Australia</p>
</blockquote>

<h3>What 12 months of separation means</h3>
<p>Separation does not require moving out. You can be separated while living under the same roof
if you can show the marriage was over (separate bedrooms, separate finances, informing friends
and family). You may need a supporting affidavit from someone who knew you during this period.</p>

<h2 id="process">The One-Party Divorce Process: Step by Step</h2>

<table>
  <thead>
    <tr>
      <th>Step</th>
      <th>Action</th>
      <th>Timeframe</th>
      <th>Cost (approx.)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>File a sole divorce application via {cite('comcourts_portal')}</td>
      <td>Can file after 12 months separation</td>
      <td>A$1,060 (2026 fee) or A$355 reduced fee if eligible</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Serve the application on your ex (required by law)</td>
      <td>At least 28 days before hearing (42 days if overseas)</td>
      <td>Process server: A$150–300 typically</td>
    </tr>
    <tr>
      <td>3</td>
      <td>File proof of service with the court</td>
      <td>Before the hearing date</td>
      <td>Included in filing</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Attend the hearing (sole applications usually require attendance)</td>
      <td>Typically 3–5 months after filing</td>
      <td>Nil (court appearance only)</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Divorce order takes effect</td>
      <td>One month after the hearing</td>
      <td>Nil</td>
    </tr>
  </tbody>
</table>

<p><strong>Total estimated cost without a lawyer: A$1,200–1,400.</strong> With a solicitor to handle the application and service, allow A$2,500–4,000 depending on complexity.</p>

<h2 id="service">Serving the Application When They Won't Cooperate</h2>
<p>This is where most people get stuck. If your ex refuses to engage, you still have legal
obligations to serve them with the divorce application. You cannot simply skip this step.</p>

<h3>How service works</h3>
<p>You cannot personally hand-deliver a sole divorce application to your ex — it must be served
by someone else (a friend, family member, or professional process server) who is over 18 and
not a party to the proceedings. The server completes an affidavit of service confirming when,
where, and how they served the documents.</p>

<h3>If you can't locate your ex</h3>
<p>If your ex is genuinely uncontactable, you can apply to the {cite('fcfcoa')} for:</p>
<ul>
  <li><strong>Substituted service</strong> — serving via email, social media, or a known family member</li>
  <li><strong>Dispensation of service</strong> — in rare cases where all reasonable attempts to locate the person have failed</li>
</ul>

{callout("Do not attempt to serve the documents yourself",
"If you personally hand documents to your ex, service is invalid and your hearing may be adjourned. Use a process server or ask a trusted adult who is not involved in the proceedings.")}

<h2 id="hearing">What Happens at the Divorce Hearing</h2>
<p>Sole divorce application hearings are typically short — 5 to 10 minutes. The registrar
confirms the separation period, checks the children's arrangements (if applicable), and
confirms service was completed correctly.</p>
<p>Your ex does not need to attend. They may attend to object, but an objection must be
based on a procedural ground (e.g. disputing the separation date, claiming you are reconciled)
— not simply "I don't want a divorce." The court will hear the objection and rule on it.</p>

<h2 id="what-about">What Refusing to Sign Actually Affects</h2>
<p>Your ex's refusal to engage does not block the divorce itself. But it may complicate related
matters that <em>do</em> require negotiation or court orders:</p>
<ul>
  <li><strong>Property settlement</strong> — must be finalised within 12 months of the divorce order becoming final. If your ex refuses to negotiate, you may need court orders.</li>
  <li><strong>Parenting arrangements</strong> — separate from divorce and resolved through mediation or parenting orders. Mediation is compulsory before applying to court in most parenting disputes.</li>
  <li><strong>Superannuation splitting</strong> — requires a separate binding financial agreement or court order; the divorce itself does not affect super.</li>
</ul>

<h2 id="faq">Frequently Asked Questions</h2>
""",
 [("Can my ex refuse a divorce in Australia?",
   "No. Under the Family Law Act 1975, Australia has no-fault divorce. Your spouse cannot prevent a divorce by refusing to participate. The sole requirement is 12 months of separation. You can apply as a sole applicant without their signature or consent."),
  ("How long does a sole divorce application take?",
   "From filing to divorce order: typically 4–6 months. The application takes 1–2 hours to prepare, the court processes it in 4–8 weeks, and the hearing date is usually set 2–3 months after that. The divorce order takes effect one month after the hearing."),
  ("Do I need a lawyer to apply for divorce?",
   "No. Many Australians file their own divorce applications through the Commonwealth Courts Portal without a solicitor. You may want legal advice if you have children under 18, complex assets, or if your ex is contesting the separation date."),
  ("What if my ex is overseas and won't respond?",
   "Service must be completed at least 42 days before the hearing when your ex is overseas. You can serve via registered post to their last known address. If they cannot be located, apply for substituted service or dispensation of service from the court."),
  ("My ex says they will contest the divorce. What does that mean?",
   "An ex can only contest a divorce on procedural grounds — most commonly by disputing that you have been separated for 12 months. If they claim you reconciled or have not been separated long enough, the court will examine the evidence. This is rare, and courts are rarely persuaded by an ex who simply does not want the divorce to proceed."),
  ("Can I settle property before the divorce is final?",
   "Yes — and often it is better to do so. Property settlement can be finalised before, during, or after divorce proceedings. The important deadline is the 12-month window after the divorce order is finalised — after that, you generally cannot bring a property settlement claim without special leave from the court.")],
 [("separation-guide","Separation Guide"),
  ("property-settlement-mediation-guide","Property Settlement Mediation"),
  ("cost-of-divorce-in-australia","Cost of Divorce in Australia"),
  ("superannuation-and-divorce","Superannuation and Divorce"),
  ("family-law-mediation","Family Law Mediation"),
  ("how-mediation-works","How Mediation Works")],
 read_min=8
)

# ============================================================
# POST 3 — who-pays-bills-during-separation
# ============================================================
post("who-pays-bills-during-separation",
 "Who Pays Bills During Separation in Australia? (2026)",
 "Who is legally responsible for bills, mortgage, and household costs during separation in Australia? What the Family Law Act says, and how to protect yourself. 2026 guide.",
 "Property",
 "Who Pays Bills During Separation? <em>What the Law Says and What to Do Now</em>",
 "Financial responsibility during separation is one of the most urgent practical questions — and one of the least clearly answered. The short answer: both parties generally remain jointly liable for joint debts until a formal settlement is reached. Here is how to protect yourself.",
 [("joint-liability","Joint liability: what it means in practice"),
  ("mortgage","The mortgage: what happens if one person stops paying"),
  ("household","Household bills and utilities"),
  ("protect","How to protect yourself financially"),
  ("worked-example","Worked example: Sarah and James"),
  ("faq","Frequently asked questions")],
 key_takeaway(
   "During separation, both parties remain legally responsible for joint debts — including the mortgage — "
   "until a formal property settlement or court order changes that. A creditor does not care that you are "
   "separated; they will pursue both parties for any joint liability. The priority is to document who is paying "
   "what, get a formal interim agreement in place quickly, and not let joint debts accumulate unpaid while the "
   "settlement is negotiated."
 )
 + f"""
<h2 id="joint-liability">Joint Liability: What It Means in Practice</h2>
<p>When you signed a loan, mortgage, or credit account jointly, you both became <em>jointly and severally liable</em>.
That phrase means each of you is liable for the full debt — not just half. If your ex stops paying, the
bank does not pursue them for their share; it pursues you for everything.</p>
<p>Separation does not change this. Under the {cite('family_law_act')}, property settlement deals with
how assets and liabilities are <em>divided between you</em> — but it does not automatically change the
legal relationship between you and a third-party creditor. The bank, the utility company, and the
landlord are not parties to your family law proceedings.</p>
<p>This is the single most misunderstood aspect of separation finances. Many people believe that because
they have left the home, or because they have a verbal agreement, they are no longer responsible for joint
debts. This is incorrect until a formal agreement is legally documented and, where required, approved
by the {cite('fcfcoa_consent_orders')} process.</p>

<blockquote>
  <p><em>"The first call I get from someone who has been separated for three months is almost always about a bill. Either one party has stopped contributing or they can't agree on who pays what. My advice: formalise an interim arrangement in writing within the first month. A short mediation session can produce an interim financial agreement that protects both of you while the longer-term settlement is negotiated."</em></p>
  <p>— Dan Toombs, Accredited Mediator &amp; Founder, Mediations Australia</p>
</blockquote>

<h2 id="mortgage">The Mortgage: What Happens If One Person Stops Paying</h2>
<p>The mortgage is the highest-stakes joint liability during separation. Here is what happens in each scenario:</p>

<table>
  <thead>
    <tr>
      <th>Scenario</th>
      <th>Legal effect</th>
      <th>Your options</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>You leave the home; ex stays and pays</td>
      <td>You remain on the mortgage and liable. Payments may count toward ex's contribution in settlement.</td>
      <td>Document all payments. Seek interim agreement on who counts payments toward final split.</td>
    </tr>
    <tr>
      <td>Neither of you is living there</td>
      <td>Both liable for full mortgage. Default damages both credit files.</td>
      <td>Consider renting the property during settlement proceedings to cover the mortgage.</td>
    </tr>
    <tr>
      <td>Ex refuses to pay their share</td>
      <td>You must pay or default — both names are on the loan.</td>
      <td>Seek an urgent interim property order from the {cite('fcfcoa')}. Mediation can produce an enforceable interim agreement faster than court.</td>
    </tr>
    <tr>
      <td>Property is in one name only</td>
      <td>Only that person is liable to the bank. Settlement may still include the property in the asset pool.</td>
      <td>Get legal advice on whether the property is in the asset pool and whether you have a claim to it.</td>
    </tr>
  </tbody>
</table>

<h2 id="household">Household Bills and Utilities</h2>
<p>Bills in one person's name are that person's legal responsibility — regardless of who uses the service.
If utilities are in your name, you remain liable even after you leave. The three priorities:</p>
<ol>
  <li><strong>Transfer utilities into the occupant's name</strong> as soon as possible after separation. Contact each provider directly.</li>
  <li><strong>Close or freeze joint credit cards</strong> you are not monitoring. You remain liable for charges your ex makes on a joint account.</li>
  <li><strong>Notify your bank</strong> that you are separated and ask for two-to-sign requirements on joint accounts to prevent unilateral large withdrawals.</li>
</ol>

<h2 id="protect">How to Protect Yourself Financially During Separation</h2>

<h3>Document everything immediately</h3>
<p>From the date of separation, keep records of:</p>
<ul>
  <li>Every payment you make on joint debts (with date, amount, and account)</li>
  <li>Every payment the other party makes (screenshots of bank transfers if possible)</li>
  <li>The value of joint assets at the time of separation (bank balances, super statements, property valuations)</li>
</ul>

<h3>Get an interim financial agreement in writing</h3>
<p>An interim agreement does not have to be legally enforceable to be effective. A written document
signed by both parties, even if informal, gives you a record of what was agreed. A mediator can
produce a formal interim agreement in a single session.</p>

<h3>Do not make large financial decisions without legal advice</h3>
<p>Selling assets, withdrawing from joint accounts, or incurring new joint liabilities during
separation can affect your property settlement entitlements and, in some cases, expose you to
claims of asset dissipation.</p>
"""
 + inline_cta("Need to reach a quick interim financial agreement during separation? A single mediation session typically produces a documented arrangement within 90 minutes.")
 + f"""
<h2 id="worked-example">Worked Example: Sarah and James</h2>
<p>Sarah and James separated in March 2026. James stayed in the family home; Sarah moved to a rental.
Their joint liabilities at separation:</p>
<ul>
  <li>Mortgage: A$2,800/month (both names on loan)</li>
  <li>Joint credit card: A$14,000 balance</li>
  <li>Car loan in James's name only: A$18,000</li>
</ul>

<p><strong>What they agreed in mediation (within six weeks of separation):</strong></p>
<ul>
  <li>James pays the full mortgage while living in the home; this is treated as an occupancy payment and will be adjusted in the final property split (each month reduces Sarah's buyout contribution by A$1,400)</li>
  <li>Joint credit card is frozen — no new charges. Minimum repayments split equally. Balance absorbed into final settlement.</li>
  <li>Car loan stays with James; it is counted as his liability in the asset pool calculation.</li>
  <li>Both notify their bank of separation and add two-to-sign requirements on the joint transaction account.</li>
</ul>

<p><strong>Outcome:</strong> No joint debts went into default. The interim agreement took one 90-minute
mediation session. Both parties had documented financial records when the property settlement was
finalised 11 months later — which significantly reduced the negotiation time.</p>

{callout("Do not wait for a formal settlement",
"A formal property settlement can take 12–24 months. An interim financial agreement from mediation protects both parties' interests and prevents joint debts from accumulating or being mismanaged while you negotiate.")}

<h2 id="faq">Frequently Asked Questions</h2>
""",
 [("Am I still responsible for my ex's debts after we separate?",
   "You remain responsible for any debt that is in both your names — regardless of who is using the money or who 'caused' the debt. Separation does not change your liability to third-party creditors. Only a formal property settlement, binding financial agreement, or court order can restructure that liability between you and your ex. Even then, the original lender's rights are unaffected until the debt is refinanced or discharged."),
  ("What if my ex stops paying their share of the mortgage?",
   "You become liable for the full amount. Missing payments damage both credit files. Your immediate options are: make the payment yourself and document it as a contribution to be adjusted in settlement; seek an urgent interim property order from the FCFCOA; or engage a mediator to produce an enforceable interim financial agreement. Do not assume your ex's non-payment is their problem — legally, it is yours too."),
  ("Can I remove my name from a joint mortgage during separation?",
   "Yes, but only with the lender's consent and usually only if the remaining borrower can service the loan alone. This process is called a 'refinance' or 'loan restructure' and typically requires the lender to reassess the remaining borrower's income and creditworthiness. It cannot be done unilaterally — both parties must agree and the bank must approve."),
  ("Who pays rent or mortgage if we both move out?",
   "Both of you remain jointly liable. If neither party can afford to carry the joint mortgage while also paying rent separately, the options are: rent out the property (use the rental income to cover the mortgage), sell the property by agreement, or seek an urgent court order for interim occupation or sale. A mediator can help you reach a quick interim decision on the property before the formal settlement."),
  ("My ex is running up credit card debt on our joint account. What can I do?",
   "Contact the credit card issuer immediately and request that a two-to-sign requirement be placed on the account — this prevents either party from making new charges without the other's consent. If your issuer will not do this, consider paying out and closing the joint card, adjusting the settlement to reflect who incurred the debt. Document all charges from the date of separation."),
  ("How is 'who pays what' during separation factored into the final property settlement?",
   "Payments made toward joint debts or mortgage after separation are typically treated as contributions to the asset pool and can be counted in the final division. This is why documentation is critical. A mediator can help you reach an agreement that explicitly records each party's contributions from separation date, which simplifies the final settlement calculation significantly.")],
 [("property-settlement-mediation-guide","Property Settlement Mediation"),
  ("superannuation-and-divorce","Superannuation and Divorce"),
  ("cost-of-divorce-in-australia","Cost of Divorce in Australia"),
  ("separation-guide","Separation Guide"),
  ("family-law-mediation","Family Law Mediation"),
  ("consent-orders-explained","Consent Orders Explained")],
 read_min=10
)
