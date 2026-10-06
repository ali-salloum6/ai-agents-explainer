#!/usr/bin/env python3
"""
Five simple thumbnail candidates for video 3, drawn as SVG and rendered with headless Chrome/Chromium
(no Manim needed). Same palette and cursor as the video (our_scenes/kit.py, agent_kit.py).

  c  shopkeeper   the shop fridge with the iPad as its face, wearing the tie from the hook
  d  writes       «بس بيكتب» (it only writes) with the writing cursor
  e  request      one big typed request, an envelope flying out
  f  ring         the agent loop as one glowing ring, the cursor in the middle
  g  cube         one metal cube with a falling price tag (the shop's first strange moment)

Output (docs/youtube/thumbnails/candidates/): thumb_<x>_<name>_1920x1080.png and _1280x720.png,
plus candidates_sheet.png (phone feed and stamp size, next to the current thumbnail and video 2's).

  python3 scripts/thumb_candidates.py                # everything
  python3 scripts/thumb_candidates.py --only c,e     # some candidates (the sheet is rebuilt too)
  CHROME_BIN=/path/to/chrome python3 scripts/thumb_candidates.py

Needs Chrome or Chromium on the machine (found automatically; macOS Chrome works) and Pillow or ffmpeg for the crop. The bottom-right corner
is kept empty on purpose: YouTube's duration badge sits there.
"""
from __future__ import annotations

import argparse
import glob
import math
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FONT = ROOT / "assets" / "fonts" / "Amiri-Regular.ttf"
OUT = ROOT / "docs" / "youtube" / "thumbnails" / "candidates"
CURRENT = ROOT / "docs" / "youtube" / "thumbnails" / "thumb_a_loop_1920x1080.png"
VIDEO2 = ROOT.parent / "ai-image-explainer" / "media" / "thumbnails" / "ThumbWritten.png"
TITLE = "كيف الـ AI Agent بيدير محل؟"

INK, INK2 = "#f2f1ec", "#c9ccd1"
TEAL, AMBER = "#3dd6c6", "#f0a35e"
CARD, STROKE = "#151a28", "#3a4256"
RED, TIE, YELLOW = "#e5484d", "#d64545", "#f2d06b"
FRIDGE_BODY, EDGE, GLASS = "#252c3b", "#8a93a6", "#101623"

DEFS = f"""
<filter id="glow" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="16" result="b"/>
  <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<radialGradient id="amberGlow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="{AMBER}" stop-opacity="0.30"/>
  <stop offset="1" stop-color="{AMBER}" stop-opacity="0"/></radialGradient>
<radialGradient id="tealGlow" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="{TEAL}" stop-opacity="0.26"/>
  <stop offset="1" stop-color="{TEAL}" stop-opacity="0"/></radialGradient>
"""

# one tiny layout helper: puts a cursor at the left end of right-to-left text and centres the pair
LAYOUT_JS = """
function layout(tid, cid, cx, cy, gap, curW, dy) {
  const t = document.getElementById(tid), c = document.getElementById(cid);
  t.removeAttribute('transform');
  const b = t.getBBox(), total = b.width + gap + curW, left = cx - total / 2;
  t.setAttribute('transform', 'translate(' + ((left + curW + gap) - b.x) + ',' + (cy - (b.y + b.height * 0.5) + dy) + ')');
  c.setAttribute('transform', 'translate(' + (left + curW / 2) + ',' + cy + ')');
  return [left, left + total];
}
"""


def cursor(h: float, color: str = TEAL, glow: bool = True, cid: str | None = None, at: tuple[float, float] = (0, 0)) -> str:
    sw, w = h * 0.085, h * 0.42
    f = ' filter="url(#glow)"' if glow else ""
    i = f' id="{cid}"' if cid else ""
    return (f'<g{i} transform="translate({at[0]},{at[1]})"{f}>'
            f'<rect x="{-sw / 2}" y="{-h / 2}" width="{sw}" height="{h}" rx="{sw / 2}" fill="{color}"/>'
            f'<rect x="{-w / 2}" y="{-h / 2}" width="{w}" height="{sw}" rx="{sw / 2}" fill="{color}"/>'
            f'<rect x="{-w / 2}" y="{h / 2 - sw}" width="{w}" height="{sw}" rx="{sw / 2}" fill="{color}"/></g>')


