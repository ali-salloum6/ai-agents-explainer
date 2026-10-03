"""
Bit6Fixes — round two: newer models, and a few small changes around them.

Starts on bit 5's last frame (the master diagram lit: writer, hands, world, tools guide, the desk with
the writer's view cone, the loop lane, five slips on the desk) and adds one part per line:
  1 the shop dims for a moment and reopens under a «المحاولة التانية» marker; a sheen runs across the
    writer (newer models); sparkles where the changes are about to go (around it)
  2 the shop's price menu, large: the cost bars grow into its dashed slots, the cube's red bar longer
    than its price; then it parks above the world
  3 the two oldest slips slide off, the checklist pins on the desk's left end; a tick on each item's word
  4 the marker moves to the corner; a smaller writer above the hands, «المدير»; a request goes up to it,
    gets a tick, goes down into the hands (twice, the second faster)
  5 the diagram dims: discounts shrink to about a fifth, free items to half (dashed outlines keep the old
    height); weekly bars, red below the line, flip to mostly small bars at or above it (+2 s hold)
  6 night over everything but the two writers; slips fly between them faster and faster; their text
    swells into ETERNAL TRANSCENDENCE; no envelope goes to the world, which stays dark
  7 the two writers glow in turn; a dashed line goes out from the hands to the dark world, nothing comes back
  8 the night lifts; the checklist glows and its ticks pulse; hold on it
End frame: the master diagram + the checklist on the desk + the boss above the hands + the price menu with
its cost column above the world (the marker is gone).

Render (preview): .venv/bin/manimgl our_scenes/bit6_fixes.py Bit6Fixes -w -l --video_dir ./media
"""
from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from our_scenes.agent_kit import *  # noqa: F401,F403

# Draw order in this bit (agent_kit.behind / flying explain why it matters): the checklist stands over
# the desk's edge, the veils (dimming, night) cover the whole diagram, what stays lit sits above them.
Z_CHECK, Z_VEIL, Z_LIT, Z_LIT_FLY, Z_WORDS = 1, 5, 6, 7, 8

MARKER_C = np.array([0.15, 2.92, 0])          # «المحاولة التانية», top centre (lines 1–3)
MARKER_PARK = np.array([-4.85, 2.95, 0])      # ...then smaller in the top-left corner (lines 4–7)
MENU_BIG_C, MENU_BIG_H = np.array([3.10, 0.55, 0]), 3.4      # the price menu while line 2 reads it (covers hands + world)
MENU_PARK_C, MENU_PARK_H = np.array([4.60, 2.615, 0]), 1.33  # parked above the world
CHECK_SCALE = 1.15
CHECK_DL = np.array([DESK_X0 + 0.05, DESK_Y + 0.08, 0])      # the checklist stands on the desk's left end
SLIP_NUDGE = 0.35                                            # the slips left on the desk make a little room
BOSS_C, BOSS_SCALE = np.array([1.30, 2.30, 0]), 0.6          # the boss: a smaller writer above the hands
REQ_FROM = np.array([-0.75, 1.45, 0])                        # a request leaves the writer here...
BOSS_READ = np.array([1.30, 1.50, 0])                        # ...and is read here, under the boss
TALK_A, TALK_B = np.array([-0.95, 1.62, 0]), np.array([0.05, 2.32, 0])   # night slips: writer <-> boss
WORDS_C, WORDS_W = np.array([-0.4, -0.6, 0]), 7.6            # ETERNAL TRANSCENDENCE, across the middle
CHART_L_C, CHART_R_C = np.array([-3.15, 0.30, 0]), np.array([2.60, 0.30, 0])


# ----------------------------------------------------------------------------
# Pieces for this bit
# ----------------------------------------------------------------------------
def _veil(color=BG) -> Rectangle:
    """A full-frame sheet that dims everything under it (starts clear)."""
    v = Rectangle(width=FRAME_WIDTH + 1.0, height=FRAME_HEIGHT + 1.0)
    v.set_fill(color, opacity=0.0).set_stroke(width=0)
    return v.set_z_index(Z_VEIL)


