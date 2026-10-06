# Video 3: publish pack

Everything to publish the video, decided 5 Oct 2026. Packaging was chosen by learning from video 2 (the packaging that got Ali above 5% CTR), a scan of the Arabic and English "AI agent" shelf, and YouTube's own rules. Rules behind it: [`../../../1-hour-challenge/docs/thumbnail_title_guide.md`](../../../1-hour-challenge/docs/thumbnail_title_guide.md). Plan: [`../agents_plan.md`](../agents_plan.md) §3 and §9.

| What | File |
| --- | --- |
| The video (1080p, 5:54, voice + music bed, bottom 20% clear for captions) | `media/output/full_cut_ar.mp4` (not committed) |
| Subtitles (Arabic, 69 cues) | [`subtitles_ar.srt`](subtitles_ar.srt) |
| Thumbnail, **default** (upload this) | [`thumbnails/thumb_a_loop_1280x720.png`](thumbnails/thumb_a_loop_1280x720.png) (and `_1920x1080`) |
| Thumbnail, challenger | [`thumbnails/thumb_b_riddle_1280x720.png`](thumbnails/thumb_b_riddle_1280x720.png) |
| Description (paste as is) | [`description.txt`](description.txt) |
| How the thumbnails look in a feed | [`thumbnails/packaging_test.png`](thumbnails/packaging_test.png) |

---

## 1. Copy blocks

**Title (default)**

```
كيف الـ AI Agent بيدير محل؟
```

**Pair 2, only for a test or a later swap** (title and thumbnail change together)

```
الـ AI Agent ما بيعرف غير يكتب… كيف أدار محل؟
```

with `thumb_b_riddle_1280x720.png`.

**Tags** (Studio → More options)

```
AI Agent, AI Agents, وكلاء الذكاء الاصطناعي, وكيل الذكاء الاصطناعي, ايجنت, شرح AI Agent, كيف يعمل AI Agent, الذكاء الاصطناعي, شرح الذكاء الاصطناعي, agentic AI, tool use, context window, MCP, Model Context Protocol, Project Vend, Anthropic, Claude, ReAct, AutoGPT, LLM, نماذج اللغة, شرح بالعربي, تعلم الذكاء الاصطناعي
```

**Pinned comment** (post it the moment the video is live, then pin it)

```
لو عندكم AI Agent يدير شغلكم، شو أول أداة بتعطوه ياها؟ 👇
وإذا في شي بالفيديو ما انفهم، اكتبوه هون وبرد عليه. المصادر بالوصف. وبالفيديو الجاي: كيف بنعلّم آلة بزر اللايك؟
```

---

## 2. When to publish (Syria time)

**Friday 9 October 2026, 15:00 (UTC+3).** Upload today (Monday) and schedule it.

- **Why Friday afternoon.** The Arabic-audience guide I checked names **Thursday and Friday** as the best days and **Friday 14:00–17:00 Riyadh time** as the window for the most views in the first 24 hours; the UAE guide has Friday 12:00–21:00 strong and says to avoid Monday and Tuesday. Syria and Riyadh share the same clock (UTC+3, no daylight saving in Syria since 2022), so that window is 14:00–17:00 in Damascus too. 15:00 sits in the middle of it, after the midday prayer and lunch and a few hours before the evening peak, so YouTube has time to test the video on the afternoon audience before the busiest hours. A common rule says to publish 1 to 2 hours before your audience's peak.
- **Same clock this week:** 15:00 in Damascus is 15:00 in Riyadh, Baghdad, Amman and Cairo (Egypt stays on summer time until 29 Oct) and 16:00 in Dubai.
- **Upload today** so HD processing and the music copyright check are finished long before Friday; the days in between are for the checks in §4. Don't publish on Monday or Tuesday.
- **Fallback:** Saturday 10 October, 15:00 (the UAE guide rates Saturday 12:00–21:00 highly). Not Thursday: neither source supports a Thursday-evening slot.
- **Honest limit:** these are marketing-blog recommendations, not data for your channel, and a small channel's first audience is partly whoever you send the link to. Check once in Studio → Analytics → Audience → **When your viewers are on YouTube**; if your own chart shows a clear peak, publish about 2 hours before it.
- In the Schedule box check the time-zone label reads GMT+3, or Studio uses the computer's zone.

