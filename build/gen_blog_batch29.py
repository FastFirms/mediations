"""gen_blog_batch29.py — SEO recovery stage 3: restored answer pages (brief §3).

consent-orders-example                — how consent orders are set out, annotated illustrative example
court-ordered-drug-and-alcohol-testing — where testing fits in parenting proceedings, how orders are worded
my-ex-wont-sign-divorce-papers         — sole applications and service when a spouse won't cooperate
                                         (supersedes the batch12/batch16 versions of this slug)

v2 (8 Nov 2026): expanded after competitor SERP review. Competitor gaps addressed: annotated example
layout, worked scenarios, filing checklist, official order-wording examples, forms/fees/timing tables.

DRAFT — legal/editorial review by an Australian family lawyer required before publication.
Every factual claim is drawn from the official page cited next to it (checked 8 Nov 2026).
Competitor-only claims (test prices, detection windows) are deliberately NOT used.
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
               "federal family law in Australia (Western Australia has its own Family Court and forms). It is not "
               "legal advice. Mediations Australia does not prepare or file court documents. Get independent legal "
               "advice about your own circumstances.</p>")

RESPECT = '<a href="https://www.1800respect.org.au/" target="_blank" rel="noopener">1800RESPECT</a>'

NOTICE = ('<div class="answer" style="border-left-color:var(--sage-deep)"><p><strong>Illustrative only.</strong> '
          'Everything in this box is fictional and simplified to show structure. It is not court-ready wording, '
          'does not recommend any outcome and must not be filed. Use the Court\'s proposed orders template and get '
          'independent legal advice.</p></div>')


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
     "This guide walks through an annotated example layout, two worked property scenarios and a parenting example, "
     "then the documents, fee and checks involved. Use it to understand the structure, not as wording to copy."),
    [("what-examples-show", "What an example can and cannot show"),
     ("annotated", "An annotated example of proposed orders"),
     ("worked", "Two worked property scenarios"),
     ("super", "Superannuation splitting: the extra steps"),
     ("parenting-example", "Parenting consent orders example"),
     ("filing", "Filing: documents, fee and checklist"),
     ("rejected", "Why proposed orders get sent back"),
     ("cannot-cover", "What consent orders cannot do"),
     ("compare", "Consent orders vs parenting plans and BFAs"),
     ("from-mediation", "From a mediated agreement to orders")],
    key_takeaway("A consent orders example shows the layout: a heading, the words \"by consent the Court orders\", "
                 "then numbered orders saying who does what and by when, with parenting and property orders kept separate. "
                 "It cannot tell you which orders suit your family. Property orders must be just and equitable, parenting "
                 "orders must be in the child's best interests, and the Court decides whether to make them.")
    + f"""
<h2 id="what-examples-show">What a consent order example can and cannot show</h2>
<p>People search for examples because a blank template is daunting. An example can show you <strong>how</strong> proposed orders are usually organised: who does what, by when, and what happens if a step is not completed. It cannot show you <strong>what</strong> should be in your orders, because that depends on your assets, debts, superannuation, children and circumstances.</p>
<p>The Court applies different legal tests to the two kinds of orders. According to the Court's guidance on how to {cite('fcfcoa_apply_consent')}, parenting orders must be in the best interests of the child, and financial or property orders must be just and equitable. Agreement between you is the starting point, not the finish line: the Court still has to be satisfied the orders meet those requirements under the {cite('family_law_act')}.</p>
<p>An application has two parts. The first is the Application for Consent Orders, which gives the Court the information it needs to decide whether to make the orders. The second is the proposed orders themselves: the actual wording you want the Court to make.</p>
"""
    + cta(STD_CTA)
    + f"""