def _marker() -> VGroup:
    """«المحاولة التانية» in a WARM-outlined chip. Attributes: .box, .text"""
    text = ar_text(ROUND_TWO_AR, font_size=36, color=WARM)
    box = RoundedRectangle(width=text.get_width() + 0.7, height=text.get_height() + 0.34, corner_radius=0.2)
    box.set_fill(CARD_FILL, opacity=1.0).set_stroke(WARM, width=2.4)
    text.move_to(box)
    out = VGroup(box, text)
    out.box, out.text = box, text
    return out


def _sparkle(size: float = 0.5, color=WARM) -> VMobject:
    """A four-pointed twinkle."""
    pts = [np.array([np.cos(a), np.sin(a), 0.0]) * (0.5 if k % 2 == 0 else 0.13) * size
           for k, a in enumerate(PI / 2 + np.arange(8) * PI / 4)]
    return Polygon(*pts).set_fill(color, opacity=1.0).set_stroke(width=0)


def _twinkle(sp: VMobject, run_time: float = 0.8, turn: float = PI / 2) -> Animation:
    """Grow from nothing, turn a little, shrink back to nothing."""
    base, c = sp.copy(), sp.get_center()

    def upd(m, a):
        m.become(base.copy().scale(max(np.sin(PI * a), 1e-3)).rotate(turn * a).move_to(c))
    return UpdateFromAlphaFunc(sp, upd, run_time=run_time, rate_func=linear)


def _sheen(box: VMobject, run_time: float = 0.8, color=INK, opacity: float = 0.4) -> Animation:
    """A slanted band of light sweeping across a box from left to right, clipped to the box."""
    shape = box.copy().set_stroke(width=0)
    yb, yt = box.get_bottom()[1] - 0.05, box.get_top()[1] + 0.05
    half, slant = 0.22, 0.3
    x0, x1 = box.get_left()[0] - half - slant, box.get_right()[0] + half + slant
    band_mob = VMobject().set_fill(color, opacity).set_stroke(width=0)

    def upd(m, a):
        x = interpolate(x0, x1, a)
        band = Polygon(np.array([x - half - slant, yb, 0]), np.array([x + half - slant, yb, 0]),
                       np.array([x + half + slant, yt, 0]), np.array([x - half + slant, yt, 0]))
        cut = Intersection(shape, band)
        if cut.get_num_points() > 0:
            m.set_points(cut.get_points())
        else:
            m.clear_points()
        m.set_fill(color, opacity).set_stroke(width=0)
    return UpdateFromAlphaFunc(band_mob, upd, run_time=run_time, rate_func=smooth)


def _halo(shape: VMobject, color, k: float = 1.0) -> VGroup:
    """A soft glow around a box: copies of its outline with wide, faint strokes (starts invisible)."""
    g = VGroup()
    for wd, op in ((28, 0.13), (16, 0.26), (6, 0.7)):
        h = shape.copy().set_fill(opacity=0).set_stroke(color, width=wd * k, opacity=0)
        h.peak = op
        g.add(h)
    return g


def _halo_to(halo: VGroup, level_from: float, level_to: float, run_time: float, rate_func=smooth) -> Animation:
    """Fade a halo between two brightness levels (0 = off, 1 = full)."""
    def upd(m, a):
        lv = interpolate(level_from, level_to, a)
        for h in m:
            h.set_stroke(opacity=h.peak * lv)
    return UpdateFromAlphaFunc(halo, upd, run_time=run_time, rate_func=rate_func)


def _talk_slip(scale: float = 1.0, words: float = 0.7) -> VGroup:
    """A night slip: teal-edged card whose line is the words they kept writing (tiny, WARM).
    Attributes: .card, .edge, .text"""
    w, h = 1.25, 0.46
    card = RoundedRectangle(width=w, height=h, corner_radius=0.08)
    card.set_fill(CARD_FILL, opacity=1.0).set_stroke(ACCENT, width=2.0)
    edge = RoundedRectangle(width=0.07, height=h - 0.10, corner_radius=0.035).set_fill(ACCENT, 0.95).set_stroke(width=0)
    edge.move_to(card.get_right() + 0.075 * LEFT)
    text = en_text(TRANSCEND_EN, font_size=32, color=WARM)
    text.set_width(words * (w - 0.3))
    text.move_to(card.get_center() + 0.05 * LEFT)
    out = VGroup(card, edge, text)
    out.card, out.edge, out.text = card, edge, text
    return out.scale(scale)