---

## 3. Why this packaging

### What the channel's own history says

| | Title | Thumbnail | Result |
| --- | --- | --- | --- |
| Video 1 | «كيف الموبايل بيعرف وجهك؟ الشبكات العصبية» (two promises), then «كيف تعمل الشبكات العصبية؟» | phone + net (two objects), then a dense net | 0.4–0.8% CTR; the shelf placed it next to career and Excel videos |
| **Video 2** | «كيف الذكاء الاصطناعي بيرسم الصور؟» | **the video's own mechanism, one picture, no text:** a face half written, the cursor at the next cell | **above 5% CTR (Ali). The repo's last recorded read, from the first two days, was 1.8% on 222 impressions.** |

What video 2 did that video 1 did not, and what video 3 copies:

1. **One plain question in dialect:** «كيف + AI + the thing it does؟», names the subject in the viewer's own words, with the surprising verb.
2. **One still of the video's own mechanism, no text,** dark ground, one subject, the bottom-right corner empty.
3. **Brand continuity:** the glowing writing cursor. Video 3's still has the same cursor, now the new I-beam.
4. One idea per video; the packaging doesn't make a second promise.

### What the shelf looks like (searched on YouTube, 5 Oct)

- **Arabic "AI Agent" results** are tutorials («كيفية بناء وكلاء…»: 219K views) and hype thumbnails: faces, logos, neon, three lines of text (28K, 45K views). Nobody does a quiet visual explainer. A dark minimal diagram stands out *and* sits in the explainer neighbourhood instead of next to "AI hustle" videos, which is what hurt video 1.
- **English** is plain: «AI Agents, Clearly Explained» (5.2M views).
- **The shop story** exists in Arabic only as one Short (about 2K views): new, but not proven demand. So the title leads with the searchable subject and the task, not the story.

### YouTube rules that shaped it

- Title and thumbnail work as a team; winner of an A/B test is chosen by **watch time**, not CTR.
- A/B tests ("Test & compare"): up to 3 variants, every thumbnail at least 1280×720 (else the whole test drops to 480p), needs Advanced features, desktop Studio, finishes within 2 weeks; if inconclusive the **first** variant uploaded stays.
- No thumbnail may promise something the video doesn't show: every object here appears in the video (the page with its caret is hook.4, the shop is the hook and the world card, the slips are bit 1).

### Decision

| | Pair 1 (publish) | Pair 2 (challenger) |
| --- | --- | --- |
| Title | «كيف الـ AI Agent بيدير محل؟» | «الـ AI Agent ما بيعرف غير يكتب… كيف أدار محل؟» |
| Thumbnail | **the loop:** the page the AI writes → request slip → the shop → result slip back | **the riddle:** the page ? the shop |
| Job | exactly video 2's recipe; the picture is the mechanism, the title the question | the video's hook as a puzzle; stronger curiosity, untested on this channel |
| Why not default | | the claim in the title could pull the "funny story" audience |

Rejected: the master diagram as a thumbnail (turns to mush at 160 px, see the control in `packaging_test.png`), the fridge in a blazer as a portrait (right click, wrong audience), any text on the picture (video 2 worked without it).

Honest limits: nobody can know which pair wins before it runs. Pair 1 is the lowest-risk bet because it copies what already worked here. The channel gets roughly 100 impressions a day, so an A/B test may well end inconclusive; that is why Pair 1 goes first (the first variant is the default).

---

## 4. Upload checklist (Studio on desktop)

