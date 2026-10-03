"""
Bit7Exit — the recap: the finished master diagram lights part by part as it's named, the loop turns
once; it now runs inside apps on a phone; next video's dial; video 2's end card.

Starts on bit 6's end, dimmed (the finished master diagram at ~25%: guide, writer, hands, world,
desk with four slips and the notebook, the view, the loop lane). Each part lights to full as it's named.
  1 «الإيجنت هوي كاتب» the writer lights, its cursor comes on and blinks; «جوّا دورة» the lane lights
    and a dot runs once around it
  2 «دليل» the tools guide lights (fast: the line is short); a reading frame runs down its rows
  3 «طاولة بتتعبّى» the desk and its slips light and one more slip lands; «ودفتر بيحفظ فيه المهم» the
    notebook lights and two lines are written into it
  4 «وإيدين» the hands light; «برنامج…» a request slip goes in, an envelope out to the world (the world
    lights); in the +2 s hold the loop turns once, everything lit: the reply comes back, a result slip
    lands on the desk (the oldest slides off its left end), the writer reads it, writes the next
    request, and out it goes
  5 «وهالدورة» a dot runs the loop once more; «جوا تطبيقات فيك تراسلا من موبايلك» the diagram
    shrinks to the left half; a phone (plain silhouette) slides in on the right with a chat thread of
    wordless bubbles, a small copy of the loop turning behind it
  6 «وبالفيديو الجايي» everything fades; «كيف بتدرّب آلة بزر اللايك؟» bit 4's dial returns at the
    centre, two thumbs-ups drop in and press its needle further toward yes; a question mark: the
    teaser for video 4
  7 «حط لايك واشترك بالقناة» video 2's end card: the dial steps back and up, the like pops in on
    «لايك», the red subscribe pill on «اشترك» and ripples; the pause fades to black

Render (preview): .venv/bin/manimgl our_scenes/bit7_exit.py Bit7Exit -w -l --video_dir ./media
"""
from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from our_scenes.agent_kit import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Layout (frame 14.2 x 8; keep inside |x| <= 5.9, |y| <= 3.3)
# ---------------------------------------------------------------------------
DIM = 0.25                                       # bit 6's finished diagram, dimmed
LIGHT_T = 0.4                                    # a part lights to full
N_START = 4                                      # slips on the desk at the start (row_of_slips(4))
N_FRONT = 5                                      # slips that fit in front of the notebook
NB_C = np.array([DESK_X1 - 0.6, -1.98, 0.0])     # the notebook at the desk's right end, its top under the lane
NB_Z = 1                                         # ... drawn over the desk's edges (they'd cross its page)
REQ_START = CUR_POS + np.array([0.68, 0.40, 0])  # a request slip appears by the cursor, clear of the guide

SMALL = 0.62                                     # beat 5: the diagram shrinks to the left half ...
SMALL_C = np.array([-2.30, 0.25, 0.0])           # ... centred here (x -5.9 .. 1.3)
PHONE_H = 3.4
PHONE_C = np.array([3.60, 0.05, 0.0])
RING_R = 1.32                                    # a small copy of the loop turning behind the phone
RING_SPIN = 0.9                                  # rad / s, clockwise

DIAL_R = 1.7                                     # beat 6: bit 4's dial
DIAL_HUB = np.array([-0.45, -0.35, 0.0])
DIAL_V = 0.9
THUMB_A = np.array([-0.25, 0.98, 0.0])           # two thumbs-ups inside the dial, pressing on the needle
THUMB_B = np.array([0.47, 0.66, 0.0])            # ... (offsets from the hub)
THUMB_H = (0.74, 0.60)
PUSH = 0.16                                      # how far a thumb presses (across the needle)
Q_C = np.array([2.70, 0.90, 0.0])                # a question mark beside it (offset from the hub)

