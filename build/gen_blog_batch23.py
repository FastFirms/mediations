"""gen_blog_batch23.py — Two new cornerstones:
1. what-age-can-a-child-choose-which-parent-to-live-with — children's views in Australian family law
2. hiding-assets-in-divorce — hidden assets, the duty of disclosure and what to do about it
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, key_takeaway, inline_cta, callout
from authority_sources import cite


# ── POST 1: WHAT AGE CAN A CHILD CHOOSE WHICH PARENT TO LIVE WITH ────────────

post(
    "what-age-can-a-child-choose-which-parent-to-live-with",
    "What Age Can a Child Choose Which Parent to Live With?",
    "There is no set age in Australia. How courts weigh a child's views, how those views "
    "are heard, and how child-inclusive mediation gives children a voice.",
    "Parenting &amp; children",
    "What age can a child <em>choose a parent</em>?",
    ("It is one of the most common questions separated parents ask — and one of the most "
     "misunderstood. Many people believe a child gets to decide at 12, or 14, or 16. In "
     "Australia, no such rule exists. A child's views matter, and they matter more as the "
     "child matures, but they are one factor in a wider best-interests assessment. This guide "
     "explains how children's wishes are actually heard, and why the quietest path to hearing "
     "them is rarely a courtroom."),
    [
        ("no-fixed-age",        "Is there a legal age a child can choose?"),
        ("how-courts-weigh",    "How the law weighs a child's views"),
        ("age-and-maturity",    "Age, maturity and the weight given to views"),
        ("how-views-are-heard", "How a child's views are actually heard"),
        ("teenagers",           "Teenagers who 'vote with their feet'"),
        ("pressure",            "Pressure, loyalty conflicts and coaching"),
        ("child-inclusive",     "Child-inclusive mediation: a gentler way to listen"),
        ("next-steps",          "Practical next steps for parents"),
    ],
    key_takeaway(
        "There is no age in Australia at which a child can legally choose which parent to live "
        "with. Under the Family Law Act 1975, a child's views are one of the matters considered "
        "in deciding what is in their best interests, and those views carry more weight as the "
        "child grows older and more mature. Parenting orders end at 18, and in practice the views "
        "of mature teenagers are very influential — but the decision is never simply handed to the child."
    )
    + f"""
<h2 id="no-fixed-age">Is there a legal age a child can choose?</h2>
<p>No. Unlike some overseas jurisdictions where a particular birthday is often discussed as a
turning point, Australian family law does not set an age at which a child gets to decide where
they live. The {cite('family_law_act')} requires decision-makers to treat the child's best
interests as the paramount consideration, and a child's expressed views are one of the matters
considered within that assessment — not a trump card.</p>
<p>That said, the reality on the ground is more nuanced than "the child has no say". A parenting
order ends when a child turns 18, and courts are well aware that orders forcing a determined
16-year-old to live somewhere they refuse to go are hard to enforce and can damage the child's
relationship with both parents. The older and more mature the child, the more their views
tend to shape the outcome.</p>
<p>For most families, the more useful question is not "when can my child choose?" but "how do
we make sure our child feels heard, without putting the weight of the decision on their
shoulders?" That is where <a href="/child-custody-mediation/">child custody mediation</a> and a
well-drafted <a href="/parenting-plans-guide/">parenting plan</a> come in.</p>
"""
    + inline_cta("Want your child's perspective considered without putting them in the middle? Talk to us about child-focused mediation.")
    + f"""
