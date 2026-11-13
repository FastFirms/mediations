"""gen_blog_batch33.py — refreshed cornerstones (Nov 2026) replacing stale imported versions.

best-apps-for-separated-parents   — co-parenting apps, verified AUD pricing for OurFamilyWizard,
                                    amica, what courts expect, when apps are not enough
who-pays-bills-during-separation  — interim bills, joint debts, mortgage, spousal maintenance,
                                    hardship help, mediation

These two slugs are owned by THIS file only. They were removed from gen_imported_posts.py,
gen_blog_batch12.py and gen_blog_batch16.py so those cannot overwrite them.
Facts checked 14 Nov 2026 against the official pages cited inline.
General information only, not legal advice.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, key_takeaway, inline_cta, callout
from authority_sources import cite


# ─────────────────────────────────────────────────────────────────────────────
# 1. Best apps for separated parents
# ─────────────────────────────────────────────────────────────────────────────
post(
    "best-apps-for-separated-parents",
    "Best Co-Parenting Apps in Australia (2026)",
    "Compare the best co-parenting apps for separated Australian parents in 2026: features, current costs, court-ready records, and when an app is not enough.",
    "Parenting",
    "Best apps for separated parents <em>in 2026</em>",
    ("A good co-parenting app will not fix a difficult relationship, but it can take a lot of heat out of the "
     "day-to-day: who has the kids this weekend, who paid for the school shoes, what the doctor said. "
     "This guide compares the main options available to Australian parents in 2026, what they cost, "
     "and how to choose one that suits your family."),
    [("why-apps", "Why co-parenting apps help"),
     ("comparison", "The main apps compared"),
     ("app-profiles", "App-by-app guide"),
     ("amica", "amica: the government-backed option"),
     ("choosing", "How to choose the right app"),
     ("court", "Apps, records and the family court"),
     ("limits", "When an app is not enough"),
     ("mediation", "Putting the app into your parenting plan")],
    key_takeaway(
        "The best co-parenting app is the one both parents will actually use. For high-conflict "
        "families, an app with tamper-proof message records such as OurFamilyWizard or TalkingParents "
        "is usually best. For cooperative parents, a free option such as AppClose or a shared calendar is "
        "often enough. To reach a formal agreement, amica is a low-cost government-backed tool.")
    + f"""
<h2 id="why-apps">Why co-parenting apps help</h2>
<p>Most conflict between separated parents is not about the big decisions. It is about the small, constant ones: a late handover, an unexpected expense, a message sent at 11pm that lands badly. Research from the {cite('aifs')} has consistently found that the quality of communication between parents after separation has a strong effect on how children adjust.</p>
<p>Co-parenting apps help in three practical ways:</p>
<ul>
<li><strong>One source of truth.</strong> A shared calendar removes arguments about whose weekend it is or when school holidays start.</li>
<li><strong>Calmer messages.</strong> Several apps include tone checkers that flag hostile wording before you hit send.</li>
<li><strong>A record.</strong> Messages, expenses and schedule changes are time-stamped and cannot be edited, which discourages bad behaviour and helps if a dispute arises later.</li>
</ul>
<p>They also keep co-parenting out of your personal inbox and text messages, which many parents say is the single biggest relief.</p>
"""
    + inline_cta("Struggling to communicate with your co-parent? A mediator can help you agree on how you will talk, as well as what you will do.")
    + f"""
