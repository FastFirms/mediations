"""gen_blog_batch41.py: two estate-dispute cornerstones.
1. notional-estate-nsw
2. superannuation-death-benefit-disputes
LEGAL REVIEW REQUIRED before merge: official sources (NSW legislation, AFCA, ATO) were
unreachable from the build environment on 28 Nov 2026, so statutory details are stated
from established law and must be checked by a lawyer."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, key_takeaway, inline_cta, callout
from authority_sources import cite

# ─────────────────────────────────────────────────────────────────────────────
# 1. Notional estate (NSW)
# ─────────────────────────────────────────────────────────────────────────────
body1 = (
  key_takeaway("In NSW, a court hearing a family provision claim can treat property that never passed through "
               "the will, such as a jointly owned home, superannuation paid directly to a nominee, or assets given "
               "away shortly before death, as part of the estate. This is called notional estate. It exists only "
               "in NSW, and claims must generally be made within 12 months of death.")
  + f"""
<h2 id="what-is">What is notional estate?</h2>
<p>When someone dies, most people assume the "estate" is whatever the will deals with: the house in their sole name, bank accounts, shares. In practice, a large share of many people's wealth never passes through the will at all. A home owned as joint tenants passes automatically to the surviving owner. Superannuation is paid by the fund trustee, often straight to a nominated beneficiary. Assets may have been gifted or transferred to a family trust before death.</p>
<p>In most Australian states, those assets are simply out of reach of a family provision claim. New South Wales is different. Under Chapter 3 of the {cite('nsw_succession')}, the Supreme Court can make an order <strong>designating property outside the estate as "notional estate"</strong>, so it can be used to make provision for an eligible person who has been left without adequate provision. NSW is the only Australian jurisdiction with a regime this broad.</p>
<p>If you are new to family provision claims, start with our guide to <a href="/contesting-a-will-nsw/">contesting a will in NSW</a>, then come back to this one.</p>
"""
  + inline_cta("Worried that most of the estate sits outside the will? Talk to us about resolving it by agreement.")
  + """
<h2 id="what-property">What property can be caught</h2>
<p>Notional estate is built around the idea of a <strong>"relevant property transaction"</strong>: broadly, something the deceased did, or failed to do, that resulted in property being held by someone else or subject to someone else's interest, without full value being given in return. Common examples include:</p>
<figure class="tbl"><table><caption>Property that may be designated as notional estate in NSW</caption>
<thead><tr><th>Type of property</th><th>Why it sits outside the will</th><th>How notional estate can reach it</th></tr></thead>
<tbody>
<tr><td>Home or account held as joint tenants</td><td>Passes automatically to the surviving joint owner</td><td>The deceased's share (severed interest) can be designated</td></tr>
<tr><td>Superannuation paid to a nominee</td><td>Paid by the fund trustee, not the executor</td><td>The benefit paid on or after death can be designated</td></tr>
<tr><td>Life insurance paid to a nominated beneficiary</td><td>Paid directly under the policy</td><td>Can be designated in the same way</td></tr>
<tr><td>Gifts or transfers before death</td><td>Already given away</td><td>Only within strict time limits (see below)</td></tr>
<tr><td>Assets moved into a family trust or company</td><td>Owned by the trust or company</td><td>May be caught if the deceased had effective control or made the transfer within the time limits</td></tr>
</tbody></table></figure>
<p class="source-note">General information only. Whether a particular asset can be designated depends on the facts and the court's discretion. Get advice from an estates lawyer.</p>
"""
  + inline_cta("Not sure what counts? A mediator can help everyone see the full picture before positions harden.")
  + """
<h2 id="time-limits">The look-back periods for gifts and transfers</h2>
<p>Lifetime transactions are not caught indefinitely. Broadly, a transaction can be treated as notional estate if it:</p>
<ul>
  <li>took effect within <strong>three years before death</strong> and was entered into with the intention of denying or limiting provision for a person who could make a family provision claim;</li>
  <li>took effect within <strong>one year before death</strong> at a time when the deceased had a moral obligation to provide for an eligible person that was substantially greater than any obligation to the person who received the property; or</li>
  <li>takes effect <strong>on or after death</strong>, which is how jointly held property, superannuation and life insurance are usually caught.</li>
</ul>
<p>Separately, a family provision claim in NSW must generally be filed within <strong>12 months of the date of death</strong>. The court can allow a late claim if there is sufficient cause, but you should not rely on that.</p>
"""
  + inline_cta("Close to the 12-month deadline? Mediation can run alongside the court timetable.")
  + f"""
