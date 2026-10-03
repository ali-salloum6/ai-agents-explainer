"""
KitDemo — exercises every element of our_scenes/kit.py on screen (~20 s).
Not a video beat; a visual test bench for the shared kit.

Render (preview 854×480):
  .venv/bin/manimgl our_scenes/kit_demo.py KitDemo -w -l --video_dir ./media
Keyframes:
  python3 scripts/export_keyframes.py --segment kit_demo --video media/KitDemo.mp4 --count 12
"""
from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from our_scenes.kit import *  # noqa: F401,F403  (also re-exports manimlib)


class KitDemo(Scene):
    def construct(self):
        self.camera.background_rgba = list(color_to_rgba(BG))

        # ---- 1. hero at three sizes + smooth photo ----------------------------------------
        big = hero_pixels("base", width=4.4).move_to(3.4 * LEFT + 0.6 * UP)
        mid = hero_pixels("base", width=2.4).next_to(big, RIGHT, buff=0.5).align_to(big, UP)
        small = hero_pixels("base", width=1.2).next_to(mid, DOWN, buff=0.3).align_to(mid, LEFT)
        photo = hero_image("base", width=2.4).next_to(mid, RIGHT, buff=0.5).align_to(big, UP)
        photo_small = hero_image("base", width=1.2).next_to(photo, DOWN, buff=0.3).align_to(photo, LEFT)
        self.add(big, mid, small, photo, photo_small)
        self.wait(1.0)

        # ---- 2. tile grid + patches + glyph tray ---------------------------------------------
        cells = tile_cells(width=4.4).move_to(big)
        self.play(ShowCreation(cells, lag_ratio=0.01, run_time=0.8))
        patches = tile_patches("base", width=4.4).move_to(big)
        self.remove(big)
        self.add(patches)
        grid = VGroup(cells, patches)
        self.play(grid.animate.space_out_submobjects(1.06), run_time=0.6)
        self.play(grid.animate.space_out_submobjects(1 / 1.06), run_time=0.6)
        tray = glyph_tray(size=0.42).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(tray, shift=0.3 * UP, lag_ratio=0.05, run_time=0.8))
        self.wait(0.6)

        # ---- 3. cards flipping to patches -----------------------------------------------------------
        self.play(FadeOut(mid), FadeOut(small), FadeOut(photo), FadeOut(photo_small), run_time=0.4)
        idxs = [tile_index(2, 2), tile_index(3, 4), tile_index(0, 6)]
        fronts = VGroup(*[glyph_card(glyph_for_tile("base", i), size=0.8) for i in idxs])
        fronts.arrange(RIGHT, buff=0.5).move_to(2.2 * RIGHT + 1.4 * UP)
        self.play(FadeIn(fronts, lag_ratio=0.2, run_time=0.5))
        backs = [patch_card("base", i, size=0.8) for i in idxs]
        for f, b in zip(fronts, backs):
            self.play(flip_card(f, b, run_time=0.5))
        self.wait(0.5)

        # ---- 4. cursor writing three tiles on the grid + a candidate fan ----------------------------
        cur = cursor(height=0.44).move_to(tile_center(idxs[0], width=4.4) + patches.get_center())
        cur.shift(0.0 * RIGHT)
        self.add(cur)
        self.play(blink(cur, n=2, period=0.35))
        written = [tile_index(4, 1), tile_index(4, 2), tile_index(4, 3)]
        hidden = VGroup(*[patches[i] for i in written])
        hidden.set_opacity(0)
        fan = candidate_fan([3, 10, 7], [0.62, 0.27, 0.11], size=0.42)
        fan.next_to(patches, RIGHT, buff=0.3).align_to(cur, UP)
        for i in written:
            c = tile_center(i, width=4.4) + patches.get_center()
            self.play(cur.animate.move_to(c), run_time=0.25)
            if i == written[0]:
                self.play(FadeIn(fan, lag_ratio=0.15, run_time=0.4))
                self.wait(0.4)
                self.play(FadeOut(fan, run_time=0.25))
            card = glyph_card(glyph_for_tile("base", i), size=0.5).move_to(c)
            self.play(FadeIn(card, scale=0.6, run_time=0.2))
            self.play(FadeOut(card, run_time=0.15), patches[i].animate.set_opacity(1), run_time=0.25)
        self.wait(0.4)

        # ---- 5. chat: bubble + reply card + ribbon of chips -----------------------------------------
        self.play(FadeOut(VGroup(fronts, *backs, cur)), FadeOut(tray), run_time=0.4)
        bub = user_bubble(REQUEST_AR, width=4.5).move_to(3.3 * RIGHT + 2.6 * UP)
        card = reply_card(width=4.5, height=3.2).next_to(bub, DOWN, buff=0.25)
        pic = hero_image("base", width=2.6).move_to(card)
        self.play(FadeIn(bub, shift=0.2 * DOWN), run_time=0.5)
        self.play(FadeIn(card), FadeIn(pic), run_time=0.5)
        line = ribbon(
            [word_chip(w) for w in REQUEST_AR.split(" ")]
            + [glyph_card(glyph_for_tile("base", i), size=0.5) for i in range(0, 5)]
            + [ellipsis_mark(0.5)],
            height=0.5,
        )
        line.move_to(np.array([0.0, RIBBON_Y, 0.0]))
        self.play(FadeIn(line, lag_ratio=0.1, run_time=0.8))
        self.wait(0.8)

        # ---- 6. printer box + snow sequence ------------------------------------------------------------
        self.play(FadeOut(VGroup(patches, cells, bub, card)), FadeOut(pic), FadeOut(line), run_time=0.4)
        writer = model_box(label_ar=None).move_to(4.2 * LEFT + 1.0 * UP)
        printer = printer_box().next_to(writer, RIGHT, buff=1.2)
        snow = snow_pixels("base", width=2.4, level=1.0).next_to(printer, RIGHT, buff=1.0)
        strip = soft_strip("alt_portrait", width=3.0, height=0.5)
        strip.move_to(np.array([0.0, RIBBON_Y, 0.0]))
        self.play(FadeIn(writer), FadeIn(printer), FadeIn(snow), FadeIn(strip), run_time=0.6)
        for lvl in (0.75, 0.5, 0.25, 0.0):
            self.play(recolor_to(snow, snow_array("base", lvl)), run_time=0.5)
            self.wait(0.15)
        self.wait(0.4)

        # ---- 7. two same-silhouette boxes + safe rect + family label ------------------------------------
        self.play(FadeOut(snow), FadeOut(strip), run_time=0.3)
        box_a = model_box(label_ar=None)
        box_b = model_box(label_ar=None)
        VGroup(box_a, box_b).arrange(RIGHT, buff=1.4).move_to(1.0 * UP)
        fam = ar_text(FAMILY_LABEL_AR, font_size=30, color=INK_2).next_to(VGroup(box_a, box_b), DOWN, buff=0.35)
        safe = safe_rect()
        self.play(Transform(writer, box_a), FadeIn(box_b), printer.animate.next_to(box_b, RIGHT, buff=0.8).shift(0.0 * UP), run_time=0.6)
        self.play(FadeIn(fam), ShowCreation(safe), run_time=0.5)
        self.wait(0.6)

        # ---- 8. the four (six) hero variants side by side -------------------------------------------------
        self.play(FadeOut(VGroup(writer, box_b, printer, fam)), FadeOut(safe), run_time=0.3)
        variants = ["base", "dark_sky", "hat", "sign", "alt_portrait", "alt_hat"]
        row = Group(*[hero_image(v, width=1.8) for v in variants]).arrange(RIGHT, buff=0.18).move_to(2.2 * UP)
        self.play(FadeIn(row, lag_ratio=0.1), run_time=0.8)
        # thumbnail test: two-thirds assembled, cursor at the next cell
        n_done = int(round(2 / 3 * N_TILES * N_TILES))
        thumb_w = 3.4
        tp = tile_patches("base", width=thumb_w)
        tc = tile_cells(width=thumb_w)
        thumb = VGroup(tc, tp).move_to(1.35 * DOWN)
        for i in range(n_done, len(tp)):
            tp[i].set_opacity(0)
        cur2 = cursor(height=0.36).move_to(tile_center(n_done, width=thumb_w) + thumb.get_center())
        self.play(FadeIn(tc), FadeIn(tp[:n_done], lag_ratio=0.01), FadeIn(cur2), run_time=0.8)
        self.play(blink(cur2, n=3, period=0.4))
        self.wait(1.0)


