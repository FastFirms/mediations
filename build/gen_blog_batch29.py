"""gen_blog_batch29.py — SEO recovery stage 3: restored answer pages (brief §3).

consent-orders-example                — how consent orders are set out, fictional illustrative examples
court-ordered-drug-and-alcohol-testing — where testing fits in federal parenting proceedings
my-ex-wont-sign-divorce-papers         — sole applications and service when a spouse won't cooperate
                                         (supersedes the batch12/batch16 versions of this slug)

DRAFT — legal/editorial review by an Australian family lawyer required before publication.
Every factual claim is drawn from the FCFCOA page cited next to it (checked 8 Nov 2026).
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, key_takeaway
from authority_sources import cite


def cta(text, btn="Ask about mediation"):
    """Brief §3 CTA: links to /contact-us/, promises no legal advice or filing."""
    return f"""<div class="post-cta reveal">
  <div class="post-cta-inner">
    <p>{text}</p>
    <a href="/contact-us/" class="btn btn-primary">{btn} <span class="arr">→</span></a>
  </div>
</div>"""


STD_CTA = ("Want help discussing parenting or property arrangements? Ask Mediations Australia whether "
           "mediation is suitable for your situation.")

REVIEW_NOTE = ("<p class=\"small\" style=\"color:var(--muted)\">This guide is general information about "
               "federal family law in Australia, not legal advice. Mediations Australia does not prepare or "
               "file court documents. Get independent legal advice about your own circumstances.</p>")

RESPECT = '<a href="https://www.1800respect.org.au/" target="_blank" rel="noopener">1800RESPECT</a>'


# ─────────────────────────────────────────────────────────────────────────────
# 1. Consent orders example
# ─────────────────────────────────────────────────────────────────────────────
post(
    "consent-orders-example",
    "Consent Orders Example: Australian Property & Parenting",
    "Understand how Australian consent orders are set out, compare illustrative property and parenting examples, and see when independent legal advice is needed.",
    "Consent orders",
    "Consent orders examples <em>in Australia</em>",
    ("Consent orders are court orders made after parties agree on proposed arrangements and the Court approves them. "
     "A useful example shows the structure of numbered orders and the issues to address, not wording you should copy "
     "without advice. Property orders must be just and equitable; parenting orders must be in the child's best interests."),
    [("what-examples-show", "What an example can and cannot show"),
     ("financial-example", "Financial consent orders example"),
     ("parenting-example", "Parenting consent orders example"),
     ("layout", "Annotated layout of proposed orders"),
     ("compare", "Consent orders vs parenting plans and BFAs"),
     ("from-mediation", "From a mediated agreement to an application"),
     ("time-limits", "Time limits for financial orders"),
     ("checklist", "Before you file: a short checklist")],
    key_takeaway("A consent orders example is useful for understanding the layout: numbered orders, what each "
                 "party will do, and by when. It cannot tell you which orders suit your family. Property orders must "
                 "be just and equitable, parenting orders must be in the child's best interests, and the Court decides "
                 "whether to make them.")
    + f"""
<h2 id="what-examples-show">What a consent order example can and cannot show</h2>
<p>People search for examples because a blank page is daunting. An example can show you <strong>how</strong> proposed orders are usually organised: who does what, by when, and what happens if a step is not completed. It cannot show you <strong>what</strong> should be in your orders, because that depends on your assets, debts, superannuation, children and circumstances.</p>
<p>The Court applies different legal tests to the two kinds of orders. According to the {cite('fcfcoa_apply_consent')} guidance, parenting orders must be in the best interests of the child, and financial or property orders must be just and equitable. Agreement between you is the starting point, not the finish line: the Court still has to be satisfied the orders meet those requirements.</p>
<p>The examples below are <strong>fictional and explanatory only</strong>. They use labelled placeholders, recommend no particular split and are not wording to file. For the Court's own forms and formatting, use the materials linked from the Court's consent orders page.</p>
"""
    + cta(STD_CTA)
    + f"""
