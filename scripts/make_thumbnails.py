#!/usr/bin/env python3
"""
Video 3's thumbnails: export the upload files and build the packaging test sheet.

  python3 scripts/make_thumbnails.py          # after rendering our_scenes/thumbnail.py (see its docstring)

in:   media/thumbnails/Thumb*.png                       1920×1080 Manim stills (our_scenes/thumbnail.py)
out:  docs/youtube/thumbnails/<name>_1920x1080.png      the full-size still
      docs/youtube/thumbnails/<name>_1280x720.png       the upload file (>= 1280×720 for every variant, or YouTube
                                                        downscales a whole A/B test to 480p; under 2 MB for mobile upload)
      docs/youtube/thumbnails/packaging_test.png        the pairs as a viewer meets them: phone feed card, suggested
                                                        sidebar, and 160 px stamp size next to the control and video 2

The test sheet draws the title under each thumbnail with a real Arabic shaper (Pillow + Raqm), the duration badge
where YouTube puts it (bottom right), and the channel's own video 2 as a neighbour.
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "media" / "thumbnails"
OUT = ROOT / "docs" / "youtube" / "thumbnails"
VIDEO2 = ROOT.parent / "ai-image-explainer" / "media" / "thumbnails" / "ThumbWritten.png"

# name in media/thumbnails -> (file stem, title shown beside it in the test sheet)
PAIRS = {
    "ThumbLoop": ("thumb_a_loop", "كيف الـ AI Agent بيدير محل؟"),
    "ThumbRiddle": ("thumb_b_riddle", "الـ AI Agent ما بيعرف غير يكتب… كيف أدار محل؟"),
}
CONTROL = ("ThumbMaster", "the finished master diagram (control)")
VIDEO2_TITLE = "كيف الذكاء الاصطناعي بيرسم الصور؟"
CHANNEL = "Ali Salloum - علي سلوم"

BG, INK, INK2 = (15, 15, 15), (241, 241, 241), (170, 170, 170)
AR = LAT = "/System/Library/Fonts/Supplemental/Arial.ttf"      # both scripts, so "AI Agent" inside an Arabic title shapes


def font(path: str, size: int, index: int = 0) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size, index=index, layout_engine=ImageFont.Layout.RAQM)


def wrap_rtl(draw: ImageDraw.ImageDraw, text: str, fnt, width: int, max_lines: int = 2) -> list[str]:
    """Greedy word wrap in reading order (the first line holds the first words); the last line gets an ellipsis
    if the title doesn't fit, as YouTube does."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt, direction="rtl") <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    lines.append(cur)
    if len(lines) > max_lines:
        lines = lines[:max_lines]
        lines[-1] = lines[-1].rstrip() + "…"
    return lines


def rounded(im: Image.Image, r: int) -> Image.Image:
    mask = Image.new("L", im.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, im.width - 1, im.height - 1), r, fill=255)
    out = im.convert("RGBA")
    out.putalpha(mask)
    return out


def badge(canvas: Image.Image, box: tuple[int, int, int, int], scale: float = 1.0) -> None:
    """The duration badge, bottom right of a thumbnail box (x0, y0, x1, y1)."""
    d = ImageDraw.Draw(canvas)
    f = font(LAT, int(13 * scale))
    w, h = int(38 * scale), int(20 * scale)
    x1, y1 = box[2] - int(6 * scale), box[3] - int(6 * scale)
    d.rounded_rectangle((x1 - w, y1 - h, x1, y1), int(4 * scale), fill=(0, 0, 0))
    d.text((x1 - w / 2, y1 - h / 2), "5:54", font=f, fill=(255, 255, 255), anchor="mm")


def card(canvas: Image.Image, xy: tuple[int, int], thumb: Image.Image, title: str, width: int) -> int:
    """A phone-feed card: full-width thumbnail, avatar, two-line title, channel and stats. Returns its height."""
    x, y = xy
    h = int(width * 9 / 16)
    t = rounded(thumb.resize((width, h), Image.LANCZOS), 12)
    canvas.paste(t, (x, y), t)
    badge(canvas, (x, y, x + width, y + h))
    d = ImageDraw.Draw(canvas)
    ty = y + h + 12
    d.ellipse((x, ty, x + 36, ty + 36), fill=(0, 142, 128))
    d.text((x + 18, ty + 18), "A", font=font(LAT, 18), fill=(255, 255, 255), anchor="mm")
    f = font(AR, 17, 0)
    left, right = x + 48, x + width
    for i, line in enumerate(wrap_rtl(d, title, f, right - left)):
        d.text((right, ty + i * 24), line, font=f, fill=INK, anchor="ra", direction="rtl")
    meta = font(LAT, 13)
    d.text((left, ty + 52), f"{CHANNEL} · 1.2K views · 3 hours ago", font=meta, fill=INK2)
    return h + 12 + 72


