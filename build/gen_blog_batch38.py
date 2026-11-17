"""gen_blog_batch38.py: tax-on-property-settlement-australia, centrelink-after-separation.
Facts checked against Income Tax Assessment Act 1997 (Cth) Subdiv 126-A,
Family Law Act 1975, Services Australia guidance (Nov 2026)."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, key_takeaway, inline_cta, callout
from authority_sources import cite

# ── POST 1: tax-on-property-settlement-australia ─────────────────────────────

tax_body = (
  key_takeaway("When property is transferred between separating spouses under a court order or "
               "binding financial agreement, CGT rollover relief applies automatically and stamp "
               "duty is exempt in every state and territory. A deal that ignores tax can turn an "
               "equal split into one worth tens of thousands less for the wrong side.")
  + f"""
<h2 id="why-tax-matters">Why tax matters in property settlement</h2>
<p>Most separating couples focus on the gross value of assets — the house is worth $1.2 million, the super balance is $400,000, the share portfolio is $180,000. But a dollar of equity in the family home is not the same as a dollar locked in superannuation or a dollar sitting in shares with a large unrealised capital gain.</p>
<p>Tax changes the after-tax value of every asset in the pool. The {cite('ato')} administers the rules that determine whether a property transfer triggers capital gains tax, and each state and territory decides whether stamp duty applies. Getting these wrong can cost $20,000 to $80,000 on a typical settlement — money that neither side intended to give to the government.</p>
<p>This guide covers the main tax rules that apply when you divide property after separation in Australia. It is general information, not tax or legal advice. Always get advice specific to your situation from a qualified tax professional before you finalise any agreement.</p>
"""
  + inline_cta("Want a property split that accounts for tax? Talk to us about mediation with financial input.")
  + f"""
<h2 id="cgt-rollover">CGT rollover relief on asset transfers</h2>
<p>Under Subdivision 126-A of the <em>Income Tax Assessment Act 1997</em>, when a CGT asset is transferred between spouses or former de facto partners as a result of a relationship breakdown, the transfer is automatically rolled over. That means:</p>
<ul>
  <li>No capital gains tax event is triggered at the time of transfer.</li>
  <li>The receiving spouse inherits the original cost base and acquisition date.</li>
  <li>CGT is deferred until the receiving spouse eventually sells or disposes of the asset.</li>
</ul>
<p>The rollover applies when the transfer happens because of:</p>
<ol>
  <li>a court order under the {cite('family_law_act')};</li>
  <li>a binding financial agreement (BFA) made under Part VIIIA of that Act; or</li>
  <li>an arbitral award under Division 4 of Part VIIIAB.</li>
</ol>
<p>This covers real property, shares, managed fund units, business assets and virtually any other CGT asset. The key requirement is that the transfer must be <strong>under a formal family law instrument</strong> — a handshake deal or an informal private sale does not qualify and can trigger a full CGT event.</p>
"""
  + inline_cta("Mediation leads to consent orders or a BFA — both qualify for CGT rollover. Book a free consultation.")
  + """
<h2 id="stamp-duty">Stamp duty exemptions by state</h2>
<p>Every Australian state and territory provides a stamp duty (transfer duty) exemption or concession for property transfers made under a family law order or financial agreement. The exemption generally covers transfers of real property, including the family home and investment properties.</p>
<figure class="tbl"><table><caption>Stamp duty position for family law property transfers (2026)</caption>
<thead><tr><th>State / Territory</th><th>Exemption</th><th>Key requirement</th></tr></thead>
<tbody>
<tr><td>New South Wales</td><td>Full exemption</td><td>Court order, consent orders or BFA</td></tr>
<tr><td>Victoria</td><td>Full exemption</td><td>Court order, consent orders or BFA</td></tr>
<tr><td>Queensland</td><td>Full exemption</td><td>Court order, consent orders or BFA</td></tr>
<tr><td>Western Australia</td><td>Full exemption</td><td>Court order, consent orders or BFA</td></tr>
<tr><td>South Australia</td><td>Full exemption</td><td>Court order, consent orders or BFA</td></tr>
<tr><td>Tasmania</td><td>Full exemption</td><td>Court order, consent orders or BFA</td></tr>
<tr><td>ACT</td><td>Full exemption</td><td>Court order, consent orders or BFA</td></tr>
<tr><td>Northern Territory</td><td>Full exemption</td><td>Court order, consent orders or BFA</td></tr>
</tbody></table></figure>
<p class="source-note">Summary of state/territory revenue legislation. Conditions vary — check your state's revenue office. General information only, not tax advice.</p>
<p>The critical point is the same as for CGT rollover: the transfer must be under a <strong>formal family law instrument</strong>. If you simply transfer a property by private agreement without court orders or a BFA, you may be liable for full stamp duty — potentially tens of thousands of dollars on a typical home.</p>
<p>This is one of the strongest practical reasons to formalise your agreement through consent orders or a binding financial agreement, both of which are natural outcomes of mediation.</p>
"""
  + inline_cta("Formalising your agreement saves stamp duty. We can help you reach one through mediation.")
  + """
