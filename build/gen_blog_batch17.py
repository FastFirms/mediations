#!/usr/bin/env python3
"""Access Mediation SEO content cluster — 8 informational articles.

These pages form the organic-search ecosystem around /access-mediation/.
They are generated using the post() format but are NOT added to the blog feed.
Wire into: gen_meta.py (sitemap) and check_authority.py (validation).

Build: python3 build/gen_blog_batch17.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from gen_blog import post, inline_cta, callout, key_takeaway
from authority_sources import cite

# ─────────────────────────────────────────────────────────────────────────────
# PAGE 1 — /cant-afford-mediation/
# ─────────────────────────────────────────────────────────────────────────────
post(
    "cant-afford-mediation",
    "Can't Afford Mediation? Your Options in Australia",
    "Can't afford private mediation? Compare free, community, Legal Aid and reduced-fee options available in Australia. Honest guide covering all realistic pathways.",
    "Costs &amp; fees",
    "Can't Afford Mediation? <em>Your Realistic Options in Australia</em>",
    ("If standard private mediation fees are genuinely out of reach, you may still have "
     "several pathways available in Australia — including government-supported Family Dispute "
     "Resolution, Legal Aid services, community providers, and reduced-fee private mediation. "
     "This guide explains each option honestly so you can choose what fits your situation."),
    [
        ("do-i-have-to-pay",     "Do I have to pay for mediation?"),
        ("options",              "What are my options if I can't afford private mediation?"),
        ("frc",                  "Family Relationship Centres"),
        ("community-fdr",        "Community and government-funded FDR"),
        ("legal-aid",            "Legal Aid mediation"),
        ("reduced-fee",          "Reduced-fee private mediation"),
        ("cant-qualify",         "What if I don't qualify for free mediation?"),
        ("assets-no-cash",       "What if I own a house but don't have cash?"),
        ("without-lawyer",       "Can I mediate without a lawyer?"),
        ("access-mediation",     "When might Access Mediation be relevant?"),
    ],
    body=(
        key_takeaway(
            "Private mediation is not the only option. Australia has free and low-cost "
            "family dispute resolution pathways — including Family Relationship Centres, "
            "community FDR, Legal Aid, and reduced-fee private mediation — and the right "
            "pathway depends on your circumstances, the complexity of your matter, and "
            "whether you qualify."
        )
        + f"""
<h2 id="do-i-have-to-pay">Do I Have to Pay for Mediation?</h2>
<p>Not necessarily. Whether you pay for mediation depends on the type of service and
provider you use. Government-funded and community services can be free or subsidised.
Private mediation carries a fee — but some private providers, including Mediations
Australia, offer assessed reduced-fee pathways for eligible participants.</p>
<p>The {cite('ag_fdr')} maintains a register of approved family dispute resolution
providers across Australia, including government-funded and community services that do
not charge standard private rates.</p>
"""
        + inline_cta(
            "Wondering whether a reduced-fee private pathway might be available to you?",
            btn="See how Access Mediation works"
        )
        + f"""
<h2 id="options">What Are My Options If I Can't Afford Private Mediation?</h2>
<p>There are several realistic pathways for people who cannot comfortably pay standard
private mediation fees. The right choice depends on your eligibility, the urgency of
your matter, and how complex the issues are.</p>

<h2 id="frc">1. Family Relationship Centres</h2>
<p>Family Relationship Centres (FRCs) are government-funded services that provide free
or low-cost family dispute resolution across Australia. They are operated by
community organisations under Commonwealth Government funding.</p>
<p>{cite('ag_frc')} lists the locations of FRCs around the country.
Services at FRCs can be free or subsidised depending on your circumstances, and they
are available for parenting matters and, in some cases, other family disputes.</p>
<p><strong>Considerations:</strong> FRCs can have waiting lists. They may be better
suited to simpler matters and may have limitations on the complexity of disputes they
can manage. Check with the specific centre for their current eligibility and waiting
times.</p>
<p>{cite('frc')} is the government's central directory for finding local
family relationship services.</p>
"""
        + inline_cta(
            "If an FRC isn't available or suitable, a reduced-fee private option may bridge the gap.",
            btn="Explore Access Mediation"
        )
        + f"""
<h2 id="community-fdr">2. Community and Government-Funded FDR</h2>
<p>Beyond FRCs, a range of community organisations and non-profits offer family dispute
resolution at reduced or no cost. These are typically funded through government grants
and operate in specific regions.</p>
<p>Availability varies considerably by location. Rural and remote areas can have limited
access to community FDR services. Online delivery has expanded access in some areas,
but not uniformly.</p>
<p>You can search for registered providers via {cite('ag_fdr')} or contact
{cite('frc')} to find local services.</p>

<h2 id="legal-aid">3. Legal Aid Mediation</h2>
<p>Legal Aid commissions in each state and territory provide legal assistance to
eligible people on lower incomes. In the family law context, Legal Aid may fund
participation in mediation or family dispute resolution for people who meet the means
and merit tests.</p>
<p>{cite('legal_aid')} provides a national contact point, but eligibility is
assessed separately by each state and territory commission. Eligibility generally
depends on your income and assets, and the nature of the legal matter.</p>
<p><strong>Important:</strong> Legal Aid funding is not guaranteed and may not cover
all aspects of a matter. Availability varies between states. If you are not sure
whether you qualify, contact your state Legal Aid commission directly.</p>

<h2 id="reduced-fee">4. Reduced-Fee and Fee-Assessed Private Mediation</h2>
<p>Some private mediation providers offer a reduced-fee or fee-assessed pathway for
people who cannot afford standard rates but do not qualify for free community services.
Under these arrangements, participants are assessed individually based on their own
income, assets, and circumstances — not their former partner's.</p>
<p>This is distinct from free mediation. A reduced-fee pathway still involves a cost,
but it is calculated on what you can reasonably contribute based on your personal
financial situation.</p>

<h2 id="cant-qualify">What If I Don't Qualify for Free Mediation?</h2>
<p>Free and government-supported services have eligibility criteria. If you do not
qualify — because your income is above the threshold, your matter is considered complex,
or services are not available in your area — you may still have options.</p>
<p>Some private providers offer structured reduced-fee pathways. These sit between
free community services and standard private mediation, and are intended for people
in the gap: too financially capable for Legal Aid, but genuinely unable to pay
standard private fees without hardship.</p>
"""
        + inline_cta(
            "Access Mediation is designed specifically for this situation — assessed individually, not by your partner's income.",
            btn="Check your indicative contribution"
        )
        + f"""
<h2 id="assets-no-cash">What If I Own a House But Don't Have Cash?</h2>
<p>This is one of the most common situations for separating people in Australia. You
may have a share of significant property, but that asset is not readily convertible
to cash — particularly while a property settlement is unresolved, or while you are
covering rent and household expenses after moving out.</p>
<p>Owning a home or having superannuation does not automatically mean you have
accessible funds to pay for legal or mediation costs. Reduced-fee private mediation
providers who assess financial capacity individually — rather than simply looking at
asset ownership — will consider this distinction.</p>
<p>See <a href="/asset-rich-cash-poor-mediation/">Asset rich but cash poor: can I get
reduced-fee mediation?</a> for a full explanation of how financial capacity is assessed
in this context.</p>

<h2 id="without-lawyer">Can I Mediate Without a Lawyer?</h2>
<p>Yes. You can attend mediation without a lawyer. You do not need legal representation
to participate in family dispute resolution.</p>
<p>That said, obtaining independent legal advice before or after mediation is strongly
recommended — particularly for property matters. A lawyer can advise you on your
entitlements before the session and help formalise any agreement reached without you
needing to have them present throughout the process.</p>
<p>Many people consult a lawyer once before mediation, attend the session without legal
representation, and then return to their lawyer to formalise the outcome. This
approach can reduce costs significantly compared with having a lawyer present for the
full mediation.</p>
"""
        + inline_cta(
            "Mediation without a lawyer is straightforward. A free consultation can help you understand what to expect.",
            btn="Book a free consultation"
        )
        + f"""
