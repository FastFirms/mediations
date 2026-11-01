"""gen_blog_batch27.py — New cornerstones:
should-i-move-out-of-the-family-home — moving out during separation: property, children, money and safety
how-to-tell-children-about-separation — telling children about separation, by age, and planning it together
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, key_takeaway, inline_cta, callout
from authority_sources import cite


post(
    "should-i-move-out-of-the-family-home",
    "Should I Move Out of the Family Home? (Australia)",
    "Moving out won't cost you your share of the home, but it can affect parenting, money and evidence. What to agree first, and how mediation helps.",
    "Separation",
    "Should I move out of <em>the family home</em>",
    ("When a relationship ends, one of the first practical questions is who stays in the house. Many people "
     "worry that leaving means giving up their share of the property or their time with the children. "
     "The law is more reassuring than the rumours, but the way you move out still matters. This guide "
     "explains what moving out does and does not change, what to agree before you go, and how mediation "
     "can settle the interim arrangements without anyone filing in court."),
    [
        ("does-it-affect-property", "Does moving out affect your share of the property?"),
        ("children-status-quo",     "Moving out and the children"),
        ("money-while-apart",       "Who pays the mortgage and bills after you leave"),
        ("before-you-go",           "What to agree and organise before you move out"),
        ("staying-under-one-roof",  "If neither of you can afford to move"),
        ("safety-first",            "When safety means leaving now"),
        ("can-you-be-forced",       "Can your ex force you out, or stop you returning?"),
        ("mediation-interim",       "Settling interim arrangements through mediation"),
    ],
    key_takeaway(
        "No, moving out of the family home does not mean you lose your share of it. Ownership and your "
        "property settlement entitlements are unchanged. What moving out can affect is the day-to-day care "
        "of children, who pays which bills, and your access to records, so agree interim arrangements "
        "in writing before you leave. If you are unsafe, leave first and seek help."
    )
    + f"""
<h2 id="does-it-affect-property">Does moving out affect your share of the property?</h2>
<p>Moving out does not change who owns the home. If your name is on the title, it stays there until a property settlement or sale changes it. Under the {cite('family_law_act')}, a property settlement looks at the whole asset pool, each person's contributions over the relationship (financial and non-financial, including caring for children and the home), their future needs and whether the outcome is just and equitable. Who happened to be living in the house on the day of separation is not one of those factors.</p>
<p>What <em>can</em> matter is what happens after you leave. If you keep paying half the mortgage while living elsewhere and also paying rent, that is a post-separation contribution and may be taken into account. If your ex alone pays the mortgage for two years, that may count in their favour. The point is that the money trail after separation is relevant, not the address you sleep at.</p>
<figure class="tbl"><table><caption>Moving out: common myths and what usually happens</caption>
  <thead><tr><th>Myth</th><th>What usually happens</th></tr></thead>
  <tbody>
    <tr><td>"If I leave, I give up the house."</td><td>Your legal ownership and settlement rights are unaffected.</td></tr>
    <tr><td>"The person who stays keeps the home."</td><td>Who keeps the home is decided in the settlement, by agreement or court order.</td></tr>
    <tr><td>"Leaving counts as desertion."</td><td>Australia has no-fault divorce; why the relationship ended is not weighed.</td></tr>
    <tr><td>"Payments after I leave don't count."</td><td>Post-separation mortgage and bill payments can be taken into account.</td></tr>
    <tr><td>"I can't go back in once I've left."</td><td>A co-owner generally keeps a right to the property unless a court order says otherwise.</td></tr>
  </tbody>
</table></figure>
<p class="source-note">General information only. Your circumstances may differ; family lawyers and mediators can advise on your situation.</p>
"""
    + inline_cta("Worried that leaving will hurt your position? A short, confidential conversation can clear up what really changes, and what doesn't.")
    + f"""
<h2 id="children-status-quo">Moving out and the children</h2>
<p>This is where moving out needs the most thought. Parenting decisions are made on what is in the child's best interests, and the law does not favour mothers or fathers. But if you move out and the children stay with the other parent for months, a routine forms. When parents later cannot agree, the arrangement that has been working, sometimes called the status quo, can carry real weight in interim decisions, because courts are reluctant to disrupt a settled child.</p>
<p>That does not mean you should stay in a tense house at any cost. It means you should agree, before or as you move, when the children will spend time with you, and put it in writing. A simple interim parenting plan, signed and dated by you both, records that the arrangement is temporary and was agreed rather than abandoned. Our <a href="/parenting-plans-guide/">parenting plans guide</a> explains what to include.</p>
<ul>
<li>Agree a written schedule for the children's time with each parent from the first week.</li>
<li>Choose a new home close enough to school and activities to make that schedule realistic.</li>
<li>Keep a bedroom or space for the children, even if modest.</li>
<li>Keep records of the time you spend with them and your involvement in school and health.</li>
<li>Avoid taking the children with you without the other parent's agreement unless there is a safety risk.</li>
</ul>
"""
    + inline_cta("Agreeing an interim parenting schedule before you move out protects your relationship with your children. We can help you put one together quickly.")
    + f"""
