"""gen_blog_batch22.py — Two new cornerstones:
1. section-60i-certificate-guide         — Complete guide to the s60I FDR certificate
2. relocation-with-children-after-separation — Australian law on relocating with children
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, key_takeaway, inline_cta, callout
from authority_sources import cite


# ── POST 1: SECTION 60I CERTIFICATE GUIDE ────────────────────────────────────

post(
    "section-60i-certificate-guide",
    "Section 60I Certificate: Your Complete Guide",
    "What a Section 60I FDR certificate is, when you need one, the four types, "
    "exemptions, how to get one, and what it means for your parenting application.",
    "Family law mediation",
    "Section 60I Certificates <em>Explained</em>",
    ("If you're hoping to file for parenting orders in the Federal Circuit and Family "
     "Court of Australia — orders about where your children live, how much time they "
     "spend with each parent, or parental responsibility — you will almost certainly "
     "need a Section 60I certificate before the court will accept your application. "
     "Many parents are caught off guard by this requirement, and end up delaying a court "
     "filing because they don't yet have one. This guide explains exactly what the "
     "certificate is, which type you'll receive, and what happens next."),
    [
        ("what-is-s60i",       "What is a Section 60I FDR certificate?"),
        ("when-you-need-one",  "When you need a Section 60I certificate"),
        ("four-types",         "The four types of Section 60I certificate"),
        ("exemptions",         "Exemptions: when you don't need to attend FDR"),
        ("how-to-get-one",     "How to get a Section 60I certificate"),
        ("how-long-valid",     "How long is the certificate valid?"),
        ("western-australia",  "A note on Western Australia"),
        ("what-comes-next",    "After the certificate: what comes next"),
    ],
    key_takeaway(
        "A Section 60I certificate is a document issued by an accredited Family Dispute "
        "Resolution (FDR) practitioner — such as a registered mediator — confirming that "
        "you have attended, attempted, or been assessed as exempt from FDR before applying "
        "for parenting orders. It is a legal requirement under section 60I of the "
        "Family Law Act 1975 (Cth) for most parenting applications filed in the Federal "
        "Circuit and Family Court of Australia. Without the right certificate, the court "
        "will not accept your application."
    )
    + f"""
<h2 id="what-is-s60i">What is a Section 60I FDR certificate?</h2>
<p>Under {cite('family_law_act')}, parties seeking parenting orders must first attempt
Family Dispute Resolution — a structured, impartial process where an accredited practitioner
helps both parents try to reach an agreement about their children's arrangements. After
completing (or attempting) FDR, the practitioner issues a certificate under section 60I(5)
of the Act confirming what occurred. That certificate — commonly called a "Section 60I
certificate" or "FDR certificate" — is the document you file with your court application.</p>
<p>The purpose of the requirement is straightforward: courts want parents to attempt
resolution before consuming court time and resources. Where parents do reach an agreement
at FDR, a court application may not be necessary at all — the agreement can be formalised
as <a href="/consent-orders-explained/">consent orders</a> or a
<a href="/parenting-plans-guide/">parenting plan</a> without a judge ever being involved.</p>
<p>The certificate is issued by an {cite('amdras')}-accredited FDR practitioner,
which is the qualification the government requires of mediators offering this service.
Mediations Australia's practitioners hold this accreditation and issue Section 60I
certificates as part of their family dispute resolution service.</p>
"""
    + inline_cta("Need to start FDR and get your Section 60I certificate? Book a free initial consultation to discuss your situation.")
    + f"""
<h2 id="when-you-need-one">When you need a Section 60I certificate</h2>
<p>You need a Section 60I certificate when you are filing an application for a
<strong>parenting order</strong> — including applications about:</p>
<ul>
  <li>Who a child lives with (what was previously called "residence")</li>
  <li>The time a child spends with each parent (previously called "contact" or "access")</li>
  <li>Parental responsibility — who makes major long-term decisions for a child</li>
  <li>Communication between a child and a parent or other person</li>
  <li>Any other aspect of the care, welfare, or development of a child</li>