<h2 id="court-limits">The court's limits and the risk of costs</h2>
<p>Notional estate is a last resort. Before designating property, the court must be satisfied that the actual estate is not enough to make the provision it considers appropriate, and it must weigh fairness to the people who hold the property, including the importance of not interfering with reasonable expectations about property and the substantial justice of the case.</p>
<p>That matters in practice because notional estate arguments make litigation longer, more complex and more expensive. Costs in NSW family provision cases are often ordered to come out of the estate, which means a contested hearing can shrink the very pool everyone is arguing about. The {cite('nsw_supreme_court')} requires family provision matters to go to mediation before a final hearing in most cases.</p>
"""
  + inline_cta("Want to settle before costs eat into the estate? Book a free, confidential consultation.")
  + """
<h2 id="mediation">How mediation helps with notional estate claims</h2>
<p>Notional estate disputes often set a surviving spouse, who received the home by joint tenancy, against adult children from an earlier relationship. Emotions run high and every option the court has is blunt. Mediation gives the family room to agree something more precise.</p>
<ul>
  <li><strong>Everything can go on the table.</strong> The parties can agree on outcomes involving jointly held property, super or trust assets without waiting for the court to decide whether to designate them.</li>
  <li><strong>Creative terms.</strong> A life interest in the home, staged payments, or a sale with a split of proceeds can all be agreed, where a court would usually order a lump sum.</li>
  <li><strong>Costs stay contained.</strong> Settling early preserves more of the estate for the family.</li>
  <li><strong>Relationships survive.</strong> A confidential conversation is gentler on grieving families than a public hearing.</li>
</ul>
"""
  + callout("A worked example (illustrative only)",
            "Margaret dies leaving a will that gives her small estate of about $120,000 to her second husband, Ray. Their home, "
            "worth about $1.4 million, was held as joint tenants and passes to Ray automatically. Her daughter from her first "
            "marriage, who cares for a child with a disability, files a family provision claim and asks the court to designate "
            "Margaret's half of the home as notional estate. At mediation, the parties agree Ray keeps the home for life, with "
            "a payment to the daughter now from the estate and a further share of the sale proceeds when the home is eventually "
            "sold. This is a composite scenario, not a real client, and the figures are for illustration only.")
  + inline_cta("Facing a claim like this? Talk to an accredited estate mediator.")
  + """
<h2 id="next-steps">What to do next</h2>
<p><strong>If you are thinking of making a claim:</strong> diarise the 12-month deadline from the date of death, gather what you know about jointly held property, super and gifts, and get advice from an estates lawyer early.</p>
<p><strong>If you hold property that may be designated:</strong> keep records of how and when you acquired it, and what you contributed. Don't sell or transfer it without advice once a claim is in prospect.</p>
<p><strong>Executors:</strong> you will usually need to hold off distributing the estate while a claim is possible. See our guide to <a href="/executor-dispute-mediation/">executor disputes</a>.</p>
<p>Our <a href="/estate-dispute-mediation/">estate dispute mediation</a> service works alongside each party's own lawyer.</p>
"""
)

qa1 = [
 ("What is notional estate in NSW?",
  "Notional estate is property outside a deceased person's estate, such as jointly held property, superannuation paid to a nominee, or certain gifts made before death, that the NSW Supreme Court can treat as part of the estate in order to make provision for someone in a family provision claim."),
 ("Does notional estate apply in other states?",
  "No. Notional estate is unique to NSW. Other states have much narrower rules, so in most cases only property that passes under the will or intestacy is available for a family provision claim."),
 ("Can jointly owned property be claimed after death?",
  "In NSW, the deceased's interest in property held as joint tenants can be designated as notional estate, even though it passed automatically to the surviving owner. The court decides whether this is appropriate in each case."),
 ("Is superannuation part of notional estate?",
  "Superannuation paid directly to a nominated beneficiary does not form part of the actual estate, but in NSW it can be designated as notional estate in a family provision claim."),
 ("How long do I have to make a family provision claim in NSW?",
  "Generally 12 months from the date of death. The court can extend the time if there is sufficient cause, but late claims are not guaranteed."),
 ("Do notional estate claims go to mediation?",
  "Most family provision matters in the NSW Supreme Court are referred to mediation before a final hearing, and many settle there. Private mediation can also happen earlier, before proceedings are filed."),
]

post(
  "notional-estate-nsw",
  "Notional Estate in NSW: What Can Be Claimed",
  "How NSW notional estate rules let a family provision claim reach jointly held property, super and gifts made before death, and how mediation resolves it.",
  "Estate Disputes",
  "Notional estate <em>in NSW</em>",
  "In NSW, a family provision claim can reach property that never passed through the will. Here is what notional estate is, what it can catch, and how families resolve these claims without a long hearing.",
  [("what-is", "What is notional estate?"),
   ("what-property", "What property can be caught"),
   ("time-limits", "The look-back periods"),
   ("court-limits", "The court's limits and costs"),
   ("mediation", "How mediation helps"),
   ("next-steps", "What to do next")],
  body1, qa1,
  [("contesting-a-will-nsw", "Contesting a Will in NSW"),
   ("estate-dispute-mediation", "Estate Dispute Mediation"),
   ("executor-dispute-mediation", "Executor Disputes"),
   ("superannuation-death-benefit-disputes", "Super Death Benefit Disputes"),
   ("estate-inheritance-dispute-mediation", "Estate & Inheritance Mediation"),
   ("contesting-a-will", "Contesting a Will")],
  read_min=9,
)

# ─────────────────────────────────────────────────────────────────────────────
# 2. Superannuation death benefit disputes
# ─────────────────────────────────────────────────────────────────────────────
body2 = (
  key_takeaway("Superannuation does not automatically form part of a person's estate. Unless there is a valid binding "
               "nomination, the fund trustee decides who receives the death benefit, choosing among dependants and the "
               "estate. If you disagree with a proposed payment, object to the trustee within the time it gives you, and "
               "you may then complain to AFCA, which has strict time limits.")
  + f"""
