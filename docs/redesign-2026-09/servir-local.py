"""Servidor estático local que respeita os rewrites do vercel.json (só para desenvolvimento).

Uso, a partir da raiz do repositório: python docs/redesign-2026-09/servir-local.py . 4188
(`npx serve` não aplica /privacidade nem /excluir-conta.)
"""
import json
import sys
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(sys.argv[1]).resolve()
PORT = int(sys.argv[2]) if len(sys.argv) > 2 else 4188
REWRITES = {
    r["source"]: r["destination"]
    for r in json.loads((ROOT / "vercel.json").read_text(encoding="utf-8")).get("rewrites", [])
}


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *a, **k):
        super().__init__(*a, directory=str(ROOT), **k)

    def do_GET(self):
        parts = urlsplit(self.path)
        if parts.path in REWRITES:
            self.path = REWRITES[parts.path] + (("?" + parts.query) if parts.query else "")
        super().do_GET()

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, *a):
        pass


ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
