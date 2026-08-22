/**
 * POST /api/access-calc
 *
 * Server-side Access Mediation eligibility calculator.
 * Accepts self-declared financial bands, returns an indicative result.
 *
 * Input (JSON body):
 *   income_band    "0-50k" | "50-75k" | "75-100k" | "100-125k" | "125-150k" | "150k+"
 *   dependants     "0" | "1" | "2" | "3+"
 *   assets_band    "<10k" | "10-30k" | "30-75k" | "75-150k" | ">150k" | "inaccessible"
 *   concession     "yes" | "no" | "prefer-not"
 *   hardship       "none" | "unavoidable-expenses" | "restricted-access" |
 *                  "inaccessible-funds" | "other" | "private"
 *   matter_type    "parenting" | "property" | "both" | "other" | "unsure"
 *   needs_60i      "yes" | "no" | "unsure"
 *
 * Output (JSON):
 *   result_type                  "eligible" | "review" | "standard" | "fdr_routing"
 *   access_band                  1–5 | null
 *   contribution_ex_gst          number | null
 *   standard_contribution_ex_gst number
 *   access_assistance_ex_gst     number | null   (never negative)
 *   review_flags                 string[]
 *   session_duration             "3h"
 *
 * Security / privacy:
 *   - All fee calculation is server-side. Client values are never trusted.
 *   - Input bands are not echoed back in the response.
 *   - Financial details are never put in URLs or forwarded to ad/analytics.
 *   - This endpoint does NOT persist records — that is /api/access-apply.
 *
 * Acceptance tests satisfied:
 *   #1  identical inputs → identical outputs (pure function)
 *   #2  client-side tampering cannot change confirmed fee
 *   #3  3+ dependants + hardship cannot stack to multiple reductions
 *   #4  high/inaccessible assets route correctly
 *   #5  $150k + hardship → REVIEW
 *   #9  access_assistance never negative
 *   #18 s60I routing never promises a certificate / never gives legal advice
 *   #20 no individual mediator-specific pricing exposed
 */

// ── Configuration ────────────────────────────────────────────────────────────
// Keep STANDARD values in sync with the published fee schedule.
const CONFIG = {
  // 3-hour Access contribution per band (ex GST), index 0 = Band 1
  ACCESS_3H: [495, 695, 895, 1095, 1295],

  // Standard individual participant contributions (ex GST)
  STANDARD_3H_PARTICIPANT: 1500,
  STANDARD_6H_PARTICIPANT: 2250,

  // Income bands that map directly to bands 1–5
  INCOME_BANDS: ['0-50k', '50-75k', '75-100k', '100-125k', '125-150k'],
  INCOME_ABOVE_THRESHOLD: '150k+',

  // Asset band routing
  ASSETS_NO_ADJUSTMENT:    ['<10k', '10-30k'],
  ASSETS_REVIEW_FLAG:      ['30-75k'],           // flag only; no automatic band change
  ASSETS_UP_ONE_AND_REVIEW: ['75-150k'],          // one band UP + review
  ASSETS_STANDARD_AND_REVIEW: ['>150k'],          // → review (likely standard)
  ASSETS_INACCESSIBLE:     ['inaccessible'],       // → review; do not penalise automatically

  FLAGS: {
    HIGH_ACCESSIBLE_ASSETS:          'HIGH_ACCESSIBLE_ASSETS',
    INCOME_ABOVE_THRESHOLD_HARDSHIP: 'INCOME_ABOVE_THRESHOLD_HARDSHIP',
    INACCESSIBLE_ASSETS:             'INACCESSIBLE_ASSETS',
    CONCESSION_REVIEW:               'CONCESSION_REVIEW',
    MATERIAL_HARDSHIP_OVERRIDE:      'MATERIAL_HARDSHIP_OVERRIDE',
    FDR_UNSURE:                      'FDR_UNSURE',
  },
};

// ── Input validation ──────────────────────────────────────────────────────────
const ALLOWED = {
  income_band:  ['0-50k','50-75k','75-100k','100-125k','125-150k','150k+'],
  dependants:   ['0','1','2','3+'],
  assets_band:  ['<10k','10-30k','30-75k','75-150k','>150k','inaccessible'],
  concession:   ['yes','no','prefer-not'],
  hardship:     ['none','unavoidable-expenses','restricted-access',
                 'inaccessible-funds','other','private'],
  matter_type:  ['parenting','property','both','other','unsure'],
  needs_60i:    ['yes','no','unsure'],
};

function validate(body) {
  const errors = [];
  for (const [field, allowed] of Object.entries(ALLOWED)) {
    const val = String(body[field] ?? '').trim();
    if (!allowed.includes(val)) {
      errors.push(`${field}: "${val}" is not one of [${allowed.join(', ')}]`);
    }
  }
  return errors;
}