- [ ] Upload `media/output/full_cut_ar.mp4`; wait for HD (1080p) processing and the copyright check to finish
- [ ] Title, thumbnail `thumb_a_loop_1280x720.png`, description from `description.txt`
- [ ] If the channel has Advanced features: Title box → **A/B testing** → add Pair 2 as a second variant (Pair 1 first). If Studio refuses a test on a scheduled upload, skip it and use the swap rule in §5
- [ ] Playlist: create «كيف يشتغل الذكاء الاصطناعي من جوا» and add video 2 and this one
- [ ] Audience: **No, not made for kids**; age restriction: no; paid promotion: no; altered or synthetic content: **no** (stylised animation; the voice is Ali's own, cleaned of noise)
- [ ] Tags; language **Arabic**; category Science & Technology
- [ ] Subtitles → Add language → Arabic → upload `subtitles_ar.srt`
- [ ] Card at **0:34** (where the half-written face from video 2 appears): video 2
- [ ] End screen over the last 6 s (5:48–5:54): Subscribe + video 2, small, top corners (the end card already shows like and subscribe)
- [ ] Visibility → **Schedule → Friday 9 Oct 2026, 15:00**; check the GMT+3 label
- [ ] Watch the processed 1080p version once start to finish

---

## 5. After it's live

- **First hour:** post and pin the comment; send the link to 10–20 people who would really watch (AI-curious). Video 1's lesson: a wrong first audience froze the shelf, so the first clicks should come from the right people.
- **Don't touch the title or thumbnail for 72 hours** (video 1: swaps don't reopen a closed shelf; an A/B test also stops if either is edited).
- **At 72 h, with at least 500 impressions** (Studio → Analytics → Reach). These thresholds are a rule of thumb, not data: CTR 4% or more, keep; 2–4%, wait 24 h more; under 2%, swap to Pair 2 (title and thumbnail together) and leave it another 72 h.
- **Revised 6 Oct:** at this channel's volume 500 impressions takes ~5 days (the video had 6 after 13.5 h), so the rule above can't trigger. Use the decision rule in [`../video3_analytics.md`](../video3_analytics.md).
- If CTR is fine but average view duration drops hard, look at the retention graph around 0:26 (video 1 lost cold viewers there; this video pays the title at about 0:25 with «كل اللي بيعرف يعملو إنو يكتب»).
- Record the reads in `docs/video3_analytics.md` like video 2's.

---

## 6. How the files were made

- Stills: `our_scenes/thumbnail.py` (`ThumbLoop`, `ThumbRiddle`, `ThumbMaster` as the control), rendered with
  `.venv/bin/manimgl our_scenes/thumbnail.py ThumbLoop -w -s --hd --video_dir ./media/thumbnails`
  (`-w -s` together saves the last frame; `-s` alone opens a window and waits).
- Exports and the test sheet: `.venv/bin/python scripts/make_thumbnails.py`.
- The cut: `.venv/bin/python scripts/build_srt_cut.py --cues config/cues_ar_vo.json --out media/output/full_cut_ar.mp4 --no-subs --lang ar --music "media/music/No.10 _A New Beginning - Esther Abrami.mp3" --music-lufs -38 --caption-band 0.20`

## 7. Sources

- YouTube Help: [A/B test titles & thumbnails](https://support.google.com/youtube/answer/16391400), [thumbnail & title tips](https://support.google.com/youtube/answer/12340300), [add custom thumbnails](https://support.google.com/youtube/answer/72431)
- Publish-time guidance for Arab audiences: [Arabic guide: Friday 2–5 PM Riyadh time](https://likefawry.com/blog/best-posting-times-each-platform-arab-audience), [UAE guide: Thursday/Friday/Saturday windows](https://rightmedia.ae/blog/best-time-to-post-on-youtube-in-uae-2025-tips-101/); Syria's time zone: [Time in Syria](https://en.wikipedia.org/wiki/Time_in_Syria)
- Facts in the description were checked on the original pages: [Project Vend 1](https://www.anthropic.com/research/project-vend-1), [Project Vend 2](https://www.anthropic.com/research/project-vend-2), [ReAct](https://arxiv.org/abs/2210.03629), [MCP](https://www.anthropic.com/news/model-context-protocol), [AutoGPT](https://en.wikipedia.org/wiki/AutoGPT), [TechCrunch](https://techcrunch.com/2023/04/22/what-is-auto-gpt-and-why-does-it-matter/)
