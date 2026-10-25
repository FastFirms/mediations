"""gen_blog_batch24.py — Two new cornerstones:
1. christmas-parenting-arrangements-after-separation — agreeing Christmas and summer holiday care
2. how-to-change-parenting-orders — varying final parenting orders by agreement or application
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, key_takeaway, inline_cta, callout
from authority_sources import cite


# ── POST 1: CHRISTMAS PARENTING ARRANGEMENTS AFTER SEPARATION ────────────────

post(
    "christmas-parenting-arrangements-after-separation",
    "Christmas Parenting Arrangements After Separation",
    "How separated parents share Christmas and summer holidays in Australia: common "
    "schedules, court cut-off dates, travel rules and agreeing early in mediation.",
    "Parenting &amp; children",
    "Christmas parenting arrangements after separation: <em>a calmer holiday starts with an early agreement</em>",
    ("For separated families, Christmas can be the most emotionally loaded week of the year. "
     "Who wakes up with the children, who hosts lunch, who gets the beach week — small questions "
     "that can turn into big disputes when they are left to December. This guide covers the "
     "arrangements that work for Australian families, the deadlines that matter, and how to agree "
     "a plan early, without turning the holidays into a court matter."),
    [
        ("why-early",        "Why Christmas arrangements need to start early"),
        ("common-schedules", "Common Christmas schedules that work"),
        ("summer-holidays",  "Sharing the summer school holidays"),
        ("existing-orders",  "If you already have parenting orders or a plan"),
        ("court-cutoff",     "The court's Christmas cut-off and urgent applications"),
        ("travel",           "Interstate and overseas travel over the holidays"),
        ("mediation",        "Agreeing a holiday plan through mediation"),
        ("children-first",   "Keeping the day about the children"),
    ],
    key_takeaway(
        "There is no default rule for who has the children at Christmas in Australia. Separated "
        "parents can agree any arrangement that is in the children's best interests — alternating "
        "years, splitting the day, or celebrating on different days are all common. Agree it in "
        "writing by October or early November: if you cannot agree and need the court, the "
        "Federal Circuit and Family Court sets a filing cut-off for Christmas applications, usually "
        "in early-to-mid November."
    )
    + f"""
<h2 id="why-early">Why Christmas arrangements need to start early</h2>
<p>The {cite('family_law_act')} does not say which parent has the children on Christmas Day.
Instead, it asks parents — and, if they cannot agree, the court — to make arrangements that are
in the children's best interests. That flexibility is a good thing, but it means nothing is
settled until you settle it.</p>
<p>Leaving the conversation until December creates three problems. Families make bookings and
travel plans months in advance. Emotions run higher as the day gets closer. And the formal
options shrink: family dispute resolution services book out, and the court stops accepting
ordinary Christmas applications after its November cut-off. Parents who start in September or
October have time to talk, try a draft, and adjust it — parents who start on 20 December often
have only stress.</p>
<p>An early agreement also gives children certainty. Knowing where they will be on Christmas
morning, and that both parents are comfortable with it, removes one of the biggest worries
children carry through a family's first holidays apart.</p>
"""
    + inline_cta("Starting the Christmas conversation now? A short mediation session can turn a tense topic into a clear written plan.")
    + f"""
