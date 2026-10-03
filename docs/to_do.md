# To-do (human scratchpad)

- [ ] Answer the open questions in `agents_plan.md` §9 (packaging pair, wording, date)
- [ ] Fix the packaging mismatch (plan warning box): the title + thumbnail must say what this video explains
- [ ] Confirm the upload date
- [ ] Verify the claims in the plan's accuracy guardrails before writing VO
- [ ] Write the hook's Arabic lines into `script_visual_map.md`
- [x] Install / link `manim/` (see README): linked to `../1-hour-challenge/manim` (ManimGL 1.7.2), KitDemo renders (3 Oct)

## Handoff (3 Oct, session stopped at the usage limit)

- [ ] Adobe Enhance: was running (37+/56 done). Re-run `.venv/bin/python scripts/enhance_takes.py`; done takes are skipped.
- [ ] Then `.venv/bin/python scripts/process_takes.py`. It now finds speech in the enhanced audio (on the raw takes the
      room noise hid quiet syllables and cut words); check its report has no "cut short" warnings.
- [x] Video-3 kit (`our_scenes/agent_kit.py`, gallery `AgentKitDemo`), `HookShop`, `Bit1Loop` (preview renders)
- [ ] Scenes bits 2–7 (beats: `docs/script_visual_map.md`; same kit, master layout, AgentScene word anchors)
- [ ] HD: `MANIM_HD=1 ./scripts/render_segments.py` → `scripts/narrate.py track` → `scripts/mux_audio.py` →
      `scripts/build_srt_cut.py` Arabic upload-cut command (music bed, caption band, SRT; see its docstring)
