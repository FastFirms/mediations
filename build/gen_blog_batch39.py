"""gen_blog_batch39.py: sole-parental-responsibility-australia, parenting-arrangements-for-babies-australia.
Facts checked against Family Law Act 1975 (Cth) as amended by the Family Law Amendment Act 2023
(in force 6 May 2024): ss 4 (major long-term issues), 60CC, 61C, 61D, 61DAA, 60I (Nov 2026)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, key_takeaway, inline_cta, callout
from authority_sources import cite

# ── POST 1: sole-parental-responsibility-australia ───────────────────────────

spr_body = (
  key_takeaway("Since 6 May 2024 there is no presumption of equal shared parental responsibility in "
               "Australia. A court can give one parent sole decision-making on major long-term issues "
               "(education, health, religion, name and big relocations) if that is in the child's best "
               "interests, most often where there is family violence, abuse or a parent who cannot "
               "co-operate. Sole responsibility is about decisions, not how much time a child spends with each parent.")
  + f"""
<h2 id="what-it-means">What sole parental responsibility means</h2>
<p>Parental responsibility is the legal power and duty to make decisions about a child. Under section 61C of the {cite('family_law_act')}, each parent of a child under 18 has parental responsibility, unless a court order says otherwise. That means that without orders, both parents can make decisions about their child.</p>
<p><strong>Sole parental responsibility</strong> is an order that gives one parent the power to make some or all <em>major long-term decisions</em> alone, without needing to consult or agree with the other parent. It is different from day-to-day care. The parent who has the child on a given day still decides what they eat, when they go to bed and who they play with.</p>
<p>People often say "sole custody" when they mean sole parental responsibility. Australian family law stopped using the word "custody" decades ago. Today the law separates two questions:</p>
<ul>
  <li><strong>Who decides?</strong> That is parental responsibility, which can be joint or sole, and can be split issue by issue.</li>
  <li><strong>Who does the child live with and spend time with?</strong> That is the care arrangement, dealt with separately in parenting orders or a parenting plan.</li>
</ul>
<p>A parent can have sole parental responsibility and the child can still spend substantial time with the other parent. Equally, parents can share decision-making while the child lives mostly with one of them.</p>
"""
  + inline_cta("Unsure whether joint or sole decision-making suits your family? Talk it through with a mediator.")
  + f"""
<h2 id="2024-changes">What changed in May 2024</h2>
<p>The Family Law Amendment Act 2023 took effect on 6 May 2024 and changed how courts approach parental responsibility. The main changes were:</p>
<ul>
  <li><strong>The presumption of equal shared parental responsibility was removed.</strong> Courts no longer start from the assumption that both parents should share major decisions.</li>
  <li><strong>The link between equal responsibility and equal time was removed.</strong> Courts are no longer required to consider equal time or "substantial and significant time" just because joint responsibility is ordered.</li>
  <li><strong>New joint decision-making rules.</strong> Section 61DAA now explains that where parents have joint decision-making, they must consult each other and make a genuine effort to reach a joint decision.</li>
  <li><strong>Simplified best interests factors.</strong> Section 60CC now lists a shorter set of considerations, with safety placed first.</li>
</ul>
<p>The practical effect is that every case is decided on its own facts. A parent seeking sole responsibility no longer has to "rebut" a presumption, but they still have to show why it is in the child's best interests. Our guide to the <a href="/changes-to-family-law-act-2025/">changes to the Family Law Act</a> covers the reforms in more detail.</p>
"""
  + inline_cta("The law changed in 2024. Get up to date before you negotiate parenting arrangements.")
  + """