<h2 id="common-schedules">Common Christmas schedules that work</h2>
<p>There is no "right" schedule. The best one suits the children's ages, the distance between
homes, and each family's traditions. These are the arrangements Australian families most often
agree on.</p>
<figure class="tbl"><table><caption>Common Christmas arrangements for separated parents</caption>
  <thead><tr><th>Arrangement</th><th>How it works</th><th>Works well when</th><th>Watch out for</th></tr></thead>
  <tbody>
    <tr><td>Alternating years</td><td>One parent has Christmas Eve and Day in even years, the other in odd years</td><td>Homes are far apart or families travel</td><td>A long gap for the parent who misses out; plan a second celebration</td></tr>
    <tr><td>Split day</td><td>Christmas Eve to midday Christmas Day with one parent, midday to Boxing Day with the other</td><td>Homes are close and children are young</td><td>Rushed handovers; travel time cutting into the day</td></tr>
    <tr><td>Eve / Day split</td><td>One parent has Christmas Eve, the other has Christmas Day, swapping each year</td><td>Each family has a different tradition</td><td>Fairness depends on the swap actually happening each year</td></tr>
    <tr><td>Two Christmases</td><td>Each household celebrates on a different day (e.g. 25th and 27th)</td><td>Children enjoy two celebrations; conflict is low</td><td>Needs both parents to treat both days as real</td></tr>
    <tr><td>Shared celebration</td><td>Both parents attend part of the day together</td><td>Relationship is cooperative and safe</td><td>Not suitable where there is conflict or family violence</td></tr>
  </tbody>
</table></figure>
<p class="source-note">Arrangements are illustrative. Any arrangement can be recorded in a
<a href="/parenting-plans-guide/">parenting plan</a> or made into
<a href="/consent-orders-explained/">consent orders</a>.</p>
<p>Whichever model you choose, write down the exact times, the handover location, who drives,
and how phone or video calls with the other parent will work on the day. Vague plans
("we'll sort out the afternoon") are where most December disputes start.</p>
"""
    + inline_cta("Not sure which Christmas schedule suits your children's ages? Our mediators can help you weigh the options together.")
    + """
<h2 id="summer-holidays">Sharing the summer school holidays</h2>
<p>Christmas sits inside the longest school break of the year — around six weeks in most states,
and dates differ between states and between government and private schools. A good holiday plan
covers the whole period, not just 25 December.</p>
<ul>
  <li><strong>Halves or blocks:</strong> each parent has an equal block (often two or three weeks), with
  the order swapping each year.</li>
  <li><strong>Week-about:</strong> the children alternate weekly through the break — common for older
  children used to a 50/50 schedule.</li>
  <li><strong>Regular schedule plus a block:</strong> the usual term-time pattern continues, with each
  parent also getting one uninterrupted holiday week.</li>
  <li><strong>New Year's Eve:</strong> agree it separately if it matters to either family — it is a
  frequent flashpoint.</li>
</ul>
<p>For very young children, long stretches away from their main carer can be hard. Shorter
blocks with more frequent contact usually suit toddlers better, increasing as they grow. A
schedule that is right for a two-year-old should be revisited by the time they start school.</p>
"""
    + inline_cta("Want a holiday plan that covers the whole summer, not just Christmas Day? Book a free consultation.")
    + f"""
<h2 id="existing-orders">If you already have parenting orders or a plan</h2>
<p>If you have <a href="/consent-orders-explained/">consent orders</a> or court orders, read
the holiday clauses carefully — many orders already say who has Christmas in which years, and
those orders are binding. Deliberately not following them without a reasonable excuse can be a
contravention.</p>
<p>That does not mean you cannot do something different. Parents can usually agree on a one-off
change for a particular Christmas. Put it in writing — a signed and dated note or a clear
email or text exchange — so there is no confusion later about what was agreed. Depending on
how your orders are worded, a later written <a href="/parenting-plans-guide/">parenting
plan</a> may change some arrangements; get advice on your specific orders.</p>
<p>If you only have an informal arrangement or an older parenting plan, now is a good time to
update it. Plans that were written when children were babies often do not reflect what
teenagers want, new partners, or a parent who has moved.</p>
"""
    + inline_cta("Orders not working for this Christmas? A mediated written agreement is the simplest way to vary the plan for the holidays.")
    + f"""
