# Video 3 analytics — «كيف الـ AI Agent بيدير محل؟»

Packaging live: Pair 1 from [`youtube/publish_pack.md`](youtube/publish_pack.md): the title above, thumbnail `thumb_a_loop`, the description, tags and Arabic subtitles. Per Studio it went live **Mon 5 Oct 2026, 12:46 UTC (15:46 Syria)**. The pack had planned a Friday 9 Oct 15:00 schedule; the video went public on upload day instead. **Packaging has changed since: see Read 2.**

## Read 1: 6 Oct 2026 (~13.5 h after upload)

Source: Studio's numbers as read out by YouTube's built-in assistant and passed on by Ali; no screenshots yet.

| Metric | Value |
|---|---|
| Views | 0 (Studio can lag; also check whether the pack's first-hour share went out) |
| Thumbnail impressions | 6 |
| Impression sources | YouTube search 5, Suggested videos 1, **Browse features (Home) 0** |
| Thumbnail CTR | 0% (0 of 6) |

**Same stage, video 2** (its first-read charts, eyeballed ±15; see `../../ai-image-explainer/docs/video2_analytics.md`): about 180 impressions in the first ~4 h, 222 by 1.9 days, 73% of them "from YouTube recommending your content" at Read 1; its flat stretch ran about 110 impressions a day, and its Browse wave began at day ~2.6. Video 3: 6 impressions in 13.5 h (about 11 a day), none from Browse.

### What YouTube's assistant said

Ali asked why the video had zero views, then whether to change the thumbnail or wait (his packaging is built for Home, most impressions came from search).
- It called this normal: published ~13 h ago, analytics lag 24–48 h, 6 impressions is too few to read, a 0% CTR on 6 means little.
- Advice: **wait.** Let it reach 100–300 impressions across Browse and Home before judging; Browse "takes 24–48 hours to pick up"; changing now "interrupts the initial calibration".
- Its thresholds: healthy CTR "typically 4–8%+" for the niche; test a new thumbnail only if impressions stay flat after 48 h or Browse CTR stays under 2–3%.
- If preparing a backup: high contrast, a clean focal point, clear curiosity.

**How much to trust it:** the facts about this video (6 impressions, 5 search + 1 suggested, publish time) are Studio's. The benchmarks and the "calibration" claim are generic and unsourced, and "Browse picks up in 24–48 h" doesn't match this channel's own video 2, whose recommendation test showed up within hours.

### Reading
- **This isn't a thumbnail verdict.** CTR is clicks ÷ impressions: 0 of 6, five of them searchers, says nothing. And a thumbnail can't cause low impressions; it only matters once YouTube shows it.
- **It is a distribution anomaly.** No Browse/Home impressions at all in 13.5 h, where video 2 had ~180 in 4 h. Cause unknown. In the order worth checking:
  1. Something blocking it in Studio (still processing at SD, a copyright claim or Restrictions entry, audience set wrong, visibility).
  2. The first test audience is likely people who watched the channel's recent videos; for this channel that is a small, mostly short-watch group (video 2's wave viewers averaged ~25 s; 9 unique viewers at its Read 2). A guess, not checkable.
  3. Timing: Monday 15:46 Syria instead of Friday. Unknown effect.
  4. The packaging read as not worth testing on Home. Unknowable.
- **Search works.** Five impressions came from searches, so the title is indexed and matches queries. Studio shows the actual search terms.
- **The thumbnail, by inspection** (`youtube/thumbnails/packaging_test.png`): clean and consistent with the video, but two outlined boxes of equal weight and no focal point; the right object reads as a phone or vending machine, not a shop; no face, which was the strongest anchor in video 2's thumbnail; at 160 px the arrows and slips turn to texture. Plausibly weaker than video 2's. **Unproven until Browse impressions exist.**

### Checks today (10 min in Studio)
1. Content → this video: **Restrictions** column (any copyright note; the bed is Esther Abrami, "A New Beginning"), Visibility = Public, Audience = *not made for kids*, HD processing finished.
2. Analytics → Reach → traffic sources → YouTube search → **search terms** that produced the 5 impressions.
3. Did the link go to the 10–20 AI-curious people in the pack's §5? External shares create views, not impressions.
4. Video 2 now: still getting Home impressions? If it is, the channel's Browse attention may be busy there; log it in its own file.

### Decision rule (replaces the pack's §5 "500 impressions at 72 h", unreachable here)

_Superseded on 9 Oct: with ~7 impressions a day and two packaging changes this rule can't be applied. See Read 2 → Plan._

