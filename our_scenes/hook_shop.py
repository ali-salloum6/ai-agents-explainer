"""
HookShop — the shop nobody ran by hand, then: all it can do is write.

Voice-driven (AgentScene / NarratedScene): every beat plays inside `with self.narrate("hook.<n>")`
and lands on its word with self.until("word"), so the picture follows Ali's recorded lines.
  1 the office corner (fridge, baskets, iPad) draws in; the month's calendar fills day by day
  2 the four jobs pop on their words (what to sell, prices, ordering, customers); a box rolls in
    on a dolly with nobody pushing it
  3 three strange moments on their words: the cube's tag drops below cost, discounts pour out of
    a chat bubble, the iPad's speech bubble shows a blue blazer and a red tie
  4 a cross on the box and on a button; the shop folds into the iPad, the iPad becomes a page of
    writing with the cursor at its end; a chat reply writing itself; video 2's half-written face
  5 the cursor, a small fridge and a question mark; the three strange moments, faint, beside it

Render (preview): .venv/bin/manimgl our_scenes/hook_shop.py HookShop -w -l --video_dir ./media
"""
from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from our_scenes.agent_kit import *  # noqa: F401,F403

FRIDGE_C = np.array([-2.6, -0.45, 0])
FRIDGE_H = 4.1
IPAD_C = np.array([-0.15, -0.55, 0])
CAL_C = np.array([4.95, 2.35, 0])


def dolly_with_box(size: float = 0.9) -> VGroup:
    """A hand truck carrying a carton, nobody holding it."""
    box = icon_box(size)
    frame = VMobject()
    frame.start_new_path(box.get_corner(DR) + np.array([0.1, 0.9 * size, 0]))
    frame.add_line_to(box.get_corner(DR) + np.array([0.1, -0.08, 0]))
    frame.add_line_to(box.get_corner(DL) + np.array([-0.05, -0.08, 0]))
    frame.set_stroke(INK_2, width=4).set_fill(opacity=0)
    wheels = VGroup(*[Circle(radius=0.11).set_fill("#2a3140", 1).set_stroke(INK_2, width=2.5)
                      .move_to(box.get_corner(DR) + np.array([0.02 - k * 0.5 * size, -0.2, 0])) for k in (0, 1)])
    return VGroup(frame, box, wheels)