<h2 id="financial-example">Financial consent orders example (fictional, explanatory only)</h2>
<p>Imagine a couple, Party A and Party B, who have agreed in principle on how to divide their property after separation. Their proposed orders would typically need to deal with each of the following.</p>
<h3>Identifying property and debts</h3>
<p>Each asset and liability needs to be identified clearly enough that there is no doubt about what the order refers to: the property address and title details, the account or policy, the vehicle, the business interest. Vague descriptions such as "the furniture" invite later disputes.</p>
<table>
<thead><tr><th>Item (placeholder)</th><th>What the order needs to make clear</th></tr></thead>
<tbody>
<tr><td>[Former home at ADDRESS]</td><td>Whether it is retained, transferred or sold; who pays the mortgage until then</td></tr>
<tr><td>[Joint bank account]</td><td>How the balance is divided and by what date the account is closed</td></tr>
<tr><td>[Vehicle, registration X]</td><td>Who keeps it and who transfers the registration</td></tr>
<tr><td>[Credit card / personal loan]</td><td>Who becomes solely responsible for repayment</td></tr>
<tr><td>[Superannuation interest]</td><td>Whether it is split, and the trustee requirements (see below)</td></tr>
</tbody>
</table>
<h3>Proposed transfer or sale steps and timing</h3>
<p>Orders usually set out a sequence: who signs which documents, the date by which a transfer or refinance must happen, and what occurs if it does not (for example, the property is listed for sale). Clear timing avoids the most common post-settlement argument: "you were supposed to do that months ago."</p>
<h3>Superannuation and trustee requirements</h3>
<p>Superannuation splitting orders have their own procedure. The Court's {cite('fcfcoa_apply_consent')} page explains that written notice must be served on the superannuation trustee at least 28 days before filing, and the trustee may object within 28 days of receiving it. This is one reason super cannot be treated as an afterthought in a settlement.</p>
<h3>Questions to ask your lawyer</h3>
<ul>
<li>Is the overall division likely to be considered just and equitable on our facts?</li>
<li>Have we identified every asset, debt and superannuation interest?</li>
<li>Are there tax, stamp duty or lender consequences to the transfers?</li>
<li>What happens if one of us does not complete a step on time?</li>
</ul>
"""
    + cta("Close to agreement on property but stuck on a few items? Mediation can help you work through the details before you see a lawyer about the orders.")
    + f"""
<h2 id="parenting-example">Parenting consent orders example</h2>
<p>Parenting orders deal with arrangements for children rather than money. There is no automatic starting point of equal time: the question is what arrangement is in the best interests of the particular child.</p>
<h3>Living and time arrangements</h3>
<p>An example structure might cover where the children live, when they spend time with each parent during the school term, how school holidays and special days such as birthdays are shared, and where and how changeovers happen. Specific days and times reduce ambiguity.</p>
<h3>Major decisions and practical communication</h3>
<p>Orders may address how decisions about major long-term issues, such as education and health, are made, and how parents communicate about day-to-day matters (for example, through a shared app or email rather than through the children).</p>
<h3>Safety and individual circumstances</h3>
<p>Where there are concerns about family violence or child safety, standard templates are not a substitute for legal advice. The Court requires additional information in parenting applications, and some arrangements that look reasonable on paper will not be appropriate. See our guide to <a href="/domestic-violence-and-family-law/">domestic violence and family law</a>.</p>

<h2 id="layout">Annotated layout of proposed orders</h2>
<p>Most proposed orders follow a recognisable shape:</p>
<ol>
<li><strong>Heading</strong> identifying the parties and the Court.</li>
<li><strong>Numbered paragraphs</strong>, each dealing with one obligation, so it is clear what has and has not been done.</li>
<li><strong>Parenting orders</strong> and <strong>financial orders</strong> grouped separately where both are sought.</li>
<li><strong>Signatures</strong> of each party.</li>
</ol>
<p>The proposed orders are filed together with an Application for Consent Orders. The Court's {cite('fcfcoa_apply_consent')} page sets out the current documents required, and parenting and superannuation applications carry additional requirements. Check the Court's current checklist rather than relying on any example, including this one.</p>
"""
    + cta(STD_CTA)
    + f"""
