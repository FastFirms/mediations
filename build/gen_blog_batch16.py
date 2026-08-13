#!/usr/bin/env python3
"""Batch 16 — AI Overview cannibal rebuilds.

Three posts that gained ranking position but lost impressions/clicks to AI Overviews.
Rebuilt as full cornerstones with FAQ schema, worked examples, and practitioner insight.

Slugs:
  best-apps-for-separated-parents
  my-ex-wont-sign-divorce-papers
  who-pays-bills-during-separation
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, inline_cta, callout, key_takeaway
from authority_sources import cite

# ─────────────────────────────────────────────────────────────────────────────
# 1. BEST APPS FOR SEPARATED PARENTS
# ─────────────────────────────────────────────────────────────────────────────

post(
    slug="best-apps-for-separated-parents",
    title="Best Apps for Separated Parents in Australia",
    desc="The top co-parenting apps used by separated Australian parents — from shared calendars to expense tracking and court-admissible communication logs.",
    category="Parenting",
    h1="The Best Apps for Separated Parents — <em>and the One Thing They Can't Replace</em>",
    dek=(
        "Co-parenting technology has genuinely improved life for thousands of separated "
        "Australian families. The right app reduces conflict, documents communication, "
        "and keeps both parents informed. Here is what actually works — and where apps "
        "reach their limits."
    ),
    toc=[
        ("why-apps-help", "Why co-parenting apps reduce conflict"),
        ("what-to-look-for", "What to look for in a co-parenting app"),
        ("top-apps", "The top apps for separated parents in Australia"),
        ("app-comparison", "Side-by-side comparison"),
        ("court-admissible", "Court-admissible communication logs"),
        ("expense-tracking", "Tracking shared expenses without arguments"),
        ("what-apps-cant-do", "What apps cannot do"),
        ("worked-example", "Worked example: Aisha and Daniel"),
        ("faq", "Frequently asked questions"),
    ],
    body=(
        key_takeaway(
            "The most effective co-parenting apps for separated Australian parents are "
            "OurFamilyWizard, 2Houses, and AppClose — each suited to different conflict "
            "levels and budgets. Apps reduce miscommunication and create a record, but they "
            "work best alongside a clear parenting plan agreed through mediation."
        )
        + f"""
<h2 id="why-apps-help">Why co-parenting apps reduce conflict</h2>
<p>Miscommunication is the engine of most post-separation conflict. A text misread at
11 pm, a forgotten pickup time, a disputed reimbursement — these are the everyday
frictions that escalate into formal disputes. Co-parenting apps address this by moving
communication out of personal messaging channels into a structured, timestamped
environment where everything is recorded.</p>
<p>Research from the {cite('aifs')} consistently finds that high-conflict co-parenting
harms children's wellbeing more than the separation itself. Apps that reduce the
temperature of day-to-day communication make a measurable difference — particularly
in the first two years after separation, when conflict tends to be highest.</p>
<p>Apps also create a contemporaneous record. If a parenting dispute reaches the
{cite('fcfcoa')}, timestamped, unedited communication is far more useful than
reconstructing events from memory months or years later.</p>
"""
        + inline_cta("If you're still working out the parenting arrangements, a mediator can help you reach a plan that both parents can actually follow.")
        + f"""
<h2 id="what-to-look-for">What to look for in a co-parenting app</h2>
<p>Not all apps are equal. Before choosing, consider:</p>
<ul>
  <li><strong>Tamper-proof messaging.</strong> Messages should be timestamped and
  uneditable — unlike SMS or email, which can be deleted or claimed to be out of context.</li>
  <li><strong>Shared calendar with notifications.</strong> Both parents see pickups,
  school events, medical appointments, and activity changes in real time.</li>
  <li><strong>Expense tracking.</strong> Logging and splitting costs (medical,
  extracurricular, school fees) without constant back-and-forth.</li>
  <li><strong>Document storage.</strong> A central place for school reports, medical
  records, passports, and parenting orders — accessible to both parents.</li>
  <li><strong>Court export.</strong> The ability to produce a formatted PDF of all
  communications for use in legal proceedings if needed.</li>
  <li><strong>Australian privacy compliance.</strong> The app should comply with Australian
  Privacy Act requirements for data storage and handling.</li>
</ul>
"""
        + f"""
<h2 id="top-apps">The top apps for separated parents in Australia</h2>

<h3>OurFamilyWizard</h3>
<p>OurFamilyWizard is the most court-accepted co-parenting platform in use in Australia
and internationally. Its <strong>ToneMeter</strong> feature flags messages that may be
read as hostile before they are sent — a surprisingly effective circuit-breaker in
high-conflict situations. It includes a shared calendar, expense log, info bank for
documents, and a journal. Messages cannot be edited or deleted after sending.</p>
<p><strong>Cost:</strong> approximately AUD $199 per parent per year. Some family
lawyers recommend it specifically for clients in high-conflict arrangements because of
the court-ready export.</p>
<p><strong>Best for:</strong> high-conflict situations; cases involving legal proceedings
or where a court record may be needed.</p>

<h3>2Houses</h3>
<p>2Houses is a solid mid-tier option with a clean interface, shared calendar, expense
tracking, and a document store. It lacks OurFamilyWizard's tone analysis but is more
affordable and sufficient for the majority of separated parents.</p>
<p><strong>Cost:</strong> approximately AUD $15–$20 per month per household.</p>
<p><strong>Best for:</strong> moderate-conflict situations; parents who want structure
without the premium price.</p>