</ul>
<p>You do <strong>not</strong> need a Section 60I certificate for purely financial applications
(property settlement, spousal maintenance, child support), consent orders, or for applications
that fall within the exemptions listed below.</p>
<figure class="tbl"><table><caption>When a Section 60I certificate is required</caption>
<thead><tr><th>Application type</th><th>Certificate required?</th></tr></thead>
<tbody>
<tr><td>Parenting orders (live-with, spend time, parental responsibility)</td><td>Yes — unless exempt</td></tr>
<tr><td>Consent orders (parenting)</td><td>No — consent orders are exempt</td></tr>
<tr><td>Property settlement / financial orders</td><td>No</td></tr>
<tr><td>Child support</td><td>No (separate system)</td></tr>
<tr><td>Urgent interim parenting orders</td><td>No — urgency is an exemption</td></tr>
<tr><td>Variation of existing parenting orders</td><td>Usually yes, unless exempt</td></tr>
</tbody></table></figure>
"""
    + inline_cta("Unsure whether you need a certificate for your application? A free consultation will clarify your exact situation.")
    + f"""
<h2 id="four-types">The four types of Section 60I certificate</h2>
<p>There are four types of Section 60I certificate, and which one you receive matters —
because the certificate tells the court exactly what happened at FDR, and the type can
affect how the court views the parties' conduct.</p>
<figure class="tbl"><table><caption>The four Section 60I certificate types</caption>
<thead><tr><th>Certificate type</th><th>What it means</th><th>Can you file for court orders?</th></tr></thead>
<tbody>
<tr>
  <td><strong>Type 1</strong></td>
  <td>The other party refused or failed to attend FDR</td>
  <td>Yes</td>
</tr>
<tr>
  <td><strong>Type 2</strong></td>
  <td>The FDR practitioner assessed that the matter was not appropriate for FDR
  (for example, because of concerns about family violence or safety)</td>
  <td>Yes</td>
</tr>
<tr>
  <td><strong>Type 3</strong></td>
  <td>One or both parties attended FDR but did not make a genuine effort to resolve the dispute</td>
  <td>Yes — but the court may take the failure into account</td>
</tr>
<tr>
  <td><strong>Type 4</strong></td>
  <td>Both parties attended FDR, made a genuine effort, but were unable to reach agreement</td>
  <td>Yes</td>
</tr>
</tbody></table></figure>
<p>A Type 3 certificate — where a party is found not to have made a genuine effort — carries
a consequence: under {cite('family_law_act')}, the court may take that failure into account
when making orders about costs. In practice, this creates a genuine incentive for both
parents to engage constructively at FDR rather than simply attending to tick a box.</p>
<p>A Type 4 certificate is the most common outcome when both parties attend and engage but
simply cannot bridge their differences at the table. It confirms that FDR was attempted
in good faith, and it allows you to file your application with the court if needed.</p>
"""
    + inline_cta("Our mediators help both parties engage constructively at FDR — the kind of genuine effort that leads to better outcomes.")
    + f"""
<h2 id="exemptions">Exemptions: when you don't need to attend FDR</h2>
<p>Section 60I(9) of the {cite('family_law_act')} sets out the circumstances in which a
person may apply for parenting orders without first attending FDR and without a Section 60I
certificate. These exemptions include:</p>
<ul>
  <li><strong>Family violence or child abuse:</strong> where there has been, or there is
  a risk of, family violence, or abuse or risk of abuse of a child</li>
  <li><strong>Urgency:</strong> where the matter is urgent</li>
  <li><strong>Consent orders:</strong> where the application is by consent of all parties</li>
  <li><strong>Contravention:</strong> where a court order has been contravened and there
  are reasonable grounds to believe the contravention was intentional</li>
  <li><strong>Response applications:</strong> where the application is a response to
  another application already before the court</li>
  <li><strong>Inability to participate:</strong> where a party is unable to participate
  effectively in FDR (for example, due to incapacity or geographic remoteness that makes
  participation impractical)</li>