<h2 id="compare">Consent orders vs parenting plans and financial agreements</h2>
<table>
<thead><tr><th></th><th>Consent orders</th><th>Parenting plan</th><th>Binding financial agreement</th></tr></thead>
<tbody>
<tr><td>Made by</td><td>The Court, on agreed terms</td><td>The parents</td><td>The parties, with independent legal advice</td></tr>
<tr><td>Covers</td><td>Parenting and/or property</td><td>Parenting only</td><td>Property and financial matters</td></tr>
<tr><td>Court approval</td><td>Yes</td><td>No</td><td>No</td></tr>
<tr><td>Enforceable as a court order</td><td>Yes</td><td>No</td><td>Binding under the Family Law Act if its requirements are met</td></tr>
</tbody>
</table>
<p>For more detail see <a href="/consent-orders-explained/">consent orders explained</a>, our <a href="/parenting-plans-guide/">parenting plans guide</a> and the <a href="/binding-financial-agreements-guide/">binding financial agreements guide</a>. Which option suits you is a legal question; a lawyer can advise on the trade-offs.</p>

<h2 id="from-mediation">From a mediated agreement to an application</h2>
<p>Mediation can help you reach an agreement, but a mediator does not make court orders. Once you have agreed in principle, each of you can get independent legal advice and, if appropriate, ask the Court to make orders in those terms. The <a href="/property-settlement-mediation-guide/">property settlement mediation guide</a> explains how that process usually runs.</p>
<h3>The Court can ask for changes or refuse</h3>
<p>Agreement between you does not guarantee that every proposed order will be made. If the Court is not satisfied the orders are just and equitable, or in the child's best interests, it can ask for more information or decline to make them. Getting advice before filing reduces the risk of delay.</p>
"""
    + cta("Want to reach agreement first, then formalise it with your lawyers? Ask whether mediation is suitable for your situation.")
    + f"""
<h2 id="time-limits">Time limits for financial orders</h2>
<p>The Court's {cite('fcfcoa_apply_consent')} page says an application for consent orders can be filed any time after separation but should be filed within 12 months of a divorce becoming final, or two years after the end of a de facto relationship. Filing outside those periods raises additional requirements under the {cite('family_law_act')}. If you are near either deadline, get legal advice promptly; an example document will not solve a time-limit problem.</p>

<h2 id="checklist">Before you file: a short checklist</h2>
<ul>
<li>Every asset, debt and superannuation interest is identified.</li>
<li>Each order says who does what, and by when.</li>
<li>Parenting and property orders are clearly separated.</li>
<li>Superannuation trustee notice requirements have been met.</li>
<li>Each of you has had independent legal advice on the substance.</li>
<li>You have checked the Court's current checklist and forms.</li>
</ul>
{REVIEW_NOTE}
""",
    [("Can I copy an example consent order?",
      "An example can help you understand the layout, but it cannot tell you what orders are appropriate for your family. Use the Court's own materials for formatting and ask a lawyer to review the substance before filing."),
     ("Are property and parenting consent orders the same?",
      "No. Parenting orders must be in the child's best interests, while financial or property orders must be just and equitable. Both can be sought in one application, but each needs appropriate supporting information."),
     ("What documents accompany proposed consent orders?",
      "The Court requires an Application for Consent Orders and the signed proposed orders, with other documents depending on the orders sought. Parenting and superannuation applications have additional requirements, so check the Court's current checklist."),
     ("Can mediation produce consent orders?",
      "Mediation can help people reach an agreement, but the mediator does not make court orders. Parties can get independent legal advice and ask the Court to make orders in agreed terms. The Court still decides whether to make them."),
     ("Are there time limits for financial consent orders?",
      "The Court says financial consent-order applications should generally be filed within 12 months after a divorce becomes final, or two years after a de facto relationship ends. Applying later raises additional requirements, so get legal advice promptly.")],
    [("consent-orders-explained", "Consent orders explained"),
     ("parenting-plans-guide", "Parenting plans guide"),
     ("property-settlement-mediation-guide", "Property settlement mediation"),
     ("binding-financial-agreements-guide", "Binding financial agreements"),
     ("superannuation-and-divorce", "Superannuation and divorce"),
     ("bfa-or-consent-orders", "BFA or consent orders?")],
    read_min=8,
)


# ─────────────────────────────────────────────────────────────────────────────
# 2. Court-ordered drug and alcohol testing
# ─────────────────────────────────────────────────────────────────────────────
post(
    "court-ordered-drug-and-alcohol-testing",
    "Drug and Alcohol Testing in Australian Parenting Cases",
    "Learn where drug and alcohol testing fits in parenting proceedings, who can request it, who may pay, and why medical and legal advice matter.",
    "Parenting",
    "Court-ordered drug and alcohol testing <em>in parenting cases</em>",
    ("Drug and alcohol testing can form part of the evidence used to assess risk in parenting proceedings. "
     "The Court identifies urine, blood and hair-follicle tests among the investigations that may assist it. "
     "A mediator is not a court or a testing authority, so get legal advice about orders and clinical advice about what a test can show."),
    [("why", "Why testing may arise in a parenting case"),
     ("who-decides", "Court orders, voluntary testing and a mediator's role"),
     ("types", "Types of testing mentioned by the Court"),
     ("arrangements", "What a testing arrangement needs to clarify"),
     ("cost", "What does testing cost?"),
     ("results", "Positive results, refusal and disputed evidence"),
     ("child-protection", "Child protection testing vs family court proceedings"),
     ("mediation-safety", "When mediation is unsafe or inappropriate")],
    key_takeaway("In federal parenting proceedings, drug and alcohol testing is one kind of evidence the Court may use "
                 "to assess risk to a child. The Court lists urine, blood and hair-follicle tests among possible investigations, "
                 "and in most cases the parties pay. A mediator cannot order a test, and no single result automatically decides "
                 "parenting arrangements.")
    + f"""
