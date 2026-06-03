#!/usr/bin/env python3
"""Booking / consultation page with an accessible form."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from templates import (head, nav, page_end, esc, crumb_html, org_schema,
                       breadcrumb_schema, PHONE, PHONE_HREF, SERVICES)
OUT = os.environ.get("MED_SITE_OUT") or os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

opts="".join(f'<option value="{esc(n)}">{esc(n)}</option>' for _,n,_ in SERVICES)
opts+='<option value="Estate dispute">Estate dispute</option><option value="Commercial dispute">Commercial dispute</option><option value="Other / not sure">Other / not sure</option>'

title="Book a Free Consultation | Mediations Australia · 1800 952 380"
desc=("Book a fixed-fee mediation consultation with Mediations Australia. "
      "Tell us about your dispute and we'll explain how mediation can help — no obligation. Call 1800 952 380.")
schema=[org_schema(),breadcrumb_schema([("Home",""),("Book a Consultation","book-a-consultation")])]
d=head(title,desc,"book-a-consultation",extra_schema=schema)+nav()
d+=f"""<main id="main">
{crumb_html([("Home",""),("Book a Consultation",None)])}
<section class="phero"><div class="phero-blob"></div><div class="wrap">
<span class="eyebrow"><span class="pulse"></span>Fixed-fee · No obligation · In person or online</span>
<h1>Book a Free Consultation — <em>take the first step</em>.</h1>
<p class="lede">Tell us about your dispute and we'll give you an honest view of whether mediation can help, how it works, and what it costs. There's no obligation, and the first conversation costs nothing but a few minutes.</p>
</div></section>
<section class="sec" style="padding-top:20px"><div class="wrap" style="max-width:920px">
<div class="reveal book-grid">
<form id="bookform" action="https://formspree.io/f/mredjobj" method="POST" novalidate style="background:var(--cream);border:1px solid var(--line);border-radius:var(--r);padding:36px;display:flex;flex-direction:column;gap:18px">
  <!-- Spam honeypot: hidden from humans, bots fill it -->
  <input type="text" name="_gotcha" tabindex="-1" autocomplete="off" style="position:absolute;left:-9999px;opacity:0" aria-hidden="true">
  <!-- Email subject sent to your inbox -->
  <input type="hidden" name="_subject" value="New consultation request — Mediations Australia">
  <div>
    <label for="name" style="display:block;font-weight:600;margin-bottom:6px;font-size:.95rem">Your name <span aria-hidden="true" style="color:var(--terra)">*</span></label>
    <input id="name" name="name" type="text" required autocomplete="name" style="width:100%;padding:13px 15px;border:1.5px solid var(--line);border-radius:10px;font-family:var(--sans);font-size:1rem;background:var(--sand)">
  </div>
  <div style="display:flex;gap:14px;flex-wrap:wrap">
    <div style="flex:1;min-width:180px">
      <label for="email" style="display:block;font-weight:600;margin-bottom:6px;font-size:.95rem">Email <span aria-hidden="true" style="color:var(--terra)">*</span></label>
      <input id="email" name="email" type="email" required autocomplete="email" style="width:100%;padding:13px 15px;border:1.5px solid var(--line);border-radius:10px;font-family:var(--sans);font-size:1rem;background:var(--sand)">
    </div>
    <div style="flex:1;min-width:180px">
      <label for="phone" style="display:block;font-weight:600;margin-bottom:6px;font-size:.95rem">Phone <span aria-hidden="true" style="color:var(--terra)">*</span></label>
      <input id="phone" name="phone" type="tel" required autocomplete="tel" style="width:100%;padding:13px 15px;border:1.5px solid var(--line);border-radius:10px;font-family:var(--sans);font-size:1rem;background:var(--sand)">
    </div>
  </div>
  <div>
    <label for="matter" style="display:block;font-weight:600;margin-bottom:6px;font-size:.95rem">What's your matter about?</label>
    <select id="matter" name="matter" style="width:100%;padding:13px 15px;border:1.5px solid var(--line);border-radius:10px;font-family:var(--sans);font-size:1rem;background:var(--sand)">
      <option value="">Please choose…</option>{opts}
    </select>
  </div>
  <div>
    <label for="location" style="display:block;font-weight:600;margin-bottom:6px;font-size:.95rem">Your location</label>
    <input id="location" name="location" type="text" placeholder="e.g. Melbourne, or 'online'" style="width:100%;padding:13px 15px;border:1.5px solid var(--line);border-radius:10px;font-family:var(--sans);font-size:1rem;background:var(--sand)">
  </div>
  <div>
    <label for="message" style="display:block;font-weight:600;margin-bottom:6px;font-size:.95rem">Briefly, how can we help? <span style="font-weight:400;color:var(--ink-soft)">(optional)</span></label>
    <textarea id="message" name="message" rows="4" style="width:100%;padding:13px 15px;border:1.5px solid var(--line);border-radius:10px;font-family:var(--sans);font-size:1rem;background:var(--sand);resize:vertical"></textarea>
  </div>
  <button type="submit" class="btn btn-primary" style="justify-content:center;font-size:1.05rem">Request my consultation <span class="arr">→</span></button>
  <p id="formnote" role="status" aria-live="polite" style="font-size:.88rem;color:var(--ink-soft);margin:0">We'll respond within one business day. Your details are kept private and confidential.</p>