# ----------------------------------------------------------------------------------------------
# Video 3's kit (our_scenes/agent_kit.py): four pages, ~2 s each.
#   .venv/bin/manimgl our_scenes/kit_demo.py AgentKitDemo -w -l --video_dir ./media
# ----------------------------------------------------------------------------------------------
from our_scenes import agent_kit as ak  # noqa: E402


class AgentKitDemo(Scene):
    def construct(self):
        self.camera.background_rgba = list(color_to_rgba(BG))

        # ---- 1. the master diagram, finished: guide, writer, hands, world, desk, notebook, loop ----
        m = ak.master(guide=True, desk_on=True)
        slips = VGroup(*[ak.slip(kind="request" if k % 2 else "result", width=0.95, seed=k).move_to(ak.desk_slot(k, 5))
                         for k in range(5)])
        nb = ak.notebook(0.8, 0.95).move_to(np.array([ak.DESK_X1 - 0.55, ak.SLIP_Y + 0.12, 0]))
        req = ak.slip(ak.REQUEST_SLIP_AR, font_size=24).next_to(m.to_hands, UP, buff=0.12)
        page1 = VGroup(m.view, m.guide, m.writer, m.hands, m.world, m.to_hands, m.to_world, m.back, m.desk, slips, nb, req)
        self.add(page1, ak.loop_ring(radius=3.6, opacity=0.25))
        self.wait(2.0)
        self.clear()

        # ---- 2. the shop and the icons ----
        fr = ak.fridge(3.2).move_to(np.array([-3.6, 0.2, 0]))
        pad = ak.ipad(1.1).next_to(fr, RIGHT, buff=0.4).align_to(fr, DOWN).shift(0.9 * UP)
        icons = VGroup(ak.icon_box(), ak.icon_tag(), ak.envelope(), ak.icon_bubble(), ak.icon_search(), ak.icon_note(),
                       ak.icon_shelves(), ak.icon_can(), ak.icon_chips(), ak.icon_cube(), ak.icon_percent(), ak.icon_gift(),
                       ak.icon_star(), ak.icon_clock(), ak.icon_calendar(0.7), ak.icon_blazer(0.9), ak.icon_button(),
                       ak.icon_supplier(), ak.icon_check(), ak.icon_cross(), ak.question_mark(0.6), ak.thumbs_up())
        icons.arrange_in_grid(4, 6, buff=0.35).move_to(np.array([2.6, 0.2, 0]))
        phone = ak.icon_phone(2.0).move_to(np.array([6.0, -2.4, 0]))
        self.add(fr, pad, icons, phone)
        self.wait(2.0)
        self.clear()

        # ---- 3. the tools guide, the filled row, the price menu (before / after round two) ----
        g = ak.tools_guide().move_to(np.array([-3.3, 1.2, 0]))
        filled = ak.filled_row_slip(["المورّد", "أربعين علبة كولا"]).next_to(g, DOWN, buff=0.4)
        pm = ak.price_menu().move_to(np.array([3.3, 1.6, 0]))
        pm2 = ak.price_menu(show_cost=True, title=False).next_to(pm, DOWN, buff=0.3)
        self.add(g, filled, pm, pm2)
        self.wait(2.0)
        self.clear()

        # ---- 4. desk pieces, the dial, plugs and the socket, the English chips ----
        row = VGroup(ak.job_card(), ak.todo_card(), ak.notebook(), ak.slip(kind="result", width=1.0, n_lines=3),
                     ak.checklist_card()).arrange(RIGHT, buff=0.3).move_to(np.array([0, 2.3, 0]))
        d = ak.dial(1.3).move_to(np.array([-4.0, -1.3, 0]))
        d.set_value(0.85)
        plugs = VGroup(*[ak.plug(k) for k in range(5)], ak.plug(-1)).arrange(RIGHT, buff=0.3).move_to(np.array([1.0, -0.6, 0]))
        sock = ak.socket().next_to(plugs, RIGHT, buff=0.5)
        chips = VGroup(ak.chip_en(ak.AGENT_EN), ak.chip_en(ak.CONTEXT_EN, color=INK_2),
                       ak.en_text(ak.TRANSCEND_EN, 30, WARM)).arrange(RIGHT, buff=0.4).move_to(np.array([1.8, -2.6, 0]))
        self.add(row, d, plugs, sock, chips)
        self.wait(2.0)
