#!/usr/bin/env python3
"""Validate that every blog cornerstone links to ≥1 service pillar and /book-a-consultation/.

Fails the build if any cornerstone is missing either requirement.
Run after any rebuild that touches blog generator files.
"""
import re, glob, os, sys

OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Service pillar slugs that count as "links up to a commercial pillar"
PILLARS = {
    "family-law-mediation", "divorce-mediation", "property-settlement-mediation",
    "parenting-plan-mediation", "section-60i-certificates", "financial-agreements-mediation",
    "spousal-support-mediation", "child-support-mediation", "de-facto-mediation",
    "grandparents-mediation", "consent-orders", "online-divorce", "workplace-mediation",
    "estate-dispute-mediation", "collaborative-family-lawyers", "family-law-arbitration",
}

BOOK_SLUG = "book-a-consultation"

# Keep in sync with check_authority.py's BLOG list.
BLOG = [
    "cost-of-divorce-in-australia","mediation-with-a-narcissist",
    "what-am-i-entitled-to-in-a-separation-in-australia","how-long-does-mediation-take",
    "consent-orders-explained","property-settlement-after-separation",
    "how-to-get-a-divorce-in-australia-a-step-by-step-guide","binding-financial-agreements-guide",
    "parenting-plans-guide","what-is-mediation-in-family-law","mediate-or-litigate",
    "child-custody-mediation","domestic-violence-and-family-law","separation-guide",
    "de-facto-relationships-guide","spousal-maintenance-guide","child-support-guide",
    "is-family-law-mediation-compulsory","fathers-rights-after-separation","superannuation-and-divorce",
    "high-conflict-mediation","mothers-rights","grandparents-rights","shuttle-mediation-guide",
    "conciliation-vs-mediation","workplace-mediation-guide","property-settlement-mediation-guide",
    "business-in-divorce","family-court-process","divorce-without-a-lawyer",
    "how-long-does-a-divorce-take","how-much-does-mediation-cost","arbitration-in-family-law",
    "pets-and-family-law","same-sex-family-law","changes-to-family-law-act-2025",
    "stepparent-rights","surrogacy-laws","can-you-record-your-ex",
    "best-divorce-lawyers-sydney","parental-alienation-australia",
    "who-pays-for-mediation","private-vs-free-mediation","divorce-mediator-vs-divorce-lawyer",
    "mediation-before-divorce","what-happens-if-mediation-fails","what-is-in-the-property-pool",
    "delaying-property-settlement","co-parenting-mediation",
]

fails = []

for slug in BLOG:
    path = os.path.join(OUT, slug, "index.html")
    if not os.path.exists(path):
        fails.append(f"  [MISSING] /{slug}/ — file not found")
        continue

    html = open(path).read()
    hrefs = set(re.findall(r'href="/([a-z0-9-]+)/', html))

    missing = []
    if not (hrefs & PILLARS):
        missing.append("no service pillar link")
    if BOOK_SLUG not in hrefs:
        missing.append("no /book-a-consultation/ link")

    if missing:
        fails.append(f"  [FAIL] /{slug}/: {', '.join(missing)}")

for f in fails:
    print(f)

print(f"\nChecked {len(BLOG)} cornerstones.")
if fails:
    print(f"{len(fails)} LINKING VIOLATIONS — add in-body links to service pillars and /book-a-consultation/")
    sys.exit(1)
else:
    print("ALL CORNERSTONES MEET LINKING STANDARD")