<h3>Cozi</h3>
<p>Cozi is a free family organiser — not purpose-built for separation, but widely used
by separated parents for its shared calendar and shopping/task lists. It lacks messaging
logs and court-export features. Appropriate only for low-conflict arrangements.</p>
<p><strong>Cost:</strong> free (Cozi Gold is approximately AUD $45/year for extra features).</p>
<p><strong>Best for:</strong> low-conflict co-parents who just need a shared calendar.</p>

<h3>AppClose</h3>
<p>AppClose is a free co-parenting app that includes messaging, a shared calendar,
expense tracking, and child information storage. A paid version adds court-ready
reports. It is less widely known in Australia than OurFamilyWizard but offers
comparable core features at a lower price point.</p>
<p><strong>Cost:</strong> free, with paid plan approximately AUD $15/month.</p>
<p><strong>Best for:</strong> cost-conscious parents who need more than a basic calendar.</p>

<h3>MyMedici</h3>
<p>MyMedici is an Australian-built platform designed for family coordination including
separated parents. It includes a calendar, shared task lists, and a family hub. Less
court-focused than OurFamilyWizard but built with Australian privacy standards.</p>
<p><strong>Cost:</strong> free tier available; premium approximately AUD $100/year.</p>
<p><strong>Best for:</strong> parents who prefer an Australian-developed product.</p>
"""
        + inline_cta("A clear parenting plan — agreed through mediation — makes co-parenting apps far more effective. Book a free initial consultation.")
        + f"""
<h2 id="app-comparison">Side-by-side comparison</h2>
<figure class="tbl">
<table>
<caption>Co-parenting app comparison for Australian separated parents</caption>
<thead>
<tr>
  <th>App</th>
  <th>Approx. cost (AUD/yr)</th>
  <th>Tamper-proof msgs</th>
  <th>Court export</th>
  <th>Expense tracking</th>
  <th>Best for</th>
</tr>
</thead>
<tbody>
<tr>
  <td>OurFamilyWizard</td>
  <td>~$398 (both parents)</td>
  <td>Yes</td>
  <td>Yes</td>
  <td>Yes</td>
  <td>High conflict / legal proceedings</td>
</tr>
<tr>
  <td>2Houses</td>
  <td>~$360 (both parents)</td>
  <td>Yes</td>
  <td>Yes</td>
  <td>Yes</td>
  <td>Moderate conflict</td>
</tr>
<tr>
  <td>AppClose</td>
  <td>Free / ~$360 paid</td>
  <td>Yes</td>
  <td>Paid only</td>
  <td>Yes</td>
  <td>Budget-conscious</td>
</tr>
<tr>
  <td>Cozi</td>
  <td>Free / ~$45 Gold</td>
  <td>No</td>
  <td>No</td>
  <td>No</td>
  <td>Low conflict / calendar only</td>
</tr>
<tr>
  <td>MyMedici</td>
  <td>Free / ~$100</td>
  <td>Partial</td>
  <td>No</td>
  <td>Yes</td>
  <td>Australian privacy preference</td>
</tr>
</tbody>
</table>
<p class="source-note">Prices are indicative as at mid-2026 and may vary. Check each provider's current pricing.</p>
</figure>
"""
        + f"""
<h2 id="court-admissible">Court-admissible communication logs</h2>
<p>If your co-parenting dispute is heading toward the {cite('fcfcoa')}, the way you
communicate now will matter later. SMS and email can be screenshotted, cropped, and
presented selectively. Co-parenting apps with tamper-proof logging produce a complete,
unedited record — which courts tend to find more credible than cherry-picked
screenshots.</p>
<p>OurFamilyWizard explicitly markets its court-export feature to family lawyers and
is the most commonly recommended platform by Australian family law practitioners for
this purpose. If you are currently in proceedings — or think you might be — it is
worth the subscription cost.</p>
<p>One practical note: switching communication to a dedicated app mid-dispute can
itself be contentious if the other parent refuses to use it. A mediator can help you
agree on a communication platform as part of a parenting plan, which avoids the
standoff entirely.</p>
"""
        + inline_cta("Having trouble getting the other parent to agree on ground rules? A mediator can help you establish a communication framework both parents will actually follow.")
        + f"""
<h2 id="expense-tracking">Tracking shared expenses without arguments</h2>
<p>Shared child-related expenses — medical costs, school excursions, sport fees,
clothing — are a consistent source of post-separation conflict. The default position
under {cite('services_australia_cs')} child support arrangements is that the paying
parent's child support covers ordinary costs, with some extraordinary costs shared by
agreement.</p>
<p>"By agreement" is where things often break down. Co-parenting apps with expense
tracking create a log of what was spent, what was agreed, and what remains outstanding —
removing the "I never agreed to pay for that" ambiguity.</p>
<p>A well-drafted parenting plan will specify which categories of expense require
prior agreement and how they are to be split. This is something we routinely work
through with parents in mediation — the app then just implements the plan.</p>
"""
        + inline_cta("Need help agreeing on how to split expenses? Our mediators work through parenting finances with you so both parents know exactly where they stand.")
        + f"""