# ---------------------------------------------------------------------------------------------------------------
def cand_shopkeeper() -> tuple[str, str]:
    rows = [(TIE, TIE, TEAL, TEAL), (AMBER, AMBER, INK2, TIE), (TEAL, YELLOW, YELLOW, AMBER), (INK2, TIE, TEAL, AMBER)]
    shelves, items = [], []
    top, door_h = 462, 470
    for r, cols in enumerate(rows):
        y = top + (r + 1) * door_h / 4 - 8
        if r < 3:
            shelves.append(f'<line x1="722" x2="1198" y1="{y}" y2="{y}" stroke="{EDGE}" stroke-width="4" opacity="0.8"/>')
        for k, x in enumerate((736, 826, 1054, 1144)):
            items.append(f'<rect x="{x}" y="{y - 100}" width="62" height="92" rx="14" fill="{cols[k]}" opacity="0.92"/>')
    body = f"""
<ellipse cx="960" cy="610" rx="780" ry="520" fill="url(#amberGlow)"/>
<rect x="660" y="380" width="600" height="620" rx="44" fill="{FRIDGE_BODY}" stroke="{EDGE}" stroke-width="8"/>
<rect x="704" y="462" width="512" height="470" rx="24" fill="{GLASS}" stroke="{EDGE}" stroke-width="5"/>
{''.join(shelves)}{''.join(items)}
<rect x="672" y="520" width="16" height="170" rx="8" fill="{EDGE}"/>
<polygon points="900,380 1020,380 1052,424 868,424" fill="#3b4559" stroke="{EDGE}" stroke-width="5" stroke-linejoin="round"/>
<rect x="610" y="50" width="700" height="335" rx="46" fill="#1b2130" stroke="{INK2}" stroke-width="9"/>
<rect x="640" y="80" width="640" height="275" rx="30" fill="#0c1a1f"/>
<g filter="url(#glow)"><circle cx="850" cy="190" r="38" fill="{TEAL}"/><circle cx="1070" cy="190" r="38" fill="{TEAL}"/>
<path d="M 878 268 Q 960 326 1042 268" fill="none" stroke="{TEAL}" stroke-width="15" stroke-linecap="round"/></g>
<polygon points="916,404 1004,404 992,468 928,468" fill="{TIE}" stroke="#a83434" stroke-width="3" stroke-linejoin="round"/>
<polygon points="930,468 990,468 1044,786 960,858 876,786" fill="{TIE}" stroke="#a83434" stroke-width="3" stroke-linejoin="round"/>
<polygon points="960,468 990,468 1044,786 960,858" fill="#9d2f2f" opacity="0.55"/>
"""
    return "", body


def cand_writes() -> tuple[str, str]:
    body = f"""
<ellipse cx="960" cy="540" rx="900" ry="420" fill="url(#tealGlow)"/>
<g id="grp">
  <text id="t" x="0" y="0" font-family="Amiri" font-size="400" direction="rtl" text-anchor="start"
        stroke-linejoin="round" paint-order="stroke" stroke-width="10">
    <tspan fill="{INK}" stroke="{INK}">بس</tspan><tspan fill="{TEAL}" stroke="{TEAL}"> بيكتب</tspan></text>
  {cursor(430, cid="cur")}
</g>"""
    js = "document.fonts.load('400px Amiri').then(()=>layout('t','cur',960,540,70,150,40));"
    return js, body


