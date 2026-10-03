"""
Bit5History — the loop is old: 2022, 2023's viral project going in circles, trained writers since.

Starts on bit 4's last frame (the writer, the yes dial at «أكيد», two thumbs-up, a question mark).
  1 that frame clears; "this loop": a loop draws in the middle; "isn't new": a thin timeline across
    the top, three years on it (2022 · 2023 · 2024)
  2 2022 lights and the loop slides back under it; «فكّر · نفّذ · اقرا» sit around it and light in
    turn; on «وعيد» a dot runs once around
  3 2023 lights; a second loop with a small writer in it; on «يشغّل حالو بحالو» a dot laps it by
    itself (the writer flashes each lap); «وبكم أسبوع ... GitHub»: a star on a bar that shoots up
  4 the loop winds itself into a spiral; the dot goes round and round, into its inner ring, and never
    gets out
  5 2024 lights and the shared socket (bit 2) drops under it; the spiral unwinds into a clean circle;
    the writer glows each lap; three quick laps, a tick each (practice)
  6 the small writer becomes the master writer and the loop its lane: the whole diagram, dim; the
    writer lights (its training), then everything around it (guide, hands, desk, world); hold on the
    lit diagram (bit 6 starts from it)

Render (preview): .venv/bin/manimgl our_scenes/bit5_history.py Bit5History -w -l --video_dir ./media
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from our_scenes.agent_kit import *  # noqa: F401,F403

# ---- layout ---------------------------------------------------------------------------------------
TL_Y = 2.6                                   # the timeline
TL_X0, TL_X1 = -5.4, 5.4
YEARS = ["2022", "2023", "2024"]
YEAR_X = [-3.8, 0.0, 3.8]
C_MID, R_MID = np.array([0.0, 0.1, 0]), 1.35  # "this loop", before it goes back to 2022
C22, R22 = np.array([-3.8, 0.3, 0]), 0.9     # the 2022 loop (think · act · read)
C23, R23 = np.array([0.0, 0.3, 0]), 1.05     # the 2023 loop, a small writer in it
SPIRAL_OUT, SPIRAL_IN, SPIRAL_TURNS = 1.62, 0.82, 2.0
HEAD_DEGS = (30, -90, 150)                   # arrowheads, between the three words
WORD_DEGS = (90, -30, 210)                   # فكّر top, نفّذ right, اقرا left: clockwise
BAR_X, BAR_Y0, BAR_H = 2.35, -0.75, 2.15     # the popularity bar (x, bottom, full height)
SOCKET_SIZE = 1.25
SOCKET_C = np.array([3.8, TL_Y - 0.17 - 0.45 * SOCKET_SIZE, 0])  # hangs under the 2024 tick
TOKEN_Y, TOKEN_XS = -1.5, (-0.8, 0.0, 0.8)   # practice ticks, under the loop
TRAIL = 0.45 * TAU                           # the running dot's tail (angle behind it)
RING_W = 4.0
FRAME = 1 / 15 + 0.005                       # fills stop a frame short, so a block never overruns its line

# The recording of bit5_history.3 pauses four times but its text has only two punctuation marks, so
# line_word_at() pins most of its words seconds early. Its phrases, one per voiced stretch:
PHRASES_3 = ["وسنة 2023،", "مشروع هواة", "اسمو AutoGPT", "خلّى نموذج تشات يشغّل حالو بحالو.",
             "وبكم أسبوع صار أكتر مشروع trendy ع GitHub…"]


# ---- small helpers ---------------------------------------------------------------------------------
def _polar(center, r: float, phi: float) -> np.ndarray:
    """The point at distance r from center, phi radians clockwise from straight up."""
    a = PI / 2 - phi
    return center + r * np.array([np.cos(a), np.sin(a), 0.0])


def _near(phi: float, station: float, width: float = 0.8) -> float:
    """1 when phi is at the station angle, falling to 0 `width` radians either side."""
    d = abs((phi - station + PI) % TAU - PI)
    return float(max(0.0, 1.0 - d / width))


def _head(center, r: float, deg: float, color=ACCENT, size: float = 0.24) -> VMobject:
    """An arrowhead on a circle at `deg` (counter-clockwise from +x), pointing clockwise."""
    th = deg * DEGREES
    tip = Triangle().set_height(size).set_fill(color, 1.0).set_stroke(width=0)
    tip.rotate(th - PI).move_to(center + r * np.array([np.cos(th), np.sin(th), 0]))
    return tip


def _circle(center, r: float, phi0: float = 0.0, color=ACCENT, width: float = RING_W) -> VMobject:
    """A clockwise circle that starts phi0 clockwise from the top (so morphs line up)."""
    p = Arc(start_angle=PI / 2 - phi0, angle=-TAU, radius=r, arc_center=center)
    return p.set_stroke(color, width=width).set_fill(opacity=0)


def _ring(center, r: float, color=ACCENT) -> VGroup:
    """A small loop: a circle with three arrowheads (clockwise). Attributes: .path, .heads"""
    path = _circle(center, r, 0.0, color)
    heads = VGroup(*[_head(center, r, d, color) for d in HEAD_DEGS])
    out = VGroup(path, heads)
    out.path, out.heads = path, heads
    return out


def _curve(center, phi0: float, s0: float, s1: float, rf, color=ACCENT, width: float = RING_W,
           fade: float = 0.0) -> VMobject:
    """The clockwise polar curve phi0+s, radius rf(s), for s in [s0, s1]. With `fade`, the spiral's
    outer coils are fainter (1 - fade at its outer end), so the eye runs inward."""
    n = max(12, int((s1 - s0) / 0.05))
    ss = np.linspace(s0, s1, n + 1)
    p = VMobject()
    p.set_points_smoothly([_polar(center, rf(s), phi0 + s) for s in ss])
    p.set_stroke(color, width=width).set_fill(opacity=0)
    if fade > 0:
        p.set_stroke(opacity=1.0 - fade * (1.0 - np.clip(ss / (SPIRAL_TURNS * TAU), 0.0, 1.0)))
    return p


def _spiral_r(s: float) -> float:
    """The spiral's radius s radians along it: winds in, then stays on its inner ring."""
    k = float(np.clip(s / (SPIRAL_TURNS * TAU), 0.0, 1.0))
    return SPIRAL_OUT + (SPIRAL_IN - SPIRAL_OUT) * k