Times: **48 h = Wed 7 Oct 12:46 UTC (15:46 Syria)**, 72 h = Thu 8 Oct, 7 days = Mon 12 Oct.
Judge CTR on **Browse/Home impressions only** (Reach → traffic source types → Browse features), not the blended figure; search CTR is a different animal.

| At 48 h | Do |
|---|---|
| ≥ 100 impressions, Browse the majority | CTR ≥ 4%: keep. 2–4%: wait 24 h. < 2%: swap the **thumbnail only** (challenger below), keep the title |
| < 50 impressions, almost all search | Not a packaging problem: don't swap. Do the checks, make sure the share went out, wait through day 3–4 (video 2's wave began at day 2.6), re-decide at 7 days |
| In between | Wait 24 h |

At 7 days, if total impressions are still < 100: swap the thumbnail anyway as a relaunch experiment; there is nothing left to lose. A/B "Test & compare" can't resolve at ~11 impressions a day, so don't use it.

### Thumbnail swap (6 Oct)
Ali decided to replace the thumbnail now, without waiting for 48 h: the loop picture has two boxes of equal weight, no focal point and a right-hand object that reads as a phone. **Thumbnail only; the title stays** (it is what brings the search impressions).

Five simple candidates, one or two objects each, built from the video's own palette, cursor and drawings: [`youtube/thumbnails/candidates/`](youtube/thumbnails/candidates/) (sheet: `candidates_sheet.png`, phone feed and 160 px next to the current thumbnail and video 2's; source: `scripts/thumb_candidates.py`, needs only Chrome/Chromium):

| | Candidate | What it is | Reads as |
|---|---|---|---|
| c | `thumb_c_shopkeeper` | the shop fridge with the iPad as a smiling face and the red tie from the hook | "an AI runs a shop": a face to land on, the title's object |
| d | `thumb_d_writes` | «بس بيكتب» (it only writes) + the writing cursor | the video's thesis as a hook word; the highest-contrast of the five |
| e | `thumb_e_request` | one typed request, «ابعت إيميل», an envelope flying out | the mechanism: words turn into actions |
| f | `thumb_f_ring` | the agent loop as one glowing ring, the cursor in the middle | the simplest; may read as a "refresh" icon |
| g | `thumb_g_cube` | one metal cube with a falling price tag | the shop's first strange moment; the most "story", least "explainer" |

**Pick: c first, d second.** They are the two with a real hook (a face; a hook word), and c follows the guide's split: the thumbnail shows the object, the title asks the question. Each file comes in 1280×720 (upload) and 1920×1080.

**Log the swap.** Write the exact time and which candidate here, so reads before and after can be told apart:
- Swapped at: 6 Oct, after ~03:00 UTC (exact time not recorded), to: **c** (Ali, 9 Oct)
- The 48 h rule above now runs from the swap, and CTR counts only impressions after it.
- "Test & compare" can't resolve at ~11 impressions a day; once the video has a few hundred, a c-vs-d test is the one worth running.

### Open
- Report back: the four checks, then the 48 h numbers by source.
- ~~Upload the chosen candidate and fill in the swap time~~ (done 6 Oct, see Read 2).
- Video 4's thumbnail needs one focal point at stamp size; learn from this before it's drawn.

## Read 2: 9 Oct 2026 (~3.5 days after upload; data through ~8 Oct)

Source: Studio's numbers as read out by YouTube's built-in assistant in a longer chat with Ali. Only its figures are recorded. Its explanations (topic size, "each video is judged independently", title ideas, and the claim that 4.17% CTR and 53% retention show the content resonates) are opinions without data and are left out. Its video 2 figures match Ali's earlier screenshots, so its numbers look like Studio's.

### Packaging changes (facts)
- **Thumbnail:** candidate c (the shop fridge with a face on its screen and the red tie; Ali calls it "the vending machine with a face on top") has been live since **6 Oct**: Ali uploaded it as soon as it was generated, so after ~03:00 UTC (the candidates were committed at 02:58 UTC), about 14 h after publishing. Exact time not recorded.
- **Title**, changed by Ali during the 8–9 Oct chat (~3.5 days in): «كيف AI Agent بيدير محل؟» → «كيف ايجنت ذكاء اصطناعي يدير محل؟». Ali's reason: the successful video's title had no Latin letters.
- **So the first 3 days mix two thumbnails and one title:** the loop thumbnail (a) for the first ~14 h (the 6 impressions of Read 1 were all under it), then c for the rest (≈ 18 of the 24 impressions), all under the old title.

| State | From | To |
|---|---|---|
| Old title + loop thumbnail (a) | Mon 5 Oct 12:46 UTC | 6 Oct, after ~03:00 UTC |
| Old title + c | 6 Oct | ~8–9 Oct |
| New title + c | ~8–9 Oct | now (stable; no more edits planned before 19 Oct) |