class HookShop(AgentScene):
    def construct(self):
        fr = fridge(FRIDGE_H).move_to(FRIDGE_C)
        pad = ipad(1.35).move_to(IPAD_C)
        cal = icon_calendar(1.3).move_to(CAL_C)
        floor = Line(np.array([-6.0, FRIDGE_C[1] - FRIDGE_H / 2 - 0.02, 0]), np.array([6.0, FRIDGE_C[1] - FRIDGE_H / 2 - 0.02, 0]))
        floor.set_stroke(CARD_STROKE, width=2)

        # ---- 1. a whole month, a small shop in an office ------------------------------------------
        with self.narrate("hook.1"):
            self.play(ShowCreation(floor), FadeIn(fr, shift=0.25 * UP), run_time=0.9)
            self.play(FadeIn(pad, shift=0.2 * UP), FadeIn(cal, shift=0.2 * DOWN), run_time=0.6)
            days = cal.days[:30]
            self.play(LaggedStart(*[d.animate.set_fill(TIE, 0.85) for d in days[:24]], lag_ratio=0.25),
                      blink(pad.cursor, n=3, period=0.5), run_time=max(1.2, self.line_left() - 0.1))

        # ---- 2. it chose, priced, ordered, answered; people only carried the boxes ----------------
        with self.narrate("hook.2"):
            prod = VGroup(icon_can(0.72), icon_chips(0.72), icon_cube(0.72)).arrange(RIGHT, buff=0.22)
            prod.move_to(np.array([1.75, 1.75, 0]))
            tag = icon_tag(0.8).move_to(np.array([3.55, 0.85, 0]))
            env = envelope(0.7).move_to(pad.screen)
            bub = icon_bubble(0.95, INK_2).move_to(np.array([1.85, 0.2, 0]))
            self.until("شو يبيع")
            self.play(LaggedStart(*[FadeIn(p, scale=0.5) for p in prod], lag_ratio=0.25), run_time=0.6)
            self.until("الأسعار")
            self.play(FadeIn(tag, scale=0.5, shift=0.1 * DOWN), run_time=0.45)
            self.until("البضاعة")
            self.play(env.animate.move_to(np.array([7.5, 1.0, 0])).set_opacity(0.0), run_time=0.9, rate_func=rush_into)
            self.remove(env)
            self.until("عالزباين")
            self.play(FadeIn(bub, scale=0.5, shift=0.1 * UP), run_time=0.45)
            self.until("الكراتين", lead=0.6)
            truck = dolly_with_box(0.85).move_to(np.array([7.8, floor.get_y() + 0.62, 0]))
            self.play(truck.animate.move_to(np.array([0.9 + 0.7, floor.get_y() + 0.62, 0])), run_time=1.1, rate_func=smooth)
            if self.line_left() > 0.01:
                self.wait(self.line_left())
            self.play(FadeOut(VGroup(prod, tag, bub)), run_time=min(0.4, max(0.1, self.hold_left() - 0.05)))

        # ---- 3. by the end of the month: cubes below cost, discounts for anyone, the blazer -------
        with self.narrate("hook.3"):
            self.until("الشهر", lead=0.3)
            self.play(LaggedStart(*[d.animate.set_fill(TIE, 0.85) for d in cal.days[24:30]], lag_ratio=0.3), run_time=0.6)
            cube = icon_cube(1.0).move_to(np.array([2.9, 2.15, 0]))
            ctag = icon_tag(0.7).next_to(cube, RIGHT, buff=0.15)
            self.until("مكعبات", lead=0.25)
            self.play(FadeIn(cube, scale=0.5), FadeIn(ctag, scale=0.5), run_time=0.45)
            red_tag = icon_tag(0.7, RED).move_to(ctag)
            down = Arrow(UP * 0.35, DOWN * 0.35, buff=0, thickness=4).set_fill(RED, 1).set_stroke(width=0)
            down.next_to(red_tag, RIGHT, buff=0.1)
            self.until("بأقل", lead=0.1)
            self.play(Transform(ctag, red_tag), FadeIn(down, shift=0.25 * DOWN), run_time=0.5)
            cbub = icon_bubble(1.0, INK_2).move_to(np.array([4.1, 0.45, 0]))
            self.until("خصم", lead=0.35)
            self.play(FadeIn(cbub, scale=0.5), run_time=0.35)
            chips = VGroup(*[icon_percent(0.44) for _ in range(6)])
            for k, c in enumerate(chips):
                c.move_to(cbub.get_center())
            targets = [cbub.get_center() + np.array([-1.35 + 0.52 * k, -1.15 - 0.22 * (k % 2), 0]) for k in range(6)]
            self.play(LaggedStart(*[c.animate.move_to(p) for c, p in zip(chips, targets)], lag_ratio=0.15),
                      run_time=1.0)
            speech = speech_bubble(2.0, 1.6, tail="DL")    # the iPad speaks: a picture, not words
            speech.move_to(pad.get_corner(UR) + np.array([0.62, 1.0, 0]))
            blz = icon_blazer(1.15).move_to(speech.body.get_center())
            self.until("وقال", lead=0.2)
            self.play(FadeIn(speech, scale=0.6, shift=0.2 * UP), run_time=0.45)
            self.until("جاكيت", lead=0.3)
            self.play(GrowFromCenter(blz), run_time=0.6)
            strange = VGroup(cube, ctag, down, cbub, chips, speech, blz)

        # ---- 4. but it can't lift a box or press a button: all it can do is write ----------------
        with self.narrate("hook.4"):
            btn = icon_button(0.8).move_to(np.array([3.4, -1.85, 0]))
            self.until("كرتونة", lead=0.4)
            x1 = icon_cross(0.5).move_to(truck[1])
            self.play(FadeIn(x1, scale=1.4), run_time=0.35)
            self.until("زر", lead=0.35)
            self.play(FadeIn(btn, scale=0.6), run_time=0.3)
            x2 = icon_cross(0.5).move_to(btn)
            self.play(FadeIn(x2, scale=1.4), run_time=0.3)
            shop = VGroup(fr, cal, floor, truck, x1, btn, x2, strange)
            self.until("كل اللي", lead=0.3)
            # the shop folds into the iPad's screen; the screen becomes a page of writing
            self.play(shop.animate.scale(0.05, about_point=pad.screen.get_center()).set_opacity(0),
                      pad.animate.scale(1.25).move_to(np.array([0, 0.3, 0])), run_time=0.8)
            self.remove(shop)
            page = _page_of_writing()
            self.play(FadeOut(pad), FadeIn(page.panel), run_time=0.4)
            self.play(LaggedStart(*[GrowFromEdge(l, RIGHT) for l in page.lines], lag_ratio=0.35),
                      run_time=min(1.4, self.to("التشات", lead=0.4)))
            page.cur.next_to(page.lines[-1], LEFT, buff=0.08)
            self.add(page.cur)
            self.until("التشات", lead=0.3)
            chat = _chat_reply().move_to(np.array([-3.3, 0.1, 0]))
            self.play(page.animate.scale(0.62).move_to(np.array([0.2, 0.1, 0])).set_opacity(0.35),
                      FadeIn(chat.bubble, shift=0.2 * DOWN), FadeIn(chat.card), run_time=0.6)
            self.play(LaggedStart(*[GrowFromEdge(l, RIGHT) for l in chat.lines], lag_ratio=0.4), run_time=1.0)
            self.until("الصورة", lead=0.45)
            face = _half_written_face(2.3).move_to(np.array([3.7, 0.1, 0]))
            self.play(FadeIn(face, shift=0.2 * LEFT), run_time=0.6)
            self.play(blink(face.cur, n=2, period=0.45), run_time=0.9)
            examples = Group(page, chat, face)

        # ---- 5. so how does writing run a shop? and why did this one go so wrong? -----------------
        with self.narrate("hook.5"):
            big = cursor(1.9).move_to(np.array([-1.9, 0.45, 0]))
            mini = fridge(2.2).move_to(np.array([1.9, 0.45, 0]))
            q = question_mark(1.2, INK).move_to(np.array([0.0, 0.45, 0]))
            self.play(FadeOut(examples, scale=0.9), FadeIn(big), run_time=0.5)
            self.play(FadeIn(mini, shift=0.2 * LEFT), FadeIn(q, scale=0.6), run_time=0.5)
            self.until("وليش", lead=0.2)
            row = VGroup(VGroup(icon_cube(0.7), icon_tag(0.55, RED)).arrange(RIGHT, buff=0.1),
                         icon_percent(0.6), icon_blazer(0.85)).arrange(RIGHT, buff=0.9)
            row.move_to(np.array([0.0, -2.0, 0])).set_opacity(0.0)
            self.play(row.animate.set_opacity(0.55), run_time=0.6)
            self.blink_for(big, max(0.5, self.hold_left() - 0.1), period=0.55)


