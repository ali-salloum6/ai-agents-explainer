"""
Thumbnail candidates for video 3 (AI agents, through the shop) — 1920×1080 stills built from the video's own
pictures (packaging rules: ../1-hour-challenge/docs/thumbnail_title_guide.md; what worked on video 2:
docs/youtube/publish_pack.md). One subject, dark ground, NO text on the image, nothing the video doesn't show,
the bottom-right corner (YouTube's duration badge) left empty.

  ThumbLoop     the loop as the picture: the page the AI writes (lines of text, the caret blinking at the end:
                hook.4's picture) on the left, the shop (the fridge, in the world's amber card) on the right, a
                request slip riding the top arrow and a result slip coming back underneath: it writes, the
                world answers, round it goes.
  ThumbRiddle   page-with-caret ? fridge: the title's riddle («ما بيعرف غير يكتب… كيف أدار محل؟») as a picture
  ThumbMaster   (control, not for upload) the finished master diagram: shows why a busier picture loses at ~160 px

Render (PNG of the last frame, 1920×1080), then scripts/make_thumbnails.py for the upload sizes:
  .venv/bin/manimgl our_scenes/thumbnail.py ThumbLoop -w -s --hd --video_dir ./media/thumbnails
"""
from __future__ import annotations

import hashlib
import sys
from pathlib import Path

from PIL import Image

_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from our_scenes.agent_kit import *  # noqa: F401,F403

WARM_CARD = "#1c1a17"          # the world's card fill (agent_kit.world_node)


def fat_beam(height: float, color=ACCENT) -> VMobject:
    """The text cursor, a little chunkier than kit.cursor so it survives the ~160 px shelf thumbnail (video 2's
    fat cursor did the same job)."""
    h = height
    stem, bar, wide = 0.11 * h, 0.095 * h, 0.46 * h
    pts = [(-wide / 2, h / 2), (wide / 2, h / 2), (wide / 2, h / 2 - bar), (stem / 2, h / 2 - bar),
           (stem / 2, bar - h / 2), (wide / 2, bar - h / 2), (wide / 2, -h / 2), (-wide / 2, -h / 2),
           (-wide / 2, bar - h / 2), (-stem / 2, bar - h / 2), (-stem / 2, h / 2 - bar), (-wide / 2, h / 2 - bar)]
    beam = Polygon(*[np.array([x, y, 0.0]) for x, y in pts])
    beam.round_corners(0.035 * h)
    beam.set_fill(color, opacity=1.0).set_stroke(width=0)
    return beam


def glow(width: float, height: float, center, color=ACCENT, strength: float = 0.30, power: float = 2.0) -> ImageMobject:
    """A soft elliptical glow (an RGBA raster): `strength` opacity at the centre, falling to 0 at the edge."""
    nx = 512
    ny = max(8, int(nx * height / width))
    yy, xx = np.mgrid[0:ny, 0:nx]
    r = np.sqrt(((xx - nx / 2) / (nx / 2)) ** 2 + ((yy - ny / 2) / (ny / 2)) ** 2)
    alpha = np.clip(1.0 - r, 0.0, 1.0) ** power * strength
    rgb = np.array(color_to_rgb(color)) * 255
    img = np.dstack([np.full((ny, nx), c) for c in rgb] + [alpha * 255]).astype(np.uint8)
    key = hashlib.md5(img.tobytes()).hexdigest()[:10]
    path = MEDIA_DIR / f"_glow_{key}.png"
    if not path.is_file():
        Image.fromarray(img, "RGBA").save(path)
    im = ImageMobject(str(path))
    im.set_width(width)
    return im.move_to(center)


def world_card(width: float, height: float, center, fridge_h: float) -> VGroup:
    """The world (amber): a card holding the fridge, as in the master diagram."""
    card = RoundedRectangle(width=width, height=height, corner_radius=0.5)
    card.set_fill(WARM_CARD, opacity=1.0).set_stroke(WARM, width=9)
    fr = fridge(fridge_h)
    out = VGroup(card, fr).move_to(center)
    fr.move_to(card.get_center() + 0.06 * UP)
    return out


def typed_page(width: float, height: float, center, caret_h: float = 1.5) -> VGroup:
    """The page the AI writes (hook.4's picture, bigger): lines of text, right to left, and the caret waiting at
    the end of the last one. Attributes: .caret"""
    panel = RoundedRectangle(width=width, height=height, corner_radius=0.45)
    panel.set_fill(CARD_FILL, opacity=1.0).set_stroke(ACCENT, width=7)
    inner = width - 1.0
    rows = VGroup()
    for frac in (0.94, 0.74, 0.36):
        rows.add(RoundedRectangle(width=inner * frac, height=0.40, corner_radius=0.20)
                 .set_fill(INK, opacity=0.92).set_stroke(width=0))
    rows.arrange(DOWN, buff=0.85, aligned_edge=RIGHT)
    rows.move_to(panel).align_to(panel.get_right() + 0.5 * LEFT, RIGHT)
    caret = fat_beam(caret_h)
    caret.next_to(rows[-1], LEFT, buff=0.26).match_y(rows[-1])
    out = VGroup(panel, rows, caret).move_to(center)
    out.caret = caret
    return out