<h2 id="access-mediation">When Might Access Mediation Be Relevant?</h2>
<p>Access Mediation is Mediations Australia's assessed reduced-contribution pathway for
eligible participants in family mediation. It is designed for people who fall between
two situations: they do not qualify for free or government-funded services, but
standard private mediation fees would cause genuine financial hardship.</p>
<p>Under Access Mediation, each participant's contribution is assessed individually
based on their personal income, accessible assets, dependants, and circumstances.
The other participant's financial position does not affect your assessment.</p>
<p>Access Mediation is not free. Contributions start from $495 + GST per person for
a 3-hour session. It is a private, reduced-fee pathway, not a government or Legal Aid
service. Places are limited.</p>
<p>If you are in a family or property matter and standard fees are difficult,
<a href="/access-mediation/">see how Access Mediation works and check your indicative
contribution</a> — it takes about 60 seconds.</p>
<p><em>General information only. This is not legal advice. For advice about your
specific situation, consult a family lawyer or contact Legal Aid in your state.</em></p>
"""
    ),
    qa=[
        ("Is there free family mediation in Australia?",
         "Yes. Family Relationship Centres and some community FDR providers offer "
         "free or subsidised family mediation. Eligibility depends on the provider, "
         "your location, and the nature of your dispute. Government-funded services "
         "can have waiting times and may not be available in all areas."),
        ("Does Legal Aid cover mediation costs?",
         "Legal Aid may fund participation in mediation for eligible people in some "
         "states, subject to means and merit tests. Eligibility varies by state and "
         "territory. Contact your state Legal Aid commission to find out whether you "
         "qualify."),
        ("Can I get reduced-fee private mediation if I earn too much for Legal Aid?",
         "Possibly. Some private mediation providers offer assessed reduced-fee "
         "pathways for people who do not qualify for free services but cannot "
         "comfortably pay standard private rates. Each participant is assessed "
         "individually based on their own income, assets, and circumstances."),
        ("Does my former partner's income affect what I pay?",
         "Under a properly structured reduced-fee pathway, no. Each participant's "
         "contribution should be assessed separately based on their own financial "
         "circumstances, not their partner's. Neither party is told the financial "
         "basis for the other's contribution."),
        ("Do I need a lawyer to attend mediation?",
         "No. You can attend mediation without a lawyer. However, independent legal "
         "advice before and after mediation is strongly recommended, particularly "
         "for property matters, to ensure you understand your entitlements and "
         "any agreement you reach is appropriately formalised."),
    ],
    related=[
        ("access-mediation",                         "Access Mediation"),
        ("is-family-mediation-free-australia",        "Is Family Mediation Free?"),
        ("who-pays-mediation-one-person-earns-more",  "Who Pays When One Person Earns More?"),
        ("asset-rich-cash-poor-mediation",            "Asset Rich but Cash Poor"),
        ("legal-aid-vs-private-mediation",            "Legal Aid vs Private Mediation"),
        ("our-fee-structure",                         "Our Fee Structure"),
    ],
    read_min=8,
)


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 2 — /is-family-mediation-free-australia/
# ─────────────────────────────────────────────────────────────────────────────
post(
    "is-family-mediation-free-australia",
    "Is Family Mediation Free in Australia?",
    "Is family mediation free in Australia? Explains when it can be free, which services are subsidised, and what to do if you don't qualify for free FDR.",
    "Costs &amp; fees",
    "Is Family Mediation Free in Australia? <em>What You Need to Know</em>",
    ("Family mediation can be free in Australia — but only through specific government-funded "
     "services, and only if you meet their eligibility requirements. This guide explains exactly "
     "when mediation is free, when it is subsidised, and what your options are if neither applies "
     "to you."),
    [
        ("when-free",      "When can family mediation be free?"),
        ("frcs",           "Family Relationship Centres"),
        ("community-fdr",  "Community FDR providers"),
        ("legal-aid",      "Legal Aid mediation"),
        ("when-pay",       "When might you have to pay?"),
        ("dont-qualify",   "What if you don't qualify for free mediation?"),
        ("reduced-fee",    "Reduced-fee private mediation"),
        ("is-access-free", "Is Access Mediation free?"),
        ("how-to-choose",  "How to choose the right option"),
    ],
    body=(
        key_takeaway(
            "Family mediation can be free in Australia through government-funded Family "
            "Relationship Centres, community FDR providers, and, for eligible people, "
            "Legal Aid. However, free services have eligibility requirements, can have "
            "waiting times, and are not always available for complex matters. If you do "
            "not qualify, reduced-fee private mediation may be an option."
        )
        + f"""
<h2 id="when-free">When Can Family Mediation Be Free?</h2>
<p>Family mediation can be free in Australia when accessed through government-funded or
community services. These services are subsidised by Commonwealth or state government
funding, which means eligible participants do not pay — or pay only a nominal amount.</p>
<p>Free mediation is not available on demand. It depends on:</p>
<ul>
<li>the provider and their eligibility criteria;</li>
<li>your location (services are not equally available everywhere);</li>
<li>the nature and complexity of your dispute;</li>
<li>current waiting times and service capacity;</li>
<li>whether the service can handle your particular type of matter.</li>
</ul>

<h2 id="frcs">Family Relationship Centres</h2>
<p>Family Relationship Centres (FRCs) are government-funded services that offer family
dispute resolution at no cost or low cost to eligible families. They are located across
Australia and can be found through {cite('frc')}.</p>
<p>FRCs primarily deal with parenting matters. For a first session of up to one hour,
the service is generally free. Longer sessions may involve a small subsidised fee
depending on the provider and your income.</p>
<p>FRCs can issue section 60I certificates, which are required before filing parenting
orders in court under the {cite('family_law_act')}.</p>
<p><strong>Limitations to be aware of:</strong> FRCs can have significant waiting times.
They may not be well-suited to matters involving complex property issues, businesses,
superannuation disputes, or high-conflict situations. Their mediators are generalist
FDR practitioners rather than specialist accredited mediators.</p>

<h2 id="community-fdr">Community FDR Providers</h2>
<p>Beyond FRCs, a range of community organisations funded by the Commonwealth or state
governments provide family dispute resolution at no cost or low cost. These services
are typically operated by charities, legal aid bodies, or community legal centres.</p>
<p>Availability varies significantly by state and region. The {cite('ag_fdr')}
lists registered FDR providers across Australia, including community services.</p>
<p>Like FRCs, community providers can have waiting times and may not handle complex
property or high-conflict matters.</p>

<h2 id="legal-aid">Legal Aid Mediation</h2>
<p>Each state and territory has a Legal Aid commission that provides legal assistance to
eligible people on lower incomes. In some circumstances, Legal Aid may fund or
facilitate participation in mediation as part of a broader family law matter.</p>
<p>{cite('legal_aid')} provides a national contact point. Eligibility is assessed
by each state commission based on a means test (your income and assets) and a merit
test (the nature of the dispute).</p>
<p>Legal Aid funding is not automatic and availability differs between states. In some
jurisdictions, Legal Aid runs its own mediation or conciliation conferences for eligible
parties.</p>
"""
        + inline_cta(
            "Not sure if you qualify for free mediation? A free consultation can help clarify your options.",
            btn="Book a free consultation"
        )
        + f"""
<h2 id="when-pay">When Might You Have to Pay?</h2>
<p>You will generally need to pay for mediation when:</p>
<ul>
<li>your income or assets are above the eligibility threshold for free services;</li>
<li>your matter is too complex for community FDR providers;</li>
<li>free services have long waiting times and you need to resolve the matter sooner;</li>
<li>you want greater control over the mediator, timing, and process;</li>
<li>your matter involves business interests, investment property, or complex
    superannuation issues;</li>
<li>community services are not available in your location;</li>
<li>the other party wants a private mediator.</li>
</ul>

<h2 id="dont-qualify">What If You Don't Qualify for Free Mediation?</h2>
<p>Not qualifying for free mediation does not mean standard private fees are your only
option. Some private mediation providers offer a reduced-fee or fee-assessed pathway
for people who cannot comfortably pay standard rates but do not meet the eligibility
criteria for free government-funded services.</p>
<p>Under these arrangements, each participant's contribution is assessed individually
based on their own income, accessible assets, and circumstances — not their partner's.
This means participants in the same mediation can pay different amounts.</p>

<h2 id="reduced-fee">Reduced-Fee Private Mediation</h2>
<p>Reduced-fee private mediation sits between free community services and standard
private mediation in terms of cost. It is a privately delivered service with an
assessed, lower contribution for eligible participants.</p>
<p>It is typically more flexible than government-funded services in terms of timing,
mediator choice, and the complexity of matters it can handle. However, it is not free —
participants contribute based on their assessed financial capacity.</p>

<h2 id="is-access-free">Is Access Mediation Free?</h2>
<p><strong>No.</strong> Access Mediation is not free mediation. It is Mediations
Australia's reduced-contribution pathway for eligible participants in family and
property matters. Contributions start from $495 + GST per person for a 3-hour session
and are assessed individually based on your personal income, accessible assets,
dependants, and circumstances.</p>
<p>Access Mediation is a private service operating on a reduced-fee basis. It is
not a government or Legal Aid service, and it does not provide free mediation.
If you are eligible for free government-funded services and they suit your matter,
you should consider using them first.</p>
"""
        + inline_cta(
            "Access Mediation is not free — but your contribution is assessed individually and may be significantly lower than standard rates.",
            btn="Check your indicative contribution"
        )
        + f"""
<h2 id="how-to-choose">How to Choose the Right Option</h2>
<figure class="tbl" style="overflow-x:auto">
<table>
<caption>Comparing mediation options in Australia</caption>
<thead>
<tr><th>Option</th><th>Cost</th><th>Eligibility</th><th>Waiting time</th><th>Complexity</th></tr>
</thead>
<tbody>
<tr>
  <td>Family Relationship Centre</td>
  <td>Free to low-cost</td>
  <td>Most families; parenting focus</td>
  <td>Can be significant</td>
  <td>Simpler matters</td>
</tr>
<tr>
  <td>Community FDR</td>
  <td>Free to subsidised</td>
  <td>Varies by provider</td>
  <td>Varies by provider</td>
  <td>Simpler to moderate</td>
</tr>
<tr>
  <td>Legal Aid</td>
  <td>Free if eligible</td>
  <td>Means + merit test</td>
  <td>Variable</td>
  <td>Varies by service</td>
</tr>
<tr>
  <td>Reduced-fee private (e.g. Access Mediation)</td>
  <td>Assessed contribution</td>
  <td>Income + asset assessment</td>
  <td>Generally faster</td>
  <td>Full range</td>
