"""gen_blog_batch26.py — New cornerstones:
buying-out-your-ex-family-home-australia — refinancing and buying out a partner's share of the home
inheritance-in-property-settlement-australia — how inheritances are treated in a property settlement
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, key_takeaway, inline_cta, callout
from authority_sources import cite


post(
    "buying-out-your-ex-family-home-australia",
    "Buying Out Your Ex's Share of the Family Home",
    "How to buy out your ex's share of the family home in Australia: valuation, refinancing, stamp duty, tax and how mediation turns a handshake into a binding deal.",
    "Property &amp; Finances",
    "Buying out your ex's share of <em>the family home</em>",
    ("For many separating couples the most workable outcome is that one person keeps the family home "
     "and the other is paid out. It keeps children in a familiar neighbourhood and avoids a forced sale. "
     "But a buy-out is really three separate questions: what is the home worth, can the person staying "
     "actually borrow enough, and how do you make the deal binding. This guide walks through each one, "
     "and shows how mediation can settle the numbers before anyone files in court."),
    [
        ("how-buyouts-work",   "How a buy-out works"),
        ("valuation",          "Agreeing what the home is worth"),
        ("working-out-payout", "Working out the payout figure"),
        ("refinancing",        "Refinancing and removing your ex from the loan"),
        ("stamp-duty-tax",     "Stamp duty and capital gains tax"),
        ("making-binding",     "Making the buy-out legally binding"),
        ("when-it-wont-work",  "When a buy-out isn't realistic"),
        ("faq",                "Frequently asked questions"),
    ],
    key_takeaway(
        "A buy-out means one partner keeps the home and pays the other their agreed share, usually by "
        "refinancing. The steps are: agree a valuation, work out the payout within the whole property "
        "pool, confirm the lender will approve the new loan, and record the deal in consent orders or a "
        "binding financial agreement. Mediation lets you settle the numbers early, without court."
    )
    + f"""
<h2 id="how-buyouts-work">How a buy-out works</h2>
<p>In a buy-out, one partner takes full ownership of the home and the other receives value in return. That value is most often a cash payment funded by a new loan, but it can also be a larger share of superannuation, savings or other assets. Because the home is usually the biggest asset, how you handle it shapes the whole property settlement.</p>
<p>The {cite('family_law_act')} does not set a fixed percentage for who gets what. The outcome depends on contributions, future needs and what is fair overall. A buy-out is therefore not "half the house value": it is whatever share of the <em>entire</em> pool you agree (or a court would order) is yours, paid in the form that works. Our guide to <a href="/what-is-in-the-property-pool/">what is in the property pool</a> explains how that pool is built.</p>
<figure class="tbl"><table><caption>Common ways to structure a buy-out</caption>
  <thead><tr><th>Structure</th><th>How it works</th><th>Best suited to</th></tr></thead>
  <tbody>
    <tr><td>Cash payout via refinance</td><td>Staying partner borrows to pay out the other's share</td><td>Strong income, equity in the home</td></tr>
    <tr><td>Asset offset</td><td>Staying partner keeps the home; leaving partner takes more super or savings</td><td>Limited borrowing capacity</td></tr>
    <tr><td>Staged payout</td><td>Payment over an agreed period, often secured by a charge</td><td>Temporary cash-flow gap</td></tr>
    <tr><td>Deferred sale</td><td>Home kept until a trigger (children finish school, a set date), then sold</td><td>Young children, stable housing priority</td></tr>
  </tbody>
</table></figure>
"""
    + inline_cta("Not sure which structure suits your situation? A mediator can help you compare options before you commit to one.")
    + f"""
