"""
Bit2Menu — the tools guide (دليل الأدوات) the writer is handed, then the shop's price menu (منيو المحل).

Starts on bit 1's last frame (the master diagram, the request slip, an envelope and a question mark).
  1 the slip, envelope and ? leave; the diagram fades back (the writer stays lit); the tools guide
    unfolds big at the right, an arrow hands it to the writer, its five rows come in on «لأدواتو»
  2 «كل أداة هيي سطر» the rows pulse in turn; a big copy of the email row comes out at the top left;
    a frame lands on its name («اسم»), its line («وجملة»), its two blanks («وفراغات»)
  3 an envelope beside the writer gets a cross («ما بيستعمل الإيميل أبداً»); the writer's highlight
    reaches over the guide («بيقرا الدليل»); the big row becomes the writer's next slip: the email row
    with its blanks filled (المورّد · أربعين علبة كولا), the cursor writing it
  4 the guide goes home above the writer; two look-alike rows (email, chat) come out big; «موصوفة غلط»
    the email row's line turns into a red scribble; «بينقّي السطر الغلط» a teal pick lands on the chat
    row and flashes red with a cross; «أو بيعبّي الفراغات غلط» the pick moves to the email row and a
    blank gets a red ?
  5 a blank strip on a cable to the writer; five app plugs (five tips) bump into it and bounce off;
    «من 2024» one socket with "2024" above it; «شكل واحد» every tip turns into the shared shape;
    «وأغلب الشركات» the strip fills with that socket; «فصار أي تطبيق بيركب» the plugs click in one after
    another and a pulse runs down the cable into the writer; then the stage clears
  6 the shop's price menu unfolds big; «الأسعار موجودة» the price bars and tags light; «بس قديش دفع»
    the dashed what-it-paid slots pulse and each gets a ?; «مانو موجود» they stay empty (a dim flash)
  7 «ما خسر عن قصد» the cube's real cost shows as a red dashed ghost bar under the card, off the menu;
    «الخسارة ما كانت مكتوبة» the writer's highlight reaches the card; the ghost fades, the slot is empty
  8 «طيب الأسعار فهمناها» the menu shrinks away and the diagram comes back at full strength (the guide
    at its home); «بس الجاكيت الزرقا والكرافة الحمرا؟» a small speech bubble with the blazer and a ?

End frame (bit 3 starts here): master(guide=True) at full strength — writer, hands, world, both
arrows, behind(loop_lane()), row_of_slips(N_ROW), the guide at GUIDE_C — plus blazer_bubble() at the
top right (see that helper). No cursor.

Z-order note: a LaggedStart / AnimationGroup wraps its animations' mobjects in a fresh VGroup (z_index 0)
and the scene adds that group, pulling the members out of their parent and below anything at a higher
z. So every lagged() here names the on-screen group it animates inside, and no ad-hoc VGroup of
z-raised parts goes into a Transform.

Render (preview): .venv/bin/manimgl our_scenes/bit2_menu.py Bit2Menu -w -l --video_dir ./media
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
Z_CARD, Z_MOVE, Z_TOP = 1, 2, 3          # cards over the faded diagram; movers over cards; marks on top
DIM = 0.15                               # the diagram while this bit talks about the guide and the menu

GUIDE_BIG_W = 5.8                        # the tools guide, unfolded (x -0.05..5.75, y -1.16..3.16)
GUIDE_BIG_C = np.array([2.85, 1.0, 0.0])
BIG_ROW_W, BIG_ROW_H = 4.8, 0.8          # the email row, zoomed: above the writer, clear of the guide
BIG_ROW_C = np.array([-3.4, 2.45, 0.0])
SLIP_RIGHT = -1.0                        # the filled slip ends here (above the writer's cursor)
MAIL_C = np.array([-4.85, 0.6, 0.0])     # "it never uses email": left of the writer
PAIR_W = 5.6                             # beat 4's two look-alike rows
ROW_A_C = np.array([2.55, 1.2, 0.0])     # email
ROW_B_C = np.array([2.55, 0.05, 0.0])    # chat with customers

STRIP_Y = 0.25                           # beat 5: the socket strip, on a cable from the writer
FACE_X = [0.30 + 1.13 * i for i in range(5)]
P_BIG = 1.05                             # an app's plug while its tip matters
P_IN = 0.6                               # plugged in (fits socket(P_IN / 0.7))
REST_TIP_Y = -0.95                       # where the plugs wait, tips up

MENU_SCALE = 1.25                        # the price menu, unfolded (x -0.03..5.72, y -1.21..2.41)
MENU_C = np.array([2.85, 0.6, 0.0])

BUBBLE_C = np.array([3.6, 2.72, 0.0])    # the blazer bubble's body centre (its tail stops above the world)


# ---------------------------------------------------------------------------
# Pieces
# ---------------------------------------------------------------------------
def lagged(*anims, group: Mobject, lag_ratio: float = 0.25, **kwargs) -> LaggedStart:
    """LaggedStart inside `group`: a group already on screen, or one with the members' z_index (see the
    z-order note at the top)."""
    return LaggedStart(*anims, group=group, lag_ratio=lag_ratio, **kwargs)


def faded(mob: Mobject, k: float) -> Mobject:
    """Multiply every part's opacity by k (unfilled parts stay unfilled)."""
    for sm in mob.get_family():
        if isinstance(sm, VMobject) and sm.has_points():
            sm.set_fill(opacity=sm.get_fill_opacity() * k, recurse=False)
            sm.set_stroke(opacity=sm.get_stroke_opacity() * k, recurse=False)
    return mob