<h2 id="annotated">An annotated example of proposed orders</h2>
<p>Below is a simplified, fictional layout for a couple, Party A and Party B, who want both property and parenting orders. The notes on the right explain what each part is doing.</p>
{NOTICE}
<div style="overflow-x:auto">
<table>
<thead><tr><th>Example text (fictional)</th><th>What this part does</th></tr></thead>
<tbody>
<tr><td><em>Proposed orders. [Party A] and [Party B]. File number [to be allocated].</em></td><td>Identifies the parties and the proceeding. The Court's template sets the exact heading.</td></tr>
<tr><td><em>By consent, the Court orders that:</em></td><td>Signals the orders are agreed, not decided after a contested hearing.</td></tr>
<tr><td colspan="2"><strong>Parenting orders</strong></td></tr>
<tr><td><em>1. The child [Name, born DD/MM/YYYY] live with [Party A].</em></td><td>Where the child lives. Each order deals with one obligation.</td></tr>
<tr><td><em>2. The child spend time with [Party B] each alternate weekend from [time, day] to [time, day], commencing [date].</em></td><td>Specific days, times and a start date avoid later arguments about what was meant.</td></tr>
<tr><td><em>3. Changeover occur at [location].</em></td><td>Practical arrangements reduce conflict at handovers.</td></tr>
<tr><td colspan="2"><strong>Property orders</strong></td></tr>
<tr><td><em>4. Within [X] days, [Party B] transfer to [Party A] all right, title and interest in [property at ADDRESS].</em></td><td>A transfer with a deadline. The property must be identified precisely.</td></tr>
<tr><td><em>5. [Party A] refinance the mortgage over that property to release [Party B] within [X] days, failing which the property be sold.</em></td><td>A fallback if a step fails, so the orders do not stall.</td></tr>
<tr><td><em>6. [Party A] retain the funds in [account] and [Party B] retain the vehicle [registration].</em></td><td>Who keeps which asset.</td></tr>
<tr><td><em>7. [Party B] be solely responsible for the debt owed to [lender] and indemnify [Party A] against it.</em></td><td>Allocates debts, not just assets.</td></tr>
<tr><td><em>8. Each party and the Trustee have liberty to apply in relation to the implementation of the orders affecting the superannuation interest.</em></td><td>Required wording where super is split (see below).</td></tr>
<tr><td><em>9. Except as provided in these orders, each party retain the property in their possession.</em></td><td>A catch-all so nothing is left unaddressed.</td></tr>
<tr><td><em>Signed: [Party A], [Party B]. Date: [DD/MM/YYYY].</em></td><td>Both parties sign the proposed orders.</td></tr>
</tbody>
</table>
</div>
<p>The Court publishes a proposed orders template, and the parenting fact sheet referred to on its consent orders page helps with parenting wording. Real orders are usually longer and more precise than this example, particularly where there is a business, a trust or a superannuation split.</p>
"""
    + cta("Close to agreement but stuck on a few items? Mediation can help you work through the details before your lawyers draft the orders.")
    + f"""
<h2 id="worked">Two worked property scenarios</h2>
<p>These fictional scenarios show how the same structure handles different situations. The figures are invented and the outcomes are <strong>not</strong> recommendations: what is just and equitable depends on contributions, future needs and other factors a lawyer can assess.</p>
<h3>Scenario 1: one home, two super funds, one car loan</h3>
<table>
<thead><tr><th>Item (fictional)</th><th>Value</th><th>How the orders would need to deal with it</th></tr></thead>
<tbody>
<tr><td>Home, net of mortgage</td><td>$420,000</td><td>Transfer to one party with a refinance deadline, or sale and division of proceeds</td></tr>
<tr><td>Party A super</td><td>$180,000</td><td>Retain, or split by a superannuation splitting order (trustee notice required)</td></tr>
<tr><td>Party B super</td><td>$60,000</td><td>As above</td></tr>
<tr><td>Car loan</td><td>-$18,000</td><td>Allocate responsibility and an indemnity</td></tr>
<tr><td>Joint savings</td><td>$25,000</td><td>Divide and close the account by a set date</td></tr>
</tbody>
</table>
<p>Whatever split the parties agree, the orders translate it into actions: who transfers what, who refinances, whether super is split and by how much, and what happens if a step is missed.</p>
<h3>Scenario 2: renting, no real estate, a small business</h3>
<p>Party A runs a sole-trader business; there is no home, but there is a vehicle used in the business and a tax debt. Here the orders need to identify the business assets, address the tax liability, and be clear about who keeps the business and any future obligations. A lawyer and, often, an accountant should look at tax consequences before orders are finalised.</p>

<h2 id="super">Superannuation splitting: the extra steps</h2>
<p>Super is the part of a property settlement most often underestimated. The Court's {cite('fcfcoa_apply_consent')} page sets out specific requirements:</p>
<ul>
<li>At least <strong>28 days before filing</strong>, written notice of the proposed orders must be served on the trustee of the fund, stating that the trustee may object within 28 days.</li>
<li>If the trustee does not object within 28 days of receiving the notice, the application can be filed, with proof of the trustee's response and proof of the current value of the interest.</li>
<li>The proposed orders must include a provision that each party and the trustee have liberty to apply about implementing the orders affecting the super interest.</li>
<li>Without this proof, the Court cannot make the orders sought.</li>
</ul>
<p>Legal and, where needed, accounting advice is recommended, including on tax consequences.</p>
"""
    + cta(STD_CTA)
    + f"""