<h2 id="major-long-term-issues">Which decisions are covered</h2>
<p>Section 4 of the Family Law Act defines <strong>major long-term issues</strong>. These are the decisions sole parental responsibility can cover. Orders can give one parent sole responsibility for all of them, or for only one or two, with the rest shared.</p>
<figure class="tbl"><table><caption>Major long-term issues vs day-to-day decisions</caption>
<thead><tr><th>Decision</th><th>Category</th><th>Who decides under sole responsibility?</th></tr></thead>
<tbody>
<tr><td>Which school the child attends</td><td>Major long-term (education)</td><td>Parent with sole responsibility</td></tr>
<tr><td>Non-urgent medical treatment, surgery, mental health care</td><td>Major long-term (health)</td><td>Parent with sole responsibility</td></tr>
<tr><td>Religious and cultural upbringing</td><td>Major long-term</td><td>Parent with sole responsibility</td></tr>
<tr><td>Changing the child's name</td><td>Major long-term</td><td>Parent with sole responsibility</td></tr>
<tr><td>Moving that makes it significantly harder to see the other parent</td><td>Major long-term</td><td>Parent with sole responsibility (subject to existing time orders)</td></tr>
<tr><td>Meals, bedtime, homework, weekend activities</td><td>Day-to-day</td><td>Whichever parent has the child at the time</td></tr>
<tr><td>Emergency medical treatment</td><td>Urgent</td><td>Whichever parent is present</td></tr>
</tbody></table></figure>
<p class="source-note">Based on s 4 and Part VII of the Family Law Act 1975 (Cth). General information only, not legal advice.</p>
<p>A common middle ground is a <strong>split order</strong>: for example, joint responsibility for education and religion, but sole responsibility for health decisions because the parents strongly disagree about a child's treatment.</p>
"""
  + inline_cta("Split decision-making can resolve deadlock without going to court. Book a free consultation.")
  + f"""
<h2 id="when-courts-order-it">When courts order sole parental responsibility</h2>
<p>The court's paramount consideration is the best interests of the child. Under section 60CC, the court considers the child's safety and that of their carers, the child's views, their developmental, emotional and cultural needs, each parent's capacity to meet those needs, the benefit of relationships with both parents where safe, and anything else relevant.</p>
<p>Sole parental responsibility is most often ordered where:</p>
<ul>
  <li><strong>There is family violence or abuse.</strong> Requiring a victim to consult and agree with a perpetrator can expose them and the child to ongoing harm. Courts take this very seriously.</li>
  <li><strong>The parents cannot communicate at all.</strong> Where every decision ends in deadlock, joint responsibility can leave a child without timely schooling or treatment.</li>
  <li><strong>One parent is absent or uninvolved.</strong> A parent who has had no contact for years, or who cannot be located, may be removed from the decision-making role.</li>
  <li><strong>Serious drug, alcohol or mental health concerns</strong> affect a parent's capacity to make sound decisions.</li>
  <li><strong>One parent has repeatedly obstructed decisions</strong>, for example refusing to sign school enrolment or passport forms to gain leverage.</li>
</ul>
<p>A parent's disagreement with the other parent's choices is not, on its own, enough. Courts expect separated parents to tolerate some difference in parenting styles. If you are dealing with violence, our <a href="/domestic-violence-and-family-law/">guide to domestic violence and family law</a> explains your options and the safety supports available.</p>
"""
  + inline_cta("Worried about safety? Our intake process screens for risk before any joint session.")
  + """
<h2 id="how-to-apply">How to get sole parental responsibility</h2>
<p>There are three main routes, from least to most costly:</p>
<ol>
  <li><strong>Agree it in a parenting plan.</strong> A signed and dated parenting plan can record that one parent will make certain decisions. It is not legally enforceable, but courts consider it.</li>
  <li><strong>Consent orders.</strong> If both parents agree, you can file an application for consent orders with the Federal Circuit and Family Court. The court reviews the terms and, if satisfied they are in the child's best interests, makes binding orders without a hearing.</li>
  <li><strong>Contested court application.</strong> If you cannot agree, you can apply to the court. You will usually need a section 60I certificate from a family dispute resolution practitioner first, unless an exception such as family violence or urgency applies.</li>
</ol>
<p>Evidence matters in a contested case. Useful material often includes school and medical records, police reports or intervention orders, written communication showing refusal to co-operate, and reports from family consultants or independent children's lawyers.</p>
<p>See our guides on <a href="/consent-orders-explained/">consent orders</a> and the <a href="/section-60i-certificate-guide/">section 60I certificate</a> for the next steps.</p>
"""
  + inline_cta("Most parents settle decision-making in mediation. Start with a free, confidential consultation.")
  + """