def _dashed_outline(width: float, height: float, color, opacity: float = 0.8, dash: float = 0.11) -> VGroup:
    """A rectangle drawn as four dashed sides (evenly dashed whatever the aspect ratio)."""
    c = [np.array([-width / 2, -height / 2, 0]), np.array([width / 2, -height / 2, 0]),
         np.array([width / 2, height / 2, 0]), np.array([-width / 2, height / 2, 0])]
    sides = VGroup(*[DashedLine(c[i], c[(i + 1) % 4], dash_length=dash, positive_space_ratio=0.55) for i in range(4)])
    return sides.set_stroke(color, width=2.2, opacity=opacity)


def _col(width: float, height: float, color, r: float = 0.1) -> RoundedRectangle:
    """A chart column (square-ish corners so it keeps its shape as it shrinks)."""
    c = RoundedRectangle(width=width, height=max(height, 0.02), corner_radius=min(r, height / 2, width / 2))
    return c.set_fill(color, opacity=1.0).set_stroke(width=0)


def _panel(width: float, height: float, center) -> RoundedRectangle:
    p = RoundedRectangle(width=width, height=height, corner_radius=0.22)
    return p.set_fill(CARD_FILL, opacity=1.0).set_stroke(CARD_STROKE, width=2.0).move_to(center)


DISC_SHARE, GIFT_SHARE = 0.2, 0.5          # about a fifth, half (bars only, never numbers)
WEEKS_BEFORE = [-0.95, -0.70, -1.20, -0.85, -0.60, -1.05, -0.90, -0.75]
WEEKS_AFTER = [0.22, -0.14, 0.30, 0.05, 0.26, -0.10, 0.34, 0.18]   # mostly at or above the line


def _two_bars() -> VGroup:
    """Discounts (right, read first) and free items (left), as two thick columns over their icons.
    Attributes: .panel, .base, .disc, .gift, .disc_ghost, .gift_ghost, .icons, .h, .w"""
    panel = _panel(3.7, 4.2, CHART_L_C)
    base_y = panel.get_bottom()[1] + 1.05
    bw, bh = 0.92, 2.5
    x_gift, x_disc = panel.get_x() - 0.72, panel.get_x() + 0.72
    base = Line(np.array([panel.get_left()[0] + 0.35, base_y, 0]), np.array([panel.get_right()[0] - 0.35, base_y, 0]))
    base.set_stroke(INK_2, width=2.5)
    disc = _col(bw, bh, WARM).move_to(np.array([x_disc, base_y, 0]), aligned_edge=DOWN)
    gift = _col(bw, bh, ACCENT).move_to(np.array([x_gift, base_y, 0]), aligned_edge=DOWN)
    disc_ghost = _dashed_outline(bw, bh, WARM).move_to(disc)
    gift_ghost = _dashed_outline(bw, bh, ACCENT).move_to(gift)
    icons = VGroup(icon_percent(0.66).move_to(np.array([x_disc, base_y - 0.52, 0])),
                   icon_gift(0.66).move_to(np.array([x_gift, base_y - 0.5, 0])))
    out = VGroup(panel, base, gift, disc, icons)
    out.panel, out.base, out.disc, out.gift, out.icons = panel, base, disc, gift, icons
    out.disc_ghost, out.gift_ghost, out.h, out.w = disc_ghost, gift_ghost, bh, bw
    return out


def _week_bar(x: float, base_y: float, v: float, width: float = 0.36) -> RoundedRectangle:
    color = GREEN if v > 0 else RED
    b = _col(width, abs(v), color, r=0.06)
    return b.move_to(np.array([x, base_y, 0]), aligned_edge=DOWN if v > 0 else UP)


def _week_flip(bar: Mobject, x: float, base_y: float, v0: float, v1: float) -> Animation:
    """A week's bar sinks into the line and comes out the other side: red below (a loss), green above."""
    def upd(m, a):
        v = interpolate(v0, v1, a)
        if abs(v) < 0.015:
            v = 0.015 if v1 > 0 else -0.015
        m.become(_week_bar(x, base_y, v))
    return UpdateFromAlphaFunc(bar, upd, rate_func=smooth)


