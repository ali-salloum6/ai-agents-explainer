# To-do (human scratchpad)

- [ ] Answer the open questions in `agents_plan.md` §9 (packaging pair, wording, date)
- [ ] Fix the packaging mismatch (plan warning box): the title + thumbnail must say what this video explains
- [ ] Confirm the upload date
- [ ] Verify the claims in the plan's accuracy guardrails before writing VO
- [ ] Write the hook's Arabic lines into `script_visual_map.md`
- [x] Install / link `manim/` (see README): linked to `../1-hour-challenge/manim` (ManimGL 1.7.2), KitDemo renders (3 Oct)

## Handoff (3 Oct, session stopped at the usage limit)

- [x] Adobe Enhance: all 56 chosen takes
- [x] Then `.venv/bin/python scripts/process_takes.py`. It now finds speech in the enhanced audio (on the raw takes the
      room noise hid quiet syllables and cut words); check its report has no "cut short" warnings.
- [x] Video-3 kit (`our_scenes/agent_kit.py`, gallery `AgentKitDemo`), `HookShop`, `Bit1Loop` (preview renders)
- [x] Scenes bits 2–7 (beats: `docs/script_visual_map.md`; same kit, master layout, AgentScene word anchors)
- [x] HD: `MANIM_HD=1 ./scripts/render_segments.py` → `scripts/narrate.py track` → `scripts/mux_audio.py` →
      `scripts/build_srt_cut.py` Arabic upload-cut command (music bed, caption band, SRT; see its docstring)

- [x] Upload cut (3 Oct): `media/output/full_cut_ar.mp4` (1080p, 5:54, voice + "A New Beginning" bed, bottom 20% clear)
      and `media/output/full_cut_ar.ar.srt` (69 cues)
- [x] Packaging decided (5 Oct): `docs/youtube/publish_pack.md` (titles, thumbnails, description, tags, pinned comment, schedule)
- [x] Published: live since Mon 5 Oct 12:46 UTC (the Friday schedule in the pack was not used)
- [x] Read 1 logged (6 Oct): 6 impressions in 13.5 h, none from Browse. See `docs/video3_analytics.md`
- [ ] Today: the four Studio checks in `docs/video3_analytics.md`; make sure the first-hour share went out
- [ ] Prepare the challenger thumbnail (thumbnail only, don't upload) by Tue night
- [ ] Wed 7 Oct ~12:46 UTC (48 h): read impressions by source and apply the decision rule
- [ ] Thu 8 Oct (72 h) and Mon 12 Oct (7 d): log Reads 3 and 4