<h2 id="court-cutoff">The court's Christmas cut-off and urgent applications</h2>
<p>Each year the {cite('fcfcoa')} publishes a deadline for filing applications that need to be
heard before Christmas. It is usually in early-to-mid November, and applications filed after it
are generally only dealt with before the holidays if they are genuinely urgent. Check the court's
website for this year's date — and remember that most parenting applications also need a
<a href="/section-60i-certificate-guide/">section 60I certificate</a> from a family dispute
resolution practitioner before they can be filed, unless an exemption applies.</p>
<p>Even if you file in time, a court hearing about Christmas is expensive, stressful and
uncertain, and the outcome is decided by someone who has never met your children. Court has its
place — particularly where there is a risk to a child — but for most holiday disagreements it
is rarely the best place to start.</p>
"""
    + callout("Safety comes first",
              "If you or your children are at risk, mediation may not be appropriate and exemptions "
              "from family dispute resolution apply. In an emergency call 000. For confidential support "
              "call 1800RESPECT on 1800 737 732, and read our guide to "
              "<a href=\"/domestic-violence-and-family-law/\">domestic violence and family law</a>.")
    + inline_cta("Close to the court's November cut-off? Mediation can often be arranged within days and a 60I certificate issued if needed.")
    + f"""
<h2 id="travel">Interstate and overseas travel over the holidays</h2>
<p>Summer is when many families travel to see relatives interstate or overseas. Interstate
trips mainly need cooperation and clear dates. Overseas travel is more serious: under the
{cite('family_law_act')}, taking a child out of Australia without the other parent's written
consent or a court order can be a criminal offence where parenting orders are in place or
proceedings are underway.</p>
<p>Before booking, agree in writing on:</p>
<ul>
  <li>the destination, dates and full itinerary, including accommodation;</li>
  <li>flight details and how the children will contact the other parent while away;</li>
  <li>passport arrangements — both parents usually need to consent to a child's passport application;</li>
  <li>how missed time will be made up, if the trip overlaps the other parent's holiday time.</li>
</ul>
<p>See our guide to <a href="/travel-overseas-after-a-separation/">travelling overseas after a
separation</a> for more detail. If a trip is a sticking point, mediation lets the travelling
parent offer reassurances — such as itineraries and return-flight confirmation — that make
agreement easier.</p>
"""
    + inline_cta("Planning an overseas holiday with the children? Agree the travel terms in mediation before you book.")
    + f"""
<h2 id="mediation">Agreeing a holiday plan through mediation</h2>
<p>Family mediation is designed for exactly this kind of decision: practical, time-sensitive and
emotional. An accredited family dispute resolution practitioner helps both parents focus on the
children, work through options, and record what is agreed. The
{cite('ag_fdr')} explains how family dispute resolution works and why it is expected before most
parenting applications.</p>
<p>Holiday mediation is often quicker than people expect — many families resolve Christmas and
summer arrangements in a single session, sometimes online, sometimes with
<a href="/shuttle-mediation-guide/">shuttle mediation</a> so parents do not have to sit in the
same room. The agreement can be written up as a parenting plan, or turned into consent orders
if you want it enforceable.</p>
<p>Low-cost options also exist through Family Relationship Centres — see
{cite('frc')} — although demand rises sharply before Christmas, so book early. Our guide to
<a href="/how-much-does-mediation-cost/">how much mediation costs</a> compares private and
subsidised options.</p>
"""
    + inline_cta("Our accredited family mediators can usually meet before the holiday rush. Book a free initial consultation.")
    + """
<h2 id="children-first">Keeping the day about the children</h2>
<p>However the time is divided, children remember how Christmas felt more than how many hours
they spent in each house. A few simple habits make a big difference:</p>
<ul>
  <li>Tell children the plan early and present it as something both parents agreed on.</li>
  <li>Keep handovers short, punctual and friendly — never use them to raise disputes.</li>
  <li>Let children take a favourite present between homes, and encourage a call to the other parent.</li>
  <li>Agree on big gifts in advance so presents do not become a competition.</li>
  <li>Look after yourself on the days the children are away — plan time with friends or family.</li>
