/* Tia Médica — interação do site. Sem dependências. CSP: script-src 'self'. */
(() => {
  "use strict";
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const wait = (ms) => new Promise((r) => setTimeout(r, reduceMotion ? 0 : ms));

  /* ---------------- N12 · banner + barra que recolhe ---------------- */
  const nav = $("#nav");
  const banner = $("#banner");
  const bannerX = $("#banner-x");
  if (nav) {
    let lastY = window.scrollY;
    let ticking = false;
    const update = () => {
      const y = window.scrollY;
      nav.classList.toggle("is-scrolled", y > 8);
      if (y < 48) nav.classList.remove("is-compact");
      else if (y > lastY + 4) nav.classList.add("is-compact");
      else if (y < lastY - 4) nav.classList.remove("is-compact");
      lastY = y;
      ticking = false;
    };
    window.addEventListener("scroll", () => {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    }, { passive: true });
    update();
    if (bannerX && banner) {
      bannerX.addEventListener("click", () => {
        document.documentElement.style.setProperty("--banner-h", "0px");
        nav.classList.add("is-dismissed");
        nav.classList.remove("is-compact");
      });
    }
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

  /* ---------------- hero · papéis + simulador ---------------- */
  const WPP = "https://wa.me/551140402232?text=";
  const wa = (t) => WPP + encodeURIComponent(t);
  const ROLES = {
    mim: {
      lede: "Remédios, hábitos e consultas na hora certa — numa conversa de WhatsApp que você já sabe usar. A Tia lembra, você confirma, e fica registrado.",
      cta: { label: "Falar com a Tia", href: wa("Oi! Quero começar com os lembretes gratuitos.") },
      script: {
        start: [{ who: "tia", text: "Oi, Dona Maria! Já são 8h. Passando pra lembrar da Losartana. 💛", time: "08:00" }],
        replies: [
          { label: "Já tomei", time: "08:04", then: [
            { who: "tia", text: "Registrei sua confirmação. ✅ Seu próximo lembrete está programado para 12h.", time: "08:04" },
            { who: "tia", text: "Conta comigo. Se precisar, é só me chamar.", time: "08:04" },
          ] },
          { label: "Ainda não", time: "08:06", then: [
            { who: "tia", text: "Tudo bem — sem pressa. Volto a lembrar daqui a 30 minutos. Quando tomar, é só me avisar que eu registro.", time: "08:06" },
          ], replies: [
            { label: "Já tomei", time: "08:31", then: [
              { who: "tia", text: "Registrei sua confirmação. ✅ Seu próximo lembrete está programado para 12h.", time: "08:31" },
            ] },
          ] },
        ],
      },
    },
    mae: {
      lede: "Você não precisa ligar todo dia pra perguntar se ela tomou. A Tia lembra, ela confirma, e você fica sabendo — sem sua mãe se sentir fiscalizada.",
      cta: { label: "Falar com a Tia", href: wa("Oi! Vim pelo site e quero conhecer a Tia.") },
      script: {
        start: [{ who: "tia", text: "Oi, Ana. Dona Maria confirmou o remédio das 8h. ✅", time: "08:31" }],
        replies: [
          { label: "Obrigada 💛", time: "08:40", then: [
            { who: "tia", text: "De nada. Se ela não confirmar até as 9h, eu te aviso — sem você precisar ligar todo dia.", time: "08:40" },
          ] },
          { label: "E se ela esquecer?", time: "08:41", then: [
            { who: "tia", text: "Eu lembro de novo, com jeito — atraso nunca vira culpa. Se mesmo assim ela não confirmar, eu te aviso.", time: "08:41" },
          ] },
        ],
      },
    },
    clinica: {
      lede: "A adesão vaza no intervalo entre as consultas. A Tia sustenta esse intervalo sem sua recepção operar mais um sistema — e devolve o paciente melhor informado.",
      cta: { label: "Propor uma parceria", href: "mailto:admin@tiamedica.com?subject=" + encodeURIComponent("Proposta de piloto para clínica") },
      script: {
        start: [{ who: "tia", text: "Oi, Seu José. Sua consulta de retorno na clínica é dia 14, às 9h. Quer que eu lembre na véspera?", time: "16:10" }],
        replies: [
          { label: "Quero", time: "16:12", then: [
            { who: "tia", text: "Combinado. Lembro você dia 13 à tarde. Até lá, sigo com os lembretes dos remédios. 💛", time: "16:12" },
          ] },
          { label: "Não precisa", time: "16:12", then: [
            { who: "tia", text: "Tudo bem. Sigo com os lembretes dos remédios — se mudar de ideia, é só me avisar.", time: "16:12" },
          ] },
        ],
      },
    },
  };

  const lede = $("#hero-lede");
  const heroCta = $("#hero-cta");
  const heroCtaLabel = $("#hero-cta-label");
  const simBody = $("#sim-body");
  const simReplies = $("#sim-replies");
  const simStatus = $("#sim-status");
  const simReplay = $("#sim-replay");
  let run = 0; // invalida execuções antigas quando o papel muda

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
      tick.textContent = "✓✓";
      meta.appendChild(tick);
    }
    el.appendChild(meta);
    return el;
  };

  const typingEl = () => {
    const el = document.createElement("div");
    el.className = "msg typing";
    el.setAttribute("aria-hidden", "true");
    el.innerHTML = "<i></i><i></i><i></i>";
    return el;
  };

  async function say(id, msgs) {
    for (const m of msgs) {
      if (id !== run) return;
      if (m.who === "tia") {
        if (simStatus) simStatus.textContent = "digitando…";
        const t = typingEl();
        simBody.appendChild(t);
        await wait(Math.min(1400, 500 + m.text.length * 12));
        t.remove();
        if (simStatus) simStatus.textContent = "online";
      }
      if (id !== run) return;
      simBody.appendChild(bubble(m.who, m.text, m.time));
      await wait(320);
    }
  }

  function offer(id, replies, onDone) {
    simReplies.replaceChildren();
    if (!replies || !replies.length) { onDone(); return; }
    replies.forEach((r) => {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "reply";
      b.textContent = r.label;
      b.addEventListener("click", async () => {
        if (id !== run) return;
        $$("button", simReplies).forEach((x) => { x.disabled = true; });
        simBody.appendChild(bubble("me", r.label, r.time));
        simReplies.replaceChildren();
        await wait(500);
        await say(id, r.then || []);
        if (id !== run) return;
        offer(id, r.replies, onDone);
      });
      simReplies.appendChild(b);
    });
  }

  async function play(roleKey) {
    if (!simBody || !simReplies) return;
    const id = ++run;
    const script = ROLES[roleKey].script;
    simReplay.hidden = true;
    simBody.replaceChildren();
    const day = document.createElement("span");
    day.className = "chat__day";
    day.textContent = "hoje";
    simBody.appendChild(day);
    simReplies.replaceChildren();
    await wait(400);
    await say(id, script.start);
    if (id !== run) return;
    offer(id, script.replies, () => { if (id === run) simReplay.hidden = false; });
  }

  let currentRole = "mim";
  function setRole(key, { replay = true } = {}) {
    currentRole = key;
    $$(".role").forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.role === key)));
    const role = ROLES[key];
    if (lede) {
      lede.classList.add("is-swapping");
      setTimeout(() => { lede.textContent = role.lede; lede.classList.remove("is-swapping"); }, reduceMotion ? 0 : 200);
    }
    if (heroCta && heroCtaLabel) {
      heroCta.href = role.cta.href;
      heroCtaLabel.textContent = role.cta.label;
      if (role.cta.href.startsWith("mailto:")) { heroCta.removeAttribute("target"); heroCta.removeAttribute("rel"); }
      else { heroCta.target = "_blank"; heroCta.rel = "noopener"; }
    }
    if (replay) play(key);
  }

  $$(".role").forEach((b) => b.addEventListener("click", () => {
    if (b.dataset.role !== currentRole) setRole(b.dataset.role);
  }));
  if (simReplay) simReplay.addEventListener("click", () => play(currentRole));

  // começa quando o hero está visível (não antes)
  const sim = $("#sim");
  if (sim && "IntersectionObserver" in window) {
    const io = new IntersectionObserver((entries) => {
      if (entries.some((e) => e.isIntersecting)) { io.disconnect(); play(currentRole); }
    }, { threshold: 0.4 });
    io.observe(sim);
  } else if (sim) {
    play(currentRole);
  }

  /* ---------------- Feature Stack · painel sincronizado com o scroll ---------------- */
  const stages = $$(".stage");
  const plates = $$(".plate");
  const threads = $$(".pane__thread");
  const wide = window.matchMedia("(min-width: 60rem)");
  if (stages.length && "IntersectionObserver" in window) {
    const activate = (n) => {
      stages.forEach((s) => s.classList.toggle("is-active", s.dataset.stage === n));
      plates.forEach((p) => p.classList.toggle("is-active", p.dataset.plate === n));
      threads.forEach((t) => t.classList.toggle("is-active", t.dataset.thread === n));
    };
    let io = null;
    const arm = () => {
      if (io) { io.disconnect(); io = null; }
      if (!wide.matches) { activate("1"); return; }
      io = new IntersectionObserver((entries) => {
        entries.forEach((e) => { if (e.isIntersecting) activate(e.target.dataset.stage); });
      }, { rootMargin: "-45% 0px -45% 0px", threshold: 0 });
      stages.forEach((s) => io.observe(s));
    };
    arm();
    wide.addEventListener("change", arm);
  }

  /* ---------------- dúvidas · acordeão ---------------- */
  $$(".faq__q").forEach((q) => {
    q.addEventListener("click", () => {
      const item = q.closest(".faq__item");
      const open = !item.classList.contains("is-open");
      item.classList.toggle("is-open", open);
      q.setAttribute("aria-expanded", String(open));
    });
  });

  /* ---------------- C4 · barra fixa depois do hero (celular) ---------------- */
  const dock = $("#dock");
  const hero = $("#hero");
  if (dock && hero && "IntersectionObserver" in window) {
    const io = new IntersectionObserver((entries) => {
      const e = entries[0];
      dock.classList.toggle("is-visible", !e.isIntersecting && e.boundingClientRect.bottom < 0);
    }, { threshold: 0 });
    io.observe(hero);
  }
})();
