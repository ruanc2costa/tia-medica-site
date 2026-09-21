"""Smoke test do site.

Execute a partir da raiz do repositório contra um servidor estático local.
Defina SITE_BASE_URL quando a porta não for 4188.
"""

from pathlib import Path
import json
import os

from playwright.sync_api import sync_playwright


BASE_URL = os.environ.get("SITE_BASE_URL", "http://127.0.0.1:4188")
TEMP_DIR = Path.home() / "AppData" / "Local" / "Temp"
WIDTHS = {"mobile": (390, 844), "tablet": (768, 1024), "desktop": (1440, 900)}


def scroll_through(page) -> None:
    page.evaluate(
        """async () => {
            document.documentElement.style.scrollBehavior = 'auto';
            const step = Math.max(500, window.innerHeight * 0.8);
            for (let y = 0; y <= document.body.scrollHeight; y += step) {
                window.scrollTo(0, y);
                await new Promise((resolve) => setTimeout(resolve, 80));
            }
            window.scrollTo(0, 0);
        }"""
    )
    page.wait_for_timeout(100)


def assert_no_legacy_claims(text: str) -> None:
    forbidden = [
        "100% gratuito",
        "totalmente gratuito",
        "24/7",
        "24x7",
        "entende tudo",
        "em tempo real",
        "horário exato",
        "reduza reinternações",
        "conformidade total",
        "100% compatível",
        "nunca mais esqueça",
    ]
    lower = text.lower()
    found = [claim for claim in forbidden if claim in lower]
    assert not found, f"Legacy claims still present: {found}"


def assert_no_horizontal_overflow(page, label: str) -> None:
    overflow = page.evaluate(
        """() => {
            const root = document.documentElement;
            const wide = [...document.querySelectorAll('body *')]
                .filter((el) => getComputedStyle(el).position !== 'fixed')
                .filter((el) => el.getBoundingClientRect().right > root.clientWidth + 1)
                .map((el) => el.className || el.tagName);
            return {scrollWidth: root.scrollWidth, clientWidth: root.clientWidth, wide: wide.slice(0, 5)};
        }"""
    )
    assert overflow["scrollWidth"] <= overflow["clientWidth"] + 1, f"Horizontal overflow ({label}): {overflow}"
    assert not overflow["wide"], f"Elements wider than the viewport ({label}): {overflow}"


