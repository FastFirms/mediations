// Floating chat widget. Add to any page with:
//   <script src="/widget.js" defer></script>
// Talks to /api/chat. No dependencies. Adjust colours to match the site.
(function () {
  const API = '/api/chat';
  const BRAND = '#1f3a5f';       // adjust to Mediations Australia brand
  const BRAND_TEXT = '#ffffff';

  const css = `
    #ma-bot-btn{position:fixed;bottom:20px;right:20px;z-index:99998;width:56px;height:56px;border:none;border-radius:50%;background:${BRAND};color:${BRAND_TEXT};font-size:24px;cursor:pointer;box-shadow:0 4px 14px rgba(0,0,0,.25)}
    #ma-bot-panel{position:fixed;bottom:88px;right:20px;z-index:99999;width:360px;max-width:calc(100vw - 40px);height:520px;max-height:calc(100vh - 120px);background:#fff;border-radius:14px;box-shadow:0 10px 40px rgba(0,0,0,.25);display:none;flex-direction:column;overflow:hidden;font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
    #ma-bot-panel.open{display:flex}
    #ma-bot-head{background:${BRAND};color:${BRAND_TEXT};padding:14px 16px;font-weight:600}
    #ma-bot-head small{display:block;font-weight:400;opacity:.85;font-size:12px;margin-top:2px}
    #ma-bot-log{flex:1;overflow-y:auto;padding:14px;background:#f7f8fa}
    .ma-msg{margin:0 0 10px;padding:10px 12px;border-radius:12px;max-width:85%;line-height:1.4;font-size:14px;white-space:pre-wrap;word-wrap:break-word}
    .ma-user{background:${BRAND};color:${BRAND_TEXT};margin-left:auto;border-bottom-right-radius:4px}
    .ma-ai{background:#fff;border:1px solid #e5e7eb;color:#1f2937;border-bottom-left-radius:4px}
    .ma-src{font-size:12px;margin-top:6px}
    .ma-src a{color:${BRAND};display:block;margin-top:2px}
    #ma-bot-form{display:flex;border-top:1px solid #e5e7eb;padding:8px;gap:8px;background:#fff}
    #ma-bot-input{flex:1;border:1px solid #d1d5db;border-radius:10px;padding:10px;font-size:14px;resize:none;font-family:inherit}
    #ma-bot-send{background:${BRAND};color:${BRAND_TEXT};border:none;border-radius:10px;padding:0 14px;cursor:pointer;font-size:14px}
    #ma-bot-send:disabled{opacity:.5;cursor:default}
    .ma-note{font-size:11px;color:#6b7280;padding:6px 12px;text-align:center;background:#f7f8fa}
  `;
  const style = document.createElement('style');
  style.textContent = css;
  document.head.appendChild(style);

  const btn = document.createElement('button');
  btn.id = 'ma-bot-btn';
  btn.setAttribute('aria-label', 'Open chat');
  btn.textContent = '💬';
  document.body.appendChild(btn);

  const panel = document.createElement('div');
  panel.id = 'ma-bot-panel';
  panel.innerHTML = `
    <div id="ma-bot-head">Ask Mediations Australia<small>General info only — not legal advice</small></div>
    <div id="ma-bot-log"></div>
    <div class="ma-note">Answers use our website content. For your situation, book a free consult.</div>
    <form id="ma-bot-form">
      <textarea id="ma-bot-input" rows="1" placeholder="Ask a question…" maxlength="500"></textarea>
      <button id="ma-bot-send" type="submit">Send</button>
    </form>`;
  document.body.appendChild(panel);

  const log = panel.querySelector('#ma-bot-log');
  const form = panel.querySelector('#ma-bot-form');
  const input = panel.querySelector('#ma-bot-input');
  const send = panel.querySelector('#ma-bot-send');

  function add(text, cls, sources) {
    const div = document.createElement('div');
    div.className = 'ma-msg ' + cls;
    div.textContent = text;
    if (sources && sources.length) {
      const s = document.createElement('div');
      s.className = 'ma-src';
      s.innerHTML = 'Learn more:' + sources.slice(0, 3)
        .map((x) => `<a href="${x.url}" target="_blank" rel="noopener">${x.title || x.url}</a>`).join('');
      div.appendChild(s);
    }
    log.appendChild(div);
    log.scrollTop = log.scrollHeight;
    return div;
  }

  let greeted = false;
  btn.addEventListener('click', () => {
    panel.classList.toggle('open');
    if (panel.classList.contains('open') && !greeted) {
      add("Hi! I can answer questions about mediation and how we work — costs, timeframes, the process and our services. What would you like to know?", 'ma-ai');
      greeted = true;
      input.focus();
    }
  });

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const q = input.value.trim();
    if (!q) return;
    add(q, 'ma-user');
    input.value = '';
    send.disabled = true;
    const thinking = add('…', 'ma-ai');
    try {
      const r = await fetch(API, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: q }),
      });
      const data = await r.json();
      thinking.remove();
      if (data.error) add(data.error, 'ma-ai');
      else add(data.answer, 'ma-ai', data.sources);
    } catch (_) {
      thinking.remove();
      add('Sorry, something went wrong. Please call 1800 952 380.', 'ma-ai');
    } finally {
      send.disabled = false;
      input.focus();
    }
  });

  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); form.requestSubmit(); }
  });
})();