</ul>
<p>Even where a family violence exemption applies, it is worth speaking with an FDR
practitioner early. An experienced practitioner can assess whether <a href="/shuttle-mediation-guide/">shuttle mediation</a>
— where the parties never meet face-to-face — or another adapted format might be workable
and beneficial, even where direct contact would not be appropriate. See also our guide to
<a href="/domestic-violence-and-family-law/">domestic violence and family law</a> for more
information on safety planning in the family law process.</p>
<p>If you believe a family violence exemption applies to your situation, you should seek
legal advice before deciding how to proceed.</p>
<p><strong>1800RESPECT — 1800 737 732</strong> (free, 24/7 support for family violence)</p>
"""
    + inline_cta("Not sure whether a family violence exemption applies? Talk to us — we'll help you understand your options without pressure.")
    + f"""
<h2 id="how-to-get-one">How to get a Section 60I certificate</h2>
<p>The process for obtaining a Section 60I certificate is straightforward when both parties
are willing to engage. Here is a typical pathway:</p>
<ol>
  <li><strong>Contact an accredited FDR provider.</strong> The practitioner must hold
  accreditation under the National Mediator Accreditation System (NMAS) as a Family Dispute
  Resolution Practitioner — not all mediators hold this credential. Government-funded services
  are available through {cite('ag_frc')} and the {cite('frc')}, though wait times can be
  several months. Private FDR practitioners like Mediations Australia typically have shorter
  wait times and more scheduling flexibility.</li>
  <li><strong>Initial assessment.</strong> The FDR practitioner will conduct a preliminary
  assessment — often called a MIAM or intake — to assess both parties' suitability for FDR,
  screen for family violence or safety concerns, and explain the process.</li>
  <li><strong>Attend FDR.</strong> Both parties (either together or separately via
  <a href="/shuttle-mediation-guide/">shuttle mediation</a>) work with the practitioner
  to try to reach an agreement. Sessions can be held in person or via
  <a href="/online-mediation-australia/">online mediation</a>.</li>
  <li><strong>Certificate issued.</strong> Whether or not agreement is reached, the
  practitioner issues a Section 60I certificate. If one party refuses to attend, the
  practitioner can issue a certificate after attempting to bring them to the table.</li>
</ol>
<figure class="tbl"><table><caption>Private vs government-funded FDR: key differences</caption>
<thead><tr><th></th><th>Government-funded FRC</th><th>Private FDR provider</th></tr></thead>
<tbody>
<tr><td>Cost</td><td>Free or low-cost (means-tested)</td><td>Fee-for-service; varies by provider</td></tr>
<tr><td>Wait time</td><td>Often 6–12 weeks or longer</td><td>Usually 1–4 weeks</td></tr>
<tr><td>Scheduling</td><td>Fixed appointment times</td><td>More flexible including evenings/online</td></tr>
<tr><td>Certificate issued</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Shuttle / online options</td><td>Available at some centres</td><td>Widely available</td></tr>
</tbody></table></figure>
"""
    + inline_cta("Our accredited FDR practitioners can usually schedule an intake assessment within a week. Book your free consultation.")
    + f"""
<h2 id="how-long-valid">How long is the certificate valid?</h2>
<p>There is no statutory expiry date on a Section 60I certificate under the
{cite('family_law_act')}. Once issued, the certificate does not automatically lapse. However,
in practice, the passage of significant time between the certificate and a court application
may be noted by the court, particularly if circumstances have changed substantially. If
your certificate is more than a year old and the matter has not yet been filed, it is worth
seeking legal advice on whether a fresh attempt at FDR — and a new certificate — would
better reflect the current situation.</p>

<h2 id="western-australia">A note on Western Australia</h2>
<p>Western Australia operates its own separate family court system — the
{cite('family_court_wa')} — under the Family Court Act 1997 (WA). While the FDR requirement
for parenting matters applies nationally, the specific procedures and forms differ from
the Federal Circuit and Family Court of Australia. If you are in WA, ensure you are working
with an FDR practitioner familiar with WA-specific processes and filing requirements.</p>