</tr>
<tr>
  <td>Standard private mediation</td>
  <td>$1,500–$2,250 per party</td>
  <td>No eligibility criteria</td>
  <td>Flexible</td>
  <td>Full range</td>
</tr>
</tbody>
</table>
</figure>
<p>If you are unsure which option suits you, the starting point is whether you qualify
for a free or subsidised service. If you do, and the service can handle your matter in
a reasonable timeframe, that is generally the most cost-effective path. If you do not
qualify, or if community services cannot meet your needs, a reduced-fee private pathway
may be the practical alternative.</p>
<p>See <a href="/cant-afford-mediation/">Can't afford mediation? Your options in
Australia</a> for a fuller explanation of all available pathways.</p>
<p><em>General information only. This is not legal advice.</em></p>
"""
    ),
    qa=[
        ("Is family mediation always free at a Family Relationship Centre?",
         "Not always. The first hour of a FRC service is generally free for most "
         "families. Longer sessions may involve a small fee depending on the "
         "provider and your income. FRCs are government-funded and substantially "
         "subsidised, but not unconditionally free for all services."),
        ("Can I get free mediation for a property settlement?",
         "Government-funded FDR services primarily focus on parenting matters. "
         "Some community services handle property disputes, but availability is "
         "more limited. For complex property matters, a reduced-fee or standard "
         "private mediator is more likely to be appropriate."),
        ("Is Legal Aid available for family mediation in all states?",
         "Legal Aid commissions operate in all states and territories, but "
         "eligibility criteria and the scope of services provided vary. Not all "
         "commissions fund mediation directly. Contact your state Legal Aid "
         "commission to confirm what is available."),
        ("If free mediation is available, why would anyone pay?",
         "Several reasons: free services can have long waiting times; they may not "
         "handle complex matters well; you may not qualify; you may need a "
         "specialist mediator; or you may want greater flexibility in timing and "
         "process. Private mediation can be more responsive and better suited to "
         "complex family law matters."),
        ("Is Access Mediation the same as Legal Aid?",
         "No. Access Mediation is a privately operated reduced-fee pathway, not a "
         "Legal Aid service. It is funded by reduced contributions from eligible "
         "participants, not by government grants. The eligibility criteria, process, "
         "and outcomes are different from Legal Aid."),
    ],
    related=[
        ("cant-afford-mediation",                     "Can't Afford Mediation?"),
        ("access-mediation",                          "Access Mediation"),
        ("legal-aid-vs-private-mediation",            "Legal Aid vs Private Mediation"),
        ("family-relationship-centre-vs-private-mediation", "FRC vs Private Mediation"),
        ("low-cost-family-mediation-australia",       "Low-Cost Family Mediation"),
        ("our-fee-structure",                         "Our Fee Structure"),
    ],
    read_min=8,
)


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 3 — /low-cost-family-mediation-australia/
# ─────────────────────────────────────────────────────────────────────────────
post(
    "low-cost-family-mediation-australia",
    "Low-Cost Family Mediation in Australia: A Complete Guide",
    "Find low-cost family mediation options in Australia — FRCs, community FDR, Legal Aid, and reduced-fee private mediation compared honestly on cost, wait times, and suitability.",
    "Costs &amp; fees",
    "Low-Cost Family Mediation in Australia: <em>A Complete Guide</em>",
    ("Not everyone can comfortably pay standard private mediation fees. Australia has several "
     "lower-cost and reduced-fee family mediation pathways — from government-funded Family "
     "Relationship Centres to fee-assessed private mediation. This guide compares them "
     "honestly so you can make an informed choice."),
    [
        ("usual-cost",        "What does family mediation usually cost?"),
        ("is-free-available", "Is free family mediation available?"),
        ("reduced-fee",       "What is reduced-fee private mediation?"),
        ("vs-free",           "How does it differ from free mediation?"),
        ("lower-quality",     "Does lower cost mean lower quality?"),
        ("who-benefits",      "Who may benefit from reduced-fee mediation?"),
        ("unequal-income",    "What if one person can afford more?"),
        ("assets-no-cash",    "What if I own property but have little cash?"),
        ("comparison",        "Comparing the main options"),
        ("how-access-works",  "How Access Mediation works"),
    ],
    body=(
        key_takeaway(
            "Family mediation in Australia ranges from free (through government-funded FRCs "
            "and community services) to standard private rates of $1,500–$2,250 per person "
            "per session. Between those extremes, some private providers offer assessed "
            "reduced-fee pathways for people who cannot comfortably pay standard rates but "
            "do not qualify for free services."
        )
        + f"""
<h2 id="usual-cost">What Does Family Mediation Usually Cost?</h2>
<p>Standard private family mediation in Australia typically costs between $1,500 and
$2,250 per participant for a half or full day session. For two participants, that is
$3,000–$4,500 in total. These figures cover the mediator's time; additional costs such
as preparation, venue, and consent order drafting may apply.</p>
<p>The {cite('fcfcoa_fees')} provides a useful reference point for what contested
litigation costs — typically $30,000–$150,000 or more per party — which puts the cost
of even standard private mediation in context.</p>

<h2 id="is-free-available">Is Free Family Mediation Available?</h2>
<p>Yes, in certain circumstances. Australia's government-funded family dispute resolution
system provides free or heavily subsidised services through:</p>
<ul>
<li><strong>Family Relationship Centres</strong> — government-funded centres offering
    the first session free for most families. {cite('frc')} is the national directory.</li>
<li><strong>Community FDR providers</strong> — non-profit and community organisations
    funded by the Commonwealth or states to provide low-cost dispute resolution.</li>
<li><strong>Legal Aid</strong> — {cite('legal_aid')} can facilitate or fund
    mediation for eligible people who meet means and merit tests.</li>
</ul>
<p>Free services have eligibility requirements and can have waiting lists.
See <a href="/is-family-mediation-free-australia/">Is family mediation free in
Australia?</a> for a detailed breakdown.</p>
"""
        + inline_cta(
            "If free services don't fit your situation, a fee-assessed private option may be available.",
            btn="Check your indicative contribution"
        )
        + f"""
<h2 id="reduced-fee">What Is Reduced-Fee Private Mediation?</h2>
<p>Reduced-fee private mediation is a privately delivered service where each
participant's contribution is assessed against their individual financial capacity —
their income, accessible assets, dependants, and circumstances — rather than charged
at a flat standard rate.</p>
<p>It sits between free government services and standard private mediation in terms of
cost, but it is closer to standard private mediation in terms of quality, flexibility,
and the complexity of matters it can handle.</p>

<h2 id="vs-free">How Does It Differ From Free Mediation?</h2>
<ul>
<li><strong>Cost:</strong> There is still a participant contribution, assessed on
    financial capacity. It is not free.</li>
<li><strong>Funding:</strong> Privately funded through participant contributions,
    not government grants.</li>
<li><strong>Eligibility:</strong> Assessment based on financial capacity, not a
    Legal Aid means and merit test.</li>
<li><strong>Flexibility:</strong> Private services tend to offer more flexibility on
    timing, mediator selection, and complexity of matters handled.</li>
<li><strong>Speed:</strong> Private providers generally offer shorter lead times than
    government-funded services, which can have significant waiting lists.</li>
</ul>

<h2 id="lower-quality">Does Lower Cost Mean Lower Quality?</h2>
<p>Not necessarily. A reduced-fee private mediation service using qualified, accredited
mediators can deliver the same professional standard as a standard-rate service.
The qualification and accreditation requirements for mediators do not vary by fee
level. What a lower assessed contribution reflects is the participant's financial
capacity — not the quality of the mediator or the process.</p>

<h2 id="who-benefits">Who May Benefit From Reduced-Fee Mediation?</h2>
<p>Reduced-fee mediation may be appropriate for people who:</p>
<ul>
<li>have an income above the Legal Aid threshold but cannot comfortably pay standard
    private rates;</li>
<li>do not qualify for free community services;</li>
<li>are in a period of financial transition after separation;</li>
<li>need a specialist accredited mediator for a complex matter;</li>
<li>want a faster process than government-funded services can currently offer;</li>
<li>need the matter handled with greater confidentiality or flexibility.</li>
</ul>

<h2 id="unequal-income">What If One Person Can Afford More?</h2>
<p>Under a well-structured reduced-fee pathway, each participant is assessed
individually. You are not assessed on your former partner's income. Participants in
the same mediation can pay different amounts without either being told the other's
financial details or contribution level.</p>
<p>See <a href="/who-pays-mediation-one-person-earns-more/">Who pays for mediation
when one person earns more?</a> for a full explanation of how this works.</p>

<h2 id="assets-no-cash">What If I Own Property But Have Little Cash?</h2>
<p>Owning a house or having superannuation does not automatically mean you have
accessible cash available. A reduced-fee provider that assesses financial capacity
properly will consider the difference between what you own and what you can readily
access. See <a href="/asset-rich-cash-poor-mediation/">Asset rich but cash poor:
can I get reduced-fee mediation?</a> for details.</p>
"""
        + inline_cta(
            "Mediations Australia's Access Mediation uses the same mediators and process as our standard service.",
            btn="See how Access Mediation works"
        )
        + f"""
<h2 id="comparison">Comparing the Main Options</h2>
<figure class="tbl" style="overflow-x:auto">
<table>
<caption>Lower-cost family mediation options compared</caption>
<thead>
<tr>
  <th>Option</th><th>Approx. cost</th><th>Eligibility</th>
  <th>Wait time</th><th>Complexity handled</th>