<h2 id="money-while-apart">Who pays the mortgage and bills after you leave</h2>
<p>Running two households costs more than one, and money pressure is a common source of conflict in the first months. There is no automatic rule about who pays the mortgage after one person moves out. Lenders still expect the full repayment from everyone on the loan, so a missed payment affects both credit files regardless of who lives there.</p>
<p>Common interim arrangements include the person staying paying the mortgage and household bills, the person leaving continuing to contribute to the mortgage while the other pays outgoings, or both continuing as before until a sale. Whatever you choose, record it, and note that the arrangement is without prejudice to the final settlement. Our guide to <a href="/who-pays-bills-during-separation/">who pays bills during separation</a> goes through the options in detail.</p>
<p>If there are children, child support is assessed separately by {cite('services_australia_cs')}, using both incomes and the level of care each parent provides. Changes in care after one parent moves can change the assessment, so update Services Australia promptly. If one partner cannot meet their reasonable expenses, interim <a href="/spousal-maintenance-guide/">spousal maintenance</a> may also be relevant.</p>
<figure class="tbl"><table><caption>Typical interim money arrangements after one partner moves out</caption>
  <thead><tr><th>Arrangement</th><th>How it works</th><th>Watch out for</th></tr></thead>
  <tbody>
    <tr><td>Staying partner pays everything</td><td>Mortgage, rates and utilities paid by the person in the home</td><td>Can they actually afford it? Record it as a contribution.</td></tr>
    <tr><td>Shared mortgage, split bills</td><td>Both keep paying the loan; the occupant pays usage bills</td><td>The leaver may also be paying rent; agree a review date.</td></tr>
    <tr><td>Occupation offset</td><td>Occupant pays more of the loan in return for sole use</td><td>Write down how it will be treated in the settlement.</td></tr>
    <tr><td>Sell and divide later</td><td>Both maintain the home until it sells</td><td>Agree on agent, price range and timing early.</td></tr>
  </tbody>
</table></figure>
"""
    + inline_cta("Money arrangements in the first few months set the tone for everything else. A mediator can help you agree a fair interim budget in a single session.")
    + f"""
<h2 id="before-you-go">What to agree and organise before you move out</h2>
<p>A planned departure is calmer for everyone, and it leaves you in a much better position later. Before you leave, if it is safe to do so:</p>
<ol>
<li><strong>Copy financial records.</strong> Bank and super statements, tax returns, loan documents, insurance policies and the title or rates notice. Both of you have a duty of full and frank disclosure in a property settlement, and it is far easier to gather documents while you still have access.</li>
<li><strong>Photograph the contents.</strong> A quick record of furniture, vehicles and valuables helps avoid disputes about what was there.</li>
<li><strong>Take personal items and essentials.</strong> Identity documents, medication, sentimental items and work equipment. Leave shared household items for the settlement.</li>
<li><strong>Agree the children's schedule in writing.</strong> See above.</li>
<li><strong>Agree interim money arrangements.</strong> Mortgage, bills, joint accounts and credit cards.</li>
<li><strong>Change your passwords and mail.</strong> Secure email, banking and phone accounts, and redirect your post.</li>
<li><strong>Note the date of separation.</strong> It matters later for divorce (you need 12 months apart) and for working out the property pool.</li>
</ol>
<p>MoneySmart, {cite('moneysmart')}, has practical guidance on managing money and joint debts through a relationship breakdown.</p>
"""
    + callout("Avoid emptying joint accounts",
              "Taking more than your fair share from joint accounts, or cancelling the other person's cards, "
              "often escalates conflict and can be added back into the pool later. If you need money to set "
              "up a new home, agree an amount and record it as an advance against your final share.")
    + inline_cta("A checklist is easier to follow when you have agreed it together. We can help you both sign off on the practical steps before anyone moves.")
    + f"""