### First 3 days, video 2 vs video 3 (the assistant's table)

| | Video 2 | Video 3 |
|---|---|---|
| Impressions | 347 | 24 |
| Views | 36 | 4 |
| CTR | 3.17% | 4.17% |
| Average % viewed | 36.51% | 53.42% |

- **4.17% of 24 is exactly 1 click, and 53.42% of 5:54 (≈ 3:09) is the average of 4 views.** n = 1 and n = 4: neither number says anything about quality, in either direction.
- **Impressions since Read 1:** 6 at 13.5 h → 24 at 3 days, about 7 a day. That is video 2's level after its wave (5–8 a day), with no wave before it.
- The sources of the 24 weren't given (the first 6 were 5 search + 1 suggested).
- 4 views against 1 click: video 2 shows the same gap (views ≈ 3× the clicks CTR implies), so it isn't evidence of how many came from shares.

### Video 2's pattern, for comparison (details in its Read 3)
Browse wave ≈ 30 Sep – 2 Oct (≈ 430 impressions and 65 views in 3 days) at 5.36% Browse CTR; Suggested 172 impressions, 0 clicks; then 10 impressions on 3 Oct and 5–8 a day since. Lifetime to 8 Oct: just over 800 impressions, ~106 views.

### Three videos side by side

| | Video 1 | Video 2 | Video 3 |
|---|---|---|---|
| Title now (Studio id) | «كيف بتشتغل الشبكات العصبية؟ أساس الذكاء الاصطناعي» (gB0a33ZZYmE) | «كيف الذكاء الاصطناعي بيرسم الصور؟» (C-31-hB0-cY) | «كيف ايجنت ذكاء اصطناعي يدير محل؟» (HygDWiw5PS0), first «كيف AI Agent بيدير محل؟» |
| Latin letters in the title | none | none | at first; none now |
| Length | 14:24 | 3:48 | 5:54 |
| Published | not recorded here | Sun 27 Sep 2026 (time of day: check Studio) | Mon 5 Oct 2026, 12:46 UTC (15:46 Syria) |
| Thumbnail | phone + net, then a dense net | a half-written face, no text | the loop picture, then candidate c (the shop fridge with a face) |
| Impressions | 1,051 lifetime (to 13 Sep); hundreds on day 1, mostly Suggested | 347 in 3 days; just over 800 by 8 Oct | 24 in 3 days |
| Views | ~80 lifetime: ~66 friends/direct, ~14 impression clicks | 36 in 3 days; ~106 by 8 Oct | 4 in 3 days |
| Where impressions came from | mostly Suggested | Browse 560, Suggested 172, Search ~81 | not split; first 13.5 h: 5 search, 1 suggested |
| CTR | 0.4–0.8% day one; 1.33% lifetime | 3.17% (3 days); 5.36% on Browse; 0% on Suggested | 4.17% = 1 click of 24 |
| Average % viewed | ~7.5% per raw view (1:05); friends 14.8% | 36.5% (3 days), ~30% (6 days) | 53.4% over 4 views |

Video 1's column is from `../../ai-image-explainer/docs/image_plan.md` §1.

### Retracted from Read 1
Hypothesis 2 ("the first test audience is a small, mostly short-watch group; video 2's wave viewers averaged ~25 s") rested on a wrong figure. It came from a lagging watch-time card; the processed retention of video 2's wave viewers was about a minute of 3:48. **Why video 3 got no Browse test is unknown.** Videos 2 and 3 differ in topic, title (Latin letters or none), thumbnail (a face or an abstract picture), publish time and first-hour audience; one pair of videos can't separate them. Video 1 had no Latin letters in its title either and also froze, so the title alone doesn't explain the pattern.

### Plan (supersedes the 48 h decision rule in Read 1)
- **No more edits** to title, thumbnail or description until **Mon 19 Oct** (day 14; 10 days after the title change). At ~7 impressions a day nothing can be learned from further changes, and each one muddies the read.
- **Reads:** Mon 12 Oct (day 7): impressions by source and the Search terms (do they still match the Arabic title?). Mon 19 Oct (day 14): the verdict read.
- **Free bridges, today:** cards and end screens on videos 1 and 2 pointing to video 3 (and 3 → 2); a playlist «كيف يشتغل الذكاء الاصطناعي من جوا» with videos 2 and 3; a pinned comment on videos 1 and 2.
- **Next video:** don't wait for video 3's verdict. Start video 4 (`../../ai-rl-explainer/docs/rl_plan.md` §0 has the data to design against).