<h2 id="main-residence">The main residence exemption</h2>
<p>The family home is usually the largest asset in the pool, and the main residence exemption means its sale is generally CGT-free. But separation introduces complexity.</p>
<p>If the home is sold as part of the settlement, the main residence exemption usually covers the entire gain, provided neither spouse used it to produce income (such as renting out a room) during the period of ownership.</p>
<p>If one spouse keeps the home and the other moves out, two rules interact:</p>
<ul>
  <li><strong>Absent owner rule.</strong> The spouse who moves out can continue to treat the home as their main residence for up to six years, provided it is not used to produce income. This can matter if they later need to claim the exemption on a share they retained.</li>
  <li><strong>Receiving spouse.</strong> If the home is transferred to the staying spouse under a family law order, the CGT rollover applies at the time of transfer. When that spouse eventually sells, they can usually claim the main residence exemption for the full period of ownership (including the period before the transfer).</li>
</ul>
<p>The exemption can be <strong>partial</strong> if the home was rented out for any period, used partly for business, or if either spouse claimed another property as their main residence at the same time. These situations need individual tax advice.</p>
"""
  + inline_cta("Not sure how the family home affects your tax position? Get clarity before you agree.")
  + """
<h2 id="super-splitting">Tax on superannuation splits</h2>
<p>Superannuation can be split between separating spouses under a family law order or BFA. The split itself is not a taxable event — there is no CGT, no income tax, and no contributions tax at the point of transfer.</p>
<p>What the receiving spouse does inherit is the <strong>tax components</strong> of the super — the tax-free and taxable portions. These components determine how the super will be taxed when it is eventually withdrawn, which depends on the receiving spouse's age and preservation status at that time.</p>
<p>Key points for mediation:</p>
<ul>
  <li>A dollar of super is not the same as a dollar of cash. Super is locked away until preservation age (currently 60 for most people) and taxed differently on withdrawal depending on the components.</li>
  <li>When comparing a super split against a cash or property offset, the after-tax, after-access value of super should be discounted to reflect these restrictions.</li>
  <li>Defined benefit super funds (common in government employment) have their own valuation rules and may not allow a simple percentage split.</li>
</ul>
"""
  + inline_cta("Super splitting is complex. Our mediators work with financial advisers to get it right.")
  + """
<h2 id="maintenance-tax">Tax treatment of spousal maintenance</h2>
<p>Spousal maintenance (sometimes called alimony) has a straightforward tax treatment in Australia:</p>
<ul>
  <li>It is <strong>not assessable income</strong> for the person receiving it.</li>
  <li>It is <strong>not tax-deductible</strong> for the person paying it.</li>
  <li>It does not need to be reported on either party's tax return.</li>
</ul>
<p>Child support has the same treatment — not taxable for the recipient and not deductible for the payer.</p>
<p>This means that when you are comparing a lump-sum property split against ongoing spousal maintenance, the maintenance payments do not create a tax burden for the recipient. However, the lump sum may come from the sale of an asset that does trigger CGT (such as an investment property), so the source of the payment matters.</p>
"""
  + inline_cta("Weighing a lump sum against ongoing payments? Mediation lets you explore every option.")
  + f"""