def dim_flash(mob: Mobject, k: float = 0.25) -> Animation:
    """A flat dim flash: mob fades to k of itself and back."""
    return Transform(mob, faded(mob.copy(), k), rate_func=there_and_back)


def frame_around(mob: Mobject, color=ACCENT, buff: float = 0.08, fill: float = 0.10, width: float = 3.0,
                 r: float = 0.1) -> RoundedRectangle:
    """A highlight frame (this part, now)."""
    f = RoundedRectangle(width=mob.get_width() + 2 * buff, height=mob.get_height() + 2 * buff,
                         corner_radius=min(r, (mob.get_height() + 2 * buff) / 2))
    f.move_to(mob).set_stroke(color, width=width).set_fill(color, opacity=fill)
    return f.set_z_index(Z_TOP)


def reach(writer: Mobject, target: Mobject, opacity: float = 0.12) -> VMobject:
    """The writer's soft highlight, from its right edge over a card (what it reads)."""
    a = writer.get_corner(UR) + 0.2 * DOWN
    b = writer.get_corner(DR) + 0.2 * UP
    cone = Polygon(a, target.get_corner(UL), target.get_corner(UR), target.get_corner(DR), target.get_corner(DL), b)
    cone.set_fill(ACCENT, opacity=opacity).set_stroke(width=0)
    return cone.set_z_index(Z_TOP)


def scribble(width: float, height: float = 0.2, color=RED, n: int = 15, seed: int = 4) -> VMobject:
    """A described-wrong line: a red scrawl the length of the description."""
    rng = np.random.default_rng(seed)
    xs = np.linspace(-width / 2, width / 2, n)
    pts = [np.array([x, (height / 2) * (1 if k % 2 else -1) * (0.35 + 0.65 * rng.random()), 0.0]) for k, x in enumerate(xs)]
    v = VMobject()
    v.set_points_smoothly(pts)
    v.set_stroke(color, width=4).set_fill(opacity=0)
    return v


def prep_unfold(card_group: VGroup) -> None:
    """Fold a card (tools guide / price menu) shut: Restore its .card, .title and .rows to unfold it."""
    card_group.card.save_state()
    card_group.card.stretch(0.02, 1, about_edge=UP)
    card_group.title.save_state()
    faded(card_group.title, 0.0).shift(0.1 * UP)
    for r in card_group.rows:
        r.save_state()
        faded(r, 0.0).shift(0.12 * UP)