<h2 id="not-in-will">Why super is not covered by the will</h2>
<p>For many families, superannuation is the largest asset after the home, and it is the one most often misunderstood. Super is held on trust by the fund's trustee. When a member dies, the trustee pays the death benefit under the fund's rules and superannuation law, not under the member's will. The will only controls super if the benefit is paid to the estate.</p>
<p>That is why disputes about super often look different from other estate disputes. The decision-maker is a trustee, not an executor or a court, and the complaints process runs through the {cite('afca')} rather than the Supreme Court.</p>
"""
  + inline_cta("Family disagreeing about a super payout? Talk to us confidentially about your options.")
  + f"""
<h2 id="who-can-receive">Who can receive a super death benefit</h2>
<p>Under the {cite('sis_act')} and its regulations, a death benefit can generally be paid only to:</p>
<ul>
  <li>the member's <strong>dependants</strong>: a spouse (including a de facto partner), children of any age, a person who was financially dependent on the member, or a person in an <em>interdependency relationship</em> with the member; or</li>
  <li>the member's <strong>legal personal representative</strong> (the executor or administrator), so the benefit is paid into the estate and distributed under the will or intestacy rules.</li>
</ul>
<p>The tax treatment depends on who receives it. Payments to dependants for tax purposes, such as a spouse or a minor child, are generally tax-free, while adult children who were not financially dependent may pay tax on part of the benefit. The {cite('ato_death_benefits')} explains the rules.</p>
"""
  + inline_cta("Unsure whether you count as a dependant? An early conversation can save months of uncertainty.")
  + """
<h2 id="nominations">Binding, non-binding and no nomination</h2>
<figure class="tbl"><table><caption>How the type of nomination affects who decides</caption>
<thead><tr><th>Situation</th><th>Who decides</th><th>Room for dispute</th></tr></thead>
<tbody>
<tr><td>Valid binding death benefit nomination</td><td>The trustee must generally follow it</td><td>Limited, usually about whether the nomination is valid (correct form, witnesses, not lapsed, eligible nominee)</td></tr>
<tr><td>Non-binding (preferred) nomination</td><td>The trustee, taking the wishes into account</td><td>Significant: other dependants can argue they should share</td></tr>
<tr><td>No nomination</td><td>The trustee, under the fund rules</td><td>Significant: competing claims from spouse, children, the estate</td></tr>
<tr><td>Self-managed super fund (SMSF)</td><td>The remaining trustees, under the trust deed</td><td>Often high, especially in blended families where a new spouse controls the fund</td></tr>
</tbody></table></figure>
<p class="source-note">General information only. Binding nominations commonly lapse after three years unless they are non-lapsing; check the fund's rules.</p>
"""
  + inline_cta("Blended family and an SMSF? Mediation can stop a dispute between trustees becoming a court case.")
  + f"""
<h2 id="disputing">How to dispute a trustee's decision</h2>
<p>For an APRA-regulated fund, the usual path is:</p>
<ol>
  <li><strong>Lodge a claim with the fund</strong> as early as possible, explaining your relationship with the member and any financial dependence, with evidence.</li>
  <li><strong>Respond to the proposed decision.</strong> Trustees commonly notify potential beneficiaries of a proposed distribution and allow a period (often 28 days) to object. Put your objection in writing within that time.</li>
  <li><strong>Complain to AFCA.</strong> If you objected and the trustee confirms its decision, you can complain to the {cite('afca')}. Death benefit complaints have strict time limits, commonly 28 days from the trustee's notice of its final decision. If you miss them, AFCA may be unable to help.</li>