</form>
<aside>
  <div style="background:var(--sage-deep);color:var(--cream);border-radius:var(--r);padding:30px">
    <h2 style="color:var(--cream);font-size:1.4rem;margin-bottom:14px">Prefer to talk now?</h2>
    <p style="color:rgba(251,248,242,.85);margin-bottom:20px;font-size:.98rem">Call us directly and speak with our team about your situation.</p>
    <a href="{PHONE_HREF}" class="btn btn-primary" style="justify-content:center;width:100%">Call {PHONE}</a>
    <div style="margin-top:26px;padding-top:22px;border-top:1px solid rgba(251,248,242,.18);display:flex;flex-direction:column;gap:14px;font-size:.95rem">
      <div style="display:flex;gap:10px"><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M6 10.5l2.5 2.5L14 7" stroke="#a8c89f" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Fixed-fee, no surprises</div>
      <div style="display:flex;gap:10px"><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M6 10.5l2.5 2.5L14 7" stroke="#a8c89f" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>In person or online</div>
      <div style="display:flex;gap:10px"><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M6 10.5l2.5 2.5L14 7" stroke="#a8c89f" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>Nationally accredited mediators</div>
      <div style="display:flex;gap:10px"><svg width="20" height="20" viewBox="0 0 20 20" fill="none"><path d="M6 10.5l2.5 2.5L14 7" stroke="#a8c89f" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>90% resolved without court</div>
    </div>
  </div>
</aside>
</div>
</div></section>
</main>"""
d+=page_end().replace("</script>","""
const f=document.getElementById('bookform');
if(f){f.addEventListener('submit',async function(e){
  e.preventDefault();
  const note=document.getElementById('formnote');
  const btn=f.querySelector('button[type=submit]');
  const req=['name','email','phone'];let ok=true;
  req.forEach(id=>{const el=document.getElementById(id);
    if(!el.value.trim()){el.style.borderColor='var(--terra)';ok=false;}
    else{el.style.borderColor='var(--line)';}});
  if(!ok){note.textContent='Please complete the required fields so we can get back to you.';note.style.color='var(--terra-deep)';return;}
  // honeypot tripped -> silently pretend success (don't tip off bots)
  if(f.querySelector('[name=_gotcha]').value){
    note.textContent='Thank you \\u2014 your request has been received.';
    note.style.color='var(--sage-deep)';btn.textContent='Request sent \\u2713';btn.disabled=true;return;
  }
  btn.disabled=true;btn.textContent='Sending\\u2026';
  note.textContent='Sending your request\\u2026';note.style.color='var(--ink-soft)';
  try{
    const res=await fetch(f.action,{method:'POST',body:new FormData(f),headers:{Accept:'application/json'}});
    if(res.ok){
      note.textContent='Thank you \\u2014 your request has been received. We\\'ll be in touch within one business day.';
      note.style.color='var(--sage-deep)';btn.textContent='Request sent \\u2713';f.reset();
    }else{
      const data=await res.json().catch(()=>({}));
      const msg=(data.errors&&data.errors.map(x=>x.message).join(', '))||'Sorry, something went wrong. Please try again, or call us on 1800 952 380.';
      note.textContent=msg;note.style.color='var(--terra-deep)';btn.disabled=false;btn.textContent='Request my consultation';
    }
  }catch(err){
    note.textContent='Network error \\u2014 please try again, or call us on 1800 952 380.';
    note.style.color='var(--terra-deep)';btn.disabled=false;btn.textContent='Request my consultation';
  }
});}
</script>""")
open(os.path.join(OUT,"book-a-consultation","index.html") if os.makedirs(os.path.join(OUT,"book-a-consultation"),exist_ok=True) or True else "","w").write(d)
print("Booking page built.")
