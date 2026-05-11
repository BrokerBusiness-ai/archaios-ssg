"""
Generator OG image dla aidzisiaj.pl — neural network composition (1200×630).
Używa Pillow do narysowania spójnego z og-image.html design.
Output: domains/assets/aidzisiaj-pl/og-default.png

Uruchomienie:
    python generate_aidzisiaj_og.py
"""
from PIL import Image, ImageDraw, ImageFilter
import random
import math
from pathlib import Path

ROOT = Path(__file__).parent.parent
OUT_DIR = ROOT / "domains" / "assets" / "aidzisiaj-pl"
OUT_DIR.mkdir(parents=True, exist_ok=True)

W, H = 1200, 630
SEED = 7  # deterministic — ten sam wynik za każdym uruchomieniem

# Paleta dark cyber
BG_BASE = (10, 10, 10)
BG_AMBIENT_VIOLET = (167, 139, 250, 25)  # left ambient glow
BG_AMBIENT_CYAN = (0, 217, 255, 35)       # hub area glow
CYAN = (0, 217, 255)
MAGENTA = (255, 45, 146)
VIOLET = (167, 139, 250)
NODE_GLOW_FACTOR = 4

random.seed(SEED)

# Główny obraz + warstwa do rysowania glow (osobno żeby blur tylko na nią)
img = Image.new("RGB", (W, H), BG_BASE)
glow_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
draw_glow = ImageDraw.Draw(glow_layer)
draw = ImageDraw.Draw(img)

# ─── 1. Tło: subtelny radial gradient od (68%,42%) ─────────────────────
center_x, center_y = int(W * 0.68), int(H * 0.42)
max_r = int(math.sqrt(W**2 + H**2))
for r in range(max_r, 0, -8):
    t = r / max_r
    # ciemny granat #141426 -> głęboka czerń #070708
    rcol = int(20 - 16 * t)
    gcol = int(20 - 18 * t)
    bcol = int(38 - 30 * t)
    rcol, gcol, bcol = max(7, rcol), max(7, gcol), max(8, bcol)
    draw.ellipse([center_x - r, center_y - r, center_x + r, center_y + r],
                 fill=(rcol, gcol, bcol))

# ─── 2. Lewy ambient violet glow ─────────────────────────────────────
amb_x, amb_y = int(W * 0.20), int(H * 0.55)
for r in range(int(W * 0.5), 0, -4):
    alpha = max(0, int(15 * (1 - r / (W * 0.5))))
    draw_glow.ellipse([amb_x - r, amb_y - r, amb_x + r, amb_y + r],
                      fill=(167, 139, 250, alpha))

# ─── 3. Generowanie węzłów (Poisson-disk approximation) ──────────────
nodes = []  # list of (x, y, kind)
HUB_X, HUB_Y = int(W * 0.78), int(H * 0.42)

def try_place(x_min, x_max, y_min, y_max, target, min_dist):
    placed, attempts = 0, 0
    while placed < target and attempts < target * 60:
        attempts += 1
        x = random.randint(x_min, x_max)
        y = random.randint(y_min, y_max)
        ok = True
        for n in nodes:
            if (n[0] - x) ** 2 + (n[1] - y) ** 2 < min_dist ** 2:
                ok = False
                break
        if ok:
            nodes.append((x, y, "normal"))
            placed += 1

# Lewa gęsta strefa
try_place(40, int(W * 0.66), 30, H - 30, 34, 54)
# Prawa rzadka
try_place(int(W * 0.66), W - 40, 30, H - 30, 8, 84)

# Diagonalne nodes dla flow
for i in range(6):
    t = (i + random.random() * 0.6) / 6
    x = int(W * (0.15 + t * 0.7) + (random.random() - 0.5) * W * 0.05)
    y = int(H * (0.85 - t * 0.65) + (random.random() - 0.5) * H * 0.08)
    nodes.append((x, y, "normal"))

# Hub
nodes.append((HUB_X, HUB_Y, "hub"))

# Wybór 4 magenta pulse nodes
sectors = [(0.05, 0.40, 0.0, 0.5), (0.0, 0.35, 0.45, 1.0),
           (0.4, 0.65, 0.1, 0.55), (0.4, 0.7, 0.5, 0.95)]
for (xa, xb, ya, yb) in sectors:
    in_sec = [i for i, n in enumerate(nodes)
              if n[2] == "normal" and W*xa <= n[0] <= W*xb and H*ya <= n[1] <= H*yb]
    if in_sec:
        idx = random.choice(in_sec)
        x, y, _ = nodes[idx]
        nodes[idx] = (x, y, "pulse")

