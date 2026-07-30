#!/usr/bin/env python3
"""Generate sitemap.xml and robots.txt for the full site."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import DOMAIN, SERVICES
from location_data import LOCATION_DATA

OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATE = "2026-05-28"

urls = [("", "1.0", "weekly")]
core = ["family-law-mediation","how-mediation-works","about-mediations-australia",
        "preparing-for-mediation","contact-us","book-a-consultation",
        "estate-dispute-mediation","collaborative-family-lawyers","family-law-arbitration",
        "divorce-counselling","our-fee-structure",
        "parenting-plan-template","bfa-or-consent-orders","getting-ready-for-separation",
        "family-law-cost-estimator","separation-under-one-roof",
        "guides","cost-of-divorce-in-australia","mediation-with-a-narcissist",
        "what-am-i-entitled-to-in-a-separation-in-australia","how-long-does-mediation-take",
        "consent-orders-explained","property-settlement-after-separation",
        "how-to-get-a-divorce-in-australia-a-step-by-step-guide","binding-financial-agreements-guide","parenting-plans-guide",
        "what-is-mediation-in-family-law","mediate-or-litigate","child-custody-mediation","domestic-violence-and-family-law",
        "separation-guide","de-facto-relationships-guide","spousal-maintenance-guide","child-support-guide",
        "is-family-law-mediation-compulsory","fathers-rights","superannuation-and-divorce","high-conflict-mediation",
        "mothers-rights","grandparents-rights","shuttle-mediation-guide","conciliation-vs-mediation","workplace-mediation-guide",
        "property-settlement-mediation-guide","business-in-divorce","family-court-process","divorce-without-a-lawyer","how-long-does-a-divorce-take",
        "how-much-does-mediation-cost","arbitration-in-family-law","pets-and-family-law","same-sex-family-law","changes-to-family-law-act-2025","stepparent-rights","surrogacy-laws","can-you-record-your-ex","best-divorce-lawyers-sydney","parental-alienation-australia","our-mediators","memberships","mediation-podcast","books",
        "who-pays-for-mediation","private-vs-free-mediation","divorce-mediator-vs-divorce-lawyer","mediation-before-divorce","what-happens-if-mediation-fails","what-is-in-the-property-pool","delaying-property-settlement","co-parenting-mediation"]
for c in core:
    urls.append((c, "0.9", "monthly"))
for s, _, _ in SERVICES:
    urls.append((s, "0.9", "monthly"))
for row in LOCATION_DATA:
    urls.append((row[0], "0.8", "monthly"))

entries = ""
for slug, pri, freq in urls:
    loc = f"{DOMAIN}/" if slug == "" else f"{DOMAIN}/{slug}/"
    entries += f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{DATE}</lastmod>
    <changefreq>{freq}</changefreq>
    <priority>{pri}</priority>
  </url>
"""

sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{entries}</urlset>
"""
with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
    f.write(sitemap)

robots = f"""User-agent: *
Allow: /

# AI answer engines are welcome to crawl and cite
User-agent: GPTBot
Allow: /
User-agent: OAI-SearchBot
Allow: /
User-agent: PerplexityBot
Allow: /
User-agent: Google-Extended
Allow: /
User-agent: ClaudeBot
Allow: /
User-agent: Claude-Web
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
"""
with open(os.path.join(OUT, "robots.txt"), "w") as f:
    f.write(robots)

print(f"sitemap.xml written with {len(urls)} URLs")
print("robots.txt written")