def cand_request() -> tuple[str, str]:
    body = f"""
<ellipse cx="900" cy="560" rx="900" ry="420" fill="url(#tealGlow)"/>
<rect id="card" x="120" y="290" width="1480" height="500" rx="70" fill="{CARD}" stroke="{TEAL}" stroke-width="11"/>
<text id="t" x="0" y="0" font-family="Amiri" font-size="330" direction="rtl" fill="{INK}" stroke="{INK}"
      stroke-width="7" paint-order="stroke" stroke-linejoin="round">ابعت إيميل</text>
{cursor(400, cid="cur")}
<g id="env" transform="translate(1600,270) rotate(14)" filter="url(#glow)">
  <rect x="-170" y="-118" width="340" height="236" rx="30" fill="{CARD}" stroke="{AMBER}" stroke-width="12"/>
  <polyline points="-166,-100 0,24 166,-100" fill="none" stroke="{AMBER}" stroke-width="12" stroke-linejoin="round" stroke-linecap="round"/>
</g>
<g id="streaks" stroke="{AMBER}" stroke-width="14" stroke-linecap="round" opacity="0.85">
  <line x1="0" y1="0" x2="-80" y2="0"/><line x1="20" y1="72" x2="-90" y2="72"/></g>"""
    js = """document.fonts.load('330px Amiri').then(()=>{
  const cx=860, cy=540, pad=110;
  const [L,R]=layout('t','cur',cx,cy,70,150,60);
  const left=L-pad, right=R+pad, k=document.getElementById('card');
  k.setAttribute('x',left); k.setAttribute('width',right-left); k.setAttribute('y',cy-250); k.setAttribute('height',500);
  document.getElementById('env').setAttribute('transform','translate('+(right-30)+','+(cy-290)+') rotate(14)');
  document.getElementById('streaks').setAttribute('transform','translate('+(right-330)+','+(cy-345)+')');
});"""
    return js, body


def _pol(cx, cy, r, deg):
    a = math.radians(deg)
    return cx + r * math.cos(a), cy - r * math.sin(a)


def _ring_arc(cx, cy, r, a0, a1, color, sw):
    x0, y0 = _pol(cx, cy, r, a0)
    x1, y1 = _pol(cx, cy, r, a1)
    tip = _pol(cx, cy, r, a1 - 15)
    o, i = _pol(cx, cy, r + sw * 0.95, a1), _pol(cx, cy, r - sw * 0.95, a1)
    return (f'<path d="M {x0:.1f} {y0:.1f} A {r} {r} 0 0 1 {x1:.1f} {y1:.1f}" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round"/>'
            f'<polygon points="{o[0]:.1f},{o[1]:.1f} {tip[0]:.1f},{tip[1]:.1f} {i[0]:.1f},{i[1]:.1f}" fill="{color}" '
            f'stroke="{color}" stroke-width="8" stroke-linejoin="round"/>')


def cand_ring() -> tuple[str, str]:
    cx, cy, r, sw = 960, 540, 365, 74
    body = f"""
<ellipse cx="960" cy="540" rx="760" ry="520" fill="url(#tealGlow)"/>
<g filter="url(#glow)">{_ring_arc(cx, cy, r, 166, 32, TEAL, sw)}{_ring_arc(cx, cy, r, -14, -148, AMBER, sw)}</g>
{cursor(380, at=(cx, cy))}"""
    return "", body


