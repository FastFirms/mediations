// Mediations Australia — floating chat widget
// Add to any page with: <script src="/widget.js" defer></script>
// Talks to /api/chat. No external dependencies.
(function () {
  const API   = '/api/chat';
  const GREEN = '#1e6040';
  const DEEP  = '#0d2218';
  const SAND  = '#f1f5f1';
  const SAND2 = '#e8efe9';
  const LINE  = 'rgba(13,34,24,.14)';
  const MUTED = '#3d5248';
  const FONT  = '"Hanken Grotesk",-apple-system,BlinkMacSystemFont,sans-serif';
  const BOOK_URL = '/book-a-consultation/';
  const AVATAR   = '/assets/images/Dan-Bio.png';

  /* ── Styles ─────────────────────────────────────────── */
  const css = `
    #ma-btn {
      position:fixed;bottom:24px;right:24px;z-index:99998;
      width:60px;height:60px;border:none;border-radius:50%;
      background:${GREEN};cursor:pointer;
      box-shadow:0 4px 18px rgba(30,96,64,.35),0 1px 4px rgba(30,96,64,.2);
      padding:0;overflow:hidden;
      transition:transform .3s cubic-bezier(.16,1,.3,1),box-shadow .3s;
    }
    #ma-btn:hover {
      transform:translateY(-3px) scale(1.04);
      box-shadow:0 8px 28px rgba(30,96,64,.45);
    }
    #ma-btn img {
      width:100%;height:100%;object-fit:cover;
      border-radius:50%;display:block;
    }
    #ma-btn .ma-close-icon {
      display:none;position:absolute;inset:0;
      align-items:center;justify-content:center;
      font-size:22px;color:#fff;font-family:${FONT};font-weight:300;
    }
    #ma-btn.open .ma-close-icon { display:flex; }
    #ma-btn.open img { opacity:0; }

    #ma-panel {
      position:fixed;bottom:100px;right:24px;z-index:99999;
      width:380px;max-width:calc(100vw - 32px);
      height:560px;max-height:calc(100vh - 130px);
      background:#fff;border-radius:20px;
      box-shadow:0 20px 60px rgba(13,34,24,.18),0 2px 8px rgba(13,34,24,.08);
      display:none;flex-direction:column;overflow:hidden;
      font-family:${FONT};
      border:1px solid ${LINE};
    }
    #ma-panel.open { display:flex; }

    #ma-head {
      background:${GREEN};color:#fff;
      padding:16px 18px 14px;
      flex-shrink:0;
    }
    #ma-head-inner {
      display:flex;align-items:center;gap:12px;
    }
    #ma-head img {
      width:40px;height:40px;border-radius:50%;object-fit:cover;
      border:2px solid rgba(255,255,255,.35);flex-shrink:0;
    }
    #ma-head-name {
      font-weight:700;font-size:.95rem;line-height:1.2;
    }
    #ma-head-sub {
      font-size:.75rem;opacity:.82;margin-top:2px;line-height:1.3;
    }
    #ma-head-disclaimer {
      margin-top:10px;padding:8px 10px;
      background:rgba(255,255,255,.12);border-radius:8px;
      font-size:.72rem;line-height:1.45;opacity:.9;
    }

    #ma-log {
      flex:1;overflow-y:auto;padding:16px;
      background:${SAND};display:flex;flex-direction:column;gap:12px;
      scroll-behavior:smooth;
    }
    #ma-log::-webkit-scrollbar { width:4px; }
    #ma-log::-webkit-scrollbar-track { background:transparent; }
    #ma-log::-webkit-scrollbar-thumb { background:${LINE};border-radius:4px; }

    .ma-bubble {
      max-width:88%;line-height:1.5;font-size:.875rem;word-wrap:break-word;
    }
    .ma-bubble-user {
      align-self:flex-end;
      background:${GREEN};color:#fff;
      padding:10px 14px;border-radius:16px 16px 4px 16px;
      font-weight:500;
    }
    .ma-bubble-ai-wrap {
      align-self:flex-start;display:flex;flex-direction:column;
      max-width:92%;
    }
    .ma-bubble-ai {
      background:#fff;color:${DEEP};
      padding:11px 14px;border-radius:4px 16px 16px 16px;
      border:1px solid ${LINE};
      box-shadow:0 1px 4px rgba(13,34,24,.06);
      white-space:pre-wrap;
    }
    .ma-cta-nudge {
      margin-top:6px;padding:10px 13px;
      background:${SAND2};border-radius:0 0 12px 12px;
      border:1px solid ${LINE};border-top:2px solid ${GREEN};
      display:flex;align-items:center;justify-content:space-between;gap:8px;
    }
    .ma-cta-nudge span {
      font-size:.78rem;color:${MUTED};font-weight:500;
    }
    .ma-cta-nudge a {
      color:#fff;font-weight:700;font-size:.75rem;
      background:${GREEN};padding:5px 11px;border-radius:100px;
      text-decoration:none;white-space:nowrap;flex-shrink:0;
      display:inline-flex;align-items:center;gap:4px;
      transition:background .2s;
    }
    .ma-cta-nudge a:hover { background:${DEEP}; }
    .ma-sources {
      margin-top:6px;font-size:.72rem;color:${MUTED};padding:0 2px;
    }
    .ma-sources a {
      color:${GREEN};display:inline-block;margin-top:2px;
      text-decoration:none;font-weight:500;
    }
    .ma-sources a:hover { text-decoration:underline; }
    .ma-thinking {
      font-style:italic;color:${MUTED};opacity:.7;
      padding:10px 14px;font-size:.85rem;align-self:flex-start;
    }

    #ma-form {
      display:flex;border-top:1px solid ${LINE};
      padding:10px;gap:8px;background:#fff;flex-shrink:0;
    }
    #ma-input {
      flex:1;border:1.5px solid ${LINE};border-radius:12px;
      padding:10px 12px;font-size:.875rem;resize:none;
      font-family:${FONT};color:${DEEP};background:${SAND};
      transition:border-color .2s;outline:none;line-height:1.4;
    }
    #ma-input:focus { border-color:${GREEN};background:#fff; }
    #ma-send {
      background:${GREEN};color:#fff;border:none;
      border-radius:12px;padding:0 16px;cursor:pointer;
      font-family:${FONT};font-size:.875rem;font-weight:600;
      transition:background .2s;flex-shrink:0;
    }
    #ma-send:hover { background:${DEEP}; }
    #ma-send:disabled { opacity:.45;cursor:default; }

    @media(max-width:600px){
      #ma-btn{
        bottom:max(16px,env(safe-area-inset-bottom,16px));
        right:16px;
        width:54px;height:54px;
      }
      #ma-panel{
        position:fixed;
        inset:0;
        width:100%;
        height:100%;
        max-width:100%;
        max-height:100%;
        bottom:0;right:0;
        border-radius:0;
        border:none;
      }
      #ma-head{
        padding-top:max(16px,env(safe-area-inset-top,16px));
        padding-left:max(18px,env(safe-area-inset-left,18px));
        padding-right:max(18px,env(safe-area-inset-right,18px));
      }
      #ma-form{
        padding-bottom:max(10px,env(safe-area-inset-bottom,10px));
        padding-left:max(10px,env(safe-area-inset-left,10px));
        padding-right:max(10px,env(safe-area-inset-right,10px));
      }
    }
  `;

  const style = document.createElement('style');
  style.textContent = css;
  document.head.appendChild(style);

  /* ── Button ──────────────────────────────────────────── */
  const btn = document.createElement('button');
  btn.id = 'ma-btn';
  btn.setAttribute('aria-label', 'Chat with Mediations Australia');
  btn.innerHTML = '<img src="' + AVATAR + '" alt="Dan Toombs"><span class="ma-close-icon">&#x2715;</span>';
  document.body.appendChild(btn);

  /* ── Panel ───────────────────────────────────────────── */
  const panel = document.createElement('div');
  panel.id = 'ma-panel';
  panel.setAttribute('role', 'dialog');
  panel.setAttribute('aria-label', 'Mediations Australia chat');
  panel.innerHTML =
    '<div id="ma-head">' +
      '<div id="ma-head-inner">' +
        '<img src="' + AVATAR + '" alt="Dan Toombs">' +
        '<div>' +
          '<div id="ma-head-name">Mediations Australia</div>' +
          '<div id="ma-head-sub">Ask us anything about mediation</div>' +
        '</div>' +
      '</div>' +
      '<div id="ma-head-disclaimer">General information only &#8212; not legal advice for your specific situation.</div>' +
    '</div>' +
    '<div id="ma-log"></div>' +
    '<form id="ma-form">' +
      '<textarea id="ma-input" rows="1" placeholder="Ask a question…" maxlength="500" aria-label="Your question"></textarea>' +
      '<button id="ma-send" type="submit">Send</button>' +
    '</form>';
  document.body.appendChild(panel);

  const log   = panel.querySelector('#ma-log');
  const form  = panel.querySelector('#ma-form');
  const input = panel.querySelector('#ma-input');
  const send  = panel.querySelector('#ma-send');

  /* ── Helpers ─────────────────────────────────────────── */
  function addUser(text) {
    const el = document.createElement('div');
    el.className = 'ma-bubble ma-bubble-user';
    el.textContent = text;
    log.appendChild(el);
    log.scrollTop = log.scrollHeight;
  }

  function addThinking() {
    const el = document.createElement('div');
    el.className = 'ma-thinking';
    el.textContent = 'Thinking…';
    log.appendChild(el);
    log.scrollTop = log.scrollHeight;
    return el;
  }

  function addAI(text, sources) {
    const wrap = document.createElement('div');
    wrap.className = 'ma-bubble-ai-wrap';

    // Answer bubble
    const bubble = document.createElement('div');
    bubble.className = 'ma-bubble ma-bubble-ai';
    bubble.textContent = text;
    wrap.appendChild(bubble);

    // Consultation nudge — shown after every AI reply
    const nudge = document.createElement('div');
    nudge.className = 'ma-cta-nudge';
    nudge.innerHTML =
      '<span>Need more information?</span>' +
      '<a href="' + BOOK_URL + '">Book a free consultation &#8594;</a>';
    wrap.appendChild(nudge);

    // Source links
    if (sources && sources.length) {
      const src = document.createElement('div');
      src.className = 'ma-sources';
      src.innerHTML = 'Read more: ' + sources.slice(0, 3)
        .map(function(x) {
          return '<a href="' + x.url + '" target="_blank" rel="noopener">' + (x.title || x.url) + '</a>';
        }).join(' &middot; ');
      wrap.appendChild(src);
    }

    log.appendChild(wrap);
    log.scrollTop = log.scrollHeight;
  }

  /* ── Open / close ────────────────────────────────────── */
  var greeted = false;
  btn.addEventListener('click', function() {
    var isOpen = panel.classList.toggle('open');
    btn.classList.toggle('open', isOpen);
    if (isOpen) {
      if (!greeted) {
        addAI('Hi! I can answer questions about mediation, our services, costs, and how the process works. What would you like to know?', []);
        greeted = true;
      }
      input.focus();
    }
  });

  /* ── Submit ──────────────────────────────────────────── */
  form.addEventListener('submit', async function(e) {
    e.preventDefault();
    var q = input.value.trim();
    if (!q) return;
    addUser(q);
    input.value = '';
    input.style.height = '';
    send.disabled = true;
    var thinking = addThinking();
    try {
      var r = await fetch(API, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: q }),
      });
      var data = await r.json();
      thinking.remove();
      addAI(data.error || data.answer, data.sources);
    } catch (_) {
      thinking.remove();
      addAI('Sorry, something went wrong. Please call 1800 952 380 or book a consultation using the button below.', []);
    } finally {
      send.disabled = false;
      input.focus();
    }
  });

  /* ── Auto-grow textarea ──────────────────────────────── */
  input.addEventListener('input', function() {
    input.style.height = 'auto';
    input.style.height = Math.min(input.scrollHeight, 100) + 'px';
  });

  /* ── Enter to send (Shift+Enter for newline) ─────────── */
  input.addEventListener('keydown', function(e) {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); form.requestSubmit(); }
  });
})();