def run_desktop(browser) -> None:
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    console_errors = []
    page.on("console", lambda message: console_errors.append(message.text) if message.type == "error" else None)
    page_errors = []
    page.on("pageerror", lambda error: page_errors.append(str(error)))

    response = page.goto(BASE_URL, wait_until="networkidle")
    assert response and response.ok, f"Home failed: {response.status if response else 'no response'}"
    assert page.title() == "Tia Médica — a rotina de cuidado, organizada por conversa"
    assert "Você não precisa ligar todo dia" in page.locator("h1").inner_text()
    assert page.locator("h1").count() == 1
    assert page.locator('a[href^="mailto:admin@tiamedica.com"]').count() >= 6

    cta_links = page.locator("a[data-cta]")
    assert cta_links.count() >= 3, f"Expected >=3 CTAs data-cta, got {cta_links.count()}"
    for href in cta_links.evaluate_all("(links) => links.map((link) => link.getAttribute('href'))"):
        assert href.startswith("https://wa.me/") and "text=" in href, f"CTA sem destino de WhatsApp: {href}"

    # ofertas: preços e condições preservados, com o status de cada uma
    assert page.locator("section#precos").count() == 1
    pricing_text = page.locator("section#precos").inner_text()
    for snippet in ("R$ 0", "Preço em breve", "Mercado Pago", "192", "Em piloto", "Em breve"):
        assert snippet in pricing_text, f"{snippet!r} missing from #precos"
    # decisão do fundador (2026-09-20): os valores das ofertas pagas ainda não estão definidos — nenhum preço na página além do R$ 0
    whole_page = page.content()
    for price in ("49,90", "69,90"):
        assert price not in whole_page, f"Preço {price} não pode aparecer enquanto não for anunciado"
    # decisão do fundador (2026-09-20): tudo o que é pago está "em breve"; só a rotina gratuita abre o WhatsApp
    assert "Disponível" not in pricing_text, "Nenhuma oferta paga está disponível ainda"
    assert page.locator('#precos a[href*="wa.me"]').count() == 1
    assert page.locator("#precos .status--plan").count() >= 3
    assert "lista de espera" in pricing_text.lower()
    assert "crédito devolvido" in pricing_text.lower()
    # decisão do fundador (2026-09-20): leitura de receita por foto é da rotina gratuita, não item do Plano
    assert "por foto" not in pricing_text.lower(), "Leitura por foto não é item pago"

    # a lista do que a Tia recusa precisa ser, de fato, a maior
    does, refuses = page.locator(".marks--yes li").count(), page.locator(".marks--no li").count()
    assert does >= 5 and refuses > does, f"Recusas ({refuses}) devem superar o que ela faz ({does})"
    # preço nunca em fonte mono: o zero cortado vira "R$ Ø" para quem lê
    price_fonts = page.locator("#precos .price").evaluate_all("(els) => els.map((el) => getComputedStyle(el).fontFamily)")
    assert price_fonts and all("Mono" not in font for font in price_fonts), price_fonts

    # contratos de estrutura e de CSP
    assert page.locator("form").count() == 0
    assert page.locator('a[href="#"]').count() == 0
    assert page.locator("main#conteudo").count() == 1
    assert page.locator('.skip[href="#conteudo"]').count() == 1
    assert page.locator('script[src="/assets/tia.js"]').count() == 1
    assert page.locator("script:not([src]):not([type='application/ld+json'])").count() == 0
    broken_anchors = page.locator('a[href^="#"]').evaluate_all(
        "(links) => links.map((l) => l.getAttribute('href')).filter((h) => !document.getElementById(h.slice(1)))"
    )
    assert not broken_anchors, f"Anchors without target: {broken_anchors}"
    for anchor in ("como-funciona", "precos", "duvidas", "clinicas"):
        assert page.locator(f"#{anchor}").count() == 1, f"#{anchor} missing"

    body_text = page.locator("body").inner_text()
    assert_no_legacy_claims(body_text)
    assert "SAMU 192" in body_text
    assert "nomes fictícios" in body_text
    page.screenshot(path=str(TEMP_DIR / "tia-site-top.png"))

    # demonstração: a confirmação dela chega ao celular de quem cuida
    her, you = page.locator("#sim-her"), page.locator("#sim-you")
    assert "confirmou o remédio das 8h" in you.inner_text()
    page.locator("#sim-replies button", has_text="Ainda não").click()
    page.wait_for_function("document.querySelector('#sim-try-label').textContent.includes('meia hora')")
    assert "sem pressa" in her.inner_text()
    assert "confirmou" not in you.inner_text(), "Quem cuida não pode ser avisado antes da confirmação"
    page.locator("#sim-replies button", has_text="Já tomei").click()
    page.wait_for_function("document.querySelector('#sim-you').innerText.includes('08:31')")
    assert "confirmou o remédio das 8h" in you.inner_text()

    # dúvidas
    faq_button = page.locator(".faq__q").first
    assert faq_button.get_attribute("aria-expanded") == "false"
    assert faq_button.get_attribute("aria-controls")
    faq_button.click()
    assert faq_button.get_attribute("aria-expanded") == "true"
    assert page.locator(".faq__item.is-open").count() == 1

    scroll_through(page)
    broken_images = page.locator("img").evaluate_all(
        "(images) => images.filter((image) => !image.complete || image.naturalWidth === 0).length"
    )
    assert broken_images == 0, f"Broken images: {broken_images}"
    assert not page_errors, f"Page errors: {page_errors}"
    assert not console_errors, f"Console errors: {console_errors}"
    page.screenshot(path=str(TEMP_DIR / "tia-site-desktop.png"), full_page=True)
    page.close()


