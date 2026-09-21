"""Recompõe o pin oficial (coração creme) por cima do pin gerado por IA.

Uso: python recompor_pin.py <imagem_gerada.png> <saida.png> <x0> <y0> <x1> <y1>
(x0,y0,x1,y1) = janela de busca, em pixels da imagem gerada, em volta do pin de IA.
"""
import math
import sys
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFilter

PIN = Path(r"D:/EstudosProgramacao/TiaMedica/BrandBrain/logo/tia-pin-coracao-creme-1024.png")
src, out = Path(sys.argv[1]), Path(sys.argv[2])
x0, y0, x1, y1 = map(int, sys.argv[3:7])

img = Image.open(src).convert("RGB")
win = img.crop((x0, y0, x1, y1))

# 1. máscara do pin de IA: pixels creme dentro da janela
px = win.load()
mask = Image.new("L", win.size, 0)
mp = mask.load()
for y in range(win.height):
    for x in range(win.width):
        r, g, b = px[x, y]
        if r > 232 and g > 222 and b > 200 and (r - b) < 45:
            mp[x, y] = 255
mask = mask.filter(ImageFilter.MedianFilter(5))
# só a mancha que contém o centro da janela (o filete creme da gola fica de fora)
seed = (win.width // 2, win.height // 2)
assert mask.getpixel(seed) == 255, "o centro da janela precisa cair dentro do pin"
ImageDraw.floodfill(mask, seed, 200)
mask = mask.point(lambda v: 255 if v == 200 else 0)
mp = mask.load()
bbox = mask.getbbox()
assert bbox, "pin não encontrado na janela"
bx0, by0, bx1, by1 = bbox
pts = [(x, y) for y in range(by0, by1) for x in range(bx0, bx1) if mp[x, y]]
cx = sum(p[0] for p in pts) / len(pts)
cy = sum(p[1] for p in pts) / len(pts)
# ponta do coração = ponto da máscara mais distante do centróide na metade de baixo
tip = max((p for p in pts if p[1] > cy), key=lambda p: (p[0] - cx) ** 2 + (p[1] - cy) ** 2)
angle = math.degrees(math.atan2(tip[0] - cx, tip[1] - cy))  # 0 = ponta exatamente para baixo
w, h = bx1 - bx0, by1 - by0
print(f"pin de IA: bbox={bbox} centro=({cx:.0f},{cy:.0f}) ponta={tip} inclinação={angle:.1f}° tamanho={w}x{h}")

# 2. pin oficial: o PNG já tem transparência; só descarta a coluna espúria da borda direita
pin = Image.open(PIN).convert("RGBA")
alpha = pin.split()[3]
ImageDraw.Draw(alpha).rectangle((1000, 0, pin.width, pin.height), fill=0)
pin.putalpha(alpha)
pin = pin.crop(alpha.getbbox())

# 3. escala para cobrir o pin antigo com folga, gira e cola com uma sombra leve em tinta
scale = max(w / pin.width, h / pin.height) * 1.13
pin = pin.resize((round(pin.width * scale), round(pin.height * scale)), Image.LANCZOS)
pin = pin.rotate(angle, resample=Image.BICUBIC, expand=True)  # PIL gira no sentido anti-horário; ponta para a esquerda = horário
pin = pin.filter(ImageFilter.GaussianBlur(0.5))
# alinha centróide com centróide (o centro da caixa engana num coração inclinado)
pa = pin.split()[3].load()
tot = sx = sy = 0
for yy in range(0, pin.height, 2):
    for xx in range(0, pin.width, 2):
        v = pa[xx, yy]
        if v:
            tot += v; sx += v * xx; sy += v * yy
pos = (round(x0 + cx - sx / tot), round(y0 + cy - sy / tot))

shadow = Image.new("RGBA", pin.size, (32, 68, 78, 0))
shadow.putalpha(pin.split()[3].point(lambda v: int(v * 0.22)))
shadow = shadow.filter(ImageFilter.GaussianBlur(3))
canvas = img.convert("RGBA")
canvas.alpha_composite(shadow, (pos[0] + 2, pos[1] + 3))
canvas.alpha_composite(pin, pos)
canvas.convert("RGB").save(out, "PNG")
print("salvo:", out, "posição", pos, "tamanho do pin", pin.size)