<h2 id="what-comes-next">After the certificate: what comes next</h2>
<p>Once you have your Section 60I certificate, you have three main options:</p>
<ol>
  <li><strong>File for parenting orders</strong> using the certificate. This is necessary
  where agreement has broken down and you need the court to resolve the matter.
  See our guide to the <a href="/family-court-process-2026/">family court process</a>
  for what to expect.</li>
  <li><strong>Formalise the agreement reached at FDR</strong> as <a href="/consent-orders-explained/">consent orders</a>,
  which are filed with the court but do not require a hearing. This gives the agreement
  the legal force of a court order.</li>
  <li><strong>Document the agreement as a parenting plan</strong> — a written record of
  what was agreed. A parenting plan is not legally enforceable in the same way as orders,
  but it provides clarity and a shared reference point for both parents.
  See our <a href="/parenting-plans-guide/">parenting plans guide</a> for when this works
  and when it doesn't.</li>
</ol>
<p>If you reached agreement at FDR but want it to be binding, consent orders are almost
always the better choice. For help understanding which option suits your situation, a
free initial consultation with one of our accredited mediators is a good starting point.</p>
""",
    [
        ("Can I get a Section 60I certificate without attending FDR?",
         "Yes, in certain circumstances. If the other party refuses to attend, the FDR practitioner "
         "can issue a Type 1 certificate without both parties being present. If the matter is assessed "
         "as inappropriate for FDR (for example, due to family violence), a Type 2 certificate can be "
         "issued. Various other exemptions also apply — including urgency, consent orders, and "
         "contravention of orders."),
        ("What if my ex refuses to attend FDR?",
         "If the other party refuses or fails to attend FDR after being invited by the practitioner, "
         "the FDR practitioner will issue a Type 1 Section 60I certificate. This certificate allows "
         "you to file your application with the court. You are not stuck — a refusal to participate "
         "does not prevent you from proceeding."),
        ("Can I get a Section 60I certificate from any mediator?",
         "No. The practitioner must hold specific accreditation as a Family Dispute Resolution "
         "Practitioner under the National Mediator Accreditation System. Not all mediators hold this "
         "credential. Always confirm accreditation before booking FDR if you need a Section 60I "
         "certificate for a court application."),
        ("Does a Type 3 certificate hurt my chances in court?",
         "A Type 3 certificate — where a party did not make a genuine effort — can be taken into "
         "account by the court when making costs orders. It may also reflect negatively on that "
         "party's willingness to co-operate. This is why engaging genuinely in FDR matters, even "
         "when you expect to disagree."),
        ("Do I need a Section 60I certificate for property matters?",
         "No. The Section 60I certificate requirement applies only to parenting applications, not "
         "property settlement, financial orders, or child support. However, some couples choose to "
         "address parenting and financial matters together at FDR, even though only the parenting "
         "issues require a certificate."),
        ("How much does it cost to get a Section 60I certificate?",
         "Government-funded Family Relationship Centres offer free or low-cost FDR, though wait "
         "times can be long. Private FDR providers charge a professional fee that varies by provider, "
         "the complexity of the matter, and the number of sessions required. Many providers, including "
         "Mediations Australia, will confirm their fee structure upfront."),
    ],
    related=[
        ("is-family-law-mediation-compulsory", "Is Family Law Mediation Compulsory?"),
        ("parenting-plans-guide",              "Parenting Plans in Australia"),
        ("consent-orders-explained",           "Consent Orders Explained"),
        ("child-custody-mediation",            "Child Custody Mediation"),
        ("shuttle-mediation-guide",            "Shuttle Mediation"),
        ("family-court-process-2026",          "The Family Court Process in 2026"),
    ],
    read_min=10,
)


# ── POST 2: RELOCATING WITH CHILDREN AFTER SEPARATION ──────────────────────

post(
    "relocation-with-children-after-separation",
    "Relocating with Children After Separation",
    "How Australian law handles parental relocation — notice, the best-interests "
    "test, what to do if your ex objects, and why mediation is the smarter first step.",
    "Parenting &amp; children",
    "Relocating With Children <em>After Separation</em>",
    ("You've been offered a job in Brisbane. Your support network is in Adelaide. Your "
     "new partner lives in Perth. Whatever the reason, wanting to relocate after separation "
     "when children are involved is one of the most emotionally and legally complex "
     "situations in family law. There is no simple answer, but there is a clear process — "
     "and getting it right from the start can save your family from a prolonged and "
     "expensive court battle."),
    [
        ("what-counts",         "What counts as relocation in family law?"),
        ("legal-position",      "The legal position: no automatic right to relocate"),
        ("notice-and-consent",  "Notice, consent, and the first steps"),
        ("best-interests-test", "How courts decide: the best-interests test"),
        ("mediation-role",      "Why mediation is the smarter first step"),
        ("if-ex-objects",       "If your ex objects: what the court process looks like"),
        ("moving-without",      "Moving without consent: the real risks"),
        ("practical-steps",     "Practical steps when considering a move"),
    ],
    key_takeaway(
        "There is no automatic right to relocate with children after separation in Australia. "
        "If there are existing parenting orders, you generally cannot move in a way that is "
        "inconsistent with those orders without the other parent's agreement or a new court "
        "order. If there are no orders, either parent can apply to the Federal Circuit and "
        "Family Court of Australia to seek or oppose relocation — and the court will decide "
        "based on what is in the child's best interests. Attempting mediation first is "
        "strongly advisable and often leads to faster, more workable outcomes than litigation."
    )
    + f"""