<h2 id="what-apps-cant-do">What apps cannot do</h2>
<p>Co-parenting apps are tools, not solutions. They cannot:</p>
<ul>
  <li>Create a parenting arrangement where none has been agreed</li>
  <li>Resolve a genuine dispute about where a child lives or spends time</li>
  <li>Replace the co-parenting relationship — a child's wellbeing depends on both
  parents being able to work together, not on which app they use</li>
  <li>Protect a parent or child where there is family violence or safety risk</li>
</ul>
"""
        + callout(
            "If there is family violence",
            "If you are using a co-parenting app in a situation involving family violence "
            "or coercive control, get specialist advice before enabling location-sharing "
            "or other monitoring features. Call 1800RESPECT on 1800 737 732 for "
            "confidential support, or see our guide to domestic violence and family law."
        )
        + f"""
<p>The foundation of good co-parenting is a clear, agreed arrangement — one that both
parents understand and can actually follow. A <a href="/parenting-plans-guide/">parenting
plan</a> agreed through <a href="/child-custody-mediation/">mediation</a> gives the app
something real to implement. Without it, you are using sophisticated software to manage
an unresolved dispute.</p>
"""
        + inline_cta("Ready to agree on a parenting arrangement? Our FDR practitioners work with separated parents across Australia — in person and online.")
        + f"""
<h2 id="worked-example">Worked example: Aisha and Daniel</h2>
<p>Aisha and Daniel separated in early 2025, with two children aged 7 and 10. Their
initial week-about arrangement was agreed verbally but created constant friction: missed
pickups, disputed school holiday splits, and ongoing arguments over who had paid for
swimming lessons.</p>
<p>Through mediation, they formalised a parenting plan that specified:</p>
<ul>
  <li>Week-about care with handover Sunday 5 pm at a neutral location</li>
  <li>Extraordinary expenses over $150 requiring both parents' written agreement before
  being incurred</li>
  <li>School holidays alternating yearly, with Christmas Eve–26 December with one parent
  and 27 December–New Year with the other</li>
  <li>OurFamilyWizard as the agreed communication platform for all co-parenting matters</li>
</ul>
<p>Within three months, both reported significantly less conflict. The app did not
change their relationship — but the plan gave them clear rules, and the app gave them
a record to point to when disputes arose. The parenting plan was later filed as consent
orders, making it legally enforceable.</p>
<p><strong>Dan Toombs, FDRP:</strong> "I see this pattern constantly. Parents arrive
with an app already installed and no agreement underneath it. The technology is
fine — but without a clear parenting plan, the app just becomes another place to
have the same argument."</p>
"""
        + inline_cta("A parenting plan agreed through mediation gives co-parenting apps something real to work with. Book a consultation to get started.")
    ),
    qa=[
        (
            "What is the best free co-parenting app in Australia?",
            "Cozi is the most popular free option, but it lacks tamper-proof messaging "
            "and court-export features. AppClose offers a free tier with more co-parenting "
            "specific features. For high-conflict situations, OurFamilyWizard or 2Houses "
            "are worth the cost."
        ),
        (
            "Can co-parenting app messages be used in Family Court?",
            "Yes — messages from apps with tamper-proof logging such as OurFamilyWizard "
            "can be exported in a court-ready format. They are generally considered more "
            "reliable than screenshots of SMS or email, which can be edited or taken "
            "out of context."
        ),
        (
            "What if the other parent refuses to use a co-parenting app?",
            "You cannot force the other parent to use an app. However, if you are working "
            "through a parenting plan in mediation, the choice of communication platform "
            "can be included as one of the agreed terms. Refusal to use an agreed platform "
            "can be relevant in any subsequent court proceedings."
        ),
        (
            "Do co-parenting apps track location?",
            "Some apps include optional location-sharing features. Whether to use these "
            "is a matter for both parents to agree on. If there is a family violence "
            "concern, location-sharing should not be enabled without specialist advice."
        ),
        (
            "Is OurFamilyWizard available in Australia?",
            "Yes. OurFamilyWizard is available to Australian users and is widely recommended "
            "by Australian family law practitioners. Pricing is in USD — check their website "
            "for current rates."
        ),
        (
            "What is the difference between a parenting plan and a co-parenting app?",
            "A parenting plan is a written agreement about how separated parents will raise "
            "their children. A co-parenting app helps implement that agreement day-to-day. "
            "The plan comes first — the app makes it easier to follow."
        ),
    ],
    related=[
        ("parenting-plans-guide", "Parenting Plans: The Complete Guide"),
        ("child-custody-mediation", "Child Custody Mediation"),
        ("co-parenting-mediation", "Co-Parenting Mediation"),
        ("domestic-violence-and-family-law", "Family Violence and Family Law"),
        ("high-conflict-mediation", "Mediation in High-Conflict Separations"),
        ("questions/do-i-need-mediation-before-family-court", "Do I Need Mediation Before Family Court?"),
    ],
    read_min=7,
)

# ─────────────────────────────────────────────────────────────────────────────
# 2. MY EX WON'T SIGN DIVORCE PAPERS
# ─────────────────────────────────────────────────────────────────────────────

post(
    slug="my-ex-wont-sign-divorce-papers",
    title="My Ex Won't Sign the Divorce Papers",
    desc="In Australia, your spouse cannot block a divorce by refusing to sign. Learn how a sole-applicant divorce works, typical costs, and when mediation helps.",
    category="Divorce",
    h1="My Ex Won't Sign the Divorce Papers — <em>Here's What Actually Happens</em>",
    dek=(
        "One of the most common fears after separation: what if my ex refuses to sign "
        "the divorce? The answer is more straightforward than most people expect — "
        "and the refusal itself usually has nothing to do with the divorce papers at all."
    ),
    toc=[
        ("can-they-block-divorce", "Can your ex actually block the divorce?"),
        ("how-divorce-works-australia", "How divorce works in Australia"),
        ("sole-applicant", "Applying for divorce without your ex"),
        ("what-theyre-really-refusing", "What they're really refusing"),
        ("property-and-parenting", "Property and parenting are separate from divorce"),
        ("service-and-non-response", "What if your ex ignores the papers?"),
        ("timeline-and-cost", "Timeline and cost"),
        ("worked-example", "Worked example: Sophie's sole-applicant divorce"),
        ("faq", "Frequently asked questions"),
    ],
    body=(
        key_takeaway(
            "In Australia, your spouse cannot legally prevent a divorce by refusing to "
            "sign. You can apply as a sole applicant once you have been separated for "
            "12 months. The divorce itself is a straightforward administrative process — "
            "what your ex may actually be resisting is the property or parenting settlement, "
            "which is where mediation helps."
        )
        + f"""