<h2 id="valuation">Agreeing what the home is worth</h2>
<p>Almost every dispute about a buy-out starts with the number on the house. The person staying tends to hope it is low and the person leaving hopes it is high, so agreeing a method is more productive than arguing about the figure.</p>
<p>The most reliable approach is a written valuation from an independent registered valuer, jointly instructed so neither side can say it was chosen to suit the other. Appraisals from real estate agents are cheaper and quicker, and many couples take two or three and average them. A desktop valuation is often enough for an agreement between cooperative parties, while a full inspection valuation is stronger evidence if the deal is later tested. The fees are usually shared, and a valuer's report is typically a modest cost compared with the sums involved.</p>
<p>Agree the <strong>valuation date</strong> too. Property markets move, and a figure from six months ago may no longer reflect reality when the deal is signed. Parties who have {cite('fcfcoa_disclosure')} obligations in mind tend to settle faster, because both sides lay out their numbers openly.</p>
"""
    + inline_cta("Disagreeing about the value of the home is one of the most common sticking points, and one of the easiest to resolve with a neutral process.")
    + f"""
<h2 id="working-out-payout">Working out the payout figure</h2>
<p>Start with the whole pool: the home, super, savings, vehicles, investments and any business interests, minus debts. Then agree the percentage split, and subtract the value of what each person already takes. The difference is the balancing payment.</p>
<figure class="tbl"><table><caption>Worked example: a buy-out within the whole pool</caption>
  <thead><tr><th>Item</th><th>Value</th></tr></thead>
  <tbody>
    <tr><td>Family home (agreed valuation)</td><td>$900,000</td></tr>
    <tr><td>Mortgage</td><td>−$400,000</td></tr>
    <tr><td>Superannuation (combined)</td><td>$250,000</td></tr>
    <tr><td>Savings and vehicles</td><td>$50,000</td></tr>
    <tr><td><strong>Net pool</strong></td><td><strong>$800,000</strong></td></tr>
    <tr><td>Agreed split 55 / 45 in favour of the partner staying</td><td>$440,000 / $360,000</td></tr>
    <tr><td>Staying partner takes the home (net $500,000 equity)</td><td>Owes a balancing payment of roughly $60,000 less any offset in super or savings</td></tr>
  </tbody>
</table></figure>
<p>Notice that the staying partner may owe far less than "half the equity", because the other person can take a larger share of super or savings. That flexibility is why a buy-out should be negotiated alongside the rest of the settlement. Our <a href="/property-settlement-mediation-guide/">property settlement mediation guide</a> shows how couples work through these trade-offs in one session. The figures above are illustrative only.</p>
"""
    + inline_cta("Seeing the whole pool on one page often makes a fair split obvious. We can help you build that picture together.")
    + f"""
<h2 id="refinancing">Refinancing and removing your ex from the loan</h2>
<p>A promise to pay does not release your ex from the mortgage. Their name stays on the loan until the lender agrees to remove it, which usually means the staying partner must refinance in their sole name. Lenders assess the application on that person's income alone, so check borrowing capacity <em>before</em> you agree to a figure. {cite('moneysmart')} publishes independent tools for estimating repayments and understanding home loan costs.</p>
<p>Speak to a mortgage broker or your lender early and ask for a written indication of how much they would lend. Lenders may count child support and spousal maintenance as income in some cases, but policies vary. If the answer is "not enough", you still have options: a larger offset from other assets, a longer timeframe to refinance, or a staged payout.</p>
<ul>
<li>Set a firm refinance deadline in the agreement, for example 90 or 120 days.</li>
<li>Decide who pays repayments, rates and insurance until the new loan settles.</li>
<li>Agree what happens if the lender declines: usually a listing for sale by a set date.</li>
<li>Budget for discharge fees, legal costs and any break costs on a fixed-rate loan.</li>
</ul>
"""
    + inline_cta("Setting a realistic refinance deadline protects both of you. A mediator can help you build a timeline a lender will actually meet.")
    + f"""