</tr>
</thead>
<tbody>
<tr>
  <td>Family Relationship Centre</td>
  <td>Free (1hr) to low-cost</td>
  <td>Most families; parenting focus</td>
  <td>Often weeks–months</td>
  <td>Simpler matters</td>
</tr>
<tr>
  <td>Community FDR</td>
  <td>Free to subsidised</td>
  <td>Varies by provider</td>
  <td>Varies</td>
  <td>Simpler to moderate</td>
</tr>
<tr>
  <td>Legal Aid</td>
  <td>Free if eligible</td>
  <td>Means + merit test</td>
  <td>Variable</td>
  <td>Varies</td>
</tr>
<tr>
  <td>Reduced-fee private (Access Mediation)</td>
  <td>From $495 + GST pp assessed</td>
  <td>Income + asset assessment</td>
  <td>Generally 1–2 weeks</td>
  <td>Full range incl. property</td>
</tr>
<tr>
  <td>Standard private mediation</td>
  <td>$1,500–$2,250 pp</td>
  <td>None</td>
  <td>Flexible</td>
  <td>Full range</td>
</tr>
</tbody>
</table>
</figure>

<h2 id="how-access-works">How Access Mediation Works</h2>
<p>Access Mediation is Mediations Australia's assessed reduced-contribution pathway.
It is available for eligible family and property matters. Contributions are assessed
individually using a structured process based on your income, accessible assets,
dependants, and hardship circumstances — not your partner's financial position.</p>
<p>Assessment details are private. To check your indicative contribution, use the
calculator on the <a href="/access-mediation/">Access Mediation page</a>.</p>
<p><em>General information only. This is not legal advice.</em></p>
"""
    ),
    qa=[
        ("What is the cheapest way to get family mediation in Australia?",
         "The cheapest option is a government-funded Family Relationship Centre, "
         "which provides the first hour free for most families, or a community FDR "
         "provider. If you do not qualify, a reduced-fee private pathway assessed on "
         "your income and assets may be the next most affordable option."),
        ("Can I use a low-cost mediator for property settlement?",
         "Government-funded FDR services are primarily focused on parenting matters "
         "and may not be well-suited to complex property disputes. For property "
         "settlement, a specialist accredited family mediator — on a reduced-fee "
         "basis if eligible — is often more appropriate."),
        ("Is reduced-fee mediation as good as standard private mediation?",
         "A reduced-fee service using qualified, accredited mediators applies the "
         "same professional standards as a standard-rate service. The reduced fee "
         "reflects the participant's assessed financial contribution, not the quality "
         "of the mediator or process."),
        ("Can both parties use reduced-fee mediation at the same time?",
         "Yes. Under an individual assessment model, each participant is assessed "
         "separately. Both participants could qualify for a reduced contribution, or "
         "one might qualify while the other pays the standard rate. Neither party is "
         "told the other's contribution."),
        ("How long does it take to access low-cost mediation?",
         "Government-funded FDR services can have waiting times of weeks or months. "
         "Reduced-fee private mediation through providers like Mediations Australia "
         "can generally be arranged within one to two weeks of eligibility "
         "confirmation."),
    ],
    related=[
        ("cant-afford-mediation",                     "Can't Afford Mediation?"),
        ("is-family-mediation-free-australia",        "Is Family Mediation Free?"),
        ("access-mediation",                          "Access Mediation"),
        ("who-pays-mediation-one-person-earns-more",  "Who Pays When One Person Earns More?"),
        ("asset-rich-cash-poor-mediation",            "Asset Rich but Cash Poor"),
        ("our-fee-structure",                         "Our Fee Structure"),
    ],
    read_min=9,
)


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 4 — /who-pays-mediation-one-person-earns-more/
# ─────────────────────────────────────────────────────────────────────────────
post(
    "who-pays-mediation-one-person-earns-more",
    "Who Pays for Mediation When One Person Earns More?",
    "Do mediation fees have to be split 50/50 when incomes are unequal? How fee arrangements work in private and reduced-fee mediation — and what happens under Access Mediation.",
    "Costs &amp; fees",
    "Who Pays for Mediation When <em>One Person Earns More?</em>",
    ("When incomes are unequal after separation, the question of who pays for mediation "
     "is a real one. This guide explains how mediation fees are normally divided, when the "
     "split does not have to be equal, and how services like Access Mediation assess "
     "each participant separately."),
    [
        ("always-50-50",      "Are mediation fees always split 50/50?"),
        ("can-pay-different", "Can participants pay different amounts?"),
        ("private-mediation", "What happens in standard private mediation?"),
        ("access-model",      "What happens under Access Mediation?"),
        ("privacy",           "Will the other person know what I pay?"),
        ("refuses-to-pay",    "What if one person refuses to pay?"),
        ("cant-afford-share", "What if I can't afford my share?"),
        ("next-steps",        "Next steps"),
    ],
    body=(
        key_takeaway(
            "There is no rule that mediation fees must be divided equally. The arrangement "
            "depends on the provider, the agreement between participants, and — where a "
            "reduced-fee pathway is used — each person's individually assessed financial "
            "capacity. Under Access Mediation, each participant's contribution is assessed "
            "privately and separately from the other's."
        )
        + f"""
<h2 id="always-50-50">Are Mediation Fees Always Split 50/50?</h2>
<p>No. There is no universal rule that mediation fees must be divided equally. How the
cost is shared depends on the service, any agreement between participants, and whether
a reduced-fee or individually assessed pathway is used.</p>
<p>In standard private mediation, the most common arrangement is for each participant to
pay their own share — which is typically equal if using a flat-rate schedule. But
participants can agree to a different arrangement, and some private providers offer
assessed models where contributions are not equal.</p>

<h2 id="can-pay-different">Can Participants Pay Different Amounts?</h2>
<p>Yes. Under an individually assessed reduced-fee model, each participant's
contribution is calculated based on their own income, assets, and circumstances.
Two participants in the same mediation can end up paying significantly different
amounts without either being entitled to know what the other is contributing.</p>
<p>This arrangement is designed to remove the assumption that both parties have equal
financial resources — an assumption that is frequently wrong after separation.</p>
"""
        + inline_cta(
            "If the standard fee is difficult for you but your partner can afford it, you may still qualify for a reduced contribution.",
            btn="Check your indicative contribution"
        )
        + f"""
<h2 id="private-mediation">What Happens in Standard Private Mediation?</h2>
<p>In most standard private mediation, the fee is set as a flat per-person rate. The
{cite('amdras')} sets accreditation standards for mediators but does not prescribe
how fees must be allocated between participants.</p>
<p>In practice, each participant usually pays their own share directly to the mediation
provider. A participant's financial circumstances are not typically taken into account
in setting the fee under a standard arrangement.</p>
<p>Mediations Australia's standard fee is $1,500 + GST per participant for a 3-hour
session, or $2,250 + GST per participant for a full day. See our
<a href="/our-fee-structure/">full fee structure</a> for details.</p>

<h2 id="access-model">What Happens Under Access Mediation?</h2>
<p>Under Access Mediation, each participant is assessed separately. Your contribution
is calculated based on your personal gross annual income, your accessible assets, the
number of dependants you support, whether you hold a concession card, and whether you
have a genuine hardship circumstance.</p>
<p>Your partner's financial situation has no bearing on your assessment. You may qualify
for a reduced contribution even if your former partner earns significantly more. You
may also pay a different amount from your partner without either of you being told
the other's contribution or the financial details behind it.</p>

<h2 id="privacy">Will the Other Person Know What I Pay?</h2>
<p>No. Under Access Mediation, your financial assessment and contribution are entirely
private. The other participant is never told your income, your assets, your hardship
circumstances, or your contribution level.</p>
"""
        + inline_cta(
            "Your contribution assessment under Access Mediation is private — your partner will never know your financial details.",
            btn="See how Access Mediation works"
        )
        + f"""
<h2 id="refuses-to-pay">What If One Person Refuses to Pay?</h2>
<p>If the other participant refuses to pay their share of the mediation fee, the
mediation session generally cannot proceed. A mediation provider cannot force someone
to attend or pay for mediation.</p>
<p>If the other party refuses to participate in mediation for parenting matters, this
may be relevant if you later need to file for parenting orders — as the
{cite('family_law_act')} requires genuine attempts at FDR before court proceedings
in most parenting matters (with some exceptions). In some cases a section 60I
certificate can be issued noting that the other party declined to attend.</p>

<h2 id="cant-afford-share">What If I Can't Afford My Share?</h2>
<p>If standard private mediation fees are genuinely out of reach, several options
may apply:</p>
<ul>
<li>Apply for Access Mediation and have your contribution assessed against your
    personal financial capacity.</li>
<li>Use a government-funded FDR service such as a Family Relationship Centre,
    which may be free or low-cost for eligible participants.</li>
<li>Contact Legal Aid in your state to assess whether you meet the eligibility
    criteria for funded legal assistance.</li>
</ul>
<p>See <a href="/cant-afford-mediation/">Can't afford mediation? Your options in
Australia</a> for a full overview of available pathways.</p>

<h2 id="next-steps">Next Steps</h2>
<ol>
<li>Check whether you qualify for a free or subsidised government service.</li>
<li>If not, check your indicative contribution under Access Mediation using the
    <a href="/access-mediation/">calculator on the Access Mediation page</a>.</li>
