"""gen_blog_batch32.py — topical cornerstone for the post-holiday separation peak.

separating-after-the-holidays — practical first steps for people deciding to separate
                                in January: safety, money, children, school year,
                                disclosure, time limits and mediation first.

General information only, not legal advice. Figures drawn from the cited official pages.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, key_takeaway, inline_cta, callout
from authority_sources import cite


post(
    "separating-after-the-holidays",
    "Separating After the Holidays: First Steps",
    "Thinking of separating in the new year? A calm, practical guide to the first steps: safety, money, children, the school year and resolving it without court.",
    "Separation",
    "Separating after the holidays <em>calmly</em>",
    ("For many families the summer break is when a long-building decision becomes clear. "
     "If you are thinking about separating in the new year, the first few weeks matter more than most people realise. "
     "This guide sets out the practical first steps, in order, and how to keep the process out of court."),
    [("why-january", "Why separations rise after the holidays"),
     ("safety", "Safety comes first"),
     ("first-30-days", "Your first 30 days: a checklist"),
     ("children", "Children and the new school year"),
     ("money", "Money, the home and disclosure"),
     ("time-limits", "Time limits you should know"),
     ("mediation", "Why mediation is the smarter first step"),
     ("support", "Looking after yourself")],
    key_takeaway(
        "If you are separating after the holidays, start with safety, then secure copies of key financial "
        "documents, agree a short-term plan for the children before school returns, and try mediation before "
        "anyone files in court. Separation itself needs no paperwork, but property and parenting arrangements "
        "should be formalised, and time limits apply.")
    + f"""
<h2 id="why-january">Why separations rise after the holidays</h2>
<p>Family lawyers, mediators and counsellors consistently describe January and early February as one of the busiest times of the year for new separation enquiries. The reasons are rarely mysterious. The holidays compress families into the same space for weeks, add financial pressure, bring extended family into old tensions, and remove the routine that kept difficult conversations at a distance.</p>
<p>Many people also hold off deliberately. They want the children to have one more Christmas together, or they do not want to make a decision during a stressful period. When the new year arrives, the decision that has been waiting finally gets made.</p>
<p>None of this means a separation has to become a dispute. Most separating couples in Australia never set foot in a courtroom. Research from the {cite('aifs')} has found that most separated parents sort out their parenting arrangements through discussion, with only a small minority relying on court orders. How you begin has a large effect on which path you end up on.</p>
"""
    + inline_cta("Not sure where to start? A free, confidential conversation can help you map out the first steps.")
    + f"""
<h2 id="safety">Safety comes first</h2>
<p>If you or your children are not safe, everything else in this guide comes second. Call <strong>000</strong> in an emergency. For confidential support and safety planning, contact 1800RESPECT on <strong>1800 737 732</strong> ({cite('respect_1800')}), available 24 hours a day.</p>
<p>Family violence includes coercive and controlling behaviour, financial control, threats and intimidation, not only physical harm. If it is part of your relationship:</p>
<ul>
<li>Plan how and when you will leave, and where you will go, with a support service if possible.</li>
<li>Keep important documents, medication and a phone charger somewhere you can reach quickly.</li>
<li>Know that an exemption from the usual requirement to attempt Family Dispute Resolution may apply.</li>
<li>Get legal advice early. <a href="/domestic-violence-and-family-law/">Read our guide to family violence and family law</a>.</li>
</ul>
<p>Mediation is not appropriate where one person cannot speak freely or safely. A good mediator screens for this at the start and will tell you honestly if another process is better.</p>
"""
    + callout("A note on timing",
              "Telling your partner you want to separate is one of the hardest conversations you will have. Choose a calm, private moment, not a family event or a day the children are home. If you are worried about how they will react, speak to a counsellor or support service first.")
    + f"""