<h2 id="mediation-advantage">Why mediation produces better tax outcomes</h2>
<p>A court can divide the property pool, but it is not required to optimise the tax consequences for either party. In mediation, both sides can work with their own financial advisers — or a jointly appointed one — to structure the split in a way that minimises the total tax paid by both.</p>
<p>Common strategies that emerge from tax-aware mediation include:</p>
<ul>
  <li><strong>Choosing which assets to transfer and which to sell.</strong> Transferring a low-cost-base investment property (which would trigger a large CGT bill on sale) to the spouse who plans to hold it, while offsetting with cash from other assets.</li>
  <li><strong>Timing the settlement.</strong> Completing the transfer in a financial year where one or both parties have lower income can reduce CGT on any assets that must be sold.</li>
  <li><strong>Using the main residence exemption strategically.</strong> Agreeing that the spouse who keeps the home will not rent it out, preserving the full exemption for a future sale.</li>
  <li><strong>Splitting super efficiently.</strong> Taking account of the tax components in each fund so the receiving spouse does not inherit a disproportionately taxable balance.</li>
</ul>
<p>The {cite('moneysmart_separation')} guide is a good starting point for understanding the financial decisions involved. Our mediators routinely help couples work through these scenarios with the support of independent financial professionals.</p>
"""
  + inline_cta("A tax-aware settlement can save both sides tens of thousands. Book a free consultation.")
  + """
<h2 id="common-mistakes">Common tax mistakes to avoid</h2>
<p>These are the errors that most often cost separating couples money:</p>
<ol>
  <li><strong>Transferring property without a court order or BFA.</strong> An informal transfer does not qualify for CGT rollover or stamp duty exemption. Formalising through consent orders costs a few hundred dollars; not doing so can cost tens of thousands.</li>
  <li><strong>Ignoring the cost base of shares or investment property.</strong> The person who receives a low-cost-base asset inherits a future tax liability. If you agree to take $200,000 in shares with a cost base of $80,000, you are really receiving $200,000 minus future CGT on $120,000 of gain.</li>
  <li><strong>Forgetting about the Medicare levy surcharge.</strong> After separation, your individual income determines whether you need private health cover to avoid the surcharge. This can be a surprise in the first tax return after separation.</li>
  <li><strong>Not updating tax file number declarations.</strong> If you claimed the tax-free threshold based on a spouse's income, your withholding may need to change.</li>
  <li><strong>Treating super and cash as equivalent.</strong> Taking $100,000 in super instead of $100,000 in cash means you cannot access the money until preservation age, and it will be taxed on withdrawal. The effective value is lower.</li>
</ol>
<p>Each of these mistakes is avoidable with professional advice. A mediator cannot give tax advice, but good mediation creates the space for both parties to get advice and bring it back to the table before anything is finalised.</p>
"""
  + inline_cta("Avoid costly tax mistakes. Start with a free, confidential mediation consultation.")
)

tax_qa = [
 ("Do I have to pay capital gains tax when transferring property to my ex?",
  "Not if the transfer is made under a court order, consent orders or a binding financial agreement under the Family Law Act. The CGT rollover in Subdivision 126-A of the Income Tax Assessment Act 1997 applies automatically, deferring the tax until the receiving spouse eventually sells."),
 ("Is stamp duty payable on a family law property transfer?",
  "No. Every Australian state and territory exempts property transfers made under a family law court order or binding financial agreement from stamp duty. An informal private transfer without a formal instrument may not qualify, so it is important to formalise your agreement."),
 ("What happens to the cost base when an asset is rolled over?",
  "The receiving spouse inherits the original cost base and acquisition date. When they eventually sell the asset, their capital gain or loss is calculated from the original cost base, not the value at the time of transfer."),
 ("Is spousal maintenance taxable in Australia?",
  "No. Spousal maintenance is not assessable income for the recipient and is not tax-deductible for the payer. The same applies to child support payments."),
 ("Should I get independent tax advice before agreeing to a property split?",
  "Yes. A mediator helps you negotiate but cannot give tax advice. Getting advice from a qualified accountant or tax professional before you finalise ensures you understand the after-tax value of what you are agreeing to."),
]

post(
  "tax-on-property-settlement-australia",
  "Tax on Property Settlement in Australia",
  "How CGT rollover relief, stamp duty exemptions and other tax rules apply when you divide property after separation — and why tax-aware mediation matters.",
  "Property",
  "Tax on property settlement <em>explained</em>",
  "A property split that looks equal on paper can leave one side with a much larger tax bill. Understanding CGT rollover, stamp duty exemptions and super splitting before you agree is the difference between a fair deal and a costly mistake.",
  [("why-tax-matters", "Why tax matters in property settlement"),
   ("cgt-rollover", "CGT rollover relief on asset transfers"),
   ("stamp-duty", "Stamp duty exemptions by state"),
   ("main-residence", "The main residence exemption"),
   ("super-splitting", "Tax on superannuation splits"),
   ("maintenance-tax", "Tax treatment of spousal maintenance"),
   ("mediation-advantage", "Why mediation produces better tax outcomes"),
   ("common-mistakes", "Common tax mistakes to avoid")],
  tax_body, tax_qa,
  [("property-settlement-after-separation", "Property Settlement After Separation"),
   ("buying-out-your-ex-family-home-australia", "Buying Out Your Ex's Share of the Home"),
   ("superannuation-and-divorce", "Superannuation and Divorce"),
   ("what-is-in-the-property-pool", "What's in the Property Pool?"),
   ("property-settlement-mediation-guide", "Property Settlement Mediation Guide"),
   ("consent-orders-explained", "Consent Orders Explained")],
  read_min=9,
)
print("tax-on-property-settlement-australia built")


# ── POST 2: centrelink-after-separation ──────────────────────────────────────

cl_body = (
  key_takeaway("You must tell Centrelink within 14 days of separating. Your payments are then "
               "assessed on your income alone, which often means higher rates and new entitlements "
               "like Parenting Payment (Single) and Family Tax Benefit Part B. Understanding what "
               "changes helps you plan finances and negotiate in mediation from a position of knowledge.")
  + f"""