<h2 id="cost-and-timeframe">Cost and timeframe compared</h2>
<figure class="tbl"><table><caption>Routes to sole parental responsibility: typical cost and time (2026)</caption>
<thead><tr><th>Route</th><th>Typical cost (per parent)</th><th>Typical timeframe</th><th>Binding?</th></tr></thead>
<tbody>
<tr><td>Parenting plan via mediation</td><td>$1,500 – $4,000</td><td>2 – 6 weeks</td><td>No (but persuasive)</td></tr>
<tr><td>Consent orders after mediation</td><td>$2,500 – $7,000 incl. filing fee</td><td>1 – 3 months</td><td>Yes</td></tr>
<tr><td>Contested parenting proceedings</td><td>$30,000 – $150,000+</td><td>12 – 36 months</td><td>Yes</td></tr>
</tbody></table></figure>
<p class="source-note">Indicative ranges only. Actual costs depend on complexity, legal representation and whether expert reports are needed.</p>
<p>The difference is stark. Even where one parent has strong grounds, reaching agreement on decision-making through mediation, then formalising it as consent orders, is usually far faster and cheaper than a contested hearing.</p>
"""
  + inline_cta("A fraction of the cost of court. See how mediation can resolve parental responsibility.")
  + f"""
<h2 id="joint-decision-making">Making joint decision-making work instead</h2>
<p>In many families, the real problem is not that one parent is unfit, but that the parents have no system for making decisions. Before seeking sole responsibility, consider whether a clearer process would solve the conflict. Practical tools parents agree in mediation include:</p>
<ul>
  <li><strong>A written consultation protocol.</strong> For example, the proposing parent emails details, the other replies within 7 days, and silence counts as consent.</li>
  <li><strong>Tie-break rules.</strong> One parent has the final say on health, the other on education, after genuine consultation.</li>
  <li><strong>Neutral third parties.</strong> Agreeing to follow the child's GP or school principal's recommendation if you cannot agree.</li>
  <li><strong>A return-to-mediation clause</strong> for disagreements before anyone files in court.</li>
  <li><strong>A co-parenting app</strong> that records every proposal and reply.</li>
</ul>
<p>Section 61DAA requires parents with joint decision-making to consult and make a genuine effort to agree. A structured protocol shows you are meeting that obligation. The {cite('aifs')} has published research on how the 2024 reforms are working in practice, and {cite('frc')} lists free and low-cost services that can help.</p>
"""
  + inline_cta("Build a decision-making protocol that actually works. Book a mediation consultation.")
  + f"""
<h2 id="mediation">How mediation resolves parental responsibility</h2>
<p>Family dispute resolution is required before most parenting applications, and it is where most decision-making disputes are resolved. A mediator can help you:</p>
<ul>
  <li>separate the question of <em>who decides</em> from <em>how much time</em> each parent has;</li>
  <li>identify which decisions are actually causing conflict, so you are not fighting over everything;</li>
  <li>agree a split arrangement or protocol that both parents can live with;</li>
  <li>use shuttle mediation, where you are in separate rooms, if there are safety concerns; and</li>
  <li>turn your agreement into a parenting plan or draft consent orders.</li>