<h2 id="first-30-days">Your first 30 days: a checklist</h2>
<p>You do not have to resolve everything at once. In the first month, the goal is stability and information, not final decisions. The table below sets out what to prioritise.</p>
<figure class="tbl"><table><caption>First 30 days after separating</caption>
<thead><tr><th>Week</th><th>Focus</th><th>Practical steps</th></tr></thead>
<tbody>
<tr><td>Week 1</td><td>Safety and housing</td><td>Confirm where each person will live, or agree how you will share the home for now. Note your separation date.</td></tr>
<tr><td>Week 1–2</td><td>Children</td><td>Agree a simple interim care schedule and how you will tell the children together.</td></tr>
<tr><td>Week 2</td><td>Documents</td><td>Copy recent bank, super, tax, mortgage and loan statements. Store them securely.</td></tr>
<tr><td>Week 2–3</td><td>Money</td><td>Agree who pays which bills in the short term. Consider a separate account for your own income.</td></tr>
<tr><td>Week 3</td><td>Child support</td><td>Check your position with Services Australia if one parent will provide most of the care.</td></tr>
<tr><td>Week 3–4</td><td>Advice</td><td>Get initial legal advice on your property and parenting position, and book a mediation consultation.</td></tr>
</tbody></table></figure>
<p class="source-note">General guide only. Your order of priorities will depend on your circumstances.</p>
<p>Write down your separation date and keep a note of what happened. It matters for the twelve-month separation period required before a divorce, and it can matter for property and child support. If you will keep living in the same house for a time, our guide to <a href="/separated-under-one-roof/">separation under one roof</a> explains what to record. Our <a href="/pre-separation-checklist/">pre-separation checklist</a> has a fuller list of documents to gather.</p>
"""
    + inline_cta("Want help putting together an interim plan for the first few months? Talk to an accredited mediator.")
    + f"""
<h2 id="children">Children and the new school year</h2>
<p>A January separation runs straight into the start of the school year, which is why it helps to agree interim arrangements early. Children cope best when they know where they will be sleeping, who is doing school drop-offs and what happens on weekends.</p>
<p>Some practical points to agree before term starts:</p>
<ul>
<li><strong>The weekly schedule:</strong> which nights with each parent, and how handovers will work around school.</li>
<li><strong>School communication:</strong> both parents should usually receive school notices, reports and event information.</li>
<li><strong>Costs:</strong> uniforms, books, fees and activities. Our guide to <a href="/who-pays-school-fees-after-separation/">who pays school fees after separation</a> covers this.</li>
<li><strong>Telling the children:</strong> where possible, together, in simple age-appropriate language, without blame.</li>
</ul>
<p>Under the {cite('family_law_act')}, the child's best interests are the paramount consideration, and the Act encourages parents to reach agreement rather than litigate. A written <a href="/parenting-plans-guide/">parenting plan</a> is a flexible way to record what you agree. If you later want it to be enforceable, it can be turned into <a href="/consent-orders-explained/">consent orders</a>.</p>
"""
    + inline_cta("Need a parenting arrangement in place before school goes back? Parenting mediation can usually be arranged quickly.")
    + f"""
<h2 id="money">Money, the home and disclosure</h2>
<p>Financial uncertainty is the most common source of stress early in a separation. A few early steps reduce it considerably.</p>
<ul>
<li><strong>Get a clear picture:</strong> list assets, debts, superannuation and income for both of you. Many people know less about their household finances than they think.</li>
<li><strong>Do not hide or move assets:</strong> both parties have a continuing duty to make full and frank financial disclosure. See {cite('fcfcoa_disclosure')} and our guide to the <a href="/duty-of-disclosure-in-australian-family-law/">duty of disclosure</a>.</li>
<li><strong>Keep paying the essentials:</strong> mortgage, rent and utilities still need to be covered. Agree a short-term arrangement in writing.</li>
<li><strong>Check joint accounts and credit:</strong> consider whether redraw facilities or joint credit cards need agreed limits.</li>
<li><strong>Child support:</strong> Services Australia can assess child support once parents have separated. Start with {cite('services_australia_cs')}.</li>
</ul>
<p>The home is usually the largest and most emotional asset. Nobody automatically has to leave, and moving out does not give up your share. Read <a href="/who-gets-to-stay-in-the-house-during-separation/">who gets to stay in the house during separation</a> before making a decision.</p>
<p>For budgeting help during the transition, {cite('moneysmart')} has free, practical tools.</p>
"""
    + inline_cta("Property settlement does not have to mean a court battle. Mediation helps you divide assets by agreement.", btn="Talk about property settlement")
    + f"""
<h2 id="time-limits">Time limits you should know</h2>
<p>Separation has no deadline of its own, but several important processes do. Missing them can mean needing the court's permission to proceed.</p>
<figure class="tbl"><table><caption>Key family law time limits</caption>
<thead><tr><th>Matter</th><th>Time limit</th></tr></thead>
<tbody>
<tr><td>Divorce application (married couples)</td><td>Must have been separated for at least 12 months</td></tr>
<tr><td>Property or spousal maintenance claim (married)</td><td>Within 12 months of the divorce becoming final</td></tr>
<tr><td>Property or maintenance claim (de facto)</td><td>Within 2 years of separation</td></tr>
<tr><td>Parenting arrangements</td><td>No fixed time limit, but Family Dispute Resolution is generally required before applying to court</td></tr>
</tbody></table></figure>
<p class="source-note">Sources: {cite('family_law_act')} and {cite('fcfcoa')}. Western Australian de facto couples are covered by the {cite('family_court_wa')}.</p>
<p>There is no rule that you must divorce before sorting out property. Many couples reach a property agreement well within the first year and formalise it through consent orders, then apply for a <a href="/applying-for-a-divorce-in-australia/">divorce</a> once the twelve months have passed.</p>
"""
    + inline_cta("Keen to settle things before time limits become an issue? Start with a free consultation.")
    + f"""