<h2 id="why">Why testing may arise in a parenting case</h2>
<p>Parenting cases turn on the best interests of the child, and child safety sits at the centre of that question. Where one parent raises concerns about the other's drug or alcohol use, the Court may need evidence to assess whether there is a risk to the child, and how serious it is. The Court's guidance on {cite('fcfcoa_safety_risk')} describes the kinds of investigations that may assist it.</p>
<h3>Allegations, evidence and safety are different things</h3>
<p>An allegation is a claim. Evidence is material the Court can weigh. Safety is the outcome everyone should be focused on. Testing can help close the gap between a claim and evidence, but it is only one part of the picture, alongside reports, records and other material relevant to the particular family.</p>

<h2 id="who-decides">Court orders, voluntary testing and a mediator's role</h2>
<h3>A mediator has no power to compel testing</h3>
<p>A mediator, including a family dispute resolution practitioner, helps people explore possible agreements. A mediator does not make binding orders and cannot require anyone to undergo a test. Parents sometimes agree to voluntary testing as part of reaching an arrangement, but whether that is appropriate, and how it should be structured, is a matter for legal and clinical advice.</p>
<h3>If there is already an order</h3>
<p>If a court order already requires testing, the terms of that order govern what has to happen. Ask a lawyer what the order requires and what the consequences of non-compliance may be. Do not rely on a general guide, including this one, to interpret a specific order.</p>
"""
    + cta(STD_CTA)
    + f"""
<h2 id="types">Types of testing mentioned by the Court</h2>
<p>The Court's {cite('fcfcoa_safety_risk')} page lists drug and/or alcohol tests, including urine tests, blood tests and/or hair follicle tests, among the investigations that may assist it.</p>
<table>
<thead><tr><th>Test type named by the Court</th><th>What to ask a clinician or provider</th></tr></thead>
<tbody>
<tr><td>Urine</td><td>What substances are tested for, and how samples are collected and verified</td></tr>
<tr><td>Blood</td><td>What the test is designed to measure, and its limitations</td></tr>
<tr><td>Hair follicle</td><td>What period the result relates to, and how it should be interpreted</td></tr>
</tbody>
</table>
<p>That list does not mean every test suits every concern or every person.</p>
<h3>What about "CDT" tests?</h3>
<p>Many people search for "CDT test" in this context. What any particular blood marker can and cannot indicate is a clinical question. Ask a qualified clinician or testing provider to explain the purpose and limits of a test before relying on it, and ask a lawyer how it may be treated as evidence.</p>