<h2 id="when-to-notify">When and how to notify Centrelink</h2>
<p>Under social security law, you must tell {cite('services_australia_cs')} about a change in your relationship status within <strong>14 days</strong>. Failing to notify can lead to overpayments that Centrelink will recover, sometimes with penalties.</p>
<p>You can update your status:</p>
<ul>
  <li><strong>Online</strong> through your myGov account linked to Centrelink — this is the fastest method.</li>
  <li><strong>By phone</strong> on the Families line (136 150) or the general line (132 850).</li>
  <li><strong>In person</strong> at a Services Australia service centre.</li>
</ul>
<p>If you are <strong>separated under one roof</strong> — still living in the same house but no longer in a relationship — Centrelink recognises this, but you will need to provide evidence. This can include statutory declarations, separate finances, sleeping in different rooms and no longer sharing meals or social activities as a couple. Our guide on <a href="/should-i-move-out-of-the-family-home/">whether to move out of the family home</a> covers the practical considerations.</p>
"""
  + inline_cta("Need help planning the financial side of separation? Talk to us — the first consultation is free.")
  + """
<h2 id="single-parent-payment">Parenting Payment (Single)</h2>
<p>If you are the primary carer of at least one child under 14, you may qualify for Parenting Payment (Single) — one of the highest regular Centrelink payments. It replaces any partnered payment you were receiving and has a more generous income test.</p>
<p>Key points:</p>
<ul>
  <li>You must have at least 35% care of a dependent child under 14.</li>
  <li>The income-free area is higher than for partnered payments, so you can earn more before your payment reduces.</li>
  <li>If you were on Parenting Payment (Partnered), your rate will generally increase after separation.</li>
  <li>If you were not receiving any payment, you may now qualify.</li>
</ul>
<p>The payment rate changes with indexation. Check the Services Australia website for the current fortnightly rate. As a rough guide, a single parent with one or two children can receive a base rate of around $900 to $1,000 per fortnight before the income test applies, though this changes with indexation and individual circumstances.</p>
"""
  + inline_cta("Understanding your entitlements helps you negotiate. Book a free mediation consultation.")
  + """