<li>If you have questions about your specific circumstances, book a free initial
    consultation.</li>
</ol>
<p><em>General information only. This is not legal advice.</em></p>
"""
    ),
    qa=[
        ("Does my ex-partner's income affect what I pay for mediation?",
         "Under a standard private mediation arrangement, no — you typically pay "
         "your own share regardless of your partner's income. Under Access "
         "Mediation, your contribution is assessed individually on your own income, "
         "assets, and circumstances. Your partner's financial position has no "
         "bearing on your assessed contribution."),
        ("Can I ask my ex to pay for my mediation?",
         "You can ask, but there is no legal mechanism that compels the other "
         "party to pay your mediation fees. If one party has significantly greater "
         "financial resources, you could discuss a voluntary arrangement. "
         "Alternatively, an individually assessed reduced-fee pathway means your "
         "contribution reflects your financial capacity rather than requiring the "
         "other party to subsidise you."),
        ("Is there a 50/50 rule for paying mediation costs?",
         "No. There is no rule requiring fees to be divided equally. The arrangement "
         "depends on the provider and any agreement between participants. Some "
         "providers use individually assessed contributions where each party pays "
         "according to their own financial capacity."),
        ("What happens if I can't afford mediation on a single income?",
         "Several options may be available: free government-funded FDR services, "
         "Legal Aid (if eligible), or a reduced-fee private pathway such as Access "
         "Mediation, where your contribution is assessed on your individual "
         "circumstances."),
        ("Will the mediator know my income?",
         "Your income details are used only for the financial assessment process "
         "and are handled by administrative staff, not the mediator. They are never "
         "shared with the other participant."),
    ],
    related=[
        ("does-mediation-have-to-be-paid-50-50",      "Does Mediation Have to Be 50/50?"),
        ("cant-afford-mediation",                     "Can't Afford Mediation?"),
        ("access-mediation",                          "Access Mediation"),
        ("asset-rich-cash-poor-mediation",            "Asset Rich but Cash Poor"),
        ("low-cost-family-mediation-australia",       "Low-Cost Family Mediation"),
        ("our-fee-structure",                         "Our Fee Structure"),
    ],
    read_min=7,
)


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 5 — /does-mediation-have-to-be-paid-50-50/
# ─────────────────────────────────────────────────────────────────────────────
post(
    "does-mediation-have-to-be-paid-50-50",
    "Does Mediation Have to Be Paid 50/50?",
    "Does mediation have to be paid 50/50? No — here's how fee arrangements actually work in Australian family mediation, including reduced-fee and unequal-contribution options.",
    "Costs &amp; fees",
    "Does Mediation Have to Be Paid 50/50? <em>What the Rules Actually Say</em>",
    ("Mediation fees do not have to be divided equally. How costs are allocated depends "
     "on the mediator, the service model, any agreement between participants, and the "
     "circumstances of the matter. This page explains the common arrangements and when "
     "an unequal contribution is legitimate."),
    [
        ("the-answer",      "The direct answer"),
        ("common-models",   "Common fee arrangements in Australian family mediation"),
        ("unequal",         "Unequal contributions — when and how"),
        ("access-model",    "Access Mediation's individual assessment model"),
        ("how-to-arrange",  "How to arrange a different split"),
    ],
    body=(
        key_takeaway(
            "No. Mediation fees do not necessarily have to be divided equally. How "
            "the cost is allocated depends on the provider, the service model, any "
            "agreement between participants, and — where a reduced-fee pathway is "
            "used — each person's individually assessed financial capacity."
        )
        + f"""
<h2 id="the-answer">The Direct Answer</h2>
<p>There is no rule in Australian law or in standard mediation practice that requires
mediation costs to be split equally between participants. The fee arrangement is a
matter between the participants and the mediation provider.</p>
<p>In most standard private mediation in Australia, each participant simply pays their
own per-person fee — which means an equal split by default. But this is a convention,
not a legal requirement, and it is not universal across all service types.</p>

<h2 id="common-models">Common Fee Arrangements in Australian Family Mediation</h2>
<figure class="tbl" style="overflow-x:auto">
<table>
<caption>How mediation fees are typically allocated</caption>
<thead>
<tr><th>Service type</th><th>Who pays</th><th>Equal split?</th></tr>
</thead>
<tbody>
<tr>
  <td>Standard private mediation</td>
  <td>Each participant pays their own per-person fee</td>
  <td>Effectively yes (flat rate)</td>
</tr>
<tr>
  <td>Reduced-fee private mediation (Access Mediation)</td>
  <td>Each participant pays assessed contribution</td>
  <td>Not necessarily — assessed individually</td>
</tr>
<tr>
  <td>Family Relationship Centre</td>
  <td>Subsidised by government; participant may pay nothing or a small amount</td>
  <td>N/A — no split as such</td>
</tr>
<tr>
  <td>Legal Aid-funded mediation</td>
  <td>Legal Aid may fund one or both parties</td>
  <td>N/A — subject to eligibility</td>
</tr>
<tr>
  <td>Workplace mediation</td>
  <td>Typically paid by the employer</td>
  <td>No split — single payer</td>
</tr>
</tbody>
</table>
</figure>
"""
        + inline_cta(
            "Want to check whether a reduced-fee contribution applies to your situation?",
            btn="Check your indicative contribution"
        )
        + f"""
<h2 id="unequal">Unequal Contributions — When and How</h2>
<p>An unequal contribution arrangement can arise in several ways:</p>
<ul>
<li><strong>Voluntary agreement:</strong> The two participants agree between themselves
    that one will pay a larger share — for example, if one has significantly greater
    financial resources after separation.</li>
<li><strong>Fee-assessed service:</strong> Under a reduced-fee model like Access
    Mediation, contributions are assessed individually based on each participant's own
    income and assets. The result can be that one participant pays a standard rate while
    the other pays a reduced rate.</li>
<li><strong>Third-party payment:</strong> In some circumstances, a third party may pay
    for one or both participants.</li>
</ul>
<p>None of these arrangements requires the other participant's consent to your own
contribution being assessed differently. Under Access Mediation, each participant's
financial details are private.</p>

<h2 id="access-model">Access Mediation's Individual Assessment Model</h2>
<p>Under Access Mediation:</p>
<ul>
<li>each participant's contribution is assessed on their own income, accessible assets,
    dependants, and hardship circumstances;</li>
<li>the other participant's financial position is irrelevant to your assessment;</li>
<li>neither participant is told the other's financial basis for contribution;</li>
<li>contributions start from $495 + GST per person for a 3-hour session.</li>
</ul>
<p>Two participants in the same mediation session can legitimately pay different amounts.
For more detail, see <a href="/who-pays-mediation-one-person-earns-more/">Who pays for
mediation when one person earns more?</a> and the
<a href="/access-mediation/">Access Mediation page</a>.</p>
"""
        + inline_cta(
            "Mediation does not have to be out of reach because of an unequal financial situation.",
            btn="See how Access Mediation works"
        )
        + f"""
<h2 id="how-to-arrange">How to Arrange a Different Split</h2>
<p>If you believe a 50/50 split would cause genuine financial hardship:</p>
<ol>
<li>Check whether you qualify for a government-funded free service first
    (Family Relationship Centre or {cite('legal_aid')}).</li>
<li>If not, apply for Access Mediation and have your contribution assessed
    individually. Your partner does not need to agree to your assessment being
    reduced — it is separate from theirs.</li>
<li>Alternatively, discuss with the mediation provider whether a voluntary different
    split can be arranged if both parties agree.</li>