# The end card (video 2's, ../ai-image-explainer/our_scenes/bit5_exit.py, adapted)
OUTRO_SCALE = 0.90                               # the dial steps back and up ...
OUTRO_STILL_C = np.array([0.0, 0.85, 0.0])
OUTRO_MOVE_T = 0.9                               # ... under the line's first words
OUTRO_ROW_C = np.array([0.0, -1.55, 0.0])        # the like + subscribe row, under it
OUTRO_GAP = 0.65
LIKE_H = 0.62
PILL_W, PILL_H = 2.4, 0.72                       # video 1's subscribe pill ...
LIKE_BLUE, YT_RED = "#3EA6FF", "#FF0000"         # ... and its end card's colours
POP_IN_T = 0.35                                  # each piece pops in on its word ...
POP_LEAD = 0.12                                  # ... starting this much before it
RIPPLES, RIPPLE_T, RIPPLE_GAP = 2, 1.0, 0.15     # then the pill invites: a soft ring leaves it, twice
RIPPLE_GROW = 0.24
END_FADE, END_BLACK = 0.70, 0.10                 # the last ~0.8 s of the pause: fade to black, then black


# ---------------------------------------------------------------------------
# Dimming and lighting
# ---------------------------------------------------------------------------
SOLID_V = 0.27                                   # opaque fills darker than this (card backs) stay solid


class Glow:
    """A part's brightness: k scales its own stroke and fill opacities (1 = as the kit built it), so a
    part dims and lights without losing its look (the lane's 0.6, the text lines' 0.55, the cone's 0.10).
    Dark opaque fills (the cards' backs) stay solid: a dimmed box still hides the lane running behind it,
    and on black it looks dimmed anyway."""

    def __init__(self, mob: Mobject, k: float = 1.0):
        self.mob = mob
        self.parts = []
        for m in mob.family_members_with_points():
            fill = m.data["fill_rgba"]
            solid = len(fill) > 0 and float(fill[:, :3].max()) < SOLID_V and float(fill[:, 3].min()) > 0.99
            self.parts.append((m, fill[:, 3].copy(), m.data["stroke_rgba"][:, 3].copy(), solid))
        self.k = 1.0
        self.set(k)

    def set(self, k: float) -> "Glow":
        for m, f, s, solid in self.parts:
            fill, stroke = m.data["fill_rgba"], m.data["stroke_rgba"]
            if not solid and len(fill) == len(f):
                fill[:, 3] = np.clip(f * k, 0.0, 1.0)
            if len(stroke) == len(s):
                stroke[:, 3] = np.clip(s * k, 0.0, 1.0)
            m.note_changed_data()
        self.k = k
        return self


def glow(glows, k: float, run_time: float = LIGHT_T, rate_func=smooth, time_span=None) -> Animation:
    """Take parts to brightness k. Runs on a stand-in mobject, so the parts stay where they are in the
    scene's drawing order (animating a group of them would regroup them and lose behind() / flying()).
    Inside a longer play, pass time_span=(t0, t1): a play's run_time overrides each animation's own."""
    glows = list(glows)
    start: dict[int, float] = {}

    def f(_m, a):
        for g in glows:
            k0 = start.setdefault(id(g), g.k)
            g.set(k0 + (k - k0) * a)
    return UpdateFromAlphaFunc(VGroup(), f, run_time=run_time, rate_func=rate_func, time_span=time_span)


def read_frame(mob: Mobject, pad: float = 0.05) -> RoundedRectangle:
    """The writer reading something: a teal frame around it (beat 2 runs it down the guide's rows)."""
    f = RoundedRectangle(width=mob.get_width() + 2 * pad, height=mob.get_height() + 2 * pad, corner_radius=0.07)
    return f.set_fill(ACCENT, opacity=0.08).set_stroke(ACCENT, width=2.4, opacity=0.95).move_to(mob)


def ink_bar(width: float, height: float = 0.05, color=ACCENT, opacity: float = 0.95) -> RoundedRectangle:
    b = RoundedRectangle(width=width, height=height, corner_radius=height / 2)
    return b.set_fill(color, opacity=opacity).set_stroke(width=0)


