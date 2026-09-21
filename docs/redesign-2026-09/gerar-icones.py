"""Conjunto de ícones de traço único (24×24, traço 1.9, pontas redondas), usado como máscara em CSS.

Uso, a partir da raiz do repositório: python docs/redesign-2026-09/gerar-icones.py .
"""
import sys
from pathlib import Path

OUT = Path(sys.argv[1]) / "assets" / "icones"
OUT.mkdir(parents=True, exist_ok=True)

LINE = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round">{}</svg>'
ICONS = {
    "check": '<path d="M5 12.6l4.4 4.4L19 7.4"/>',
    "checks": '<path d="M1.8 12.8l4 4 8.2-9.2"/><path d="M10.4 15.4l1.4 1.4 8.4-9.2"/>',
    "recusa": '<path d="M6.5 6.5l11 11M17.5 6.5l-11 11"/>',
    "seta": '<path d="M4.5 12h15M13.5 6l6 6-6 6"/>',
    "seta-baixo": '<path d="M12 4.5v15M6 13.5l6 6 6-6"/>',
    "cadeado": '<path d="M7.5 11V8.2a4.5 4.5 0 019 0V11"/><rect x="5" y="11" width="14" height="9.5" rx="2.2"/><path d="M12 15v2"/>',
    "telefone": '<path d="M8.2 4.2l2 4.3-2 1.6a11.5 11.5 0 005.7 5.7l1.6-2 4.3 2v2.6a1.6 1.6 0 01-1.7 1.6A15.6 15.6 0 014 5.9a1.6 1.6 0 011.6-1.7z"/>',
}
for name, body in ICONS.items():
    (OUT / f"{name}.svg").write_text(LINE.format(body), encoding="utf-8")

# a estrela da marca (marcador de categoria), preenchida
star = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2.6l2.75 6.1 6.65.7-4.97 4.47 1.4 6.53L12 17.05 6.17 20.4l1.4-6.53L2.6 9.4l6.65-.7z"/></svg>'
(OUT / "estrela.svg").write_text(star, encoding="utf-8")
print(sorted(f.name for f in OUT.iterdir()))
