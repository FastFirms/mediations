"""Workplace mediation pricing — the ONLY source of workplace fees on the site.

Dan-approved 7 November 2026 (brief §5, "Approved workplace pricing — single source of truth").
Use ONLY on workplace/employment URLs. Never import into family/FDR, estate, property or
commercial pages: those use their own fee sources (family fees are locked).

Visible copy and JSON-LD are both rendered from WORKPLACE below, so they cannot disagree.
Do not add terms that have not been approved (session hours, cancellation, extra sessions,
initial-consultation scope, outcome documents).
"""
from templates import DOMAIN

GST = 0.10

WORKPLACE = {
    "half_day_ex": 2200,
    "full_day_ex": 3800,
    "extra_party_ex": 500,
    "included_parties": 2,
    "intake_included": True,      # an intake session with each party
    "travel": "quoted separately",
    "group_facilitation": "quoted on request",
}


def inc(ex):
    """GST-inclusive total (10%), as an int — arithmetic only, not a new fee decision."""
    return int(round(ex * (1 + GST)))


def money(n):
    return f"${n:,}"


def price_block(heading_tag="h3"):
    """The approved customer-facing workplace pricing block (brief §5)."""
    w = WORKPLACE
    h, f, x = w["half_day_ex"], w["full_day_ex"], w["extra_party_ex"]
    return f"""<div class="answer" style="border-left-color:var(--sage-deep)">
<{heading_tag} style="margin-top:0">Workplace mediation pricing</{heading_tag}>
<figure class="tbl" style="margin:0 0 .75rem"><table>
<thead><tr><th>Option</th><th>Fee</th><th>Including GST</th></tr></thead>
<tbody>
<tr><td><strong>Half day</strong></td><td>{money(h)} + GST</td><td>{money(inc(h))}</td></tr>
<tr><td><strong>Full day</strong></td><td>{money(f)} + GST</td><td>{money(inc(f))}</td></tr>
<tr><td>Each additional party</td><td>{money(x)} + GST</td><td>{money(inc(x))}</td></tr>
</tbody></table></figure>
<p>Standard pricing covers <strong>two parties</strong> and includes <strong>an intake session with each party and the mediation session</strong>. Prices are totals for the engagement, not per person. Intake with each additional participating party remains included.</p>
<p><strong>Travel is extra and quoted separately.</strong> <strong>Group or team facilitation is quoted on request.</strong></p>
</div>"""


def offers_schema(page_slug):
    """Offers for the workplace Service node (GST-inclusive prices, tax flag true)."""
    w = WORKPLACE
    url = f"{DOMAIN}/{page_slug}/"

    def offer(name, ex, desc):
        p = inc(ex)
        return {"@type": "Offer", "name": name, "description": desc, "url": url,
                "price": p, "priceCurrency": "AUD",
                "priceSpecification": {"@type": "UnitPriceSpecification", "price": p,
                                       "priceCurrency": "AUD", "valueAddedTaxIncluded": True}}
    scope = ("Covers two parties; includes an intake session with each party and the mediation "
             "session. Travel quoted separately.")
    return [
        offer("Workplace mediation — half day, two parties", w["half_day_ex"], scope),
        offer("Workplace mediation — full day, two parties", w["full_day_ex"], scope),
        offer("Additional party (workplace mediation)", w["extra_party_ex"],
              "Surcharge per additional participating party; intake with that party included."),
    ]


def faq_answers():
    """Pricing FAQ answers built from the same config (no separate hard-coded figures)."""
    w = WORKPLACE
    h, f, x = w["half_day_ex"], w["full_day_ex"], w["extra_party_ex"]
    return {
        "cost": (f"Mediations Australia charges {money(h)} + GST ({money(inc(h))}) for a half-day workplace "
                 f"mediation or {money(f)} + GST ({money(inc(f))}) for a full day. The fee covers two parties and "
                 f"includes an intake session with each party and the mediation session. Each extra party is "
                 f"{money(x)} + GST; travel is quoted separately."),
        "per_person": (f"No. Standard fees are totals for the engagement and cover two parties. Each additional "
                       f"party is {money(x)} + GST ({money(inc(x))})."),
        "more_parties": (f"Each additional party is {money(x)} + GST, and intake with that party is included. For "
                         f"example, three parties would be {money(h + x)} + GST for a half day or {money(f + x)} + GST "
                         f"for a full day, before any travel. Group or team facilitation is quoted on request."),
        "intake": "Yes. Standard pricing includes an intake session with each party as well as the mediation session.",
        "travel": "No. Travel is extra and quoted separately.",
    }
