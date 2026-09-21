/* Tia Médica — interação do site. Sem dependências. CSP: script-src 'self'. */
(() => {
  "use strict";
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  const wait = (ms) => new Promise((r) => setTimeout(r, reduceMotion.matches ? 0 : ms));

  document.documentElement.classList.add("js");

  /* ---------------- nav · fio de borda ao rolar ---------------- */
  const nav = $("#nav");
  if (nav) {
    let ticking = false;
    const update = () => { nav.classList.toggle("is-scrolled", window.scrollY > 8); ticking = false; };
    window.addEventListener("scroll", () => {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    }, { passive: true });
    update();
  }

  /* ---------------- menu (celular) ---------------- */
  const menuBtn = $("#nav-menu");
  const links = $("#nav-links");
  if (menuBtn && links) {
    const setOpen = (open) => {
      links.classList.toggle("is-open", open);
      menuBtn.setAttribute("aria-expanded", String(open));
      menuBtn.setAttribute("aria-label", open ? "Fechar menu" : "Abrir menu");
    };
    menuBtn.addEventListener("click", () => setOpen(!links.classList.contains("is-open")));
    $$("a", links).forEach((a) => a.addEventListener("click", () => setOpen(false)));
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && links.classList.contains("is-open")) { setOpen(false); menuBtn.focus(); }
    });
  }

  /* ---------------- hero · as duas pontas do fio ----------------
   * O HTML já traz a conversa completa nos dois celulares. Aqui o visitante pode
   * responder no lugar da Dona Maria e ver a confirmação chegar a quem cuida. */
  const REMINDER = { who: "tia", text: "Oi, Dona Maria! Já são 8h. Passando pra lembrar da Losartana. 💛", time: "08:00" };
  const REGISTERED = "Registrei sua confirmação. ✅ Seu próximo lembrete está programado para 12h.";
  const ARRIVAL = "Oi, Ana. Dona Maria confirmou o remédio das 8h. ✅";
  const QUIET_WAITING = "Quando ela confirmar, a Tia avisa você aqui.";
  const QUIET_LATE = "Por enquanto, nada de alarme. Se ela não confirmar até as 9h, a Tia avisa você.";
  const REPLIES = [
    { label: "Já tomei", time: "08:04", then: [{ who: "tia", text: REGISTERED, time: "08:04" }], arrives: "08:04" },
    { label: "Ainda não", time: "08:06", quiet: QUIET_LATE,
      then: [{ who: "tia", text: "Tudo bem — sem pressa. Volto a lembrar daqui a 30 minutos. Quando tomar, é só me avisar que eu registro.", time: "08:06" }],
      replies: [
        { label: "Já tomei", time: "08:31", then: [{ who: "tia", text: REGISTERED, time: "08:31" }], arrives: "08:31" },
      ] },
  ];

  const duo = $("#sim");
  const her = $("#sim-her");
  const you = $("#sim-you");
  const herStatus = $("#sim-status");
  const youStatus = $("#sim-you-status");
  const tryBox = $("#sim-try");
  const tryLabel = $("#sim-try-label");
  const repliesBox = $("#sim-replies");
  const hop = $("#sim-hop");
  let run = 0; // invalida execuções antigas quando o visitante responde de novo

  const bubble = (who, text, time) => {
    const el = document.createElement("div");
    el.className = "msg is-new" + (who === "me" ? " msg--me" : "");
    el.textContent = text;
    const meta = document.createElement("span");
    meta.className = "msg__meta";
    const t = document.createElement("span");
    t.textContent = time;
    meta.appendChild(t);
    if (who === "me") {
      const tick = document.createElement("span");
      tick.className = "tick";
      tick.setAttribute("aria-hidden", "true");
      meta.appendChild(tick);
    }
    el.appendChild(meta);
    return el;
  };

  const typingEl = () => {
    const el = document.createElement("div");
    el.className = "msg typing";
    el.setAttribute("aria-hidden", "true");
    el.append(document.createElement("i"), document.createElement("i"), document.createElement("i"));
    return el;
  };

  const quiet = (text) => {
    const p = document.createElement("p");
    p.className = "chat__quiet";
    p.textContent = text;
    you.replaceChildren(p);
  };

  async function say(id, box, status, msg) {
    if (status) status.textContent = "digitando…";
    const t = typingEl();
    box.appendChild(t);
    await wait(Math.min(1300, 450 + msg.text.length * 11));
    t.remove();
    if (status) status.textContent = "online";
    if (id !== run) return null;
    const el = bubble(msg.who, msg.text, msg.time);
    box.appendChild(el);
    await wait(300);
    return el;
  }

  async function sendAcross(id, time) {
    hop.textContent = time;
    duo.classList.remove("is-sending");
    void duo.offsetWidth; // reinicia a animação do pulso
    duo.classList.add("is-sending");
    await wait(1100);
    if (id !== run) return;
    you.replaceChildren();
    const el = await say(id, you, youStatus, { who: "tia", text: ARRIVAL, time });
    if (el) el.classList.add("is-landing");
  }

  function offer(id, replies, label) {
    repliesBox.replaceChildren();
    tryLabel.textContent = label;
    replies.forEach((r) => {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "reply";
      b.textContent = r.label;
      b.addEventListener("click", () => choose(r));
      repliesBox.appendChild(b);
    });
  }

  async function choose(reply) {
    const id = ++run;
    $$("button", repliesBox).forEach((b) => { b.disabled = true; });
    // primeira resposta de uma rodada: volta ao lembrete das 8h
    if (REPLIES.includes(reply)) {
      her.replaceChildren(bubble(REMINDER.who, REMINDER.text, REMINDER.time));
      her.firstElementChild.classList.remove("is-new");
      quiet(QUIET_WAITING);
    }
    her.appendChild(bubble("me", reply.label, reply.time));
    await wait(450);
    for (const m of reply.then) {
      if (id !== run) return;
      await say(id, her, herStatus, m);
    }
    if (id !== run) return;
    if (reply.quiet) quiet(reply.quiet);
    if (reply.arrives) await sendAcross(id, reply.arrives);
    if (id !== run) return;
    if (reply.replies) offer(id, reply.replies, "E meia hora depois:");
    else offer(id, REPLIES, "Responda de novo no lugar dela:");
  }

  if (duo && her && you && tryBox && repliesBox && hop) {
    tryBox.hidden = false;
    offer(run, REPLIES, "Responda no lugar dela:");
  }

  /* ---------------- um dia com a Tia · o fio desce trançando ----------------
   * Sem isto o fio já está inteiro na página. Aqui ele acompanha a rolagem: a trama é
   * revelada até a altura da ponta, gira enquanto desce, e os três fios seguem soltos
   * logo abaixo, entrando na trança. Cada hora acende quando o fio chega nela. */
  const fio = $("#day-fio");
  const lista = fio && fio.parentElement;
  if (fio && lista) {
    const PERIODO = 64, AMPLITUDE = 6, EIXO = 14, CAUDA = 34;
    const soltos = [[".fio__c", EIXO], [".fio__b", 23], [".fio__a", 5]].map(([sel, x]) => [$(".day__cauda " + sel, fio), x]);
    const momentos = $$(".moment", lista);
    let agendado = false;

    const desenha = () => {
      agendado = false;
      const r = lista.getBoundingClientRect();
      const corte = Math.max(0, Math.min(r.height, window.innerHeight * 0.62 - r.top));
      const fase = (corte * 0.5) % PERIODO;
      fio.style.setProperty("--fio-corte", corte + "px");
      fio.style.setProperty("--fio-fase", fase + "px");
      // onde cada fio da trama está na altura do corte — é dali que a ponta solta sai
      const u = (2 * Math.PI * (corte - fase)) / PERIODO;
      const naTrama = [EIXO + AMPLITUDE * Math.cos(u), EIXO - AMPLITUDE * Math.sin(u), EIXO + AMPLITUDE * Math.sin(u)];
      const solta = Math.min(1, (r.height - corte) / 80); // perto do fim a ponta se recolhe
      soltos.forEach(([path, alvo], i) => {
        const x0 = naTrama[i].toFixed(1);
        const x1 = (EIXO + (alvo - EIXO) * solta).toFixed(1);
        path.setAttribute("d", `M${x0} 0C${x0} 12 ${x1} 18 ${x1} ${CAUDA}`);
      });
      momentos.forEach((m) => {
        const hora = $(".moment__time", m).getBoundingClientRect();
        m.classList.toggle("is-reached", hora.top + hora.height / 2 - r.top <= corte);
      });
    };
    const agenda = () => { if (!agendado) { agendado = true; requestAnimationFrame(desenha); } };
    const liga = () => {
      const vivo = !reduceMotion.matches;
      fio.classList.toggle("is-vivo", vivo);
      if (vivo) { desenha(); return; }
      fio.style.removeProperty("--fio-corte");
      fio.style.removeProperty("--fio-fase");
      momentos.forEach((m) => m.classList.remove("is-reached"));
    };
    window.addEventListener("scroll", () => { if (!reduceMotion.matches) agenda(); }, { passive: true });
    window.addEventListener("resize", () => { if (!reduceMotion.matches) agenda(); });
    reduceMotion.addEventListener("change", liga);
    liga();
  }

  /* ---------------- dúvidas · acordeão ----------------
   * No HTML as respostas vêm abertas (é assim que ficam sem JavaScript); aqui elas recolhem. */
  $$(".faq__q").forEach((q) => {
    q.setAttribute("aria-expanded", "false");
    q.addEventListener("click", () => {
      const item = q.closest(".faq__item");
      const open = !item.classList.contains("is-open");
      item.classList.toggle("is-open", open);
      q.setAttribute("aria-expanded", String(open));
    });
  });

  /* ---------------- barra fixa depois do hero (celular) ---------------- */
  const dock = $("#dock");
  const hero = $("#hero");
  if (dock && hero && "IntersectionObserver" in window) {
    const io = new IntersectionObserver((entries) => {
      const e = entries[0];
      const visible = !e.isIntersecting && e.boundingClientRect.bottom < 0;
      dock.classList.toggle("is-visible", visible);
      if (nav) nav.classList.toggle("has-dock", visible); // no celular, uma ação por tela
    }, { threshold: 0 });
    io.observe(hero);
  }
})();
