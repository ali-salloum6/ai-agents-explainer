"""
Bit4Yes — why it said yes: it was trained to be a helpful assistant, and helpful leans toward yes.

Opens on bit 3's last frame (the master diagram with the desk, the notebook and the loop lane; a
discount chip and a question mark at the top right).
  1 «قبل ما يدير أي محل»: the shop fades away, the writer glides left and grows a little;
    «مساعد مفيد»: a yes/no odds dial builds beside it, needle in the middle, the two odds bars equal
  2 «طلع بيحب يقول «أكيد»»: thumbs-up (the training) fly in from below and push the needle toward
    «أكيد», the bars tip; then they let go and the needle stays where they left it
  3 «زبون بيطلب خصم»: a customer's «خصم؟»; «الاحتمالات بتميل»: the needle tips further;
    «وبيطلع الخصم»: a discount chip pops out to the customers; again and again, quicker each time,
    the chips pile up
  4 «حكوها بصراحة»: the needle sticks at «أكيد», a shake can't move it back; «كل شي بينطلب منو»:
    the three requests pulse once more; «زيادة عن اللزوم»: a stop mark at the end of the yes bar's
    track, and the bar runs past it and glows
  5 «كيف التدريب بيدفش»: the requests and chips clear; the thumbs come back and keep pushing; a
    question mark beside the dial; «هاد موضوع الفيديو الجاي»: hold, the picture dims a little
End frame (bit 5 clears it): the writer, the dial at yes (its bar past the stop mark, glowing), the
thumbs on the needle, the question mark; all under a 30% black veil (z 5).

Render (preview): .venv/bin/manimgl our_scenes/bit4_yes.py Bit4Yes -w -l --video_dir ./media
"""
from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from our_scenes.agent_kit import *  # noqa: F401,F403
from our_scenes.agent_kit import _bar  # noqa: E402  (not exported by *)

WRITER_AT = np.array([-4.25, 0.35, 0.0])     # the writer, on its own now
WRITER_GROW = 1.2
DIAL_R = 2.2
HUB = np.array([0.85, -0.42, 0.0])          # the dial's hub (its semicircle sits on it)
NEEDLE_L = DIAL_R - 0.18                    # the kit's needle length
LABEL_GROW = 1.4                            # «لأ» / «أكيد» read at the upload size
REST = 0.72                                 # where the training leaves the needle
OVERFILL = 1.12                             # the yes bar at the end: past its track

THUMB_H = 0.55
THUMB_D = (0.32, 0.9, 1.48)                 # where along the needle each thumb pushes (line 2)
THUMB_D_END = (0.55, 1.13, 1.71)            # ... and on the needle pinned at yes, clear of the hub (line 5)
THUMB_GAP = 0.03

BUB_X = 4.95
BUB_YS = (2.72, 1.56, 0.40)                 # the customers' «خصم؟», a chat column
CHIP = 0.6
PILE = (np.array([4.65, -1.15, 0.0]), np.array([5.25, -1.15, 0.0]), np.array([4.95, -0.65, 0.0]))
QMARK_AT = np.array([4.75, 0.85, 0.0])


def _support(mob: Mobject, direction: np.ndarray) -> np.ndarray:
    """Offset from mob's centre to its outline point farthest along `direction`."""
    pts = mob.get_all_points()
    c = mob.get_center()
    return pts[int(np.argmax((pts - c) @ direction))] - c


def _bezier2(a: np.ndarray, c: np.ndarray, b: np.ndarray, t: float) -> np.ndarray:
    return (1 - t) ** 2 * a + 2 * (1 - t) * t * c + t ** 2 * b