def writer_with_cursor(center, scale: float = 1.75) -> VGroup:
    """The model's symbol from bit 1: the writer box with its cursor beside it."""
    w = writer_box().scale(scale)
    w.box.set_stroke(ACCENT, width=10)
    cur = fat_beam(1.35 * scale / 1.75 * 1.2)
    cur.next_to(w, RIGHT, buff=0.12).align_to(w, UP).shift(0.15 * UP)
    return VGroup(w, cur).move_to(center)


def tangent_tip(point, direction, size: float, color) -> Triangle:
    """An arrowhead at `point`, pointing along `direction`."""
    tip = Triangle().set_fill(color, opacity=1.0).set_stroke(width=0)
    tip.set_height(size)
    tip.rotate(np.arctan2(direction[1], direction[0]) - PI / 2)
    tip.move_to(point)
    return tip


def ring_arrow(center, radius: float, start_deg: float, sweep_deg: float, color, width: float = 26,
               tip: float = 0.78) -> VGroup:
    """An arc of the loop with an arrowhead at its end (a negative sweep goes clockwise)."""
    arc = Arc(start_angle=start_deg * DEGREES, angle=sweep_deg * DEGREES, radius=radius, arc_center=center)
    arc.set_stroke(color, width=width).set_fill(opacity=0)
    end = (start_deg + sweep_deg) * DEGREES
    sgn = 1.0 if sweep_deg > 0 else -1.0
    direction = sgn * np.array([-np.sin(end), np.cos(end), 0.0])
    point = center + radius * np.array([np.cos(end), np.sin(end), 0.0])
    return VGroup(arc, tangent_tip(point, direction, tip, color))


def the_loop(center, radius: float) -> tuple[VGroup, list]:
    """The loop: (arrows, slips): a request slip on the top arrow (writer -> world), a result slip on the bottom
    one (back). The slips must be added to the scene on their own, after the arrows (see agent_kit.flying)."""
    arrows = VGroup(ring_arrow(center, radius, 152, -124, ACCENT), ring_arrow(center, radius, -28, -124, WARM))
    req = flying(slip(kind="request", width=1.7, n_lines=2, seed=4).scale(1.5).move_to(center + radius * UP))
    res = flying(slip(kind="result", width=1.7, n_lines=2, seed=7).scale(1.5).move_to(center + radius * DOWN))
    for s in (req, res):
        s.card.set_fill("#0c1017", opacity=1.0).set_stroke(width=4)
    return arrows, [req, res]


class _Thumb(Scene):
    def setup(self):
        super().setup()
        self.camera.background_rgba = list(color_to_rgba(BG))


class ThumbLoop(_Thumb):
    def construct(self):
        page = typed_page(4.5, 4.5, np.array([-4.55, 0.1, 0.0]))
        card = world_card(4.4, 5.3, np.array([4.55, 0.1, 0.0]), 4.3)
        arrows, slips = the_loop(np.array([0.0, 0.1, 0.0]), 1.8)
        self.add(glow(8.5, 7.0, page.get_center(), ACCENT, 0.26), glow(7.6, 7.4, card.get_center(), WARM, 0.18))
        self.add(page, card, arrows)
        for s in slips:
            self.add(s)


class ThumbRiddle(_Thumb):
    def construct(self):
        page = typed_page(4.6, 4.6, np.array([-4.5, 0.1, 0.0]), caret_h=1.55)
        card = world_card(4.4, 5.3, np.array([4.55, 0.1, 0.0]), 4.3)
        q = Text("?", font="Helvetica Neue", weight=BOLD, font_size=300, fill_color=INK)
        q.set_height(3.7).move_to(np.array([0.0, 0.2, 0.0]))
        self.add(glow(8.5, 7.0, page.get_center(), ACCENT, 0.26), glow(7.6, 7.4, card.get_center(), WARM, 0.18))
        self.add(page, card, q)


class ThumbMaster(_Thumb):
    """Control: the finished master diagram, as big as it goes. Not for upload."""

    def construct(self):
        m = master(guide=True, desk_on=True)
        parts = VGroup(m.view, m.guide, m.writer, m.hands, m.world, m.to_hands, m.to_world, m.back, m.desk)
        parts.scale(1.18).move_to(ORIGIN)
        self.add(parts)