<h2 id="comparison">The main apps compared</h2>
<p>Prices change often and are usually charged per parent. The table below reflects what was publicly listed in November 2026. Always check the provider's Australian page before you subscribe.</p>
<figure class="tbl"><table><caption>Co-parenting apps available in Australia</caption>
<thead><tr><th>App</th><th>Best for</th><th>Cost (per parent)</th><th>Tamper-proof records</th></tr></thead>
<tbody>
<tr><td>OurFamilyWizard</td><td>High-conflict families, court-ordered use</td><td>From AUD $199.99 a year (Essentials); Premium AUD $299.99; Max AUD $399.99</td><td>Yes</td></tr>
<tr><td>TalkingParents</td><td>Documented communication on a budget</td><td>Free tier; paid plans add features</td><td>Yes</td></tr>
<tr><td>AppClose</td><td>Cooperative parents wanting a free all-rounder</td><td>Free core features</td><td>Records kept in-app</td></tr>
<tr><td>2houses</td><td>Families wanting calendar plus expenses</td><td>Paid, with a free trial</td><td>Records kept in-app</td></tr>
<tr><td>Shared calendar (Google, Apple, Cozi)</td><td>Low-conflict parents who just need scheduling</td><td>Free</td><td>No</td></tr>
<tr><td>amica</td><td>Reaching a parenting or property agreement online</td><td>Low cost, per couple</td><td>Not a messaging app</td></tr>
</tbody></table></figure>
<p class="source-note">OurFamilyWizard pricing from its Australian plans page, checked 14 November 2026. Other apps: features and plans change; confirm on the provider's site.</p>
"""
    + inline_cta("Not sure which app suits your situation? We can talk it through at a free consultation.")
    + f"""
<h2 id="app-profiles">App-by-app guide</h2>
<h3>OurFamilyWizard</h3>
<p>OurFamilyWizard is the best known co-parenting platform and the one most often named in parenting orders. It combines a shared calendar, an expense log with reimbursement requests, an information bank for medical and school details, and a message board whose records cannot be edited or deleted. Its ToneMeter tool flags emotionally charged wording before a message is sent.</p>
<p>Each parent needs their own subscription, though one parent can pay for both. Children, extended family and professionals such as lawyers or mediators can be given limited free access. The cost is the main drawback for families on tight budgets.</p>
<h3>TalkingParents</h3>
<p>TalkingParents focuses on documented communication. Messages are time-stamped and cannot be changed, and records can be exported. A free tier covers secure messaging, with paid plans adding features such as recorded calls, a shared calendar and payment tracking. It is a sensible middle ground for parents who need a reliable record without paying for a full suite.</p>
<h3>AppClose</h3>
<p>AppClose offers messaging, a shared calendar, expense requests and payments without a subscription for its core features. It suits parents who get along reasonably well and want to keep logistics organised in one place.</p>
<h3>2houses</h3>
<p>2houses, developed in Europe, combines a calendar, a shared expense ledger, a family journal and an information bank. It works well for families who want the financial side handled cleanly.</p>
<h3>Shared calendars</h3>
<p>For cooperative parents, a shared Google or Apple calendar, or a family organiser such as Cozi, is often all that is needed. These are free and familiar, but they do not keep a tamper-proof record of messages, so they are not the right choice if conflict is high.</p>
"""
    + callout("A practical tip",
              "Whatever app you choose, agree on ground rules too: how quickly you will reply to non-urgent messages, what counts as urgent, and that children's issues stay in the app rather than spilling into text messages and social media.")
    + f"""
<h2 id="amica">amica: the government-backed option</h2>
<p>{cite('amica')} is different from the apps above. Developed by National Legal Aid and the state and territory Legal Aid Commissions, it is an online tool that helps separating couples work through and record agreements about parenting, property and money. It includes guidance on how property is generally divided and can generate a parenting plan or a formal agreement.</p>
<p>amica is designed for couples who can communicate reasonably well. It is not suitable where there is family violence, a significant power imbalance or complex finances. It is low cost, and the Australian Government has continued funding it under the Community Legal Services Program. See also {cite('legal_aid')}.</p>
<p>Many parents use amica or mediation to reach the agreement, then a co-parenting app to manage it day to day.</p>
"""
    + inline_cta("Need help reaching an agreement before choosing a tool to manage it? Parenting mediation can help.")
    + f"""