<h2 id="arrangements">What a testing arrangement needs to clarify</h2>
<p>Whether testing is ordered or agreed, vague arrangements cause disputes. Points that usually need to be clear include:</p>
<ul>
<li><strong>Provider:</strong> who conducts the testing.</li>
<li><strong>Identity and chain of custody:</strong> how the person tested is identified and how samples are handled.</li>
<li><strong>Timing and frequency:</strong> when tests occur and over what period.</li>
<li><strong>Costs:</strong> who pays, and how.</li>
<li><strong>Reporting:</strong> who receives results and in what form.</li>
<li><strong>Privacy:</strong> how sensitive health information is stored and shared.</li>
</ul>
<p>There is no standard wording that suits every case. A lawyer can advise on how these points should be addressed in an order or agreement under the {cite('family_law_act')}.</p>
"""
    + cta("Need a calm, structured conversation about parenting arrangements where there are concerns? Ask whether mediation is suitable, or whether another pathway is safer.")
    + f"""
<h2 id="cost">What does testing cost?</h2>
<p>There is no single national price. The Court says that in most cases the costs of expert services and investigations, other than those provided by the Court's own Children's Services, are paid by the parties ({cite('fcfcoa_safety_risk')}). The actual fee depends on the provider and the testing regime. Before agreeing, ask for:</p>
<ul>
<li>a written quote per test and for any reporting;</li>
<li>whether collection, analysis and reports are charged separately;</li>
<li>how costs will be shared between the parties.</li>
</ul>
<p>Mediation fees do not include external testing or expert reports.</p>

<h2 id="results">Positive results, refusal and disputed evidence</h2>
<p>A test result is not an automatic parenting outcome. The Court considers child safety and risk using all the evidence appropriate to the case. If you receive a result you dispute, if the other parent refuses testing, or if you are unsure what a result means, get legal advice about the evidence and clinical advice about interpretation, rather than drawing conclusions from one result.</p>

<h2 id="child-protection">Child protection agency testing vs family court proceedings</h2>
<p>This guide addresses testing in federal family law parenting proceedings. A state or territory child protection agency operates under a different legal framework, and its requirements differ between jurisdictions. There is no single nationwide child protection drug testing policy. If an agency is involved, ask that agency and a qualified lawyer about its requirements.</p>
"""
    + cta(STD_CTA)
    + f"""
<h2 id="mediation-safety">When mediation is unsafe or inappropriate</h2>
<p>Where there are serious safety concerns, including family violence or risk to a child, mediation may not be appropriate and exemptions from family dispute resolution can apply. See <a href="/is-family-law-mediation-compulsory/">is family law mediation compulsory?</a> and our guide to <a href="/domestic-violence-and-family-law/">domestic violence and family law</a>. If anyone is in immediate danger, call <strong>000</strong>. For confidential support, contact {RESPECT} on 1800 737 732.</p>
{REVIEW_NOTE}
""",
    [("Can a mediator order a drug test?",
      "No. A mediator helps participants explore possible agreements and does not make binding court orders. If testing is proposed, get legal advice about whether an order or voluntary arrangement is appropriate, and medical advice about the testing itself."),
     ("What kinds of tests can be relevant?",
      "The Court lists urine, blood and hair-follicle tests among investigations that may assist its assessment of risk. That does not mean every test suits every concern. A clinician can explain a test's purpose and limitations; a lawyer can explain its role in proceedings."),
     ("Who pays for drug or alcohol testing?",
      "The Court says that, in most cases, the parties pay for expert services and investigations other than those provided by Court Children's Services. Ask the provider for written costs and get legal advice about how they should be shared."),
     ("Does a positive result automatically decide parenting arrangements?",
      "No. The Court considers child safety and risk using the evidence appropriate to the case, which may include reports, records and testing. Get legal advice about the evidence and clinical advice about interpretation."),
     ("Is child-protection drug testing the same as family court testing?",
      "No. A state or territory child protection agency operates under a different legal framework from federal family law proceedings. Ask that agency and a qualified lawyer about its requirements rather than assuming one national policy applies.")],
    [("domestic-violence-and-family-law", "Domestic violence and family law"),
     ("is-family-law-mediation-compulsory", "Is family law mediation compulsory?"),
     ("child-custody-mediation", "Child custody mediation"),
     ("family-court-process", "The family court process"),
     ("how-to-change-parenting-orders", "How to change parenting orders"),
     ("ex-not-following-parenting-orders", "Ex not following parenting orders")],
    read_min=8,
)


# ─────────────────────────────────────────────────────────────────────────────
# 3. My ex won't sign divorce papers
# ─────────────────────────────────────────────────────────────────────────────
post(
    "my-ex-wont-sign-divorce-papers",
    "Ex Won't Sign Divorce Papers? Australian Service Guide",
    "A spouse refusing to sign is not the same as stopping a divorce. Understand sole applications, service requirements and when to seek legal advice.",
    "Divorce",
    "My ex won't sign divorce papers <em>in Australia</em>",
    ("A spouse's refusal to sign does not necessarily prevent a sole divorce application. The key issue is usually "
     "properly serving the documents and proving service to the Court. Posting the papers is not the only method: "
     "the Court explains service by hand and, where appropriate, applications for substituted service."),
    [("joint-vs-sole", "Refusing a joint application vs refusing service"),
     ("service", "Sole application: what service means"),
     ("postal", "If the postal acknowledgement is not returned"),
     ("refuses", "If your spouse refuses the documents"),
     ("cannot-find", "If you cannot locate or serve your spouse"),
     ("separate", "Divorce is separate from property and parenting"),
     ("special", "Safety, overseas and special-service situations"),
     ("checklist", "Checklist")],
    key_takeaway("In Australia your ex cannot stop a divorce simply by refusing to sign. You can apply on your own "
                 "(a sole application), but you must then serve the documents properly: at least 28 days before the "
                 "hearing if your spouse is in Australia, or 42 days if overseas. You cannot serve them yourself.")
    + f"""