def zoom_row(src: VGroup, dst: VGroup, z: int = Z_MOVE) -> list[Animation]:
    """A copy of a guide row becomes a bigger tool_row: its shapes morph, its name cross-fades (Arabic
    glyphs shaped at another font size don't morph cleanly). Both run at z (see the z-order note)."""
    parts = lambda r: VGroup(r.bg, r.icon, r.desc, r.blanks).set_z_index(z)
    name = FadeTransform(src.name, dst.name)
    name.mobject.set_z_index(z)
    return [ReplacementTransform(parts(src), parts(dst)), name]


def plug_at(kind: int, size: float, tip_c, color=None) -> VGroup:
    p = plug(kind, size, color=color)
    return p.shift(np.array(tip_c) - p.tip.get_center())


def late_there_and_back(t: float, start: float = 0.6) -> float:
    """Still until `start`, then out and back (a click at the end of a move)."""
    return there_and_back(max(0.0, (t - start) / (1.0 - start)))


def blazer_bubble() -> VGroup:
    """The end frame's small speech bubble (top right): a blue blazer in it and a ? beside it.
    Attributes: .bubble, .blazer, .q"""
    bub = speech_bubble(1.5, 1.05, tail="DR")
    bub.shift(BUBBLE_C - bub.body.get_center())
    blz = icon_blazer(0.75).move_to(bub.body)
    q = question_mark(0.6, WARM).next_to(bub.body, RIGHT, buff=0.2)
    out = VGroup(bub, blz, q)
    out.bubble, out.blazer, out.q = bub, blz, q
    return out