<h2 id="can-they-block-divorce">Can your ex actually block the divorce?</h2>
<p>No. Under the {cite('family_law_act')}, the only ground for divorce is irretrievable
breakdown of the marriage, established by at least 12 months of separation. There is
no concept of fault and no mechanism for one spouse to veto a divorce the other spouse
genuinely wants.</p>
<p>If your ex refuses to sign a joint application, you apply as a sole applicant instead.
The court does not require your ex's agreement. Their signature is not needed.</p>
<p>What your ex can do is contest whether you have actually been separated for 12 months —
but this is rare and difficult to sustain if you have lived apart, maintained separate
finances, or told friends and family about the separation.</p>
"""
        + inline_cta("Confused about what your ex can and can't affect in a separation? A free initial consultation with one of our mediators can help you understand what's actually at stake.")
        + f"""
<h2 id="how-divorce-works-australia">How divorce works in Australia</h2>
<p>A divorce in Australia is granted by the {cite('fcfcoa')} once you have been
separated for at least 12 months. The application is made through the Commonwealth
Courts Portal. You can apply jointly with your spouse, or alone as a sole applicant.</p>
<p>Joint applications are slightly simpler to process, but sole applications are
entirely routine — the {cite('fcfcoa')} grants thousands of sole-applicant divorces
every year.</p>
<p>The filing fee as at 2026 is approximately $940 for a standard application, or $315
if you hold a concession card. See {cite('fcfcoa_fees')} for current rates.</p>
<p>Where children under 18 are involved, the court must be satisfied that proper
arrangements have been made for their care. This is a threshold requirement — it is
not a contested hearing about parenting, merely a procedural check.</p>
"""
        + f"""
<h2 id="sole-applicant">Applying for divorce without your ex</h2>
<p>A sole-applicant divorce follows the same legal process as a joint application, with
one additional step: you must serve the divorce application on your spouse. This means
they receive formal notice that the application has been made — they do not have to
agree to it.</p>
<p>Service is typically done by a process server or registered post with acknowledgement.
Once served, your ex has 28 days to respond. If they do not respond, the court proceeds
with the application anyway. If they respond to dispute the separation period, a
hearing is listed — but the bar for contesting successfully is high.</p>
<p>The divorce order is made at or after the hearing and takes effect one month later.</p>
"""
        + inline_cta("If your ex isn't cooperating on separation matters, our mediators can clarify what steps actually need their agreement — and what doesn't.")
        + f"""
<h2 id="what-theyre-really-refusing">What they're really refusing</h2>
<p>When a spouse says they "won't sign the divorce papers," they usually mean something
else. They may be:</p>
<ul>
  <li>Trying to delay the property settlement — a 12-month time limit to apply for
  property orders starts from the divorce date, and some spouses mistakenly believe
  refusing the divorce buys them time</li>
  <li>Using non-cooperation as leverage in negotiations about the family home, children,
  or financial support</li>
  <li>Genuinely distressed about the end of the marriage and not ready to formalise it</li>
  <li>Confused — some people believe agreeing to the divorce means agreeing to a
  particular financial split</li>
</ul>
<p>Understanding which of these is actually happening is the key to resolving it —
and often the right tool is mediation, not a court application.</p>
<p><strong>Dan Toombs, FDRP:</strong> "I've sat with many people who've told me their
ex 'won't cooperate'. In almost every case, what the other party is actually worried
about is the financial outcome — not the divorce itself. Once we address that fear
directly, the cooperation usually follows."</p>
"""
        + callout(
            "The property time limit matters",
            "Once a divorce is granted, you have 12 months to apply to the Family Court "
            "for property orders. If this deadline passes without an application or a "
            "binding financial agreement, you may need the court's leave to proceed. "
            "Don't delay the property settlement after the divorce is granted."
        )
        + f"""