<h2 id="staying-under-one-roof">If neither of you can afford to move</h2>
<p>Housing costs mean many couples stay in the same home after deciding to separate, at least for a while. That is legally recognised: you can be <a href="/separated-under-one-roof/">separated under one roof</a> as long as the relationship has genuinely ended. If you later apply for divorce, you will need to show the separation was real, usually with evidence of separate finances, separate bedrooms and no longer presenting as a couple.</p>
<p>Living together while separated works best with clear ground rules: who uses which rooms, how the children's routines run, how bills are split and how you will communicate. It can be a sensible bridge while you agree a property settlement and plan a sale or <a href="/buying-out-your-ex-family-home-australia/">buy-out</a>, but it is not suitable where there is fear, control or violence.</p>
"""
    + inline_cta("Sharing a home while separated is easier with agreed house rules. Mediation is a practical way to set them without another argument.")
    + f"""
<h2 id="safety-first">When safety means leaving now</h2>
<p>Everything above assumes it is safe to plan. If you or your children are at risk, your safety comes first. Leave when you need to, take the children with you if they are in danger, and get help. Leaving because of family violence does not reduce your property entitlements, and courts take family violence seriously in parenting and, since the 2025 reforms, in property matters too.</p>
<ul>
<li>In an emergency, call <strong>000</strong>.</li>
<li>For confidential support, call <strong>1800RESPECT on 1800 737 732</strong> or visit {cite('respect_1800')}.</li>
<li>Police and local courts can make protection orders that may exclude a violent person from the home.</li>
</ul>
<p>Mediation may not be appropriate where there is family violence, and exemptions from family dispute resolution apply. Our guide to <a href="/domestic-violence-and-family-law/">domestic violence and family law</a> explains your options.</p>
"""
    + inline_cta("If there are safety concerns but you still want to resolve things without court, we can talk through whether shuttle or online mediation is suitable.", btn="Talk to us confidentially")
    + f"""
<h2 id="can-you-be-forced">Can your ex force you out, or stop you returning?</h2>
<p>Generally, a partner cannot lawfully lock out a co-owner or a joint tenant without a court order. Changing the locks on a jointly owned home can escalate things quickly and may be challenged. Courts can make orders for one person to have sole use of the home, and protection orders can exclude a person for safety reasons, but these are decided on evidence, not unilaterally. The {cite('fcfcoa')} handles applications for such orders where parties cannot agree.</p>
<p>If the home is in one person's sole name or rented in one name, the position can differ, and if you are in Western Australia, de facto matters go through the Family Court of WA. Because the details matter, it is worth getting legal advice if you are being pressured to leave or prevented from returning. Family lawyers <em>and</em> mediators often work together on exactly this kind of interim question.</p>
"""
    + inline_cta("Most disputes about who stays in the house can be settled by agreement. Book a free consultation to explore options before anyone applies to court.")
    + f"""