<h2 id="how-courts-weigh">How the law weighs a child's views</h2>
<p>Following amendments that commenced in May 2024, the best-interests factors in the
{cite('family_law_act')} were simplified. Courts now consider a short list of general matters,
which include the child's safety, their developmental, psychological, emotional and cultural
needs, the capacity of each parent to meet those needs, the benefit of maintaining relationships
with both parents and other significant people (where safe), and <strong>any views expressed by
the child</strong>.</p>
<p>Notice the wording: <em>views expressed</em>, not <em>wishes obeyed</em>. The law also says a
child is never required to express a view. Children may say nothing at all, and that is
respected too. A judge — or, more often, two parents negotiating with a mediator — weighs what
the child says alongside everything else that affects their wellbeing.</p>
<figure class="tbl"><table><caption>How a child's views fit into the best-interests assessment</caption>
<thead><tr><th>What the law considers</th><th>Where the child's view fits</th></tr></thead>
<tbody>
<tr><td>Safety from family violence, abuse or neglect</td><td>Safety concerns override a stated preference</td></tr>
<tr><td>The child's developmental and emotional needs</td><td>Views help reveal what the child needs</td></tr>
<tr><td>Each parent's capacity to meet those needs</td><td>Views are tested against practical capacity</td></tr>
<tr><td>Relationships with both parents (where safe)</td><td>A preference for one home rarely means no time in the other</td></tr>
<tr><td>Any views expressed by the child</td><td>Weighed according to age, maturity and understanding</td></tr>
</tbody></table></figure>
<p class="source-note">Summary of the general best-interests considerations; see the Act for the full wording.</p>
"""
    + inline_cta("Every family's facts are different. A free consultation can help you understand how these factors apply to your children.")
    + f"""
<h2 id="age-and-maturity">Age, maturity and the weight given to views</h2>
<p>Courts and family consultants look past the number on the birthday cake to the quality of the
view itself. Is it consistent over time? Does the child understand what living arrangements mean
in practice — school, friends, travel, the other household? Is the view the child's own, or does
it echo a parent's language? Research published by the {cite('aifs')} has consistently found that
children want to be <em>heard</em> in separation decisions, but most do not want to be the ones
who decide.</p>
<figure class="tbl"><table><caption>A general guide to how views tend to be weighed</caption>
<thead><tr><th>Age range</th><th>Typical weight</th><th>What usually matters most</th></tr></thead>
<tbody>
<tr><td>Under 7</td><td>Limited</td><td>Attachment, routine, stability and safety</td></tr>
<tr><td>7–11</td><td>Moderate</td><td>Views explored gently; reasons matter more than the preference</td></tr>
<tr><td>12–14</td><td>Significant</td><td>Consistency of view, maturity, school and friendships</td></tr>
<tr><td>15–17</td><td>Often decisive in practice</td><td>Enforceability, autonomy and the relationship with each parent</td></tr>
</tbody></table></figure>
<p class="source-note">An indicative guide only — there is no legislated scale, and every child is assessed individually.</p>
"""
    + inline_cta("Parenting a teenager through separation? Mediation can build arrangements flexible enough to grow with them.")
    + f"""
<h2 id="how-views-are-heard">How a child's views are actually heard</h2>
<p>Children are almost never asked to give evidence or sit in a courtroom. Instead, their views
reach decision-makers indirectly, through trained professionals:</p>
<ul>
  <li><strong>Family consultants and family reports</strong> — a social scientist (usually a
  psychologist or social worker) attached to the {cite('fcfcoa')} interviews the child and
  parents and prepares a report for the court.</li>
  <li><strong>Independent Children's Lawyer (ICL)</strong> — a lawyer appointed to represent the
  child's best interests (not simply their instructions). Since 2024, ICLs are generally required
  to meet with the child, unless an exception applies.</li>
  <li><strong>Child consultants in mediation</strong> — in child-inclusive mediation, a specialist
  meets with the child separately and feeds back themes, with the child's consent, to the parents.</li>
</ul>
<p>Only the last of these happens <em>before</em> anyone files in court. It is also the only one
where the feedback goes directly to the parents so they can shape the arrangements together.
Read more about the <a href="/family-court-process-2026/">family court process in 2026</a> if you
want to understand the formal route.</p>
"""
    + inline_cta("Hear your child's perspective early — before positions harden. Ask us about child-inclusive mediation.")
    + """