<h2 id="parenting-example">Parenting consent orders example</h2>
<p>Parenting orders deal with arrangements for children rather than money. There is no automatic starting point of equal time: the question is what arrangement is in the best interests of the particular child. Parenting orders commonly cover:</p>
<table>
<thead><tr><th>Topic</th><th>Example of what the order addresses (fictional)</th></tr></thead>
<tbody>
<tr><td>Living arrangements</td><td>The children live with [Party A]</td></tr>
<tr><td>School-term time</td><td>Alternate weekends and one weeknight with [Party B]</td></tr>
<tr><td>School holidays</td><td>Half of each school holiday period, alternating the first half each year</td></tr>
<tr><td>Special days</td><td>Christmas, Mother's and Father's Day, birthdays</td></tr>
<tr><td>Communication</td><td>Phone or video calls with the other parent at set times</td></tr>
<tr><td>Decisions</td><td>How major long-term decisions, such as schooling and health, are made</td></tr>
<tr><td>Changeovers</td><td>Where and how handovers happen</td></tr>
</tbody>
</table>
<p>Where there are concerns about family violence or child safety, templates are not a substitute for legal advice. Parenting consent applications must include a Notice of child abuse, family violence or risk. See our guide to <a href="/domestic-violence-and-family-law/">domestic violence and family law</a> and the <a href="/parenting-plans-guide/">parenting plans guide</a>.</p>

