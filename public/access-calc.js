/**
 * Access Mediation — multi-step contribution calculator + application form.
 * Mounts into: <div id="access-calc-root">
 *
 * Steps:
 *   1  income_band     · Your income
 *   2  dependants      · Dependants
 *   3  assets_band     · Accessible assets
 *   4  concession      · Concession card
 *   5  hardship        · Financial hardship
 *   6  matter_type     · Matter type
 *   7  needs_60i       · Section 60I
 *   8  → POST /api/access-calc → show result
 *   9  (if eligible/review) → application form → POST /api/access-apply → confirmation
 *
 * Privacy rules (build-pack §19):
 *   - Never put financial answers in URLs.
 *   - Answers live only in JS module state and are sent once, server-side, over HTTPS.
 *   - No financial inputs are echoed back in the result display.
 *   - Analytics events carry only step numbers and result type — never financial values.
 */
(function () {
  'use strict';

  var root = document.getElementById('access-calc-root');
  if (!root) return;

  // ── Palette / brand tokens ───────────────────────────────────────────────
  var GREEN = '#1e6040';
  var DEEP  = '#0d2218';
  var SAND  = '#f1f5f1';
  var LINE  = 'rgba(13,34,24,.14)';
  var MUTED = '#3d5248';
  var FONT  = '"Hanken Grotesk",-apple-system,BlinkMacSystemFont,sans-serif';

  // ── In-memory state (never written to URL or localStorage) ──────────────
  var answers = {
    income_band: null, dependants: null, assets_band: null,
    concession: null, hardship: null, matter_type: null, needs_60i: null,
  };
  var calcResult  = null;
  var applyResult = null;
  var currentStep = 0;

  var STEPS = [
    {
      key: 'income_band',
      topic: 'Your income',
      question: 'What is your personal gross annual income?',
      hint: 'Your individual income — not household income.',
      options: [
        { value: '0-50k',    label: 'Up to $50,000' },
        { value: '50-75k',   label: '$50,001 – $75,000' },
        { value: '75-100k',  label: '$75,001 – $100,000' },
        { value: '100-125k', label: '$100,001 – $125,000' },
        { value: '125-150k', label: '$125,001 – $150,000' },
        { value: '150k+',    label: 'More than $150,000' },
      ],
    },
    {
      key: 'dependants',
      topic: 'Dependants',
      question: 'How many financial dependants do you have?',
      hint: 'Children or other persons financially dependent on you.',
      options: [
        { value: '0',  label: 'None' },
        { value: '1',  label: '1 dependant' },
        { value: '2',  label: '2 dependants' },
        { value: '3+', label: '3 or more dependants' },
      ],
    },
    {
      key: 'assets_band',
      topic: 'Accessible assets',
      question: 'What are your accessible financial assets (approximate total)?',
      hint: 'Savings, shares, investment properties and similar. Not your family home or superannuation.',
      options: [
        { value: '<10k',         label: 'Under $10,000' },
        { value: '10-30k',       label: '$10,000 – $30,000' },
        { value: '30-75k',       label: '$30,001 – $75,000' },
        { value: '75-150k',      label: '$75,001 – $150,000' },
        { value: '>150k',        label: 'Over $150,000' },
        { value: 'inaccessible', label: 'Assets are frozen or inaccessible' },
      ],
    },
    {
      key: 'concession',
      topic: 'Concession card',
      question: 'Do you hold a current government concession card?',
      hint: 'For example, a Health Care Card, Pensioner Concession Card, or DVA card.',
      options: [
        { value: 'yes',        label: 'Yes' },
        { value: 'no',         label: 'No' },
        { value: 'prefer-not', label: 'Prefer not to say' },
      ],
    },
    {
      key: 'hardship',
      topic: 'Financial hardship',
      question: 'Are you experiencing any of the following financial hardship?',
      hint: 'Select the option that best describes your situation.',
      options: [
        { value: 'none',                 label: 'No particular hardship' },
        { value: 'unavoidable-expenses', label: 'Unavoidable major expenses (medical, housing, care)' },
        { value: 'restricted-access',    label: 'Income significantly restricted (parental leave, carer, illness)' },
        { value: 'inaccessible-funds',   label: 'Funds frozen or disputed in the separation' },
        { value: 'other',                label: 'Other significant hardship' },
        { value: 'private',              label: 'I have hardship but prefer not to specify' },
      ],
    },
    {
      key: 'matter_type',
      topic: 'Matter type',
      question: 'What type of family law matter do you have?',
      hint: '',
      options: [
        { value: 'parenting', label: 'Parenting arrangements (children)' },
        { value: 'property',  label: 'Property settlement' },
        { value: 'both',      label: 'Both parenting and property' },
        { value: 'other',     label: 'Other family law matter' },
        { value: 'unsure',    label: 'Not sure yet' },
      ],
    },
    {
      key: 'needs_60i',
      topic: 'Section 60I',
      question: 'Do you need a Section 60I certificate?',
      hint: 'Required before most parenting applications to the Federal Circuit and Family Court. Select "Not sure" if you are unsure.',
      options: [
        { value: 'yes',    label: 'Yes, I need one' },
        { value: 'no',     label: 'No' },
        { value: 'unsure', label: 'Not sure' },
      ],
    },
  ];

  // ── Analytics (privacy-safe — never send financial values) ───────────────
  function track(name, params) {
    try {
      if (typeof gtag === 'function') gtag('event', name, params || {});
    } catch (e) { /* silently ignore */ }
  }

  // ── Styles ────────────────────────────────────────────────────────────────
  var css = [
    // Container — 660px wide, centred (brief §4)
    '#acc-calc{font-family:' + FONT + ';max-width:660px;margin:0 auto;background:#fff;border-radius:14px;padding:28px 32px;box-shadow:0 2px 12px rgba(13,34,24,.08)}',

    // Progress — label + bar (brief §5)
    '#acc-step-label{font-size:.82rem;font-weight:700;color:' + GREEN + ';letter-spacing:.04em;text-transform:uppercase;margin:0 0 10px}',
    '#acc-progress{display:flex;gap:6px;margin-bottom:24px}',
    '.acc-pip{flex:1;height:5px;border-radius:3px;background:' + LINE + ';transition:background .3s}',
    '.acc-pip.done{background:' + GREEN + '}',
    '.acc-pip.active{background:' + GREEN + ';opacity:.5}',

    // Question
    '#acc-question{font-size:1.1rem;font-weight:700;color:' + DEEP + ';margin:0 0 6px;line-height:1.4}',
    '#acc-hint{font-size:.84rem;color:' + MUTED + ';margin:0 0 20px;line-height:1.5}',

    // Options — large click targets (brief §6)
    '.acc-options{display:flex;flex-direction:column;gap:10px}',
    '.acc-opt{display:flex;align-items:center;gap:14px;padding:14px 18px;border:1.5px solid ' + LINE + ';',
    '  border-radius:10px;cursor:pointer;background:#fff;transition:border-color .15s,background .15s;text-align:left;width:100%;min-height:52px}',
    '.acc-opt:hover,.acc-opt:focus{border-color:' + GREEN + ';background:' + SAND + ';outline:none}',
    '.acc-opt.selected{border-color:' + GREEN + ';background:' + SAND + '}',
    '.acc-opt-dot{width:18px;height:18px;border-radius:50%;border:2px solid ' + LINE + ';flex-shrink:0;transition:border-color .15s,background .15s}',
    '.acc-opt.selected .acc-opt-dot{border-color:' + GREEN + ';background:' + GREEN + '}',
    '.acc-opt-label{font-size:.95rem;color:' + DEEP + ';font-weight:500;line-height:1.4}',

    // Back button
    '#acc-back{background:none;border:none;color:' + MUTED + ';font-size:.83rem;cursor:pointer;padding:0;margin-top:16px;text-decoration:underline}',

    // Result box — three-row breakdown (brief §9)
    '#acc-result{padding:26px;border-radius:14px;border:2px solid ' + GREEN + ';background:#fff;margin-top:6px}',
    '.acc-res-rows{margin:0 0 20px;border-radius:8px;overflow:hidden;border:1px solid ' + LINE + '}',
    '.acc-res-row{display:flex;justify-content:space-between;align-items:center;padding:10px 14px;font-size:.9rem;border-bottom:1px solid ' + LINE + ';background:#fafafa}',
    '.acc-res-row:last-child{border-bottom:none;background:' + SAND + ';padding:14px;font-weight:700}',
    '.acc-res-row-label{color:' + MUTED + '}',
    '.acc-res-row-value{color:' + DEEP + ';font-weight:600}',
    '.acc-res-row:last-child .acc-res-row-label{color:' + DEEP + ';font-weight:700}',
    '.acc-res-price{font-size:2.4rem;font-weight:800;color:' + GREEN + ';line-height:1;margin:0 0 4px}',
    '.acc-res-sub{font-size:.86rem;color:' + MUTED + ';margin:0 0 20px;line-height:1.5}',
    '.acc-res-disclaimer{font-size:.78rem;color:' + MUTED + ';line-height:1.5;margin-top:16px;padding-top:12px;border-top:1px solid ' + LINE + '}',

    // Buttons
    '.acc-apply-btn{display:inline-flex;align-items:center;gap:8px;background:' + GREEN + ';color:#fff;',
    '  border:none;border-radius:100px;padding:13px 28px;font-family:' + FONT + ';font-size:.95rem;font-weight:700;cursor:pointer;transition:background .2s;text-decoration:none}',
    '.acc-apply-btn:hover{background:' + DEEP + ';color:#fff}',
    '.acc-talk-link{display:inline-block;margin-left:16px;font-size:.88rem;color:' + GREEN + ';text-decoration:underline;vertical-align:middle}',
    '.acc-btn-row{margin-top:18px;display:flex;flex-wrap:wrap;align-items:center;gap:10px}',

    // Review note
    '.acc-review-note{padding:13px 16px;background:#fff9e6;border-left:4px solid #f0a500;border-radius:0 8px 8px 0;font-size:.86rem;line-height:1.6;margin-bottom:18px}',

    // Application form
    '.acc-form{margin-top:22px}',
    '.acc-form h3{color:' + DEEP + ';margin:0 0 18px;font-size:1rem}',
    '.acc-field{margin-bottom:16px}',
    '.acc-field label{display:block;font-size:.86rem;font-weight:600;color:' + DEEP + ';margin-bottom:4px}',
    '.acc-field input,.acc-field textarea,.acc-field select{width:100%;box-sizing:border-box;border:1.5px solid ' + LINE + ';',
    '  border-radius:9px;padding:10px 13px;font-family:' + FONT + ';font-size:.88rem;color:' + DEEP + ';background:' + SAND + ';outline:none;transition:border-color .2s}',
    '.acc-field input:focus,.acc-field textarea:focus{border-color:' + GREEN + ';background:#fff}',
    '.acc-section-label{font-size:.88rem;font-weight:700;color:' + DEEP + ';margin:22px 0 6px;border-bottom:1px solid ' + LINE + ';padding-bottom:6px}',
    '.acc-section-hint{font-size:.79rem;color:' + MUTED + ';margin-bottom:12px;line-height:1.5}',
    '.acc-consent{display:flex;gap:10px;align-items:flex-start;margin-bottom:10px}',
    '.acc-consent input[type=checkbox]{margin-top:3px;flex-shrink:0;accent-color:' + GREEN + '}',
    '.acc-consent label{font-size:.83rem;color:' + MUTED + ';line-height:1.5}',
    '.acc-consent a{color:' + GREEN + '}',
    '.acc-submit{display:block;width:100%;background:' + GREEN + ';color:#fff;border:none;border-radius:100px;',
    '  padding:14px 20px;font-family:' + FONT + ';font-size:.95rem;font-weight:700;cursor:pointer;transition:background .2s;margin-top:12px}',
    '.acc-submit:hover{background:' + DEEP + '}',
    '.acc-submit:disabled{opacity:.4;cursor:default}',
    '.acc-error{padding:11px 15px;background:#fdecea;border-left:4px solid #d32f2f;border-radius:0 8px 8px 0;font-size:.86rem;color:#b71c1c;margin:10px 0}',
    '.acc-confirm{text-align:center;padding:30px 16px}',
    '.acc-confirm-icon{font-size:2.6rem;margin-bottom:10px;color:' + GREEN + '}',
    '.acc-confirm h3{color:' + GREEN + ';margin:0 0 10px;font-size:1.1rem}',
    '.acc-confirm p{font-size:.9rem;color:' + MUTED + ';line-height:1.6;margin:0 0 10px}',
    '.acc-confirm strong{color:' + DEEP + '}',
    '.acc-restart{display:inline-block;margin-top:16px;font-size:.83rem;color:' + GREEN + ';cursor:pointer;text-decoration:underline}',
    '.acc-loading{text-align:center;padding:40px 0;color:' + MUTED + ';font-size:.88rem}',
    '.acc-field-hint{font-size:.77rem;color:' + MUTED + ';margin:3px 0 0;line-height:1.4}',

    // Mobile (brief §21)
    '@media(max-width:600px){',
    '#acc-calc{padding:20px 16px;border-radius:10px}',
    '.acc-opt{padding:13px 14px;min-height:48px}',
    '.acc-res-price{font-size:2rem}',
    '.acc-apply-btn{width:100%;justify-content:center}',
    '.acc-talk-link{display:block;margin:8px 0 0}',
    '}',
  ].join('');

  var styleEl = document.createElement('style');
  styleEl.textContent = css;
  document.head.appendChild(styleEl);

  // ── Helpers ───────────────────────────────────────────────────────────────
  function el(tag, props) {
    var e = document.createElement(tag);
    if (!props) return e;
    Object.keys(props).forEach(function (k) {
      if      (k === 'class')  e.className   = props[k];
      else if (k === 'html')   e.innerHTML   = props[k];
      else if (k === 'text')   e.textContent = props[k];
      else if (k === 'style')  e.style.cssText = props[k];
      else                     e.setAttribute(k, props[k]);
    });
    return e;
  }

  function fmt(n) {
    return n == null ? '—' : '$' + n.toLocaleString('en-AU') + ' + GST';
  }

  // ── Render router ─────────────────────────────────────────────────────────
  function render() {
    root.innerHTML = '';
    var wrap = el('div', { id: 'acc-calc' });
    root.appendChild(wrap);

    if (currentStep < STEPS.length) {
      renderStep(wrap);
    } else if (!calcResult) {
      wrap.appendChild(el('div', { class: 'acc-loading', text: 'Calculating your indicative contribution…' }));
      postCalc();
    } else if (!applyResult) {
      renderResult(wrap);
    } else {
      renderConfirm(wrap);
    }
  }

  // ── Progress — Step X of Y · Topic (brief §5) ────────────────────────────
  function progress(wrap) {
    var s = STEPS[currentStep];
    var label = el('p', {
      id: 'acc-step-label',
      text: 'Step ' + (currentStep + 1) + ' of ' + STEPS.length + ' · ' + s.topic,
    });
    wrap.appendChild(label);
    var prog = el('div', { id: 'acc-progress' });
    STEPS.forEach(function (_, i) {
      prog.appendChild(el('div', {
        class: 'acc-pip' + (i < currentStep ? ' done' : i === currentStep ? ' active' : ''),
      }));
    });
    wrap.appendChild(prog);
  }

  // ── Step (brief §6 — large click targets) ────────────────────────────────
  function renderStep(wrap) {
    var s = STEPS[currentStep];

    // Fire start event on first step
    if (currentStep === 0) track('access_calculator_start');
    track('access_calculator_step', { step: currentStep + 1 });

    progress(wrap);
    wrap.appendChild(el('p', { id: 'acc-question', text: s.question }));
    if (s.hint) wrap.appendChild(el('p', { id: 'acc-hint', text: s.hint }));

    var opts = el('div', { class: 'acc-options' });
    s.options.forEach(function (o) {
      var btn = el('button', {
        class: 'acc-opt' + (answers[s.key] === o.value ? ' selected' : ''),
        type: 'button',
      });
      var dot = el('div', { class: 'acc-opt-dot' });
      var lbl = el('span', { class: 'acc-opt-label', text: o.label });
      btn.appendChild(dot);
      btn.appendChild(lbl);
      btn.addEventListener('click', function () {
        answers[s.key] = o.value;
        currentStep++;
        if (currentStep === STEPS.length) track('access_calculator_complete');
        render();
      });
      opts.appendChild(btn);
    });
    wrap.appendChild(opts);

    if (currentStep > 0) {
      var back = el('button', { id: 'acc-back', type: 'button', text: '← Back' });
      back.addEventListener('click', function () { currentStep--; render(); });
      wrap.appendChild(back);
    }
  }

  // ── Result — three-row breakdown (brief §9) ───────────────────────────────
  function renderResult(wrap) {
    var r = calcResult;

    track('access_result_type', { type: r.result_type });

    if (r.result_type === 'fdr_routing') {
      var b = el('div', { id: 'acc-result' });
      b.appendChild(el('p', { html: '<strong>Your matter may require a Family Dispute Resolution (FDR) process</strong> to obtain a Section 60I certificate.' }));
      b.appendChild(el('p', { class: 'acc-res-disclaimer',
        text: 'Please call us to discuss whether your matter is eligible for FDR, the process involved, and your contribution options. We cannot issue a certificate in advance or guarantee one will be issued.' }));
      b.appendChild(el('a', { href: 'tel:0272277373', class: 'acc-apply-btn', html: 'Call (02) 7227 7373' }));
      wrap.appendChild(b);
      return;
    }

    if (r.result_type === 'standard') {
      var sb = el('div', { id: 'acc-result' });
      sb.appendChild(el('p', { html: '<strong>The standard mediation contribution is likely to apply.</strong>' }));
      sb.appendChild(el('p', { text: 'Based on your answers, your income is above the Access Mediation threshold. The standard individual contribution for a 3-hour session is ' + fmt(r.standard_contribution_ex_gst) + '.' }));
      sb.appendChild(el('p', { class: 'acc-res-disclaimer',
        text: 'If you believe your circumstances should be reviewed, please call us to discuss.' }));
      sb.appendChild(el('a', { href: '/book-a-consultation/', class: 'acc-apply-btn', html: 'Book a Free Consultation →' }));
      wrap.appendChild(sb);
      return;
    }

    // eligible or review — three-row result
    var box = el('div', { id: 'acc-result' });

    if (r.result_type === 'review') {
      box.appendChild(el('div', { class: 'acc-review-note',
        html: '<strong>Your application requires staff review.</strong> Your circumstances do not fit neatly within the automatic assessment — this does not mean you are ineligible. Our team will assess your individual circumstances and confirm your contribution.' }));
    }

    if (r.contribution_ex_gst != null) {
      // Heading
      box.appendChild(el('h3', { style: 'margin:0 0 16px;font-size:1rem;color:' + DEEP, text: 'Your indicative Access contribution' }));

      // Three-row breakdown
      var rows = el('div', { class: 'acc-res-rows' });
      var r1 = el('div', { class: 'acc-res-row' });
      r1.appendChild(el('span', { class: 'acc-res-row-label', text: 'Standard individual contribution' }));
      r1.appendChild(el('span', { class: 'acc-res-row-value', text: fmt(r.standard_contribution_ex_gst) }));
      rows.appendChild(r1);

      if (r.access_assistance_ex_gst != null && r.access_assistance_ex_gst > 0) {
        var r2 = el('div', { class: 'acc-res-row' });
        r2.appendChild(el('span', { class: 'acc-res-row-label', text: 'Access assistance' }));
        r2.appendChild(el('span', { class: 'acc-res-row-value', style: 'color:' + GREEN, text: '−$' + r.access_assistance_ex_gst.toLocaleString('en-AU') }));
        rows.appendChild(r2);
      }

      var r3 = el('div', { class: 'acc-res-row' });
      r3.appendChild(el('span', { class: 'acc-res-row-label', text: 'Your contribution' }));
      r3.appendChild(el('span', { class: 'acc-res-row-value', style: 'color:' + GREEN + ';font-size:1.1rem', text: fmt(r.contribution_ex_gst) }));
      rows.appendChild(r3);
      box.appendChild(rows);

      box.appendChild(el('p', { class: 'acc-res-sub',
        text: 'Your individual contribution for an Access Mediation of up to 3 hours. The other participant is assessed separately.' }));
    }

    box.appendChild(el('p', { class: 'acc-res-disclaimer',
      text: 'This is your indicative contribution only. If you apply, we confirm your contribution after reviewing your application. Access places are limited. Financial eligibility does not guarantee a booking — mediation suitability is assessed separately.' }));

    var btnRow = el('div', { class: 'acc-btn-row' });
    var applyBtn = el('button', { class: 'acc-apply-btn', type: 'button', text: 'Apply for an Access appointment →' });
    applyBtn.addEventListener('click', function () {
      track('access_application_cta');
      box.style.display = 'none';
      renderApplicationForm(wrap);
    });
    btnRow.appendChild(applyBtn);
    var talkLink = el('a', { href: '/book-a-consultation/', class: 'acc-talk-link', text: 'Talk to our team' });
    talkLink.addEventListener('click', function () { track('access_consultation_cta'); });
    btnRow.appendChild(talkLink);
    box.appendChild(btnRow);
    wrap.appendChild(box);
  }

  // ── Application form ──────────────────────────────────────────────────────
  function renderApplicationForm(wrap) {
    var form = el('form', { class: 'acc-form', novalidate: '' });

    function textField(id, label, type, required, placeholder, hint) {
      var d = el('div', { class: 'acc-field' });
      d.appendChild(el('label', { for: 'acf-' + id, text: label + (required ? ' *' : '') }));
      var inp = type === 'textarea'
        ? el('textarea', { id: 'acf-' + id, name: id, rows: '3', placeholder: placeholder || '' })
        : el('input', { id: 'acf-' + id, name: id, type: type || 'text',
                        placeholder: placeholder || '', autocomplete: id });
      if (required) inp.setAttribute('required', '');
      d.appendChild(inp);
      if (hint) d.appendChild(el('p', { class: 'acc-field-hint', text: hint }));
      return d;
    }

    form.appendChild(el('h3', { text: 'Your contact details' }));
    form.appendChild(textField('party_a_name',  'Your full name',  'text',  true,  'Your full name'));
    form.appendChild(textField('party_a_email', 'Email address',   'email', true,  'you@example.com'));
    form.appendChild(textField('party_a_phone', 'Phone number',    'tel',   false, '0400 000 000'));

    form.appendChild(el('p', { class: 'acc-section-label', text: 'Other participant (optional)' }));
    form.appendChild(el('p', { class: 'acc-section-hint',
      text: 'We will send them an invitation to complete their own separate assessment. They are not told your financial details or contribution.' }));
    form.appendChild(textField('other_party_name',  'Their name',  'text',  false, 'Full name'));
    form.appendChild(textField('other_party_email', 'Their email', 'email', false, 'them@example.com'));

    form.appendChild(textField('preferred_timing', 'Preferred timing', 'text', false,
      'e.g. weekday mornings, after 3pm', 'Optional — helps us find a suitable session time.'));

    // Consent
    var c1 = el('div', { class: 'acc-consent' });
    var chk1 = el('input', { type: 'checkbox', id: 'acf-privacy' });
    chk1.required = true;
    c1.appendChild(chk1);
    c1.appendChild(el('label', { for: 'acf-privacy',
      html: 'I have read and agree to the <a href="/privacy-policy/" target="_blank">Privacy Policy</a>. I consent to Mediations Australia collecting and using my personal information to assess my Access Mediation application and arrange a session.' }));
    form.appendChild(c1);

    var c2 = el('div', { class: 'acc-consent' });
    var chk2 = el('input', { type: 'checkbox', id: 'acf-accuracy' });
    chk2.required = true;
    c2.appendChild(chk2);
    c2.appendChild(el('label', { for: 'acf-accuracy',
      text: 'I declare that the information I have provided is accurate to the best of my knowledge. I understand that providing false information may affect my application.' }));
    form.appendChild(c2);

    var errDiv = el('div', { style: 'display:none' });
    form.appendChild(errDiv);

    var submitBtn = el('button', { class: 'acc-submit', type: 'submit', text: 'Submit Application' });
    form.appendChild(submitBtn);

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      errDiv.style.display = 'none';
      errDiv.innerHTML = '';

      var name  = form.querySelector('#acf-party_a_name').value.trim();
      var email = form.querySelector('#acf-party_a_email').value.trim();

      if (!name || !email || !chk1.checked || !chk2.checked) {
        errDiv.className = 'acc-error';
        errDiv.textContent = 'Please complete all required fields (*) and tick both consent boxes.';
        errDiv.style.display = 'block';
        return;
      }

      submitBtn.disabled = true;
      submitBtn.textContent = 'Submitting…';

      var payload = Object.assign({}, answers, {
        party_a_name:         name,
        party_a_email:        email,
        party_a_phone:        (form.querySelector('#acf-party_a_phone').value.trim()  || undefined),
        other_party_name:     (form.querySelector('#acf-other_party_name').value.trim()  || undefined),
        other_party_email:    (form.querySelector('#acf-other_party_email').value.trim() || undefined),
        preferred_timing:     (form.querySelector('#acf-preferred_timing').value.trim()  || undefined),
        privacy_consent:      true,
        accuracy_declaration: true,
      });

      fetch('/api/access-apply', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      })
      .then(function (r) { return r.json().then(function (d) { return { ok: r.ok, data: d }; }); })
      .then(function (res) {
        if (!res.ok) throw new Error(res.data.error || 'Submission failed. Please try again.');
        applyResult = res.data;
        render();
      })
      .catch(function (err) {
        submitBtn.disabled = false;
        submitBtn.textContent = 'Submit Application';
        errDiv.className = 'acc-error';
        errDiv.textContent = err.message || 'An unexpected error occurred. Please call (02) 7227 7373.';
        errDiv.style.display = 'block';
      });
    });

    wrap.appendChild(form);
  }

  // ── Confirmation ──────────────────────────────────────────────────────────
  function renderConfirm(wrap) {
    var r = applyResult || {};
    var conf = el('div', { class: 'acc-confirm' });
    conf.appendChild(el('div', { class: 'acc-confirm-icon', html: '&#10003;' }));
    conf.appendChild(el('h3', { text: 'Application submitted' }));
    if (r.matter_id) {
      conf.appendChild(el('p', {
        html: 'Your reference number is <strong>' + r.matter_id + '</strong>. Please keep this for your records.',
      }));
    }
    conf.appendChild(el('p', {
      text: r.waitlisted
        ? 'Access capacity is currently full. You have been added to the waitlist and we will contact you as soon as a place becomes available.'
        : 'Our team will review your application and be in touch within 1–2 business days to confirm your contribution and arrange scheduling.',
    }));
    conf.appendChild(el('p', { text: 'If you have any questions in the meantime, please call (02) 7227 7373.' }));

    var restart = el('span', { class: 'acc-restart', text: 'Start a new enquiry' });
    restart.addEventListener('click', function () {
      answers = { income_band:null, dependants:null, assets_band:null,
                  concession:null, hardship:null, matter_type:null, needs_60i:null };
      calcResult = null; applyResult = null; currentStep = 0;
      render();
    });
    conf.appendChild(restart);
    wrap.appendChild(conf);
  }

  // ── API ───────────────────────────────────────────────────────────────────
  function postCalc() {
    fetch('/api/access-calc', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(answers),
    })
    .then(function (r) { return r.json(); })
    .then(function (d) { calcResult = d; render(); })
    .catch(function () {
      root.innerHTML = '<div class="acc-error">Unable to check your contribution right now. Please call '
        + '<a href="tel:0272277373" style="color:#b71c1c">(02) 7227 7373</a> or try again shortly.</div>';
    });
  }

  // ── Boot ──────────────────────────────────────────────────────────────────
  track('access_page_view');
  render();
})();