<h2 id="teenagers">Teenagers who 'vote with their feet'</h2>
<p>Many parents come to mediation because a teenager has already decided. A 15-year-old stops
going to the other parent's house on changeover days; a 16-year-old moves in with a friend's
family. Technically, if there are parenting orders in place, the parent with whom the child is
living may face questions about whether the orders have been contravened. In practice, courts
recognise that a parent cannot physically force a resistant teenager into a car, and that the
reasonable response is to encourage compliance, keep communication open and seek to vary the
arrangements rather than ignore them.</p>
<p>If your existing orders no longer reflect what your teenager will realistically do, the
smarter first step is usually to mediate a variation — and record it as new
<a href="/consent-orders-explained/">consent orders</a> — rather than wait for a contravention
application. That keeps the focus on the young person's relationship with both parents rather
than on blame.</p>
"""
    + inline_cta("Existing orders no longer working for your teenager? A mediated variation is faster and calmer than a contravention dispute.")
    + f"""
<h2 id="pressure">Pressure, loyalty conflicts and coaching</h2>
<p>Asking a child to choose between parents can be one of the most stressful things a child
experiences. Children often say different things to each parent because they want to please
whoever they are with. Professionals are trained to spot this, and a view that appears to have
been coached — or that reflects one parent's grievances — tends to be given little weight. In
serious cases it may raise concerns about <a href="/parental-alienation-australia/">parental
alienation</a>.</p>
<p>Where a child's reluctance stems from fear, the picture changes. Concerns about family
violence or abuse must be taken seriously and dealt with first; mediation may not be
appropriate, and exemptions from family dispute resolution apply. If you or your children are in
immediate danger, call <strong>000</strong>. For confidential support, contact
{cite('respect_1800')} on <strong>1800 737 732</strong>, and see our guide to
<a href="/domestic-violence-and-family-law/">domestic violence and family law</a>.</p>
"""
    + callout("A simple rule for parents",
              "Tell your children they will be listened to, but that the adults will make the decision. "
              "That one sentence removes an enormous burden from a child's shoulders.")
    + inline_cta("Our accredited mediators screen every matter for safety before any joint session. Book a confidential first conversation.")
    + f"""
<h2 id="child-inclusive">Child-inclusive mediation: a gentler way to listen</h2>
<p>Child-inclusive mediation is a form of family dispute resolution in which a qualified child
consultant meets with the child (usually aged around 5 and over) in a safe, low-pressure setting.
The consultant then shares the child's experiences and worries with the parents — framed around
needs, not "votes". The {cite('frc')} service describes this child-focused approach as a way of
keeping children at the centre of arrangements without involving them in the conflict.</p>
<p>Parents often find this feedback shifts the conversation. Hearing that a child is worried
about missing sport on weekends, or anxious about changeovers, is far more useful than a
one-word answer to "who do you want to live with?". And because mediation is confidential, the
child's words are not turned into evidence in an adversarial contest. If agreement is reached,
it can become a parenting plan or consent orders; if not, the practitioner can issue a
<a href="/section-60i-certificate-guide/">Section 60I certificate</a>.</p>
"""
    + inline_cta("Child-inclusive mediation keeps your children heard and out of the middle. Book a free consultation to see if it suits your family.")
    + f"""
<h2 id="next-steps">Practical next steps for parents</h2>
<ol>
  <li><strong>Don't ask your child to choose.</strong> Ask open questions about how they are
  finding things, and listen.</li>
  <li><strong>Talk to the other parent early</strong> — directly, through a co-parenting app, or
  with a mediator — before a preference becomes a standoff.</li>
  <li><strong>Consider child-inclusive mediation</strong> for children old enough to share their
  experience safely.</li>
  <li><strong>Build flexibility into the plan.</strong> Arrangements for a 9-year-old rarely suit a
  15-year-old; agree on review points.</li>
  <li><strong>Formalise what you agree.</strong> Parenting plans are flexible; consent orders are
  enforceable. Information on parenting arrangements is available from {cite('fcfcoa_fdr')}.</li>