<h2 id="choosing">How to choose the right app</h2>
<p>Ask yourselves these questions:</p>
<ul>
<li><strong>How high is the conflict?</strong> If messages often turn hostile, choose an app with tamper-proof records and a tone checker.</li>
<li><strong>Is there a court order?</strong> Some orders name a particular app. Use the one specified.</li>
<li><strong>What is the budget?</strong> Paid apps cost both parents money every year. A free tier may be enough.</li>
<li><strong>What do you need most?</strong> Scheduling, expenses, document storage or messaging. Pick the app that does your priority well.</li>
<li><strong>Will both of you use it?</strong> An app only one parent uses creates more conflict, not less. Agree on it together.</li>
<li><strong>Who else needs access?</strong> Grandparents, step-parents, lawyers or your mediator may need limited access.</li>
</ul>
<p>Try a free trial together before committing, and make sure both parents are comfortable with the interface.</p>
"""
    + inline_cta("Want to agree on communication rules as part of a parenting plan? Talk to an accredited mediator.")
    + f"""
<h2 id="court">Apps, records and the family court</h2>
<p>Messages from co-parenting apps can be used as evidence in family law proceedings, and records that cannot be edited are generally more persuasive than screenshots of text messages. The {cite('fcfcoa')} expects parties to behave reasonably and focus on the child's best interests, which is the paramount consideration under the {cite('family_law_act')}.</p>
<p>That cuts both ways. Write every message as if a judge might read it one day. Polite, brief and child-focused messages reflect well on you. Sarcasm, insults or long arguments do not.</p>
<p>Courts can also order parents to use a specific app, particularly where communication has broken down. If you are heading in that direction, it is worth considering whether mediation could resolve the underlying issues first.</p>
"""
    + inline_cta("Court is rarely the best place to start. Find out how mediation could resolve the dispute instead.")
    + f"""
<h2 id="limits">When an app is not enough</h2>
<p>Apps manage logistics. They do not resolve disagreements about where the children live, how much time they spend with each parent, schooling or relocation. If the same arguments keep surfacing in the app, the problem is the arrangement, not the technology.</p>
<p>Signs it is time for a different approach:</p>
<ul>
<li>every schedule change becomes a negotiation;</li>
<li>one parent ignores the app or the agreed plan;</li>
<li>messages are routinely hostile despite tone tools;</li>
<li>you are keeping records mainly because you expect to go to court.</li>
</ul>
<p>If there is family violence or you feel unsafe, contact 1800RESPECT on <strong>1800 737 732</strong> ({cite('respect_1800')}) or call <strong>000</strong> in an emergency. Mediation may not be appropriate, and an app is not a safety plan. See our guide to <a href="/domestic-violence-and-family-law/">family violence and family law</a>.</p>
<p>For high-conflict situations, read about <a href="/high-conflict-family-law-mediation/">high-conflict mediation</a> and <a href="/mediation-with-a-narcissist/">mediating with a difficult ex</a>.</p>
"""
    + inline_cta("Same arguments, different week? A mediator can help reset the arrangement itself.")
    + f"""
