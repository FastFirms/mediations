/**
 * Access Mediation — multi-step eligibility calculator + application form.
 * Mounts into: <div id="access-calc-root">
 *
 * Steps:
 *   1  income_band
 *   2  dependants
 *   3  assets_band
 *   4  concession
 *   5  hardship
 *   6  matter_type
 *   7  needs_60i
 *   8  → POST /api/access-calc → show result
 *   9  (if eligible/review) → application form → POST /api/access-apply → confirmation
 *
 * Privacy rules (build-pack §19):
 *   - Never put financial answers in URLs.
 *   - Answers live only in JS module state and are sent once, server-side, over HTTPS.
 *   - No financial inputs are echoed back in the result display.
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
      question: 'What is your personal gross annual income?',
      hint: 'This is your individual income, not household income.',
      options: [
        { value: '0-50k',    label: 'Under $50,000' },
        { value: '50-75k',   label: '$50,001 – $75,000' },
        { value: '75-100k',  label: '$75,001 – $100,000' },
        { value: '100-125k', label: '$100,001 – $125,000' },
        { value: '125-150k', label: '$125,001 – $150,000' },
        { value: '150k+',    label: 'Above $150,000' },
      ],
    },
    {
      key: 'dependants',
      question: 'How many dependants do you have?',
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
      question: 'What are your accessible assets (approximate total)?',
      hint: 'Savings, shares, investment properties, etc. Not your family home or superannuation.',
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
      question: 'Do you need a Section 60I certificate?',
      hint: 'A Section 60I certificate is required before most parenting applications to the Federal Circuit and Family Court. If you are not sure, select "Not sure".',
      options: [
        { value: 'yes',   label: 'Yes, I need one' },
        { value: 'no',    label: 'No' },
        { value: 'unsure', label: 'Not sure' },
      ],
    },
  ];

  // ── Styles ────────────────────────────────────────────────────────────────
  var css = [
    '#acc-calc{font-family:' + FONT + ';max-width:560px;margin:0 auto}',
    '#acc-progress{display:flex;gap:6px;margin-bottom:28px}',
    '.acc-pip{flex:1;height:4px;border-radius:2px;background:' + LINE + ';transition:background .3s}',
    '.acc-pip.done{background:' + GREEN + '}',
    '.acc-pip.active{background:' + GREEN + ';opacity:.55}',
    '#acc-question{font-size:1.08rem;font-weight:700;color:' + DEEP + ';margin:0 0 6px;line-height:1.4}',
    '#acc-hint{font-size:.83rem;color:' + MUTED + ';margin:0 0 18px;line-height:1.5}',
    '.acc-options{display:flex;flex-direction:column;gap:9px}',
    '.acc-opt{display:flex;align-items:center;gap:12px;padding:11px 15px;border:1.5px solid ' + LINE + ';',
    '  border-radius:10px;cursor:pointer;background:#fff;transition:border-color .15s,background .15s;text-align:left;width:100%}',
    '.acc-opt:hover,.acc-opt:focus{border-color:' + GREEN + ';background:' + SAND + ';outline:none}',
    '.acc-opt.selected{border-color:' + GREEN + ';background:' + SAND + '}',
    '.acc-opt-dot{width:17px;height:17px;border-radius:50%;border:2px solid ' + LINE + ';flex-shrink:0;transition:border-color .15s,background .15s}',
    '.acc-opt.selected .acc-opt-dot{border-color:' + GREEN + ';background:' + GREEN + '}',
    '.acc-opt-label{font-size:.93rem;color:' + DEEP + ';font-weight:500;line-height:1.4}',
    '#acc-back{background:none;border:none;color:' + MUTED + ';font-size:.83rem;cursor:pointer;padding:0;margin-top:14px;text-decoration:underline}',
    '#acc-result{padding:22px;border-radius:14px;border:2px solid ' + GREEN + ';background:#fff;margin-top:6px}',
    '.acc-res-band{font-size:2rem;font-weight:800;color:' + GREEN + ';line-height:1}',
    '.acc-res-sub{font-size:.88rem;color:' + MUTED + ';margin:6px 0 18px}',
    '.acc-res-meta{font-size:.88rem;color:' + MUTED + ';margin-bottom:16px}',
    '.acc-res-disclaimer{font-size:.78rem;color:' + MUTED + ';line-height:1.5;margin-top:16px;padding-top:12px;border-top:1px solid ' + LINE + '}',
    '.acc-apply-btn{display:inline-flex;align-items:center;gap:8px;background:' + GREEN + ';color:#fff;',
    '  border:none;border-radius:100px;padding:12px 26px;font-family:' + FONT + ';font-size:.95rem;font-weight:700;cursor:pointer;transition:background .2s;text-decoration:none}',
    '.acc-apply-btn:hover{background:' + DEEP + ';color:#fff}',
    '.acc-review-note{padding:13px 15px;background:#fff9e6;border-left:4px solid #f0a500;border-radius:0 8px 8px 0;font-size:.86rem;line-height:1.6;margin-bottom:18px}',
    '.acc-form{margin-top:22px}',
    '.acc-form h3{color:' + DEEP + ';margin:0 0 18px;font-size:1rem}',
    '.acc-field{margin-bottom:16px}',
    '.acc-field label{display:block;font-size:.86rem;font-weight:600;color:' + DEEP + ';margin-bottom:4px}',
    '.acc-field input,.acc-field textarea,.acc-field select{width:100%;box-sizing:border-box;border:1.5px solid ' + LINE + ';',
    '  border-radius:9px;padding:9px 12px;font-family:' + FONT + ';font-size:.88rem;color:' + DEEP + ';background:' + SAND + ';outline:none;transition:border-color .2s}',
    '.acc-field input:focus,.acc-field textarea:focus{border-color:' + GREEN + ';background:#fff}',
    '.acc-section-label{font-size:.88rem;font-weight:700;color:' + DEEP + ';margin:22px 0 6px;border-bottom:1px solid ' + LINE + ';padding-bottom:6px}',
    '.acc-section-hint{font-size:.79rem;color:' + MUTED + ';margin-bottom:12px;line-height:1.5}',
    '.acc-consent{display:flex;gap:10px;align-items:flex-start;margin-bottom:10px}',
    '.acc-consent input[type=checkbox]{margin-top:3px;flex-shrink:0;accent-color:' + GREEN + '}',
    '.acc-consent label{font-size:.83rem;color:' + MUTED + ';line-height:1.5}',
    '.acc-consent a{color:' + GREEN + '}',
    '.acc-submit{display:block;width:100%;background:' + GREEN + ';color:#fff;border:none;border-radius:100px;',
    '  padding:13px 20px;font-family:' + FONT + ';font-size:.95rem;font-weight:700;cursor:pointer;transition:background .2s;margin-top:10px}',
    '.acc-submit:hover{background:' + DEEP + '}',
    '.acc-submit:disabled{opacity:.4;cursor:default}',
    '.acc-error{padding:11px 15px;background:#fdecea;border-left:4px solid #d32f2f;border-radius:0 8px 8px 0;font-size:.86rem;color:#b71c1c;margin:10px 0}',
    '.acc-confirm{text-align:center;padding:30px 20px}',
    '.acc-confirm-icon{font-size:2.8rem;margin-bottom:10px;color:' + GREEN + '}',
    '.acc-confirm h3{color:' + GREEN + ';margin:0 0 10px;font-size:1.1rem}',
    '.acc-confirm p{font-size:.9rem;color:' + MUTED + ';line-height:1.6;margin:0 0 10px}',
    '.acc-confirm strong{color:' + DEEP + '}',
    '.acc-restart{display:inline-block;margin-top:16px;font-size:.83rem;color:' + GREEN + ';cursor:pointer;text-decoration:underline}',
    '.acc-loading{text-align:center;padding:36px 0;color:' + MUTED + ';font-size:.88rem;font-style:italic}',
    '.acc-field-hint{font-size:.77rem;color:' + MUTED + ';margin:3px 0 0;line-height:1.4}',
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
      wrap.appendChild(el('div', { class: 'acc-loading', text: 'Checking your eligibility…' }));
      postCalc();
    } else if (!applyResult) {
      renderResult(wrap);
    } else {
      renderConfirm(wrap);
    }
  }

  function progress(wrap) {
    var prog = el('div', { id: 'acc-progress' });
    STEPS.forEach(function (_, i) {
      prog.appendChild(el('div', {
        class: 'acc-pip' + (i < currentStep ? ' done' : i === currentStep ? ' active' : ''),
      }));
    });
    wrap.appendChild(prog);
  }

  // ── Step ──────────────────────────────────────────────────────────────────
  function renderStep(wrap) {
    var s = STEPS[currentStep];
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

  // ── Result ────────────────────────────────────────────────────────────────
  function renderResult(wrap) {
    var r = calcResult;

    if (r.result_type === 'fdr_routing') {
      var b = el('div', { id: 'acc-result' });
      b.appendChild(el('p', { html: '<strong>Your matter may require a Family Dispute Resolution (FDR) process</strong> to obtain a Section 60I certificate.' }));
      b.appendChild(el('p', { class: 'acc-res-disclaimer',
        text: 'Please call us to discuss whether your matter is eligible for FDR, the process involved, and your contribution options. We cannot issue a certificate in advance or guarantee one will be issued.' }));
      b.appendChild(el('a', { href: 'tel:0272277373', class: 'acc-apply-btn', html: 'Call (02) 7227 7373' }));
      wrap.appendChild(b);
      return;
    }

    if (r.result_type === 'standard') {
      var sb = el('div', { id: 'acc-result' });
      sb.appendChild(el('p', { html: '<strong>The standard mediation contribution is likely to apply.</strong>' }));
      sb.appendChild(el('p', { text: 'Based on your answers, your income is above the Access Mediation threshold. The standard individual contribution for a 3-hour session is ' + fmt(r.standard_contribution_ex_gst) + '.' }));
      sb.appendChild(el('p', { class: 'acc-res-disclaimer',
        text: 'If you believe your circumstances should be reviewed, please call us to discuss.' }));
      sb.appendChild(el('a', { href: '/book-a-consultation/', class: 'acc-apply-btn', html: 'Book a Standard Consultation →' }));
      wrap.appendChild(sb);
      return;
    }

    // eligible or review
    var box = el('div', { id: 'acc-result' });

    if (r.result_type === 'review') {
      box.appendChild(el('div', { class: 'acc-review-note',
        html: '<strong>Your application requires staff review.</strong> Your circumstances do not fit neatly within the automatic bands — this does not mean you are ineligible. Our team will assess your individual circumstances and confirm your contribution.' }));
    }

    if (r.contribution_ex_gst != null) {
      box.appendChild(el('div', { class: 'acc-res-band', text: fmt(r.contribution_ex_gst) }));
      box.appendChild(el('p', { class: 'acc-res-sub', text: 'Your indicative individual contribution (ex GST) for a 3-hour session' }));
      box.appendChild(el('p', { class: 'acc-res-meta',
        html: 'Standard contribution: <strong>' + fmt(r.standard_contribution_ex_gst) + '</strong>'
          + (r.access_assistance_ex_gst != null
            ? '&ensp;•&ensp;Access assistance: <strong>' + fmt(r.access_assistance_ex_gst) + '</strong>'
            : '') }));
    }

    box.appendChild(el('p', { class: 'acc-res-disclaimer',
      text: 'This is your indicative contribution only. If you apply, we confirm your contribution after reviewing your application. Access places are limited. Financial eligibility does not guarantee a booking — mediation suitability is assessed separately.' }));

    var applyBtn = el('button', { class: 'acc-apply-btn', type: 'button', html: 'Apply for Access Mediation →' });
    applyBtn.addEventListener('click', function () {
      box.style.display = 'none';
      renderApplicationForm(wrap);
    });
    box.appendChild(applyBtn);
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
      html: 'I have read and agree to the <a href="/privacy-policy/" target="_blank">Privacy Policy</a>. I consent to Mediations Australia collecting and using my personal information to assess my Access Mediation eligibility and arrange a session.' }));
    form.appendChild(c1);

    var c2 = el('div', { class: 'acc-consent' });
    var chk2 = el('input', { type: 'checkbox', id: 'acf-accuracy' });
    chk2.required = true;
    c2.appendChild(chk2);
    c2.appendChild(el('label', { for: 'acf-accuracy',
      text: 'I declare that the information I have provided is accurate to the best of my knowledge. I understand that providing false information may affect my eligibility.' }));
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
    conf.appendChild(el('p', { text: 'If you have any questions in the meantime, please call (02) 7227 7373.' }));

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
      root.innerHTML = '<div class="acc-error">Unable to check eligibility right now. Please call '
        + '<a href="tel:0272277373" style="color:#b71c1c">(02) 7227 7373</a> or try again later.</div>';
    });
  }

  // ── Boot ──────────────────────────────────────────────────────────────────
  render();
})();
