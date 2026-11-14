#!/usr/bin/env python3
"""Post-build: add one contextual body link to /sydney-mediation/ on each source page
(LOCATION-PAGES-REWRITE.md, Fix 4). Idempotent: run after any generator rebuild."""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A = lambda t: f'<a href="/sydney-mediation/">{t}</a>'
LINKS = {
 "index": f"Based in Sydney? Our {A('Sydney mediation')} team works from Kent St in the CBD, and we mediate online Australia-wide.",
 "how-much-does-mediation-cost": f"Fees are the same wherever you are; see {A('mediation costs in Sydney')} for how they compare with the local court route.",
 "parenting-mediation-sydney": f"This page covers parenting matters; for every other service see {A('Sydney mediation')}.",
 "property-settlement-mediation-sydney": f"Part of our {A('mediation across Sydney')}, focused on dividing property, super and debts.",
 "workplace-mediation-sydney": f"Looking for family or commercial help instead? See our {A('other Sydney mediation services')}.",
 "parenting-plan-mediation": f"We also offer {A('parenting mediation in Sydney')} at our Kent St office, as well as online.",
 "property-settlement-mediation": f"Prefer to meet in person? Our {A('Sydney property mediators')} work from Kent St in the CBD.",
 "commercial-mediation": f"We offer {A('commercial mediation in Sydney')} in person, and online nationally.",
 "estate-dispute-mediation": f"In NSW, family provision claims are usually mediated before trial; our {A('Sydney estate mediation')} service can help early.",
 "consent-orders": f"Reaching agreement first is quicker and cheaper; many couples {A('mediate in Sydney before filing')}.",
 "is-family-law-mediation-compulsory": f"To get a section 60I certificate you need an accredited practitioner; we have {A('accredited FDR practitioners in Sydney')}, and we also work online.",
 "family-relationship-centre-vs-private-mediation": f"If Family Relationship Centre waits are too long, {A('private mediation in Sydney')} can usually start within days.",
 "online-mediation-australia": f"Would you rather meet face to face? We offer {A('in-person mediation in our Sydney office')}.",
 "our-team": f"Several of our mediators are based at Kent St and {A('mediate in Sydney')} as well as online.",
 "contact-us": f"Find out more about our {A('Sydney mediation services')}.",
}
MARK = 'data-syd-link'
n = 0
for slug, sentence in LINKS.items():
    p = os.path.join(ROOT, "index.html" if slug == "index" else f"{slug}/index.html")
    if not os.path.exists(p):
        print("missing", slug); continue
    d = open(p).read()
    if MARK in d:
        continue
    i = d.find("<main")
    h = d.find("<h2", i)
    # skip headings in the key-takeaway box or hidden form-success panels
    while h > 0 and re.search(r"Key takeaway|Enquiry received|Thank", d[h:d.find("</h2>", h)]):
        h = d.find("<h2", h + 3)
    j = d.find("</p>", h if h > 0 else i)
    if j < 0:
        print("no anchor point", slug); continue
    j += 4
    d = d[:j] + f'\n<p {MARK}>{sentence}</p>' + d[j:]
    open(p, "w").write(d); n += 1
print(f"Sydney links injected: {n}")