<h2 id="mediation">Putting the app into your parenting plan</h2>
<p>The most effective approach is to agree on the app and the communication rules as part of your <a href="/parenting-plans-guide/">parenting plan</a> or consent orders. A mediator can help you settle details such as:</p>
<ul>
<li>which app you will use and who pays for it;</li>
<li>response times for routine and urgent matters;</li>
<li>how schedule changes are requested and confirmed;</li>
<li>how shared expenses are logged and reimbursed;</li>
<li>what information is shared about school, health and activities.</li>
</ul>
<p>Writing these rules down turns an app from a battleground into a tool. Our <a href="/co-parenting-mediation/">co-parenting mediation</a> service helps parents agree on exactly this, with or without lawyers.</p>
"""
    + inline_cta("Ready to agree a parenting plan that works day to day? Book a free consultation."),
    [("What is the best co-parenting app in Australia?",
      "There is no single best app. OurFamilyWizard is the most established and is often named in court orders, making it a strong choice for high-conflict families. TalkingParents offers documented messaging with a free tier, and AppClose provides free core features for cooperative parents."),
     ("How much does OurFamilyWizard cost in Australia?",
      "In November 2026 its Australian plans were listed at AUD $199.99 a year for Essentials, AUD $299.99 for Premium and AUD $399.99 for Max, per parent, with cheaper two-year options. One parent can pay for both. Check its Australian site for current pricing."),
     ("Are co-parenting app messages admissible in court?",
      "Messages from co-parenting apps can be used as evidence in Australian family law proceedings. Apps that keep tamper-proof, time-stamped records are generally more reliable than screenshots. Write every message as if a judge might read it."),
     ("Can a court order us to use a co-parenting app?",
      "Yes. Courts can include a requirement to communicate through a specific app in parenting orders, particularly where communication has broken down. Parents can also agree to it in a parenting plan or consent orders."),
     ("What is amica and is it free?",
      "amica is an online tool developed by National Legal Aid that helps separating couples reach agreements about parenting and property. It is low cost rather than free, and is designed for couples who can communicate reasonably well. It is not suitable where there is family violence."),
     ("What if my ex refuses to use a co-parenting app?",
      "You cannot require it without an agreement or court order. Mediation is often the best way to agree on a communication method. If it cannot be agreed, a parenting order can specify how parents must communicate.")],
    [("co-parenting-mediation", "Co-parenting mediation"),
     ("parenting-plans-guide", "Parenting plans in Australia"),
     ("parenting-plan-template", "Parenting plan template"),
     ("how-does-mediation-help-co-parenting", "How mediation helps co-parenting"),
     ("high-conflict-family-law-mediation", "High-conflict mediation"),
     ("christmas-parenting-arrangements-after-separation", "Christmas parenting arrangements")],
    read_min=10,
)


# ─────────────────────────────────────────────────────────────────────────────
# 2. Who pays the bills during separation
# ─────────────────────────────────────────────────────────────────────────────
post(
    "who-pays-bills-during-separation",
    "Who Pays the Bills During Separation? (2026)",
    "Who pays the mortgage, rent, utilities and joint debts after separating in Australia? Your obligations, interim options, hardship help and mediation.",
    "Separation",
    "Who pays the bills <em>during separation</em>",
    ("Separation does not pause the mortgage, the electricity bill or the credit card. In the first weeks, "
     "deciding who pays what is often the most urgent practical question, and the one most likely to "
     "cause conflict. This guide explains the legal position in Australia, the options for interim arrangements, "
     "and where to get help if money is tight."),
    [("short-answer", "The short answer"),
     ("joint-debts", "Joint debts and the lender"),
     ("mortgage", "The mortgage and the family home"),
     ("household", "Rent, utilities and household bills"),
     ("interim", "Interim arrangements and spousal maintenance"),
     ("children", "Children's costs and child support"),
     ("property", "How payments count in property settlement"),
     ("help", "If you cannot pay")],
    key_takeaway(
        "There is no automatic rule about who pays the bills after separation in Australia. Lenders can "
        "pursue either person named on a joint debt, regardless of any agreement between you. Most couples "
        "agree an interim arrangement, ideally in writing or through mediation, and payments made after "
        "separation can be taken into account in the final property settlement.")
    + f"""
<h2 id="short-answer">The short answer</h2>
<p>Australian family law does not set out who must pay each bill after a couple separates. Responsibility depends on whose name is on the account or loan, what you agree between yourselves, and, if needed, what a court orders. In practice, most couples work out an interim arrangement that keeps essentials paid while they negotiate the final property settlement.</p>
<p>The key principles to remember:</p>
<ul>
<li>A joint debt remains the responsibility of every person named on it until it is paid or refinanced.</li>
<li>An agreement between you does not bind the bank, landlord or utility company.</li>
<li>Payments made after separation can affect how property is divided later.</li>
<li>Child support and spousal maintenance are separate from who pays which bill.</li>
</ul>
"""
    + inline_cta("Need a fair interim arrangement quickly? Mediation can help you agree one in a single session.")
    + f"""