</ol>
<p>See <a href="/cant-afford-mediation/">Can't afford mediation? Your options in
Australia</a> for a full guide to available pathways.</p>
<p>See also the {cite('ag_fdr')} for information on government-funded FDR services.</p>
<p><em>General information only. This is not legal advice.</em></p>
"""
    ),
    qa=[
        ("Is there a legal requirement to split mediation costs equally?",
         "No. There is no legal requirement in Australia for mediation costs to be "
         "divided equally. The arrangement is between participants and the provider."),
        ("Can I pay less than my ex if I earn less?",
         "Under a standard private mediation arrangement, both parties typically pay "
         "the same per-person rate regardless of income. However, under an individually "
         "assessed reduced-fee pathway such as Access Mediation, your contribution is "
         "assessed on your own income and assets — so you may pay less than your "
         "former partner without needing their agreement."),
        ("Does my ex need to agree to me paying less?",
         "Under Access Mediation, no. Your contribution is assessed independently. "
         "Your former partner does not need to consent to your reduced assessment, "
         "and they will not be told your contribution or the financial details behind it."),
        ("Can one person pay for both parties' mediation?",
         "In principle, yes — but this is uncommon and would require agreement "
         "between both parties and the provider. More commonly, each party pays their "
         "own assessed contribution, which may be a different amount."),
        ("What if we can't agree on how to split the cost?",
         "If cost-sharing is a barrier, a reduced-fee model with individual "
         "assessment sidesteps the issue entirely — each party pays their own "
         "assessed contribution with no negotiation required between them."),
    ],
    related=[
        ("who-pays-mediation-one-person-earns-more",  "Who Pays When One Person Earns More?"),
        ("cant-afford-mediation",                     "Can't Afford Mediation?"),
        ("access-mediation",                          "Access Mediation"),
        ("low-cost-family-mediation-australia",       "Low-Cost Family Mediation"),
        ("is-family-mediation-free-australia",        "Is Family Mediation Free?"),
        ("our-fee-structure",                         "Our Fee Structure"),
    ],
    read_min=6,
)


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 6 — /asset-rich-cash-poor-mediation/
# ─────────────────────────────────────────────────────────────────────────────
post(
    "asset-rich-cash-poor-mediation",
    "Asset Rich but Cash Poor: Can I Get Reduced-Fee Mediation?",
    "Own a home but can't afford mediation? Being asset-rich doesn't mean cash is available. How reduced-fee mediation assesses financial capacity — not just what you own.",
    "Costs &amp; fees",
    "Asset Rich but Cash Poor: <em>Can I Get Reduced-Fee Mediation?</em>",
    ("Owning a home or having superannuation does not mean you have accessible cash. "
     "After separation, many people have assets on paper but very limited liquid funds. "
     "This guide explains how financial capacity is assessed for reduced-fee mediation — "
     "and why asset ownership alone does not determine eligibility."),
    [
        ("what-it-means",   "What does 'asset rich but cash poor' mean after separation?"),
        ("why-not-cash",    "Why property ownership does not always mean available cash"),
        ("common-examples", "Common examples"),
        ("how-assessed",    "How financial capacity may be assessed"),
        ("how-access",      "How Access Mediation assesses financial capacity"),
        ("home-exclude",    "Does owning a home automatically exclude me?"),
        ("superannuation",  "What about superannuation?"),
        ("next-steps",      "What happens next?"),
    ],
    body=(
        key_takeaway(
            "Owning a house or having superannuation does not automatically disqualify "
            "you from reduced-fee mediation. Financial capacity is assessed on accessible "
            "funds — your income and liquid assets — not on the total value of assets "
            "that are jointly owned, tied up in property, or not yet divided."
        )
        + f"""
<h2 id="what-it-means">What Does "Asset Rich but Cash Poor" Mean After Separation?</h2>
<p>After separation, many people find themselves with a share of significant assets —
a family home, superannuation, or an investment property — but very little accessible
cash. The assets exist on paper, but they cannot easily be converted to cash. The home
cannot be sold without the other party's agreement or a court order. Superannuation
cannot be accessed until retirement age. Jointly held assets may be frozen in a
dispute.</p>
<p>Meanwhile, the day-to-day financial pressures of separation — rent or mortgage
payments on a reduced income, legal costs, caring for children — can leave a person
with little or no accessible cash, even if their asset position looks substantial.</p>

<h2 id="why-not-cash">Why Property Ownership Does Not Always Mean Available Cash</h2>
<p>A share in a family home worth $600,000 does not give you $300,000 in accessible
funds. It gives you a contingent interest in property that:</p>
<ul>
<li>cannot be sold unilaterally;</li>
<li>may still carry a mortgage;</li>
<li>is subject to property settlement proceedings which can take months or years
    to finalise;</li>
<li>generates no income unless rented, and often cannot be rented while the other
    party occupies it;</li>
<li>may have encumbrances, guarantees, or claims affecting its net value.</li>
</ul>
<p>The gap between asset value on paper and accessible funds is a real financial
reality for many separating Australians, and it is particularly acute in high
property-value markets.</p>
"""
        + inline_cta(
            "Your asset position doesn't automatically determine your Access Mediation contribution — it's assessed on accessible funds.",
            btn="Check your indicative contribution"
        )
        + f"""
<h2 id="common-examples">Common Examples</h2>
<p><strong>The family home:</strong> Alex and Sam own a home together. Alex has moved
out and is paying rent while also covering child-related expenses. The home has not
yet been sold. Alex has an interest in a valuable asset, but no accessible cash from
it and a reduced income. (Hypothetical example only — does not indicate eligibility.)</p>

<p><strong>Superannuation:</strong> Lee has accumulated significant superannuation
over a long working life but is 48 years old and cannot access it for another decade.
Lee's income is modest and accessible savings are minimal. (Hypothetical example only.)</p>

<p><strong>Investment property:</strong> Jordan holds a share in an investment
property with their former partner. Jordan cannot access the equity without the
property being sold, which requires both parties' agreement. Jordan is paying rent
on a separate residence and has limited monthly cash flow.
(Hypothetical example only.)</p>

<h2 id="how-assessed">How Mediation Providers May Assess Financial Capacity</h2>
<p>A well-designed reduced-fee program distinguishes between:</p>
<ul>
<li><strong>Gross annual income</strong> — your actual earned income, not assets;</li>
<li><strong>Accessible assets</strong> — cash, savings, and investments that can
    readily be converted to cash;</li>
<li><strong>Illiquid assets</strong> — property, superannuation, jointly held assets
    — noted but not treated as equivalent to accessible funds;</li>
<li><strong>Dependants</strong> — the number of people financially dependent on you;</li>
<li><strong>Hardship circumstances</strong> — material hardship such as disability,
    significant debt, or unusual expense burdens.</li>
</ul>
<p>This distinction matters because treating total asset value as equivalent to
accessible cash would exclude many people who genuinely cannot pay without hardship.
The {cite('ag_fdr')} provides context on the role of family dispute resolution in
Australia's legal system. {cite('legal_aid')} provides state-by-state information
on funded assistance for eligible participants.</p>

<h2 id="how-access">How Access Mediation Assesses Financial Capacity</h2>
<p>Access Mediation assesses each participant's contribution based on:</p>
<ul>
<li>personal gross annual income (generally assessed below $150,000);</li>
<li>accessible assets — cash, savings, readily realisable investments;</li>
<li>number of dependants (three or more may attract a further reduction);</li>
<li>concession card status;</li>
<li>genuine material hardship.</li>
</ul>
<p>Assessment details are private. The financial basis for your contribution is
never shared with the other participant.</p>

<h2 id="home-exclude">Does Owning a Home Automatically Exclude Me?</h2>
<p>No. Under Access Mediation, owning a home is taken into account as part of the
overall financial picture — but it does not automatically make you ineligible or
place you in a higher contribution band. What matters most is your accessible cash
and income position. If the home is jointly owned and subject to property settlement
proceedings, it is generally not treated as accessible funds for the purpose of
the assessment.</p>

<h2 id="superannuation">What About Superannuation?</h2>
<p>Superannuation is included in the broader financial assessment but treated as an
illiquid asset unless you are at or near preservation age. A large superannuation
balance does not automatically push you into a higher contribution band if your
accessible cash and income are limited.</p>
"""
        + inline_cta(
            "If your assets are tied up in property or super but your cash flow is limited, Access Mediation may be accessible to you.",
            btn="See how Access Mediation works"
        )
        + f"""
<h2 id="next-steps">What Happens Next?</h2>
<ol>
<li>Check your indicative contribution using the calculator on the
    <a href="/access-mediation/">Access Mediation page</a>. This takes about
    60 seconds and does not require financial documents at that stage.</li>
<li>If you qualify for an indicative reduced contribution, the next step is to make
    a formal application and provide supporting information.</li>
<li>If you are not sure whether the value of your assets affects your eligibility,
    a free initial consultation can help clarify this before you apply.</li>
</ol>
<p>See also <a href="/cant-afford-mediation/">Can't afford mediation? Your options
in Australia</a> for a full overview of alternatives.</p>
<p><em>General information only. This is not legal advice. Do not rely on the
examples above as guidance about your specific eligibility.</em></p>
"""
    ),
    qa=[
        ("I own a house — does that automatically disqualify me from reduced-fee mediation?",
         "No. Under Access Mediation, owning a home is considered in the overall "
         "financial picture but does not automatically exclude you. What matters "
         "most is your accessible cash and income position. A jointly owned home "
         "subject to property settlement is generally not treated as accessible funds."),
        ("Can I get reduced-fee mediation if I have superannuation?",
         "Possibly. Superannuation is considered in the broader assessment but "
         "treated as illiquid if you are below preservation age. A large super "
         "balance does not automatically push you into a higher contribution band "
         "if your income and accessible cash are limited."),
        ("What counts as 'accessible assets' in the assessment?",
         "Accessible assets are those readily convertible to cash — savings accounts, "
         "cash deposits, and marketable securities. A family home subject to "
         "settlement proceedings, superannuation, and jointly held illiquid assets "
         "are generally not treated as accessible funds."),
        ("Does my partner's share of the assets affect my assessment?",
         "No. Each participant is assessed individually. Your former partner's "
         "assets, income, and financial position have no bearing on your "
         "assessment under Access Mediation."),
        ("What if I own property but earn a low income?",
         "This is precisely the situation Access Mediation is designed for. "
         "Your contribution is based primarily on your income and accessible "
         "assets. Property you own but cannot readily access is assessed "
         "differently from liquid funds."),
    ],
    related=[
        ("cant-afford-mediation",                     "Can't Afford Mediation?"),
        ("who-pays-mediation-one-person-earns-more",  "Who Pays When One Person Earns More?"),
        ("access-mediation",                          "Access Mediation"),
        ("does-mediation-have-to-be-paid-50-50",      "Does Mediation Have to Be 50/50?"),
        ("low-cost-family-mediation-australia",       "Low-Cost Family Mediation"),
        ("our-fee-structure",                         "Our Fee Structure"),
    ],
    read_min=8,
)


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 7 — /family-relationship-centre-vs-private-mediation/
# ─────────────────────────────────────────────────────────────────────────────
post(
    "family-relationship-centre-vs-private-mediation",
    "Family Relationship Centre vs Private Mediation",
    "FRC vs private mediation in Australia — an honest comparison of cost, wait times, complexity, and who each option suits. Includes when reduced-fee private may be the better fit.",
    "Family Mediation",
    "Family Relationship Centre vs Private Mediation: <em>An Honest Comparison</em>",
    ("Family Relationship Centres and private mediation are both legitimate pathways "
     "for resolving family disputes in Australia — but they suit different situations. "
     "This guide compares them honestly so you can choose the right option for "
     "your circumstances."),
    [
        ("what-is-frc",       "What is a Family Relationship Centre?"),
        ("what-is-private",   "What is private mediation?"),
        ("comparison",        "Side-by-side comparison"),
        ("when-frc",          "When an FRC may be the right choice"),
        ("when-private",      "When private mediation may be better"),
        ("gap",               "What if an FRC is not suitable but standard fees are difficult?"),
    ],
    body=(
        key_takeaway(
            "Family Relationship Centres are free or low-cost government-funded services "
            "primarily suited to parenting matters between cooperative parents. Private "
            "mediation is more flexible, faster, and better suited to complex matters "
            "including property settlement. If standard private fees are a barrier, a "
            "reduced-fee private pathway may bridge the gap."
        )
        + f"""