<h2 id="what-counts">What counts as relocation in family law?</h2>
<p>There is no fixed distance in Australian law that triggers "relocation" rules. The
relevant question is whether the proposed move would <strong>materially affect the other
parent's ability to spend time with the child</strong> under existing parenting orders or
established arrangements. A move from Sydney's inner west to Sydney's northern beaches
probably doesn't require court approval — a move from Sydney to Melbourne almost certainly
does, even if it is technically within Australia.</p>
<p>Relocation disputes most commonly arise when a parent wants to:</p>
<ul>
  <li>Move to a different city or state within Australia</li>
  <li>Move to another country (international relocation)</li>
  <li>Move to a regional area that significantly increases travel times for the other parent</li>
</ul>
<p>International relocation carries additional complexity. Australia is a signatory to the
Hague Convention on the Civil Aspects of International Child Abduction — taking a child
overseas without the other parent's consent or a court order may constitute international
child abduction with serious legal consequences under both Australian and international law.
If you are considering moving overseas with children, specialist legal advice is essential
before you take any steps.</p>
"""
    + inline_cta("Considering a move? A free consultation with one of our mediators helps you understand your position before committing to anything.")
    + f"""
<h2 id="legal-position">The legal position: no automatic right to relocate</h2>
<p>Under the {cite('family_law_act')}, neither parent has an automatic right to relocate
with a child. If there are existing parenting orders, moving in a way that is inconsistent
with those orders — for example, if they specify the child living in a particular city or
school zone, or require regular face-to-face time with the other parent that would become
impractical — can constitute a breach of those orders.</p>
<p>If there are no parenting orders in place, either parent is technically free to move —
but the other parent can file an application with the {cite('fcfcoa')} seeking orders to
prevent or reverse the relocation. In urgent cases, a court can issue interim orders very
quickly — sometimes within days — preventing a relocation from taking effect while the
matter is before the court.</p>
<figure class="tbl"><table><caption>Relocation and existing orders: what you can and can't do</caption>
<thead><tr><th>Situation</th><th>What you can do</th><th>What you need</th></tr></thead>
<tbody>
<tr>
  <td>No existing parenting orders</td>
  <td>Move, but other parent can immediately apply for orders</td>
  <td>Best to have consent or seek orders proactively</td>
</tr>
<tr>
  <td>Existing orders — move consistent with them</td>
  <td>Move without a new order</td>
  <td>Notify the other parent; document carefully</td>