<h2 id="joint-debts">Joint debts and the lender</h2>
<p>If both your names are on a loan, credit card or other finance contract, the lender can usually ask either of you to repay the full amount. This is called joint and several liability. It does not change because you have separated, or because your former partner agreed to pay.</p>
<p>That means missed payments can affect both credit reports. Practical steps:</p>
<ul>
<li>List every joint debt, its balance, repayment and due date.</li>
<li>Contact lenders to ask about freezing redraw facilities or reducing limits on joint cards, which may need both parties' consent.</li>
<li>Agree in writing who will make each repayment until settlement.</li>
<li>Keep records of every payment you make.</li>
</ul>
<p>Debts in one person's name alone are that person's legal responsibility to the lender, though they are still considered in the overall property pool. Our guide to <a href="/who-is-responsible-for-debts-after-separation/">who is responsible for debts after separation</a> explains this in more detail. {cite('moneysmart_separation')} also has a useful financial checklist.</p>
"""
    + callout("Financial abuse",
              "Being forced to take on debt, having money withheld, or being prevented from accessing accounts can be financial abuse, a form of family violence. Contact 1800RESPECT on 1800 737 732 for confidential support, and get legal advice before agreeing to any arrangement.")
    + f"""
<h2 id="mortgage">The mortgage and the family home</h2>
<p>The mortgage is usually the largest bill and the most contentious. Common interim arrangements include:</p>
<figure class="tbl"><table><caption>Common interim mortgage arrangements</caption>
<thead><tr><th>Arrangement</th><th>How it works</th><th>Things to consider</th></tr></thead>
<tbody>
<tr><td>Person staying pays</td><td>The person living in the home covers the mortgage and outgoings</td><td>May be credited in settlement, offset against their use of the home</td></tr>
<tr><td>Shared payments continue</td><td>Both keep contributing as before</td><td>Simple, but the person who left may also be paying rent elsewhere</td></tr>
<tr><td>Person leaving contributes</td><td>The person who moved out pays part or all, often where children live in the home</td><td>Can be treated as partial support; record the reason</td></tr>
<tr><td>Hardship arrangement with lender</td><td>Reduced or paused repayments for a period</td><td>Interest usually still accrues; both borrowers may need to agree</td></tr>
<tr><td>Sell the property</td><td>Proceeds held in trust pending settlement</td><td>Ends the ongoing cost; needs agreement or a court order</td></tr>
</tbody></table></figure>
<p class="source-note">General guide. The right option depends on income, children's needs and each person's circumstances.</p>
<p>Moving out does not mean giving up your interest in the home. Read <a href="/who-gets-to-stay-in-the-house-during-separation/">who gets to stay in the house during separation</a> before deciding.</p>
"""
    + inline_cta("Can't agree on the mortgage? A mediator can help you weigh the options without escalating the conflict.")
    + f"""
<h2 id="household">Rent, utilities and household bills</h2>
<p>For rent, every person named on the lease is usually responsible to the landlord until the lease ends or is changed. If you leave a shared rental, speak with the agent about removing your name and the bond process in your state.</p>
<p>For utilities, the account holder is responsible to the provider. If the account is in your name and you have moved out, arrange to close or transfer it, but give fair notice so the other person and any children are not left without power or water.</p>
<p>Other common outgoings to agree on include council rates, strata levies, insurance, car registration and loan repayments, phone and internet plans, and subscriptions. A simple spreadsheet showing each bill, who pays and when avoids most arguments.</p>
"""
    + inline_cta("Want a written interim budget both of you can live with? Talk to an accredited mediator.")
    + f"""
<h2 id="interim">Interim arrangements and spousal maintenance</h2>
<p>Where one person earns significantly less, or stayed home to care for children, they may be unable to meet their reasonable expenses after separation. Under the {cite('family_law_act')}, a party may be entitled to spousal maintenance if they cannot adequately support themselves and the other party can reasonably afford to contribute. See our guide to <a href="/spousal-maintenance/">spousal maintenance</a>.</p>
<p>Interim maintenance can be agreed, or ordered by the court in urgent circumstances. Most couples prefer to agree, because court applications take time and cost money. An agreement can cover regular payments, one party paying certain bills directly, or a combination of both.</p>
<p>Whatever you agree, put it in writing, say whether it is intended to be taken into account in the final settlement, and get legal advice before signing anything long term.</p>
"""
    + inline_cta("Interim support is often easier to agree than people expect. A mediator can help.")
    + f"""