<h2 id="stamp-duty-tax">Stamp duty and capital gains tax</h2>
<p>Transferring a title can trigger stamp duty (transfer duty), but most states and territories provide a concession or exemption when the transfer is made under a family law agreement or court order following a relationship breakdown. The rules, forms and conditions differ between jurisdictions, so check with your state revenue office before relying on a concession, and note that the transfer often needs to be backed by consent orders or a financial agreement.</p>
<p>On the tax side, the {cite('ato')} offers a capital gains tax rollover for assets transferred between spouses or de facto partners because of a relationship breakdown, which defers the gain rather than removing it. The home you live in is often exempt from CGT anyway, but investment properties and holiday homes are different. Tax advice from an accountant is worth the fee.</p>
<figure class="tbl"><table><caption>Typical costs of a buy-out (illustrative ranges)</caption>
  <thead><tr><th>Cost</th><th>Typical range</th><th>Who usually pays</th></tr></thead>
  <tbody>
    <tr><td>Independent valuation</td><td>$400 – $900</td><td>Shared</td></tr>
    <tr><td>Mortgage discharge and establishment fees</td><td>$500 – $1,500</td><td>Staying partner</td></tr>
    <tr><td>Conveyancing / title transfer</td><td>$800 – $2,000</td><td>Often shared or by agreement</td></tr>
    <tr><td>Consent orders (legal drafting plus filing)</td><td>Varies by provider</td><td>Shared</td></tr>
  </tbody>
</table></figure>
<p class="source-note">Ranges are indicative and vary by state and provider. Confirm current fees with your valuer, lender and state revenue office.</p>
"""
    + inline_cta("Costs add up fast when disputes drag on. Agreeing the structure early keeps professional fees where they belong: on the paperwork, not the argument.")
    + f"""
<h2 id="making-binding">Making the buy-out legally binding</h2>
<p>An agreement shaken on at the kitchen table is not enough. Without formal orders, your ex could still change their mind, and a title transfer may not attract stamp duty relief. There are two main routes. <a href="/consent-orders-explained/">Consent orders</a> are filed with the {cite('fcfcoa_consent_orders')} registry and, once made, have the force of a court order without a hearing. A <a href="/binding-financial-agreements-guide/">binding financial agreement</a> is a private contract, with each party receiving independent legal advice.</p>
<p>Time limits matter. Generally, you must start property proceedings within 12 months of a divorce becoming final, or within two years of a de facto separation, unless the court gives permission. Do not let a handshake deal run past those dates. See our <a href="/property-settlement-timeline/">property settlement timeline</a> for the typical sequence.</p>
"""
    + inline_cta("Once a mediated agreement is reached, your lawyer can turn it into consent orders quickly. Start the conversation with a free consultation.")
    + f"""