</ol>
<p>SMSF disputes are different: AFCA generally cannot hear them, and they usually end up in the state Supreme Court unless the parties agree. That makes early mediation especially valuable.</p>
"""
  + inline_cta("Received a trustee's proposed decision? Get advice quickly, and consider mediation alongside your objection.")
  + """
<h2 id="mediation">Where mediation fits</h2>
<p>A fund trustee cannot be ordered into family mediation, but most super disputes are really disputes between family members: a second spouse and adult children, separated parents of a minor child, or siblings arguing about who was "financially dependent". Mediation helps those people reach an agreed position, which can then be put to the trustee, or settled through the estate.</p>
<ul>
  <li><strong>Agree how the whole picture is shared.</strong> Super, the estate and jointly held assets can be considered together, so no one is fighting on three fronts at once.</li>
  <li><strong>Protect a grieving family.</strong> A confidential, structured conversation is gentler than formal objections and complaints.</li>
  <li><strong>Save time.</strong> Trustee and AFCA processes can take months. An agreement can shorten them.</li>
  <li><strong>Avoid court in SMSF disputes,</strong> where the alternative is often Supreme Court proceedings.</li>
</ul>
"""
  + callout("A worked example (illustrative only)",
            "David dies with about $600,000 in an industry super fund and no binding nomination. His de facto partner of four years "
            "and his two adult sons from his marriage all lodge claims. The trustee proposes paying everything to the partner; the "
            "sons object. Before the trustee finalises its decision, the three agree at mediation that the partner will receive "
            "the larger share and each son a smaller share, and they write to the trustee together. This is a composite scenario, "
            "not a real client, and the figures are for illustration only.")
  + inline_cta("Talk to an accredited estate mediator about a super dispute, confidentially.")
)

qa2 = [
 ("Does superannuation form part of my estate?",
  "Not automatically. Super is paid by the fund trustee, not under your will. It only becomes part of your estate if it is paid to your legal personal representative (your executor), either because you nominated them or because the trustee decided to pay it that way."),
 ("Who decides who gets my super when I die?",
  "If you have a valid binding death benefit nomination, the trustee must generally follow it. Otherwise the trustee decides, choosing among your dependants and your estate under the fund's rules."),
 ("Can an adult child claim a super death benefit?",
  "Yes. Children of any age are dependants under superannuation law, so they can be paid a death benefit. Whether they receive a share depends on any nomination and the trustee's decision, and adult children who were not financially dependent may pay tax on part of it."),
 ("How do I dispute a super death benefit decision?",
  "Lodge a claim with the fund, object in writing to any proposed decision within the time the trustee gives you, and if you are still unhappy, complain to AFCA within its time limits. Get advice early because the deadlines are short."),
 ("Can AFCA deal with SMSF death benefit disputes?",
  "Generally no. Disputes about self-managed super funds usually have to be resolved by agreement or in the state Supreme Court, which makes mediation particularly useful."),
 ("Can mediation resolve a super death benefit dispute?",
  "Mediation cannot bind a fund trustee, but it can help family members reach an agreed position that is put to the trustee, or settled together with the rest of the estate."),
]

post(
  "superannuation-death-benefit-disputes",
  "Super Death Benefit Disputes: Who Gets the Super?",
  "Who gets super when someone dies, how binding nominations work, how to dispute a trustee's decision through AFCA, and how mediation helps families agree.",
  "Estate Disputes",
  "Super death benefit <em>disputes</em>",
  "Superannuation is often the biggest asset after the home, yet it usually sits outside the will. Here is who can receive it, how trustees decide, and how families resolve disagreements.",
  [("not-in-will", "Why super is not covered by the will"),
   ("who-can-receive", "Who can receive a death benefit"),
   ("nominations", "Binding, non-binding and no nomination"),
   ("disputing", "How to dispute a trustee's decision"),
   ("mediation", "Where mediation fits")],
  body2, qa2,
  [("estate-dispute-mediation", "Estate Dispute Mediation"),
   ("notional-estate-nsw", "Notional Estate in NSW"),
   ("contesting-a-will", "Contesting a Will"),
   ("superannuation-and-divorce", "Superannuation and Divorce"),
   ("why-you-have-to-update-your-will-after-separation", "Update Your Will After Separation"),
   ("executor-dispute-mediation", "Executor Disputes")],
  read_min=8,
)
print("batch41 built")