</ol>
<p>Court has its place — particularly where safety is at risk — but for the vast majority of
families, a child's voice is best heard in a room designed for listening, not for contest.</p>
"""
    + inline_cta("Ready to build arrangements that reflect your child's voice? Our family law mediators can help you start today."),
    [
        ("Can a 12-year-old choose which parent to live with in Australia?",
         "Not on their own. There is no age at which a child can legally decide. A 12-year-old's views "
         "will usually be given significant weight if they are consistent and genuinely their own, but they "
         "are considered alongside safety, the child's needs and each parent's capacity under the "
         "best-interests test."),
        ("At what age does a child's opinion matter in family court?",
         "A child's views can be considered at any age, but the weight increases with age and maturity. "
         "Views of very young children are given limited weight, while the consistent, well-reasoned views "
         "of mid-to-late teenagers are often highly influential in practice."),
        ("Can a 16-year-old refuse to see a parent?",
         "Practically, it is very difficult to force a 16-year-old to spend time with a parent. If there are "
         "orders in place, the parent the child lives with should encourage compliance and may need to seek a "
         "variation. Mediation is often the fastest way to agree new arrangements that the young person will "
         "actually follow."),
        ("Will my child have to speak to a judge?",
         "Almost never. Children's views usually reach the court through a family consultant's report or an "
         "Independent Children's Lawyer. In mediation, a child consultant may meet with the child and share "
         "themes with the parents, with the child's consent."),
        ("When do parenting orders stop applying?",
         "Parenting orders cease when a child turns 18, or if the child marries or enters a de facto "
         "relationship. Child support may continue until the end of the school year in which the child turns 18 "
         "in some circumstances."),
        ("What is child-inclusive mediation?",
         "It is family dispute resolution in which a trained child consultant meets with the child separately "
         "and then shares the child's experiences and concerns with the parents, helping them make "
         "child-focused decisions without asking the child to choose."),
    ],
    related=[
        ("child-custody-mediation",                    "Child Custody Mediation"),
        ("parenting-plans-guide",                      "Parenting Plans in Australia"),
        ("co-parenting-mediation",                     "Co-Parenting Mediation"),
        ("parental-alienation-australia",              "Parental Alienation in Australia"),
        ("relocation-with-children-after-separation",  "Relocating with Children After Separation"),
        ("section-60i-certificate-guide",              "Section 60I Certificate Guide"),
    ],
    read_min=10,
)


# ── POST 2: HIDING ASSETS IN DIVORCE ─────────────────────────────────────────

post(
    "hiding-assets-in-divorce",
    "Hiding Assets in Divorce: Signs, Law and What to Do",
    "Suspect your ex is hiding assets? The duty of disclosure, warning signs, how hidden "
    "assets are uncovered, and the consequences under Australian family law.",
    "Property &amp; finances",
    "Why hiding assets in divorce <em>backfires</em>",
    ("Few things erode trust after separation faster than the suspicion that your former partner "
     "is not being honest about money. Perhaps a bank account has gone quiet, a business is "
     "suddenly 'struggling', or cash is moving to a relative. Australian family law takes hidden "
     "assets seriously — and full and frank disclosure is a legal duty, not a courtesy. This guide "
     "explains the duty, the warning signs, how assets are traced, and how to resolve a property "
     "settlement on a foundation of facts rather than suspicion."),
    [
        ("duty-of-disclosure",  "The duty of full and frank disclosure"),
        ("common-methods",      "Common ways assets are hidden"),
        ("warning-signs",       "Warning signs to look out for"),
        ("uncovering",          "How hidden assets are uncovered"),
        ("consequences",        "Consequences of hiding assets"),
        ("in-mediation",        "Disclosure in mediation"),
        ("protect-yourself",    "Protecting yourself: a practical checklist"),
        ("when-court",          "When court is the right step"),
    ],
    key_takeaway(
        "Hiding assets in a divorce or separation breaches the duty of full and frank disclosure under "
        "Australian family law. Courts can draw adverse inferences, make costs orders, add the hidden "
        "value back into the property pool, and set aside a settlement later under section 79A of the "
        "Family Law Act if it was obtained by fraud or suppressed evidence. Early, documented disclosure — "
        "whether in mediation or court — is the best protection for both parties."
    )
    + f"""
