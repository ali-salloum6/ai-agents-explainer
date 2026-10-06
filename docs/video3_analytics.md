# Video 3 analytics — «كيف الـ AI Agent بيدير محل؟»

Packaging live: Pair 1 from [`youtube/publish_pack.md`](youtube/publish_pack.md): the title above, thumbnail `thumb_a_loop`, the description, tags and Arabic subtitles. Per Studio it went live **Mon 5 Oct 2026, 12:46 UTC (15:46 Syria)**. The pack had planned a Friday 9 Oct 15:00 schedule; the video went public on upload day instead.

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
- Swapped at: _(time, Syria)_ to: _(candidate)_
- The 48 h rule above now runs from the swap, and CTR counts only impressions after it.
- "Test & compare" can't resolve at ~11 impressions a day; once the video has a few hundred, a c-vs-d test is the one worth running.

### Open
- Report back: the four checks, then the 48 h numbers by source.
- Upload the chosen candidate (thumbnail only) and fill in the swap time above.
- Video 4's thumbnail needs one focal point at stamp size; learn from this before it's drawn.