</ul>
<p>The {cite('fcfcoa_fdr')} page explains the court's expectations around dispute resolution. If you are experiencing family and domestic violence, confidential support is available through 1800RESPECT on 1800 737 732. If you are in immediate danger, call 000.</p>
"""
  + inline_cta("Ready to settle who decides? Book a free, confidential consultation today.")
)

spr_qa = [
 ("Is there still equal shared parental responsibility in Australia?",
  "Not as a presumption. Since 6 May 2024 courts no longer start from the assumption that parents should share major decisions. Joint decision-making is still common, but each case is decided on the child's best interests."),
 ("Does sole parental responsibility mean the other parent loses contact?",
  "No. Sole parental responsibility only covers major long-term decisions. The child can still spend regular, even equal, time with the other parent under a separate care arrangement."),
 ("Can I get sole parental responsibility without going to court?",
  "Yes, if the other parent agrees. You can record it in a parenting plan, or formalise it as consent orders filed with the court without a hearing. Mediation is the usual way parents reach that agreement."),
 ("What decisions can the other parent still make?",
  "The parent caring for the child at the time can still make day-to-day decisions such as meals, bedtime and activities, and can consent to emergency medical treatment."),
 ("Can sole parental responsibility orders be changed?",
  "Yes, but you generally need to show a significant change in circumstances since the orders were made. Parents can also agree to new consent orders at any time."),
]

post(
  "sole-parental-responsibility-australia",
  "Sole Parental Responsibility in Australia (2026)",
  "What sole parental responsibility means after the 2024 law changes, when courts order it, which decisions it covers, costs and how to agree it in mediation.",
  "Parenting",
  "Sole parental responsibility in Australia: <em>who decides</em>",
  "Since the 2024 reforms there is no presumption that separated parents share major decisions. Here is what sole parental responsibility covers, when courts order it, and how most parents settle it without a hearing.",
  [("what-it-means", "What sole parental responsibility means"),
   ("2024-changes", "What changed in May 2024"),
   ("major-long-term-issues", "Which decisions are covered"),
   ("when-courts-order-it", "When courts order it"),
   ("how-to-apply", "How to get sole parental responsibility"),
   ("cost-and-timeframe", "Cost and timeframe compared"),
   ("joint-decision-making", "Making joint decision-making work"),
   ("mediation", "How mediation resolves it")],
  spr_body, spr_qa,
  [("changes-to-family-law-act-2025", "Changes to the Family Law Act"),
   ("child-custody-mediation", "Child Custody Mediation"),
   ("domestic-violence-and-family-law", "Domestic Violence and Family Law"),
   ("consent-orders-explained", "Consent Orders Explained"),
   ("parenting-plans-guide", "Parenting Plans Guide"),
   ("parallel-parenting-australia", "Parallel Parenting in Australia")],
  read_min=9,
)
print("sole-parental-responsibility-australia built")

# ── POST 2: parenting-arrangements-for-babies-australia ──────────────────────

baby_body = (
  key_takeaway("There is no fixed legal schedule for babies and toddlers after separation. Courts and "
               "mediators look at the child's age, attachment, feeding and each parent's involvement. "
               "Most workable plans for under-threes start with frequent, shorter time with each parent, "
               "add overnights gradually, and build in review points as the child grows.")
  + f"""
<h2 id="why-babies-are-different">Why babies and toddlers need a different plan</h2>
<p>Separating when you have a baby or toddler raises questions that older children's arrangements do not. A six-month-old cannot tell you how they feel about a handover, cannot hold a parent in mind for a week at a time, and may still be breastfeeding. A schedule that works well for a nine-year-old, such as week about, can be very stressful for an infant.</p>
<p>The {cite('family_law_act')} does not set out an age-based timetable. Instead, section 60CC asks what is in the child's best interests, including their <strong>developmental, psychological and emotional needs</strong> and the benefit of a relationship with both parents where it is safe. For very young children, that usually means two things are true at once:</p>
<ul>
  <li>Babies need <strong>predictability and a secure base</strong>: consistent routines, sleep and feeding, and a primary caregiver they can rely on.</li>
  <li>Babies also benefit from <strong>building a strong bond with both parents</strong>, which happens through frequent, regular contact rather than long gaps.</li>
</ul>
<p>Good parenting arrangements for babies balance those needs, and change as the child develops.</p>
"""
  + inline_cta("Separating with a baby? A mediator can help you build a plan around your child's needs.")
  + f"""