def run_widths(browser) -> None:
    for label, (width, height) in WIDTHS.items():
        page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=1)
        page.goto(BASE_URL, wait_until="networkidle")
        scroll_through(page)
        assert_no_horizontal_overflow(page, label)
        page.close()


def run_mobile(browser) -> None:
    page = browser.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=1)
    page.goto(BASE_URL, wait_until="networkidle")

    menu = page.locator("#nav-menu")
    assert menu.is_visible()
    assert menu.get_attribute("aria-expanded") == "false"
    menu.click()
    assert menu.get_attribute("aria-expanded") == "true"
    assert page.locator("#nav-links").evaluate("(element) => element.classList.contains('is-open')")
    page.keyboard.press("Escape")
    assert menu.get_attribute("aria-expanded") == "false"
    assert not page.locator("#nav-links").evaluate("(element) => element.classList.contains('is-open')")

    # a ação principal e o começo da conversa aparecem antes da primeira dobra
    cta_bottom = page.locator(".hero a[data-cta]").first.evaluate("(el) => el.getBoundingClientRect().bottom")
    assert cta_bottom <= 844, f"CTA do hero abaixo da dobra no celular: {cta_bottom}"
    first_message_bottom = page.locator("#sim-her .msg").first.evaluate("(el) => el.getBoundingClientRect().bottom")
    assert first_message_bottom <= 844, f"Lembrete das 8h abaixo da dobra no celular: {first_message_bottom}"
    scroll_through(page)
    page.screenshot(path=str(TEMP_DIR / "tia-site-mobile.png"), full_page=True)
    page.close()


def run_without_javascript(browser) -> None:
    """Nada essencial depende de script: a conversa completa e as respostas das dúvidas ficam na página."""
    context = browser.new_context(java_script_enabled=False, viewport={"width": 390, "height": 844})
    page = context.new_page()
    page.goto(BASE_URL, wait_until="networkidle")
    assert "Já tomei" in page.locator("#sim-her").inner_text()
    assert "confirmou o remédio das 8h" in page.locator("#sim-you").inner_text()
    assert page.locator("#sim-try").is_hidden(), "Botões sem função não podem aparecer sem JavaScript"
    assert page.locator("#faq-1 p").is_visible()
    assert page.locator(".faq__q").first.get_attribute("aria-expanded") == "true", "Resposta aberta precisa dizer que está aberta"
    context.close()


def run_thread_animation(browser) -> None:
    """O fio da linha do tempo desce trançando com a rolagem e acende cada hora quando chega nela."""
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto(BASE_URL, wait_until="networkidle")
    page.add_style_tag(content="html{scroll-behavior:auto!important}")
    list_top, list_height = page.evaluate(
        "() => { const r = document.querySelector('.day__list').getBoundingClientRect(); return [r.top + scrollY, r.height]; }"
    )
    state = "() => { const f = document.getElementById('day-fio'); return [f.classList.contains('is-vivo'), parseFloat(getComputedStyle(f).getPropertyValue('--fio-corte')), document.querySelectorAll('.moment.is-reached').length]; }"
    page.evaluate("(y) => window.scrollTo(0, y)", list_top - 200)
    page.wait_for_timeout(300)
    alive, early_cut, early_lit = page.evaluate(state)
    page.evaluate("(y) => window.scrollTo(0, y)", list_top + list_height * 0.6)
    page.wait_for_timeout(300)
    _, late_cut, late_lit = page.evaluate(state)
    assert alive, "Fio sem animação com movimento liberado"
    assert 0 < early_cut < late_cut < list_height, f"O fio não acompanha a rolagem: {early_cut} → {late_cut} de {list_height}"
    assert late_lit > early_lit, f"As horas não acendem com a chegada do fio: {early_lit} → {late_lit}"
    assert page.locator(".day__cauda .fio__a").get_attribute("d"), "Ponta solta do fio sem traçado"
    page.close()


