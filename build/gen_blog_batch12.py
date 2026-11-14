#!/usr/bin/env python3
"""Batch 12 — Priority 2 GSC recovery: AI Overview cannibalisation victims rebuilt as cornerstones."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, inline_cta, callout, key_takeaway


def _retired_post(*a, **k):
    """Superseded by gen_blog_batch29.py (SEO recovery stage 3)."""
    return None
from authority_sources import cite

# ============================================================
# POST 1 — best-apps-for-separated-parents
# ============================================================
# best-apps-for-separated-parents: moved to gen_blog_batch33.py (Nov 2026 refresh)

# ============================================================
# POST 2 — my-ex-wont-sign-divorce-papers
# ============================================================


# ============================================================
# POST 2 — my-ex-wont-sign-divorce-papers
# ============================================================
_retired_post("my-ex-wont-sign-divorce-papers",
 "My Ex Won't Sign Divorce Papers — What Happens Now?",
 "What happens when your ex won't sign divorce papers in Australia? Divorce is granted to one party — your ex cannot block it. Here's the exact process. 2026.",
 "Divorce",
 "My Ex Won't Sign <em>the Divorce Papers</em>" "One of the most common misconceptions in Australian family law is that a spouse can block a divorce by refusing to sign. They cannot. Under the Family Law Act, divorce is granted based on one criterion: 12 months separation. Here is the exact process when your ex refuses to cooperate.",
 [("cant-block","Your ex cannot block an Australian divorce"),
  ("twelve-months","What counts as 12 months separation?"),
  ("process","The one-party divorce process step by step"),
  ("joint-vs-sole","Joint vs sole application — full comparison"),
  ("fill-application","How to fill out the divorce application"),
  ("service","Serving the application when they won't cooperate"),
  ("hearing","What happens at the divorce hearing"),
  ("contest-separation-date","What if your ex contests the separation date?"),
  ("divorce-vs-separation","Divorce vs separation — what is legally different?"),
  ("property-after-divorce","What happens to property after divorce?"),
  ("state-notes","State-specific notes"),
  ("children-divorce","Children and divorce"),
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

<h2 id="twelve-months">What Counts as 12 Months Separation?</h2>
<p>The 12-month separation requirement under the {cite('family_law_act')} is more flexible than most
people assume. Separation is a state of fact and intent — not a legal event triggered by moving out.
Here is how the most common scenarios are treated.</p>

<h3>Same-roof separation</h3>
<p>You can be legally separated while still living in the same home. This commonly occurs when
neither party can afford to move, when one parent needs to stay for school term continuity, or
when the property cannot be sold quickly. Courts accept same-roof separation provided you can
demonstrate that the marital relationship had ended.</p>
<p>What evidence is needed for same-roof separation:</p>
<ul>
  <li><strong>Separate bedrooms</strong> — affidavit evidence from one or both parties confirming this</li>
  <li><strong>Separate finances</strong> — bank statements showing separate accounts opened after the separation date</li>
  <li><strong>Social evidence</strong> — an affidavit from a friend, family member, or neighbour who knew the parties and can confirm they presented as separated (not as a couple)</li>
  <li><strong>Domestic separation</strong> — no longer sharing meals regularly, no longer performing domestic tasks for each other as a couple</li>
</ul>
<p>The supporting affidavit from a third party is important. The court requires at least one
corroborating affidavit in same-roof separation cases where only one party is applying.</p>

<h3>Brief reconciliation attempts — do they reset the clock?</h3>
<p>Many couples try to reconcile after separating. A brief reconciliation attempt does not automatically
reset the 12-month separation clock — but it must be short. Under section 50 of the
{cite('family_law_act')}, a period of resumption of cohabitation of up to three months is
disregarded for the purposes of calculating the separation period, provided the parties
subsequently separated again.</p>
<p>In practical terms:</p>
<ul>
  <li>If you separated, got back together for six weeks, then separated again — the six weeks does not
  reset the clock. Your original separation date still counts as the start.</li>
  <li>If you reconciled for four months or more and then separated again, the clock restarts from the
  new separation date.</li>
  <li>You can use this provision only once. Multiple short reconciliation attempts that cumulatively
  exceed three months may cause problems.</li>
</ul>
<p>If you have had a reconciliation attempt, disclose it honestly in your application. Courts treat
attempted reconciliation as a positive factor — it shows both parties made an effort.</p>

<h3>Overseas separation</h3>
<p>Separation that occurred while one or both parties were living overseas counts toward the 12-month
requirement. You do not need to have been in Australia for any part of the separation period.
What matters is that at least one party is currently an Australian citizen, is domiciled in
Australia, or has been ordinarily resident in Australia for the 12 months immediately before
filing. Evidence of overseas separation may include:</p>
<ul>
  <li>Emails or correspondence between the parties from the separation period</li>
  <li>Statutory declarations from people who knew the parties overseas</li>
  <li>Records showing separate addresses (lease agreements, utility bills)</li>
</ul>
<p>If your ex is currently overseas, there are special service rules — covered in the service
section below.</p>

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

<h2 id="joint-vs-sole">Joint Application vs Sole Application — Full Comparison</h2>
<p>When your ex refuses to cooperate, you proceed as a sole applicant. Here is exactly how the two
pathways differ in cost, attendance, and timeline.</p>

<table>
  <thead>
    <tr>
      <th>Factor</th>
      <th>Joint application</th>
      <th>Sole application</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Who can use it</strong></td>
      <td>Both parties agree to apply together</td>
      <td>One party applies; the other does not need to agree or sign</td>
    </tr>
    <tr>
      <td><strong>Filing fee (2026)</strong></td>
      <td>A$1,060 standard; A$355 reduced (split between parties if agreed)</td>
      <td>A$1,060 standard; A$355 reduced (paid by applicant alone)</td>
    </tr>
    <tr>
      <td><strong>Service requirement</strong></td>
      <td>Not required — both parties signed the application</td>
      <td>Mandatory — applicant must serve the respondent and file proof of service</td>
    </tr>
    <tr>
      <td><strong>Attendance at hearing</strong></td>
      <td>Not required if no children under 18</td>
      <td>Required if there are children under 18; optional otherwise (but court may require attendance)</td>
    </tr>
    <tr>
      <td><strong>Processing time</strong></td>
      <td>3–5 months from filing to hearing</td>
      <td>3–5 months from filing to hearing (same — service adds 4–6 weeks of preparation)</td>
    </tr>
    <tr>
      <td><strong>Risk of delay</strong></td>
      <td>Low — no service issues, no potential objections</td>
      <td>Medium — service problems or a separation date dispute can delay the hearing</td>
    </tr>
    <tr>
      <td><strong>Complexity</strong></td>
      <td>Lower — shorter form, no affidavit of service required</td>
      <td>Higher — applicant must prepare affidavit of service; may need supporting affidavits for same-roof or overseas separation</td>
    </tr>
    <tr>
      <td><strong>Respondent's options</strong></td>
      <td>N/A — both parties are applicants</td>
      <td>Respondent may attend the hearing and raise a procedural objection (rare)</td>
    </tr>
  </tbody>
</table>

<p>The practical conclusion: a sole application costs the same as a joint application and takes roughly
the same time. The only additional steps are service and, where relevant, a supporting affidavit.
Do not wait for your ex to agree — apply now.</p>
"""
 + inline_cta("Not sure which application pathway suits your situation? We can walk you through it — or help you resolve outstanding property and parenting issues through mediation first.")
 + f"""
<h2 id="fill-application">How to Fill Out the Divorce Application — Step by Step</h2>
<p>The divorce application is filed through the {cite('comcourts_portal')}. You do not need a lawyer
to do this, but the form requires care. Here is a walkthrough of the key steps.</p>

<h3>Step 1 — Create a Commonwealth Courts Portal account</h3>
<p>Go to comcourts.gov.au and register for a free account. You will need a valid email address and
identification documents. Once registered, select "eLodgment" and then "Divorce application."</p>

<h3>Step 2 — Choose joint or sole application</h3>
<p>If your ex will not cooperate, select "Sole application." The form will then ask you to provide
the respondent's (your ex's) details for the purpose of service.</p>

<h3>Step 3 — Complete the application form</h3>
<p>Key sections of the form:</p>
<ul>
  <li><strong>Marriage details</strong> — date, location, and country of marriage. You will need to attach
  a marriage certificate (original or certified copy). If your marriage was overseas, you may need a
  translated certificate.</li>
  <li><strong>Separation date</strong> — enter the date you separated. If you lived under the same roof
  after separating, tick the "separated under one roof" box and be prepared to file a supporting affidavit.</li>
  <li><strong>Children</strong> — list all children of the marriage under 18. The court requires a brief
  statement about current parenting arrangements. This does not need to be a formal parenting plan, but
  it must show the court that proper arrangements exist.</li>
  <li><strong>Respondent's address</strong> — enter your ex's last known address. This is where the
  documents will be served.</li>
</ul>

<h3>Step 4 — Attach required documents</h3>
<p>You must attach:</p>
<ul>
  <li>A certified copy of your marriage certificate (or an affidavit explaining why you cannot obtain it)</li>
  <li>If applicable: a translator's certificate for a non-English marriage certificate</li>
  <li>If applicable: a supporting affidavit for same-roof separation (signed before a Justice of the Peace or solicitor)</li>
</ul>

<h3>Step 5 — Pay the filing fee</h3>
<p>The standard fee is A$1,060 (2026). Check the current {cite('fcfcoa_fees')} page before filing as fees
are indexed annually. You may be eligible for the reduced fee of A$355 if you:</p>
<ul>
  <li>Hold a current Health Care Card or Pensioner Concession Card</li>
  <li>Are experiencing financial hardship (requires a statutory declaration)</li>
  <li>Receive certain Centrelink payments including JobSeeker, Youth Allowance, or Austudy</li>
</ul>
<p>Reduced fee eligibility is assessed at the time of filing. You will be prompted to upload evidence
of your concession card or hardship declaration during the online lodgement process.</p>

<h3>Step 6 — Receive your hearing date</h3>
<p>After filing, the court allocates a hearing date — typically 3–5 months from the filing date. You
will receive the date by email through the Portal. You then have the respondent served before the
service deadline (at least 28 days before the hearing, or 42 days if overseas).</p>

{callout("Keep a copy of everything you file",
"Download and save a PDF copy of your completed application and all attachments immediately after lodgement. If the Portal has a technical issue or your account becomes inaccessible, you will need this copy to verify what was filed.")}

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

<h2 id="contest-separation-date">What If Your Ex Contests the Separation Date?</h2>
<p>A separation date dispute is the most common (and almost the only legitimate) objection your
ex can raise at a divorce hearing. Here is how the court handles it.</p>

<h3>Why the separation date matters</h3>
<p>The separation date determines whether the 12-month requirement is met. If your ex claims
you did not separate until a later date, they may be arguing the 12 months has not elapsed.
In some cases, one party disputes the date for tactical reasons — for example, to delay the
divorce while property settlement or spousal maintenance negotiations continue.</p>

<h3>What evidence the court considers</h3>
<p>If your ex contests the separation date, the court considers:</p>
<ul>
  <li><strong>Contemporaneous documentary evidence</strong> — emails, text messages, or letters
  from around the claimed separation date that are consistent with separation (for example,
  messages referring to moving out, dividing property, or telling people about the separation)</li>
  <li><strong>Financial records</strong> — bank accounts opened separately, joint accounts frozen
  or split, changes to insurance or superannuation beneficiary nominations</li>
  <li><strong>Third-party affidavits</strong> — evidence from friends, family, or a counsellor
  who knew the parties at the time</li>
  <li><strong>Living arrangements</strong> — lease agreements, utility bills, or other records
  showing separate addresses</li>
  <li><strong>Communication patterns</strong> — a sudden shift from regular couple communication
  to formal or reduced contact</li>
</ul>

<h3>How courts typically rule</h3>
<p>Courts are pragmatic about separation date disputes. The question is not whether both parties
agreed they were separated — it is when, objectively, the marriage broke down. Courts have
accepted separation dates where one party did not initially accept the separation but where
the evidence shows the relationship had irretrievably ended.</p>
<p>Generic example: A and B separated in March 2024. A moves out in April 2024 but B claims
the separation did not occur until A moved out. The court reviews the parties' text messages
from March 2024 — which include A explicitly stating the relationship is over — and accepts
March 2024 as the separation date. B's subjective belief that reconciliation was possible
does not override the objective evidence.</p>
<p>If your ex raises a separation date dispute and you have contemporaneous evidence, the
dispute is unlikely to succeed. Very few separation date challenges result in a divorce being
refused entirely.</p>

<h3>What if the dispute means 12 months has not elapsed?</h3>
<p>If the court accepts your ex's separation date and finds 12 months has not yet elapsed,
the divorce application will be dismissed without prejudice — meaning you can re-apply once
the 12-month period is reached. This is a procedural dismissal, not a finding against you on
the merits.</p>

<h2 id="divorce-vs-separation">Divorce vs Separation — What Is Legally Different?</h2>
<p>Many people use "separation" and "divorce" interchangeably. They are legally distinct and the
difference matters for property settlement, spousal maintenance, and remarriage.</p>

<table>
  <thead>
    <tr>
      <th>Factor</th>
      <th>Separation</th>
      <th>Divorce</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Legal definition</strong></td>
      <td>The end of the marital relationship as a matter of fact and intent — no court order required</td>
      <td>A formal court order dissolving the marriage</td>
    </tr>
    <tr>
      <td><strong>When it takes effect</strong></td>
      <td>The date both parties (or at least one party, communicated to the other) decided the marriage was over</td>
      <td>One month and one day after the divorce order is made at the hearing</td>
    </tr>
    <tr>
      <td><strong>Effect on property rights</strong></td>
      <td>Starts the limitation clock for property settlement claims (12 months from divorce to bring a claim)</td>
      <td>Finalises the clock — you have 12 months from the divorce order to bring property or maintenance claims</td>
    </tr>
    <tr>
      <td><strong>Effect on marriage</strong></td>
      <td>No legal effect — you remain legally married while separated</td>
      <td>Legal end of the marriage — you are free to remarry</td>
    </tr>
    <tr>
      <td><strong>Wills and superannuation</strong></td>
      <td>Your spouse may remain your next of kin and super beneficiary during separation</td>
      <td>In most states, divorce revokes gifts to a former spouse under a will made before the divorce</td>
    </tr>
    <tr>
      <td><strong>Required for property settlement?</strong></td>
      <td>No — you can finalise property settlement before or during divorce proceedings</td>
      <td>Not required — but the 12-month window starts from the divorce order</td>
    </tr>
  </tbody>
</table>

<p>The key practical point: you do not need to wait for the divorce order to finalise your property
settlement. In fact, settling property before or during divorce proceedings avoids the 12-month
limitation period problem entirely.</p>

<h2 id="property-after-divorce">What Happens to Property After Divorce?</h2>
<p>Divorce and property settlement are separate legal processes. The divorce order ends the marriage.
Property settlement determines who gets what from the asset pool. You can finalise property
settlement before, during, or after divorce — but there is a hard deadline you must not miss.</p>

<h3>The 12-month window</h3>
<p>Once the divorce order takes effect, you have 12 months to bring a property settlement claim
or spousal maintenance claim to court. If you miss this deadline, you generally cannot bring
a claim without obtaining special leave from the {cite('fcfcoa')} — and special leave is not
easily granted.</p>
<p>This deadline catches people who assume they can sort out property "later." If your property
settlement is not finalised or proceedings are not on foot within 12 months of the divorce order,
you may lose significant entitlements.</p>

<h3>What happens if you miss the deadline?</h3>
<p>If you miss the 12-month window, you must apply for special leave to extend time. The court
considers:</p>
<ul>
  <li>Whether there is a reasonable explanation for the delay</li>
  <li>Whether the other party would suffer prejudice if leave were granted</li>
  <li>The strength of the underlying property claim</li>
  <li>Whether granting leave would be just and equitable in all the circumstances</li>
</ul>
<p>Courts do grant special leave in genuine hardship cases, but it is not routine. Do not rely
on it as a fallback. The simplest protection is to begin mediation or file consent orders
well before the 12-month deadline.</p>

<h3>Property settlement through mediation</h3>
<p>Most property settlements are resolved through negotiation and formalised as consent orders
filed with the {cite('fcfcoa_consent_orders')} process. A property settlement mediation session
typically takes 3–6 hours and produces a heads of agreement that both parties sign. That
agreement is then drafted into consent orders and filed with the court — no hearing required
in most cases.</p>
"""
 + inline_cta("Approaching the 12-month deadline after your divorce? A single property mediation session can finalise your settlement and protect your entitlements.")
 + f"""
<h2 id="state-notes">State-Specific Notes</h2>
<p>Divorce in Australia is a federal matter governed by the {cite('family_law_act')}, which means
the process is largely the same regardless of which state or territory you live in.
However, there are important jurisdictional differences to be aware of.</p>

<h3>Western Australia — Family Court of WA</h3>
<p>Western Australia is the only state with its own family court — the {cite('family_court_wa')}.
WA residents do not file divorce applications through the Federal Circuit and Family Court of
Australia (FCFCOA). Instead, they file through the Family Court of Western Australia's own
eLodgment system. The substantive law is the same (Family Law Act 1975), and the process is
nearly identical, but the portal, fees schedule, and administrative procedures are managed by
the WA court separately. If you live in WA and attempt to file through the FCFCOA portal,
your application will not be processed correctly.</p>
<p>Key practical difference for WA residents:</p>
<ul>
  <li>File at: familycourt.wa.gov.au (not comcourts.gov.au)</li>
  <li>Hearings held at the Family Court of WA's registries (Perth, Bunbury, and regional circuits)</li>
  <li>The {cite('fcfcoa')} handles appeals from WA in federal family law matters</li>
</ul>

<h3>Northern Territory and Australian Capital Territory</h3>
<p>Residents of the NT and ACT file through the FCFCOA like all other states. However, in the NT,
hearings outside Darwin may be conducted by circuit sittings that visit regional centres on a
schedule — check current circuit dates on the FCFCOA website when planning your application
timeline. Darwin residents generally have access to regular registry sittings.</p>
<p>ACT residents file and attend hearings at the FCFCOA's Canberra registry. There is no
ACT-specific family court.</p>

<h3>Remote and regional Australia</h3>
<p>If you live in a regional or remote area without a nearby FCFCOA registry, divorce hearings
can be conducted by telephone or video link in most cases. The FCFCOA has invested in remote
hearing capability and it is now routine for applicants in regional areas to attend their
hearing by phone without travelling to a registry. Confirm this option when your hearing date
is allocated.</p>

<h2 id="children-divorce">Children and Divorce</h2>
<p>If you have children under 18 from the marriage, the court has an additional obligation before
granting a divorce. This does not mean the divorce can be blocked — it means the court must
be satisfied that proper arrangements exist for the children.</p>

<h3>What the court checks</h3>
<p>Under the {cite('family_law_act')}, when a divorce application involves children under 18,
the court must be satisfied that:</p>
<ul>
  <li>Proper arrangements have been made for the welfare of the children, or</li>
  <li>There are circumstances that make it impracticable or inappropriate to require the
  applicant to provide details of those arrangements at this time</li>
</ul>
<p>This does not require a formal parenting plan or court orders to be in place before the
divorce is granted. It is a relatively low threshold — the court is not conducting a detailed
parenting assessment. In most cases, a brief statement in the divorce application describing
the current living and care arrangements for the children is sufficient.</p>

<h3>What the statement should cover</h3>
<p>Your divorce application will ask you to describe the current arrangements for any children
under 18. Include:</p>
<ul>
  <li>Who the children currently live with (and for how many nights per week or fortnight)</li>
  <li>How schooling is managed</li>
  <li>Any existing parenting plan or consent orders (if you have them)</li>
  <li>Whether the other parent has regular time with the children</li>
</ul>
<p>You do not need to describe the arrangements in detail — a few sentences is normally adequate.
The court is looking for evidence that the children are not being neglected or that their needs
are not being completely unaddressed during the divorce proceedings.</p>

<h3>Divorce does not determine parenting arrangements</h3>
<p>The divorce order does not set out parenting arrangements, residence, or contact. Those matters
are entirely separate and are dealt with through:</p>
<ul>
  <li>A parenting plan (informal written agreement between the parents)</li>
  <li>Consent orders (formal court orders by agreement)</li>
  <li>Parenting orders made by the court after a hearing</li>
</ul>
<p>Before applying to court for parenting orders, most parents are required to attempt family
dispute resolution first. The {cite('fcfcoa_fdr')} process — commonly called mediation — is the
required first step in most parenting disputes.</p>

{callout("Parenting arrangements and divorce are separate",
"Refusing to agree on parenting arrangements does not block the divorce. But unresolved parenting disputes are often the most damaging and expensive part of separation. A parenting mediation session with an accredited mediator is typically faster, cheaper, and better for the children than contested court proceedings.")}

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
   "Yes — and often it is better to do so. Property settlement can be finalised before, during, or after divorce proceedings. The important deadline is the 12-month window after the divorce order is finalised — after that, you generally cannot bring a property settlement claim without special leave from the court."),
  ("We separated under the same roof. Do I need a supporting affidavit?",
   "Yes. Where both parties lived together for any part of the 12-month separation period, you need at least one affidavit from a third party — a friend, family member, or neighbour — who knew you during that time and can confirm the relationship had ended. You may also need your own affidavit explaining the circumstances of the same-roof separation."),
  ("We reconciled for two months during the 12-month period. Do I need to restart the clock?",
   "Not if the reconciliation attempt was three months or less. Under section 50 of the Family Law Act 1975, a single period of resumed cohabitation of up to three months is disregarded for the purposes of calculating the separation period. Disclose the reconciliation in your application — it does not prevent the divorce, and honesty reduces the risk of your ex using the reconciliation as a grounds for objection."),
  ("What happens to my will after divorce?",
   "In most Australian states and territories, a divorce order revokes any gift made to a former spouse in a will executed before the divorce. Your former spouse is also removed as executor if named. The effect is that your will is treated as if your former spouse predeceased you. To avoid unintended outcomes, update your will as soon as the divorce order takes effect — or before."),
  ("I live in Western Australia. Is the process different?",
   "The substantive law is the same — Family Law Act 1975 — but WA residents file through the Family Court of Western Australia, not the Federal Circuit and Family Court of Australia. Use familycourt.wa.gov.au rather than comcourts.gov.au. Filing through the wrong portal will cause your application to be rejected or processed incorrectly.")],
 [("separation-guide","Separation Guide"),
  ("property-settlement-mediation-guide","Property Settlement Mediation"),
  ("cost-of-divorce-in-australia","Cost of Divorce in Australia"),
  ("superannuation-and-divorce","Superannuation and Divorce"),
  ("family-law-mediation","Family Law Mediation"),
  ("how-mediation-works","How Mediation Works")],
 read_min=18
)

# ============================================================
# POST 3 — who-pays-bills-during-separation
# ============================================================
# who-pays-bills-during-separation: moved to gen_blog_batch33.py (Nov 2026 refresh)