SPIRAL_END = (SPIRAL_TURNS + 1) * TAU         # the spiral, then once more round its inner ring


def _around(word: Mobject, center, r: float, deg: float, gap: float = 0.16) -> Mobject:
    """Put `word` just outside the circle (center, r), in the direction `deg`."""
    th = deg * DEGREES
    d = np.array([np.cos(th), np.sin(th), 0])
    sup = abs(d[0]) * word.get_width() / 2 + abs(d[1]) * word.get_height() / 2
    return word.move_to(center + (r + gap + sup) * d)


def _pillar(height: float, width: float = 0.36, color=WARM) -> RoundedRectangle:
    """The popularity bar, standing on its bottom edge at (BAR_X, BAR_Y0)."""
    b = RoundedRectangle(width=width, height=max(height, 1e-3), corner_radius=min(width / 2, height / 2))
    b.set_fill(color, opacity=1.0).set_stroke(width=0)
    return b.move_to(np.array([BAR_X, BAR_Y0, 0]), aligned_edge=DOWN)


def _darken(mob: Mobject, k: float = 0.25) -> Mobject:
    """Dim a part by darkening its colours toward the black background (≈ k opacity), keeping
    fills opaque so nothing behind shows through."""
    bg = np.array(color_to_rgb(BG))
    for sm in mob.get_family():
        if not sm.has_points():
            continue
        for name in ("fill_rgba", "stroke_rgba"):
            if name in sm.data.dtype.names:
                sm.data[name][:, :3] = bg + k * (sm.data[name][:, :3] - bg)
        sm.note_changed_data()
    return mob