<h2 id="when-it-wont-work">When a buy-out isn't realistic</h2>
<p>A buy-out is not always the right answer. If neither partner can afford to refinance, or the home is the only significant asset and keeping it would leave the other with nothing, a sale may be fairer. Selling is not a failure: it can free both people to start over. Our guide on <a href="/how-to-sell-property-during-a-divorce/">selling property during a divorce</a> covers that path, and <a href="/who-gets-to-stay-in-the-house-during-separation/">who stays in the house</a> deals with the period before settlement.</p>
<p>Mediation may also be unsuitable where there is family violence or serious safety concerns. If that is your situation, call 000 in an emergency, or 1800RESPECT (1800 737 732) for confidential support via {cite('respect_1800')}, and seek legal advice before any negotiation. Exemptions to compulsory dispute resolution can apply, as explained in our guide to <a href="/domestic-violence-and-family-law/">domestic violence and family law</a>.</p>
<p>Where it is safe to proceed, mediation is usually the smarter first step. Court has its place, but it is rarely the best place to start a conversation about who keeps the home.</p>
"""
    + inline_cta("Whether the answer is a buy-out, a deferred sale or a sale now, a neutral mediator can help you decide together.")
    ,
    [
        ("Can I force my ex to sell the house instead of buying them out?",
         "Not by simply asking. If you cannot agree, either person can apply to the court for orders, and a sale is one possible outcome. In practice, most couples reach a better result by negotiating a buy-out or agreed sale through mediation first."),
        ("Do I have to pay my ex half the value of the house?",
         "No. There is no automatic 50/50 rule. Your ex's entitlement is a share of the whole property pool, which may be more or less than half, and it can be met partly through super or other assets rather than cash."),
        ("What if I can't get approved to refinance on my own?",
         "You can offset the payout against other assets, extend the timeframe, stage the payment or agree to sell. Get a written indication from a lender before agreeing a figure so your agreement is realistic."),
        ("Is stamp duty payable when my ex transfers the house to me?",
         "Often a concession or exemption applies when the transfer follows a family law agreement or court order, but rules differ in each state and territory. Check with your state revenue office before transferring."),
        ("How long do I have to finalise a property settlement?",
         "Generally 12 months from the date a divorce becomes final, or two years from the end of a de facto relationship. The court can allow late applications in limited circumstances, so do not rely on that."),
        ("Do I need consent orders for a buy-out?",
         "It is strongly recommended. Consent orders or a binding financial agreement make the deal enforceable, support stamp duty relief and give your lender the paperwork it needs."),
    ],
    [
        ("what-is-in-the-property-pool",           "What's in the Property Pool?"),
        ("property-settlement-mediation-guide",    "Property Settlement Mediation Guide"),
        ("consent-orders-explained",               "Consent Orders Explained"),
        ("how-to-sell-property-during-a-divorce",  "Selling Property During a Divorce"),
        ("who-gets-to-stay-in-the-house-during-separation", "Who Stays in the House?"),
        ("property-settlement-timeline",           "Property Settlement Timeline"),
    ],
    8
)


post(
    "inheritance-in-property-settlement-australia",
    "Is Inheritance Included in a Property Settlement?",
    "Is an inheritance part of the property pool after separation? How Australian courts treat inheritances, when they're protected and how to settle by mediation.",
    "Property &amp; Finances",
    "Inheritance in a <em>property settlement</em>",
    ("Receiving an inheritance is usually a family event, not a financial plan. Then a relationship ends, "
     "and a question follows: does my former partner get a share? The honest answer is that it depends on "
     "timing, size and what happened to the money. This guide explains how Australian family law approaches "
     "inheritances, gifts and expected inheritances, and how mediation helps you reach an agreement that "
     "feels fair without a court hearing."),
    [
        ("is-it-in-the-pool",  "Is an inheritance part of the property pool?"),
        ("what-courts-weigh",  "What decides how much weight it carries"),
        ("before-or-during",   "Received before, during or after the relationship"),
        ("mixed-into-assets",  "When inherited money was mixed into the family home"),
        ("expected-inheritance", "Inheritances you haven't received yet"),
        ("trusts-estates",     "Trusts, wills and estates that are still open"),
        ("mediation-approach", "Settling inheritance questions through mediation"),
        ("faq",                "Frequently asked questions"),
    ],
    key_takeaway(
        "Yes, an inheritance can form part of the property pool, but it is not automatically split "
        "equally. Courts treat it as a contribution by the person who received it, and the weight it "
        "carries depends on its size, when it arrived, how long the relationship lasted and whether it "
        "was kept separate or spent on shared assets. Many couples agree the result in mediation."
    )
    + f"""
<h2 id="is-it-in-the-pool">Is an inheritance part of the property pool?</h2>
<p>Under the {cite('family_law_act')}, the starting point is that the court looks at all the property of the parties, whoever owns it and however it was acquired. An inheritance that you have received is property, so it is generally within the pool. That does not mean it is divided in half. It means it is considered, and then given weight as a contribution made by the person who received it.</p>
<p>That distinction matters. An inheritance is treated differently from a salary earned during the relationship, because it came from outside the partnership and not from the efforts of both partners. Many people are surprised to learn that it can be both included and still largely protected. For the broader picture, see our guide to <a href="/what-is-in-the-property-pool/">what is in the property pool</a>.</p>
<figure class="tbl"><table><caption>How different types of inheritance are usually treated</caption>
  <thead><tr><th>Situation</th><th>Usually treated as</th></tr></thead>
  <tbody>
    <tr><td>Cash or property already received</td><td>Part of the pool, with a contribution credit to the recipient</td></tr>
    <tr><td>Gift or inheritance before the relationship began</td><td>Initial contribution, often weighed strongly in shorter relationships</td></tr>
    <tr><td>Inheritance spent on the family home</td><td>Contribution to the home, weighed against the length of the relationship</td></tr>
    <tr><td>Inheritance still expected (will not yet in effect)</td><td>Not part of the pool; may be a financial resource</td></tr>
    <tr><td>Interest in an open estate or trust</td><td>Depends on how certain and accessible it is</td></tr>
  </tbody>