</ul>
<p>If this is your family's first Christmas apart, expect it to feel strange, for adults and
children alike. The goal is not a perfect day; it is a calm one that both households can repeat
next year.</p>
"""
    + inline_cta("Want this Christmas to be the calm one? Talk to our family mediators about a holiday plan that works for everyone."),
    [
        ("Who gets the children at Christmas after separation in Australia?",
         "There is no automatic rule. Parents can agree any arrangement that is in the children's best "
         "interests, such as alternating years or splitting the day. If there are parenting orders, they "
         "must be followed unless both parents agree in writing to a change."),
        ("What is the cut-off date for Christmas applications to the Family Court?",
         "The Federal Circuit and Family Court of Australia sets a deadline each year, usually in early-to-mid "
         "November. Applications filed after it are generally only heard before Christmas if they are urgent. "
         "Check the court's website for the current year's date."),
        ("Can we change our parenting orders just for Christmas?",
         "Usually, yes — parents can agree to a one-off change. Record it in writing, signed and dated or in a "
         "clear message exchange. If the change should be permanent, consider a new parenting plan or "
         "consent orders."),
        ("Can I take my child overseas for Christmas without the other parent's consent?",
         "Generally no. Where parenting orders exist or proceedings are underway, taking a child overseas "
         "without written consent or a court order can be a criminal offence under the Family Law Act. Agree "
         "travel details in writing first."),
        ("How quickly can we mediate Christmas arrangements?",
         "Private mediation can often be arranged within days, and many families resolve holiday arrangements "
         "in one session. Subsidised services book out before Christmas, so start in October if you can."),
        ("Is it fair to split Christmas Day in half?",
         "It can work well when homes are close and children are young, but travel and rushed handovers can "
         "spoil the day. Alternating years or celebrating on two different days often suits families who live "
         "further apart."),
    ],
    related=[
        ("parenting-plans-guide",          "Parenting Plans in Australia"),
        ("co-parenting-mediation",         "Co-Parenting Mediation"),
        ("child-custody-mediation",        "Child Custody Mediation"),
        ("section-60i-certificate-guide",  "Section 60I Certificate Guide"),
        ("best-apps-for-separated-parents","Best Apps for Separated Parents"),
        ("consent-orders-explained",       "Consent Orders Explained"),
    ],
    read_min=9,
)


# ── POST 2: HOW TO CHANGE PARENTING ORDERS ───────────────────────────────────

post(
    "how-to-change-parenting-orders",
    "How to Change Parenting Orders in Australia",
    "How to vary parenting orders in Australia: changing by agreement, the significant "
    "change test, 60I certificates, costs, timeframes and mediation.",
    "Parenting &amp; children",
    "How to change parenting orders in Australia: <em>agreement first, court only when you must</em>",
    ("Parenting orders are made for children as they are at one point in time. Children grow, "
     "parents move, jobs change, and an arrangement that worked for a four-year-old may not work "
     "for a fourteen-year-old. This guide explains the ways final parenting orders can be changed "
     "in Australia, the legal test the court applies, and why an agreed variation is almost always "
     "the faster, calmer path."),
    [
        ("can-orders-change",  "Can parenting orders be changed?"),
        ("by-agreement",       "Changing orders by agreement"),
        ("change-test",        "The significant change of circumstances test"),
        ("valid-reasons",      "Reasons that commonly justify a change"),
        ("process",            "The process step by step"),
        ("costs-timeframes",   "Costs and timeframes compared"),
        ("meanwhile",          "Following orders while you seek a change"),
        ("mediation-role",     "How mediation helps vary parenting orders"),
    ],
    key_takeaway(
        "Parenting orders in Australia can be changed in two ways: both parents agree and file "
        "consent orders (or, depending on the orders, make a written parenting plan), or one parent "
        "applies to the court. Since May 2024 the Family Law Act requires the court to be satisfied "
        "there has been a significant change of circumstances and that reconsidering the orders is in "
        "the child's best interests before it will reopen final parenting orders. Agreement through "
        "mediation is usually quicker and far less expensive."
    )
    + f"""