<h2 id="family-tax-benefit">Family Tax Benefit changes</h2>
<p>Family Tax Benefit (FTB) is split into two parts, and both change after separation:</p>
<figure class="tbl"><table><caption>How FTB changes after separation</caption>
<thead><tr><th>Payment</th><th>Before separation</th><th>After separation</th></tr></thead>
<tbody>
<tr><td>FTB Part A</td><td>Assessed on combined family income</td><td>Assessed on your individual income — usually means a higher payment</td></tr>
<tr><td>FTB Part B</td><td>Income-tested on the lower earner; not paid if the lower earner earns above the threshold</td><td>Most single parents qualify automatically (primary income earner test does not apply)</td></tr>
<tr><td>Shared care</td><td>One parent claims for all children</td><td>Each parent claims for the children in their care; must have at least 35% care to receive FTB for a child</td></tr>
<tr><td>Maintenance Income Test</td><td>Does not apply</td><td>Child support received above the free area can reduce FTB Part A</td></tr>
</tbody></table></figure>
<p><strong>Shared care percentages matter.</strong> If you have 50/50 shared care, both parents can claim FTB for the children in their care during their time. If the split is 65/35, the parent with 65% care receives a larger share of FTB. These percentages are determined by the actual care arrangement, which is exactly the kind of detail that mediation helps parents agree on.</p>
"""
  + inline_cta("Care arrangements affect your payments. Mediation helps you agree on a plan that works for everyone.")
  + """
<h2 id="child-care-subsidy">Child Care Subsidy after separation</h2>
<p>The Child Care Subsidy (CCS) is assessed on your individual income and activity level after separation. Because your household income drops to a single income, the subsidy percentage usually <strong>increases</strong>.</p>
<p>Both separated parents can claim the subsidy for sessions of child care during their care time. The key requirements are:</p>
<ul>
  <li>You meet the activity test (work, study, volunteering or looking for work) for the hours of care claimed.</li>
  <li>You use an approved child care service.</li>
  <li>The child is not yet in secondary school.</li>
</ul>
<p>If you are receiving an income support payment such as Parenting Payment (Single), you are generally treated as meeting the activity test for a minimum number of hours. This can make a significant difference to your out-of-pocket child care costs in the first months after separation.</p>
"""
  + inline_cta("Child care costs are a real concern after separation. We can help you plan.")
  + f"""
<h2 id="child-support-link">How child support interacts with Centrelink</h2>
<p>Child support and Centrelink are closely linked. When you separate and have children, {cite('services_australia_cs')} handles both systems, and what happens in one affects the other.</p>
<p>The main interactions are:</p>
<ul>
  <li><strong>Maintenance Income Test (MIT).</strong> Child support you receive (whether through Services Australia collection or private collection) can reduce your FTB Part A once it exceeds the Maintenance Income Free Area. The more child support you receive, the more your FTB Part A may reduce.</li>
  <li><strong>Child support assessment.</strong> The child support formula uses each parent's adjusted taxable income. After separation, this is your individual income, which may differ significantly from what it was as a couple.</li>
  <li><strong>Care percentage.</strong> The percentage of care each parent provides affects both the child support calculation and FTB entitlements. A change in care arrangements, agreed through mediation, flows through to both systems.</li>
</ul>
<p>Because these systems interact, an agreement reached in mediation about care arrangements, income and child support has knock-on effects for Centrelink payments. Understanding these connections before you agree helps avoid surprises. Our <a href="/child-support-guide/">child support guide</a> explains the formula in detail.</p>
"""
  + inline_cta("Child support and Centrelink are connected. Get informed before you negotiate.")
  + f"""