def run_reduced_motion(browser) -> None:
    context = browser.new_context(reduced_motion="reduce", viewport={"width": 1440, "height": 900})
    page = context.new_page()
    page.goto(BASE_URL, wait_until="networkidle")
    durations = page.evaluate(
        """() => ['.msg', '.cta', '.day__fio', '.faq__a'].map((selector) => {
            const style = getComputedStyle(document.querySelector(selector));
            return Math.max(...style.transitionDuration.split(',').concat(style.animationDuration.split(',')).map(parseFloat));
        })"""
    )
    assert max(durations) <= 0.001, f"Movimento com prefers-reduced-motion: {durations}"
    # o fio fica inteiro e parado
    static = page.evaluate("() => { const f = document.getElementById('day-fio'); return [f.classList.contains('is-vivo'), getComputedStyle(f.querySelector('.day__cauda')).display]; }")
    assert static == [False, "none"], f"Fio animado com prefers-reduced-motion: {static}"
    context.close()


def run_secondary_pages(browser) -> None:
    expectations = {
        "/politica-de-privacidade.html": [
            "Versão 1.2",
            "confirmações reportadas",
            "3 (três) dias úteis",
        ],
        "/excluir-conta.html": [
            "excluir minha conta",
            "confirmação explícita",
            "confirmações reportadas",
        ],
    }
    for path, snippets in expectations.items():
        page = browser.new_page()
        response = page.goto(BASE_URL + path, wait_until="networkidle")
        assert response and response.ok, f"{path} failed"
        assert page.locator("main#conteudo-principal").count() == 1
        assert page.locator('.skip-link[href="#conteudo-principal"]').count() == 1
        body = page.locator("body").inner_text()
        assert body.strip()
        for snippet in snippets:
            assert snippet in body, f"{snippet!r} missing from {path}"
        screenshot_name = "tia-site-" + Path(path).stem + ".png"
        page.screenshot(path=str(TEMP_DIR / screenshot_name), full_page=True)
        page.close()


def run_static_endpoints(request) -> None:
    for path in (
        "/robots.txt",
        "/sitemap.xml",
        "/assets/site.js",
        "/assets/tia.js",
        "/assets/tia.css",
        "/assets/og-tia-2026.jpg",
    ):
        response = request.get(BASE_URL + path)
        assert response.ok, f"{path} failed with {response.status}"

    missing = request.get(BASE_URL + "/rota-que-nao-existe")
    assert missing.status == 404, f"Expected 404, got {missing.status}"


config = json.loads(Path("vercel.json").read_text(encoding="utf-8"))
assert not any(rule["source"] == "/(.*)" for rule in config["rewrites"])
privacy_rewrite = next((rule for rule in config["rewrites"] if rule["source"] == "/privacidade"), None)
assert privacy_rewrite == {
    "source": "/privacidade",
    "destination": "/politica-de-privacidade.html",
}
headers = {
    item["key"]: item["value"]
    for rule in config["headers"]
    for item in rule["headers"]
}
assert headers["Content-Security-Policy"]
assert "script-src 'self';" in headers["Content-Security-Policy"]
assert "script-src 'self' 'unsafe-inline'" not in headers["Content-Security-Policy"]
assert headers["Referrer-Policy"] == "strict-origin-when-cross-origin"
assert headers["Strict-Transport-Security"] == "max-age=31536000"

for html_path in ("index.html", "politica-de-privacidade.html", "excluir-conta.html"):
    assert "onclick=" not in Path(html_path).read_text(encoding="utf-8")


with sync_playwright() as playwright:
    chromium = playwright.chromium.launch(headless=True)
    request_context = playwright.request.new_context()
    run_desktop(chromium)
    run_widths(chromium)
    run_mobile(chromium)
    run_without_javascript(chromium)
    run_thread_animation(chromium)
    run_reduced_motion(chromium)
    run_secondary_pages(chromium)
    run_static_endpoints(request_context)
    request_context.dispose()
    chromium.close()

print("site smoke test: PASS")