def cand_cube() -> tuple[str, str]:
    cx, cy, a = 700, 540, 340
    k = 0.8660254
    T, UR, LR, B, LL, UL, C = ((cx, cy - a), (cx + k * a, cy - a / 2), (cx + k * a, cy + a / 2), (cx, cy + a),
                              (cx - k * a, cy + a / 2), (cx - k * a, cy - a / 2), (cx, cy))
    pts = lambda *p: " ".join(f"{x:.1f},{y:.1f}" for x, y in p)
    tag_c = (1330, 460)
    hole = (tag_c[0] - 110 * math.cos(math.radians(12)), tag_c[1] - 110 * math.sin(math.radians(12)))
    body = f"""
<defs>
 <linearGradient id="fTop" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f4f6fa"/><stop offset="1" stop-color="#aeb6c3"/></linearGradient>
 <linearGradient id="fLeft" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9aa3b4"/><stop offset="1" stop-color="#5d6678"/></linearGradient>
 <linearGradient id="fRight" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5a6479"/><stop offset="1" stop-color="#2b3242"/></linearGradient>
</defs>
<ellipse cx="900" cy="560" rx="840" ry="500" fill="url(#tealGlow)"/>
<ellipse cx="{cx}" cy="{cy + a + 40}" rx="330" ry="46" fill="#000" opacity="0.7"/>
<polygon points="{pts(UL, C, B, LL)}" fill="url(#fLeft)"/>
<polygon points="{pts(C, UR, LR, B)}" fill="url(#fRight)"/>
<polygon points="{pts(T, UR, C, UL)}" fill="url(#fTop)"/>
<polyline points="{pts(UL, C, UR)}" fill="none" stroke="#fff" stroke-width="5" opacity="0.55" stroke-linejoin="round"/>
<polyline points="{pts(C, B)}" fill="none" stroke="#fff" stroke-width="4" opacity="0.28"/>
<polygon points="{pts(T, UR, LR, B, LL, UL)}" fill="none" stroke="#d8dde6" stroke-width="5" stroke-linejoin="round" opacity="0.7"/>
<path d="M {UR[0]:.1f} {UR[1]:.1f} Q {(UR[0] + hole[0]) / 2 + 10:.1f} {UR[1] + 110:.1f} {hole[0]:.1f} {hole[1]:.1f}" fill="none" stroke="{INK2}" stroke-width="6"/>
<g transform="translate({tag_c[0]},{tag_c[1]}) rotate(12)" filter="url(#glow)">
  <path d="M -150 -100 H 100 L 190 0 L 100 100 H -150 Q -172 100 -172 78 V -78 Q -172 -100 -150 -100 Z" fill="{INK}"/>
  <circle cx="-110" cy="0" r="20" fill="#000"/>
  <rect x="-10" y="-70" width="40" height="80" fill="{RED}"/>
  <polygon points="-62,0 82,0 10,76" fill="{RED}" stroke="{RED}" stroke-width="10" stroke-linejoin="round"/>
</g>"""
    return "", body


CANDIDATES = {
    "c": ("shopkeeper", cand_shopkeeper),
    "d": ("writes", cand_writes),
    "e": ("request", cand_request),
    "f": ("ring", cand_ring),
    "g": ("cube", cand_cube),
}


# ---------------------------------------------------------------------------------------------------------------
def page(js: str, body: str, w: int, h: int) -> str:
    return f"""<!doctype html><meta charset="utf-8">
<style>@font-face{{font-family:Amiri;src:url("file://{FONT}")}}
html,body{{margin:0;background:#000;overflow:hidden}}svg{{display:block}}</style>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="{w}" height="{h}"><defs>{DEFS}</defs>
<rect width="1920" height="1080" fill="#000"/>{body}</svg>
<script>{LAYOUT_JS}{js}</script>"""


def find_chrome() -> str:
    env = os.environ.get("CHROME_BIN")
    cands = [env] if env else []
    cands += sorted(glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome"))
    cands += ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
              "/Applications/Chromium.app/Contents/MacOS/Chromium"]
    cands += [shutil.which(n) for n in ("google-chrome", "chromium", "chromium-browser", "chrome")]
    for c in cands:
        if c and Path(c).exists():
            return c
    sys.exit("No Chrome/Chromium found. Set CHROME_BIN=/path/to/chrome.")


EXTRA = 160   # headless Chrome's viewport is shorter than --window-size; ask for more, then crop to w x h


def crop(raw: Path, png: Path, w: int, h: int) -> None:
    try:
        from PIL import Image
        Image.open(raw).crop((0, 0, w, h)).save(png)
    except ImportError:
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(raw), "-vf", f"crop={w}:{h}:0:0", str(png)],
                       check=True)


