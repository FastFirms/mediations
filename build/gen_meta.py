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
        "family-lawyers","estate-dispute-mediation","collaborative-family-lawyers","family-law-arbitration",
        "commercial-mediation","real-estate-mediation","elder-mediation",
        "divorce-counselling","our-fee-structure",
        "parenting-plan-template","bfa-or-consent-orders","getting-ready-for-separation",
        "family-law-cost-estimator","separation-under-one-roof",
        "unfair-dismissal-21-day-rule","is-mediation-right-for-workplace-dispute",
        "redundancy-was-it-genuine","contesting-a-will","commercial-dispute-guide",
        "real-estate-construction-disputes","workplace-dispute-guide",
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
        "who-pays-for-mediation","private-vs-free-mediation","divorce-mediator-vs-divorce-lawyer","mediation-before-divorce","what-happens-if-mediation-fails","what-is-in-the-property-pool","delaying-property-settlement","co-parenting-mediation","online-mediation-australia","victorian-right-to-work-from-home","belbin-team-roles-training",
        "prepare-for-mediation",
        # service-city pages
        "property-settlement-mediation-sydney","divorce-mediation-sydney",
        "parenting-mediation-sydney","workplace-mediation-sydney",
        "property-settlement-mediation-melbourne","divorce-mediation-melbourne",
        "parenting-mediation-melbourne","workplace-mediation-melbourne",
        "property-settlement-mediation-brisbane","divorce-mediation-brisbane",
        "parenting-mediation-brisbane","workplace-mediation-brisbane",
        "property-settlement-mediation-perth","divorce-mediation-perth",
        "parenting-mediation-perth","workplace-mediation-perth",
        "property-settlement-mediation-adelaide","divorce-mediation-adelaide",
        "parenting-mediation-adelaide","workplace-mediation-adelaide",
        "property-settlement-mediation-canberra","divorce-mediation-canberra",
        "parenting-mediation-canberra","workplace-mediation-canberra",
        "property-settlement-mediation-gold-coast","divorce-mediation-gold-coast",
        "parenting-mediation-gold-coast","workplace-mediation-gold-coast",
        "how-we-help","privacy-policy",
        "unfair-dismissal-termination-mediation","workplace-bullying-harassment-mediation",
        "general-protections-discrimination-mediation","partnership-executive-exit-mediation",
        "redundancy-restructure-mediation","workplace-investigations-grievance-mediation",
        # Q&A knowledge hub
        "questions",
        "questions/do-i-need-mediation-before-family-court",
        "questions/what-if-my-ex-refuses-mediation",
        "questions/what-is-a-section-60i-certificate",
        "questions/who-can-issue-a-section-60i-certificate",
        "questions/how-much-does-family-mediation-cost",
        "questions/how-long-does-family-mediation-take",
        "questions/what-happens-if-family-mediation-fails",
        "questions/is-family-mediation-confidential",
        "questions/can-mediation-cover-parenting-and-property",
        "questions/can-i-bring-a-lawyer-to-family-mediation",
        "questions/mediation-family-violence-coercive-control",
        "questions/what-is-shuttle-mediation",
        "questions/how-much-does-mediation-cost",
        "questions/how-long-does-mediation-take",
        "questions/what-happens-during-mediation",
        "questions/do-i-need-a-lawyer-for-mediation",
        "questions/is-mediation-legally-binding",
        "questions/when-should-hr-use-an-external-mediator",
        "questions/workplace-investigation-vs-mediation",
        "questions/is-workplace-mediation-confidential",
        "best-apps-for-separated-parents",
        "my-ex-wont-sign-divorce-papers",
        "who-pays-bills-during-separation",
        "questions/what-is-family-dispute-resolution",
        "questions/whats-the-difference-between-mediation-and-family-dispute-resolution",
        "questions/when-can-i-be-exempt-from-family-dispute-resolution",
        "questions/can-i-get-a-s60i-certificate-without-attending-mediation",
        "questions/how-long-is-a-s60i-certificate-valid",
        "questions/can-grandparents-use-family-mediation",
        "questions/can-we-make-a-parenting-plan-at-mediation",
        "questions/can-property-settlement-be-resolved-through-mediation",
        "questions/can-mediation-happen-online",
        "questions/what-should-i-bring-to-family-mediation",
        "questions/how-does-workplace-mediation-work",
        "questions/can-an-employee-refuse-workplace-mediation",
        "questions/can-a-support-person-attend-workplace-mediation",
        "questions/can-workplace-mediation-deal-with-bullying-allegations",
        "questions/what-happens-if-workplace-mediation-fails",
        "questions/how-much-does-commercial-mediation-cost",
        "questions/how-does-commercial-mediation-work",
        "questions/mediation-vs-arbitration-whats-the-difference",
        "questions/should-i-mediate-a-shareholder-dispute",
        "questions/can-business-partners-use-mediation",
        "questions/can-mediation-resolve-a-contract-dispute",
        "questions/is-commercial-mediation-confidential",
        "questions/can-lawyers-attend-commercial-mediation",
        "questions/what-happens-if-commercial-mediation-fails",
        "questions/can-you-mediate-a-contested-will",
        "questions/what-is-estate-mediation",
        "questions/can-mediation-resolve-an-inheritance-dispute",
        "questions/how-much-does-estate-mediation-cost",
        "questions/when-should-an-estate-dispute-go-to-mediation",
        "questions/what-happens-if-estate-mediation-fails",
        # Access Mediation SEO cluster
        "cant-afford-mediation",
        "is-family-mediation-free-australia",
        "low-cost-family-mediation-australia",
        "who-pays-mediation-one-person-earns-more",
        "does-mediation-have-to-be-paid-50-50",
        "asset-rich-cash-poor-mediation",
        "family-relationship-centre-vs-private-mediation",
        "legal-aid-vs-private-mediation"]
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