</tr>
<tr>
  <td>Existing orders — move would be inconsistent</td>
  <td>Cannot move without new order or agreement</td>
  <td>Other parent's consent (in writing) or court order</td>
</tr>
<tr>
  <td>International relocation (any situation)</td>
  <td>Cannot move without agreement or court order</td>
  <td>Written consent of all with parental responsibility, or court order</td>
</tr>
</tbody></table></figure>
"""
    + inline_cta("Already have parenting orders and thinking of moving? Talk to us before acting — the wrong step now creates much bigger problems.")
    + f"""
<h2 id="notice-and-consent">Notice, consent, and the first steps</h2>
<p>The practical first step when considering relocation is to <strong>give the other parent
genuine notice and an opportunity to discuss the proposal</strong>. This is not just courtesy
— it is what courts expect to see evidence of, and it dramatically improves the prospects
of reaching agreement without litigation.</p>
<p>Practical notice means:</p>
<ul>
  <li>Putting your proposal in writing, including when you're thinking of moving and what
  arrangements you're proposing for the children's ongoing time with the other parent</li>
  <li>Giving enough lead time for the other parent to consider the proposal properly — at
  least several weeks, and ideally months in advance</li>
  <li>Not presenting the move as a done deal before agreement has been reached</li>
</ul>
<p>If the other parent consents in writing, and there are no existing court orders that
would be breached, the relocation can proceed. The written agreement should be specific
about the new address, school, and what the new parenting arrangements will look like.
For this kind of agreement to be enforceable, it should be made into <a href="/consent-orders-explained/">consent orders</a>
or a <a href="/parenting-plans-guide/">detailed parenting plan</a> — a verbal agreement
is not sufficient if things later break down.</p>
"""
    + inline_cta("Want to move but need the other parent on board? Our mediators have helped hundreds of families reach workable relocation agreements.")
    + f"""
<h2 id="best-interests-test">How courts decide: the best-interests test</h2>
<p>When a relocation dispute reaches court, the judge's sole focus is on <strong>what
is in the best interests of the child</strong> — not what is best or most convenient
for either parent. Following the 2023 amendments to the {cite('family_law_act')}, the
court applies a refined best-interests framework, with the primary considerations being:</p>
<ul>
  <li>The benefit to the child of having a meaningful relationship with both parents
  (and other significant people, such as grandparents)</li>
  <li>The need to protect the child from family violence, abuse, or harm</li>
</ul>
<p>Beyond those, the court considers any other relevant factor — including the reason for
the proposed move, whether it is genuine (a job offer, family support) or motivated by a
desire to limit the other parent's contact, and what the practical impact on the child's
relationship with each parent would be if the move did or didn't proceed.</p>
<p>There is no presumption in favour of relocation. A genuine, reasonable reason for the
move is necessary but not sufficient — the court will still examine the impact on the
child. The relocating parent carries the practical burden of demonstrating that the move
serves the child's best interests, not just their own.</p>
<p>Courts look favourably on parents who can propose detailed, workable arrangements to
preserve the child's relationship with the other parent — including how travel costs
would be covered, what school holidays would look like, and how communication would be
maintained. Coming to court with a vague proposal rarely succeeds.</p>
"""
    + inline_cta("Mediation helps you build a proposal the court — or the other parent — can actually accept. Book a free consultation.")
    + f"""