<h2 id="what-is-frc">What Is a Family Relationship Centre?</h2>
<p>Family Relationship Centres (FRCs) are government-funded services designed to
help separating families resolve disputes without going to court. They are operated
by community organisations under Commonwealth Government funding and can be found
through {cite('frc')}.</p>
<p>FRCs provide family dispute resolution (FDR), information, and referrals. They
are registered FDR providers and can issue section 60I certificates under the
{cite('family_law_act')} — required before filing parenting orders in most
circumstances.</p>
<p>The first hour of FRC services is generally free for most families.</p>

<h2 id="what-is-private">What Is Private Mediation?</h2>
<p>Private mediation is delivered by accredited mediators or mediation organisations
operating outside the government-funded FDR system. Participants pay directly for
the mediator's time at privately set rates.</p>
<p>Private mediators must be accredited under the {cite('amdras')} framework.
They handle the full range of family disputes — parenting, property, spousal
maintenance, superannuation, and combined matters — and can work at times and
in formats agreed by the parties.</p>
<p>Some private mediation providers offer assessed reduced-fee pathways for
eligible participants.</p>
"""
        + inline_cta(
            "If standard private fees are a concern, our Access Mediation pathway may make a difference.",
            btn="Check your indicative contribution"
        )
        + f"""
<h2 id="comparison">Side-by-Side Comparison</h2>
<figure class="tbl" style="overflow-x:auto">
<table>
<caption>Family Relationship Centre vs private mediation — key factors</caption>
<thead>
<tr><th>Factor</th><th>Family Relationship Centre</th><th>Private Mediation</th></tr>
</thead>
<tbody>
<tr><td>Cost</td>
  <td>First hour free; subsidised beyond that</td>
  <td>$1,500–$2,250 per person (or assessed reduced-fee)</td></tr>
<tr><td>Government-funded</td><td>Yes</td><td>No</td></tr>
<tr><td>Waiting time</td>
  <td>Often weeks to months</td>
  <td>Generally 1–2 weeks</td></tr>
<tr><td>Choice of mediator</td>
  <td>Assigned by centre</td>
  <td>You can request a specific mediator</td></tr>
<tr><td>Issues handled</td>
  <td>Primarily parenting; some property</td>
  <td>Full range — parenting, property, super, combined</td></tr>
<tr><td>Complex property matters</td>
  <td>Limited suitability</td>
  <td>Well-suited</td></tr>
<tr><td>Section 60I certificate</td>
  <td>Yes — can be issued</td>
  <td>Yes — if registered FDR provider</td></tr>
<tr><td>Lawyer involvement</td>
  <td>Typically without lawyers present</td>
  <td>Flexible — lawyers may attend if agreed</td></tr>
<tr><td>Online sessions</td>
  <td>Some centres offer online</td>
  <td>Widely available online</td></tr>
<tr><td>Reduced-fee option</td>
  <td>Service is subsidised by design</td>
  <td>Available through Access Mediation (if eligible)</td></tr>
</tbody>
</table>
</figure>
<p><em>This comparison is general in nature. Individual FRCs and private providers
may vary. Check with the specific provider for current information.</em></p>

<h2 id="when-frc">When an FRC May Be the Right Choice</h2>
<p>A Family Relationship Centre is likely to suit you well if:</p>
<ul>
<li>your matter primarily involves parenting arrangements and is not highly contentious;</li>
<li>you qualify for the free or subsidised service and timing is not urgent;</li>
<li>you and your former partner are broadly cooperative;</li>
<li>a section 60I certificate is your immediate need;</li>
<li>budget is the primary concern.</li>
</ul>

<h2 id="when-private">When Private Mediation May Be Better</h2>
<p>Private mediation is likely to be more suitable when:</p>
<ul>
<li>the matter involves property settlement, superannuation splitting, or complex
    financial issues;</li>
<li>the dispute is high-conflict or there is a significant power imbalance;</li>
<li>you want a specific, experienced accredited mediator;</li>
<li>timing is important — FRC waiting lists could delay resolution;</li>
<li>you need a flexible process that can accommodate lawyers attending if required;</li>
<li>you want the matter handled with specialist expertise.</li>
</ul>
"""
        + inline_cta(
            "Private mediation doesn't have to be unaffordable — Access Mediation assesses your contribution individually.",
            btn="See how Access Mediation works"
        )
        + f"""
<h2 id="gap">What If an FRC Is Not Suitable but Standard Fees Are Difficult?</h2>
<p>For many people, an FRC is not ideal — perhaps the matter involves property
settlement, waiting times are too long, or the dispute is too complex for a
generalist service. But standard private mediation fees may also be difficult
to meet.</p>
<p>Access Mediation is designed precisely for this situation. It provides specialist
accredited private mediation at an assessed reduced contribution based on each
participant's own financial capacity. It is not free, but it may be significantly
more affordable than standard private rates for eligible participants.</p>
<p>See the <a href="/access-mediation/">Access Mediation page</a> to check your
indicative contribution. For a broader overview of options, see
<a href="/cant-afford-mediation/">Can't afford mediation? Your options in Australia</a>.</p>
<p><em>General information only. This is not legal advice. Check {cite('ag_frc')}
for current FRC availability in your area.</em></p>
"""
    ),
    qa=[
        ("Is a Family Relationship Centre the same as a private mediator?",
         "No. FRCs are government-funded services operating under a Commonwealth "
         "program. Private mediators are independently accredited practitioners "
         "operating outside the government FDR system. Both can facilitate FDR and "
         "issue section 60I certificates, but they differ in cost, availability, "
         "focus, and complexity of matters handled."),
        ("Can I go to both an FRC and a private mediator?",
         "Yes. You might use an FRC for a section 60I certificate on a parenting "
         "matter and then engage a private mediator for a property settlement. "
         "However, a registered FDR provider who is also a private mediator can "
         "handle both in one process."),
        ("Do I need to try an FRC before using a private mediator?",
         "For parenting matters, the Family Law Act requires genuine participation "
         "in FDR before filing parenting orders in court — but this does not have "
         "to be at an FRC. A registered FDR provider, which includes many private "
         "mediators, can satisfy the section 60I requirement."),
        ("Are FRCs available everywhere in Australia?",
         "FRCs are available in most major Australian cities and many regional "
         "areas, but they are not uniformly distributed. Remote areas may have "
         "limited local access. Some FRCs offer online or telephone services."),
        ("What is the quality difference between an FRC and a private mediator?",
         "Both must be registered FDR practitioners. However, private mediators "
         "are more likely to have specialist family law mediation experience and "
         "to handle complex property or high-conflict matters regularly. The FRC "
         "model is designed for accessibility and general parenting disputes."),
    ],
    related=[
        ("legal-aid-vs-private-mediation",            "Legal Aid vs Private Mediation"),
        ("is-family-mediation-free-australia",        "Is Family Mediation Free?"),
        ("cant-afford-mediation",                     "Can't Afford Mediation?"),
        ("access-mediation",                          "Access Mediation"),
        ("low-cost-family-mediation-australia",       "Low-Cost Family Mediation"),
        ("family-law-mediation",                      "Family Law Mediation"),
    ],
    read_min=8,
)


# ─────────────────────────────────────────────────────────────────────────────
# PAGE 8 — /legal-aid-vs-private-mediation/
# ─────────────────────────────────────────────────────────────────────────────
post(
    "legal-aid-vs-private-mediation",
    "Legal Aid vs Private Mediation: Which Is Right for You?",
    "Legal Aid vs private mediation in Australia — what Legal Aid covers for family mediation, how it compares with private options, and what to do if you don't qualify.",
    "Family Mediation",
    "Legal Aid vs Private Mediation: <em>Which Option Is Right for You?</em>",
    ("Legal Aid and private mediation are not the same thing — and understanding the "
     "difference can help you choose the right pathway for your family law matter. "
     "This guide explains what Legal Aid covers, how private mediation compares, and "
     "what your options are if you do not qualify for Legal Aid."),
    [
        ("what-is-legal-aid",  "What is Legal Aid in the family law context?"),
        ("what-is-private",    "What is private mediation?"),
        ("comparison",         "Comparison table"),
        ("questions",          "Six questions to ask before choosing"),
        ("dont-qualify",       "What if I don't qualify for Legal Aid?"),
        ("where-access-fits",  "Where Access Mediation fits"),
    ],
    body=(
        key_takeaway(
            "Legal Aid provides funded legal assistance to eligible people in lower income "
            "brackets — it is not itself a mediation service. Private mediation is a "
            "separately delivered process. If you do not qualify for Legal Aid and "
            "cannot afford standard private fees, a reduced-fee private pathway "
            "such as Access Mediation may be appropriate."
        )
        + f"""