def _page_of_writing() -> VGroup:
    """A panel of written lines (right to left) with the cursor waiting at the end. .panel .lines .cur"""
    panel = RoundedRectangle(width=5.6, height=3.4, corner_radius=0.25)
    panel.set_fill(CARD_FILL, 1).set_stroke(CARD_STROKE, width=2)
    panel.move_to(np.array([0, 0.3, 0]))
    lines = VGroup()
    rng = np.random.default_rng(5)
    for k in range(6):
        w = 4.5 if k < 5 else 2.1
        w *= 0.82 + 0.18 * rng.random() if k < 5 else 1
        lines.add(RoundedRectangle(width=w, height=0.13, corner_radius=0.065).set_fill(INK_2, 0.75).set_stroke(width=0))
    lines.arrange(DOWN, buff=0.3, aligned_edge=RIGHT).move_to(panel).align_to(panel.get_right() + 0.5 * LEFT, RIGHT)
    cur = cursor(0.42)
    out = VGroup(panel, lines)
    out.panel, out.lines, out.cur = panel, lines, cur
    out.add(cur)
    cur.set_opacity(1)
    return out


def _chat_reply() -> VGroup:
    """A chat: a question bubble (abstract) over a reply card whose lines write in. .bubble .card .lines"""
    bubble = icon_bubble(1.5, INK_2)
    card = RoundedRectangle(width=3.2, height=1.9, corner_radius=0.25)
    card.set_fill(CARD_FILL, 0.9).set_stroke(CARD_STROKE, width=1.6)
    bubble.next_to(card, UP, buff=0.2).align_to(card, RIGHT)
    lines = VGroup(*[RoundedRectangle(width=w, height=0.11, corner_radius=0.055).set_fill(ACCENT, 0.7).set_stroke(width=0)
                     for w in (2.6, 2.4, 1.3)]).arrange(DOWN, buff=0.28, aligned_edge=RIGHT)
    lines.move_to(card).align_to(card.get_right() + 0.3 * LEFT, RIGHT)
    out = VGroup(bubble, card, lines)
    out.bubble, out.card, out.lines = bubble, card, lines
    return out


def _half_written_face(width: float) -> Group:
    """Video 2's picture, two thirds written, the cursor at the next cell. .cur"""
    n_done = int(round(2 / 3 * N_TILES * N_TILES))
    tp = tile_patches("base", width=width)
    tc = tile_cells(width=width)
    thumb = VGroup(tc, tp)
    for i in range(n_done, len(tp)):
        tp[i].set_opacity(0)
    cur = cursor(height=0.32 * width / 2.3).move_to(tile_center(n_done, width=width) + thumb.get_center())
    out = Group(thumb, cur)
    out.cur = cur
    return out