def shoot(chrome: str, html_text: str, png: Path, w: int, h: int, tmp: Path) -> None:
    f = tmp / (png.stem + ".html")
    f.write_text(html_text, encoding="utf-8")
    raw = tmp / (png.stem + ".raw.png")
    cmd = [chrome, "--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
           f"--window-size={w},{h + EXTRA}", "--virtual-time-budget=5000", "--allow-file-access-from-files",
           f"--screenshot={raw}", f"file://{f}"]
    subprocess.run(cmd, check=True, capture_output=True, timeout=90)
    crop(raw, png, w, h)


def sheet_html(items: list[tuple[str, Path]]) -> str:
    card = lambda lab, p: (f'<div class="c"><div class="t"><img src="file://{p}"><b>5:54</b></div>'
                           f'<div class="ti">{TITLE}</div><div class="m">Ali Salloum · 3 hours ago</div>'
                           f'<div class="l">{lab}</div></div>')
    stamp = lambda lab, p: f'<div class="s"><img src="file://{p}"><div class="l">{lab}</div></div>'
    return f"""<!doctype html><meta charset="utf-8"><style>
@font-face{{font-family:Amiri;src:url("file://{FONT}")}}
body{{margin:0;padding:28px 30px;background:#0f0f0f;color:#eee;font:15px/1.3 Arial,Helvetica,sans-serif;width:1700px}}
h2{{font:600 15px Arial;color:#aaa;margin:6px 0 14px;letter-spacing:.04em}}
.g{{display:flex;flex-wrap:wrap;gap:26px}}.c{{width:390px}}
.t{{position:relative;width:390px;height:219px;border-radius:12px;overflow:hidden;background:#000}}.t img{{width:100%;height:100%;display:block}}
.t b{{position:absolute;right:8px;bottom:8px;background:rgba(0,0,0,.8);padding:2px 5px;border-radius:4px;font-size:12px}}
.ti{{direction:rtl;text-align:right;font:500 16px Amiri,Arial;margin-top:10px;font-size:19px}}.m{{color:#aaa;font-size:13px;margin-top:4px}}
.l{{color:#3dd6c6;font-weight:700;margin-top:6px}}.s{{width:160px}}.s img{{width:160px;height:90px;display:block;border-radius:6px}}.sp{{height:28px}}
</style><h2>PHONE FEED (390 px)</h2><div class="g">{''.join(card(l, p) for l, p in items)}</div><div class="sp"></div>
<h2>STAMP SIZE (160 × 90)</h2><div class="g">{''.join(stamp(l, p) for l, p in items)}</div>"""


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", default="", help="comma-separated letters, e.g. c,e")
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--no-sheet", action="store_true")
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    chrome = find_chrome()
    letters = [x for x in a.only.split(",") if x] or list(CANDIDATES)
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        for k in letters:
            name, fn = CANDIDATES[k]
            js, body = fn()
            for w, h in ((1920, 1080), (1280, 720)):
                png = out / f"thumb_{k}_{name}_{w}x{h}.png"
                shoot(chrome, page(js, body, w, h), png, w, h, tmp)
                print("wrote", png.relative_to(ROOT))
        if not a.no_sheet:
            items = [(f"{k}: {CANDIDATES[k][0]}", out / f"thumb_{k}_{CANDIDATES[k][0]}_1920x1080.png") for k in CANDIDATES
                     if (out / f"thumb_{k}_{CANDIDATES[k][0]}_1920x1080.png").exists()]
            if CURRENT.exists():
                items.append(("current: loop (a)", CURRENT))
            if VIDEO2.exists():
                items.append(("video 2 (reference)", VIDEO2))
            shoot(chrome, sheet_html(items), out / "candidates_sheet.png", 1760, 1000, tmp)
            print("wrote", (out / "candidates_sheet.png").relative_to(ROOT))


if __name__ == "__main__":
    main()