<h2 id="what-is-legal-aid">What Is Legal Aid in the Family Law Context?</h2>
<p>Legal Aid commissions operate in each state and territory of Australia to provide
funded legal assistance to people who cannot afford private legal representation.
{cite('legal_aid')} provides national information, but each commission operates
independently with its own means test, merit test, and service scope.</p>
<p>In a family law context, Legal Aid may:</p>
<ul>
<li>provide legal advice on your rights and entitlements;</li>
<li>represent you in court proceedings (subject to eligibility);</li>
<li>fund or facilitate participation in mediation or family dispute resolution;</li>
<li>fund attendance at a Legal Aid conciliation conference in some jurisdictions;</li>
<li>refer you to low-cost community FDR services.</li>
</ul>
<p>Legal Aid is not a mediation service — it is a funding and legal assistance
service. Whether and how it facilitates mediation depends on the jurisdiction and
your eligibility. Eligibility requires passing both a means test and a merit test.</p>

<h2 id="what-is-private">What Is Private Mediation?</h2>
<p>Private mediation is a process facilitated by an accredited mediator that helps
participants reach an agreed resolution of their dispute. Private mediators operate
outside the government Legal Aid and FDR funding systems.</p>
<p>Mediators must be accredited under the {cite('amdras')} standards. For family
matters requiring a section 60I certificate under the {cite('family_law_act')},
the mediator must also be a registered FDR provider.</p>
<p>Private mediation covers the full range of family matters: parenting arrangements,
property settlement, superannuation splitting, spousal maintenance, and combined
disputes.</p>
"""
        + inline_cta(
            "Not sure whether Legal Aid applies to your situation? A free consultation can help clarify your options.",
            btn="Book a free consultation"
        )
        + f"""
<h2 id="comparison">Comparison Table</h2>
<figure class="tbl" style="overflow-x:auto">
<table>
<caption>Legal Aid, community FDR, and private mediation compared</caption>
<thead>
<tr>
  <th>Factor</th><th>Legal Aid</th><th>Community / FRC</th>
  <th>Standard private</th><th>Reduced-fee private</th>
</tr>
</thead>
<tbody>
<tr><td>Cost</td>
  <td>Free if eligible</td>
  <td>Free to subsidised</td>
  <td>$1,500–$2,250 pp</td>
  <td>From $495 + GST pp assessed</td></tr>
<tr><td>Eligibility test</td>
  <td>Means + merit test</td>
  <td>Varies by provider</td>
  <td>None</td>
  <td>Income + asset assessment</td></tr>
<tr><td>What it provides</td>
  <td>Legal advice, representation, possible FDR funding</td>
  <td>FDR facilitation</td>
  <td>Mediation facilitation</td>
  <td>Mediation facilitation</td></tr>
<tr><td>Mediator choice</td>
  <td>Assigned or referred</td>
  <td>Assigned by provider</td>
  <td>Request specific mediator</td>
  <td>Request specific mediator</td></tr>
<tr><td>Property settlement</td>
  <td>Varies — legal advice more common</td>
  <td>Limited</td>
  <td>Well-suited</td>
  <td>Well-suited</td></tr>
<tr><td>Speed</td>
  <td>Variable; waiting lists possible</td>
  <td>Often weeks–months</td>
  <td>1–2 weeks typically</td>
  <td>1–2 weeks typically</td></tr>
</tbody>
</table>
</figure>
<p><em>Legal Aid services vary significantly between states and territories.
Check with your state commission for current eligibility criteria.</em></p>

<h2 id="questions">Six Questions to Ask Before Choosing</h2>
<ol>
<li><strong>Do I meet the eligibility requirements for Legal Aid?</strong>
    Contact your state commission and ask about the means and merit tests for
    family law matters. If you do not qualify, move to the next question.</li>
<li><strong>How quickly do I need this resolved?</strong>
    Government-funded services can have significant waiting times. Private
    mediation is generally faster.</li>
<li><strong>Is my matter complex?</strong>
    Property settlement, superannuation, and high-conflict matters may be better
    handled by a specialist accredited mediator.</li>
<li><strong>Can I afford standard private fees?</strong>
    If not, check whether you qualify for Access Mediation or another reduced-fee
    pathway before assuming Legal Aid is your only option.</li>
<li><strong>Do I need independent legal advice specifically?</strong>
    Legal Aid can provide legal advice as well as facilitate dispute resolution.
    If you need legal advice rather than mediation facilitation, Legal Aid or a
    community legal centre may be more directly relevant.</li>
<li><strong>Is a section 60I certificate needed?</strong>
    Both Legal Aid services and registered private mediators can facilitate
    this process for parenting matters.</li>
</ol>
"""
        + inline_cta(
            "If you don't qualify for Legal Aid, that doesn't mean standard private fees are your only option.",
            btn="Explore Access Mediation"
        )
        + f"""
<h2 id="dont-qualify">What If I Don't Qualify for Legal Aid?</h2>
<p>Not qualifying for Legal Aid does not mean you are left with only full-price options.
Several alternatives may be available:</p>
<ul>
<li><strong>Community legal centres:</strong> Many provide free legal advice regardless
    of income. They generally cannot fund representation or mediation, but they can
    help you understand your position before engaging a mediator.</li>
<li><strong>Family Relationship Centres:</strong> Free or subsidised FDR, primarily
    for parenting matters. See
    <a href="/family-relationship-centre-vs-private-mediation/">FRC vs private
    mediation</a> for a comparison.</li>
<li><strong>Reduced-fee private mediation:</strong> An individually assessed
    contribution pathway where your fee is based on your income, accessible assets,
    and circumstances — not a flat standard rate.</li>
</ul>
<p>See <a href="/cant-afford-mediation/">Can't afford mediation? Your options in
Australia</a> for a full overview.</p>

<h2 id="where-access-fits">Where Access Mediation Fits</h2>
<p>Access Mediation sits in the gap between government-funded services and standard
private mediation. It is designed for people who:</p>
<ul>
<li>earn too much for Legal Aid but cannot comfortably pay standard private rates;</li>
<li>do not qualify for free FRC services or community FDR;</li>
<li>have a matter that is too complex for a generalist government-funded service;</li>
<li>want a specialist accredited mediator with greater flexibility and speed.</li>
</ul>
<p>Under Access Mediation, your contribution is assessed individually based on your
personal income, accessible assets, dependants, and circumstances. The assessment
is private.</p>
<p>Contributions start from $495 + GST per person for a 3-hour session. See the
<a href="/access-mediation/">Access Mediation page</a> to check your indicative
contribution.</p>
<p><em>General information only. This is not legal advice. Legal Aid eligibility
varies by state and territory — contact your local commission for current criteria.
{cite('legal_aid')} provides state commission contact details.</em></p>
"""
    ),
    qa=[
        ("Is Legal Aid a mediation service?",
         "No. Legal Aid provides legal advice, representation, and in some "
         "jurisdictions facilitation of or funding for FDR participation. It is "
         "not itself a mediation service. Whether and how Legal Aid facilitates "
         "mediation depends on your state and specific eligibility."),
        ("Can I use both Legal Aid and private mediation?",
         "Potentially. Legal Aid could provide legal advice or representation "
         "while you use a private mediator for the FDR process. Discuss with "
         "your Legal Aid commission what assistance they can provide alongside "
         "a private mediation process."),
        ("Does private mediation count as FDR for section 60I certificate purposes?",
         "Yes — if the private mediator is a registered FDR provider. Most "
         "accredited family mediators are also registered FDR providers and can "
         "issue section 60I certificates when attendance requirements are met."),
        ("Will Legal Aid pay for my private mediator?",
         "This depends on your state commission and specific circumstances. "
         "Some commissions will fund participation in private FDR; others refer "
         "clients to community services. Contact your state commission directly."),
        ("Is reduced-fee private mediation the same as a Legal Aid conciliation?",
         "No. A Legal Aid conciliation conference is a government-funded process "
         "run by the Legal Aid commission. Reduced-fee private mediation is a "
         "privately run service with an assessed contribution for eligible "
         "participants. They are different processes with different eligibility "
         "and procedural rules."),
    ],
    related=[
        ("family-relationship-centre-vs-private-mediation", "FRC vs Private Mediation"),
        ("cant-afford-mediation",                           "Can't Afford Mediation?"),
        ("is-family-mediation-free-australia",              "Is Family Mediation Free?"),
        ("access-mediation",                                "Access Mediation"),
        ("low-cost-family-mediation-australia",             "Low-Cost Family Mediation"),
        ("our-fee-structure",                               "Our Fee Structure"),
    ],
    read_min=9,
)