def side(canvas: Image.Image, xy: tuple[int, int], thumb: Image.Image, title: str) -> None:
    """A suggested-sidebar row: 168×94 thumbnail, title at its right (2 lines)."""
    x, y = xy
    t = rounded(thumb.resize((168, 94), Image.LANCZOS), 8)
    canvas.paste(t, (x, y), t)
    badge(canvas, (x, y, x + 168, y + 94), 0.8)
    d = ImageDraw.Draw(canvas)
    f = font(AR, 14, 0)
    for i, line in enumerate(wrap_rtl(d, title, f, 200)):
        d.text((x + 168 + 214, y + 2 + i * 20), line, font=f, fill=INK, anchor="ra", direction="rtl")
    d.text((x + 168 + 12, y + 50), "Ali Salloum", font=font(LAT, 12), fill=INK2)
    d.text((x + 168 + 12, y + 66), "1.2K views · 3 hours ago", font=font(LAT, 12), fill=INK2)


def export(names: dict[str, tuple[str, str]]) -> dict[str, Image.Image]:
    OUT.mkdir(parents=True, exist_ok=True)
    full = {}
    for name, (stem, _) in names.items():
        src = Image.open(SRC / f"{name}.png").convert("RGB")
        assert src.size == (1920, 1080), f"{name}: expected 1920×1080, got {src.size}"
        src.save(OUT / f"{stem}_1920x1080.png", optimize=True)
        small = src.resize((1280, 720), Image.LANCZOS)
        small.save(OUT / f"{stem}_1280x720.png", optimize=True)
        for suffix in ("1920x1080", "1280x720"):
            kb = (OUT / f"{stem}_{suffix}.png").stat().st_size / 1024
            print(f"{stem}_{suffix}.png  {kb:6.0f} KB" + ("   OVER 2 MB (mobile upload)" if kb > 2048 else ""))
        full[name] = src
    return full


def sheet(thumbs: dict[str, Image.Image]) -> None:
    pairs = [(thumbs[n], t) for n, (_, t) in PAIRS.items()]
    control = Image.open(SRC / f"{CONTROL[0]}.png").convert("RGB") if (SRC / f"{CONTROL[0]}.png").is_file() else None
    v2 = Image.open(VIDEO2).convert("RGB") if VIDEO2.is_file() else None
    W = 1560
    canvas = Image.new("RGB", (W, 1060), BG)
    d = ImageDraw.Draw(canvas)
    label = font(LAT, 15)
    # 1. phone feed
    d.text((30, 18), "PHONE FEED (390 px)", font=label, fill=INK2)
    x = 30
    for im, title in pairs:
        card(canvas, (x, 44), im, title, 390)
        x += 420
    if v2:
        card(canvas, (x, 44), v2, VIDEO2_TITLE, 390)
    # 2. suggested sidebar
    d.text((30, 386), "SUGGESTED SIDEBAR (168×94)", font=label, fill=INK2)
    y = 414
    rows = pairs + ([(v2, VIDEO2_TITLE)] if v2 else [])
    for i, (im, title) in enumerate(rows):
        side(canvas, (30 + (i % 2) * 560, y + (i // 2) * 112), im, title)
    # 3. stamp size: as shown, then enlarged
    d.text((30, 660), "STAMP SIZE (160×90 as shown; below it enlarged)", font=label, fill=INK2)
    strip = [(im, n) for (im, _), n in zip(pairs, ("A: loop", "B: riddle"))]
    if control:
        strip.append((control, "control: the master diagram"))
    if v2:
        strip.append((v2, "video 2"))
    for i, (im, name) in enumerate(strip):
        x = 30 + i * 175
        canvas.paste(im.resize((160, 90), Image.LANCZOS), (x, 690))
        d.text((x, 786), name, font=font(LAT, 12), fill=INK2)
        big = im.resize((160, 90), Image.LANCZOS).resize((360, 202), Image.LANCZOS)
        canvas.paste(big, (30 + i * 380, 830))
    canvas = canvas.crop((0, 0, W, 1050))
    canvas.save(OUT / "packaging_test.png", optimize=True)
    print("packaging_test.png")


def main() -> None:
    thumbs = export(PAIRS)
    sheet(thumbs)


if __name__ == "__main__":
    main()