# ---------------------------------------------------------------------------
# The phone's chat thread (wordless bubbles)
# ---------------------------------------------------------------------------
_THREAD = [("user", 0.80, 1, 31), ("bot", 1.14, 3, 32), ("user", 0.96, 2, 33), ("bot", 1.14, 2, 34)]


def chat_bubble(who: str, width: float, n: int, seed: int) -> VGroup:
    """One message: the user's (filled, on the right, tail bottom-right) or the agent's reply
    (teal-edged card, on the left, tail bottom-left). Abstract lines, no words."""
    user = who == "user"
    lines = text_lines(width - 0.28, n=n, height=0.06, gap=0.09, color=INK if user else ACCENT,
                       opacity=0.7 if user else 0.85, seed=seed)
    h = max(0.32, lines.get_height() + 0.24)
    body = RoundedRectangle(width=width, height=h, corner_radius=min(0.14, h / 2))
    fill, edge = (BUBBLE_FILL, None) if user else (CARD_FILL, ACCENT)
    s = 1 if user else -1
    x = body.get_right()[0] - 0.16 if user else body.get_left()[0] + 0.16
    b = body.get_bottom()[1]
    tail = Polygon(np.array([x - 0.10 * s, b + 0.02, 0]), np.array([x + 0.08 * s, b + 0.02, 0]),
                   np.array([x + 0.16 * s, b - 0.11, 0]))
    shape = Union(body, tail)
    shape.set_fill(fill, opacity=1.0)
    shape.set_stroke(edge or fill, width=1.6 if edge else 0)
    lines.move_to(body)
    out = VGroup(shape, lines)
    out.who = who
    return out


def chat_thread(screen: Mobject) -> VGroup:
    bubbles = VGroup(*[chat_bubble(*spec) for spec in _THREAD]).arrange(DOWN, buff=0.14)
    bubbles.move_to(screen).align_to(screen.get_top() + 0.34 * DOWN, UP)
    for bub in bubbles:
        if bub.who == "user":
            bub.align_to(screen.get_right() + 0.10 * LEFT, RIGHT)
        else:
            bub.align_to(screen.get_left() + 0.10 * RIGHT, LEFT)
    return bubbles


# ---------------------------------------------------------------------------
# The end card (copied from video 2's bit5_exit.py)
# ---------------------------------------------------------------------------
def like_icon(height: float = LIKE_H) -> SVGMobject:
    """Video 1's like glyph (the Material thumb-up), in like-blue."""
    thumb = SVGMobject(str(_REPO_ROOT / "assets" / "icons" / "thumbs_up.svg"))
    thumb.set_fill(LIKE_BLUE, opacity=1.0)
    thumb.set_stroke(width=0)
    thumb.set_height(height)
    return thumb


def subscribe_pill(width: float = PILL_W, height: float = PILL_H) -> VGroup:
    """Video 1's red subscribe pill with a white «اشتراك» (Amiri sits optically low: nudged up)."""
    pill = RoundedRectangle(width=width, height=height, corner_radius=height / 2)
    pill.set_fill(YT_RED, opacity=1.0)
    pill.set_stroke(width=0)
    label = ar_text("اشتراك", font_size=32, color=WHITE)
    label.move_to(pill.get_center() + 0.19 * height * UP)
    return VGroup(pill, label)


def pop_in(mob: Mobject, time_span: tuple[float, float]) -> Animation:
    """Grows in from half size with a small overshoot (ease-out-back) while it fades up; it is
    invisible until its span starts, so several can share one play."""
    base = mob.copy()
    c1 = 1.70158

    def _f(m, a):
        back = 1 + (c1 + 1) * (a - 1) ** 3 + c1 * (a - 1) ** 2
        m.become(base.copy().scale(0.5 + 0.5 * back).set_opacity(min(1.0, 3.0 * a)))
    return UpdateFromAlphaFunc(mob, _f, time_span=time_span, rate_func=linear)