def _weeks() -> VGroup:
    """Weekly results around a line: red below = a losing week. Attributes: .panel, .base, .bars, .cal, .xs, .base_y"""
    panel = _panel(5.6, 4.2, CHART_R_C)
    base_y = panel.get_y() + 0.45
    n, step = len(WEEKS_BEFORE), 0.6
    xs = [panel.get_x() - step * (n - 1) / 2 + step * k for k in range(n)]
    base = Line(np.array([xs[0] - 0.45, base_y, 0]), np.array([xs[-1] + 0.45, base_y, 0])).set_stroke(INK_2, width=2.5)
    bars = VGroup(*[_week_bar(x, base_y, v) for x, v in zip(xs, WEEKS_BEFORE)])
    cal = icon_calendar(0.62).move_to(panel.get_corner(UR) + np.array([-0.55, -0.5, 0]))
    out = VGroup(panel, base, bars, cal)
    out.panel, out.base, out.bars, out.cal, out.xs, out.base_y = panel, base, bars, cal, xs, base_y
    return out


class Bit6Fixes(AgentScene):
    def construct(self):
        self.continue_from("Bit5History")              # the cut from Bit5History is seamless
        m = master(guide=True, desk_on=True)
        w, h, wd = m.writer, m.hands, m.world
        self.w, self.h, self.wd = w, h, wd
        view = behind(m.view)
        lane = behind(loop_lane())
        slips = list(row_of_slips(5))
        # bit 5's last frame
        self.add(view, lane, m.desk, *slips, m.guide, m.to_hands, m.to_world, w, h, wd)

        # ---- 1. months later they reopened the shop: newer models, a few small changes around them ----
        with self.narrate("bit6_fixes.1"):
            shade = _veil(BG)
            self.add(shade)
            self.play(shade.animate.set_fill(opacity=0.55), run_time=0.6)        # closed for a while
            marker = _marker().move_to(MARKER_C)
            self.until("رجعوا", lead=0.25)
            self.play(shade.animate.set_fill(opacity=0.0), FadeIn(marker.box, scale=0.8), run_time=0.5)
            self.remove(shade)
            self.play(write_rtl(marker.text), run_time=0.55)
            self.until("بنماذج", lead=0.1)
            sheen = _sheen(w.box, run_time=0.9)
            self.play(sheen, w.box.animate(rate_func=there_and_back).set_stroke(INK, width=5.0),
                      LaggedStart(*[l.animate(rate_func=there_and_back).set_stroke(INK, opacity=1.0) for l in w.motif],
                                  lag_ratio=0.25, group=w.motif),
                      run_time=0.9)
            self.remove(sheen.mobject)
            w.box.set_stroke(ACCENT, width=3.0)
            self.until("وكم تغيير", lead=0.1)
            spots = [(MENU_PARK_C, WARM), (CHECK_DL + np.array([1.4, 0.75, 0]), GREEN), (BOSS_C, ACCENT)]
            sparks = []
            for k, (p, col) in enumerate(spots):
                sparks.append(flying(_sparkle(0.8, col).move_to(p)))
                sparks.append(flying(_sparkle(0.42, col).move_to(p + np.array([0.48, 0.34, 0]) * (1 if k % 2 else -1))))
            self.play(LaggedStart(*[_twinkle(s, run_time=0.75) for s in sparks], lag_ratio=0.22,
                                  group=flying(VGroup(*sparks))),
                      run_time=min(1.5, max(0.8, self.line_left() - 0.1)))
            self.remove(*sparks)

        # ---- 2. the menu now shows what each item cost -------------------------------------------------
        with self.narrate("bit6_fixes.2"):
            menu = flying(price_menu(show_cost=False))
            menu.set_height(MENU_BIG_H).move_to(MENU_BIG_C)
            costs = self._place_costs(menu)
            self.play(FadeIn(menu, scale=0.9), run_time=0.4)
            self.until("قديش", lead=0.2)
            self.play(LaggedStart(*[GrowFromEdge(c, RIGHT) for c in costs], lag_ratio=0.3, group=flying(VGroup(*costs))),
                      run_time=0.7)
            self._adopt(menu, zip(menu.rows, costs))
            cube = menu.rows[2]
            self.play(Indicate(costs[2], color=RED, scale_factor=1.12),
                      cube.bg.animate(rate_func=there_and_back).set_stroke(RED, width=3.0), run_time=0.45)
            self.play(menu.animate.set_height(MENU_PARK_H).move_to(MENU_PARK_C),
                      run_time=max(0.3, min(0.55, self.hold_left() - 0.05)))
            self.menu = menu

        # ---- 3. a checklist on the desk: check the cost, check the margin, then answer -----------------
        with self.narrate("bit6_fixes.3"):
            card = checklist_card().scale(CHECK_SCALE)
            card.move_to(CHECK_DL, aligned_edge=DL)
            ticks = card.ticks
            for t, b in zip(ticks, card.boxes):            # the kit places ticks before arranging the rows
                t.scale(CHECK_SCALE).move_to(b).shift(0.03 * CHECK_SCALE * UP)
            pin = card[2]
            card.remove(pin)
            card.set_z_index(Z_CHECK)
            pin.set_z_index(Z_CHECK)
            ticks.set_z_index(Z_CHECK)
            old, kept = slips[:2], slips[2:]
            self.play(*[s.animate.shift(0.9 * LEFT).set_opacity(0.0) for s in old],
                      *[s.animate.shift(SLIP_NUDGE * RIGHT) for s in kept], run_time=0.4)
            self.remove(*old)
            self.slips = kept
            self.play(FadeIn(card, shift=0.3 * DOWN, scale=1.04), run_time=0.45)
            self.play(FadeIn(pin, scale=2.5), run_time=0.22)
            self._adopt(card, [(card, pin)])
            for k, needle in enumerate(("شوف التكلفة", "شوف الربح", "جاوب")):
                self.until(needle, lead=0.1)
                self.play(ShowCreation(ticks[k]), Indicate(card.items[k][0], color=GREEN, scale_factor=1.06),
                          run_time=0.35)
            self._adopt(card, [(card, ticks)])
            self.check = card

        # ---- 4. a second agent, the boss, reads the first one's requests before they go out ------------
        with self.narrate("bit6_fixes.4"):
            self.play(marker.animate.scale(0.8).move_to(MARKER_PARK), run_time=0.45)
            boss_box = writer_box().scale(BOSS_SCALE).move_to(BOSS_C)
            label = ar_text(BOSS_AR, font_size=32, color=INK).next_to(boss_box, UP, buff=0.1)
            self.until("agent", lead=0.05)
            self.play(FadeIn(boss_box, scale=0.8), run_time=0.5)
            self.until("المدير", lead=0.25)
            self.play(write_rtl(label), run_time=0.45)
            boss = VGroup(boss_box, label)
            boss.box, boss.label = boss_box.box, label
            self.boss = boss
            self.until("بيقرا", lead=0.2)
            self._boss_reads(speed=1.0, seed=31)
            self._boss_reads(speed=1.7, seed=32)

        # ---- 5. discounts down ~80%, free items halved, most weeks no longer at a loss (+2 s hold) -----
        with self.narrate("bit6_fixes.5", pause=line_pause("bit6_fixes.5") + 2.0):
            dimmer = _veil(BG)
            self.add(dimmer)
            bars = _two_bars().set_z_index(Z_LIT)
            bars.disc_ghost.set_z_index(Z_LIT)
            bars.gift_ghost.set_z_index(Z_LIT)
            self.play(dimmer.animate.set_fill(opacity=0.86), FadeIn(bars, scale=0.94), run_time=0.5)
            self.until("نزلت تقريباً", lead=0.0)
            small = _col(bars.w, bars.h * DISC_SHARE, WARM).move_to(bars.disc.get_bottom(), aligned_edge=DOWN)
            self.play(FadeIn(bars.disc_ghost), Transform(bars.disc, small),
                      run_time=min(1.3, max(0.6, self.to("بالمية", lead=-0.2))))
            self.until("وكمية الغراض", lead=0.1)
            self.play(Indicate(bars.icons[1], color=ACCENT, scale_factor=1.2), run_time=0.45)
            self.until("نزلت للنص", lead=0.05)
            half = _col(bars.w, bars.h * GIFT_SHARE, ACCENT).move_to(bars.gift.get_bottom(), aligned_edge=DOWN)
            self.play(FadeIn(bars.gift_ghost), Transform(bars.gift, half), run_time=0.8)
            weeks = _weeks().set_z_index(Z_LIT)
            self.until("والمحل", lead=0.25)
            self.play(FadeIn(VGroup(weeks.panel, weeks.base, weeks.cal).set_z_index(Z_LIT), scale=0.96), run_time=0.35)
            self.play(LaggedStart(*[GrowFromEdge(b, UP) for b in weeks.bars], lag_ratio=0.12, group=weeks.bars),
                      run_time=0.6)
            self.until("بطّل يخسر", lead=0.0)
            flips = [_week_flip(b, x, weeks.base_y, v0, v1)
                     for b, x, v0, v1 in zip(weeks.bars, weeks.xs, WEEKS_BEFORE, WEEKS_AFTER)]
            self.play(LaggedStart(*flips, lag_ratio=0.14, group=weeks.bars), run_time=1.2)
            leave = max(0.1, self.hold_left() - 1.6)     # the lit diagram is back for about a second before night
            self.wait(leave)
            chart = Group(bars, bars.disc_ghost, bars.gift_ghost, weeks).set_z_index(Z_LIT)
            self.play(FadeOut(chart), dimmer.animate.set_fill(opacity=0.0), run_time=0.6)
            self.remove(dimmer)

        # ---- 6. not perfect: some nights the boss and the shopkeeper wrote to each other about ... -----
        with self.narrate("bit6_fixes.6"):
            night = _veil(NIGHT)
            self.add(night)
            self._lift(w, boss, z=Z_LIT)
            self.play(night.animate.set_fill(opacity=0.7), run_time=0.9)
            self.until("في أيام", lead=0.1)
            total = max(1.2, self.to("التسامي", lead=0.45))
            n, r = 7, 0.8
            d0 = total * (1 - r) / (1 - r ** n)
            for k in range(n):
                fwd = k % 2 == 0
                s = flying(_talk_slip(scale=0.9 + 0.07 * k, words=0.6 + 0.05 * k)).set_z_index(Z_LIT_FLY)
                a, b = (TALK_A, TALK_B) if fwd else (TALK_B, TALK_A)
                self._fly_between(s, a, b, run_time=d0 * r ** k, arc=-0.5 if fwd else 0.5)
            last = flying(_talk_slip(scale=1.4, words=0.95)).set_z_index(Z_LIT_FLY)
            mid = (TALK_A + TALK_B) / 2 + 0.1 * UP
            last.move_to(mid)
            self.play(FadeIn(last, shift=mid - TALK_A, scale=0.6), run_time=0.3)
            words = en_text(TRANSCEND_EN, font_size=48, color=WARM).set_width(WORDS_W).move_to(WORDS_C)
            words.set_z_index(Z_WORDS)
            self.until("التسامي", lead=0.1)
            self.play(ReplacementTransform(last.text, words),
                      FadeOut(VGroup(last.card, last.edge).set_z_index(Z_LIT_FLY), scale=1.3), run_time=0.75)
            self.words = words

        # ---- 7. two writers reading each other, nothing from the real world to correct them ------------
        with self.narrate("bit6_fixes.7"):
            glow_w, glow_b = _halo(w.box, ACCENT).set_z_index(Z_LIT), _halo(boss.box, ACCENT, 0.7).set_z_index(Z_LIT)
            self.add(glow_w, glow_b)
            per = max(0.3, min(0.42, self.to("وما في شي", lead=0.2) / 4))
            for g in (glow_w, glow_b, glow_w, glow_b):
                self.play(_halo_to(g, 0, 1, per, rate_func=there_and_back), run_time=per)
            self.remove(glow_w, glow_b)
            self.until("وما في شي", lead=0.1)
            a = np.array([h.get_right()[0] + 0.1, HANDS_C[1] + 0.32, 0])
            b = np.array([wd.get_center()[0] - 0.35, HANDS_C[1] + 0.32, 0])
            out_line = DashedLine(a, b, dash_length=0.16, positive_space_ratio=0.55)
            out_line.set_stroke(INK, width=4.5, opacity=0.9).set_z_index(Z_LIT)
            probe = Dot(radius=0.1).set_fill(INK, 1.0).set_z_index(Z_LIT_FLY).move_to(a)
            shade_w = wd.card.copy().set_fill(NIGHT, 0.0).set_stroke(width=0).set_z_index(Z_VEIL)
            self.add(shade_w)
            self.play(ShowCreation(out_line), run_time=0.5)
            self.add(probe)
            self.play(probe.animate.move_to(b), run_time=0.6)
            self.play(FadeOut(probe, scale=0.2), shade_w.animate.set_fill(opacity=0.55), run_time=0.45)
            self.out_line, self.shade_w = out_line, shade_w

        # ---- 8. their own lesson: an agent needs a little bureaucracy, and a little goes a long way ----
        with self.narrate("bit6_fixes.8"):
            self.play(night.animate.set_fill(opacity=0.0), self.shade_w.animate.set_fill(opacity=0.0),
                      FadeOut(self.words), FadeOut(self.out_line), FadeOut(marker), run_time=0.7)
            self.remove(night, self.shade_w)
            self._lift(w, boss, z=0)
            halo = _halo(self.check.page, GREEN).set_z_index(Z_CHECK)
            self.add(halo)
            self.until("شوية بيروقراطية", lead=0.15)
            self.play(_halo_to(halo, 0, 1, 0.5),
                      self.check.page.animate.set_stroke(GREEN, width=4.0),
                      LaggedStart(*[t.animate(rate_func=there_and_back).scale(1.45) for t in ticks], lag_ratio=0.3,
                                  group=self.check),
                      run_time=0.9)
            self.until("وهالشوية", lead=0.1)
            self.play(LaggedStart(*[t.animate(rate_func=there_and_back).scale(1.3) for t in ticks], lag_ratio=0.3,
                                  group=self.check), run_time=0.8)
            settle = max(0.1, self.hold_left() - 0.7)
            self.wait(settle)
            self.play(_halo_to(halo, 1, 0, 0.6), self.check.page.animate.set_stroke(GREEN, width=2.0), run_time=0.6)
            self.remove(halo)

    # ------------------------------------------------------------------ helpers
    def _adopt(self, parent: Mobject, pairs) -> None:
        """Move mobjects that were animated in on their own (top level) into a group of `parent`, so they
        travel with it from now on. pairs: (group, child) with group inside parent."""
        for grp, kid in pairs:
            self.remove(kid)
            grp.add(kid)
        self.add(parent)

    def _place_costs(self, menu: VGroup) -> list:
        """price_menu(show_cost=False) leaves each row's cost bar where it was built (before the rows were
        arranged and the menu scaled): size it like the menu and set it into its dashed slot."""
        k = menu.rows[0].bg.get_width() / 4.3
        out = []
        for row in menu.rows:
            c = row.cost
            c.scale(k)
            c.move_to(row.cost_slot.get_right(), aligned_edge=RIGHT)
            flying(c)
            out.append(c)
        return out

    def _lift(self, *mobs: Mobject, z: int) -> None:
        """Put mobjects on another drawing layer (above or back under the veils)."""
        for mob in mobs:
            mob.set_z_index(z)
        self.add(*mobs)

    def _boss_reads(self, speed: float = 1.0, seed: int = 0) -> None:
        """A request leaves the writer, goes up under the boss, gets a tick, then goes down into the hands."""
        r = flying(slip(kind="request", width=SLIP_W, seed=seed)).scale(0.85).move_to(REQ_FROM)
        self.play(FadeIn(r, scale=0.5), run_time=0.25 / speed)
        self.play(MoveAlongPath(r, ArcBetweenPoints(REQ_FROM, BOSS_READ, angle=-PI / 4)), run_time=0.5 / speed)
        tick = flying(icon_check(0.46, GREEN)).move_to(r.get_corner(UR) + np.array([0.02, 0.0, 0]))
        self.play(ShowCreation(tick), self.boss.box.animate(rate_func=there_and_back).set_stroke(INK, width=4.5),
                  run_time=0.3 / speed)
        go = flying(VGroup(r, tick))
        self.play(go.animate.scale(0.3).move_to(self.h.get_center()).set_opacity(0.0), run_time=0.4 / speed)
        self.remove(go, r, tick)

    def _fly_between(self, s: VGroup, a, b, run_time: float, arc: float = -0.5) -> None:
        """A slip leaves one writer and flies into the other (fading in and out at the ends)."""
        path = ArcBetweenPoints(a, b, angle=arc)
        s.move_to(a)
        base_op = 1.0

        def upd(m, t):
            m.move_to(path.point_from_proportion(smooth(t)))
            m.set_opacity(base_op * min(1.0, 5 * t, 5 * (1 - t)))
        self.add(s)
        self.play(UpdateFromAlphaFunc(s, upd), run_time=run_time, rate_func=linear)
        self.remove(s)