<h2 id="property-and-parenting">Property and parenting are separate from divorce</h2>
<p>The divorce order dissolves the marriage. It does not resolve property, superannuation,
parenting arrangements, or spousal maintenance. These are entirely separate legal
processes under the {cite('family_law_act')}.</p>
<p>If your ex is resisting because they are worried about the financial consequences —
mistakenly believing that signing locks in a financial outcome — that misunderstanding
is worth addressing directly. Getting the divorce underway does not prejudge who gets what.</p>
<p>Property and parenting matters are where your ex's cooperation actually makes a
practical difference. This is where <a href="/property-settlement-mediation-guide/">
property settlement mediation</a> or <a href="/child-custody-mediation/">parenting
mediation</a> can unlock a resolution.</p>
"""
        + inline_cta("Property and parenting are where your ex's cooperation actually matters. A mediator can help you reach agreement without going to court.")
        + f"""
<h2 id="service-and-non-response">What if your ex ignores the papers?</h2>
<p>If your ex is served with a sole-applicant divorce application and simply ignores it —
does not respond and does not appear at the hearing — the court will typically grant the
divorce regardless. Non-response is treated as non-objection.</p>
<p>If you cannot locate your ex to serve them, there are provisions for substituted
service (such as service through a known contact or electronically) or, in rare cases,
dispensation from service. These require a family lawyer's assistance.</p>
<p>In all cases, the court's focus is on whether the marriage has irretrievably broken
down — not on whether both parties have cooperated.</p>
"""
        + inline_cta("Need to move forward when your ex won't engage? A mediator can help — and if mediation isn't possible, we can explain your options. Book a free consultation.")
        + f"""
<h2 id="timeline-and-cost">Timeline and cost</h2>
<figure class="tbl">
<table>
<caption>Typical sole-applicant divorce timeline and costs in Australia (2026)</caption>
<thead>
<tr>
  <th>Step</th>
  <th>Typical timeframe</th>
  <th>Typical cost</th>
</tr>
</thead>
<tbody>
<tr>
  <td>File sole application (Commonwealth Courts Portal)</td>
  <td>Day 1</td>
  <td>$940 standard / $315 concession</td>
</tr>
<tr>
  <td>Serve documents on spouse</td>
  <td>1–3 weeks after filing</td>
  <td>$150–$350 (process server)</td>
</tr>
<tr>
  <td>Response period</td>
  <td>28 days from service</td>
  <td>Nil</td>
</tr>
<tr>
  <td>Uncontested hearing listed</td>
  <td>~4–8 weeks after response period</td>
  <td>Nil (telephone or online)</td>
</tr>
<tr>
  <td>Divorce order made</td>
  <td>At or after hearing</td>
  <td>Nil</td>
</tr>
<tr>
  <td>Divorce takes effect</td>
  <td>1 month after order</td>
  <td>Nil</td>
</tr>
<tr>
  <td><strong>Total (typical, self-represented)</strong></td>
  <td><strong>4–6 months from filing</strong></td>
  <td><strong>~$1,100–$1,500</strong></td>
</tr>
</tbody>
</table>
<p class="source-note">Filing fees sourced from {cite('fcfcoa_fees')}. Process server costs vary by location.</p>
</figure>
"""
        + f"""
<h2 id="worked-example">Worked example: Sophie's sole-applicant divorce</h2>
<p>Sophie and Marcus separated in March 2024 after an eight-year marriage. They have
two children aged 5 and 8. Marcus refused to discuss the divorce and told mutual
friends he "would never sign."</p>
<p>Step by step:</p>
<ol>
  <li><strong>September 2025:</strong> 12 months of separation reached. Sophie filed a
  sole-applicant divorce through the Commonwealth Courts Portal. Filing fee: $940.</li>
  <li><strong>October 2025:</strong> A process server served Marcus at his home address.
  Cost: approximately $200.</li>
  <li><strong>November 2025:</strong> Marcus did not respond. The matter was listed for
  an uncontested hearing. Sophie did not need to attend.</li>
  <li><strong>December 2025:</strong> Divorce order granted, taking effect January 2026.</li>
  <li><strong>Meanwhile:</strong> Sophie and Marcus attended mediation to resolve the
  property settlement. This was resolved by agreement in February 2026 and formalised
  as consent orders.</li>