<h2 id="health-care-card">Health Care Card and concession cards</h2>
<p>After separation, your individual income determines whether you qualify for a Health Care Card (HCC) or other concession cards. Many newly separated parents qualify, especially if they were not working or were the lower earner during the relationship.</p>
<p>A Health Care Card provides:</p>
<ul>
  <li>Cheaper prescription medicines under the Pharmaceutical Benefits Scheme.</li>
  <li>Bulk-billed GP visits (at the doctor's discretion).</li>
  <li>Utility bill concessions (varies by state).</li>
  <li>Reduced public transport fares in some states.</li>
  <li>Waived or reduced fees for some government services.</li>
</ul>
<p>If you receive Parenting Payment (Single), JobSeeker Payment or certain other income support payments, you are automatically issued a concession card. If you are not on a payment but have a low income, you may qualify for a Low Income Health Care Card.</p>
<p>The {cite('frc')} can help you find local services and support during separation, including financial counselling.</p>
"""
  + inline_cta("Separation is financially stressful. We can help you plan your next steps.")
  + f"""
<h2 id="mediation-role">How mediation helps with financial planning</h2>
<p>Centrelink entitlements are not something a mediator decides, but they are part of the financial picture that shapes every mediation about parenting and property. When both parents understand their payments, care percentages and child support obligations before they sit down at the table, the conversation is more productive.</p>
<p>Mediation helps by:</p>
<ul>
  <li><strong>Clarifying care arrangements.</strong> The percentage of care each parent provides drives FTB, CCS and child support calculations. Agreeing on a clear, workable parenting plan in mediation flows through to every payment.</li>
  <li><strong>Aligning property and income.</strong> A property settlement that leaves one parent asset-rich but income-poor may affect their Centrelink eligibility. Mediation lets both sides factor this in.</li>
  <li><strong>Reducing conflict over money.</strong> When parents understand what each of them will receive from Centrelink and child support, there is less room for resentment or suspicion.</li>
  <li><strong>Creating binding agreements.</strong> Care arrangements agreed in mediation can be formalised as a parenting plan or through consent orders, giving both parents and Centrelink certainty.</li>
</ul>
<p>The {cite('moneysmart_separation')} guide is a useful resource for understanding the full financial picture. If you need free financial counselling, the <a href="https://ndh.org.au/" target="_blank" rel="noopener">National Debt Helpline</a> (1800 007 007) can help.</p>
<p>If you are experiencing family and domestic violence, confidential support is available through 1800RESPECT (1800 737 732). If you are in immediate danger, call 000.</p>
"""
  + inline_cta("Ready to plan your financial future? Book a free, confidential mediation consultation.")
)

cl_qa = [
 ("How soon do I have to tell Centrelink about separation?",
  "You must notify Centrelink within 14 days of the date of separation. You can do this online through myGov, by phone, or in person at a service centre. Failing to notify can lead to overpayments that will be recovered."),
 ("Can I get Centrelink payments if we are separated under one roof?",
  "Yes. Centrelink recognises separation under one roof, but you will need to provide evidence such as statutory declarations, proof of separate finances and evidence that you are no longer living as a couple."),
 ("How does shared care affect my Family Tax Benefit?",
  "You need at least 35% care of a child to receive Family Tax Benefit for that child. If you have 50/50 care, both parents can claim FTB. The percentage of care also affects the amount paid to each parent."),
 ("Does child support count as income for Centrelink?",
  "Child support is not counted as income for income-tested Centrelink payments like Parenting Payment. However, child support you receive can reduce your Family Tax Benefit Part A through the Maintenance Income Test if it exceeds the free area."),
 ("Will my Centrelink payments increase after separation?",
  "In most cases, yes. Your payments are assessed on your individual income rather than combined family income, which usually results in higher payment rates and new entitlements such as Parenting Payment (Single) and FTB Part B."),
]

post(
  "centrelink-after-separation",
  "Centrelink After Separation: Your Payments",
  "How separation changes your Centrelink payments, Family Tax Benefit, Child Care Subsidy and single parent pension. What to do, what changes and when.",
  "Separation",
  "Centrelink after separation <em>guide</em>",
  "When a relationship ends your Centrelink entitlements change — often for the better. Knowing what you can claim, how shared care affects payments and what to report helps you plan finances and negotiate in mediation from a position of knowledge.",
  [("when-to-notify", "When and how to notify Centrelink"),
   ("single-parent-payment", "Parenting Payment (Single)"),
   ("family-tax-benefit", "Family Tax Benefit changes"),
   ("child-care-subsidy", "Child Care Subsidy after separation"),
   ("child-support-link", "How child support interacts with Centrelink"),
   ("health-care-card", "Health Care Card and concession cards"),
   ("mediation-role", "How mediation helps with financial planning")],
  cl_body, cl_qa,
  [("separation-guide", "Separation Guide"),
   ("child-support-guide", "Child Support in Australia"),
   ("who-pays-bills-during-separation", "Who Pays Bills During Separation"),
   ("should-i-move-out-of-the-family-home", "Should I Move Out of the Family Home?"),
   ("spousal-maintenance-guide", "Spousal Maintenance Guide"),
   ("cost-of-divorce-in-australia", "Cost of Divorce in Australia")],
  read_min=8,
)
print("centrelink-after-separation built")