<h2 id="mediation-interim">Settling interim arrangements through mediation</h2>
<p>Court has its place, but it is rarely the best place to decide who sleeps where next week. Mediation lets you agree interim arrangements quickly: who stays, the children's schedule, who pays which bills, how you will communicate, and a timeline for the property settlement. These agreements can be recorded in a parenting plan and a written interim agreement, then made binding later through consent orders once the full picture is clear.</p>
<p>Research from the {cite('aifs')} shows that most separated parents sort out their arrangements without a judicial decision, often with the help of family dispute resolution. Starting with mediation keeps costs down and keeps decisions in your hands rather than a stranger's. Read more about <a href="/family-law-mediation/">family law mediation</a> or our <a href="/separation-guide/">complete separation guide</a>.</p>
"""
    + inline_cta("Ready to agree who stays, who goes and what happens next? Our accredited mediators can usually meet within days."),
    [
        ("Will I lose my share of the house if I move out?",
         "No. Moving out does not change legal ownership or your entitlement to a property settlement. The settlement "
         "looks at contributions, future needs and fairness across the whole relationship, not who stayed in the house."),
        ("Does moving out affect custody of the children?",
         "It can, if the children stay with the other parent and a routine forms without any agreement about your time. "
         "Agree a written interim parenting schedule before or as you move to protect your relationship with them."),
        ("Do I still have to pay the mortgage if I move out?",
         "The lender expects the full repayment from everyone on the loan. Between you, who pays is a matter for agreement, "
         "and payments made after separation can be taken into account in the final settlement."),
        ("Can my ex change the locks if we both own the house?",
         "Generally a co-owner should not be locked out without a court order. Courts can grant sole occupation and protection "
         "orders can exclude a person for safety, but these are decided on evidence. Get legal advice if this happens."),
        ("Can we be separated while still living together?",
         "Yes. You can be separated under one roof if the relationship has genuinely ended. If you later divorce, you will need "
         "evidence of the separation, such as separate finances and no longer presenting as a couple."),
        ("Can mediation help us decide who stays in the house?",
         "Yes. Mediation is a fast, low-cost way to agree interim living, parenting and money arrangements, which can later be "
         "formalised through consent orders. It may not be suitable where there is family violence."),
    ],
    [
        ("separation-guide", "Separation in Australia: Complete Guide"),
        ("who-pays-bills-during-separation", "Who Pays Bills During Separation?"),
        ("buying-out-your-ex-family-home-australia", "Buying Out Your Ex's Share of the Home"),
        ("parenting-plans-guide", "Parenting Plans in Australia"),
        ("property-settlement-after-separation", "Property Settlement After Separation"),
        ("domestic-violence-and-family-law", "Domestic Violence and Family Law"),
    ],
    read_min=9,
)


post(
    "how-to-tell-children-about-separation",
    "How to Tell Your Children About Separation",
    "How to tell your children you are separating: what to say at each age, when and where to do it, what to avoid, and how to plan the conversation with your ex.",
    "Parenting",
    "How to tell your children <em>about separation</em>",
    ("Telling your children that you are separating is one of the hardest conversations a parent will have. "
     "You cannot take the sadness away, but how the news is shared makes a real difference to how children "
     "cope in the months that follow. This guide covers what to say, how to adjust it for different ages, "
     "what to avoid, and how planning the conversation together, often with a mediator's help, sets up "
     "co-parenting on a calmer footing."),
    [
        ("plan-together",      "Plan the conversation together"),
        ("when-and-where",     "When and where to tell them"),
        ("what-to-say",        "What to say, and what to leave out"),
        ("by-age",             "Adjusting the conversation by age"),
        ("common-reactions",   "How children commonly react"),
        ("after-the-talk",     "The weeks after the conversation"),
        ("when-its-not-safe",  "When a joint conversation isn't possible"),
        ("mediation-role",     "How mediation helps you get the message right"),
    ],
    key_takeaway(
        "Tell your children together if you can, before anything changes in their daily life, in a calm and "
        "private setting. Keep the message simple and age-appropriate: the decision is an adult one, it is not "
        "their fault, both parents love them, and here is what will stay the same. Avoid blame and adult "
        "details, and agree the key messages with your ex first."
    )
    + f"""
<h2 id="plan-together">Plan the conversation together</h2>
<p>Children take their cue from their parents. When both parents sit down together and give the same message, children hear that the family is changing shape but that the adults are still working as a team for them. When they hear two conflicting stories, or hear it first from one parent with the other cast as responsible, they are drawn into the conflict from the first day.</p>
<p>Before you tell the children, agree with your ex on the essentials: a short, shared explanation of why, the practical facts you can already confirm (where each parent will live, what happens with school), and what you will say if they ask questions you have not answered yet. Australia's {cite('family_law_act')} centres every parenting decision on the best interests of the child, and that starts with how the news is delivered.</p>
<figure class="tbl"><table><caption>Points to agree with your ex before telling the children</caption>
  <thead><tr><th>Topic</th><th>What to agree</th></tr></thead>
  <tbody>
    <tr><td>The reason</td><td>One or two neutral sentences you will both use, with no blame</td></tr>
    <tr><td>Timing</td><td>A day and time when both of you can be present and available afterwards</td></tr>
    <tr><td>Living arrangements</td><td>What you can confirm now, and what is still being worked out</td></tr>
    <tr><td>What stays the same</td><td>School, friends, pets, activities, extended family</td></tr>
    <tr><td>Who else knows</td><td>Teachers, grandparents and carers, and when they will be told</td></tr>
    <tr><td>Follow-up</td><td>How you will check in with each child over the next few weeks</td></tr>
  </tbody>
</table></figure>
"""
    + inline_cta("Agreeing what to tell the children is often the first co-parenting decision you make. A mediator can help you get there calmly, before the conversation happens.")
    + f"""