</ol>
<p>Marcus's refusal to "sign the papers" delayed nothing. The divorce proceeded on
Sophie's timeline. The mediated property settlement cost each of them approximately
$2,500 — compared to an estimated $30,000–$60,000 each for a contested property hearing.</p>
"""
        + inline_cta("If your ex isn't cooperating on property or parenting, mediation is usually faster and far cheaper than court. Book a free consultation.")
    ),
    qa=[
        (
            "Can my ex prevent me from getting a divorce in Australia?",
            "No. In Australia, one spouse cannot legally block a divorce. The only ground "
            "is 12 months of separation. You can apply as a sole applicant without your "
            "ex's signature or agreement."
        ),
        (
            "Do both parties need to sign divorce papers in Australia?",
            "No. A joint application requires both parties to sign, but you can apply as "
            "a sole applicant instead. Your ex must be served with the application but "
            "their signature is not required."
        ),
        (
            "What if my ex refuses to be served with divorce papers?",
            "If your ex is deliberately evading service, you can apply to the court for "
            "substituted service or dispensation from service. A family lawyer can assist "
            "with this."
        ),
        (
            "Does getting divorced affect the property settlement?",
            "The divorce order does not decide property — they are separate processes. "
            "However, once divorced you have 12 months to apply to the court for property "
            "orders. Don't delay resolving property after the divorce is granted."
        ),
        (
            "How long does a sole-applicant divorce take in Australia?",
            "From filing to the divorce taking effect, a sole-applicant divorce typically "
            "takes four to six months — roughly one month to serve, one month response "
            "period, a few weeks for the hearing, then one month until the order takes effect."
        ),
        (
            "My ex says they'll contest the divorce. Should I be worried?",
            "Rarely. A spouse can only contest a divorce on the ground that you have not "
            "actually been separated for 12 months. If you have genuinely lived separately "
            "and apart, this is difficult to establish. The vast majority of contested "
            "applications are resolved in the applicant's favour."
        ),
    ],
    related=[
        ("how-to-get-a-divorce-in-australia-a-step-by-step-guide", "How to Get a Divorce in Australia"),
        ("property-settlement-after-separation", "Property Settlement After Separation"),
        ("how-long-does-a-divorce-take", "How Long Does a Divorce Take?"),
        ("bfa-or-consent-orders", "Consent Orders vs Binding Financial Agreements"),
        ("separation-guide", "The Complete Separation Guide"),
        ("divorce-without-a-lawyer", "Divorce Without a Lawyer"),
    ],
    read_min=7,
)

# ─────────────────────────────────────────────────────────────────────────────
# 3. WHO PAYS BILLS DURING SEPARATION
# ─────────────────────────────────────────────────────────────────────────────

post(
    slug="who-pays-bills-during-separation",
    title="Who Pays Bills During Separation in Australia?",
    desc="Who is responsible for the mortgage, utilities, and joint debts during separation? Australian law explained with a practical worked example.",
    category="Property",
    h1="Who Pays Bills During Separation — <em>and How to Avoid the Most Common Traps</em>",
    dek=(
        "The question of who pays the mortgage, the car loan, the utilities, and the "
        "joint credit card during separation has no single legal answer — but there are "
        "clear principles, practical arrangements that work, and traps that cost "
        "separating couples thousands of dollars unnecessarily."
    ),
    toc=[
        ("legal-position", "The legal position: joint debts, joint responsibility"),
        ("mortgage", "The family home mortgage"),
        ("utilities-and-insurance", "Utilities, insurance, and running costs"),
        ("joint-credit-cards", "Joint credit cards and personal loans"),
        ("who-gets-the-benefit", "The key question: who is getting the benefit?"),
        ("interim-agreement", "Reaching an interim financial agreement"),
        ("what-not-to-do", "What not to do during separation"),
        ("worked-example", "Worked example: Tom and Rebecca"),
        ("faq", "Frequently asked questions"),
    ],
    body=(
        key_takeaway(
            "During separation, both spouses remain legally responsible for joint debts "
            "regardless of who is living in the property or using the service. The practical "
            "rule is: whoever benefits pays, and both parties document everything. An interim "
            "agreement — ideally reached through mediation — protects both parties until the "
            "property settlement is finalised."
        )
        + f"""
<h2 id="legal-position">The legal position: joint debts, joint responsibility</h2>
<p>Separation does not change your legal obligations to creditors. If you and your spouse
are both named on a mortgage, a car loan, or a credit card, you both remain fully liable
for those debts — regardless of who is living where, who is using what, or what informal
arrangement you have reached between yourselves.</p>
<p>Creditors are not bound by your separation agreement. If your spouse stops paying
their half of the mortgage, the bank's recourse is against both of you. This is the
single most important thing to understand about financial obligations during separation.</p>
<p>The {cite('family_law_act')} governs how assets and debts are ultimately divided in
a property settlement — but that process takes time. In the interim, someone has to
pay the bills.</p>
"""
        + inline_cta("Not sure how to manage finances while you work toward a property settlement? A mediator can help you reach an interim agreement that protects you both.")
        + f"""
<h2 id="mortgage">The family home mortgage</h2>
<p>The mortgage is usually the largest and most urgent obligation. Three scenarios
commonly arise:</p>

<h3>One spouse stays in the home</h3>
<p>If one spouse remains in the family home, they typically take responsibility for
the mortgage payments during the separation period. These payments should be documented
carefully — they are relevant to the property settlement, since the paying spouse is
effectively servicing an asset that will be divided.</p>

<h3>Both spouses leave</h3>
<p>If the home is vacant or rented, rental income should cover or offset the mortgage.
Both parties should agree in writing on who manages the property and how income and
expenses are handled during the interim period.</p>

<h3>Neither can afford the mortgage alone</h3>
<p>This is the hardest situation. Options include: both continuing to contribute to the
mortgage while the property is sold; one party refinancing; or agreeing to list the
property for sale immediately. A mediator can help you reach a practical resolution
without letting arrears accumulate and damage both parties' credit.</p>
<p>Falling behind on the mortgage during separation can result in the bank taking
recovery action — which harms both parties regardless of who is at fault. Acting quickly
gives you more options.</p>
"""
        + inline_cta("If the mortgage is becoming unmanageable during separation, acting early gives you more options. A mediator can help you reach an interim arrangement.")
        + f"""