</table></figure>
"""
    + inline_cta("If you or your ex has received money from family, getting clear on how it will be treated early can prevent months of back-and-forth.")
    + f"""
<h2 id="what-courts-weigh">What decides how much weight it carries</h2>
<p>There is no formula. When parties cannot agree, the court looks at contributions (financial and non-financial, including home-making and parenting), then at future needs, such as age, health, earning capacity and care of children, and then asks whether the result is just and equitable. Courts commonly consider:</p>
<ul>
<li><strong>Size:</strong> a modest inheritance used for living costs has little lasting effect, while a very large sum is more likely to be treated as a distinct contribution.</li>
<li><strong>Timing:</strong> when it was received compared with the length of the relationship.</li>
<li><strong>Treatment:</strong> was it kept in a sole account, or put towards a shared home or investment?</li>
<li><strong>Length of the relationship:</strong> in a long relationship, contributions tend to merge over time.</li>
<li><strong>Needs:</strong> who will care for children and who has less earning capacity going forward.</li>
</ul>
<p>The Australian Institute of Family Studies, {cite('aifs')}, publishes research on how separating families divide property, and shows that most do so by agreement, not by court judgment. De facto couples are covered by equivalent provisions, as explained in our <a href="/de-facto-relationships-guide/">de facto relationships guide</a>.</p>
"""
    + inline_cta("Every case turns on its own facts. A mediator can help you explain yours clearly, and hear your ex's, before positions harden.")
    + f"""
<h2 id="before-or-during">Received before, during or after the relationship</h2>
<p>Timing changes the analysis. An inheritance received <em>before</em> the relationship is generally regarded as an initial contribution by that person. In a long relationship, its significance often fades as both partners contribute, while in a short relationship it tends to be more visible in the outcome.</p>
<p>An inheritance received <em>during</em> the relationship is a contribution made partway through. The court looks at what happened to it. If it paid for a family holiday it has largely gone; if it paid off the mortgage, it sits in the home. An inheritance received <em>after separation but before settlement</em> is still part of the pool at the time of settlement, but the court may give it greater weight as a contribution by the recipient, or treat it as relevant to future needs. Our <a href="/property-settlement-after-separation/">property settlement after separation</a> guide explains why it is wise not to leave settlement open for long.</p>
<figure class="tbl"><table><caption>Timing and typical significance (general guide only)</caption>
  <thead><tr><th>When received</th><th>Short relationship</th><th>Long relationship</th></tr></thead>
  <tbody>
    <tr><td>Before the relationship</td><td>Often significant to the recipient</td><td>Weight usually reduces over time</td></tr>
    <tr><td>During the relationship</td><td>Significant if kept identifiable</td><td>Often blended into the shared assets</td></tr>
    <tr><td>After separation, before settlement</td><td>Included; weight varies</td><td>Included; weight varies</td></tr>
  </tbody>
</table></figure>
"""
    + inline_cta("The date money arrived can change how it is treated. Book a free consultation to talk through your timeline in confidence.")
    + f"""
<h2 id="mixed-into-assets">When inherited money was mixed into the family home</h2>
<p>This is the most common scenario: a parent dies, you receive $150,000, and it goes into the mortgage. Years later the relationship ends. The money is no longer separate. It has become part of a shared asset, and the home is valued as one item in the pool.</p>
<p>That does not wipe out the recipient's contribution. The court (or the parties) can still recognise that a defined amount came from one side, through a larger percentage, or by treating part of the home's equity as originating from the inheritance. Keeping records matters: bank statements showing the deposit, the will or estate distribution statement, and the loan balance before and after. If you are planning a <a href="/buying-out-your-ex-family-home-australia/">buy-out of the family home</a>, an inheritance contribution can be built into the payout figure.</p>
"""
    + inline_cta("Good records make negotiation faster. We can help you work out what documents to gather before your first session.")
    + f"""