<h2 id="when-and-where">When and where to tell them</h2>
<p>Timing matters. Child development guidance generally suggests telling children once the decision is final, so you are not unsettling them over something that may not happen, and before any visible change such as a parent moving out. A gap of one to two weeks between the conversation and a move gives children time to absorb the news without a long, anxious wait.</p>
<ul>
<li><strong>Choose a quiet time at home</strong>, not in the car, at a restaurant or before school.</li>
<li><strong>Avoid special days</strong> such as birthdays, holidays or the night before exams.</li>
<li><strong>Allow time afterwards</strong>, ideally a weekend, so you are both available for questions.</li>
<li><strong>Tell siblings together</strong>, then make time for each child individually afterwards, especially if their ages differ widely.</li>
</ul>
"""
    + inline_cta("Not sure how to time the news with a move or new living arrangements? We can help you plan both together.")
    + f"""
<h2 id="what-to-say">What to say, and what to leave out</h2>
<p>Children need honesty without adult detail. Most need to hear four things clearly, and often more than once:</p>
<ol>
<li><strong>It is a grown-up decision.</strong> "Mum and Dad have decided we won't live together any more."</li>
<li><strong>It is not your fault.</strong> Children, especially younger ones, often assume they caused it. Say plainly that nothing they did or said caused this, and nothing they do can change it.</li>
<li><strong>We both love you and that will never change.</strong> Parents separate from each other, not from their children.</li>
<li><strong>Here is what happens next.</strong> Concrete facts about where they will live, school and when they will see each parent.</li>
</ol>
<p>Leave out the reasons for the breakdown, affairs, money disputes and anything that casts one parent as the villain. Avoid asking children to choose, keep secrets or carry messages. If you do not know the answer to a question yet, it is fine to say "we're still working that out, and we'll tell you as soon as we know."</p>
"""
    + callout("A sample script",
              "\"We have something important to tell you. Mum and Dad have decided not to be married any more, "
              "and we'll be living in two homes. This is a grown-up decision and it is not because of anything "
              "you did. We both love you very much, and that will never change. You'll still go to the same school "
              "and see your friends, and you'll spend time with both of us. You can ask us anything, any time.\"")
    + inline_cta("Finding the right words is easier when you have agreed them in advance. Book a free consultation to talk through your plan.")
    + f"""
<h2 id="by-age">Adjusting the conversation by age</h2>
<p>What children understand, and what they worry about, changes with age. The government-funded {cite('frc')} service and its family relationship advice line offer free guidance on talking to children about separation. As a general guide:</p>
<figure class="tbl"><table><caption>Talking about separation at different ages (general guide)</caption>
  <thead><tr><th>Age</th><th>What they understand</th><th>What helps</th></tr></thead>
  <tbody>
    <tr><td>Under 5</td><td>Little sense of time; notice changes in routine and parental mood</td><td>Very short, simple words; keep routines steady; lots of reassurance and physical comfort</td></tr>
    <tr><td>5–8</td><td>May think they caused it or can fix it; may hope parents reunite</td><td>Repeat that it is not their fault; concrete details about where they'll sleep and who picks them up</td></tr>
    <tr><td>9–12</td><td>Understand more; may feel angry or take sides; notice fairness</td><td>Honest, simple reasons; invite questions; avoid criticising the other parent</td></tr>
    <tr><td>Teenagers</td><td>Understand adult relationships; may withdraw or want more say</td><td>Respect their views and routines; involve them in practical planning without making them decide</td></tr>
  </tbody>
</table></figure>
<p>Older children may ask whether they can choose where to live. Their views are considered, with weight depending on maturity, but there is no set age at which a child decides. Our guide on <a href="/what-age-can-a-child-choose-which-parent-to-live-with/">what age a child can choose which parent to live with</a> explains how this works.</p>
"""
    + inline_cta("Children of different ages need different things from a parenting plan. We can help you build one that fits each of them.")
    + f"""
<h2 id="common-reactions">How children commonly react</h2>
<p>There is no single "right" reaction. Some children cry, some get angry, some ask practical questions and go back to playing, and some seem unaffected and react weeks later. All of these are normal. Common responses include trouble sleeping, clinginess or regression in young children, changes in behaviour at school, and anger directed at the parent they feel safest with.</p>
<p>Research summarised by the {cite('aifs')} consistently finds that it is ongoing conflict between parents, more than the separation itself, that is most closely linked to poorer outcomes for children. Keeping conflict away from children, and keeping their routines predictable, are two of the most protective things you can do.</p>
"""
    + inline_cta("Reducing conflict between parents is the single biggest thing you can do for your children. Mediation is designed to do exactly that.")
    + f"""