<h2 id="duty-of-disclosure">The duty of full and frank disclosure</h2>
<p>Every party to a family law property matter must disclose all information relevant to the case
— including assets, liabilities, income, financial resources and interests in trusts or companies.
The duty applies from the moment a dispute begins, continues until it is finalised, and covers
assets held in your own name, jointly, or through structures you control. The {cite('fcfcoa_disclosure')}
page sets out what the court expects.</p>
<p>From June 2025, reforms to the {cite('family_law_act')} moved the duty of disclosure out of the
court rules and into the Act itself, underlining how seriously Parliament regards it. Importantly,
the duty is the same whether you are negotiating informally, attending
<a href="/property-settlement-mediation-guide/">property settlement mediation</a>, or in front of a
judge. Disclosure is the foundation every fair settlement is built on — see our overview of
<a href="/what-is-in-the-property-pool/">what is in the property pool</a>.</p>
"""
    + inline_cta("Not sure what you need to disclose — or what to ask for? A free consultation will walk you through the essentials.")
    + f"""
<h2 id="common-methods">Common ways assets are hidden</h2>
<p>Most concealment is less sophisticated than people fear, and much of it leaves a paper trail.
The table below summarises the patterns family lawyers, forensic accountants and mediators see
most often.</p>
<figure class="tbl"><table><caption>Common concealment methods and how they are traced</caption>
<thead><tr><th>Method</th><th>What it looks like</th><th>How it is usually traced</th></tr></thead>
<tbody>
<tr><td>Transfers to family or friends</td><td>"Repaying" a relative; gifting cash or vehicles</td><td>Bank statements, loan documentation, subpoenas</td></tr>
<tr><td>Business manipulation</td><td>Deferred invoices, inflated expenses, sudden drop in profit</td><td>Financial statements, BAS, forensic accountant review</td></tr>
<tr><td>Trusts and companies</td><td>Assets held by a family trust or entity</td><td>Trust deeds, ASIC records, control analysis</td></tr>
<tr><td>Cash and undeclared income</td><td>Cash-heavy business, lifestyle exceeds declared income</td><td>Lifestyle analysis, tax returns, spending patterns</td></tr>
<tr><td>Cryptocurrency</td><td>Holdings on exchanges or private wallets</td><td>Exchange records, bank transfers to exchanges</td></tr>
<tr><td>Superannuation contributions</td><td>Unusual voluntary contributions before separation</td><td>Fund statements and contribution history</td></tr>
<tr><td>Undervaluation</td><td>Low-ball valuations of property, collectibles or a business</td><td>Independent, jointly-instructed valuations</td></tr>
</tbody></table></figure>
<p>Digital assets deserve particular attention; our guide to
<a href="/business-in-divorce/">businesses in divorce</a> covers valuation issues in more depth, and
<a href="/superannuation-and-divorce/">superannuation and divorce</a> explains how super is split.</p>
"""
    + inline_cta("Worried a business or trust is being used to shield value? Our mediators work with independent valuers to get the real numbers on the table.")
    + """
<h2 id="warning-signs">Warning signs to look out for</h2>
<ul>
  <li>Bank, credit card or tax documents stop arriving at the family home, or online access is changed.</li>
  <li>A business that was thriving suddenly reports losses — just as separation is discussed.</li>
  <li>Large, unexplained withdrawals or transfers, particularly to family members.</li>
  <li>New "loans" from relatives that never existed before.</li>
  <li>Reluctance to provide documents, repeated delays, or partial disclosure.</li>
  <li>A lifestyle — travel, cars, renovations — that the declared income cannot support.</li>
  <li>New accounts, crypto exchange apps or entities you were unaware of.</li>
</ul>
<p>None of these proves concealment on its own. Separations disrupt finances, and businesses do have
bad years. But a cluster of signs is a reason to ask for documents — calmly, specifically and in
writing — rather than to accuse.</p>
"""
    + inline_cta("Suspicion without evidence fuels conflict. A structured disclosure process gets you the documents and lowers the temperature.")
    + f"""