class Bit2Menu(AgentScene):
    def _hold_then(self, seconds: float) -> None:
        """Wait until `seconds` before the block's pause ends (for a closing animation that long)."""
        t = self.hold_left() - seconds
        if t > 1e-3:
            self.wait(t)

    def construct(self):
        self.continue_from("Bit1Loop")              # the cut from Bit1Loop is seamless
        # ---- bit 1's last frame -------------------------------------------------------------------
        m = master()
        w, h, wd = m.writer, m.hands, m.world
        lane = behind(loop_lane())
        # bit 1 ends with the last six result slips of its day loop (seeds 34..39), brought to full opacity
        row = VGroup(*[slip(kind="result", width=SLIP_W, seed=20 + k).set_opacity(1).move_to(desk_slot(i, N_ROW))
                       for i, k in enumerate(range(14, 20))])
        cur = cursor(0.58).move_to(CUR_POS)
        req = slip(REQUEST_SLIP_AR, kind="request", font_size=32).move_to(REQ_POS)
        env = envelope(0.8, INK).next_to(req, LEFT, buff=0.4)
        q = question_mark(0.85, WARM).next_to(env, UP, buff=0.12)
        self.add(lane, w, cur, h, m.to_hands, wd, m.to_world, row, req, env, q)
        ghosts = [h, wd, m.to_hands, m.to_world, lane, row]

        g = tools_guide(width=4.0, row_h=0.36)               # the same card master(guide=True) parks at home
        g.scale(GUIDE_BIG_W / g.get_width()).move_to(GUIDE_BIG_C)
        g.set_z_index(Z_CARD)
        link = Arrow(np.array([g.get_left()[0], 0.1, 0]), np.array([w.get_right()[0], 0.1, 0]), buff=0.1, thickness=3.0)
        link.set_fill(ACCENT, 1).set_stroke(width=0)

        # ---- 1. before the first lap, they hand the writer a guide to its tools --------------------
        with self.narrate("bit2_menu.1"):
            dims = []
            for mob in ghosts:
                mob.save_state()
                dims.append(Transform(mob, faded(mob.copy(), DIM)))
            self.play(FadeOut(req, shift=0.25 * UP), FadeOut(env, shift=0.25 * UP), FadeOut(q, shift=0.25 * UP),
                      *dims, run_time=0.45)
            prep_unfold(g)
            self.add(g)
            self.until("بيعطوا", lead=0.3)
            self.play(Restore(g.card), Restore(g.title), run_time=0.45)
            self.until("الكاتب", lead=0.25)
            self.play(GrowArrow(link), run_time=0.35)
            self.until("دليل", lead=0.3)
            self.play(lagged(*[Restore(r) for r in g.rows], group=g.rows), run_time=0.6)

        # ---- 2. every tool is a row: a name, one line of what it does, blanks to fill --------------
        with self.narrate("bit2_menu.2"):
            self.play(FadeOut(link),
                      lagged(*[r.bg.animate(rate_func=there_and_back).set_stroke(ACCENT, width=3.2) for r in g.rows],
                             group=g.rows, lag_ratio=0.3),
                      run_time=0.9)
            big = tool_row(0, width=BIG_ROW_W, height=BIG_ROW_H, name_size=40).move_to(BIG_ROW_C).set_z_index(Z_MOVE)
            self.play(*zoom_row(g.rows[0].copy(), big), run_time=0.5)
            self.until("اسم", lead=0.1)
            hl = frame_around(big.name)
            self.play(FadeIn(hl, scale=1.2), big.name.animate(rate_func=there_and_back).scale(1.15), run_time=0.35)
            self.until("وجملة", lead=-0.15)                   # Ali pauses after «اسم،»
            self.play(Transform(hl, frame_around(big.desc, buff=0.1)), big.desc.animate.set_fill(ACCENT, opacity=1.0),
                      run_time=0.35)
            self.until("وفراغات", lead=0.0)
            self.play(Transform(hl, frame_around(big.blanks)), big.desc.animate.set_fill(INK_2, opacity=0.5), run_time=0.35)
            self.play(lagged(*[b.animate(rate_func=there_and_back).scale(1.2).set_stroke(ACCENT, width=3) for b in big.blanks],
                             group=big.blanks, lag_ratio=0.4), run_time=0.6)

        # ---- 3. it never uses email: it reads the guide, writes the email row, fills the blanks ----
        with self.narrate("bit2_menu.3"):
            self.play(FadeOut(hl), run_time=0.3)
            mail = envelope(0.95, INK).move_to(MAIL_C)
            cross = icon_cross(0.55).move_to(mail)
            self.until("ما بيستعمل", lead=0.15)
            self.play(FadeIn(mail, scale=0.7), run_time=0.35)
            self.until("أبداً", lead=0.2)
            self.play(FadeIn(cross, scale=1.5), mail.animate.set_opacity(0.7), run_time=0.35)
            self.until("بيقرا", lead=0.15)
            cone = reach(w, g)
            scan = frame_around(g.rows[0], buff=0.05, fill=0.14, width=2.5)       # a reading frame runs down the rows
            self.play(FadeIn(cone), FadeIn(scan), run_time=0.2)
            for r in g.rows[1:]:
                self.play(scan.animate.move_to(r), run_time=0.1)
            self.play(FadeOut(cone), FadeOut(scan), run_time=0.25)
            # the next slip is that row: the name stays, the blanks become boxes for the values
            fs = filled_row_slip(["المورّد", "أربعين علبة كولا"], height=0.8, name_size=36)
            fs.move_to(np.array([SLIP_RIGHT - fs.get_width() / 2, BIG_ROW_C[1], 0])).set_z_index(Z_MOVE)
            vals = [v[1] for v in fs.values]
            self.until("وبيكتب", lead=0.25)
            self.play(ReplacementTransform(big.bg, fs.card), FadeIn(fs[1]), ReplacementTransform(big.name, fs.name),
                      FadeOut(big.icon, scale=0.5), FadeOut(big.desc),
                      ReplacementTransform(big.blanks[1], fs.values[0][0]), ReplacementTransform(big.blanks[0], fs.values[1][0]),
                      cur.animate.next_to(fs.card, RIGHT, buff=0.15), run_time=0.55)
            self.until("وبيعبّي", lead=0.1)
            self.play(write_rtl(vals[0]), run_time=0.35)
            self.play(write_rtl(vals[1]), run_time=0.45)
            self.play(fs.card.animate(rate_func=there_and_back).set_stroke(INK, width=4), blink(cur, n=1, period=0.4),
                      run_time=0.4)
            self.play(cur.animate.move_to(CUR_POS), run_time=0.3)

        # ---- 4. so how a row is written matters: the wrong row, or the blanks filled wrong ---------
        home = master(guide=True).guide
        ra = tool_row(0, width=PAIR_W, height=0.8, name_size=36).move_to(ROW_A_C).set_z_index(Z_MOVE)
        rb = tool_row(1, width=PAIR_W, height=0.8, name_size=36).move_to(ROW_B_C).set_z_index(Z_MOVE)
        with self.narrate("bit2_menu.4"):
            self.play(FadeOut(fs, scale=0.9), FadeOut(mail, scale=0.9), FadeOut(cross, scale=0.9), run_time=0.3)
            self.play(Transform(g, home), *zoom_row(g.rows[0].copy(), ra), *zoom_row(g.rows[1].copy(), rb), run_time=0.6)
            self.until("مكتوب", lead=0.2)
            self.play(*[r.desc.animate(rate_func=there_and_back).set_fill(ACCENT, opacity=1.0).stretch(2.2, 1) for r in (ra, rb)],
                      run_time=0.6)
            self.until("موصوفة", lead=0.2)
            bad = scribble(ra.desc.get_width() + 0.1).move_to(ra.desc).set_z_index(Z_MOVE)
            self.play(ReplacementTransform(ra.desc, bad), run_time=0.5)
            self.until("بينقّي", lead=0.25)
            pick = w.box.copy().set_fill(opacity=0).set_stroke(ACCENT, width=4).set_z_index(Z_TOP)
            self.play(Transform(pick, frame_around(rb, buff=0.1, fill=0.0, width=4)), run_time=0.45)
            self.until("الغلط،", lead=0.15)
            x2 = icon_cross(0.45).move_to(rb.get_corner(UR) + np.array([0.05, 0.05, 0])).set_z_index(Z_TOP)
            self.play(pick.animate.set_stroke(RED), rb.bg.animate(rate_func=there_and_back).set_fill(RED, opacity=0.45),
                      FadeIn(x2, scale=1.5), run_time=0.45)
            self.until("أو بيعبّي", lead=0.2)
            self.play(Transform(pick, frame_around(ra, buff=0.1, fill=0.0, width=4)), FadeOut(x2), run_time=0.4)
            self.until("الفراغات", lead=0.2)
            wrong = question_mark(0.36, RED).move_to(ra.blanks[1]).set_z_index(Z_TOP)
            self.play(FadeIn(wrong, scale=0.4), ra.blanks[1].animate.set_stroke(RED, width=2.4), run_time=0.35)

        # ---- 5. every company wrote its guide its own way; since 2024 one shape; any app plugs in --
        with self.narrate("bit2_menu.5"):
            strip = RoundedRectangle(width=FACE_X[-1] - FACE_X[0] + 1.3, height=1.0, corner_radius=0.2)
            strip.set_fill(CARD_FILL, 1).set_stroke(ACCENT, width=2.4)
            strip.move_to(np.array([(FACE_X[0] + FACE_X[-1]) / 2, STRIP_Y, 0])).set_z_index(Z_CARD)
            cable = Line(np.array([w.get_right()[0], STRIP_Y, 0]), np.array([strip.get_left()[0], STRIP_Y, 0]))
            cable.set_stroke(ACCENT, width=6)
            plugs = [plug_at(k, P_BIG, (FACE_X[k], REST_TIP_Y, 0)) for k in range(5)]
            pg = VGroup(*plugs).set_z_index(Z_MOVE)
            self.play(*[FadeOut(mob) for mob in (ra, rb, bad, pick, wrong)], ShowCreation(cable), FadeIn(strip), run_time=0.4)
            self.until("كل شركة", lead=0.15)
            self.play(lagged(*[FadeIn(p, shift=0.4 * UP) for p in plugs], group=pg, lag_ratio=0.15), run_time=0.5)
            self.until("تكتب", lead=0.15)
            bumps = [p.animate(rate_func=there_and_back).shift((strip.get_bottom()[1] - p.tip.get_top()[1]) * UP) for p in plugs]
            self.play(lagged(*bumps, group=pg, lag_ratio=0.35), run_time=min(1.5, self.to("عطريقتا", lead=-0.4)))
            # since 2024, one shape
            big_sock = socket(1.5).move_to(np.array([FACE_X[2], STRIP_Y, 0])).set_z_index(Z_CARD)
            year = en_text("2024", 50, INK).next_to(big_sock, UP, buff=0.18).set_z_index(Z_CARD)
            self.until("من 2024", lead=0.2)
            self.play(FadeIn(big_sock, scale=0.6), FadeIn(year, shift=0.15 * DOWN), run_time=0.45)
            self.until("واحد", lead=0.25)                      # «2024» is said as three words: «شكل» lands late
            morphs = []
            for p in plugs:
                ref = plug(-1, P_BIG)
                ref.shift(p.body.get_center() - ref.body.get_center())
                morphs.append(Transform(p.tip, ref.tip))
            self.play(*morphs, Indicate(big_sock[1], color=INK, scale_factor=1.3), run_time=0.5)
            # most big companies took it up: the strip fills with that socket
            faces = [socket(P_IN / 0.7).move_to(np.array([x, STRIP_Y, 0])).set_z_index(Z_CARD) for x in FACE_X]
            self.until("وأغلب", lead=0.15)
            fills = [TransformFromCopy(big_sock, f) for i, f in enumerate(faces) if i != 2]
            copies = VGroup(*[a.mobject for a in fills]).set_z_index(Z_CARD)
            self.play(ReplacementTransform(big_sock, faces[2]), lagged(*fills, group=copies),
                      year.animate.next_to(strip, UP, buff=0.14), run_time=0.8)
            self.remove(*faces)
            fg = VGroup(*faces).set_z_index(Z_CARD)
            self.add(fg)
            # so any app plugs in, one after another
            self.until("فصار", lead=0.1)
            ins = [Transform(p, plug_at(-1, P_IN, f.get_center(), color=p.body.get_fill_color())) for p, f in zip(plugs, faces)]
            clicks = [f[0].animate(rate_func=late_there_and_back).set_stroke(INK, width=4) for f in faces]
            self.play(lagged(*ins, group=pg, lag_ratio=0.45), lagged(*clicks, group=fg, lag_ratio=0.45), run_time=1.0)
            dot = Dot(radius=0.11).set_fill(INK, 1).move_to(cable.get_end()).set_z_index(Z_TOP)
            self.add(dot)
            self.play(MoveAlongPath(dot, cable), run_time=0.35, rate_func=rush_into)
            self.play(FadeOut(dot, scale=2.0), w.box.animate(rate_func=there_and_back).set_stroke(INK, width=5), run_time=0.35)
            self._hold_then(0.45)
            self.play(*[FadeOut(mob) for mob in (strip, cable, year, fg, pg)], run_time=0.4)

        # ---- 6. now the shop's menu: the prices are there; what it paid is not -----------------------
        pm = price_menu(show_cost=False).scale(MENU_SCALE).move_to(MENU_C).set_z_index(Z_CARD)
        qs = VGroup(*[question_mark(0.32, INK_2).move_to(r.cost_slot).shift(0.03 * DOWN)     # clear of the price bar
                      for r in pm.rows]).set_z_index(Z_TOP)
        with self.narrate("bit2_menu.6"):
            prep_unfold(pm)
            self.add(pm)
            self.play(Restore(pm.card), Restore(pm.title), run_time=0.45)
            self.play(lagged(*[Restore(r) for r in pm.rows], group=pm.rows, lag_ratio=0.3), run_time=0.5)
            self.until("الأسعار", lead=0.1)
            self.play(lagged(*[AnimationGroup(r.price.animate(rate_func=there_and_back).stretch(1.8, 1).set_fill("#ffd9b0"),
                                              r.tag.animate(rate_func=there_and_back).scale(1.5), group=r)
                               for r in pm.rows], group=pm.rows, lag_ratio=0.3), run_time=0.7)
            self.until("بس قديش", lead=0.05)
            self.play(lagged(*[r.cost_slot.animate(rate_func=there_and_back).set_stroke(INK, width=3.2) for r in pm.rows],
                             group=pm.rows, lag_ratio=0.35),
                      lagged(*[FadeIn(qq, scale=0.4) for qq in qs], group=qs, lag_ratio=0.35), run_time=0.9)
            self.until("مانو", lead=0.05)
            self.play(*[dim_flash(r.cost_slot) for r in pm.rows], dim_flash(qs), run_time=0.5)

        # ---- 7. it didn't lose on purpose: the loss was written nowhere in front of it ----------------
        with self.narrate("bit2_menu.7"):
            cube_row = pm.rows[2]
            bh = 0.26
            x_r = cube_row.price.get_right()[0]
            y_g = pm.card.get_bottom()[1] - 0.45
            length = ITEM_COST[2] * 1.6 * MENU_SCALE
            gbar = RoundedRectangle(width=length, height=bh, corner_radius=bh / 2)
            gbar.move_to(np.array([x_r - length / 2, y_g, 0])).set_fill(RED, opacity=0.3).set_stroke(width=0)
            gdash = DashedVMobject(gbar.copy(), num_dashes=30, positive_space_ratio=0.6).set_stroke(RED, width=3)
            gbox = icon_box(0.38).move_to(np.array([x_r + 0.34, y_g, 0]))
            gcube = icon_cube(0.7).next_to(gbox, RIGHT, buff=0.25)
            ghost = VGroup(gbar, gdash, gbox, gcube).set_z_index(Z_MOVE)
            self.until("ما خسر", lead=0.2)
            self.play(FadeIn(ghost, shift=0.15 * UP), run_time=0.45)
            self.until("الخسارة", lead=0.2)
            cone = reach(w, pm)
            self.play(FadeIn(cone), run_time=0.45)
            self.until("مكتوبة", lead=0.3)
            self.play(FadeOut(ghost, shift=0.1 * DOWN), run_time=0.5)
            self.until("بأي مكان", lead=0.1)
            self.play(dim_flash(cube_row.cost_slot), dim_flash(qs[2]), run_time=0.5)

        # ---- 8. the prices, we get. but the blue blazer and the red tie? ------------------------------
        new_row = row_of_slips(N_ROW)
        bb = blazer_bubble()
        with self.narrate("bit2_menu.8"):
            self.play(FadeOut(cone), run_time=0.25)
            self.until("الأسعار", lead=0.05)
            mc = pm.get_center()
            self.play(pm.animate.scale(0.15, about_point=mc).set_opacity(0),
                      qs.animate.scale(0.15, about_point=mc).set_opacity(0), run_time=0.45)
            self.remove(pm, qs)
            self.play(*[Restore(mob) for mob in ghosts if mob is not row], FadeOut(row), FadeIn(new_row), FadeOut(cur),
                      run_time=0.6)
            self.until("الجاكيت", lead=0.3)
            self.play(FadeIn(bb.bubble, scale=0.6, shift=0.15 * UP), run_time=0.35)
            self.play(GrowFromCenter(bb.blazer), run_time=0.4)
            self.until("الحمرا", lead=0.25)
            self.play(FadeIn(bb.q, scale=0.5, shift=0.1 * UP), run_time=0.35)
