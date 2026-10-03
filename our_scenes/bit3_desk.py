"""
Bit3Desk — the desk: each lap the writer sees only what lies on a desk of fixed width.

Starts on bit 2's last frame (the master diagram with the guide at home, the loop lane, six slips on
the row; the blazer bubble and a ? at the top right).
  1 the bubble leaves; the desk tray draws in under the row; the slips make room and the tools guide
    slides down onto the desk's left end as a small card, the job card beside it; «context window»
    under the desk; the writer's view cone covers the desk (never past its ends); the guide, the job,
    the slips light on their words
  2 «حجم محدد» brackets flash at the desk's two ends; «شهر كامل…» a stream of slips comes down from
    the hands and piles at the right end; «مستحيل يساع عليا» they crowd into an overlapping fan that
    hangs off the right end, and shudder
  3 the chip leaves; «أقدم الوراق بتوقع» the oldest slips drop off the desk into the dark below while
    the rest spread back; «ما بقا بشوفا» the cone glows over the desk, the fallen lie dim below it;
    in the silent hold, two quick laps: a new slip lands, an old one drops
  4 «البرنامج اللي حواليه» the hands glow; «دفتر» a notebook flies down and pins at the desk's right
    end (the slips squeeze to make room); «ما بيوقع أبداً» another old slip drops, the notebook stays
  5 «وبيضغط الوراق القديمة» four old slips squeeze into one summary slip, fragments falling out
  6 «قائمة المهام» a to-do card lands at the front; two quick laps, it hops back to the front each
    time; «الهدف» it lights
  7 «بيضيّع تفاصيل» fragments fall from the summary; «انكتب شي غلط» WRONG_NOTE_AR is written into the
    notebook with a dashed outline; «بصير… حقيقة» lap after lap the outline turns solid
  8 «البيّاع… إنسان» the blazer bubble returns, small, above the writer; «الضياع» quick laps, the
    desk's contents drift out of line and dim a little
  9 (bit3_desk.10) «الغرابة» the bubble leaves; «الكرم؟» a discount chip and a ? at the top right
End frame (bit 4 starts here): the master diagram with the desk (guide card + job card at the left,
the summary, slips, the to-do card, the notebook with the solid wrong note at the right end), the
view cone, the lane, the discount chip and ? at the top right. No cursor (bit 2 ends without one).

Render (preview): .venv/bin/manimgl our_scenes/bit3_desk.py Bit3Desk -w -l --video_dir ./media
"""
from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from our_scenes.agent_kit import *  # noqa: F401,F403
from our_scenes.agent_kit import _bar, _card  # noqa: E402  (not exported by *)

# ---------------------------------------------------------------------------
# The desk's layout in this bit (frame 14.2 x 8; keep inside |x| <= 5.9, |y| <= 3.3)
# ---------------------------------------------------------------------------
BASE_Y = -2.45                      # things stand on the desk with their bottom edge here
S_SLIP = 0.76                       # a slip on the desk: SLIP_W 1.1 -> 0.84 wide, 0.40 tall
CARD_H = 0.64                       # the guide card, the job card and the to-do card on the desk
GAP = 0.08                          # between things on the desk
X_LEFT = DESK_X0 + 0.14             # the guide card starts here
X_RIGHT = DESK_X1 - 0.12            # the notebook ends here
NB_W, NB_H = 2.24, 0.92             # the notebook: wide enough for WRONG_NOTE_AR at font size 26
NOTE_SIZE = 26
FLOOR_Y = -3.0                      # where fallen slips lie, below the desk (outside the view cone)
MAX_FALLEN = 5                      # fallen slips that stay (dim); older ones fade into the dark
CHIP_C = np.array([(DESK_X0 + DESK_X1) / 2, -3.03, 0.0])     # «context window», under the desk
TOP_RIGHT = np.array([3.6, 2.6, 0.0])                        # bit 4 opens with the discount chip here
BUBBLE_C = np.array([3.6, 2.72, 0.0])                        # bit 2's blazer bubble (its body centre)
SMALL_BUBBLE_C = np.array([-1.75, 2.38, 0.0])                # the blazer bubble's return, above the writer