<h2 id="filing">Filing: documents, fee and checklist</h2>
<p>For the federal Court, consent applications are filed through the Commonwealth Courts Portal. The Court's page lists the documents to upload:</p>
<table>
<thead><tr><th>Document</th><th>When it is needed</th></tr></thead>
<tbody>
<tr><td>Application for Consent Orders</td><td>Always</td></tr>
<tr><td>Proposed orders (using the Court's template), signed</td><td>Always</td></tr>
<tr><td>An identical unsigned Word (.docx) version of the proposed orders, not locked and without tracked changes</td><td>Always</td></tr>
<tr><td>Notice of child abuse, family violence or risk</td><td>If seeking parenting orders</td></tr>
<tr><td>Proof of value and proof of procedural fairness to the trustee</td><td>If seeking superannuation orders</td></tr>
<tr><td>Copy of existing orders</td><td>If varying or discharging existing orders</td></tr>
<tr><td>De facto registration certificate</td><td>If applicable</td></tr>
</tbody>
</table>
<p>Parenting and financial orders can be sought in the same application. The Court's {cite('fcfcoa_fees')} list the filing fee for an Application for Consent Orders as <strong>$215</strong> (from 1 July 2026; GST does not apply to court fees).</p>
<h3>Time limits for financial orders</h3>
<p>An application can be filed any time after separation, but financial orders should be sought within 12 months of a divorce becoming final, or two years after a de facto relationship ends. Applying later raises additional requirements, so get advice promptly if you are close to either date.</p>

<h2 id="rejected">Why proposed orders get sent back</h2>
<p>The Court can request more information or decline to make orders. Common reasons, based on the Court's requirements, include:</p>
<ul>
<li>the information does not let the Court assess whether the property orders are just and equitable;</li>
<li>parenting orders do not appear to be in the child's best interests, or risk issues are not addressed;</li>
<li>assets, debts or super are not identified precisely enough to be carried out;</li>
<li>missing superannuation trustee notice or proof of value;</li>
<li>missing documents, such as the unsigned Word version of the orders.</li>
</ul>
"""
    + cta("Want to reach agreement first, then formalise it with your lawyers? Ask whether mediation is suitable for your situation.")
    + f"""
<h2 id="cannot-cover">What consent orders cannot do</h2>
<p>Consent orders are not a catch-all. Child support for children covered by the Child Support (Assessment) Act is generally dealt with through the child support system rather than parenting orders, and orders cannot bind people who are not parties. Agreement also does not override the Court's legal tests. If something you want is unusual, ask a lawyer whether orders can achieve it.</p>

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
<p>For more detail see <a href="/consent-orders-explained/">consent orders explained</a> and the <a href="/binding-financial-agreements-guide/">binding financial agreements guide</a>.</p>

<h2 id="from-mediation">From a mediated agreement to orders</h2>
<p>Mediation can help you reach the agreement that consent orders record, but a mediator does not make court orders. A practical sequence is:</p>
<ol>
<li>Exchange financial disclosure and identify the asset pool.</li>
<li>Reach agreement in principle at mediation on property and/or parenting.</li>
<li>Each party gets independent legal advice on the agreement.</li>
<li>A lawyer drafts the proposed orders on the Court's template.</li>
<li>Serve super trustee notice if needed, then file.</li>
</ol>
<p>The <a href="/property-settlement-mediation-guide/">property settlement mediation guide</a> explains the first two steps in more detail.</p>
{REVIEW_NOTE}
""",
    [("Can I copy an example consent order?",
      "An example can help you understand the layout, but it cannot tell you what orders are appropriate for your family. Use the Court's proposed orders template and ask a lawyer to review the substance before filing."),
     ("Are property and parenting consent orders the same?",
      "No. Parenting orders must be in the child's best interests, while financial or property orders must be just and equitable. Both can be sought in one application, but each needs appropriate supporting information."),
     ("What documents are filed with proposed consent orders?",
      "The Application for Consent Orders, the signed proposed orders and an identical unsigned Word version. Parenting applications also need a Notice of child abuse, family violence or risk; super splits need proof of value and trustee notice."),
     ("How much does it cost to file consent orders?",
      "The Court's filing fee for an Application for Consent Orders is $215 from 1 July 2026. Legal fees for drafting and advice are separate."),
     ("Do I need to notify my super fund?",
      "Yes, if you are seeking a superannuation splitting order. Written notice must be served on the trustee at least 28 days before filing, and the trustee can object within 28 days."),
     ("Can mediation produce consent orders?",
      "Mediation can help people reach an agreement, but the mediator does not make court orders. Parties can get independent legal advice and ask the Court to make orders in agreed terms. The Court still decides whether to make them."),
     ("Are there time limits for financial consent orders?",
      "Financial applications should generally be filed within 12 months after a divorce becomes final, or two years after a de facto relationship ends. Applying later raises additional requirements, so get legal advice promptly.")],
    [("consent-orders-explained", "Consent orders explained"),
     ("parenting-plans-guide", "Parenting plans guide"),
     ("property-settlement-mediation-guide", "Property settlement mediation"),
     ("binding-financial-agreements-guide", "Binding financial agreements"),
     ("superannuation-and-divorce", "Superannuation and divorce"),
     ("bfa-or-consent-orders", "BFA or consent orders?")],
    read_min=11,
)


# ─────────────────────────────────────────────────────────────────────────────
# 2. Court-ordered drug and alcohol testing
# ─────────────────────────────────────────────────────────────────────────────
post(
    "court-ordered-drug-and-alcohol-testing",
    "Drug and Alcohol Testing in Australian Parenting Cases",
    "Learn where drug and alcohol testing fits in parenting proceedings, how orders are worded, who pays, and what a mediator can and cannot do.",
    "Parenting",
    "Court-ordered drug and alcohol testing <em>in parenting cases</em>",
    ("Drug and alcohol testing can form part of the evidence used to assess risk in parenting proceedings. "
     "This guide explains the tests the Court mentions, how testing orders are typically worded, who usually pays, "
     "what happens with results, and where mediation and voluntary testing fit."),
    [("why", "Why testing arises in parenting cases"),
     ("mediator", "Can a mediator order a drug test?"),
     ("types", "Types of testing the Court mentions"),
     ("cdt", "What is a CDT test?"),
     ("wording", "How testing orders are typically worded"),
     ("arrangements", "What any testing arrangement should cover"),
     ("cost", "Who pays for testing?"),
     ("results", "Results, refusal and disputed evidence"),
     ("child-protection", "Child protection testing vs family court"),
     ("mediation-safety", "When mediation is unsafe")],
    key_takeaway("In parenting proceedings, drug and alcohol testing is one kind of evidence the Court may use to assess "
                 "risk to a child; the Court names urine, blood and hair-follicle tests. Testing orders usually set the test type, "
                 "timing, photo ID, who receives results and who pays. A mediator cannot order a test, though parents can agree "
                 "to voluntary testing, and no single result automatically decides parenting arrangements.")
    + f"""
<h2 id="why">Why testing arises in parenting cases</h2>
<p>Parenting cases turn on the best interests of the child, and child safety sits at the centre of that question. Where one parent raises concerns about the other's drug or alcohol use, the Court may need evidence to assess whether there is a risk to the child, and how serious it is. The Court's guidance on {cite('fcfcoa_safety_risk')} lists the kinds of investigations that may assist it, including drug and alcohol tests.</p>
<h3>Allegations, evidence and safety are different things</h3>
<p>An allegation is a claim. Evidence is material the Court can weigh. Safety is the outcome everyone should be focused on. Testing can help close the gap between a claim and evidence, but it is one part of the picture, alongside reports, records and other material relevant to the family.</p>
<h3>How testing usually comes up</h3>
<ul>
<li><strong>By agreement:</strong> a parent offers or agrees to test to reassure the other parent, sometimes as part of a parenting plan.</li>
<li><strong>By interim order:</strong> the Court orders testing while a case is ongoing, often with conditions on time with the children.</li>
<li><strong>In final orders:</strong> testing continues for a period as a safeguard.</li>
</ul>

<h2 id="mediator">Can a mediator order a drug test?</h2>
<p><strong>No.</strong> A mediator, including a family dispute resolution practitioner, helps people explore possible agreements. A mediator does not make binding orders and cannot require anyone to be tested. What mediation <em>can</em> do is give parents a structured, safe space to discuss whether voluntary testing would help, and what it would look like: which test, how often, who pays, who sees results and what happens next.</p>
<p>Voluntary testing agreed in mediation can be recorded in a parenting plan or, with legal advice, in consent orders. A parenting plan is not enforceable like a court order, so if testing is critical to safety, ask a lawyer whether orders are more appropriate. If there is already a court order requiring testing, its terms govern; ask a lawyer what it requires.</p>
"""
    + cta("Want a structured conversation about parenting arrangements, including whether voluntary testing would help? Ask whether mediation is suitable for your situation.")
    + f"""
<h2 id="types">Types of testing the Court mentions</h2>
<p>The Court's {cite('fcfcoa_safety_risk')} page lists drug and/or alcohol tests, including urine tests, blood tests and/or hair follicle tests. Example orders published by the {cite('fcwa_parenting_examples')} show how these are used in practice.</p>
<table>
<thead><tr><th>Test</th><th>How it appears in court examples</th><th>What to ask a clinician or provider</th></tr></thead>
<tbody>
<tr><td>Urine (urinalysis)</td><td>Supervised "broadscreen" tests, either once within a set time or randomly on request</td><td>What substances are screened, how collection is supervised and verified</td></tr>
<tr><td>Hair strand</td><td>Testing for named substance groups, with an order not to cut or colour hair beforehand</td><td>What period a result relates to and how it should be interpreted</td></tr>
<tr><td>Blood (including alcohol markers)</td><td>Used where alcohol use is the concern</td><td>What the marker measures, and its limitations</td></tr>
</tbody>
</table>
<p>Detection periods and accuracy vary by test, substance, laboratory and individual. We deliberately do not quote detection windows here: ask the testing provider or a clinician, and treat figures on commercial websites with caution.</p>

<h2 id="cdt">What is a CDT test?</h2>
<p>CDT stands for <strong>carbohydrate-deficient transferrin</strong>, a blood marker used as an indicator of sustained heavy alcohol use. A peer-reviewed review describes it as widely recognised as a reliable biomarker of chronic alcohol abuse, while noting that questions about its interpretation remain ({cite('cdt_review')}). In practice that means a CDT result is evidence to be interpreted by a qualified professional, not a stand-alone answer. Ask a clinician what a particular result can and cannot show.</p>

<h2 id="wording">How testing orders are typically worded</h2>
<p>The Family Court of Western Australia publishes example parenting orders, including testing orders. Its examples show the elements courts commonly specify (paraphrased):</p>
<ul>
<li><strong>A one-off urinalysis</strong>: a supervised broadscreen urine test with photographic identification within 24 hours or by a set time, with results released to the other party, their lawyer, the Independent Children's Lawyer or the Family Consultant.</li>
<li><strong>Hair strand testing</strong>: testing for named substance groups as soon as practicable, at the cost of the party tested, with an injunction against cutting or colouring hair before the test.</li>
<li><strong>Random urinalysis</strong>: tests with photo ID within 24 hours of a written or SMS request, with the cost borne by the party tested, and an obligation to keep the other party informed of contact numbers.</li>
<li><strong>Consequences of clear results</strong>: time arrangements that change after consecutive clear results with a complete chain of custody.</li>
</ul>
<p>Source: {cite('fcwa_parenting_examples')}. These are examples from WA; the federal Court's orders vary with each case, so ask a lawyer about the right terms for yours.</p>
"""
    + cta(STD_CTA)
    + f"""
<h2 id="arrangements">What any testing arrangement should cover</h2>
<p>Whether testing is ordered or agreed, vague arrangements cause disputes. A clear arrangement covers:</p>
<table>
<thead><tr><th>Element</th><th>Question to settle</th></tr></thead>
<tbody>
<tr><td>Provider</td><td>Which independent testing provider or pathology service?</td></tr>
<tr><td>Test type</td><td>Urine, hair, blood, or a combination, and for which substances?</td></tr>
<tr><td>Identity</td><td>Photo ID and supervised collection?</td></tr>
<tr><td>Chain of custody</td><td>How is the sample tracked from collection to result?</td></tr>
<tr><td>Timing</td><td>One-off, scheduled or random? How quickly after a request?</td></tr>
<tr><td>Duration</td><td>For how long, and what ends the testing?</td></tr>
<tr><td>Results</td><td>Who receives them and in what form?</td></tr>
<tr><td>Cost</td><td>Who pays, and is it shared?</td></tr>
<tr><td>Consequences</td><td>What changes after clear, positive or missed tests?</td></tr>
<tr><td>Privacy</td><td>How is sensitive health information stored and shared?</td></tr>
</tbody>
</table>

<h2 id="cost">Who pays for testing?</h2>
<p>The federal Court says that in most cases the costs of expert services and investigations, other than those provided by the Court's own Children's Services, are paid by the parties ({cite('fcfcoa_safety_risk')}). The WA example orders commonly place the cost on the party being tested. Actual fees depend on the provider, the test and how often it is done, so get a written quote. If you are legally aided, ask Legal Aid whether testing costs can be funded in your matter. Mediation fees do not include testing or expert reports.</p>

<h2 id="results">Results, refusal and disputed evidence</h2>
<p>A test result is not an automatic parenting outcome. The Court considers child safety and risk using all the evidence appropriate to the case. Parents in this situation commonly face questions such as:</p>
<ul>
<li><strong>A positive result:</strong> what does it show, and over what period? A clinician can interpret it; a lawyer can explain how it may be used.</li>
<li><strong>A missed or refused test:</strong> how might the Court view it under the order? Ask a lawyer before deciding not to test.</li>
<li><strong>A disputed result:</strong> was the chain of custody complete? Is a confirmatory test available?</li>
</ul>
<p>Do not draw conclusions from a single result or a general guide, including this one.</p>

<h2 id="child-protection">Child protection agency testing vs family court proceedings</h2>
<p>This guide addresses testing in family law parenting proceedings. A state or territory child protection agency operates under a different legal framework, and its requirements differ between jurisdictions. There is no single nationwide child protection drug testing policy. If an agency is involved, ask that agency and a qualified lawyer about its requirements.</p>
"""
    + cta("Concerned about safety but want to avoid a long court fight? Ask whether mediation is suitable, or whether another pathway is safer.")
    + f"""
<h2 id="mediation-safety">When mediation is unsafe or inappropriate</h2>
<p>Where there are serious safety concerns, including family violence or risk to a child, mediation may not be appropriate and exemptions from family dispute resolution can apply. See <a href="/is-family-law-mediation-compulsory/">is family law mediation compulsory?</a> and our guide to <a href="/domestic-violence-and-family-law/">domestic violence and family law</a>. If anyone is in immediate danger, call <strong>000</strong>. For confidential support, contact {RESPECT} on 1800 737 732.</p>
{REVIEW_NOTE}
""",
    [("Can a mediator order a drug test?",
      "No. A mediator helps participants explore possible agreements and does not make binding orders. Parents can agree to voluntary testing in mediation; if testing is critical to safety, get legal advice about whether court orders are more appropriate."),
     ("What kinds of tests can be relevant?",
      "The Court lists urine, blood and hair-follicle tests among investigations that may assist its assessment of risk. A clinician can explain a test's purpose and limitations; a lawyer can explain its role in proceedings."),
     ("What is a CDT test?",
      "CDT (carbohydrate-deficient transferrin) is a blood marker used as an indicator of sustained heavy alcohol use. Its interpretation needs a qualified professional; it is not a stand-alone answer."),
     ("How are drug testing orders usually worded?",
      "Published example orders specify the test type, supervised collection with photo ID, timing (for example within 24 hours of a request), who receives results, who pays and, for hair tests, no cutting or colouring hair beforehand."),
     ("Who pays for drug or alcohol testing?",
      "The Court says that, in most cases, the parties pay for expert services and investigations other than those provided by Court Children's Services. Example orders often place the cost on the party tested."),
     ("Does a positive result automatically decide parenting arrangements?",
      "No. The Court considers child safety and risk using the evidence appropriate to the case. Get legal advice about the evidence and clinical advice about interpretation."),
     ("Is child-protection drug testing the same as family court testing?",
      "No. A state or territory child protection agency operates under a different legal framework from family law proceedings. Ask that agency and a qualified lawyer about its requirements.")],
    [("domestic-violence-and-family-law", "Domestic violence and family law"),
     ("is-family-law-mediation-compulsory", "Is family law mediation compulsory?"),
     ("child-custody-mediation", "Child custody mediation"),
     ("parenting-plans-guide", "Parenting plans guide"),
     ("how-to-change-parenting-orders", "How to change parenting orders"),
     ("ex-not-following-parenting-orders", "Ex not following parenting orders")],
    read_min=11,
)


# ─────────────────────────────────────────────────────────────────────────────
# 3. My ex won't sign divorce papers
# ─────────────────────────────────────────────────────────────────────────────
post(
    "my-ex-wont-sign-divorce-papers",
    "Ex Won't Sign Divorce Papers? Australian Service Guide",
    "A spouse refusing to sign is not the same as stopping a divorce. Understand sole applications, service, forms, fees and when to seek legal advice.",
    "Divorce",
    "My ex won't sign divorce papers <em>in Australia</em>",
    ("Your ex does not have to sign anything for you to get divorced. You can apply on your own, and the real task "
     "is serving the papers properly. This guide covers each scenario, from an ex who ignores the post to one you cannot "
     "find, with the forms, fees, deadlines and what your ex can and cannot do."),
    [("short-answer", "The short answer"),
     ("joint-vs-sole", "Joint vs sole applications"),
     ("scenarios", "Which situation are you in?"),
     ("service", "Serving the papers: methods and deadlines"),
     ("hand", "Service by hand, step by step"),
     ("cannot-find", "If you cannot find or serve your ex"),
     ("respond", "What your ex can and cannot do"),
     ("forms-fees", "Forms, fees and timeline"),
     ("special", "Separated under one roof, overseas and safety"),
     ("separate", "Divorce is separate from property and parenting")],
    key_takeaway("No. In Australia your ex cannot stop a divorce by refusing to sign. You can apply alone (a sole application) "
                 "and then serve the papers: at least 28 days before the hearing if your ex is in Australia, 42 days if overseas. "
                 "You cannot serve them yourself, and even if your ex signs the acknowledgment, that does not mean they agree to the divorce.")
    + f"""
<h2 id="short-answer">The short answer</h2>
<p>Australia has no-fault divorce. You do not need your spouse's signature, agreement or cooperation to apply. What you need is to meet the requirements for divorce, including 12 months' separation under the {cite('family_law_act')}, and to prove to the Court that your spouse was properly served. "Won't sign" problems are almost always service problems, and the Court has a process for each one.</p>

<h2 id="joint-vs-sole">Joint vs sole applications</h2>
<table>
<thead><tr><th></th><th>Joint application</th><th>Sole application</th></tr></thead>
<tbody>
<tr><td>Who applies</td><td>Both spouses together</td><td>One spouse alone</td></tr>
<tr><td>Ex needs to sign?</td><td>Yes</td><td>No</td></tr>
<tr><td>Service on the other spouse</td><td>Not required</td><td>Required</td></tr>
<tr><td>When it suits</td><td>You both cooperate</td><td>Your ex refuses, ignores you or cannot be found</td></tr>
</tbody>
</table>
<p>Source: {cite('fcfcoa_serve_divorce')}. If your ex will not sign a joint application, a sole application is the usual path.</p>
"""
    + cta("Divorce is only one part of separating. Want help discussing parenting or property arrangements? Ask Mediations Australia whether mediation is suitable for your situation.")
    + f"""
<h2 id="scenarios">Which situation are you in?</h2>
<table>
<thead><tr><th>Your ex...</th><th>What usually happens next</th></tr></thead>
<tbody>
<tr><td>Will sign the acknowledgment if you post it</td><td>Serve by post; they sign and return the Acknowledgment of Service</td></tr>
<tr><td>Has a lawyer</td><td>Serve the lawyer, but only if the lawyer confirms in writing they will accept service</td></tr>
<tr><td>Ignores the post or will not sign</td><td>Arrange service by hand through someone over 18</td></tr>
<tr><td>Refuses to take the papers or to confirm who they are</td><td>The server records what happened; an Affidavit proving signature may be needed</td></tr>
<tr><td>Cannot be found or keeps avoiding service</td><td>Apply for substituted service or dispensation of service</td></tr>
<tr><td>Is overseas</td><td>Serve at least 42 days before the hearing; special rules may apply</td></tr>
</tbody>
</table>

<h2 id="service">Serving the papers: methods and deadlines</h2>
<p>Service is the formal process of giving your spouse the divorce documents in a way the Court accepts, and then proving it.</p>
<table>
<thead><tr><th>Where your spouse is</th><th>Serve at least</th></tr></thead>
<tbody>
<tr><td>In Australia</td><td>28 days before the hearing</td></tr>
<tr><td>Overseas</td><td>42 days before the hearing</td></tr>
</tbody>
</table>
<p>Source: {cite('fcfcoa_serve_divorce')}. The Court's guidance is to use postal service only if you are confident your spouse will sign and return the acknowledgment. If they will not, go straight to service by hand rather than losing time.</p>

<h2 id="hand">Service by hand, step by step</h2>
<ol>
<li><strong>Choose a server.</strong> Someone over 18: a friend, family member or professional process server. <strong>You cannot serve the documents yourself.</strong></li>
<li><strong>Give them the full set of documents</strong> from the Court's divorce service kit.</li>
<li><strong>The server hands the documents to your spouse</strong> and asks them to sign the acknowledgment. Your spouse does not have to sign it.</li>
<li><strong>The server completes an Affidavit of Service by Hand</strong> describing how the documents were served.</li>
<li><strong>If the server did not know your spouse</strong>, you may also need an {cite('fcfcoa_proof_sig')} confirming the signature or identity.</li>
<li><strong>File the proof of service</strong> before the hearing.</li>
</ol>
<p>A spouse who will not take the papers creates a practical problem, not a legal block. A professional process server deals with this regularly and knows what to record.</p>
"""
    + cta(STD_CTA)
    + f"""
<h2 id="cannot-find">If you cannot find or serve your ex</h2>
<p>If you have made all reasonable attempts and still cannot serve your spouse, the Court explains two options ({cite('fcfcoa_trouble_serving')}):</p>
<table>
<thead><tr><th>Option</th><th>What it means</th></tr></thead>
<tbody>
<tr><td>Substituted service</td><td>The Court allows service another way, for example on a third person the Court is satisfied will bring the documents to your spouse's attention</td></tr>
<tr><td>Dispensation of service</td><td>The Court waives the requirement to serve, if satisfied you have made all reasonable attempts to find your spouse. It is a serious step and requires substantial evidence</td></tr>
</tbody>
</table>
<p>Both need an <strong>Application in a Proceeding</strong> and an <strong>affidavit</strong> explaining every step you took to find your spouse: enquiries made, when you last had contact, last known address, and so on. These applications are usually listed at the same time as the divorce hearing, and you should attend. The Court recommends legal advice first. Do not assume an email or social media message counts as service without the Court's permission.</p>

<h2 id="respond">What your ex can and cannot do</h2>
<p>Signing the acknowledgment does <strong>not</strong> mean your spouse agrees to the divorce ({cite('fcfcoa_served')}). If they want to oppose it, they must:</p>
<ul>
<li>file and serve a <strong>Response to Divorce</strong> within 28 days of being served in Australia, or 42 days if served overseas; and</li>
<li>attend the hearing, or the Court may treat the application as undefended.</li>
</ul>
<p>The Court notes there are <strong>limited grounds</strong> for opposing a divorce, and a respondent should get legal advice. If granted, a divorce becomes final <strong>one month and one day</strong> after the order, unless the Court orders otherwise.</p>

<h2 id="forms-fees">Forms, fees and timeline</h2>
<table>
<thead><tr><th>Item</th><th>Detail</th></tr></thead>
<tbody>
<tr><td>Application for Divorce</td><td>Filed through the Commonwealth Courts Portal</td></tr>
<tr><td>Filing fee</td><td><strong>$1,170</strong>, or <strong>$390</strong> reduced fee if eligible (from 1 July 2026)</td></tr>
<tr><td>Acknowledgment of Service</td><td>Signed by your spouse (post) or their lawyer</td></tr>
<tr><td>Affidavit of Service by Hand</td><td>Completed by the person who served the documents</td></tr>
<tr><td>Affidavit proving signature</td><td>If the server could not identify your spouse</td></tr>
<tr><td>Application in a Proceeding + affidavit</td><td>For substituted service or dispensation</td></tr>
<tr><td>Response to Divorce</td><td>Filed by your spouse only if they oppose or dispute facts</td></tr>
<tr><td>Divorce becomes final</td><td>One month and one day after the order</td></tr>
</tbody>
</table>
<p>Fees source: {cite('fcfcoa_fees')}. Fees are indexed and change, usually on 1 July, so check the current list before filing.</p>

<h2 id="special">Separated under one roof, overseas and safety</h2>
<p>If you were separated but living in the same home for part of the 12 months, you need to support your application with an affidavit explaining the separation ({cite('fcfcoa_one_roof')}). The Court has special requirements where your spouse is overseas, in prison or has a legal incapacity. If contacting your spouse raises safety concerns, get legal advice before arranging service and protect your own contact details. In an emergency call <strong>000</strong>; for confidential support contact {RESPECT} on 1800 737 732.</p>
"""
    + cta(STD_CTA)
    + f"""
<h2 id="separate">Divorce is separate from property and parenting</h2>
<p>A divorce ends the marriage. It does not divide property or set parenting arrangements. Often an ex refuses to sign because those bigger issues are unresolved. Two points matter:</p>
<ul>
<li>Financial applications should generally be made within <strong>12 months</strong> of the divorce becoming final, so do not let property drift.</li>
<li>Mediation cannot grant a divorce, but it is often the fastest way to resolve the children and property issues that sit behind the standoff.</li>
</ul>
<p>See our <a href="/how-to-get-a-divorce-in-australia-a-step-by-step-guide/">step-by-step divorce guide</a> and the <a href="/property-settlement-mediation-guide/">property settlement mediation guide</a>.</p>
{REVIEW_NOTE}
""",
    [("Can my ex stop the divorce by not signing?",
      "No. You can make a sole application without your spouse's signature. If they want to oppose it, they must file a Response to Divorce and attend the hearing, and there are only limited grounds to oppose."),
     ("Do I need my spouse to agree to a joint application?",
      "No. If you cannot make a joint application, you can apply alone. Joint applications do not need to be served on the other spouse; sole applications do."),
     ("Does signing the acknowledgment mean my ex agrees to the divorce?",
      "No. The Court says acknowledging service does not mean the person agrees to the divorce. It only confirms they received the documents."),
     ("Can I serve the papers myself?",
      "No. Service by hand must be done by someone over 18, such as a friend, family member or professional process server, who then completes an Affidavit of Service by Hand."),
     ("How long before the hearing must service happen?",
      "At least 28 days before the hearing if your spouse is in Australia, or at least 42 days if they are overseas."),
     ("What if I cannot find my spouse?",
      "After all reasonable attempts, you can apply for substituted service or dispensation of service using an Application in a Proceeding and an affidavit. The Court recommends legal advice first."),
     ("How much does a divorce application cost?",
      "The Court's filing fee is $1,170, or $390 if you are eligible for the reduced fee, from 1 July 2026. Process server and legal fees are extra.")],
    [("how-to-get-a-divorce-in-australia-a-step-by-step-guide", "How to get a divorce in Australia"),
     ("how-long-does-a-divorce-take", "How long does a divorce take?"),
     ("divorce-without-a-lawyer", "Divorce without a lawyer"),
     ("property-settlement-mediation-guide", "Property settlement mediation"),
     ("separation-under-one-roof", "Separation under one roof"),
     ("cost-of-divorce-in-australia", "Cost of divorce in Australia")],
    read_min=11,
)