class Bit4Yes(AgentScene):
    def construct(self):
        self.continue_from("Bit3Desk")              # the cut from Bit3Desk is seamless
        # ---- bit 3's last frame -------------------------------------------------------------------
        m = master(guide=False, desk_on=True)
        w = m.writer
        view = behind(m.view)
        lane = behind(loop_lane())
        slips = row_of_slips(5)
        nb = notebook().move_to(np.array([DESK_X1 - 0.62, DESK_Y + 0.62, 0]))
        pct0 = icon_percent(0.6).move_to(np.array([3.6, 2.6, 0]))
        q0 = question_mark(0.7).next_to(pct0, RIGHT, buff=0.18)
        shop = [view, lane, m.desk, slips, nb, m.to_hands, m.to_world, m.hands, m.world, pct0, q0]
        self.add(view, lane, m.desk, slips, nb, m.to_hands, m.to_world, w, m.hands, m.world, pct0, q0)

        dial = Dial(radius=DIAL_R)
        dial.shift(HUB - dial.hub.get_center())
        for label in (dial.no, dial.yes):
            label.scale(LABEL_GROW, about_edge=UP)
        self.dial = dial
        # a thin dark outline keeps neighbouring thumbs (and the needle under them) apart
        thumbs = [flying(thumbs_up(THUMB_H).set_stroke(BG, width=3, opacity=1)) for _ in THUMB_D]
        self.thumbs = thumbs

        # ---- 1. before any shop, it was trained to be a helpful assistant ---------------------------
        with self.narrate("bit4_yes.1"):
            self.play(*[FadeOut(mob) for mob in shop],
                      w.animate.scale(WRITER_GROW).move_to(WRITER_AT), run_time=min(1.1, self.to("كان", lead=0.2)))
            self.until("مساعد", lead=0.35)
            self.add(dial)
            self.play(self._build_dial(), run_time=max(0.6, min(0.95, self.line_left() - 0.15)))

        # ---- 2. and helpful, it turns out, loves to say «أكيد» --------------------------------------
        with self.narrate("bit4_yes.2"):
            self.until("طلع", lead=0.25)
            self._push_in(values=(0.58, 0.65, REST), ds=THUMB_D,             # the last push lands on «أكيد»
                          run_time=max(0.9, min(1.5, self.to("كتير", lead=0.35))))
            self.wait(max(0.01, self.hold_left() - 0.55))
            # they let go (lifting off the needle's «لأ» side) and the needle stays where they left it
            ang = (dial.value - 0.5) * PI
            away = np.array([-np.cos(ang), np.sin(ang), 0.0])
            self.play(LaggedStart(*[th.animate.shift(0.55 * away).set_opacity(0) for th in thumbs], lag_ratio=0.15),
                      run_time=0.5)
            self.remove(*thumbs)

        # ---- 3. a customer asks for a discount: the odds tip, out comes the discount; again, again ---
        with self.narrate("bit4_yes.3"):
            bubbles = [user_bubble(ASK_DISCOUNT_AR).move_to(np.array([BUB_X, y, 0])) for y in BUB_YS]
            chips = [flying(icon_percent(CHIP)) for _ in PILE]
            self.play(FadeIn(bubbles[0], shift=0.3 * LEFT), run_time=0.35)
            self.until("الاحتمالات", lead=0.1)
            self.play(dial.animate_to(0.86, run_time=min(0.9, self.to("وبيطلع", lead=0.25)), rate_func=overshoot))
            self.until("وبيطلع", lead=0.2)
            self.play(self._chip_out(chips[0], PILE[0]), run_time=0.55)
            self.play(dial.animate_to(0.74, run_time=0.45))
            # again: quicker
            self.until("ومرة تانية", lead=0.12)
            self.play(FadeIn(bubbles[1], shift=0.3 * LEFT, rate_func=squish_rate_func(smooth, 0.0, 0.4)),
                      dial.animate_to(0.88, run_time=0.7, rate_func=squish_rate_func(overshoot, 0.1, 0.55)),
                      self._chip_out(chips[1], PILE[1], window=(0.45, 1.0)), run_time=0.7)
            self.play(dial.animate_to(0.8, run_time=0.25))
            # and again: quicker still
            self.until("ومرة تالتة", lead=0.1)
            self.play(FadeIn(bubbles[2], shift=0.3 * LEFT, rate_func=squish_rate_func(smooth, 0.0, 0.4)),
                      dial.animate_to(0.92, run_time=0.55, rate_func=squish_rate_func(overshoot, 0.05, 0.5)),
                      self._chip_out(chips[2], PILE[2], window=(0.4, 1.0)), run_time=0.55)
            past = bubbles + chips

        # ---- 4. the people who ran it said so plainly: far too willing ---------------------------------
        with self.narrate("bit4_yes.4"):
            self.until("حكوها", lead=0.2)
            self.play(dial.animate_to(0.97, run_time=0.35, rate_func=rush_into))
            self.play(self._stuck_shake(0.97), run_time=0.65)
            self.until("كل شي", lead=0.2)                   # everything asked of it: the requests, once more
            self.play(LaggedStart(*[b.animate.scale(1.07).set_anim_args(rate_func=there_and_back) for b in bubbles],
                                  lag_ratio=0.3), run_time=0.6)
            self.until("زيادة", lead=0.3)
            over, glow, stop = self._overfill()
            self.add(glow, over)
            self.play(FadeIn(stop, scale=0.5), run_time=0.2)
            self.play(self._grow_over(over), self._glow_in(glow), Indicate(dial.yes, color=ACCENT, scale_factor=1.15),
                      run_time=0.6)

        # ---- 5. how does training push a model that way? the next video ---------------------------------
        with self.narrate("bit4_yes.5"):
            self.play(*[FadeOut(mob) for mob in past], run_time=0.35)
            self.until("التدريب", lead=0.15)
            self._push_in(values=(0.975, 0.98, 0.985), ds=THUMB_D_END, from_above=True,
                          run_time=max(0.9, min(1.4, self.to("بهالاتجاه", lead=0.3))))
            q = question_mark(1.1, INK).move_to(QMARK_AT)
            self.until("بهالاتجاه", lead=0.25)
            self.play(FadeIn(q, scale=0.6, shift=0.1 * UP), run_time=0.4)
            veil = Rectangle(width=FRAME_WIDTH + 1, height=FRAME_HEIGHT + 1).set_fill(BG, 0.0).set_stroke(width=0)
            veil.set_z_index(5)
            self.add(veil)
            hold = max(0.6, self.hold_left() - 0.02)
            dim_from = max(0.0, 1.0 - 1.0 / hold)          # the last second of the pause
            self.play(self._keep_pushing(hold),
                      UpdateFromAlphaFunc(veil, lambda mob, a: mob.set_fill(
                          BG, 0.3 * smooth(float(np.clip((a - dim_from) / max(1e-6, 1 - dim_from), 0, 1))))),
                      run_time=hold, rate_func=linear)

    # ------------------------------------------------------------------ the dial
    def _build_dial(self) -> Animation:
        """The dial draws in: the band from «لأ» to «أكيد», the ticks, the two words, the needle
        standing in the middle, the two odds bars growing out from the centre."""
        d = self.dial
        return LaggedStart(
            AnimationGroup(FadeIn(d.track), LaggedStart(*[ShowCreation(s) for s in d.grad], lag_ratio=0.08)),
            FadeIn(d.ticks),
            AnimationGroup(FadeIn(d.no, shift=0.1 * UP), FadeIn(d.yes, shift=0.1 * UP)),
            AnimationGroup(GrowFromPoint(d.needle, d.hub.get_center()), FadeIn(d.hub, scale=0.5)),
            AnimationGroup(FadeIn(d.bar_no_bg), FadeIn(d.bar_yes_bg),
                           GrowFromEdge(d.bar_no, RIGHT), GrowFromEdge(d.bar_yes, LEFT)),
            lag_ratio=0.22)

    def _stuck_shake(self, v: float) -> Animation:
        """The dial is shaken; the needle twitches toward «لأ» and snaps back: it won't come off yes."""
        d = self.dial
        base = d.hub.get_center().copy()

        def upd(mob, a):
            env = np.sin(PI * a)
            dx = 0.09 * env * np.sin(6 * PI * a)
            dv = -0.07 * env * abs(np.sin(4 * PI * a))
            mob.shift(base + dx * RIGHT - mob.hub.get_center())
            mob._place(v + dv)
        return UpdateFromAlphaFunc(d, upd, rate_func=linear)

    def _overfill(self):
        """A copy of the yes bar that will run past the end of its track, a soft glow behind it, and a
        stop mark at the track's end for it to run past."""
        d = self.dial
        x0 = d.bar_yes_bg.get_left()
        over = _bar(d.bar_w * d.value, 0.16, ACCENT).move_to(x0, aligned_edge=LEFT)
        over.x0, over.w0, over.w1 = x0, d.bar_w * d.value, d.bar_w * OVERFILL
        stop = flying(Line(0.2 * UP, 0.2 * DOWN).set_stroke(INK, width=3.5).move_to(d.bar_yes_bg.get_right()))
        length = over.w1
        glow = VGroup(*[RoundedRectangle(width=length + 2 * p, height=0.16 + 2 * p, corner_radius=0.08 + p)
                        .set_fill(ACCENT, op).set_stroke(width=0)
                        for p, op in ((0.07, 0.30), (0.15, 0.15), (0.25, 0.07))])
        glow.move_to(x0 + 0.5 * length * RIGHT)
        glow.ops = [0.30, 0.15, 0.07]
        for g in glow:
            g.set_fill(opacity=0)
        behind(glow)
        return over, glow, stop

    def _grow_over(self, over) -> Animation:
        def upd(mob, a):
            mob.become(_bar(interpolate(over.w0, over.w1, a), 0.16, ACCENT).move_to(over.x0, aligned_edge=LEFT))
        return UpdateFromAlphaFunc(over, upd, rate_func=overshoot)

    def _glow_in(self, glow) -> Animation:
        """The glow flares up, then settles at its resting strength."""
        def upd(mob, a):
            k = 1.8 * smooth(a / 0.3) if a < 0.3 else 1.0 + 0.8 * (1 - smooth((a - 0.3) / 0.7))
            for g, op in zip(mob, glow.ops):
                g.set_fill(ACCENT, opacity=min(1.0, op * k))
        return UpdateFromAlphaFunc(glow, upd, rate_func=linear)

    # ------------------------------------------------------------------ the thumbs
    def _contact(self, thumb: Mobject, v: float, d: float) -> np.ndarray:
        """Where `thumb` (kept upright) sits when it leans on the needle's «لأ» side, at distance d
        along the needle, with the needle at value v."""
        th = (v - 0.5) * PI
        u = np.array([np.sin(th), np.cos(th), 0.0])          # along the needle
        n = np.array([-np.cos(th), np.sin(th), 0.0])         # out of its «لأ» side
        hw = 0.06 * max(0.0, 1 - d / NEEDLE_L)
        return self.dial.hub.get_center() + d * u + (THUMB_GAP + hw) * n - _support(thumb, -n)

    def _push_in(self, values, ds, run_time: float, fly: float = 0.45, push: float = 0.3,
                 from_above: bool = False) -> None:
        """The thumbs fly in one after another from below the frame; each lands on the needle's
        «لأ» side at ds[k] along it and pushes it on, to values[k]."""
        d, thumbs = self.dial, self.thumbs
        self.thumb_d = ds
        n = len(thumbs)
        lag = max(0.05, (run_time - fly - push) / max(1, n - 1))
        vals = [d.value] + list(values)
        hub = d.hub.get_center()
        starts = [hub + np.array([-2.5 + 0.45 * k, -4.6 - hub[1], 0]) for k in range(n)]
        if from_above:      # the needle lies nearly flat: come round over it and settle on top
            ctrls = [hub + np.array([-1.3 + 0.5 * k, 1.5 + 0.2 * k, 0]) for k in range(n)]
        else:
            ctrls = [hub + np.array([-2.0, 0.5 + 0.35 * k, 0]) for k in range(n)]
        for th, s in zip(thumbs, starts):
            th.set_opacity(1).move_to(s)
        self.add(*thumbs)                                    # below the frame until they fly in

        def v_at(t: float) -> float:
            v = vals[0]
            for k in range(n):
                p = float(np.clip((t - (k * lag + fly)) / push, 0, 1))
                v += smooth(p) * (vals[k + 1] - vals[k])
            return v

        def upd(mob, a):
            t = a * run_time
            v = v_at(t)
            mob._place(v)
            for k, th in enumerate(thumbs):
                target = self._contact(th, v, ds[k])
                q = float(np.clip((t - k * lag) / fly, 0, 1))
                th.move_to(target if q >= 1 else _bezier2(starts[k], ctrls[k], target, smooth(q)))

        self.play(UpdateFromAlphaFunc(d, upd, run_time=run_time, rate_func=linear))

    def _keep_pushing(self, run_time: float) -> Animation:
        """The thumbs keep leaning on the needle: small presses in turn, the needle trembling at yes."""
        d, thumbs = self.dial, self.thumbs
        v0 = d.value
        period = 1.1

        def upd(mob, a):
            t = a * run_time
            press = [max(0.0, np.sin(TAU * (t / period - 0.3 * k))) ** 2 for k in range(len(thumbs))]
            v = min(1.0, v0 + 0.006 * sum(press))
            mob._place(v)
            for k, th in enumerate(thumbs):
                base = self._contact(th, v, self.thumb_d[k])
                th.move_to(base + 0.025 * press[k] * DOWN)
        return UpdateFromAlphaFunc(d, upd, run_time=run_time, rate_func=linear)

    # ------------------------------------------------------------------ the discounts
    def _chip_out(self, chip: Mobject, target: np.ndarray, window=(0.0, 1.0)) -> Animation:
        """A discount chip pops out at the needle's tip and drops onto the pile by the customers."""
        d = self.dial
        tmpl = chip.copy()
        a0, a1 = window
        state = {}
        pop = 0.3                                          # share of the time it spends popping at the tip

        def upd(mob, a):
            if a < a0:                                     # not yet: hidden (and the tip not yet read)
                state.clear()
                mob.become(tmpl.copy().scale(0.01)).set_opacity(0)
                return
            if not state:                                  # read the tip once, after the needle has swung
                th = (d.value - 0.5) * PI
                state["tip"] = d.hub.get_center() + (NEEDLE_L + 0.12) * np.array([np.sin(th), np.cos(th), 0.0])
                state["path"] = ArcBetweenPoints(state["tip"], target, angle=-PI / 2.2)
            b = float(np.clip((a - a0) / max(1e-6, a1 - a0), 0, 1))
            if b < pop:
                s, pos = interpolate(0.2, 1.15, smooth(b / pop)), state["tip"]
            else:
                c = smooth((b - pop) / (1 - pop))
                s, pos = interpolate(1.15, 1.0, c), state["path"].point_from_proportion(c)
            mob.become(tmpl.copy().scale(s).move_to(pos))

        chip.set_opacity(0)
        return UpdateFromAlphaFunc(chip, upd, rate_func=linear)