Z_CARD, Z_SUM, Z_NB, Z_TODO = 3, 4, 5, 6       # resting things on the desk (slips get 10, 11, 12, ...)
Z_FLY = 1000                                   # things in flight (each its own, newer on top)


def blazer_bubble() -> VGroup:
    """Bit 2's end-frame bubble (bit2_menu.blazer_bubble): a blue blazer in a speech bubble, a ? beside it."""
    bub = speech_bubble(1.5, 1.05, tail="DR")
    bub.shift(BUBBLE_C - bub.body.get_center())
    blz = icon_blazer(0.75).move_to(bub.body)
    q = question_mark(0.6, WARM).next_to(bub.body, RIGHT, buff=0.2)
    out = VGroup(bub, blz, q)
    out.bubble, out.blazer, out.q = bub, blz, q
    return out


def desk_notebook(width: float = NB_W, height: float = NB_H) -> VGroup:
    """The notebook pinned at the desk's right end, wide enough for one written line (the kit's
    notebook, in its colours). Attributes: .page, .pin, .old (an earlier note, abstract)"""
    page = _card(width, height, stroke=INK_2, fill="#1f2636", r=0.06, stroke_width=2.0)
    rings = VGroup(*[Circle(radius=0.035).set_stroke(INK_2, width=1.6).set_fill(BG, 1) for _ in range(8)])
    rings.arrange(RIGHT, buff=0.14).move_to(page.get_top() + 0.06 * DOWN)
    old = text_lines(1.05, n=1, height=0.05, color=INK_2, opacity=0.55, seed=41)
    old.move_to(page.get_corner(DR) + np.array([-0.2 - old.get_width() / 2, 0.11, 0]))
    pin = Dot(radius=0.07).set_fill(TIE, 1).move_to(page.get_corner(UR) + np.array([-0.12, -0.12, 0]))
    out = VGroup(page, old, rings, pin)
    out.page, out.pin, out.old = page, pin, old
    return out


def end_marks() -> VGroup:
    """Brackets at the desk's two ends: its width is fixed."""
    marks = VGroup()
    y0, y1 = -2.8, -1.72
    for x, s in ((DESK_X0, 1), (DESK_X1, -1)):
        pts = [np.array([x + s * 0.18, y1, 0]), np.array([x, y1, 0]), np.array([x, y0, 0]), np.array([x + s * 0.18, y0, 0])]
        br = Polyline(*pts).set_stroke(WARM, width=5).set_fill(opacity=0)
        marks.add(br)
    return marks


def outline_at(ratio: float, width: float, height: float, center, solid: bool = False) -> VMobject:
    """The wrong note's outline: dashes that grow with `ratio` (the same 44, so one stage morphs into
    the next; ratio ~1 looks solid), or the plain solid outline."""
    box = RoundedRectangle(width=width, height=height, corner_radius=0.08).move_to(center)
    if solid:
        box.set_stroke(WARM, width=2.6).set_fill(opacity=0)
        return box
    d = DashedVMobject(box, num_dashes=44, positive_space_ratio=ratio)
    d.set_stroke(WARM, width=2.6).set_fill(opacity=0)
    d.get_bounding_box()        # a Transform copies the target's cached box: make sure it is computed
    return d