<h2 id="children">Children's costs and child support</h2>
<p>Child support is assessed separately from who pays the household bills. Services Australia uses a formula based on both parents' incomes and the care each provides. Start with {cite('services_australia_cs')}.</p>
<p>Parents can also agree to pay some costs directly, such as school fees, health insurance or extracurricular activities. Depending on how they are set up, these can sometimes be credited against child support. See our guides to <a href="/child-support-guide/">child support</a> and <a href="/who-pays-school-fees-after-separation/">who pays school fees after separation</a>.</p>
"""
    + inline_cta("Need to agree children's costs alongside the household bills? Mediation can cover both together.")
    + f"""
<h2 id="property">How payments count in property settlement</h2>
<p>Payments made after separation do not disappear. In the final settlement, a court or the parties can take into account who paid down the mortgage, who serviced joint debts, and who had use of the home. The 2025 amendments to the Family Law Act also make clear that the economic effects of family violence can be considered in property matters.</p>
<p>Keep records of every bill you pay after separation, including bank statements and receipts. Both parties also have a continuing duty to provide full and frank financial disclosure. See {cite('fcfcoa_disclosure')} and our guide to <a href="/property-settlement-mediation/">property settlement mediation</a>.</p>
<p>Married couples have 12 months from the date their divorce becomes final to start property proceedings, and de facto couples have 2 years from separation. Interim bill arrangements should not drift on indefinitely.</p>
"""
    + inline_cta("Turn your interim arrangement into a final property settlement, without court. Book a free consultation.", btn="Talk about property settlement")
    + f"""
<h2 id="help">If you cannot pay</h2>
<p>If separation has left you unable to meet your bills, act early. Lenders, energy retailers and telcos have financial hardship obligations and will often agree to reduced payments, deferrals or payment plans if you contact them before you fall too far behind.</p>
<ul>
<li>Call the {cite('ndh')} on <strong>1800 007 007</strong> for free, confidential financial counselling. You will be connected to a service in your state.</li>
<li>Check what government payments you may be eligible for through Services Australia, including Family Tax Benefit and Parenting Payment.</li>
<li>Use the budgeting tools at {cite('moneysmart')}.</li>
<li>Get free legal help through {cite('legal_aid')} or a community legal centre.</li>
</ul>
<p>If money worries are affecting your wellbeing, talk to your GP or call Lifeline on <strong>13 11 14</strong>.</p>
"""
    + inline_cta("Whenever you are ready, we can help you agree the money side calmly and without court."),
    [("Do I still have to pay joint debts after separation?",
      "Yes. If your name is on a loan, credit card or lease, the lender or landlord can usually pursue you for the full amount, even if your former partner agreed to pay. An agreement between you does not change your obligations to the creditor."),
     ("Who pays the mortgage after separation in Australia?",
      "There is no automatic rule. Commonly the person who stays in the home pays the mortgage, or both continue to contribute. Payments made after separation can be taken into account in the final property settlement, so keep records."),
     ("Can I stop paying the mortgage if I move out?",
      "Stopping payments can damage both parties' credit and risk default on the loan. Moving out does not end your obligation to the lender. Agree an interim arrangement in writing, or ask the lender about a hardship arrangement."),
     ("Can I get financial support from my ex while we sort out property?",
      "You may be entitled to spousal maintenance if you cannot adequately support yourself and your former partner can reasonably afford to contribute. This can be agreed or, in urgent cases, ordered by the court on an interim basis."),
     ("Do bills I pay after separation count in the property settlement?",
      "They can. Paying down the mortgage or joint debts after separation, or having exclusive use of the home, can be taken into account when the property pool is divided. Keep receipts and bank records."),
     ("Where can I get free help if I cannot pay my bills?",
      "Call the National Debt Helpline on 1800 007 007 for free financial counselling, contact your lenders and providers about hardship arrangements, and check your eligibility for Services Australia payments.")],
    [("who-is-responsible-for-debts-after-separation", "Who is responsible for debts after separation"),
     ("who-gets-to-stay-in-the-house-during-separation", "Who stays in the house during separation"),
     ("spousal-maintenance", "Spousal maintenance"),
     ("property-settlement-mediation", "Property settlement mediation"),
     ("separating-after-the-holidays", "Separating after the holidays"),
     ("child-support-guide", "Child support guide")],
    read_min=10,
)