<h2 id="uncovering">How hidden assets are uncovered</h2>
<p>Most assets are found through ordinary, methodical disclosure rather than dramatic investigation:</p>
<ol>
  <li><strong>A disclosure list.</strong> Ask for 12–36 months of bank, credit card, loan, super and
  tax records, plus business financial statements and trust documents.</li>
  <li><strong>Joint valuations.</strong> Agree on an independent valuer for real estate and businesses.</li>
  <li><strong>Forensic accountants.</strong> Where a business or trust is involved, a forensic accountant
  can reconcile records, identify unusual transactions and estimate true earning capacity.</li>
  <li><strong>Court tools.</strong> If proceedings are on foot, subpoenas can compel banks, employers,
  accountants and third parties to produce documents. The {cite('fcfcoa')} can also order disclosure
  and the answering of specific questions.</li>
</ol>
<p>Your own records are often the best starting point. A <a href="/separation-guide/">separation
guide</a> checklist of account numbers, policy details and statements, gathered early, makes gaps far
easier to spot.</p>
"""
    + inline_cta("Start with the documents, not the dispute. We can help you build a clear disclosure list for both parties.")
    + f"""
<h2 id="consequences">Consequences of hiding assets</h2>
<p>Concealment rarely pays. Family courts have a range of powers when a party fails to disclose:</p>
<figure class="tbl"><table><caption>What can happen when a party hides assets</caption>
<thead><tr><th>Consequence</th><th>What it means in practice</th></tr></thead>
<tbody>
<tr><td>Adverse inferences</td><td>The court may assume undisclosed assets exist and adjust the division accordingly</td></tr>
<tr><td>Notional add-back</td><td>Value dissipated or hidden may be treated as already received by that party</td></tr>
<tr><td>Costs orders</td><td>The non-disclosing party can be ordered to pay the other side's legal costs</td></tr>
<tr><td>Setting aside orders</td><td>Under s79A, final orders can be set aside for fraud, duress or suppression of evidence</td></tr>
<tr><td>Contempt and penalties</td><td>Serious or deliberate breaches can lead to fines or other sanctions</td></tr>
<tr><td>Credibility damage</td><td>A party caught concealing assets loses credibility on every other issue</td></tr>
</tbody></table></figure>
<p class="source-note">Powers arise under the {cite('family_law_act')} and the court's rules; outcomes depend on the facts.</p>
<p>Crucially, even <a href="/consent-orders-explained/">consent orders</a> and
<a href="/binding-financial-agreements-guide/">binding financial agreements</a> are vulnerable if they
were made on the basis of concealed information. A settlement built on hidden assets is not final —
it is a dispute waiting to be reopened.</p>
"""
    + inline_cta("Want a settlement that stays settled? Full disclosure upfront is the surest way. Talk to us about how we structure it.")
    + f"""
<h2 id="in-mediation">Disclosure in mediation</h2>
<p>A common worry is that mediation lets a dishonest party "get away with it" because the mediator
cannot issue subpoenas. In practice, a well-run mediation builds disclosure into the process:</p>
<ul>
  <li>Both parties exchange financial documents <strong>before</strong> the first joint session.</li>
  <li>The mediator identifies gaps and can pause the process until documents are produced.</li>
  <li>Independent valuations and accountant reports can be jointly commissioned.</li>
  <li>Agreements can be made conditional on warranties that disclosure is complete.</li>
  <li>Where disclosure is refused, the mediation can end — and the court's compulsory tools remain available.</li>
</ul>
<p>Mediation is not appropriate in every case. Where there is financial or economic abuse, or a party
persistently refuses to disclose, a different process may be needed, and family violence support is
available through {cite('respect_1800')}. But for most couples, a structured mediation achieves full
disclosure faster and at a fraction of the <a href="/cost-of-divorce-in-australia/">cost of litigation</a>.</p>
"""
    + callout("Family lawyers and mediators, together",
              "Many clients have a family lawyer review disclosure and the proposed terms alongside mediation. "
              "That combination gives you independent advice and a faster, less adversarial path to agreement.")
    + inline_cta("Our accredited mediators run disclosure-first property mediations. Book a free initial consultation.")
    + """