<h2 id="can-orders-change">Can parenting orders be changed?</h2>
<p>Yes. Parenting orders are not set in stone, but they are binding until they are changed or
the child turns 18. The law balances two goals: children need stability and should not be
dragged through repeated litigation, yet orders must be able to adapt when a family's life
genuinely changes.</p>
<p>That balance is why there are two very different paths. If both parents agree on new
arrangements, the change can be made with relatively little formality. If one parent wants a
change and the other does not, the parent seeking the change has to persuade the court that it
should reopen the existing orders at all — before it even considers what the new arrangements
should be.</p>
<p>It is worth separating three things people often confuse: <strong>interim orders</strong>
(temporary orders made during proceedings, which can be revisited more readily),
<strong>final orders</strong> (the focus of this guide), and <strong>parenting plans</strong>
(written agreements that are not enforceable like orders — see our
<a href="/parenting-plans-guide/">parenting plans guide</a>).</p>
"""
    + inline_cta("Orders no longer fit your children's lives? A free consultation can help you see whether an agreed variation is possible.")
    + f"""
<h2 id="by-agreement">Changing orders by agreement</h2>
<p>When both parents agree, the cleanest option is to file an Application for Consent Orders
with the {cite('fcfcoa')} (or the Family Court of Western Australia in WA) setting out the new
arrangements. A registrar checks that the proposed orders are in the children's best interests
and, if satisfied, makes them without anyone attending court. Our guide to
<a href="/consent-orders-explained/">consent orders</a> walks through the paperwork.</p>
<p>Some parents instead record the change in a signed and dated parenting plan. Depending on
how the existing orders are worded, a later parenting plan may vary some arrangements — but a
plan cannot be enforced like an order, so if the change is significant or trust is low, new
consent orders are the safer choice.</p>
<p>No section 60I certificate is needed to file consent orders. Many parents still use a
mediator to reach the agreement, because negotiating directly with a former partner about
children is hard, and a neutral process helps both sides land on terms they can live with.</p>
"""
    + inline_cta("Close to agreeing but need it in writing? Our mediators can help you settle the terms ready for consent orders.")
    + f"""
<h2 id="change-test">The significant change of circumstances test</h2>
<p>Where parents do not agree, the court will not simply rehear the case because one parent is
unhappy. For many years this principle came from the 1979 case <em>Rice v Asplund</em>. Since
6 May 2024, it has been written into the {cite('family_law_act')} itself (section 65DAAA).
Before reconsidering final parenting orders, the court must:</p>
<ol>
  <li>consider whether there has been a <strong>significant change of circumstances</strong> since
  the orders were made; and</li>
  <li>be satisfied that, taking into account all the circumstances, it is in the
  <strong>child's best interests</strong> for the orders to be reconsidered.</li>
</ol>
<p>In weighing the second question, the court can consider matters such as the reasons for the
original orders, the likely impact of reopening them on the child and the family, and the
benefits and risks of a change. Only if it decides to reopen the orders does it move on to the
usual best-interests assessment of what the new arrangements should be.</p>
<p>The test is deliberately a hurdle. Applications that are, in substance, a second attempt at
the same argument tend to fail early — at real cost to both parents.</p>
"""
    + inline_cta("Unsure whether your situation is a 'significant change'? Talk it through confidentially before you commit to court.")
    + """
<h2 id="valid-reasons">Reasons that commonly justify a change</h2>
<p>Every case turns on its facts, but these are the kinds of changes that often lead parents —
and sometimes the court — to revisit orders:</p>
<ul>
  <li><strong>Relocation</strong> of a parent, making the existing schedule impractical (see our
  <a href="/relocation-with-children-after-separation/">relocation guide</a>).</li>
  <li><strong>A child's developmental stage</strong> — orders made for a toddler rarely suit a teenager.</li>
  <li><strong>A child's consistent, mature views</strong> about where they live or how often they
  see each parent (see <a href="/what-age-can-a-child-choose-which-parent-to-live-with/">what age
  a child can choose</a>).</li>
  <li><strong>Safety concerns</strong>, including family violence, substance misuse or neglect.</li>
  <li><strong>Changes in work or health</strong> that affect a parent's capacity to care for the child.</li>
  <li><strong>Orders that simply are not working</strong> — persistent non-compliance, or a schedule
  that creates constant conflict at handovers.</li>