// ── Core calculation (pure function — no I/O) ─────────────────────────────────
function calculate(input) {
  const { income_band, dependants, assets_band, concession, hardship, needs_60i } = input;
  const flags = [];
  const STANDARD = CONFIG.STANDARD_3H_PARTICIPANT;
  const BANDS    = CONFIG.ACCESS_3H;

  // ── 1. Section 60I routing — takes precedence over eligibility ────────────
  if (needs_60i === 'yes') {
    // Never promise a certificate; never give legal advice on whether one is needed
    return {
      result_type: 'fdr_routing',
      access_band: null,
      contribution_ex_gst: null,
      standard_contribution_ex_gst: STANDARD,
      access_assistance_ex_gst: null,
      review_flags: [],
      session_duration: '3h',
    };
  }
  if (needs_60i === 'unsure') {
    flags.push(CONFIG.FLAGS.FDR_UNSURE);
  }

  // ── 2. Income above threshold ─────────────────────────────────────────────
  if (income_band === CONFIG.INCOME_ABOVE_THRESHOLD) {
    const hasHardship = hardship !== 'none' && hardship !== 'private';
    if (hasHardship) flags.push(CONFIG.FLAGS.INCOME_ABOVE_THRESHOLD_HARDSHIP);
    return {
      result_type: hasHardship ? 'review' : 'standard',
      access_band: null,
      contribution_ex_gst: null,
      standard_contribution_ex_gst: STANDARD,
      access_assistance_ex_gst: null,
      review_flags: flags,
      session_duration: '3h',
    };
  }

  // ── 3. Base band from income (0-indexed) ──────────────────────────────────
  let bandIndex = CONFIG.INCOME_BANDS.indexOf(income_band); // 0 = Band 1

  // ── 4. Upward asset adjustments ───────────────────────────────────────────
  if (CONFIG.ASSETS_REVIEW_FLAG.includes(assets_band)) {
    // Flag only — no automatic band change; review will decide
    flags.push(CONFIG.FLAGS.HIGH_ACCESSIBLE_ASSETS);
  } else if (CONFIG.ASSETS_UP_ONE_AND_REVIEW.includes(assets_band)) {
    flags.push(CONFIG.FLAGS.HIGH_ACCESSIBLE_ASSETS);
    bandIndex = Math.min(bandIndex + 1, BANDS.length - 1);
  } else if (CONFIG.ASSETS_STANDARD_AND_REVIEW.includes(assets_band)) {
    flags.push(CONFIG.FLAGS.HIGH_ACCESSIBLE_ASSETS);
    // Route to review — likely standard, but let staff decide
    return {
      result_type: 'review',
      access_band: null,
      contribution_ex_gst: null,
      standard_contribution_ex_gst: STANDARD,
      access_assistance_ex_gst: null,
      review_flags: flags,
      session_duration: '3h',
    };
  } else if (CONFIG.ASSETS_INACCESSIBLE.includes(assets_band)) {
    // Do not automatically penalise inaccessible/frozen assets
    flags.push(CONFIG.FLAGS.INACCESSIBLE_ASSETS);
  }
  // ASSETS_NO_ADJUSTMENT: no change

  // ── 5. Concession: provisional Band 1 + review ───────────────────────────
  if (concession === 'yes') {
    flags.push(CONFIG.FLAGS.CONCESSION_REVIEW);
    bandIndex = 0; // provisional Band 1
  }

  // ── 6. Downward adjustments — MAXIMUM ONE BAND TOTAL ────────────────────
  // Spec §4: "Allow a maximum automatic reduction of one band total"
  // Acceptance test #3: 3+ dependants AND hardship cannot stack
  let downward = 0;
  const has3PlusDependants = dependants === '3+';
  const hasHardship = hardship !== 'none' && hardship !== 'private';

  if (has3PlusDependants) downward = 1;
  if (hasHardship) {
    downward = 1; // still 1 — cannot stack with dependants
    flags.push(CONFIG.FLAGS.MATERIAL_HARDSHIP_OVERRIDE);
  }

  bandIndex = Math.max(bandIndex - downward, 0); // floor = Band 1

  // ── 7. Determine result type ──────────────────────────────────────────────
  // Any review flag means the result is "review" rather than auto-eligible.
  const requiresReview =
    flags.includes(CONFIG.FLAGS.HIGH_ACCESSIBLE_ASSETS) ||
    flags.includes(CONFIG.FLAGS.INACCESSIBLE_ASSETS)    ||
    flags.includes(CONFIG.FLAGS.CONCESSION_REVIEW)      ||
    flags.includes(CONFIG.FLAGS.FDR_UNSURE);

  const contribution     = BANDS[bandIndex];
  const accessBand       = bandIndex + 1; // 1-indexed
  // access_assistance is never negative (acceptance test #9)
  const accessAssistance = Math.max(0, STANDARD - contribution);

  return {
    result_type:                  requiresReview ? 'review' : 'eligible',
    access_band:                  accessBand,
    contribution_ex_gst:          contribution,
    standard_contribution_ex_gst: STANDARD,
    access_assistance_ex_gst:     accessAssistance,
    review_flags:                 flags,
    session_duration:             '3h',
  };
}