<h2 id="protect-yourself">Protecting yourself: a practical checklist</h2>
<ol>
  <li>Make copies of financial documents you are entitled to access — tax returns, statements, super and
  insurance details — before separation logistics get complicated.</li>
  <li>Note account numbers, institutions and any business or trust names.</li>
  <li>Monitor joint accounts and consider asking your bank about requiring both signatures for withdrawals.</li>
  <li>Keep a dated record of unusual transactions or statements made about money.</li>
  <li>Put requests for documents in writing, with a reasonable timeframe.</li>
  <li>Get independent legal advice before signing any agreement.</li>
  <li>Be mindful of the time limits: generally 12 months after a divorce becomes final, or 2 years after a
  de facto separation, to apply for property orders.</li>
</ol>
<p>And disclose fully yourself. The fastest way to obtain transparency is to model it.</p>
"""
    + inline_cta("Prepared, documented and ready to resolve? Mediation can turn a stack of statements into an agreement.")
    + """
<h2 id="when-court">When court is the right step</h2>
<p>Court has its place. If assets are being actively dissipated, an urgent injunction may be needed
to freeze them. If a party refuses to engage with disclosure at all, the court's subpoena and
disclosure powers may be the only way forward. And where safety or financial abuse is a concern, a
protected process is essential. In those situations, speak with a family lawyer promptly.</p>
<p>For most separating couples, though, the smarter first step is a disclosure-led mediation: both
parties put everything on the table, independent experts value what needs valuing, and the agreement
is formalised as consent orders. It is quicker, cheaper and — because it is built on facts — far more
likely to last. Read our guide to <a href="/property-settlement-after-separation/">property settlement
after separation</a> to see the full process.</p>
"""
    + inline_cta("Ready to resolve your property settlement on a foundation of facts? Book a free consultation with our mediators."),
    [
        ("Is hiding assets in a divorce illegal in Australia?",
         "Hiding assets breaches the duty of full and frank disclosure, which is now set out in the Family Law Act. "
         "It can result in adverse inferences, costs orders, orders being set aside and, in serious cases, "
         "contempt findings. Deliberately providing false information in sworn documents can also have criminal consequences."),
        ("What happens if my ex lied on their financial statement?",
         "If proceedings are underway, raise it with your lawyer — the court can order further disclosure, issue "
         "subpoenas and draw adverse inferences. If orders are already made, you may be able to apply under "
         "section 79A to have them set aside for fraud or suppression of evidence."),
        ("Can mediation work if I think my ex is hiding money?",
         "Often, yes. Disclosure-first mediation requires both parties to exchange documents before negotiating, "
         "and the mediator can pause the process until gaps are filled. If disclosure is refused, the mediation can "
         "end and the court's compulsory disclosure tools remain available."),
        ("How far back does financial disclosure go?",
         "There is no fixed period, but parties commonly exchange 12 months to 3 years of records, and longer where "
         "relevant — for example, to trace a significant transfer or understand a business's trading history."),
        ("Can a settlement be reopened if hidden assets are found later?",
         "Yes. Under section 79A of the Family Law Act, a court can set aside property orders where there has been a "
         "miscarriage of justice because of fraud, duress, suppression of evidence or similar. Binding financial "
         "agreements can also be set aside for non-disclosure of material matters."),
    ],
    related=[
        ("property-settlement-after-separation",  "Property Settlement After Separation"),
        ("what-is-in-the-property-pool",          "What Is in the Property Pool?"),
        ("property-settlement-mediation-guide",   "Property Settlement Mediation"),
        ("business-in-divorce",                   "Businesses in Divorce"),
        ("consent-orders-explained",              "Consent Orders Explained"),
        ("superannuation-and-divorce",            "Superannuation and Divorce"),
    ],
    read_min=10,
)


print("gen_blog_batch23.py: 2 new cornerstones built (what-age-can-a-child-choose-which-parent-to-live-with, hiding-assets-in-divorce)")