<h2 id="joint-vs-sole">Refusing a joint application vs refusing to acknowledge service</h2>
<p>"Won't sign" can mean two different things. Your spouse may refuse to make a <strong>joint application</strong> with you, or, after you apply alone, they may refuse to sign the <strong>acknowledgement of service</strong>. Neither, on its own, stops you from seeking a divorce.</p>
<p>The Court's guidance on {cite('fcfcoa_serve_divorce')} distinguishes the two processes: a joint application does not require service on the other spouse, while a sole application does. If cooperation is not possible, the usual path is a sole application. Refusing to cooperate does not remove your obligation to meet the Court's requirements for your own application.</p>

<h2 id="service">Sole application: what service means</h2>
<p>Service is the formal process of giving your spouse the divorce documents in a way the Court accepts, and then proving it. The Court needs to be satisfied your spouse has been properly notified before it can grant the divorce.</p>
<h3>Deadlines for service</h3>
<table>
<thead><tr><th>Where your spouse is</th><th>Serve at least</th></tr></thead>
<tbody>
<tr><td>In Australia</td><td>28 days before the hearing</td></tr>
<tr><td>Overseas</td><td>42 days before the hearing</td></tr>
</tbody>
</table>
<p>Source: {cite('fcfcoa_serve_divorce')}. Overseas service can involve additional requirements depending on the country.</p>
<h3>Methods of service</h3>
<p>The Court describes service by post (where your spouse will sign and return an acknowledgement), by hand, and through your spouse's lawyer if the lawyer confirms in writing that they will accept service.</p>
"""
    + cta("Divorce is only one part of separating. Want help discussing parenting or property arrangements? Ask Mediations Australia whether mediation is suitable for your situation.")
    + f"""
<h2 id="postal">If the postal acknowledgement is not returned</h2>
<p>Postal service relies on your spouse signing and returning the acknowledgement. If you expect them to refuse, postal service is unlikely to work; the Court's guidance is to use it only where you are confident the form will come back. If it is not returned, you will need to arrange service by hand, keeping the 28-day or 42-day deadline in mind.</p>
<h3>Service by hand</h3>
<p>Service by hand must be done by a person over 18, such as a friend, family member or professional process server.</p>
<h3>You cannot serve the papers yourself</h3>
<p>The Court is explicit: <strong>you cannot serve the documents on your spouse yourself</strong> ({cite('fcfcoa_serve_divorce')}). The person who serves them follows the Court's identification and evidence requirements and completes the relevant affidavit.</p>

<h2 id="refuses">If your spouse refuses the documents</h2>
<p>A spouse who will not take the papers, or will not confirm who they are, creates a practical problem rather than a legal block. The server records what happened and gives evidence of it to the Court. Follow the Court's current instructions closely and keep careful notes; a professional process server deals with this situation regularly.</p>