def _bit4_last_frame() -> VGroup:
    """Bit 4's last frame (approximately): the writer, the dial stuck at yes, thumbs-up, a question."""
    w = writer_box().scale(1.1).move_to(np.array([-3.6, 0.2, 0]))
    d = dial(1.9).move_to(np.array([1.6, 0.4, 0]))
    d.set_value(0.97)
    thumbs = VGroup(thumbs_up(0.7), thumbs_up(0.7)).arrange(RIGHT, buff=0.15)
    thumbs.move_to(np.array([-0.75, -1.6, 0]))
    q = question_mark(0.9).next_to(d, RIGHT, buff=0.35)
    return VGroup(w, d, thumbs, q)


class Bit5History(AgentScene):
    def construct(self):
        self.continue_from("Bit4Yes")              # the cut from Bit4Yes is seamless
        start = _bit4_last_frame()
        self.add(start)
        self.dot = self.trail = None

        line = behind(Line(np.array([TL_X0, TL_Y, 0]), np.array([TL_X1, TL_Y, 0])))
        line.set_stroke(INK_2, width=2.5, opacity=0.65)
        tip = Triangle().set_height(0.2).rotate(-PI / 2).set_fill(INK_2, 0.65).set_stroke(width=0)
        tip.move_to(np.array([TL_X1 + 0.06, TL_Y, 0]))
        tdots = VGroup(*[Dot(radius=0.09).set_fill(MUTED, 1).move_to(np.array([x, TL_Y, 0])) for x in YEAR_X])
        years = VGroup(*[en_text(y, font_size=50, color=MUTED).next_to(d, UP, buff=0.18) for y, d in zip(YEARS, tdots)])
        self.tdots, self.years = tdots, years

        # ---- 1. the strange part: this loop isn't a new invention ---------------------------------
        with self.narrate("bit5_history.1"):
            self.play(FadeOut(start), run_time=0.55)
            ring0 = _ring(C_MID, R_MID)
            self.until("هالدورة", lead=0.5)
            self.play(ShowCreation(ring0.path), FadeIn(ring0.heads, lag_ratio=0.3), run_time=0.6)
            self.until("مانا", lead=0.15)
            self.play(ShowCreation(line), run_time=max(0.35, min(0.6, self.to("جديد", lead=0.25))))
            self.play(FadeIn(tip), LaggedStart(*[FadeIn(VGroup(d, y), shift=0.12 * DOWN) for d, y in zip(tdots, years)],
                                               lag_ratio=0.3), run_time=0.5)

        # ---- 2. 2022: researchers described it: think, act, read the result, and again --------------
        with self.narrate("bit5_history.2"):
            ring22 = _ring(C22, R22)
            self.until("2022", lead=0.35)
            self.play(*self._year("on", 0), ReplacementTransform(ring0, ring22), run_time=0.75)
            words = VGroup(*[ar_text(s, font_size=46, color=INK_2) for s in LOOP_WORDS_AR])
            for w, deg in zip(words, WORD_DEGS):
                _around(w, C22, R22, deg)
            words.set_fill(opacity=0.55)
            self.until("باحثين", lead=0.15)
            self.play(LaggedStart(*[FadeIn(w, scale=0.8) for w in words], lag_ratio=0.25), run_time=0.6)
            for k, needle in enumerate(("فكّر", "نفذ", "اقرا")):
                self.until(needle, lead=0.15)
                anims = [words[k].animate.scale(1.15).set_fill(ACCENT, 1)]
                if k:
                    anims.append(words[k - 1].animate.scale(1 / 1.15).set_fill(INK, 1))
                self.play(*anims, run_time=0.3)
            self.until("وعيد", lead=0.3)
            self._new_dot(C22, R22)
            self.play(words[2].animate.scale(1 / 1.15).set_fill(INK, 1), FadeIn(self.dot, scale=0.4), run_time=0.2)
            stations = [PI / 2 - deg * DEGREES for deg in WORD_DEGS]
            flash = [self._word_flash(w, st) for w, st in zip(words, stations)]
            self._orbit(1.0, run_time=0.85, rf=lambda phi, a: R22, hooks=flash)
            self.play(FadeOut(self.dot), FadeOut(self.trail), words[0].animate.set_fill(INK, 1), run_time=0.2)
            self.remove(self.dot, self.trail)

        # ---- 3. 2023: a hobby project lets a chat model run itself; within weeks, the top of GitHub --
        with self.narrate("bit5_history.3"):
            ring23 = _ring(C23, R23)
            w23 = writer_box().scale(0.45).move_to(C23)
            self._until_ph(0, "2023", lead=0.4)
            self.play(*self._year("on", 1), *self._year("past", 0), self._fade(VGroup(ring22, words), 0.5), run_time=0.5)
            self._until_ph(1, lead=0.2)
            self.play(ShowCreation(ring23.path), FadeIn(ring23.heads, lag_ratio=0.5),
                      run_time=min(1.4, max(0.7, self._to_ph(3, lead=0.6))))
            self._until_ph(3, "نموذج", lead=0.35)
            self.play(FadeIn(w23, scale=0.7), run_time=0.45)
            self._until_ph(3, "يشغّل", lead=0.3)
            self._new_dot(C23, R23)
            self.play(FadeIn(self.dot, scale=0.4), run_time=0.2)
            on_r = lambda phi, a: R23                       # noqa: E731
            flash_w = self._writer_flash(w23)
            self._orbit_for(self._to_ph(4, lead=0.25), 1.0, on_r, hooks=[flash_w])
            # popularity: a star on a bar that shoots up (no numbers)
            base = Line(np.array([BAR_X - 0.36, BAR_Y0, 0]), np.array([BAR_X + 0.36, BAR_Y0, 0]))
            base.set_stroke(INK_2, width=2.5, opacity=0.8)
            bar = _pillar(0.08)
            star = icon_star(0.66, WARM).next_to(bar, UP, buff=0.06)
            self.pop = VGroup(base, bar, star)
            self._orbit_for(0.25, 1.0, on_r, hooks=[flash_w], anims=[FadeIn(base), FadeIn(bar), FadeIn(star, scale=0.5)])

            def grow(m, a):
                h = 0.08 + (BAR_H - 0.08) * a ** 3          # slow, then shoots up
                m.become(_pillar(h))
                star.next_to(m, UP, buff=0.06)
            self._orbit_for(self._to_ph(4, "GitHub", lead=0.1, minimum=0.6), 1.0, on_r, hooks=[flash_w],
                            anims=[UpdateFromAlphaFunc(bar, grow)])
            self._orbit_for(0.5, 1.0, on_r, hooks=[flash_w],
                            anims=[Flash(star, color=WARM, flash_radius=0.55, line_length=0.2, num_lines=10),
                                   star.animate(rate_func=there_and_back).scale(1.3)])
            self._orbit_for(self.hold_left() - FRAME, 1.0, on_r, hooks=[flash_w])

        # ---- 4. ...and in the end it mostly went round and round in the same place -------------------
        with self.narrate("bit5_history.4"):
            phi0 = self.phi
            curve = _curve(C23, phi0, 0, TAU, lambda s: R23)    # the same circle, starting at the dot
            self.remove(ring23.path)
            self.add(curve)
            ring23.path = curve

            def wind(phi, a):                                   # circle -> spiral (the dot rides on it)
                e = smooth(a)
                curve.become(_curve(C23, phi0, 0, TAU + e * (SPIRAL_END - TAU), lambda s: (1 - e) * R23 + e * _spiral_r(s),
                                    fade=0.6 * e))
            self._reset_writer(w23)
            self._orbit(0.85, run_time=0.7, rf=lambda phi, a: (1 - smooth(a)) * R23 + smooth(a) * _spiral_r(phi - phi0),
                        hooks=[wind], anims=[FadeOut(ring23.heads), self._fade(self.pop, 0.3)])
            turns = (SPIRAL_TURNS * TAU - (self.phi - phi0)) / TAU
            self._orbit(turns, run_time=turns / 1.3, rf=lambda phi, a: _spiral_r(phi - phi0))
            self._orbit_for(self.hold_left() - FRAME, 1.45, lambda phi, a: SPIRAL_IN)

        # ---- 5. since then the writers are trained inside this loop, practising again and again ------
        with self.narrate("bit5_history.5"):
            sock = socket(SOCKET_SIZE).move_to(SOCKET_C)
            in_r = lambda phi, a: SPIRAL_IN                     # noqa: E731
            self._orbit_for(0.5, 1.45, in_r, anims=[*self._year("on", 2), *self._year("past", 1),
                                                    FadeIn(sock, shift=0.3 * DOWN), FadeOut(self.pop)])
            self._orbit_for(self.to("يدرّبوا", lead=0.3), 1.45, in_r)
            # the spiral unwinds into one clean circle
            def unwind(phi, a):
                e = smooth(a)
                curve.become(_curve(C23, phi0, e * SPIRAL_TURNS * TAU, SPIRAL_END,
                                    lambda s: (1 - e) * _spiral_r(s) + e * R23, fade=0.6 * (1 - e)))
            self._orbit(0.7, run_time=0.6, rf=lambda phi, a: (1 - smooth(a)) * SPIRAL_IN + smooth(a) * R23,
                        hooks=[unwind])
            circ = _circle(C23, R23)
            self.remove(curve)
            self.add(circ)
            ring23.path = circ
            halo = RoundedRectangle(width=w23.box.get_width() + 0.2, height=w23.box.get_height() + 0.2,
                                    corner_radius=0.22 * (w23.box.get_height() + 0.2)).move_to(w23.box)
            halo.set_stroke(ACCENT, width=10, opacity=0).set_fill(opacity=0)
            self.add(halo)
            glow = self._writer_flash(w23, halo)
            on_r = lambda phi, a: R23                           # noqa: E731
            # laps on the clean circle, the writer glowing each time round; end on the top
            t_glow = self.to("يتمرّنوا", lead=0.1, minimum=0.6)
            frac = ((-self.phi) % TAU) / TAU
            n = min(range(4), key=lambda n: abs((frac + n) / t_glow - 1.1))
            self._orbit(frac + n, run_time=t_glow, rf=on_r, hooks=[glow], anims=[FadeIn(ring23.heads)])
            # practice: three quick laps, a tick out of each
            ticks = VGroup(*[icon_check(0.62, GREEN) for _ in TOKEN_XS])
            slots = [np.array([x, TOKEN_Y, 0]) for x in TOKEN_XS]
            for t in ticks:
                flying(t)
                t.set_stroke(opacity=0).move_to(_polar(C23, R23, PI))
            self.add(ticks)
            pq = self.phi
            drop = self._drop_hook(ticks, slots, [pq + PI + k * TAU for k in range(3)])
            self._orbit(3.0, run_time=3.0 / 1.8, rf=on_r, hooks=[glow, drop])
            self._orbit_for(self.hold_left() - FRAME, 1.0, on_r, hooks=[glow])
            self.ticks, self.sock, self.halo = ticks, sock, halo

        # ---- 6. same loop; what changed is the writer's training, and everything around it ----------
        with self.narrate("bit5_history.6"):
            m = master(guide=True, desk_on=True)
            lane = behind(loop_lane())
            view = behind(m.view)
            slips = row_of_slips(5)
            parts = [view, lane, m.desk, slips, m.guide, m.writer, m.hands, m.world, m.to_hands, m.to_world]
            for p in parts:
                p.save_state()
                _darken(p, 0.25)
            self._reset_writer(w23)
            circ2 = behind(_circle(C23, R23, phi0=-PI / 4))       # the same circle, from its top left
            self.remove(ring23.path)
            self.add(circ2)
            lane_solid = behind(lane.path.copy())
            lane_solid.set_stroke(ACCENT, width=3, opacity=0.6)
            _darken(lane_solid, 0.25)
            old = VGroup(line, tip, tdots, years, ring22, words, sock, ring23.heads, self.ticks, self.halo)
            self.play(FadeOut(old, time_span=(0, 0.4)), FadeOut(self.dot, time_span=(0, 0.25)),
                      FadeOut(self.trail, time_span=(0, 0.25)),
                      ReplacementTransform(w23, m.writer, time_span=(0.15, 1.0)),
                      Transform(circ2, lane_solid, time_span=(0.15, 1.0)),
                      *[FadeIn(p, time_span=(0.35, 1.0)) for p in (view, m.desk, slips, m.guide, m.hands, m.world,
                                                                  m.to_hands, m.to_world)],
                      run_time=1.0)
            self.remove(self.dot, self.trail)
            self.play(FadeOut(circ2), FadeIn(lane), run_time=0.25)
            self.remove(circ2)
            # the writer's training: it lights, briefly glowing
            self.until("تدريب", lead=0.25)
            box = m.writer.box
            halo = RoundedRectangle(width=box.get_width() + 0.12, height=box.get_height() + 0.12,
                                    corner_radius=0.22 * (box.get_height() + 0.12)).move_to(box)
            halo.set_stroke(ACCENT, width=12, opacity=0.7).set_fill(opacity=0)
            self.play(Restore(m.writer), run_time=0.35)
            self.play(halo.animate.scale(1.18).set_stroke(opacity=0),
                      box.animate(rate_func=there_and_back).set_stroke(INK, width=6), run_time=0.6)
            self.remove(halo)
            # and everything around it, one after another
            self.until("وكل شي", lead=0.15)
            steps = [[m.guide], [m.hands, m.to_hands], [m.desk, view, slips], [m.world, m.to_world, lane]]
            self.play(*[Restore(p, time_span=(0.3 * k, 0.3 * k + 0.55)) for k, ps in enumerate(steps) for p in ps],
                      run_time=0.3 * (len(steps) - 1) + 0.55)
            # "how much that second part matters": the parts around the writer, once more
            self.until("هالجزء", lead=0.25)
            around = [m.guide.card, m.hands.box, m.desk.top, m.world.card]
            self.play(*[p.animate(rate_func=there_and_back).set_stroke(INK, width=p.get_stroke_width() + 2.0)
                        for p in around], run_time=0.8)

    # ------------------------------------------------------------------ the timeline
    def _year(self, state: str, i: int) -> list:
        """Year i lit ('on': the current one) or settled back ('past')."""
        d, y = self.tdots[i], self.years[i]
        if state == "on":
            return [d.animate.set_fill(ACCENT, 1).set_width(0.26), y.animate.set_fill(INK, 1)]
        return [d.animate.set_fill(ACCENT, 0.55).set_width(0.18), y.animate.set_fill(INK_2, 0.75)]

    def _fade(self, mob: Mobject, k: float) -> Animation:
        """Dim mob to k of its brightness (fills stay opaque)."""
        return Transform(mob, _darken(mob.copy(), k))

    # ------------------------------------------------------------------ line 3's word times
    def _ph_t(self, i: int, needle: str | None, lead: float) -> float:
        """Absolute time of `needle` in phrase i of bit5_history.3 (or of the phrase's start), from the
        recording's voiced stretches; falls back to line_word_at() if the recording splits differently."""
        ln = self._line
        phrases = line_phrases(ln["key"])
        if len(phrases) != len(PHRASES_3):
            return self._word_t(needle or PHRASES_3[i].split()[0], lead)
        a, b = phrases[i]
        frac = 0.0
        if needle:
            letters = lambda s: len(re.sub(r"[\W_]", "", s))      # noqa: E731
            text = PHRASES_3[i]
            frac = letters(text[:text.index(needle)]) / max(1, letters(text))
        return ln["start"] + a + frac * (b - a) - lead

    def _until_ph(self, i: int, needle: str | None = None, lead: float = 0.12) -> None:
        t = self._ph_t(i, needle, lead)
        if t > self.time + 1e-3:
            self.wait(t - self.time)

    def _to_ph(self, i: int, needle: str | None = None, lead: float = 0.12, minimum: float = 0.25) -> float:
        return max(minimum, self._ph_t(i, needle, lead) - self.time)

    # ------------------------------------------------------------------ the running dot
    def _new_dot(self, center, r: float, phi: float = 0.0) -> None:
        """A dot on the circle (center, r) at phi (clockwise from the top), with a fading tail."""
        self.oc, self.phi, self.trail_from = center, phi, phi
        self.dot = Dot(radius=0.12).set_fill(INK, 1).set_stroke(width=0).move_to(_polar(center, r, phi))
        self.dot.set_z_index(3)
        self.trail = flying(VMobject())
        self.trail.set_points(np.array([self.dot.get_center()] * 3))
        self.trail.set_stroke(ACCENT, width=0, opacity=0).set_fill(opacity=0)
        self.add(self.trail, self.dot)

    def _set_trail(self, phi: float, rf, a: float) -> None:
        lo = max(self.trail_from, phi - TRAIL)
        if phi - lo < 0.05:
            self.trail.set_stroke(opacity=0)
            return
        pts = [_polar(self.oc, rf(p, a), p) for p in np.linspace(lo, phi, 20)]
        self.trail.set_points_smoothly(pts)
        self.trail.set_stroke(INK, width=[0.0, 9.0], opacity=[0.0, 0.9])

    def _orbit(self, turns: float, run_time: float, rf, hooks=(), anims=(), rate_func=linear) -> None:
        """The dot goes `turns` laps clockwise in run_time; rf(phi, alpha) is its distance from the
        centre; hooks(phi, alpha) run every frame (things that react as it passes)."""
        if run_time < 0.02:
            return
        phi0 = self.phi

        def upd(m, a):
            phi = phi0 + turns * TAU * a
            m.move_to(_polar(self.oc, rf(phi, a), phi))
            self._set_trail(phi, rf, a)
            for h in hooks:
                h(phi, a)
        self.play(UpdateFromAlphaFunc(self.dot, upd, rate_func=rate_func), *anims, run_time=run_time)
        self.phi = phi0 + turns * TAU

    def _orbit_for(self, seconds: float, laps_per_s: float, rf, hooks=(), anims=()) -> None:
        """Keep the dot going for `seconds` at a steady speed."""
        if seconds < 0.05:
            return
        self._orbit(seconds * laps_per_s, seconds, rf, hooks=hooks, anims=anims)

    def _word_flash(self, word: Mobject, station: float):
        def hook(phi, a):
            word.set_fill(interpolate_color(INK, ACCENT, _near(phi, station, 0.9)), 1)
        return hook

    def _writer_flash(self, w: Mobject, halo: Mobject | None = None):
        """The small writer brightens as the dot passes the top (it writes the next step)."""
        def hook(phi, a):
            k = _near(phi, 0.0, 0.9)
            w.box.set_stroke(interpolate_color(ACCENT, INK, k), width=3.0 + 2.5 * k)
            if halo is not None:
                halo.set_stroke(ACCENT, opacity=0.6 * k)
        return hook

    def _reset_writer(self, w: Mobject) -> None:
        w.box.set_stroke(ACCENT, width=3.0)

    def _drop_hook(self, ticks: VGroup, slots: list, emit: list):
        """Each tick drops out of the bottom of the loop into its slot as the dot passes the bottom."""
        bases = [t.copy().set_stroke(opacity=1) for t in ticks]
        src = _polar(C23, R23, PI)

        def hook(phi, a):
            for t, b, slot, pe in zip(ticks, bases, slots, emit):
                p = float(np.clip((phi - pe) / (0.45 * TAU), 0.0, 1.0))
                e = smooth(p)
                t.become(b.copy().scale(0.5 + 0.5 * e).move_to(src + (slot - src) * e))
                t.set_stroke(opacity=min(1.0, 4.0 * p))
        return hook
