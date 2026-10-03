"""
Bit1Loop — the writer and its hands: write, do, read, round and round.

The master layout (agent_kit): the writer (teal) left, the hands (grey program) right of it, the world
(amber: the fridge, the supplier, the customers) at the right edge. What the writer reads lies on a row
under it (bit 3 turns the row into the desk). The loop is a closed lane: writer -> hands (the request),
hands -> down to the row (the result), along the row and back up into the writer (it reads).
  1 the hook's cursor shrinks into the writer; the slips in front of it; it reads them, writes on
  2 it writes the request slip, word for word (REQUEST_SLIP_AR)
  3 the slip can't go anywhere by itself; the hands appear; the slip goes in; an envelope to the supplier
  4 the supplier's reply comes back; the hands turn it into a result slip that lands in front of the writer
  5 it reads it and writes the next request: two more laps (customers, supplier), faster
  6 write / do / read light in turn; the loop lane is traced; the chip «AI Agent» on "agent"
  7 a day in the shop: a clock runs through a day while ~20 laps blur by (+3 s hold)
  8 the request slip again, an envelope and a question mark: how did it know it could ask for email?

Render (preview): .venv/bin/manimgl our_scenes/bit1_loop.py Bit1Loop -w -l --video_dir ./media
"""
from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from our_scenes.agent_kit import *  # noqa: F401,F403

LAP_S = 0.3 + 0.4 + 0.4 + 0.2 + 0.4 + 0.2 + 0.55      # one lap at speed 1 (see _lap)
N_SLOTS = N_ROW                            # slips the row shows before the oldest slide off (bit 3's subject)