<h2 id="after-the-talk">The weeks after the conversation</h2>
<p>The first conversation is the beginning, not the end. Children process big news in pieces and will come back with questions over days and months. Keep the door open, answer honestly at their level, and keep both homes as consistent as you can on bedtimes, screen time and school routines.</p>
<ul>
<li>Let the school know, so teachers can watch for changes and offer support.</li>
<li>Tell grandparents and close family the agreed message, and ask them not to criticise either parent.</li>
<li>Keep handovers short, calm and child-focused.</li>
<li>Use a shared calendar or co-parenting app to avoid mix-ups. See our guide to <a href="/best-apps-for-separated-parents/">the best apps for separated parents</a>.</li>
<li>Seek a counsellor or GP referral if a child's distress continues or worsens.</li>
</ul>
"""
    + inline_cta("A clear parenting plan makes the weeks after the conversation far more predictable for children. Let's put one in place.")
    + f"""
<h2 id="when-its-not-safe">When a joint conversation isn't possible</h2>
<p>Telling the children together is ideal, but it is not always possible or safe. If there has been family violence, if one parent has left suddenly, or if conflict is too high to sit in the same room, one parent may need to tell the children alone. Keep the same core messages, avoid blame, and focus on the children's safety and routine.</p>
<p>If you or your children are at risk, call <strong>000</strong> in an emergency, or contact <strong>1800RESPECT on 1800 737 732</strong> ({cite('respect_1800')}) for confidential support. Mediation may not be appropriate where there is family violence, and exemptions from family dispute resolution apply. Our guide to <a href="/domestic-violence-and-family-law/">domestic violence and family law</a> explains your options.</p>
"""
    + inline_cta("Where conflict is high but it is safe to negotiate, shuttle mediation keeps parents in separate rooms. Ask us whether it suits your situation.", btn="Talk to us confidentially")
    + f"""
<h2 id="mediation-role">How mediation helps you get the message right</h2>
<p>Court has its place, but it is rarely the best place to start planning a child's new routine. Mediation gives you a neutral space to agree the message to your children, the living arrangements you will describe, and the parenting plan that follows. Many parents find that agreeing "what we'll tell the kids" is the first point of genuine cooperation after separation, and it sets a pattern for the decisions that come next.</p>
<p>Our accredited family dispute resolution practitioners help you plan the conversation, draft a <a href="/parenting-plan-mediation/">parenting plan</a> and, if you wish, formalise arrangements through consent orders. Read more in our <a href="/co-parenting-mediation/">co-parenting mediation guide</a> or about <a href="/child-custody-mediation/">child custody mediation</a>. Family lawyers and mediators work well together here, and we often coordinate with your lawyer.</p>
"""
    + inline_cta("Want help planning the conversation and the parenting arrangements that follow? Book a free, confidential consultation."),
    [
        ("Should we tell our children about the separation together?",
         "Yes, if it is safe. Telling children together, with the same agreed message, shows them both parents are still "
         "working as a team for them. Where there is family violence or very high conflict, one parent may need to tell them alone."),
        ("When is the best time to tell children about separation?",
         "Once the decision is final and before any visible change such as a parent moving out, ideally one to two weeks ahead. "
         "Choose a calm, private time with space afterwards for questions, and avoid birthdays, holidays and exam periods."),
        ("What should I say to my child about divorce?",
         "Keep it simple: it is a grown-up decision, it is not their fault, both parents love them, and here is what will happen next. "
         "Leave out the reasons for the breakdown and never ask a child to choose sides or carry messages."),
        ("How do I tell a young child their parents are separating?",
         "Use very short, simple words, focus on concrete details like where they will sleep and who will pick them up, keep routines "
         "steady, and repeat reassurance often. Young children may need to hear the same answers many times."),
        ("What if my child asks to choose which parent to live with?",
         "A child's views are considered, with weight depending on age and maturity, but there is no age at which a child decides. "
         "Reassure them that the adults will make the decision and that their feelings matter."),
        ("Can a mediator help us plan what to tell the children?",
         "Yes. Many parents use an early mediation session to agree the message, timing and interim parenting arrangements, which then "
         "flow into a parenting plan. It may not be suitable where there is family violence."),
    ],
    [
        ("co-parenting-mediation", "Co-Parenting Mediation"),
        ("parenting-plans-guide", "Parenting Plans in Australia"),
        ("child-custody-mediation", "Child Custody Mediation"),
        ("what-age-can-a-child-choose-which-parent-to-live-with", "What Age Can a Child Choose?"),
        ("best-apps-for-separated-parents", "Best Apps for Separated Parents"),
        ("separation-guide", "Separation in Australia: Complete Guide"),
    ],
    read_min=9,
)