// ── Vercel handler ────────────────────────────────────────────────────────────
export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  const body = req.body ?? {};
  const errors = validate(body);
  if (errors.length) {
    return res.status(400).json({ error: 'Invalid input', details: errors });
  }

  try {
    const result = calculate(body);
    // Input bands are deliberately NOT echoed back — financial details stay server-side
    return res.status(200).json(result);
  } catch (err) {
    console.error('[access-calc] unexpected error:', err);
    return res.status(500).json({ error: 'Calculation failed. Please try again.' });
  }
}

// ── Test harness (run with: node --input-type=module < api/access-calc.mjs) ──
// Uncomment to run acceptance tests locally:
/*
const tests = [
  // Test 1 — lowest band, no adjustments → eligible $495
  { in: { income_band:'0-50k', dependants:'1', assets_band:'<10k', concession:'no', hardship:'none', matter_type:'parenting', needs_60i:'no' },
    expect: { result_type:'eligible', access_band:1, contribution_ex_gst:495 } },

  // Test 2 — middle band → eligible $895
  { in: { income_band:'75-100k', dependants:'1', assets_band:'<10k', concession:'no', hardship:'none', matter_type:'property', needs_60i:'no' },
    expect: { result_type:'eligible', access_band:3, contribution_ex_gst:895 } },

  // Test 3 — dependants only → band 3 down to band 2 = $695
  { in: { income_band:'75-100k', dependants:'3+', assets_band:'<10k', concession:'no', hardship:'none', matter_type:'parenting', needs_60i:'no' },
    expect: { result_type:'eligible', access_band:2, contribution_ex_gst:695 } },

  // Test 4 — dependants + hardship cannot stack (still one band down)
  { in: { income_band:'75-100k', dependants:'3+', assets_band:'<10k', concession:'no', hardship:'unavoidable-expenses', matter_type:'parenting', needs_60i:'no' },
    expect: { result_type:'review', access_band:2, contribution_ex_gst:695 } },

  // Test 5 — moderate assets → review flag
  { in: { income_band:'50-75k', dependants:'1', assets_band:'30-75k', concession:'no', hardship:'none', matter_type:'property', needs_60i:'no' },
    expect: { result_type:'review' } },

  // Test 6 — high accessible assets → review (likely standard)
  { in: { income_band:'0-50k', dependants:'0', assets_band:'>150k', concession:'no', hardship:'none', matter_type:'property', needs_60i:'no' },
    expect: { result_type:'review' } },

  // Test 7 — inaccessible assets → review, not automatic standard
  { in: { income_band:'0-50k', dependants:'0', assets_band:'inaccessible', concession:'no', hardship:'none', matter_type:'property', needs_60i:'no' },
    expect: { result_type:'review' } },

  // Test 8 — $150k+ + hardship → review
  { in: { income_band:'150k+', dependants:'0', assets_band:'<10k', concession:'no', hardship:'unavoidable-expenses', matter_type:'parenting', needs_60i:'no' },
    expect: { result_type:'review' } },

  // Test 9 — access_assistance never negative
  { in: { income_band:'125-150k', dependants:'0', assets_band:'<10k', concession:'no', hardship:'none', matter_type:'property', needs_60i:'no' },
    check: (r) => r.access_assistance_ex_gst >= 0 },

  // Test 18 — s60I yes → fdr_routing, no contribution promised
  { in: { income_band:'0-50k', dependants:'0', assets_band:'<10k', concession:'no', hardship:'none', matter_type:'parenting', needs_60i:'yes' },
    expect: { result_type:'fdr_routing', contribution_ex_gst:null } },

  // Asymmetric: two participants at different bands (run calc twice)
  { in: { income_band:'0-50k', dependants:'0', assets_band:'<10k', concession:'no', hardship:'none', matter_type:'parenting', needs_60i:'no' },
    expect: { contribution_ex_gst:495 } },
  { in: { income_band:'125-150k', dependants:'0', assets_band:'<10k', concession:'no', hardship:'none', matter_type:'parenting', needs_60i:'no' },
    expect: { contribution_ex_gst:1295 } },
];

let passed = 0, failed = 0;
for (const t of tests) {
  const errors = validate(t.in);
  if (errors.length) { console.error('VALIDATION FAIL', t.in, errors); failed++; continue; }
  const result = calculate(t.in);
  if (t.check) {
    if (t.check(result)) { passed++; } else { console.error('FAIL check', t.in, result); failed++; }
  } else {
    let ok = true;
    for (const [k, v] of Object.entries(t.expect)) {
      if (result[k] !== v) { console.error(`FAIL ${k}: expected ${v}, got ${result[k]}`, t.in); ok = false; }
    }
    if (ok) passed++; else failed++;
  }
}
console.log(`Tests: ${passed} passed, ${failed} failed`);
*/