class Bit1Loop(AgentScene):
    def construct(self):
        self.continue_from("HookShop")              # the cut from HookShop is seamless
        self.row = []                                  # result / request slips lying in front of the writer
        m = master()
        w, h, wd = m.writer, m.hands, m.world
        self.w, self.h, self.wd = w, h, wd
        cur = cursor(0.58).move_to(CUR_POS)
        self.cur = cur
        big = cursor(1.9).move_to(np.array([-1.9, 0.45, 0]))     # the hook's last frame: its big cursor
        self.add(big)

        # ---- 1. inside, the same writer: it reads everything in front of it, writes what comes next ----
        with self.narrate("bit1_loop.1"):
            self.play(ReplacementTransform(big, cur), FadeIn(w, scale=0.85), run_time=0.9)
            old = [slip(kind=k, width=SLIP_W, seed=s) for k, s in (("request", 1), ("result", 2), ("result", 3))]
            for s in old:
                self._place_new(s)
            self.until("بيقرا", lead=0.35)
            self.play(LaggedStart(*[FadeIn(s, shift=0.15 * UP) for s in old], lag_ratio=0.2), run_time=0.6)
            cone = self._cone()
            self.play(FadeIn(cone), LaggedStart(*[Indicate(s, scale_factor=1.06, color=ACCENT) for s in old], lag_ratio=0.25),
                      run_time=min(1.2, max(0.6, self.to("وبيكتب", lead=0.15))))
            self.play(FadeOut(cone), run_time=0.3)
            self.until("وبيكتب", lead=0.1)
            self.play(blink(cur, n=2, period=0.35), run_time=0.7)

        # ---- 2. so it writes a request, word for word ----------------------------------------------
        with self.narrate("bit1_loop.2"):
            req = flying(slip(REQUEST_SLIP_AR, kind="request", font_size=32).move_to(REQ_POS))
            self.play(FadeIn(req.card), FadeIn(req.edge), cur.animate.next_to(req.card, RIGHT, buff=0.12), run_time=0.4)
            self.play(write_rtl(req.content), run_time=max(1.0, self.line_left() - 0.2))
            self.play(cur.animate.move_to(CUR_POS), run_time=0.3)

        # ---- 3. it can't send anything; next to it, the hands; they do exactly that ----------------
        with self.narrate("bit1_loop.3"):
            stub = DashedLine(req.get_right() + 0.15 * RIGHT, np.array([5.6, REQ_POS[1], 0]), dash_length=0.12)
            stub.set_stroke(INK_2, width=2.5, opacity=0.7)
            x = icon_cross(0.32).move_to(stub.get_end() + 0.3 * LEFT)
            self.play(ShowCreation(stub), run_time=0.5)
            self.play(FadeIn(x, scale=1.5), req.animate.shift(0.12 * RIGHT), rate_func=there_and_back, run_time=0.5)
            self.play(FadeOut(stub), FadeOut(x), run_time=0.3)
            self.until("برنامج", lead=0.3)
            self.play(FadeIn(h, scale=0.85), GrowArrow(m.to_hands), run_time=0.7)
            self.until("بيقرا", lead=0.25)
            self.play(req.animate.scale(0.22).move_to(h.get_center()).set_opacity(0.0), run_time=0.7)
            self.remove(req)
            self.play(h.box.animate.set_stroke(INK, width=3.4), rate_func=there_and_back, run_time=0.35)
            self.until("وبينفّذو", lead=0.4)
            self.play(FadeIn(wd, shift=0.2 * LEFT), GrowArrow(m.to_world), run_time=0.6)
            self._envelope(h.get_center(), wd.supplier.get_center(), run_time=0.8)
            self.play(Indicate(wd.supplier, color=WARM, scale_factor=1.15), run_time=0.5)

        # ---- 4. the supplier's reply comes back as text and lands in front of the writer ------------
        with self.narrate("bit1_loop.4"):
            self._envelope(wd.supplier.get_center(), h.get_center(), run_time=0.8, color=WARM)
            res = flying(slip(kind="result", width=SLIP_W, seed=4))
            self.until("مكتوب", lead=0.35)
            self.play(FadeIn(res.move_to(h.get_center()), scale=0.3), run_time=0.35)
            self.until("قدام", lead=0.3)
            self._land(res, run_time=0.8)

        # ---- 5. it reads it, writes the next request, and around it goes ---------------------------
        with self.narrate("bit1_loop.5"):
            cone = self._cone()
            self.play(FadeIn(cone), Indicate(res, color=ACCENT, scale_factor=1.08), run_time=0.6)
            self.play(FadeOut(cone), run_time=0.25)
            self.until("بيكتب", lead=0.2)
            s1 = max(1.0, LAP_S * (1 + 1 / 1.6) / max(0.5, self.hold_left() - 0.25))   # both laps fit the line + pause
            self._lap(wd.customers, speed=s1, seed=5)
            self._lap(wd.supplier, speed=1.6 * s1, seed=6)

        # ---- 6. write, do, read: that loop is what's called an AI agent ----------------------------
        with self.narrate("bit1_loop.6"):
            self.play(w.box.animate.set_stroke(INK, width=5), rate_func=there_and_back, run_time=min(0.5, self.to("بينفّذ")))
            self.until("بينفّذ", lead=0.1)
            self.play(h.box.animate.set_stroke(INK, width=5), rate_func=there_and_back, run_time=min(0.5, self.to("بيقرا")))
            self.until("بيقرا", lead=0.1)
            cone = self._cone(0.18)
            self.play(FadeIn(cone), rate_func=there_and_back, run_time=0.55)
            self.remove(cone)
            lane = behind(loop_lane())                      # the lane runs behind the boxes
            self.until("هالدورة", lead=0.2)
            self.play(ShowCreation(lane[0]), FadeIn(lane[1]), run_time=0.9)
            chip = chip_en(AGENT_EN, height=0.7).move_to(np.array([(WRITER_C[0] + HANDS_C[0]) / 2, (LANE_Y + WRITER_C[1]) / 2, 0]))
            self.until("agent", lead=0.2)
            self.play(FadeIn(chip, scale=0.7), run_time=0.45)
            self.lane, self.chip = lane, chip

        # ---- 7. a day in the shop is this loop, hundreds of times ----------------------------------
        with self.narrate("bit1_loop.7", pause=line_pause("bit1_loop.7") + 3.0):
            clock = icon_clock(1.3).move_to(np.array([4.6, 2.55, 0]))
            self.play(FadeIn(clock, scale=0.7), FadeOut(chip), run_time=0.4)
            n = 20
            deadline = self.time + self.hold_left() - 0.4      # then the dot fades; each play re-measures the
                                                                # time left, so frame rounding can't add up
            dot = behind(Dot(radius=0.1).set_fill(ACCENT, 1).move_to(lane.path.get_start()))
            self.add(dot)
            for k in range(n):
                target = wd.supplier if k % 2 else wd.customers
                env = flying(envelope(0.4, WARM if k % 2 else INK_2).move_to(h.get_center()))
                new = slip(kind="result", width=SLIP_W, seed=20 + k)
                self._place_new(new)
                new.set_opacity(0)
                anims = [MoveAlongPath(dot, lane.path, rate_func=linear),
                         Succession(env.animate.move_to(target.get_center()), env.animate.move_to(h.get_center()).set_opacity(0)),
                         new.animate.set_opacity(1),
                         Rotate(clock.hour, -TAU / n * 2, about_point=clock.face.get_center()),
                         Rotate(clock.minute, -TAU * 24 / n / 6, about_point=clock.face.get_center())]
                anims += self._shift_row_anims()
                self.add(env)
                per = max(1 / 30, (deadline - self.time) / (n - k))
                self.play(*anims, run_time=per, rate_func=linear)
                self.remove(env)
            self.play(FadeOut(dot), run_time=max(0.1, min(0.3, self.hold_left() - 0.02)))

        # ---- 8. but how did it know email was something it could ask for? -------------------------
        with self.narrate("bit1_loop.8"):
            req = slip(REQUEST_SLIP_AR, kind="request", font_size=32).move_to(REQ_POS)
            env = envelope(0.8, INK).next_to(req, LEFT, buff=0.4)
            q = question_mark(0.85, WARM).next_to(env, UP, buff=0.12)
            self.play(FadeIn(req, shift=0.15 * DOWN), FadeOut(clock), run_time=0.5)
            self.play(FadeIn(env, scale=0.6), run_time=0.35)
            self.play(FadeIn(q, scale=0.5, shift=0.1 * UP), run_time=0.4)

    # ------------------------------------------------------------------ helpers
    def _place_new(self, s: Mobject) -> None:
        """Give slip s the next place on the row (not animated); the row keeps N_SLOTS, newest at the right."""
        self.row.append(s)
        k = len(self.row) - 1
        s.move_to(desk_slot(min(k, N_SLOTS - 1), N_SLOTS))

    def _shift_row_anims(self) -> list:
        """When the row is over full: everything slides one place left and the oldest fades off the edge."""
        if len(self.row) <= N_SLOTS:
            return []
        anims = []
        live = self.row[-N_SLOTS - 1:]
        for i, s in enumerate(live):
            if i == 0:
                anims.append(s.animate.shift(1.0 * LEFT).set_opacity(0))
            elif s is not self.row[-1]:
                anims.append(s.animate.move_to(desk_slot(i - 1, N_SLOTS)))
        self.row = self.row[-N_SLOTS:]
        return anims

    def _cone(self, opacity: float = 0.12) -> VMobject:
        xs = [s.get_left()[0] for s in self.row] + [s.get_right()[0] for s in self.row] or [WRITER_C[0]]
        left, right = min(xs) - 0.1, max(xs) + 0.1
        top_l, top_r = self.w.get_corner(DL) + 0.2 * RIGHT, self.w.get_corner(DR) + 0.2 * LEFT
        cone = Polygon(top_l, top_r, np.array([right, SLIP_Y + 0.3, 0]), np.array([left, SLIP_Y + 0.3, 0]))
        cone.set_fill(ACCENT, opacity=opacity).set_stroke(width=0)
        return cone

    def _envelope(self, a, b, run_time: float = 0.6, color=INK_2, fade: float = 0.2) -> None:
        env = flying(envelope(0.5, color).move_to(a))
        self.add(env)
        self.play(env.animate.move_to(b), run_time=run_time)
        self.play(FadeOut(env, scale=0.5), run_time=fade)

    def _land(self, s: Mobject, run_time: float = 0.7) -> None:
        """Slip s (at the hands) drops onto the next place on the row."""
        self.row.append(s)
        k = len(self.row) - 1
        target = desk_slot(min(k, N_SLOTS - 1), N_SLOTS)
        path = ArcBetweenPoints(s.get_center(), target, angle=-PI / 3)
        self.play(MoveAlongPath(s, path), *self._shift_row_anims(), run_time=run_time)

    def _lap(self, target: Mobject, speed: float = 1.0, seed: int = 0) -> None:
        """One lap at `speed`: a request is written, goes into the hands, out to the world and back,
        and the result drops onto the row."""
        r = flying(slip(kind="request", width=SLIP_W, seed=seed).move_to(CUR_POS + np.array([0.35, 0.45, 0])))
        self.play(FadeIn(r, scale=0.5), blink(self.cur, n=1, period=0.3 / speed), run_time=0.3 / speed)
        self.play(r.animate.scale(0.3).move_to(self.h.get_center()).set_opacity(0), run_time=0.4 / speed)
        self.remove(r)
        self._envelope(self.h.get_center(), target.get_center(), run_time=0.4 / speed, fade=0.2 / speed)
        self._envelope(target.get_center(), self.h.get_center(), run_time=0.4 / speed, color=WARM, fade=0.2 / speed)
        res = flying(slip(kind="result", width=SLIP_W, seed=seed + 50).move_to(self.h.get_center()))
        self.add(res)
        self._land(res, run_time=0.55 / speed)