def ripple(pill: VMobject, run_time: float = RIPPLE_T) -> Animation:
    """A pill-shaped ring leaves the subscribe pill and fades as it grows, by the same margin on
    every side: the 'tap here' cue of a subscribe button. The ring is the animation's mobject;
    remove it after."""
    w, h, c = pill.get_width(), pill.get_height(), pill.get_center()

    def ring(d: float) -> RoundedRectangle:
        r = RoundedRectangle(width=w + 2 * d, height=h + 2 * d, corner_radius=h / 2 + d).move_to(c)
        return r.set_fill(opacity=0)

    def _f(m, a):
        e = smooth(a)
        m.become(ring(RIPPLE_GROW * e).set_stroke(YT_RED, width=4.0 * (1.0 - 0.5 * e), opacity=0.8 * (1.0 - e)))
    return UpdateFromAlphaFunc(ring(0.0).set_stroke(YT_RED, width=4.0, opacity=0.0), _f,
                               run_time=run_time, rate_func=linear)


# ---------------------------------------------------------------------------
# The scene
# ---------------------------------------------------------------------------
class Bit7Exit(AgentScene):
    def construct(self):
        self.continue_from("Bit6Fixes")              # the cut from Bit6Fixes is seamless
        self.build_start()
        self.beat_writer()        # bit7_exit.1
        self.beat_guide()         # bit7_exit.2
        self.beat_desk()          # bit7_exit.3
        self.beat_hands()         # bit7_exit.4 (+2 s: the loop turns once)
        self.beat_phone()         # bit7_exit.5
        self.beat_next()          # bit7_exit.7
        self.beat_end_card()      # bit7_exit.8

    # ------------------------------------------------------------------ the start frame
    def build_start(self):
        m = master(guide=True, desk_on=True)
        self.m = m
        self.view = behind(m.view)
        self.lane = behind(loop_lane())
        self.slips = list(row_of_slips(N_START))
        self.nb = notebook().move_to(NB_C).set_z_index(NB_Z)
        self.cur = cursor(0.58).move_to(CUR_POS)
        self.inks: list[Mobject] = []
        parts = dict(view=self.view, lane=self.lane, guide=m.guide, desk=m.desk, nb=self.nb, writer=m.writer,
                     hands=m.hands, world=m.world, to_hands=m.to_hands, to_world=m.to_world)
        self.g = SimpleNamespace(**{k: Glow(v, DIM) for k, v in parts.items()})
        self.g.slips = [Glow(s, DIM) for s in self.slips]
        self.add(self.view, self.lane, m.guide, m.desk, *self.slips, self.nb, m.writer, m.hands, m.world,
                 m.to_hands, m.to_world)

    def diagram(self) -> list[Mobject]:
        """Every top-level piece of the diagram now on screen (animate them one by one, never as a
        group: a group would be drawn as one batch and the lane would show through the boxes)."""
        m = self.m
        return [self.view, self.lane, m.guide, m.desk, *self.slips, self.nb, *self.inks, m.writer, self.cur,
                m.hands, m.world, m.to_hands, m.to_world]

    # ------------------------------------------------------------------ 1. a writer, in a loop
    def beat_writer(self):
        g = self.g
        with self.narrate("bit7_exit.1"):
            self.until("الإيجنت", lead=0.2)
            self.play(glow([g.writer], 1.0), FadeIn(self.cur), run_time=0.45)
            self.until("كاتب", lead=0.05)
            self.play(blink(self.cur, n=1, period=0.3), run_time=0.3)
            self.until("جوّا", lead=0.25)
            path = self.lane.path
            dot = behind(Dot(radius=0.1).set_fill(ACCENT, 1.0).move_to(path.get_start()))
            self.add(dot)
            self.play(glow([g.lane], 1.0, time_span=(0.0, 0.35)), MoveAlongPath(dot, path, rate_func=smooth),
                      run_time=max(0.9, self.hold_left() - 0.3))
            self.play(FadeOut(dot), run_time=0.2)

    # ------------------------------------------------------------------ 2. a guide it reads its tools from
    def beat_guide(self):
        rows = self.m.guide.rows
        with self.narrate("bit7_exit.2"):
            self.play(glow([self.g.guide], 1.0), run_time=0.3)
            frame = read_frame(rows[0], pad=0.04)
            self.until("بيقرا", lead=0.1)
            self.play(FadeIn(frame), run_time=0.15)
            self.play(frame.animate.move_to(rows[-1]), rate_func=linear,
                      run_time=float(np.clip(self.hold_left() - 0.55, 0.6, 1.1)))
            self.play(FadeOut(frame), run_time=0.2)

    # ------------------------------------------------------------------ 3. a desk that fills, a notebook
    def beat_desk(self):
        g, nb = self.g, self.nb
        with self.narrate("bit7_exit.3"):
            self.play(glow([g.desk, g.view, *g.slips], 1.0), run_time=LIGHT_T)
            new = slip(kind="result", width=SLIP_W, seed=7).move_to(desk_slot(N_START, N_ROW))
            self.until("بتتعبّى", lead=0.15)
            self.play(FadeIn(new, shift=0.45 * DOWN), run_time=0.45)
            self.slips.append(new)
            self.until("ودفتر", lead=0.2)
            self.play(glow([g.nb], 1.0), run_time=LIGHT_T)
            w = nb.lines[0].get_width()
            ink1 = ink_bar(0.92 * w).move_to(nb.lines[0]).align_to(nb.lines[0], RIGHT).set_z_index(NB_Z)
            ink2 = ink_bar(0.55 * w).move_to(nb.lines[1]).align_to(nb.lines[1], RIGHT).set_z_index(NB_Z)
            self.until("بيحفظ", lead=0.1)
            self.play(GrowFromEdge(ink1, RIGHT), run_time=0.4)
            self.until("المهم", lead=0.1)
            self.play(GrowFromEdge(ink2, RIGHT), run_time=0.3)
            self.inks += [ink1, ink2]

    # ------------------------------------------------------------------ 4. hands; the loop turns once
    def beat_hands(self):
        g, m = self.g, self.m
        h, wd = m.hands, m.world
        key = "bit7_exit.4"
        with self.narrate(key, pause=line_pause(key) + 2.0):
            self.play(glow([g.hands, g.to_hands], 1.0), run_time=LIGHT_T)
            self.play(h.box.animate.set_stroke(INK, width=3.4), rate_func=there_and_back, run_time=0.35)
            # «برنامج صغير بينفّذ اللي بيكتبو بالحرف»: a request goes in, an envelope goes out
            self.until("برنامج", lead=0.35)
            self._request_in(speed=1.0)
            self.until("بينفّذ", lead=0.15)
            env = flying(envelope(0.5).move_to(h.get_center()))
            self.add(env)
            self.play(env.animate.move_to(wd.supplier.get_center()),
                      glow([g.world, g.to_world], 1.0, time_span=(0.1, 0.6)), run_time=0.7)
            self.play(FadeOut(env, scale=0.5), Indicate(wd.supplier, color=WARM, scale_factor=1.12), run_time=0.4)
            # the +2 s hold: the whole loop turns once, everything lit
            self.until("بالحرف", lead=0.1)
            self._turn(self.hold_left() - 0.15)

    def _request_in(self, speed: float = 1.0) -> None:
        """The writer writes a request slip by its cursor; it goes into the hands."""
        req = flying(slip(kind="request", width=SLIP_W, seed=5).move_to(REQ_START))
        self.play(FadeIn(req, scale=0.5), blink(self.cur, n=1, period=0.3 / speed), run_time=0.3 / speed)
        self.play(req.animate.scale(0.3).move_to(self.m.hands.get_center()).set_opacity(0), run_time=0.45 / speed)
        self.remove(req)

    TURN = [0.45, 0.2, 0.6, 0.55, 0.3, 0.45, 0.45, 0.2]       # the lap's plays at speed 1 (s)

    def _turn(self, budget: float) -> None:
        """One lap: the reply comes back, a result slip lands on the desk, the writer reads it, writes
        the next request, and out it goes (about 3.2 s at speed 1, fitted to `budget`; each play may
        run up to a frame long, so that is kept aside)."""
        frames = len(self.TURN) / self.camera.fps
        speed = float(np.clip(sum(self.TURN) / max(budget - frames, 0.1), 0.8, 1.4))
        h, wd = self.m.hands, self.m.world
        env = flying(envelope(0.5, WARM).move_to(wd.supplier.get_center()))
        self.add(env)
        self.play(env.animate.move_to(h.get_center()), run_time=0.45 / speed)
        res = flying(slip(kind="result", width=SLIP_W, seed=9).move_to(h.get_center()))
        self.play(FadeOut(env, scale=0.5), FadeIn(res, scale=0.3), run_time=0.2 / speed)
        self._land(res, run_time=0.6 / speed)
        frame = flying(read_frame(res))
        self.play(glow([self.g.view], 2.6, rate_func=there_and_back), FadeIn(frame, rate_func=there_and_back),
                  run_time=0.55 / speed)
        self.remove(frame)
        self._request_in(speed=speed)
        env2 = flying(envelope(0.5).move_to(h.get_center()))
        self.add(env2)
        self.play(env2.animate.move_to(wd.customers.get_center()), run_time=0.45 / speed)
        self.play(FadeOut(env2, scale=0.5), run_time=0.2 / speed)

    def _land(self, s: Mobject, run_time: float) -> None:
        """Slip s (at the hands) drops onto the desk's last place in front of the notebook; the row
        moves up one place and the oldest slides off the desk's left end."""
        target = desk_slot(N_FRONT - 1, N_ROW)
        path = ArcBetweenPoints(s.get_center(), target, angle=-PI / 3)
        anims = [MoveAlongPath(s, path)]
        old, keep = self.slips[0], self.slips[1:]
        if len(self.slips) >= N_FRONT:
            anims.append(old.animate.shift(0.6 * LEFT).set_opacity(0))
            anims += [sl.animate.move_to(desk_slot(i, N_ROW)) for i, sl in enumerate(keep)]
        self.play(*anims, run_time=run_time)
        if len(self.slips) >= N_FRONT:
            self.remove(old)
            self.slips = keep
        self.slips.append(s)

    # ------------------------------------------------------------------ 5. inside apps, on your phone
    def beat_phone(self):
        with self.narrate("bit7_exit.5"):
            path = self.lane.path                                   # «وهالدورة»: once more around the loop
            dot = behind(Dot(radius=0.1).set_fill(ACCENT, 1.0).move_to(path.get_start()))
            self.add(dot)
            self.play(MoveAlongPath(dot, path, rate_func=smooth), glow([self.g.lane], 1.6, rate_func=there_and_back),
                      run_time=float(np.clip(self.to("جوا", lead=0.4), 0.6, 0.9)))
            self.play(FadeOut(dot), run_time=0.12)
            self.remove(dot)
            pieces = self.diagram()
            o = VGroup(*[p.copy() for p in pieces]).get_center()
            phone = icon_phone(PHONE_H).move_to(PHONE_C + 6.0 * RIGHT)
            self.until("جوا", lead=0.25)
            self.play(*[p.animate.scale(SMALL, about_point=o).shift(SMALL_C - o) for p in pieces],
                      phone.animate.move_to(PHONE_C), run_time=0.75)
            thread = chat_thread(phone.screen)
            ring = behind(loop_ring(center=PHONE_C, radius=RING_R, opacity=0.55))
            ring.add_updater(lambda mob, dt: mob.rotate(-RING_SPIN * dt, about_point=PHONE_C))
            self.play(FadeIn(ring), run_time=0.3)
            self.until("تراسلا", lead=0.2)
            self.play(LaggedStart(*[FadeIn(b, shift=0.12 * UP, scale=0.9) for b in thread], lag_ratio=0.55),
                      run_time=float(np.clip(self.hold_left() - 0.35, 1.0, 1.9)))
            self.phone, self.thread, self.ring = phone, thread, ring

    # ------------------------------------------------------------------ 6. next video: the like button
    def beat_next(self):
        with self.narrate("bit7_exit.7"):
            gone = [*self.diagram(), self.phone, *self.thread, self.ring]
            self.play(*[FadeOut(p) for p in gone], run_time=0.75)
            self.ring.clear_updaters()
            d = dial(DIAL_R).set_value(DIAL_V)
            d.shift(DIAL_HUB - d.hub.get_center())
            hub = d.hub.get_center()
            thumbs = VGroup(thumbs_up(THUMB_H[0]).move_to(hub + THUMB_A), thumbs_up(THUMB_H[1]).move_to(hub + THUMB_B))
            q = question_mark(1.0, WARM).move_to(hub + Q_C)
            self.until("كيف", lead=0.45)
            self.play(FadeIn(d, scale=0.9), run_time=0.5)
            self.until("بزر", lead=0.3)
            self.play(LaggedStart(*[FadeIn(t, shift=0.4 * DOWN) for t in thumbs], lag_ratio=0.4), run_time=0.4)
            # «اللايك»: the thumbs press on the needle, twice; it swings further toward yes
            self.until("اللايك", lead=0.1)
            for v in (0.95, 0.99):
                a = (d.value - 0.5) * PI
                press = PUSH * np.array([np.cos(a), -np.sin(a), 0.0])     # across the needle, clockwise
                self.play(*[t.animate.shift(press) for t in thumbs], d.animate_to(v, run_time=0.24), run_time=0.24)
                self.play(*[t.animate.shift(-press) for t in thumbs], run_time=0.18)
            self.play(FadeIn(q, scale=0.5, shift=0.1 * UP), d.animate_to(0.96, run_time=0.4), run_time=0.4)
            self.still = VGroup(d, *thumbs, q)

    # ------------------------------------------------------------------ 7. like and subscribe (video 2's end card)
    def beat_end_card(self):
        k = "bit7_exit.8"
        still = self.still
        like, sub = like_icon(), subscribe_pill()
        row = VGroup(sub, like).arrange(RIGHT, buff=OUTRO_GAP)     # read right to left: like first
        row.move_to(OUTRO_ROW_C)
        with self.narrate(k) as ln:
            self.play(still.animate.scale(OUTRO_SCALE).move_to(OUTRO_STILL_C), run_time=OUTRO_MOVE_T)
            t_like = max(0.0, ln["start"] + line_word_at(k, "لايك") - POP_LEAD - self.time)
            t_sub = max(t_like + 0.3, ln["start"] + line_word_at(k, "واشترك") - POP_LEAD - self.time)
            self.play(pop_in(like, (t_like, t_like + POP_IN_T)), pop_in(sub, (t_sub, t_sub + POP_IN_T)),
                      run_time=t_sub + POP_IN_T)
            for _ in range(RIPPLES):
                if self.hold_left() - END_FADE - END_BLACK < RIPPLE_T + RIPPLE_GAP:
                    break
                self.wait(RIPPLE_GAP)
                rip = ripple(sub[0])
                self.play(rip)
                self.remove(rip.mobject)
            rest = self.hold_left() - END_FADE - END_BLACK
            if rest > 1e-3:
                self.wait(rest)
            self.play(FadeOut(VGroup(still, row)), run_time=END_FADE)