</ul>
<p>Things that usually are not enough on their own: a new partner, minor changes to work hours,
or a parent's dissatisfaction with the original outcome.</p>
"""
    + inline_cta("Has your child outgrown their orders? Mediation lets you build a schedule that fits who they are now.")
    + f"""
<h2 id="process">The process step by step</h2>
<p>If you cannot agree, the usual path to varying parenting orders looks like this:</p>
<ol>
  <li><strong>Read your current orders</strong> and identify exactly which clauses no longer work.</li>
  <li><strong>Propose the change in writing</strong>, calmly and with reasons focused on the children.</li>
  <li><strong>Attend family dispute resolution.</strong> Unless an exemption applies (for example,
  family violence or urgency), you need a <a href="/section-60i-certificate-guide/">section 60I
  certificate</a> before filing a parenting application. The {cite('ag_fdr')} explains the
  requirement.</li>
  <li><strong>If agreement is reached</strong>, file consent orders.</li>
  <li><strong>If not</strong>, file an Initiating Application with supporting affidavit evidence
  explaining the significant change of circumstances and why a change is in the child's best
  interests.</li>
  <li><strong>Court process</strong> — case management hearings, possibly a family report, further
  dispute resolution, and if still unresolved, a final hearing. See our
  <a href="/family-court-process/">family court process</a> guide.</li>
</ol>
"""
    + callout("Where safety is at risk",
              "If a child is at immediate risk, call 000. Urgent applications can be made without first "
              "attending mediation, and family violence is an exemption from the 60I requirement. For "
              "confidential support call 1800RESPECT on 1800 737 732, and see "
              "<a href=\"/domestic-violence-and-family-law/\">domestic violence and family law</a>.")
    + inline_cta("Need a section 60I certificate or a structured negotiation first? Our accredited FDR practitioners can help.")
    + f"""
<h2 id="costs-timeframes">Costs and timeframes compared</h2>
<p>The path you take has a dramatic effect on both cost and time. The figures below are general
estimates; filing fees change each financial year, so check the current
{cite('fcfcoa_fees')} before you file.</p>
<figure class="tbl"><table><caption>Ways to change parenting orders — typical cost and time</caption>
  <thead><tr><th>Route</th><th>Typical timeframe</th><th>Indicative cost</th><th>Enforceable?</th></tr></thead>
  <tbody>
    <tr><td>Written parenting plan (agreed)</td><td>Days to weeks</td><td>Minimal, plus any mediation fees</td><td>No — not enforceable like an order</td></tr>
    <tr><td>Mediation + consent orders</td><td>Around 1–3 months</td><td>Mediation fees plus a consent orders filing fee; legal drafting if used</td><td>Yes</td></tr>
    <tr><td>Contested application, settled before hearing</td><td>6–12+ months</td><td>Commonly $10,000–$40,000+ per parent in legal costs</td><td>Yes</td></tr>
    <tr><td>Contested application to final hearing</td><td>12–24+ months</td><td>Commonly $40,000–$100,000+ per parent</td><td>Yes</td></tr>
  </tbody>
</table></figure>
<p class="source-note">Indicative ranges only, based on common market estimates; your costs depend on
complexity, location and representation. See our guide to the
<a href="/cost-of-divorce-in-australia/">cost of family law matters</a>.</p>
"""
    + inline_cta("A mediated variation typically costs a fraction of a contested application. Book a free consultation to compare your options.")
    + """