class Bit3Desk(AgentScene):
    def construct(self):
        self.continue_from("Bit2Menu")              # the cut from Bit2Menu is seamless
        self.rng = np.random.default_rng(3)
        self._zc, self._fc, self._seed = 9, 0, 100
        self.fallen: list = []
        self.nb_on = False
        self.todo = None

        # ---- bit 2's last frame -------------------------------------------------------------------
        m = master(guide=True, desk_on=True)
        w, h, wd, g = m.writer, m.hands, m.world, m.guide
        self.w, self.h, self.wd = w, h, wd
        lane = behind(loop_lane())
        self.lane = lane
        row = list(row_of_slips(N_ROW))
        for s in row:
            self._as_slip(s)
        bb = blazer_bubble()
        self.add(lane, w, h, m.to_hands, wd, m.to_world, g, *row, bb)
        self.row = row

        desk = m.desk
        view = behind(m.view)
        self.view = view
        job = job_card().scale(CARD_H / 1.1)
        chip = chip_en(CONTEXT_EN, color=INK_2).move_to(CHIP_C)

        # the two fixtures at the desk's left end
        g_scale = CARD_H / g.get_height()
        g_w = g.get_width() * g_scale
        g.home = np.array([X_LEFT + g_w / 2, BASE_Y + CARD_H / 2, 0])
        job.home = np.array([X_LEFT + g_w + GAP + job.get_width() / 2, BASE_Y + CARD_H / 2, 0])
        self.sa0 = job.home[0] + job.get_width() / 2 + 0.12          # the slips start here
        for mob in (g, job):
            mob.ang, mob.dang, mob.doff = 0.0, 0.0, np.zeros(3)
        self.fixed = [g, job]

        # ---- 1. each lap the writer sees only the desk: the guide, the job, the slips so far ----------
        with self.narrate("bit3_desk.1"):
            desk.save_state()
            desk.stretch(0.04, 0).set_opacity(0)
            self.play(FadeOut(bb, scale=0.85), Restore(desk), run_time=0.55)
            self.play(*[self._goto(s, c, scale=S_SLIP) for s, c in zip(row, self._layout(row, self._area()))],
                      run_time=0.6)
            self._lift(g)
            job.target = job.copy().move_to(job.home)
            job.move_to(job.home + 0.45 * UP).set_opacity(0)
            g0 = g.copy()
            pts = [g.get_center(), np.array([-5.4, 2.75, 0]), np.array([-5.5, 0.3, 0]), g.home]   # around the writer

            def glide(mob, a):
                t = smooth(a)
                c = sum(k * (1 - t) ** (3 - i) * t ** i * p for i, (k, p) in enumerate(zip((1, 3, 3, 1), pts)))
                mob.become(g0.copy().scale(1 + (g_scale - 1) * t).move_to(c))
            self.play(UpdateFromAlphaFunc(g, glide), MoveToTarget(job, rate_func=squish_rate_func(smooth, 0.55, 1.0)),
                      run_time=0.85)
            self._rest(g, Z_CARD)
            self._rest(job, Z_CARD)
            self.until("عالطاولة", lead=0.15)
            self.play(FadeIn(chip, scale=0.8), run_time=0.4)
            self.until("قدامو", lead=0.15)
            self.play(FadeIn(view), run_time=0.5)
            self.until("دليل الأدوات", lead=0.12)
            self._pulse(g, ACCENT)
            self.until("والمهمة", lead=0.12)
            self._pulse(job, INK)
            self.until("والوراق", lead=0.12)
            self.play(LaggedStart(*[Indicate(s, scale_factor=1.08, color=ACCENT) for s in self.row], lag_ratio=0.15),
                      run_time=0.9)

        # ---- 2. the desk has a fixed width; a month of emails and chats will never fit ----------------
        with self.narrate("bit3_desk.2"):
            marks = flying(end_marks())
            self.until("حجم", lead=0.2)
            self.play(FadeIn(marks, scale=1.15), run_time=0.3)
            self.until("محدد", lead=0.05)
            self.play(marks.animate(rate_func=there_and_back).set_stroke(INK, width=8), run_time=0.45)
            self.until("شهر", lead=0.3)
            self.play(FadeOut(marks), run_time=0.25)
            stream = [self._mk_slip("result" if k % 3 else "request") for k in range(8)]
            arrive = []
            for k, s in enumerate(stream):
                c = np.array([1.06 + 0.055 * k, BASE_Y + s.dh / 2 + 0.24 + 0.062 * k, 0])
                ang = (-1) ** k * (0.05 + 0.012 * k)
                arrive.append(self._from_hands(s, c, ang))
            self.play(LaggedStart(*arrive, lag_ratio=0.3), run_time=self.to("مستحيل", lead=0.2, minimum=1.6))
            # it can't fit: everything crowds into one overlapping fan that hangs off the right end
            crowd = self.row + stream
            n = len(crowd)
            x_first = self.sa0 + crowd[0].dw / 2
            x_last = DESK_X1 + 0.28 - crowd[-1].dw / 2
            fan = []
            for i, s in enumerate(crowd):
                x = x_first + (x_last - x_first) * i / (n - 1)
                tilt = -0.13 * max(0, i - (n - 4))           # the last three tip over the edge
                y = BASE_Y + s.dh / 2 + (0.03 if i % 2 else 0.0) + 0.05 * max(0, i - (n - 4))
                fan.append(self._goto(s, np.array([x, y, 0]), ang=tilt))
            self.play(*fan, run_time=0.55)
            self.row = crowd
            self.until("يساع", lead=0.1)
            self.play(*[s.animate(rate_func=lambda t: wiggle(t, 4)).shift(0.05 * RIGHT) for s in crowd[-7:]],
                      run_time=0.5)

        # ---- 3. so something has to go: the oldest slips drop off and the writer can't see them ------
        with self.narrate("bit3_desk.3", pause=line_pause("bit3_desk.3") + 2.0):
            self.play(FadeOut(chip), run_time=0.35)
            n_drop = len(self.row) - N_ROW
            olds, keep = self.row[:n_drop], self.row[n_drop:]
            self.until("ينشال", lead=0.2)
            self.play(*[s.animate(rate_func=lambda t: wiggle(t, 3)).shift(0.04 * UP) for s in olds], run_time=0.4)
            self.until("أقدم", lead=0.15)
            falls = [self._fall(s, vanish=k < n_drop - MAX_FALLEN) for k, s in enumerate(olds)]
            spread = [self._goto(s, c, ang=0.0) for s, c in zip(keep, self._layout(keep, self._area()))]
            self.row = keep
            self.play(LaggedStart(*falls, lag_ratio=0.12), *spread,
                      run_time=max(1.0, min(1.7, self.to("والكاتب", lead=0.25))))
            self._drop_vanished()
            self.until("والكاتب", lead=0.1)
            self.play(view.animate(rate_func=there_and_back).set_fill(ACCENT, opacity=0.22),
                      *[f.animate.fade(0.25) for f in self.fallen], run_time=0.8)
            # the silent hold: around it goes; each lap a new slip lands and an old one drops
            if self.line_left() > 0.01:
                self.wait(self.line_left())
            self._laps(2, 0.95)

        # ---- 4. the program around it keeps a notebook on the desk that never falls off --------------
        nb = desk_notebook()
        nb.home = np.array([X_RIGHT - NB_W / 2, BASE_Y + NB_H / 2, 0])
        nb.ang, nb.dang, nb.doff = 0.0, 0.0, np.zeros(3)
        self.nb = nb
        with self.narrate("bit3_desk.4"):
            self.until("البرنامج", lead=0.15)
            halo = h.box.copy().set_fill(opacity=0).set_stroke(INK, width=12, opacity=0.3)
            self.play(h.box.animate(rate_func=there_and_back).set_stroke(INK, width=4.6),
                      h.mark.animate(rate_func=there_and_back).set_fill(INK),
                      FadeIn(halo, rate_func=there_and_back), run_time=1.0)
            self.remove(halo)
            self.until("دفتر", lead=0.5)
            nb.target = nb.copy().move_to(nb.home)
            nb.scale(0.3).move_to(HANDS_C).set_opacity(0)
            self._lift(nb)
            self.nb_on = True
            squeeze = [self._goto(s, c) for s, c in zip(self.row, self._layout(self.row, self._area()))]
            self.play(MoveToTarget(nb, path_arc=-0.6), *squeeze, run_time=0.7)
            self._rest(nb, Z_NB)
            self.fixed.append(nb)
            self.play(Indicate(nb.pin, scale_factor=1.9, color=TIE), run_time=0.35)
            self.until("ما بيوقع", lead=0.1)
            old = self.row[0]
            self.row = self.row[1:]
            spread = [self._goto(s, c) for s, c in zip(self.row, self._layout(self.row, self._area()))]
            self.play(self._fall(old), *spread, Indicate(nb.pin, scale_factor=1.7, color=TIE),
                      *self._trim_fallen(), run_time=0.65)
            self._drop_vanished()

        # ---- 5. ... squeezes old slips into a short summary ...---------------------------------------
        with self.narrate("bit3_desk.5"):
            four, rest = self.row[:4], self.row[4:]
            summ = self._mk_slip("result", n_lines=3)
            summ.role = "summary"
            summ.set_z_index(Z_SUM)
            new_row = [summ] + rest
            cs = self._layout(new_row, self._area())
            summ.move_to(cs[0])
            mid = np.array([cs[0][0], four[0].get_y(), 0])
            press = []
            for s in four:
                s.generate_target()
                s.target.stretch(0.45, 0).move_to(mid)
                press.append(MoveToTarget(s))
            self.play(*press, run_time=self.to("بملخّص", lead=0.3, minimum=0.6))
            bits, drops = self._fragments(mid, 9, seed=5)
            self.play(*[FadeOut(s, scale=0.8) for s in four], FadeIn(summ, scale=0.6), LaggedStart(*drops, lag_ratio=0.08),
                      run_time=0.6)
            self.remove(*bits)
            self.row = new_row
            self.play(*[self._goto(s, c) for s, c in zip(self.row[1:], cs[1:])], run_time=0.45)

        # ---- 6. ... and puts the to-do list back in front every lap, so the goal stays in view -------
        with self.narrate("bit3_desk.6"):
            todo = todo_card().scale(CARD_H / 1.1)
            todo.dw, todo.dh, todo.role, todo.ang, todo.dang, todo.doff = todo.get_width(), todo.get_height(), "todo", 0.0, 0.0, np.zeros(3)
            self.until("قائمة المهام", lead=0.3)
            row6 = self.row + [todo]
            cs = self._layout(row6, self._area())
            todo.set_z_index(Z_TODO)
            self.play(self._from_hands(todo, cs[-1], 0.0, a0=0.0, a1=1.0), run_time=0.65)
            self._rest(todo, Z_TODO)
            self.row, self.todo = row6, todo
            self._laps(2, 0.72, hop=True)
            self.until("الهدف", lead=0.15)
            self._pulse(todo, ACCENT, run_time=0.65)

        # ---- 7. every summary drops details; a wrong line in the notebook sits on the desk as fact -----
        with self.narrate("bit3_desk.7"):
            self.until("بيضيّع", lead=0.15)
            bits, drops = self._fragments(summ.get_center(), 9, seed=9)
            self.play(LaggedStart(*drops, lag_ratio=0.1), summ.animate(rate_func=there_and_back).shift(0.04 * DOWN),
                      run_time=0.8)
            self.remove(*bits)
            note = ar_text(WRONG_NOTE_AR, font_size=NOTE_SIZE, color=INK)
            slot = nb.page.get_top() + 0.48 * DOWN
            note.move_to(slot)
            ow, oh = note.get_width() + 0.08, 0.46
            ratios = [0.42, 0.62, 0.82, 0.997]
            box = outline_at(ratios[0], ow, oh, slot)
            box.set_z_index(Z_NB + 1)
            note.set_z_index(Z_NB + 1)
            self.until("انكتب", lead=0.2)
            self.play(ShowCreation(box), run_time=0.35)
            self.play(write_rtl(note), run_time=max(0.7, min(1.1, self.to("بصير", lead=0.25))))
            self.remove(box, note)
            nb.add(box, note)                       # the note and its outline belong to the notebook now
            self.add(nb)
            nb.note, nb.box = note, box
            self.until("بصير", lead=0.12)
            for k in range(3):
                nxt = outline_at(ratios[k + 1], ow, oh, slot)
                self._laps(1, 0.62, extra=[Transform(box, nxt)], dot_fade=(k == 2))
            solid = outline_at(1.0, ow, oh, slot, solid=True)
            nb.remove(box)
            self.remove(box)
            nb.add(solid)
            nb.box = solid
            self.add(nb)
            self.play(solid.animate(rate_func=there_and_back).set_stroke(width=5.5), run_time=0.45)

        # ---- 8. nobody knows exactly why it decided it was a person; long jobs drift ------------------
        bub2 = speech_bubble(1.25, 0.9, tail="DL")
        bub2.shift(SMALL_BUBBLE_C - bub2.body.get_center())
        blz2 = icon_blazer(0.6).move_to(bub2.body)
        small = VGroup(bub2, blz2)
        with self.narrate("bit3_desk.8"):
            self.until("البيّاع", lead=0.3)
            self.play(FadeIn(small, scale=0.6, shift=0.1 * UP), run_time=0.45)
            self.until("بس هاد", lead=0.1)
            per = max(0.6, min(0.95, (self.hold_left() - 0.35) / 4))
            self._laps(4, per, drift=True)

        # ---- 9. that explains the strange; not the generous: why yes to every discount? --------------
        pct = icon_percent(0.6).move_to(TOP_RIGHT)
        q = question_mark(0.7).next_to(pct, RIGHT, buff=0.18)
        with self.narrate("bit3_desk.10"):
            self.play(FadeOut(small, scale=0.8), *[FadeOut(f) for f in self.fallen], run_time=0.45)
            self.fallen = []
            self.until("بس الكرم", lead=0.15)
            self.play(FadeIn(pct, scale=0.5), run_time=0.4)
            self.play(FadeIn(q, scale=0.5, shift=0.1 * UP), run_time=0.35)
            self.until("خصم", lead=0.15)
            self.play(pct.animate(rate_func=there_and_back).scale(1.15), run_time=0.5)

    # ------------------------------------------------------------------ desk bookkeeping
    def _as_slip(self, s: Mobject, role: str = "slip") -> Mobject:
        """Tag a slip for the desk (its size on the desk, its tilt, its own z so newer lies on top)."""
        s.dw, s.dh = SLIP_W * S_SLIP, s.get_height() * S_SLIP / max(1e-6, s.get_width() / SLIP_W)
        s.role, s.ang, s.dang, s.doff = role, 0.0, 0.0, np.zeros(3)
        self._zc += 1
        s.set_z_index(self._zc)
        return s

    def _mk_slip(self, kind: str = "result", n_lines: int = 2) -> VGroup:
        self._seed += 1
        s = slip(kind=kind, width=SLIP_W, n_lines=n_lines, seed=self._seed).scale(S_SLIP)
        self._as_slip(s)
        s.dw, s.dh = s.get_width(), s.get_height()
        return s

    def _area(self) -> tuple[float, float]:
        """The part of the desk the slips (and the summary and the to-do card) may use."""
        x1 = (X_RIGHT - NB_W - 0.1) if self.nb_on else X_RIGHT
        return self.sa0, x1

    @staticmethod
    def _width(items, gap: float = GAP) -> float:
        return sum(m.dw for m in items) + gap * max(0, len(items) - 1)

    def _layout(self, items, area) -> list:
        """Centres for items laid left (oldest) to right (newest) from the area's left edge, bottoms on
        BASE_Y; when they don't fit they overlap evenly up to the area's right edge."""
        x0, x1 = area
        n = len(items)
        if n == 0:
            return []
        tot = sum(m.dw for m in items)
        gap = GAP if (n == 1 or tot + GAP * (n - 1) <= x1 - x0 + 1e-6) else (x1 - x0 - tot) / (n - 1)
        out, x = [], x0
        for mob in items:
            out.append(np.array([x + mob.dw / 2, BASE_Y + mob.dh / 2, 0]) + mob.doff)
            x += mob.dw + gap
        return out

    def _lift(self, mob: Mobject) -> None:
        self._fc += 1
        mob.set_z_index(Z_FLY + self._fc)
        self.add(mob)

    def _rest(self, mob: Mobject, z: int) -> None:
        mob.set_z_index(z)
        self.add(mob)

    # ------------------------------------------------------------------ animations
    def _goto(self, mob: Mobject, center, ang: float | None = None, scale: float | None = None,
              fade: float | None = None, path_arc: float = 0.0, rate_func=smooth) -> Animation:
        """Move a desk item to `center` (tilted to `ang`), as one MoveToTarget."""
        ang = mob.ang if ang is None else ang
        mob.generate_target()
        if scale is not None:
            mob.target.scale(scale)
        if abs(ang - mob.ang) > 1e-9:
            mob.target.rotate(ang - mob.ang)
        mob.target.move_to(center)
        if fade:
            mob.target.fade(fade)
        mob.ang = ang
        return MoveToTarget(mob, path_arc=path_arc, rate_func=rate_func)

    def _from_hands(self, mob: Mobject, center, ang: float = 0.0, a0: float = 0.0, a1: float = 1.0) -> Animation:
        """A new thing comes out of the hands and lands at `center` on the desk."""
        mob.generate_target()
        if abs(ang) > 1e-9:
            mob.target.rotate(ang)
        mob.target.move_to(center)
        mob.ang = ang
        mob.scale(0.3).move_to(HANDS_C + 0.25 * DOWN).set_opacity(0)
        return MoveToTarget(mob, path_arc=-0.5, rate_func=squish_rate_func(smooth, a0, a1))

    def _fall(self, mob: Mobject, vanish: bool = False, a0: float = 0.0, a1: float = 1.0) -> Animation:
        """A slip drops off the desk into the dark below it (dim, or gone)."""
        rng = self.rng
        x = float(np.clip(mob.get_x() + rng.uniform(-0.25, 0.25), self.sa0, 1.2))
        y = FLOOR_Y + rng.uniform(-0.05, 0.05)
        ang = rng.uniform(-0.35, 0.35)
        mob.generate_target()
        mob.target.rotate(ang - mob.ang).scale(0.85).move_to(np.array([x, y, 0]))
        mob.target.fade(1.0 if vanish else 0.62)
        mob.ang = ang
        mob.vanish = vanish
        self.fallen.append(mob)
        return MoveToTarget(mob, rate_func=squish_rate_func(rush_into, a0, a1))

    def _drop_vanished(self) -> None:
        gone = [f for f in self.fallen if getattr(f, "vanish", False)]
        self.remove(*gone)
        self.fallen = [f for f in self.fallen if not getattr(f, "vanish", False)]

    def _trim_fallen(self) -> list:
        """Fallen slips beyond MAX_FALLEN fade into the dark."""
        live = [f for f in self.fallen if not getattr(f, "vanish", False)]
        extra = live[:-MAX_FALLEN] if len(live) > MAX_FALLEN else []
        anims = []
        for f in extra:
            f.vanish = True
            anims.append(f.animate.fade(1.0))
        return anims

    def _fragments(self, center, n: int, seed: int = 0):
        """Small bars (details) falling out of a summary: (the bars, their animations)."""
        rng = np.random.default_rng(seed)
        bits, anims = [], []
        for k in range(n):
            b = _bar(rng.uniform(0.15, 0.3), 0.065, INK_2 if k % 3 else WARM, 0.95)
            b.move_to(np.array(center) + np.array([rng.uniform(-0.32, 0.32), rng.uniform(-0.12, 0.12), 0]))
            self._lift(b)
            b.generate_target()
            b.target.shift(np.array([rng.uniform(-0.55, 0.55), -rng.uniform(0.8, 1.1), 0]))
            b.target.rotate(rng.uniform(-1.2, 1.2)).set_opacity(0)
            bits.append(b)
            anims.append(MoveToTarget(b, rate_func=rush_into))
        return bits, anims

    def _pulse(self, mob: Mobject, color=ACCENT, run_time: float = 0.6) -> None:
        """Light a thing up: it swells a little inside a ring of colour."""
        halo = RoundedRectangle(width=mob.get_width() + 0.18, height=mob.get_height() + 0.18, corner_radius=0.1)
        halo.move_to(mob).set_stroke(color, width=3.5).set_fill(opacity=0)
        self._lift(halo)
        self.play(mob.animate(rate_func=there_and_back).scale(1.1),
                  FadeIn(halo, scale=0.95, rate_func=there_and_back), run_time=run_time)
        self.remove(halo)

    def _laps(self, n: int, per: float, hop: bool = False, drift: bool = False, extra: list | None = None,
              dot_fade: bool = True) -> None:
        """n quick laps: a dot runs the loop lane, an envelope goes out to the world and back, a new slip
        lands; when the slips no longer fit, the oldest plain slip drops off (the summary, the to-do card
        and the fixtures stay). hop: the new slip lands at the very front and the to-do card hops back
        over it. drift: everything on the desk tilts and shifts a little more and dims a little."""
        if getattr(self, "dot", None) is None:
            self.dot = behind(Dot(radius=0.09).set_fill(ACCENT, 1).move_to(self.lane.path.get_start()))
            self.add(self.dot)
        env_tpl = envelope(0.42, INK_2)
        for k in range(n):
            rng = self.rng
            new = self._mk_slip("result")
            row = list(self.row)
            if self.todo is not None and not hop:
                row.insert(row.index(self.todo), new)
            else:
                row.append(new)
            drops = []
            area = self._area()
            while self._width(row) > area[1] - area[0] + 1e-6:
                old = next(mob for mob in row if mob.role == "slip" and mob is not new)
                row.remove(old)
                drops.append(old)
            if drift:
                for mob in row + self.fixed:
                    if mob is new:
                        mob.dang, mob.doff = rng.uniform(-0.06, 0.06), np.array([0, rng.uniform(-0.02, 0.02), 0])
                    else:
                        mob.dang += rng.uniform(-0.028, 0.028)
                        mob.doff = mob.doff + np.array([rng.uniform(-0.02, 0.02), rng.uniform(-0.014, 0.014), 0])
            cs = self._layout(row, area)
            target_world = self.wd.supplier if (self._seed % 2) else self.wd.customers
            env = flying(env_tpl.copy().scale(0.001).move_to(self.h.get_center()))
            a, b = self.h.get_right() + 0.12 * RIGHT, target_world.get_center()

            def env_upd(mob, alpha, a=a, b=b):
                t = float(np.clip((alpha - 0.1) / 0.42, 0, 1))
                sc = 1.0 if 0 < t < 1 else 0.001
                mob.become(env_tpl.copy().scale(sc).move_to(a + (b - a) * there_and_back(t)))

            land = squish_rate_func(smooth, 0.45, 0.95)
            anims = [MoveAlongPath(self.dot, self.lane.path, rate_func=linear), UpdateFromAlphaFunc(env, env_upd)]
            anims.append(self._from_hands(new, cs[row.index(new)], new.dang, a0=0.42, a1=0.95))
            for mob, c in zip(row, cs):
                if mob is new:
                    continue
                anims.append(self._goto(mob, c, ang=mob.dang if drift else None, fade=0.06 if drift else None,
                                        rate_func=land))
            if drift:
                for mob in self.fixed:
                    anims.append(self._goto(mob, mob.home + mob.doff, ang=mob.dang, fade=0.06, rate_func=land))
            for d in drops:
                anims.append(self._fall(d, a0=0.4, a1=1.0))
            anims += self._trim_fallen()
            if extra and k == n - 1:
                anims += extra
            self.add(env)
            self.play(*anims, run_time=per)
            self.remove(env)
            self._drop_vanished()
            self.row = row
            if hop and self.todo is not None:
                # the to-do card hops back over the new slip to the front
                row2 = [mob for mob in row if mob is not self.todo] + [self.todo]
                cs2 = self._layout(row2, area)
                self._lift(self.todo)
                anims = [self._goto(mob, c) for mob, c in zip(row2, cs2) if mob is not self.todo]
                anims.append(self._goto(self.todo, cs2[-1], path_arc=-1.6))
                self.play(*anims, run_time=0.38)
                self._rest(self.todo, Z_TODO)
                self.row = row2
        if dot_fade:
            self.play(FadeOut(self.dot), run_time=0.2)
            self.dot = None
