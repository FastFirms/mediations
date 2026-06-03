#!/usr/bin/env python3
"""Build-time check: every blog post must have >=2 authoritative external links."""
import re, glob, os
SITE="/home/claude/mediations/site"
AUTH_DOMAINS=['gov.au','abs.','austlii','.edu','aifs.gov','1800respect','psychiatry.org','msb.org','fwc.gov','ato.gov']

# blog posts only (not service/location pages)
BLOG=['cost-of-divorce-in-australia','mediation-with-a-narcissist','consent-orders-explained','property-settlement-after-separation','how-to-get-a-divorce-in-australia-a-step-by-step-guide','binding-financial-agreements-guide','parenting-plans-guide','what-is-mediation-in-family-law','mediate-or-litigate','child-custody-mediation','domestic-violence-and-family-law','separation-guide','de-facto-relationships-guide','spousal-maintenance-guide','child-support-guide','is-family-law-mediation-compulsory','fathers-rights','superannuation-and-divorce','high-conflict-mediation','mothers-rights','grandparents-rights','shuttle-mediation-guide','conciliation-vs-mediation','workplace-mediation-guide','property-settlement-mediation-guide','business-in-divorce','family-court-process','divorce-without-a-lawyer','how-long-does-a-divorce-take','how-much-does-mediation-cost','arbitration-in-family-law','pets-and-family-law','same-sex-family-law','changes-to-family-law-act-2025','stepparent-rights','surrogacy-laws','can-you-record-your-ex','best-divorce-lawyers-sydney',
      'what-am-i-entitled-to-in-a-separation-in-australia','how-long-does-mediation-take']

def content_only(s):
    s=re.sub(r'<header.*?</header>','',s,flags=re.S)
    s=re.sub(r'<footer.*?</footer>','',s,flags=re.S)
    return s

print("=== AUTHORITY LINK STANDARD CHECK (min 2 per post) ===")
allpass=True
for slug in BLOG:
    p=os.path.join(SITE,slug,"index.html")
    if not os.path.exists(p): continue
    s=content_only(open(p).read())
    links=re.findall(r'href=[\'"](https?://[^\'"]+)[\'"]',s)
    auth=[l for l in links if any(d in l for d in AUTH_DOMAINS)]
    status="PASS" if len(auth)>=2 else "FAIL — needs more"
    if len(auth)<2: allpass=False
    print(f"  [{status}] {slug}: {len(auth)} authority links")
print()
print("ALL POSTS MEET STANDARD" if allpass else "SOME POSTS BELOW STANDARD — add citations")
