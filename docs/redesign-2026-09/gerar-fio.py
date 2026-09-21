"""Gera os SVGs do fio trançado ao longo de curvas (travessia do hero e coração do compromisso).

Cada fio é a curva-base deslocada pela normal com uma senoide; os cruzamentos alternam
quem passa por cima. Uso, a partir da raiz do repositório:

    python docs/redesign-2026-09/gerar-fio.py .

Saída: assets/fio/hop-largo.svg, hop-estreito.svg e coracao.svg. Se mudar uma curva do hero,
repita o mesmo caminho em `--hop-path` no assets/tia.css (é por ele que o pulso viaja).
"""
import math
import re


def cubic(p0, p1, p2, p3, t):
    u = 1 - t
    return (
        u**3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t**3 * p3[0],
        u**3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t**3 * p3[1],
    )


def sample_path(d, step=1.0):
    """Amostra um path feito de M + C absolutos em pontos igualmente espaçados pelo comprimento."""
    nums = [float(n) for n in re.findall(r"-?\d+\.?\d*", d)]
    pts = [(nums[i], nums[i + 1]) for i in range(0, len(nums), 2)]
    start, rest = pts[0], pts[1:]
    dense = [start]
    cur = start
    for i in range(0, len(rest), 3):
        p1, p2, p3 = rest[i : i + 3]
        for k in range(1, 401):
            dense.append(cubic(cur, p1, p2, p3, k / 400))
        cur = p3
    # reamostra por comprimento de arco
    out, acc, target = [dense[0]], 0.0, step
    for a, b in zip(dense, dense[1:]):
        seg = math.dist(a, b)
        while acc + seg >= target:
            r = (target - acc) / seg
            out.append((a[0] + (b[0] - a[0]) * r, a[1] + (b[1] - a[1]) * r))
            target += step
        acc += seg
    return out, acc


def strands(d, amp, wavelength, step=1.0):
    pts, length = sample_path(d, step)
    n = len(pts)
    normals = []
    for i in range(n):
        a, b = pts[max(i - 1, 0)], pts[min(i + 1, n - 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]
        m = math.hypot(dx, dy) or 1
        normals.append((-dy / m, dx / m))

    def offset(fn):
        return [(p[0] + nrm[0] * fn(i * step), p[1] + nrm[1] * fn(i * step)) for i, (p, nrm) in enumerate(zip(pts, normals))]

    w = 2 * math.pi / wavelength
    a = offset(lambda s: amp * math.sin(w * s))
    b = offset(lambda s: -amp * math.sin(w * s))
    c = offset(lambda s: amp * math.cos(w * s))
    # cruzamentos de a e b: s = k * wavelength / 2; nos ímpares, b passa por cima
    overs = []
    half = wavelength / 2
    k = 1
    while k * half < length - 4:
        if k % 2 == 1:
            lo, hi = int((k * half - 6) / step), int((k * half + 6) / step)
            overs.append(b[max(lo, 0) : min(hi, n - 1) + 1])
        k += 1
    return a, b, c, overs, length


def smooth(points, every=6):
    """Path suave com poucos pontos: quadráticas passando pelos pontos médios."""
    p = points[::every]
    if p[-1] != points[-1]:
        p.append(points[-1])
    f = lambda v: f"{v:.1f}".rstrip("0").rstrip(".")
    d = f"M{f(p[0][0])} {f(p[0][1])}"
    for i in range(1, len(p) - 1):
        mx, my = (p[i][0] + p[i + 1][0]) / 2, (p[i][1] + p[i + 1][1]) / 2
        d += f"Q{f(p[i][0])} {f(p[i][1])} {f(mx)} {f(my)}"
    d += f"L{f(p[-1][0])} {f(p[-1][1])}"
    return d


def oklch_hex(L, C, h):
    a, b = C * math.cos(math.radians(h)), C * math.sin(math.radians(h))
    l_ = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m_ = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s_ = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    rgb = (
        4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_,
        -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_,
        -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_,
    )
    enc = lambda v: 12.92 * v if v <= 0.0031308 else 1.055 * v ** (1 / 2.4) - 0.055
    return "#" + "".join(f"{round(max(0, min(1, enc(v))) * 255):02x}" for v in rgb)


CORAL = oklch_hex(0.68, 0.16, 38)      # --color-accent
INK = oklch_hex(0.365, 0.045, 218)     # --color-ink
TEAL = oklch_hex(0.80, 0.055, 190)     # --color-teal-thread


def emit(path, view, d, amp, wavelength, with_c=True, width=3.5, second=None):
    a, b, c, overs, length = strands(d, amp, wavelength)
    w, h = view
    second = second or INK
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" fill="none" stroke-width="{width}" stroke-linejoin="round">']
    if with_c:
        parts.append(f'<path stroke="{TEAL}" d="{smooth(c)}"/>')
    parts.append(f'<path stroke="{second}" d="{smooth(b)}"/>')
    parts.append(f'<path stroke="{CORAL}" d="{smooth(a)}"/>')
    parts.append(f'<path stroke="{second}" d="{"".join(smooth(o, every=4) for o in overs)}"/>')
    parts.append("</svg>")
    out = OUT / path
    out.write_text("".join(parts), encoding="utf-8")
    print(path, f"{length:.0f}px de fio", out.stat().st_size, "bytes", CORAL, second, TEAL)


import sys
from pathlib import Path

OUT = Path(sys.argv[1]) / "assets" / "fio"
OUT.mkdir(parents=True, exist_ok=True)

# hero, >= 40rem: sai de baixo do cartão dela, atravessa e entra por cima do cartão de quem cuida
emit("hop-largo.svg", (330, 136), "M30 -8 C30 60 300 36 300 104 C300 116 300 128 300 144", amp=5, wavelength=44)
# hero, celular
emit("hop-estreito.svg", (260, 124), "M24 -8 C24 50 236 34 236 92 C236 104 236 116 236 132", amp=5, wavelength=44)
# coração do compromisso: dois fios entrelaçados (coral e teal claro), como no post 02
emit(
    "coracao.svg",
    (340, 250),
    "M2 206 C62 206 112 216 162 200 C217 164 264 124 252 78 C244 42 192 38 162 86 C132 38 80 42 72 78 C60 124 107 164 162 200 C202 230 266 216 338 216",
    amp=4.5,
    wavelength=104,
    with_c=False,
    width=4,
    second=TEAL,
)