<h2 id="utilities-and-insurance">Utilities, insurance, and running costs</h2>
<figure class="tbl">
<table>
<caption>Who typically pays household bills during separation in Australia</caption>
<thead>
<tr>
  <th>Bill type</th>
  <th>Practical default</th>
  <th>Notes</th>
</tr>
</thead>
<tbody>
<tr>
  <td>Mortgage / rent</td>
  <td>Whoever is living in the property</td>
  <td>Document all payments — relevant to property settlement</td>
</tr>
<tr>
  <td>Electricity, gas, water</td>
  <td>Whoever is using the property</td>
  <td>Transfer accounts out of departing spouse's name early</td>
</tr>
<tr>
  <td>Home and contents insurance</td>
  <td>Both parties have an interest — should continue until settlement</td>
  <td>Notify insurer of change in circumstances; lapse can void cover</td>
</tr>
<tr>
  <td>Car insurance and registration</td>
  <td>Whoever is using the vehicle</td>
  <td>Update policy to reflect actual driver</td>
</tr>
<tr>
  <td>Council rates</td>
  <td>Usually the occupying spouse, or split by agreement</td>
  <td>Keep paid — rates debt attaches to the property</td>
</tr>
<tr>
  <td>Body corporate fees</td>
  <td>Whoever remains in strata property</td>
  <td>Unpaid levies attach to the lot</td>
</tr>
<tr>
  <td>Internet / subscriptions</td>
  <td>Cancel joint accounts; each party takes their own</td>
  <td>Simplest to separate immediately</td>
</tr>
</tbody>
</table>
<p class="source-note">These are practical defaults, not legal rules. Your interim agreement
should specify what applies in your situation.</p>
</figure>
<p>A practical first step is to separate utilities quickly — transfer electricity, gas,
and internet accounts into the name of whoever is staying in the property. This prevents
disputes about bills that accumulate in a departed spouse's name.</p>
"""
        + f"""
<h2 id="joint-credit-cards">Joint credit cards and personal loans</h2>
<p>Joint credit card debt is owed by both cardholders regardless of who incurred it.
If your spouse runs up the joint credit card after separation, you are still legally
liable to the bank — though you may have a claim against your spouse in the property
settlement.</p>
<p>Practical steps to take early:</p>
<ul>
  <li>Contact the bank to remove your spouse as a joint cardholder, converting the
  account to a sole account</li>
  <li>If the account cannot be converted, request a credit freeze or reduction in limit</li>
  <li>Open individual accounts in your own name and stop using joint accounts for new spending</li>
  <li>Document the balance as at the date of separation — this becomes the baseline for
  the property settlement</li>
</ul>
<p>Joint personal loans are more complex to separate, as the lender must agree to release
one borrower. In practice, joint loans are usually allocated to one party as part of the
property settlement and refinanced into their sole name at that point.</p>
"""
        + inline_cta("Separating finances is complicated. A mediator can help you reach an interim arrangement that prevents debt accumulating while you work toward a final settlement.")
        + f"""
<h2 id="who-gets-the-benefit">The key question: who is getting the benefit?</h2>
<p>The practical principle that courts and mediators apply to interim financial
arrangements is: <strong>whoever is getting the benefit of an asset or service should
bear the cost of maintaining it during the separation period.</strong></p>
<p>This is a fairness principle, not a strict legal rule. If one spouse is living in
the family home rent-free while the other rents separately, it is generally fair for
the occupying spouse to pay the mortgage, rates, insurance, and running costs. If the
family car is being used by one spouse, they should cover the insurance and running costs.</p>
<p>Where the "benefit" is less clear — for example, a rental property jointly owned
but managed by one spouse — documenting income, expenses, and management arrangements
becomes important for the eventual property settlement.</p>
"""
        + f"""
<h2 id="interim-agreement">Reaching an interim financial agreement</h2>
<p>The cleanest way to manage finances during separation is through a written interim
agreement that specifies:</p>
<ul>
  <li>Who pays the mortgage (and whether payments are credited in the property settlement)</li>
  <li>Who pays household utilities and how accounts are to be transferred</li>
  <li>What happens with any joint credit cards or loans</li>
  <li>How joint bank accounts are to be managed until the property settlement</li>
  <li>What level of spending from joint accounts (if any) is agreed</li>
</ul>
<p>An interim agreement reached in <a href="/property-settlement-mediation-guide/">
property mediation</a> can be written up and signed by both parties, providing
certainty for both sides while the full property settlement is worked through.</p>
<p>If circumstances are complex — a business, significant debt, or one party refusing
to contribute — a family lawyer can advise on interim orders from the
{cite('fcfcoa')} for financial maintenance during the separation period.</p>
"""
        + callout(
            "Financial disclosure is required",
            "Both parties to a family law property settlement are required to make full "
            "and frank disclosure of all income, assets, debts, and superannuation. "
            "See the FCFCOA's duty of disclosure guidance. Failing to disclose can have "
            "serious consequences in subsequent proceedings."
        )
        + inline_cta("An interim financial agreement through mediation gives both parties certainty while the property settlement is resolved. Book a consultation to get started.")
        + f"""