<h2 id="mediation-role">Why mediation is the smarter first step</h2>
<p>Relocation disputes are among the most acrimonious in family law — and among the most
suited to mediation, for exactly that reason. Unlike a judge, a mediator gives both parents
space to explain what they actually need, not just what they're legally asking for. The
parent wanting to move might need to be closer to family support during a difficult time.
The parent staying behind might be terrified of losing meaningful contact with the child.
Mediation surfaces those real concerns in a way that a court application usually does not.</p>
<figure class="tbl"><table><caption>Mediation vs court for relocation disputes</caption>
<thead><tr><th></th><th>Mediation</th><th>Court</th></tr></thead>
<tbody>
<tr><td>Timeframe</td><td>Often 1–4 sessions over weeks</td><td>Months to years for a final hearing</td></tr>
<tr><td>Cost</td><td>Fraction of litigation costs</td><td>Tens of thousands of dollars per side</td></tr>
<tr><td>Who decides</td><td>The parents — with the child's interests central</td><td>A judge, based on affidavits and expert evidence</td></tr>
<tr><td>Flexibility</td><td>Creative arrangements possible (block access, travel cost sharing)</td><td>Limited to what the court can order</td></tr>
<tr><td>Relationship impact</td><td>Less adversarial; future co-parenting preserved</td><td>Often permanently damages co-parenting relationship</td></tr>
</tbody></table></figure>
<p>Reaching a mediated agreement also means the outcome reflects both parents' genuine
commitment — rather than court-imposed arrangements that neither parent may have truly
accepted. Agreements reached at <a href="/co-parenting-mediation/">co-parenting mediation</a>
or <a href="/child-custody-mediation/">family dispute resolution</a> tend to last longer
and break down less frequently than court-ordered arrangements, because both parents had
a hand in designing them.</p>
<p>Even if you are prepared to go to court, demonstrating that you genuinely attempted
mediation first strengthens your position significantly — and if the other parent refuses
to engage, you will receive a Section 60I certificate that allows you to file your
application immediately. See our <a href="/section-60i-certificate-guide/">Section 60I
certificate guide</a> for more on this.</p>
"""
    + inline_cta("Our mediators are experienced in relocation disputes — contact us before filing or before being served.")
    + f"""
<h2 id="if-ex-objects">If your ex objects: what the court process looks like</h2>
<p>If the other parent refuses to consent to the relocation and mediation does not
resolve the matter, the relocating parent must either abandon the proposed move or apply
to the {cite('fcfcoa')} for permission to relocate. The opposing parent can also apply
for an order preventing the move.</p>
<p>In urgent cases — where a parent believes the other is about to move without consent —
the court can issue an <strong>urgent interim order</strong> within days, effectively
preventing the relocation until the full hearing. Courts take unilateral relocation very
seriously. The process from interim orders to a final hearing on a relocation dispute
can take twelve months or more, with significant legal costs for both parties.</p>
<p>If the matter goes to a final hearing, both parents will typically need to file
affidavit evidence setting out their position. The court may also order a family report
from a family consultant, and in complex cases may appoint an Independent Children's
Lawyer to represent the child's interests. See our <a href="/family-court-process-2026/">guide to the family court process</a>
for a fuller picture of what to expect at each stage.</p>

<h2 id="moving-without">Moving without consent: the real risks</h2>
<p>Taking children interstate or overseas without the other parent's consent — or in
breach of existing parenting orders — is one of the most serious steps a parent can take
in the family law context. It can constitute a contravention of court orders (with
significant penalties including fines or even imprisonment for repeated contraventions).
In the case of international relocation, it may amount to international child abduction
under the Hague Convention.</p>
<p>Practically, courts tend to view unilateral relocation very poorly. A parent who
simply moves and then applies for orders faces a significant uphill battle, because the
court may see the move as an attempt to create a fait accompli and undermine the other
parent's relationship with the child. In some cases, courts have ordered that a child
be returned to their previous location pending a full hearing, even where the child had
already settled into a new school and community.</p>
<p>The short-term convenience of moving first rarely outweighs the long-term legal and
practical consequences. If you are feeling pressure to act quickly, speak with an FDR
practitioner or lawyer before doing so.</p>
"""
    + inline_cta("Considering acting without agreement? Please speak with a mediator or lawyer first — the risks are real and serious.")
    + f"""