<h2 id="cannot-find">If you cannot locate or serve your spouse</h2>
<p>If you have taken all reasonable steps and still cannot serve your spouse, the Court explains two possible applications:</p>
<table>
<thead><tr><th>Option</th><th>What it means</th></tr></thead>
<tbody>
<tr><td>Substituted service</td><td>The Court allows service another way, for example by text message, email or through a third person it is satisfied will bring the documents to your spouse's attention</td></tr>
<tr><td>Dispensation of service</td><td>The Court dispenses with service altogether. The Court describes this as a very serious step, granted only in exceptional circumstances on substantial evidence</td></tr>
</tbody>
</table>
<p>Neither is automatic; both need an application and supporting evidence, and the Court recommends legal advice before applying ({cite('fcfcoa_serve_divorce')}). Do not assume an email or social media message counts as service without the Court's permission.</p>
"""
    + cta(STD_CTA)
    + f"""
<h2 id="separate">Divorce is separate from property and parenting</h2>
<p>A divorce order formally ends the marriage. It does not divide property or set parenting arrangements; those are dealt with separately, by agreement or by court order. Our <a href="/how-to-get-a-divorce-in-australia-a-step-by-step-guide/">step-by-step divorce guide</a> covers the application itself, and the <a href="/property-settlement-mediation-guide/">property settlement mediation guide</a> explains how property is commonly resolved. Time limits apply to financial applications after a divorce becomes final, so do not leave property unresolved indefinitely.</p>
<p>Mediation cannot grant a divorce. It can help separated couples reach agreement on children and property, which is often where the real conflict lies, even when the divorce paperwork has stalled.</p>

<h2 id="special">Safety, overseas and special-service situations</h2>
<p>The Court has special requirements where your spouse is overseas, in prison or has a legal incapacity. If contacting your spouse raises safety concerns, get legal advice before arranging service and make sure your own contact details are protected. In an emergency call <strong>000</strong>; for confidential support contact {RESPECT} on 1800 737 732.</p>

<h2 id="checklist">Checklist</h2>
<ul>
<li>Decide whether a sole application is needed.</li>
<li>Note the hearing date and your 28-day or 42-day service deadline.</li>
<li>Choose a method: post only if your spouse will sign; otherwise by hand through someone over 18.</li>
<li>Do not serve the documents yourself.</li>
<li>Make sure the server completes the required affidavit.</li>
<li>If you cannot serve, get legal advice about substituted service or dispensation.</li>
<li>Check the Court's current service kit and the requirements of the {cite('family_law_act')}.</li>
</ul>
{REVIEW_NOTE}
""",
    [("Do I need my spouse to agree to a joint application?",
      "No. If you cannot make a joint application, you can make a sole application instead. Joint applications do not require service on the other spouse, while sole applications do."),
     ("What if my spouse will not return the postal acknowledgement?",
      "The Court says postal service should only be used where you are confident your spouse will sign and return the acknowledgement. If it is not returned, you need to arrange service by hand before the deadline."),
     ("Can I serve the papers myself?",
      "No. The Court says you cannot serve divorce documents on your spouse yourself. Service by hand must be done by someone over 18, such as a friend, family member or professional process server, who then completes an affidavit."),
     ("How long before the hearing must service happen?",
      "At least 28 days before the hearing if your spouse is in Australia, or at least 42 days if they are overseas. Overseas service can involve additional requirements."),
     ("What if I cannot find my spouse?",
      "After reasonable attempts, you may be able to apply for substituted service or, in exceptional circumstances, dispensation of service. Both need an application and evidence, and the Court recommends legal advice.")],
    [("how-to-get-a-divorce-in-australia-a-step-by-step-guide", "How to get a divorce in Australia"),
     ("how-long-does-a-divorce-take", "How long does a divorce take?"),
     ("divorce-without-a-lawyer", "Divorce without a lawyer"),
     ("property-settlement-mediation-guide", "Property settlement mediation"),
     ("separation-guide", "Separation guide"),
     ("cost-of-divorce-in-australia", "Cost of divorce in Australia")],
    read_min=8,
)