<h2 id="meanwhile">Following orders while you seek a change</h2>
<p>Until orders are changed, they must be followed. Stopping handovers or keeping a child
because you believe the orders are wrong can amount to a contravention, which the court takes
seriously and which can count against you when it later considers a variation.</p>
<p>There are limited exceptions — for example, where a parent has a reasonable excuse, such as
genuinely needing to protect a child's health or safety. If you are in that situation, get legal
advice immediately and take steps to bring the matter before the court or an appropriate
authority.</p>
<p>Keep a factual record of what is and is not working — dates, missed handovers, school
reports, communications. A co-parenting app can help (see our guide to the
<a href="/best-apps-for-separated-parents/">best apps for separated parents</a>). Calm,
documented evidence is far more persuasive, in mediation or in court, than a long list of
grievances.</p>
"""
    + inline_cta("Orders being breached or impossible to follow? Mediation is often the fastest way to agree a workable change.")
    + f"""
<h2 id="mediation-role">How mediation helps vary parenting orders</h2>
<p>Most parenting orders that need changing can be changed by agreement, and mediation is how
most agreements get made. A skilled family mediator helps both parents focus on what the
children need now, test ideas without commitment, and reach terms specific enough to become
consent orders. <a href="/child-custody-mediation/">Child custody mediation</a> and
<a href="/co-parenting-mediation/">co-parenting mediation</a> are both designed for this.</p>
<p>Family lawyers and mediators work together well here: lawyers advise each parent on their
position and draft the final orders; mediators provide the structured, neutral space to agree
them. Research from the {cite('aifs')} has consistently found that most separated parents sort
out arrangements without going to court, and that outcomes reached cooperatively tend to be
more durable.</p>
<p>Court has its place, particularly where there are safety risks or one parent will not engage.
But for the large majority of families whose orders simply need to catch up with their lives,
an agreed variation is the smarter first step.</p>
"""
    + inline_cta("Ready to update your parenting orders without a court battle? Book a free initial consultation with our family mediators."),
    [
        ("Can parenting orders be changed without going to court?",
         "Yes. If both parents agree, you can file an Application for Consent Orders, which a registrar "
         "considers on the papers without anyone attending court. Depending on how your orders are worded, "
         "a later written parenting plan may also vary some arrangements, but it is not enforceable like an order."),
        ("What counts as a significant change of circumstances?",
         "It depends on the facts, but examples include a parent relocating, a child's needs changing as they "
         "grow, a mature child's consistent views, safety concerns, or orders proving unworkable. A new partner "
         "or dissatisfaction with the original result is usually not enough."),
        ("What is section 65DAAA of the Family Law Act?",
         "Introduced from 6 May 2024, section 65DAAA requires the court, before reconsidering final parenting "
         "orders, to consider whether there has been a significant change of circumstances and be satisfied "
         "that reconsideration is in the child's best interests. It codifies the earlier Rice v Asplund rule."),
        ("Do I need a section 60I certificate to change parenting orders?",
         "You need one before filing a contested application to vary parenting orders, unless an exemption "
         "applies, such as family violence or urgency. You do not need one to file consent orders."),
        ("How long does it take to change parenting orders?",
         "An agreed variation through mediation and consent orders often takes one to three months. A contested "
         "application can take a year or more, particularly if it proceeds to a final hearing."),
        ("Can I stop following parenting orders if they are not working?",
         "No. Orders must be followed until they are changed, unless you have a reasonable excuse such as "
         "protecting a child's safety. Breaching orders can be a contravention and may count against you. "
         "Seek advice and pursue a variation instead."),
    ],
    related=[
        ("consent-orders-explained",                  "Consent Orders Explained"),
        ("parenting-plans-guide",                     "Parenting Plans in Australia"),
        ("section-60i-certificate-guide",             "Section 60I Certificate Guide"),
        ("relocation-with-children-after-separation", "Relocating with Children After Separation"),
        ("child-custody-mediation",                   "Child Custody Mediation"),
        ("changes-to-family-law-act-2025",            "Changes to the Family Law Act"),
    ],
    read_min=10,
)
