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
- [x] Read 2 logged (9 Oct): first 3 days = 24 impressions, 4 views; title changed to «كيف ايجنت ذكاء اصطناعي يدير محل؟»; video 2's daily pattern is in its Read 3
- [ ] Confirm in `docs/video3_analytics.md` Read 2: which thumbnail has been live since when
- [ ] Today, 15 min, free: bridges. Cards/end screens on videos 1 and 2 → video 3 (and 3 → 2); playlist «كيف يشتغل الذكاء الاصطناعي من جوا» with videos 2 and 3; pinned comment on videos 1 and 2
- [ ] No more edits to video 3's title, thumbnail or description before Mon 19 Oct
- [ ] Mon 12 Oct (day 7): impressions by source, Search terms. Mon 19 Oct (day 14): the verdict read
- [ ] Studio, for the notes: video 2's publish time of day; lifetime watch time + average view duration; Reach → Suggested videos (which videos showed it)
- [ ] Video 4: start (plan and data in `../ai-rl-explainer`)
