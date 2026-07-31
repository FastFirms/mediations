#!/usr/bin/env python3
"""Generate URL migration map: CSV + .htaccess + nginx redirect snippets."""
import os, sys, csv
sys.path.insert(0, os.path.dirname(__file__))
from slugmap_data import PAGE_MAP
OUT="/home/claude/mediations/site"

# Blog post slug map: most keep their slug (rebuilt). A few consolidate.
# (old_slug, action, new_slug)
BLOG_BUILT = ["cost-of-divorce-in-australia","mediation-with-a-narcissist",
              "what-am-i-entitled-to-in-a-separation-in-australia","how-long-does-mediation-take"]

# Known duplicate/legacy blog slugs that should consolidate to a canonical post:
BLOG_CONSOLIDATE = {
 "the-cost-of-divorce-in-australia":"cost-of-divorce-in-australia",
 "how-much-does-mediation-cost":"costs-of-mediation",
 "what-am-i-entitled-to-in-a-separation":"what-am-i-entitled-to-in-a-separation-in-australia",
 "what-am-i-entitled-to-in-a-divorce-or-separation-in-australia":"what-am-i-entitled-to-in-a-separation-in-australia",
 "how-to-get-ready-for-mediation":"preparing-for-mediation",
 "how-to-prepare-for-a-property-settlement-mediation":"preparing-for-mediation",
 "how-to-get-ready-for-property-settlement-mediation":"preparing-for-mediation",
 "shuttle-mediation":"the-pros-and-cons-of-shuttle-mediation",
 "consent-order":"consent-orders",
 "spousal-maintenance":"spousal-support-mediation",
 "de-facto-relationships":"de-facto-mediation",
 "separated-under-one-roof":"separation-under-one-roof",
 "divorce-without-a-lawyer":"divorce-without-lawyers",
}

rows=[]
for old,(action,new) in PAGE_MAP.items():
    rows.append((old or "(home)", action, new or "(home)"))
for old in BLOG_BUILT:
    rows.append((old,"rebuilt-this-phase",old))
for old,new in BLOG_CONSOLIDATE.items():
    rows.append((old,"redirect-301",new))

# Write CSV
with open(os.path.join(OUT,"url-migration-map.csv"),"w",newline="") as f:
    w=csv.writer(f); w.writerow(["old_url","action","new_url"])
    for old,act,new in rows:
        oldu = "/" if old=="(home)" else f"/{old}/"
        newu = "/" if new=="(home)" else f"/{new}/"
        w.writerow([oldu,act,newu])

# Write .htaccess redirect snippet (only for redirect/consolidate actions)
with open(os.path.join(OUT,"redirects.htaccess"),"w") as f:
    f.write("# 301 redirects for Mediations Australia rebuild\n")
    f.write("# Generated migration map — review before deploying\n\n")
    for old,act,new in rows:
        if "redirect" in act:
            oldu = "/" if old=="(home)" else f"/{old}/"
            newu = "/" if new=="(home)" else f"/{new}/"
            f.write(f"Redirect 301 {oldu} {newu}\n")

print(f"Migration map written: {len(rows)} mapped URLs")
print(f"  - url-migration-map.csv")
print(f"  - redirects.htaccess ({sum(1 for _,a,_ in rows if 'redirect' in a)} 301s)")