<h2 id="mediation">Why mediation is the smarter first step</h2>
<p>Court has its place, but it is rarely the best place to start. Contested family law proceedings can take years and cost each party tens of thousands of dollars, while most mediated matters resolve far sooner. See our breakdown of the <a href="/cost-of-divorce-in-australia/">cost of divorce in Australia</a>.</p>
<p>For parenting matters, attempting <a href="/what-is-the-difference-between-mediation-and-family-dispute-resolution/">Family Dispute Resolution</a> is generally required before a court application, unless an exemption applies. If agreement is not reached, an accredited practitioner can issue a <a href="/section-60i-certificates/">Section 60I certificate</a>. See {cite('fcfcoa_fdr')}.</p>
<p>Mediation works well for separating couples because it:</p>
<ul>
<li>keeps decisions with the two people who know the family best;</li>
<li>can cover parenting, property, superannuation and child support in one process;</li>
<li>is confidential, unlike most court evidence;</li>
<li>works alongside your lawyers, who can advise you before and after each session;</li>
<li>can be done online or in separate rooms through <a href="/shuttle-mediation-guide/">shuttle mediation</a> if being together is too hard.</li>
</ul>
"""
    + callout("Family lawyers and mediators, together",
              "Mediation is not a replacement for legal advice. Many clients see a family lawyer to understand their entitlements, then use mediation to reach an agreement, and return to their lawyer to formalise it. That combination is often the fastest and least costly path.")
    + inline_cta("Ready to talk it through? Book a free, no-obligation consultation with an accredited mediator.")
    + f"""
<h2 id="support">Looking after yourself</h2>
<p>Separation is a major life change, and it is normal to feel grief, anger, relief and exhaustion, sometimes all in one day. Decisions made in the first weeks tend to be better when you are supported.</p>
<ul>
<li>Talk to your GP about how you are coping. A mental health treatment plan can give you access to subsidised counselling.</li>
<li>Family Relationship Centres offer free or low-cost information and support. Find one through {cite('frc')}.</li>
<li>Lean on a small number of trusted people, and keep adult conversations away from the children.</li>
<li>If you are in crisis, call Lifeline on <strong>13 11 14</strong>.</li>
</ul>
<p>The way a separation starts often shapes how it ends. A calm, informed first month makes an agreed outcome far more likely, and that is better for everyone, especially the children.</p>
"""
    + inline_cta("Whenever you are ready, we can help you resolve it without court."),
    [("Is January a common time to separate?",
      "Many family law and mediation practices report a rise in new separation enquiries in January and early February. The holidays add pressure, and many people delay a decision until after Christmas for the children's sake."),
     ("Do I need to do anything legally to separate?",
      "No. There is no form to separate in Australia. Separation happens when one or both partners decide the relationship is over and act on it. Record the date, and later formalise parenting and property arrangements."),
     ("Can we separate but keep living in the same house?",
      "Yes. Separation under one roof is common, especially with cost-of-living pressures. If you later apply for divorce, you will need to show the court how the relationship changed, so keep a note of what happened and when."),
     ("How soon can we sort out property after separating?",
      "You can reach a property agreement at any time after separation, and you do not need to wait for a divorce. Married couples must start court proceedings within 12 months of the divorce becoming final; de facto couples within 2 years of separation."),
     ("Do we have to go to mediation before court?",
      "For parenting matters, you are generally required to attempt Family Dispute Resolution and obtain a Section 60I certificate before applying to court, unless an exemption applies, such as family violence or urgency. For property matters, the court expects genuine steps to resolve the dispute first."),
     ("What if my ex will not agree to mediation?",
      "A mediator can contact the other party and explain the process. If they refuse or do not respond, an accredited Family Dispute Resolution Practitioner can issue a Section 60I certificate recording that, which allows a parenting application to proceed.")],
    [("pre-separation-checklist", "Pre-separation checklist"),
     ("separated-under-one-roof", "Separated under one roof"),
     ("parenting-plans-guide", "Parenting plans in Australia"),
     ("property-settlement-mediation", "Property settlement mediation"),
     ("christmas-parenting-arrangements-after-separation", "Christmas parenting arrangements"),
     ("cost-of-divorce-in-australia", "Cost of divorce in Australia")],
    read_min=9,
)