<h2 id="schedules-by-age">Common schedules by age</h2>
<p>Every family is different, but the following patterns are commonly used as starting points in Australian parenting plans and mediation. They assume both parents are safe, involved and live reasonably close to each other.</p>
<figure class="tbl"><table><caption>Typical starting arrangements for young children (non-primary parent's time)</caption>
<thead><tr><th>Age</th><th>Common pattern</th><th>Overnights</th><th>Key considerations</th></tr></thead>
<tbody>
<tr><td>0 – 6 months</td><td>2 – 4 short visits a week (2 – 3 hours)</td><td>Usually none, or very limited</td><td>Feeding, sleep routine, attachment to primary carer</td></tr>
<tr><td>6 – 12 months</td><td>3 – 4 visits a week, some longer daytime blocks</td><td>Sometimes 1 a week if the parent has been hands-on</td><td>Separation anxiety peaks; consistent handovers matter</td></tr>
<tr><td>12 – 24 months</td><td>Frequent contact, including full days</td><td>1 – 2 a week, not consecutive at first</td><td>Language and routines developing; avoid long gaps</td></tr>
<tr><td>2 – 3 years</td><td>Regular days plus weekend time</td><td>2 – 3 a week; may build to 2 consecutive</td><td>Toddler can tolerate longer separations from each parent</td></tr>
<tr><td>3 – 5 years</td><td>Progressing towards school-age patterns</td><td>Up to shared care (e.g. 5-2-2-5) where suitable</td><td>Kindy and preschool timetables; prepare for school</td></tr>
</tbody></table></figure>
<p class="source-note">Indicative patterns drawn from child development guidance and common practice. Not a legal rule; every child's needs differ. General information only, not legal advice.</p>
<p>The {cite('aifs')} has published research on shared care and overnight arrangements for young children, which highlights that the quality of parenting and the level of conflict between parents matter as much as the schedule itself.</p>
"""
  + inline_cta("Want a schedule that fits your baby's age and routine? Book a free consultation.")
  + """
<h2 id="overnights">Overnight stays: when and how</h2>
<p>Overnights are the most contested issue in parenting arrangements for babies. There is no age at which overnights automatically become appropriate. Factors that make early overnights more workable include:</p>
<ul>
  <li>The parent has been closely involved in night-time care, feeding and settling before separation.</li>
  <li>The baby already knows the home and the parent well.</li>
  <li>Both parents follow a similar sleep and feeding routine.</li>
  <li>Handovers are calm and the parents can share information about the night.</li>
  <li>The child is not unwell, teething badly or going through a big transition such as starting childcare.</li>
</ul>
<p>Where these conditions are not yet in place, many parents agree to a <strong>staged plan</strong>: daytime contact for a set period, then one overnight a week, then more, with review dates written into the plan. Staging protects the baby's routine and gives the other parent a clear, guaranteed path to more time, which often reduces conflict on both sides.</p>
"""
  + inline_cta("A staged plan gives both parents certainty. A mediator can help you agree the steps.")
  + """
<h2 id="breastfeeding">Breastfeeding and parenting arrangements</h2>
<p>Breastfeeding is a legitimate factor in planning, but it is not a veto on the other parent's time. Courts and mediators generally expect parents to work around feeding rather than use it to limit contact. Practical solutions include:</p>
<ul>
  <li>scheduling visits between feeds, or at the breastfeeding parent's home in the early months;</li>
  <li>using expressed milk for longer periods with the other parent;</li>
  <li>agreeing the feeding routine in writing so both homes are consistent; and</li>
  <li>setting a review date, for example when solids are introduced or around the first birthday.</li>
</ul>
<p>The aim is to support feeding <em>and</em> the baby's relationship with both parents. A plan that clearly addresses breastfeeding is far more likely to hold than one that ignores it.</p>
"""
  + inline_cta("Feeding and routines can be agreed calmly in mediation. Talk to us.")
  + """
<h2 id="handovers-and-communication">Handovers, routines and communication</h2>
<p>For very young children, how arrangements are carried out matters as much as the timetable. Babies are highly sensitive to tension between their parents. Things that help include:</p>
<ul>
  <li><strong>A shared baby diary or app</strong> recording sleep, feeds, nappies, medication and milestones, passed between homes.</li>
  <li><strong>Consistent routines</strong>, including bedtime rituals, comfort items and similar sleep arrangements in both homes.</li>
  <li><strong>Neutral or easy handovers</strong>, such as at childcare, so the baby does not witness conflict.</li>
  <li><strong>Duplicating essentials</strong> like a cot, car seat, pram and favourite toys so less needs to travel.</li>
  <li><strong>Agreed health decisions</strong> on vaccinations, GP and maternal and child health nurse visits.</li>
</ul>
<p>If face-to-face contact is tense, our guide to <a href="/parallel-parenting-australia/">parallel parenting</a> explains low-contact ways of sharing care.</p>
"""
  + inline_cta("Calm handovers start with a clear plan. Book a free, confidential consultation.")
  + f"""
<h2 id="review-points">Building in review points as your child grows</h2>
<p>A plan made for a four-month-old will not suit a four-year-old. The most durable parenting arrangements for babies include a built-in timetable for change, so neither parent has to fight for each step. Common review triggers include:</p>
<figure class="tbl"><table><caption>Common review points in a baby or toddler parenting plan</caption>
<thead><tr><th>Trigger</th><th>What to review</th></tr></thead>
<tbody>
<tr><td>Weaning or introducing solids</td><td>Length of visits, first or additional overnights</td></tr>
<tr><td>First birthday</td><td>Number of overnights, longer daytime blocks</td></tr>
<tr><td>Starting childcare</td><td>Handover location, which parent does drop-off and pick-up</td></tr>
<tr><td>Age 2 to 3</td><td>Consecutive overnights, holiday time</td></tr>
<tr><td>Starting kindergarten or preschool</td><td>Moving towards a school-age schedule</td></tr>
</tbody></table></figure>
<p>You can put these steps in a parenting plan or ask the court to make them part of consent orders. Our <a href="/parenting-plans-guide/">parenting plans guide</a> explains what to include. If arrangements need to change later, see <a href="/how-to-change-parenting-orders/">how to change parenting orders</a>. {cite('frc')} also lists parenting support services near you.</p>
"""
  + inline_cta("Plan for the next five years, not just the next five weeks. Talk to a mediator.")
  + f"""
<h2 id="mediation">How mediation helps parents of very young children</h2>
<p>Parents of babies are often exhausted, emotional and newly separated, which is exactly when conflict escalates. Court is slow, and a contested case can take longer than the baby's entire infancy. Mediation lets you agree a plan now, while your child is young, and adjust it as they grow.</p>
<p>In mediation we can help you:</p>
<ul>
  <li>build a schedule around your baby's actual feeding and sleep routine;</li>
  <li>agree a staged path to overnights with clear dates or milestones;</li>
  <li>set up a communication system so both homes stay consistent;</li>
  <li>use shuttle or online mediation if being in the same room is difficult; and</li>
  <li>turn your agreement into a parenting plan or consent orders.</li>
</ul>
<p>The {cite('ag_fdr')} explains the role of family dispute resolution before parenting applications. If you are experiencing family and domestic violence, confidential support is available through 1800RESPECT on 1800 737 732. If you are in immediate danger, call 000.</p>
"""
  + inline_cta("Give your baby a calm start. Book a free, confidential mediation consultation.")
)

baby_qa = [
 ("Can a baby have overnight stays with the other parent?",
  "Yes, there is no legal minimum age for overnights. Whether they are suitable depends on the baby's routine and attachment, feeding, and how involved the parent has been in night-time care. Many parents agree a staged plan that introduces overnights gradually."),
 ("Is 50/50 care suitable for a baby?",
  "Equal time with frequent long blocks, such as week about, is generally not recommended for babies. Shared care can work better with short, frequent periods with each parent and builds up as the child gets older."),
 ("Can breastfeeding stop the other parent seeing the baby?",
  "No. Breastfeeding is a factor in planning visits, but courts expect parents to work around it, for example by scheduling time between feeds or using expressed milk."),
 ("Do I need a court order for parenting arrangements for a baby?",
  "No. Many parents use a parenting plan agreed in mediation. If you want a legally enforceable arrangement, you can apply for consent orders without going to a hearing."),
 ("How often should a parenting plan for a toddler be reviewed?",
  "It is common to build review points into the plan, such as the first birthday, starting childcare and turning three, so arrangements can grow with the child without starting the negotiation from scratch."),
]

post(
  "parenting-arrangements-for-babies-australia",
  "Parenting Arrangements for Babies in Australia",
  "Separating with a baby or toddler? Common schedules by age, overnight stays, breastfeeding, handovers and how to agree a staged parenting plan without court.",
  "Parenting",
  "Parenting arrangements for babies: <em>a plan that grows</em>",
  "There is no fixed legal schedule for babies and toddlers after separation. This guide explains common arrangements by age, when overnights make sense, and how to build a plan that changes as your child grows.",
  [("why-babies-are-different", "Why babies need a different plan"),
   ("schedules-by-age", "Common schedules by age"),
   ("overnights", "Overnight stays: when and how"),
   ("breastfeeding", "Breastfeeding and parenting arrangements"),
   ("handovers-and-communication", "Handovers, routines and communication"),
   ("review-points", "Building in review points"),
   ("mediation", "How mediation helps")],
  baby_body, baby_qa,
  [("parenting-plans-guide", "Parenting Plans Guide"),
   ("child-custody-mediation", "Child Custody Mediation"),
   ("co-parenting-mediation", "Co-Parenting Mediation"),
   ("interim-parenting-orders-australia", "Interim Parenting Orders in Australia"),
   ("how-to-change-parenting-orders", "How to Change Parenting Orders"),
   ("fathers-rights-after-separation", "Fathers' Rights After Separation")],
  read_min=8,
)
print("parenting-arrangements-for-babies-australia built")