# ─── 4. Krawędzie: każdy węzeł łączy się z 2-4 najbliższymi ──────────
edges = []
seen = set()
for i, a in enumerate(nodes):
    dists = []
    for j, b in enumerate(nodes):
        if i == j:
            continue
        d = math.hypot(a[0] - b[0], a[1] - b[1])
        dists.append((j, d))
    dists.sort(key=lambda p: p[1])
    k = 7 if a[2] == "hub" else random.randint(2, 4)
    for n in range(min(k, len(dists))):
        j, d = dists[n]
        if d > W * 0.32 and a[2] != "hub" and nodes[j][2] != "hub":
            continue
        key = tuple(sorted([i, j]))
        if key in seen:
            continue
        seen.add(key)
        edges.append((i, j, d))

# ─── 5. Rysowanie krawędzi ────────────────────────────────────────────
for ai, bi, dist in edges:
    a = nodes[ai]; b = nodes[bi]
    is_hub = a[2] == "hub" or b[2] == "hub"
    color = CYAN if is_hub else VIOLET
    width = 2 if is_hub else 1
    alpha = int((0.55 if is_hub else 0.35 + max(0, 0.25 - dist / (W * 1.4))) * 255)
    line_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    line_draw = ImageDraw.Draw(line_layer)
    line_draw.line([a[0], a[1], b[0], b[1]], fill=color + (alpha,), width=width)
    glow_layer = Image.alpha_composite(glow_layer, line_layer)

# ─── 6. Węzły z glow ──────────────────────────────────────────────────
for x, y, kind in nodes:
    if kind == "hub":
        continue  # rysujemy hub na końcu
    draw_glow = ImageDraw.Draw(glow_layer)
    if kind == "pulse":
        # outer halo
        for r in (32, 18, 11, 7):
            alpha = {32: 30, 18: 60, 11: 110, 7: 200}[r]
            draw_glow.ellipse([x-r, y-r, x+r, y+r], fill=MAGENTA + (alpha,))
        draw_glow.ellipse([x-3, y-3, x+3, y+3], fill=(255, 214, 236, 255))
    else:
        r = 3
        for rr in (10, 6, r):
            alpha = {10: 60, 6: 130, 3: 255}[rr]
            draw_glow.ellipse([x-rr, y-rr, x+rr, y+rr], fill=CYAN + (alpha,))

# Hub (osobno, na wierzchu)
draw_glow = ImageDraw.Draw(glow_layer)
hub_r = 8
for rr, alpha, col in [
    (130, 30, CYAN),
    (60, 80, CYAN),
    (32, 130, CYAN),
    (18, 200, CYAN),
    (hub_r, 255, (191, 245, 255)),
]:
    draw_glow.ellipse([HUB_X-rr, HUB_Y-rr, HUB_X+rr, HUB_Y+rr], fill=col + (alpha,))
draw_glow.ellipse([HUB_X-3, HUB_Y-3, HUB_X+3, HUB_Y+3], fill=(255, 255, 255, 255))

# ─── 7. Złóż glow na bazowy obraz ────────────────────────────────────
img = img.convert("RGBA")
img = Image.alpha_composite(img, glow_layer)

# ─── 8. Subtelny grain ────────────────────────────────────────────────
grain = Image.effect_noise((W, H), 28).convert("RGBA")
grain.putalpha(40)
img = Image.alpha_composite(img, grain)

# ─── 9. Vignette ──────────────────────────────────────────────────────
vignette = Image.new("RGBA", (W, H), (0, 0, 0, 0))
vd = ImageDraw.Draw(vignette)
cx, cy = W // 2, H // 2
max_r = int(math.sqrt(cx**2 + cy**2))
for r in range(max_r, int(max_r * 0.6), -2):
    t = (r - max_r * 0.6) / (max_r * 0.4)
    a = int(140 * t * t)
    vd.ellipse([cx-r, cy-r, cx+r, cy+r], outline=(0, 0, 0, a), width=2)
img = Image.alpha_composite(img, vignette)

# ─── 10. Finalny zapis ────────────────────────────────────────────────
img = img.convert("RGB")
out_path = OUT_DIR / "og-default.png"
img.save(out_path, "PNG", optimize=True)

# Również webp dla newer browsers
out_webp = OUT_DIR / "og-default.webp"
img.save(out_webp, "WEBP", quality=88, method=6)

size_kb = out_path.stat().st_size // 1024
size_webp_kb = out_webp.stat().st_size // 1024
print(f"✓ {out_path.name} → {size_kb} KB ({W}×{H})")
print(f"✓ {out_webp.name} → {size_webp_kb} KB ({W}×{H})")
print(f"  Lokalizacja: {OUT_DIR}")
print(f"  Po rebuild + SFTP będą dostępne pod https://aidzisiaj.pl/img/og-default.png")
