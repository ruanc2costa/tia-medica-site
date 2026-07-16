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


def reveal_scroll_animations(page) -> None:
    page.evaluate(
        """async () => {
            const step = Math.max(500, window.innerHeight * 0.8);
            for (let y = 0; y <= document.body.scrollHeight; y += step) {
                window.scrollTo(0, y);
                await new Promise((resolve) => setTimeout(resolve, 80));
            }
            document
                .querySelectorAll('.p-card,.step,.f-card,.v-card,.pe-card,.t-card,.r-card,.about-card,.plat-card')
                .forEach((element) => {
                    element.style.opacity = '1';
                    element.style.transform = 'translateY(0)';
                });
            document.documentElement.style.scrollBehavior = 'auto';
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
    ]
    lower = text.lower()
    found = [claim for claim in forbidden if claim in lower]
    assert not found, f"Legacy claims still present: {found}"


def run_desktop(browser) -> None:
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    console_errors = []
    page.on("console", lambda message: console_errors.append(message.text) if message.type == "error" else None)
    page_errors = []
    page.on("pageerror", lambda error: page_errors.append(str(error)))

    response = page.goto(BASE_URL, wait_until="networkidle")
    assert response and response.ok, f"Home failed: {response.status if response else 'no response'}"
    assert page.title() == "Tia Médica — Sua rotina de cuidados com a saúde pelo WhatsApp"
    assert "Organize sua rotina de cuidados com a saúde" in page.locator("h1").inner_text()
    assert page.locator('a[href^="mailto:admin@tiamedica.com"]').count() >= 5
    assert page.locator('a[href*="wa.me"]').count() == 0
    assert page.locator("form").count() == 0
    assert page.locator('a[href="#"]').count() == 0
    assert page.locator("main#conteudo-principal").count() == 1
    assert page.locator('.skip-link[href="#conteudo-principal"]').count() == 1
    assert page.locator('script[src="/assets/site.js"]').count() == 1
    assert_no_legacy_claims(page.locator("body").inner_text())
    page.screenshot(path=str(TEMP_DIR / "tia-site-top.png"))

    faq_button = page.locator(".faq-q").first
    assert faq_button.get_attribute("aria-expanded") == "false"
    assert faq_button.get_attribute("aria-controls")
    faq_button.click()
    assert faq_button.get_attribute("aria-expanded") == "true"
    assert page.locator(".faq-item.active").count() == 1
    assert page.locator(".faq-item.active .faq-a").get_attribute("aria-hidden") == "false"

    broken_images = page.locator("img").evaluate_all(
        "(images) => images.filter((image) => !image.complete || image.naturalWidth === 0).length"
    )
    assert broken_images == 0, f"Broken images: {broken_images}"
    assert not page_errors, f"Page errors: {page_errors}"
    assert not console_errors, f"Console errors: {console_errors}"
    reveal_scroll_animations(page)
    page.screenshot(path=str(TEMP_DIR / "tia-site-desktop.png"), full_page=True)
    page.close()


def run_mobile(browser) -> None:
    page = browser.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=1)
    page.goto(BASE_URL, wait_until="networkidle")

    hamburger = page.locator(".hamburger")
    assert hamburger.is_visible()
    assert hamburger.get_attribute("aria-expanded") == "false"
    hamburger.click()
    assert hamburger.get_attribute("aria-expanded") == "true"
    assert page.locator("#navLinks").evaluate("(element) => element.classList.contains('open')")
    page.keyboard.press("Escape")
    assert hamburger.get_attribute("aria-expanded") == "false"
    assert not page.locator("#navLinks").evaluate("(element) => element.classList.contains('open')")

    overflow = page.evaluate(
        "() => ({scrollWidth: document.documentElement.scrollWidth, clientWidth: document.documentElement.clientWidth})"
    )
    assert overflow["scrollWidth"] <= overflow["clientWidth"] + 1, f"Horizontal overflow: {overflow}"
    reveal_scroll_animations(page)
    page.screenshot(path=str(TEMP_DIR / "tia-site-mobile.png"), full_page=True)
    page.close()


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
    for path in ("/robots.txt", "/sitemap.xml", "/assets/site.js"):
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
    run_mobile(chromium)
    run_secondary_pages(chromium)
    run_static_endpoints(request_context)
    request_context.dispose()
    chromium.close()

print("site smoke test: PASS")
