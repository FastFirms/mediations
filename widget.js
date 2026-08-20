// Mediations Australia — floating chat widget
// Add to any page with: <script src="/widget.js" defer></script>
(function () {
  const API      = '/api/chat';
  const GREEN    = '#1e6040';
  const DEEP     = '#0d2218';
  const SAND     = '#f1f5f1';
  const SAND2    = '#e8efe9';
  const LINE     = 'rgba(13,34,24,.14)';
  const MUTED    = '#3d5248';
  const FONT     = '"Hanken Grotesk",-apple-system,BlinkMacSystemFont,sans-serif';
  const BOOK_URL = '/book-a-consultation/';
  const AVATAR   = '/assets/images/Dan-Bio.png';

  /* ── Styles ───────────────────────────────────────────── */
  const css = `
    #ma-btn {
      position:fixed;bottom:24px;right:24px;z-index:99998;
      width:60px;height:60px;border:none;border-radius:50%;
      background:${GREEN};cursor:pointer;padding:0;overflow:hidden;
      box-shadow:0 4px 18px rgba(30,96,64,.35);
      transition:transform .3s cubic-bezier(.16,1,.3,1),box-shadow .3s;
    }
    #ma-btn:hover { transform:translateY(-3px);box-shadow:0 8px 28px rgba(30,96,64,.45); }
    #ma-btn img { width:100%;height:100%;object-fit:cover;border-radius:50%;display:block; }
    #ma-btn .ma-x {
      display:none;position:absolute;inset:0;align-items:center;justify-content:center;
      font-size:20px;color:#fff;font-family:${FONT};
    }
    #ma-btn.open .ma-x { display:flex; }
    #ma-btn.open img   { opacity:0; }

    /* ── Panel (desktop) ── */
    #ma-panel {
      position:fixed;bottom:96px;right:24px;z-index:99999;
      width:370px;max-width:calc(100vw - 48px);
      height:540px;max-height:calc(100vh - 120px);
      background:#fff;border-radius:18px;
      box-shadow:0 20px 60px rgba(13,34,24,.18);
      display:none;flex-direction:column;overflow:hidden;
      font-family:${FONT};border:1px solid ${LINE};
      box-sizing:border-box;
    }
    #ma-panel.open { display:flex; }

    /* ── Header ── */
    #ma-head {
      background:${GREEN};color:#fff;
      padding:14px 16px 12px;flex-shrink:0;
    }
    #ma-head-row { display:flex;align-items:center;gap:11px; }
    #ma-head img {
      width:38px;height:38px;border-radius:50%;object-fit:cover;
      border:2px solid rgba(255,255,255,.3);flex-shrink:0;
    }
    #ma-head-name  { font-weight:700;font-size:.92rem;line-height:1.2; }
    #ma-head-sub   { font-size:.72rem;opacity:.8;margin-top:1px; }
    #ma-disclaimer {
      margin-top:9px;padding:7px 9px;
      background:rgba(255,255,255,.12);border-radius:7px;
      font-size:.7rem;line-height:1.4;opacity:.88;
    }

    /* ── Log ── */
    #ma-log {
      flex:1;overflow-y:auto;padding:14px;
      background:${SAND};display:flex;flex-direction:column;gap:10px;
      scroll-behavior:smooth;min-height:0;
    }
    #ma-log::-webkit-scrollbar{width:3px;}
    #ma-log::-webkit-scrollbar-thumb{background:${LINE};border-radius:3px;}

    /* ── Bubbles ── */
    .ma-user {
      align-self:flex-end;max-width:82%;
      background:${GREEN};color:#fff;
      padding:9px 13px;border-radius:16px 16px 3px 16px;
      font-size:.875rem;line-height:1.5;font-weight:500;word-break:break-word;
    }
    .ma-ai-wrap {
      align-self:flex-start;display:flex;flex-direction:column;
      width:100%;max-width:100%;box-sizing:border-box;
    }
    .ma-ai {
      background:#fff;color:${DEEP};
      padding:10px 13px;border-radius:3px 16px 16px 16px;
      border:1px solid ${LINE};font-size:.875rem;line-height:1.55;
      white-space:pre-wrap;word-break:break-word;
      box-shadow:0 1px 3px rgba(13,34,24,.06);
    }

    /* ── CTA nudge ── */
    .ma-nudge {
      margin-top:5px;padding:10px 12px;
      background:${SAND2};
      border:1px solid ${LINE};border-top:2px solid ${GREEN};
      border-radius:0 0 12px 12px;
      display:flex;flex-wrap:wrap;align-items:center;
      gap:8px;box-sizing:border-box;
    }
    .ma-nudge-label {
      font-size:.78rem;color:${MUTED};font-weight:500;flex-shrink:0;
    }
    .ma-nudge a {
      display:inline-flex;align-items:center;
      background:${GREEN};color:#fff;
      padding:6px 13px;border-radius:100px;
      font-size:.75rem;font-weight:700;text-decoration:none;
      transition:background .2s;flex-shrink:0;
    }
    .ma-nudge a:hover { background:${DEEP}; }

    /* ── Sources ── */
    .ma-sources {
      margin-top:5px;font-size:.7rem;color:${MUTED};
    }
    .ma-sources a {
      color:${GREEN};text-decoration:none;font-weight:500;
      display:inline-block;margin-top:2px;
    }
    .ma-sources a:hover { text-decoration:underline; }

    /* ── Thinking ── */
    .ma-thinking {
      align-self:flex-start;font-style:italic;
      color:${MUTED};opacity:.65;font-size:.85rem;padding:8px 2px;
    }

    /* ── Form ── */
    #ma-form {
      display:flex;gap:8px;padding:10px;
      border-top:1px solid ${LINE};background:#fff;flex-shrink:0;
      box-sizing:border-box;
    }
    #ma-input {
      flex:1;min-width:0;border:1.5px solid ${LINE};border-radius:11px;
      padding:9px 12px;font-size:.875rem;resize:none;
      font-family:${FONT};color:${DEEP};background:${SAND};
      transition:border-color .2s;outline:none;line-height:1.4;
      box-sizing:border-box;
    }
    #ma-input:focus { border-color:${GREEN};background:#fff; }
    #ma-send {
      background:${GREEN};color:#fff;border:none;border-radius:11px;
      padding:0 15px;cursor:pointer;font-family:${FONT};
      font-size:.875rem;font-weight:600;flex-shrink:0;
      transition:background .2s;
    }
    #ma-send:hover    { background:${DEEP}; }
    #ma-send:disabled { opacity:.4;cursor:default; }

    /* ── Mobile ── */
    @media(max-width:600px){
      #ma-btn {
        bottom:calc(16px + env(safe-area-inset-bottom, 0px));
        right:16px;width:54px;height:54px;
      }
      #ma-panel {
        bottom:calc(84px + env(safe-area-inset-bottom, 0px));
        right:12px;left:12px;
        width:auto;max-width:100%;
        height:72vh;max-height:72vh;
        border-radius:16px;
      }
      #ma-form {
        padding-bottom:10px;
      }
      .ma-nudge { flex-direction:column;align-items:flex-start; }
    }
  `;

  const style = document.createElement('style');
  style.textContent = css;
  document.head.appendChild(style);

  /* ── Button ────────────────────────────────────────────── */
  const btn = document.createElement('button');
  btn.id = 'ma-btn';
  btn.setAttribute('aria-label', 'Chat with Mediations Australia');
  btn.innerHTML = '<img src="' + AVATAR + '" alt="Dan Toombs"><span class="ma-x">&#x2715;</span>';
  document.body.appendChild(btn);

  /* ── Panel ─────────────────────────────────────────────── */
  const panel = document.createElement('div');
  panel.id = 'ma-panel';
  panel.setAttribute('role', 'dialog');
  panel.setAttribute('aria-label', 'Mediations Australia chat');
  panel.innerHTML =
    '<div id="ma-head">' +
      '<div id="ma-head-row">' +
        '<img src="' + AVATAR + '" alt="Dan Toombs">' +
        '<div>' +
          '<div id="ma-head-name">Mediations Australia</div>' +
          '<div id="ma-head-sub">Ask us anything about mediation</div>' +
        '</div>' +
      '</div>' +
      '<div id="ma-disclaimer">General information only — not legal advice for your specific situation.</div>' +
    '</div>' +
    '<div id="ma-log"></div>' +
    '<form id="ma-form">' +
      '<textarea id="ma-input" rows="1" placeholder="Ask a question…" maxlength="500"></textarea>' +
      '<button id="ma-send" type="submit">Send</button>' +
    '</form>';
  document.body.appendChild(panel);

  const log   = panel.querySelector('#ma-log');
  const form  = panel.querySelector('#ma-form');
  const input = panel.querySelector('#ma-input');
  const send  = panel.querySelector('#ma-send');

  /* ── Helpers ────────────────────────────────────────────── */
  function addUser(text) {
    const el = document.createElement('div');
    el.className = 'ma-user';
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

  // showNudge=false for the greeting; true for real answers
  function addAI(text, sources, showNudge) {
    const wrap = document.createElement('div');
    wrap.className = 'ma-ai-wrap';

    const bubble = document.createElement('div');
    bubble.className = 'ma-ai';
    bubble.textContent = text;
    wrap.appendChild(bubble);

    if (showNudge) {
      const nudge = document.createElement('div');
      nudge.className = 'ma-nudge';
      nudge.innerHTML =
        '<span class="ma-nudge-label">Need more information?</span>' +
        '<a href="' + BOOK_URL + '">Book a free consultation &#8594;</a>';
      wrap.appendChild(nudge);
    }

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

  /* ── Toggle ─────────────────────────────────────────────── */
  var greeted = false;
  btn.addEventListener('click', function () {
    var isOpen = panel.classList.toggle('open');
    btn.classList.toggle('open', isOpen);
    if (isOpen) {
      if (!greeted) {
        addAI('Hi! I can answer questions about mediation, our services, costs, and how the process works. What would you like to know?', [], false);
        greeted = true;
      }
      input.focus();
    }
  });

  /* ── Submit ─────────────────────────────────────────────── */
  form.addEventListener('submit', async function (e) {
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
      addAI(data.error || data.answer, data.sources, true);
    } catch (_) {
      thinking.remove();
      addAI('Sorry, something went wrong. Please call (02) 7227 7373.', [], true);
    } finally {
      send.disabled = false;
      input.focus();
    }
  });

  /* ── Auto-grow textarea ─────────────────────────────────── */
  input.addEventListener('input', function () {
    input.style.height = 'auto';
    input.style.height = Math.min(input.scrollHeight, 100) + 'px';
  });

  /* ── Enter = send, Shift+Enter = newline ────────────────── */
  input.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' && !e.shiftKey) { e.preventDefault(); form.requestSubmit(); }
  });
})();