<h2 id="expected-inheritance">Inheritances you haven't received yet</h2>
<p>A parent's will can be changed at any time, and a person is alive until they are not. For these reasons, an <strong>expected</strong> inheritance is not property and is generally not divided. However, it may be considered a "financial resource" when assessing future needs, particularly if the parent is elderly, unwell and the inheritance is very likely.</p>
<p>It can also matter for spousal maintenance. Our <a href="/spousal-maintenance-guide/">spousal maintenance guide</a> explains how resources and earning capacity are weighed. If an inheritance arrives shortly after the settlement is finalised, the order generally stands, which is another reason a clear, final agreement is valuable.</p>
"""
    + inline_cta("Uncertainty about future money is a common source of conflict. A written agreement can address it directly, so nobody is left guessing.")
    + f"""
<h2 id="trusts-estates">Trusts, wills and estates that are still open</h2>
<p>Estates can take many months to administer. An interest in an estate that is not yet distributed may be valued as an asset, or the parties may agree to wait and deal with it by a defined mechanism once funds are released. Family trusts add another layer: whether you are a beneficiary with real control or only a discretionary object makes a large difference to valuation. If the other side alleges an interest in a trust or business, get specialist advice. You may also find our guide on <a href="/estate-inheritance-dispute-mediation/">estate and inheritance dispute mediation</a> useful where family members disagree about the estate itself.</p>
<p>If you are worried about assets being hidden or moved, see our guide to <a href="/hiding-assets-in-divorce/">hiding assets in divorce</a>. Both parties have a duty of full and frank financial disclosure, set out by the {cite('fcfcoa_disclosure')}.</p>
"""
    + inline_cta("Complex estates and trusts are exactly where a clear, structured process saves time. Talk to us about how mediation handles them.")
    + f"""
<h2 id="mediation-approach">Settling inheritance questions through mediation</h2>
<p>Inheritance disputes are rarely only about money. They carry grief, family loyalty and a sense of fairness. A formal court process can make those feelings worse, and a judge's decision is not easy to predict. Mediation gives you something different: a neutral, confidential setting where you decide the weight of the contribution together, test options with your lawyers' advice, and record the result.</p>
<p>Typical outcomes include recognising the inheritance through a percentage adjustment, ring-fencing a specific amount, or keeping a specific asset out of the division entirely. The agreement can then be formalised as <a href="/consent-orders-explained/">consent orders</a>. Mediation may not be suitable where there is family violence or one party refuses to disclose, in which case exemptions apply and legal advice should come first. Court has its place, but rarely the best place to start.</p>
"""
    + inline_cta("Ready to talk it through? Book a free consultation and we'll explain how a mediated settlement would work for your family.")
    ,
    [
        ("Is my inheritance safe from my ex after separation?",
         "Not automatically. An inheritance you have received is part of the pool, but it is usually weighed as your contribution, so it often has significant protection. How much depends on its size, timing and what you did with it."),
        ("What if I inherited money before we got together?",
         "It is generally treated as an initial contribution by you. In a short relationship it tends to carry substantial weight, and in a long relationship its weight can reduce as both partners contribute over time."),
        ("Does my ex get a share of an inheritance I'm still expecting?",
         "Generally no, because it is not yet property. It may be considered as a financial resource affecting future needs, particularly where the inheritance is imminent and certain."),
        ("What happens if inherited money went into the family home?",
         "The money becomes part of a shared asset, but your contribution can still be recognised through a larger share or an adjustment to the buy-out figure. Keep records of the deposit."),
        ("Can an inheritance be kept out of the settlement by agreement?",
         "Yes. You and your ex can agree to exclude an asset or fix a specific split, provided the agreement is recorded properly, as consent orders or a binding financial agreement, with legal advice."),
    ],
    [
        ("what-is-in-the-property-pool",           "What's in the Property Pool?"),
        ("property-settlement-after-separation",   "Property Settlement After Separation"),
        ("estate-inheritance-dispute-mediation",   "Estate &amp; Inheritance Dispute Mediation"),
        ("hiding-assets-in-divorce",               "Hiding Assets in Divorce"),
        ("consent-orders-explained",               "Consent Orders Explained"),
        ("spousal-maintenance-guide",              "Spousal Maintenance in Australia"),
    ],
    8
)
