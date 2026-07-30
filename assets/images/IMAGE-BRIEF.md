# Image brief — Mediations Australia

Purpose: licensed stock photography to humanise the site and break the "AI-default"
look. **Mood and context only.** Stock people must NEVER be presented as our actual
mediators or clients — the team page and bylines need real photos (separate track).

Hand finished selections to the build (high-res JPEG/PNG, see specs). They'll be
converted to WebP, sized, and wired in via the `img()` helper with width/height +
lazy-loading so Core Web Vitals aren't harmed.

---

## The authenticity test (this is what makes stock help vs. hurt)

**DO choose images that are:**
- Natural, candid, available-light — looks like a real moment, not a studio shoot
- Calm, hopeful, forward-looking (resolution, not conflict or grief)
- Australian in feel where people/places are shown
- Warm/muted in tone so they sit with the sand + sage + terracotta palette
- Roomy — negative space on one side for headline/text overlay (hero especially)

**DON'T use the clichés (these read as template/stock instantly):**
- Handshakes, gavels, scales of justice, courtrooms, contracts being signed
- "Head in hands" sadness, couples arguing, a wedding ring being removed
- Staged "perfect family on a white sofa", isolated-on-white studio people
- Anything glossy, corporate-blue, or obviously a model with a fake laugh

**Never:** present a stock person as a named mediator/staff member.

---

## Where images go (priority order)

| # | Placement | Mood / subject | Aspect | Min width | Treatment |
|---|---|---|---|---|---|
| 1 | **Homepage hero** | Two people talking calmly across a kitchen/cafe table; or a person looking forward outdoors; or a quiet warm interior detail. Hopeful, not literal. | 3:2 | 1800px | warm, soft light, space for text |
| 2 | **About page** | A real-feeling, lived-in workspace / meeting room (not a glossy boardroom) | 3:2 | 1600px | natural |
| 3 | **Location heroes** (Sydney, Melbourne, Brisbane, Perth) | Tasteful, recognisable local scene — skyline, harbour, a calm streetscape | 16:9 | 1600px | muted, not postcard-garish |
| 4 | **Service section breaks** (family, divorce, property, parenting) | One calm contextual image each — parent + child outdoors; keys/home detail; a person on a walk; kids playing. Non-cliché. | 21:9 band | 1800px | subtle, low-contrast |
| 5 | **Guides** (optional) | Per-article header where a strong, non-cliché image exists | 3:2 | 1400px | optional |

Start with #1–3; they do most of the tempering. You don't need an image on every page.

---

## Suggested sources & search terms

- **Better for authenticity (paid):** Stocksy, Adobe Stock, Gallery Stock — far less
  cliché than the free libraries.
- **Free (license is fine, but pick carefully — overused images still hurt):**
  Unsplash, Pexels.
- **Search terms that tend to surface real-feeling shots:** "candid conversation
  kitchen table", "two people talking cafe natural light", "walking outdoors
  hopeful", "Australian home keys", "parent child park backlit", "Sydney harbour
  calm morning", "warm meeting room daylight".
- **Always preview at the size it'll display** and ask: does this look like a real
  moment, or like stock? If you hesitate, skip it.

---

## Sizes

You only supply ONE master per image — the largest the stock site offers. We
downscale, compress, and generate the responsive set. Never upscale a small file.

| Placement | Aspect | Displays up to | Source master (≥) | Ships as (WebP) |
|---|---|---|---|---|
| Homepage hero | 3:2 | ~1280px | 2400px wide | ≤180 KB |
| Location heroes | 16:9 | ~1150px | 2300px wide | ≤160 KB |
| Section bands | 21:9 | ~1150px | 2300px wide | ≤140 KB |
| About | 3:2 | ~760px | 1600px wide | ≤120 KB |
| Office card | 3:2 | ~460px | 1000px wide | ≤70 KB |

- **Source master ≈ 2× the display width** — covers retina/high-DPI screens.
- We generate variants (800 / 1200 / 1600 / 2400px) + `srcset`, so phones never
  download the desktop file.
- The **hero is the LCP element** and must stay light (≤180 KB); it's the only
  large image above the fold. Everything else lazy-loads.

## Technical specs for delivery

- Format in: high-quality JPEG or PNG (we convert to WebP/AVIF).
- Provide the largest size available (we downscale; we can't upscale).
- Landscape orientation for all placements above.
- Filename: lowercase-with-hyphens, descriptive (`homepage-hero-kitchen-talk.jpg`).
- Drop files in `/assets/images/`. Tell us the intended placement and a one-line
  description (for alt text) per image.
- We handle: WebP/AVIF conversion, responsive sizing + `srcset`, `width`/`height`,
  lazy-loading, alt text, and hero `fetchpriority` so the page stays fast.