<h2 id="practical-steps">Practical steps when considering a move</h2>
<p>Whether you want to relocate or are responding to a partner who does, taking the right
steps early makes a significant difference to the outcome.</p>
<ol>
  <li><strong>Review your current orders</strong> (if any) carefully to understand whether
  the proposed move would be consistent or inconsistent with them.</li>
  <li><strong>Seek legal advice</strong> — even a brief consultation with a family lawyer
  will help you understand your specific position before taking any steps.</li>
  <li><strong>Propose the move in writing</strong> to the other parent, with enough notice
  and a genuine proposal for how the children's relationship with them would be maintained.</li>
  <li><strong>Attempt mediation.</strong> Engage an accredited family dispute resolution
  practitioner. Even a single session can resolve matters that seemed impossible in direct
  communication. For families with high conflict, <a href="/shuttle-mediation-guide/">shuttle
  mediation</a> means the parties never need to be in the same room.</li>
  <li><strong>If agreement is reached, formalise it</strong> as consent orders or a detailed
  parenting plan before moving, not after.</li>
  <li><strong>If agreement is not reached</strong>, consider whether further negotiation
  — possibly with lawyers involved — might resolve the matter, or whether a court application
  is unavoidable.</li>
</ol>
<p>Relocation disputes are genuinely difficult. The law does not give either parent a
predictable outcome, because every family's circumstances are different. What the law does
do is give both parents a process — and mediation is almost always the better first step
in that process.</p>
<p style="font-size:.9rem;color:var(--ink-soft);margin-top:32px;font-style:italic">This article is for general information purposes only and does not constitute legal or migration advice. For personalised guidance regarding your specific situation, please consult a qualified family lawyer or accredited mediator.</p>
""",
    [
        ("Do I need permission to move interstate with my children?",
         "If there are existing parenting orders and the move would be inconsistent with them — for "
         "example, by making regular face-to-face time with the other parent impractical — you generally "
         "need either the other parent's written consent or a new court order before moving. If there are "
         "no orders, you can technically move, but the other parent can immediately apply to the court "
         "for orders to prevent or reverse the relocation."),
        ("What if the move is for a genuine reason, like a job or family support?",
         "A genuine, reasonable reason for relocation is an important factor — courts distinguish between "
         "parents motivated by genuine necessity and those seeking to limit the other parent's relationship "
         "with the child. However, a good reason is not sufficient on its own: the court's primary focus "
         "is whether the move is in the child's best interests, which includes the impact on their "
         "relationship with the other parent."),
        ("Can my ex stop me from moving?",
         "If you have existing orders that would be breached by the move, yes — they can apply for "
         "orders enforcing those arrangements, and a court can issue urgent interim orders preventing the "
         "relocation very quickly. If there are no orders, they can apply for new orders as soon as they "
         "become aware of the proposed move. This is why engaging early and attempting mediation is always "
         "preferable to presenting the move as a done deal."),
        ("What happens if I move without permission and there are court orders?",
         "Moving in breach of court orders is a serious matter and can result in contravention "
         "proceedings, fines, or in serious cases imprisonment for repeated contraventions. Courts can "
         "also order that children be returned to their previous location pending a full hearing. The "
         "practical and legal consequences of unilateral relocation are almost always worse than the "
         "short-term inconvenience of seeking proper consent or a court order first."),
        ("Can we agree to relocation at mediation?",
         "Yes, and many families do. A mediated agreement about relocation — formalised as consent "
         "orders — can set out the new parenting arrangements in detail, including how travel costs are "
         "shared, what school holidays look like, and how communication is maintained. These agreements "
         "are enforceable as court orders and typically last longer than judge-imposed arrangements "
         "because both parents genuinely committed to them."),
    ],
    related=[
        ("child-custody-mediation",             "Child Custody Mediation"),
        ("co-parenting-mediation",              "Co-Parenting Mediation"),
        ("parenting-plans-guide",               "Parenting Plans in Australia"),
        ("section-60i-certificate-guide",       "Section 60I Certificate Guide"),
        ("family-court-process-2026",           "The Family Court Process in 2026"),
        ("shuttle-mediation-guide",             "Shuttle Mediation"),
    ],
    read_min=11,
)


print("gen_blog_batch22.py: 2 new cornerstones built (section-60i-certificate-guide, relocation-with-children-after-separation)")