<h2 id="what-not-to-do">What not to do during separation</h2>
<p>These actions tend to make property settlements more contested, more expensive, and
more damaging to both parties:</p>
<ul>
  <li><strong>Stopping mortgage payments unilaterally.</strong> This harms both parties'
  credit and can accelerate the bank's enforcement timeline. Always communicate with
  the lender if payments are at risk.</li>
  <li><strong>Draining joint accounts.</strong> Taking more than your fair share from
  a joint account can be undone in a property settlement — often at significant cost.</li>
  <li><strong>Running up joint credit cards.</strong> Post-separation spending on a joint
  card is generally allocated to the person who incurred it and becomes a point of dispute.</li>
  <li><strong>Cancelling the other party's access to shared accounts without agreement.</strong>
  Courts view this dimly, particularly if it leaves the other party unable to meet living expenses.</li>
  <li><strong>Delaying the property settlement unnecessarily.</strong> Time limits apply —
  12 months from divorce, or two years from the end of a de facto relationship. Missing
  these deadlines complicates your ability to apply for orders.</li>
</ul>
"""
        + f"""
<h2 id="worked-example">Worked example: Tom and Rebecca</h2>
<p>Tom and Rebecca separated in June 2025. They own a home worth approximately $900,000
with a $520,000 mortgage. Rebecca stayed in the home with the two children; Tom rented
a unit nearby for $2,200 per month.</p>
<p><strong>The problem:</strong> the mortgage was $3,400 per month, in both names.
Rebecca earned $72,000 per year; Tom earned $120,000. Rebecca could not cover the
mortgage alone. Tom was already paying $2,200 rent and did not feel it was fair to
also pay the full mortgage on a home he wasn't living in.</p>
<p><strong>What they agreed through mediation:</strong></p>
<ul>
  <li>Tom would contribute $2,200 per month toward the mortgage — equivalent to his
  rental cost, on the principle that he should pay roughly what he would spend on
  accommodation regardless</li>
  <li>Rebecca would cover the remaining $1,200 per month from her income</li>
  <li>Tom's contributions would be documented and taken into account in the property
  settlement as payments toward a joint asset</li>
  <li>Utilities, rates, and insurance were Rebecca's responsibility as the occupant</li>
  <li>Neither party would draw on the joint offset account without the other's written consent</li>
</ul>
<p>This arrangement cost each party approximately $1,200 to reach through mediation.
It prevented mortgage arrears risk and gave both parties certainty for the eight months
it took to finalise the property settlement.</p>
<p>The property settlement was ultimately resolved at mediation — the home was
transferred to Rebecca, who refinanced in her own name, with Tom receiving a cash
payment from the equity plus a superannuation split. Total mediation cost: approximately
$5,000 shared. Estimated litigation cost if contested: $60,000–$120,000 each.</p>
<p><strong>Dan Toombs, FDRP:</strong> "The interim financial arrangement is often the
hardest conversation to have, because both parties feel financially squeezed right when
their expenses have doubled. Getting that arrangement right in the first few months of
separation prevents a huge amount of conflict later."</p>
"""
        + inline_cta("An interim financial arrangement through mediation can save both parties significant stress and money. Book a free initial consultation.")
    ),
    qa=[
        (
            "Who is legally responsible for the mortgage during separation?",
            "Both spouses remain jointly and severally liable for the mortgage until it is "
            "refinanced or the property is sold. The bank does not recognise a separation "
            "agreement — if one party stops paying, the other remains fully liable."
        ),
        (
            "Can I stop paying bills if my ex is living in the house?",
            "Stopping payments on joint debts risks harming your credit and can accelerate "
            "enforcement action. The practical approach is to reach an interim agreement — "
            "usually through mediation — that reflects who is getting the benefit of the property."
        ),
        (
            "What happens to joint debt in an Australian property settlement?",
            "In the property settlement under the Family Law Act, debts are allocated to "
            "one party as part of the overall adjustment. If a joint debt is allocated to "
            "your spouse, they are responsible for it — but you remain liable to the creditor "
            "until the debt is refinanced or paid out."
        ),
        (
            "Can I close a joint bank account during separation?",
            "You generally have the right to operate or close a joint account, but doing "
            "so unilaterally — particularly if it leaves your spouse without access to funds — "
            "can be viewed poorly by the Family Court and may breach financial disclosure "
            "obligations. Get advice before taking this step."
        ),
        (
            "What if my ex runs up debt on a joint credit card after separation?",
            "Post-separation spending on a joint card is generally allocated to the "
            "cardholder who incurred it in the property settlement, but the bank holds "
            "both parties responsible. The practical solution is to remove yourself or "
            "your spouse as a joint cardholder as quickly as possible."
        ),
        (
            "Do I have to keep paying insurance on assets my ex is using?",
            "The occupying spouse should bear the insurance costs for assets they are "
            "using. However, if a joint asset is uninsured and something goes wrong, "
            "both parties bear the loss. Negotiate who pays, but keep the cover in place."
        ),
    ],
    related=[
        ("property-settlement-after-separation", "Property Settlement After Separation"),
        ("property-settlement-mediation-guide", "Property Settlement Mediation Guide"),
        ("bfa-or-consent-orders", "Consent Orders vs Binding Financial Agreements"),
        ("what-is-in-the-property-pool", "What Is In the Property Pool?"),
        ("separation-guide", "The Complete Separation Guide"),
        ("delaying-property-settlement", "The Risks of Delaying Property Settlement"),
    ],
    read_min=8,
)
