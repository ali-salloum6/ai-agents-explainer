# Video 3 plan — how AI agents work, through the AI shopkeeper

Status: **full draft, 2 Oct 2026.** Structure agreed with Ali on 1 Oct; everything else here (packaging candidates, beat details, draft lines, vocabulary) is a proposal for Ali to approve, cut or rewrite. Nothing is locked. Per [`instructions.md`](instructions.md): Ali writes the Arabic, approves the visual plan per bit, and only then Manim.

> [!WARNING]
> **Packaging must say "explainer", not "funny story".** This channel is a visual explainer of technical concepts (Computerphile balance, a little less technical), **not Al-Da7ee7 style**. The shop is the case study; the diagrams are the video. A fridge in a blazer with «خلّوا الذكاء الاصطناعي يدير محل…» is a strong click, but **nothing in it tells the viewer they are about to watch an explainer of how AI agents work.** The wrong audience clicks, leaves when the diagrams start, and YouTube scores packaging on watch time.
>
> **Test before locking:** a cold viewer who sees only the thumbnail + title must be able to say "this explains how AI agents work." §3 proposes three pairs built to pass it: every title names the subject (AI Agent) and every thumbnail shows the loop, with the fridge as one node in it, never as a portrait.

Contents: §0 accuracy · §1 why this video · §2 promise · §3 packaging · §4 visual language · §5 beats · §6 facts and sources · §7 production · §8 risks · §9 open questions

---

## 0. Accuracy guardrails

| Claim | What is on record | How to say it |
| --- | --- | --- |
| The shop failed in these specific ways | Project Vend 1: priced "without doing any research", sold metal cubes below cost, gave "numerous discount codes", asked for payment to a hallucinated account, the blazer/tie episode | As written. It was **Anthropic's own experiment with Andon Labs** (humans restocked the fridge). Say "an AI company ran this experiment", name Anthropic once in VO if Ali wants, no logo |
| *Why* it thought it was human | Anthropic: unclear what triggered it | Never "this is what happened inside it." The desk beat explains why **long tasks drift in general**; the identity crisis is shown as an example of drift, framed «ما حدا بيعرف بالزبط ليش، بس…» |
| Why it gave everything away | Anthropic: its training "as a helpful assistant made it far too willing to immediately accede to user requests" | Their words, nearly verbatim. Mechanism of that training is video 4: one dial here, no RLHF details |
| Phase 2 got profitable thanks to small changes | Phase 2: better models **and** CRM, cost visibility, checklists/procedures, a CEO agent. Discounts −~80%, free items halved, weekly losses largely gone | Credit the **combination**, including newer models. Never "only a checklist fixed it." "Mostly stopped losing money", not "became a business" |
| An agent is a model in a loop that writes actions | The standard design (ReAct 2022; every tool-calling API since) | Safe. Simplification: we show one line written per lap; real agents may write several tool calls per lap |
| The model "can't do anything, only writes" | True of the model; the harness executes | Safe and the spine. Callback to video 2 («بيكتب، ما بيرسم») |
| MCP is the shared socket | Anthropic, Nov 2024; OpenAI adopted Mar 2025; Google/Gemini support Apr 2025 | "A shared standard most big labs adopted." Not "the only way" |
| Context window = a desk of fixed size; old pages fall off | Fixed context length is real. *What* falls off is a harness choice (truncate, summarize, notes) | Show the harness's options as choices: notes, summaries, to-do list. Don't claim every product drops the oldest page |
| Long inputs make models worse even before the desk is full | Chroma "Context Rot" (Jul 2025), 18 models | Optional line: «حتى قبل ما تتعبّى الطاولة، كل ما كترت الورقات، بيصير يقرا أسوأ» |
| Keeping mistakes visible helps | Manus "context engineering" (Jul 2025): leave failed actions in context; todo.md recitation | Say "one company that builds agents found…", no brand on screen |
| Better tools > better prompt | SWE-agent (2024): with a purpose-built interface, GPT-4 Turbo solved 12.5% of SWE-bench issues vs 3.8% earlier best (a different, non-agent method) | If used, compare to "the best result before it", **not** "the same agent with worse tools" |
| AutoGPT went viral and went in circles | Released 16 Mar 2023; #1 trending on GitHub 3 Apr; 100k stars by 21 Apr; known for loops, hallucinations, cost | Safe as history |
| Agents are now consumer products | Meta Muse (Sep 2026, topped the US App Store), OpenAI dots (29 Sep 2026) | One line max, no logos, no product claims beyond "agents you can message" |

## 1. Why this video (what we carry forward)

| Lesson | Source | Apply here |
| --- | --- | --- |
| Video 2's packaging earned a Browse test (29 of 30 new views in one day from Home), but the wave's viewers watched ~25 s each | `../ai-image-explainer/docs/video2_analytics.md` Read 2 | The first 30 s decide everything. Title paid by ~0:25 with the first mechanism visible, not a long story setup |
| Video 1 lost cold viewers at 0:26, right after a «لحتى نفهم…» gate | `../ai-image-explainer/docs/image_plan.md` §1 | No gates. Each beat opens on the question the last beat raised |
| One idea per video; dual promises read badly on the shelf | video 1 launch notes | One idea: **an agent is a writer in a loop.** Everything else (menu, desk, training, fixes) hangs off it |
| Diagram-only thumbnails stayed at ~1.3% (video 1) and ~2.7% (video 2) CTR | analytics | Add a story object to the diagram, but keep the diagram (see the warning) |
| Topic is in the news: Muse and dots, late Sep 2026 | §6 | Timeless video; the news is one closing line |
| Ali found video 2 thin compared with video 1 | chat, 1 Oct | Depth without math: the loop, the menu, the desk and the fixes are all real mechanisms, each shown completely |

## 2. Promise

**One sentence:** an AI agent is a model that only writes, put in a loop with a menu of tools and a desk of limited size; the shop shows what breaks and which small changes make it work.

**Audience:** a curious general Arabic viewer who has used a chatbot and heard "AI agents" but never seen inside one. Not a developer tutorial.

**After watching, the viewer can explain:**
1. The model never touches anything: it writes a request, a program carries it out, the result is written back, and it goes round again.
2. It knows its tools only from a written menu, and it only knows what is on its desk; long jobs overflow the desk.
3. Small changes around the model (what the menu shows, notes, checklists, a second checker) change the result a lot.

## 3. Packaging

Rules (from video 1's `thumbnail_title_guide.md`, unchanged): one subject at 160 px, dark ground, bottom-right empty, thumbnail text 0–3 words and never a repeat of the title, title hook in the first words, nothing the video doesn't show.

**New rule for this channel (the warning):** the title names the subject and the thumbnail shows the mechanism. The story is the hook *inside* that frame.

| Pair | Title | Thumbnail | Why |
| --- | --- | --- | --- |
| **A (proposed day-one)** | «الـ AI Agent ما بيعرف غير يكتب… كيف أدار محل؟» | **The loop as the picture:** the teal model box on the left writes a slip; an arrow carries it to the fridge on the right (navy blazer, red tie, iPad face); a slip comes back. Three objects on one circle; no text | Subject (AI Agent) and the video's core idea (it only writes, the channel's thread from video 2) in the title; story in the picture; the loop says "diagram explainer" at a glance |
| **B (subject-first)** | «كيف بيشتغل الـ AI Agent؟ جرّبوه بمحل حقيقي» | The finished master diagram large (model, desk, menu, world), the fridge small as the "world" node | Most search-friendly and most honest; weakest Browse hook |
| **C (story-first with a subject tail)** | «خلّوا الذكاء الاصطناعي يدير محل لحالو \| AI Agents» | Fridge in blazer, big, with the loop arrow drawn around it | Strongest click; the subject tail is the first thing mobile truncation eats, so it is the riskiest for the warning |

- **A/B (Studio, title + thumbnail pairs):** A vs C. They differ in layout and promise, so the test resolves faster; the winner is judged on watch time. If no test: ship A.
- **Description, first line (search MSA, above the fold):** «شرح طريقة عمل وكلاء الذكاء الاصطناعي (AI Agents) بالرسم: الحلقة، الأدوات، والذاكرة — من خلال تجربة حقيقية لذكاء اصطناعي أدار محل.» Then chapters, sources (Project Vend 1 and 2, MCP, Vending-Bench), music credit. English terms (AI agent, tool use, context window, MCP) in the description, not the title.
- **Not testing:** fridge portrait with no loop; «أنا إنسان» text; product names or logos; robot hands.
- Thumbnails get drafted as Manim stills in `our_scenes/thumbnail.py` once the master diagram exists, so they are built from the video's own pictures (video 2's rule).

## 4. Visual language

**The master diagram** (grows one part per bit; the recap is the finished drawing):

```
            ┌──────────── the menu (tools) ────────────┐
            │  email · Slack · search · notes · prices  │
            └───────────────────────────────────────────┘
                 ▲ reads                    │ request slip
   the desk ──► [ MODEL: writes one line ] ─┴──► small program ──► the world
 (context window)        ▲                                      (supplier, customers, fridge)
                         └────────── result slip lands on the desk ◄──┘
```

| Element | Look | Built from |
| --- | --- | --- |
| The model | Teal (ACCENT) box with a blinking cursor; it only ever produces text | `model_box`, `cursor` (kit) |
| A slip | Small card with one written line (a request or a result); requests teal-edged, results amber-edged | `word_chip` / `reply_card` (kit), new `slip()` |
| The program | A small plain grey box that is clearly *not* smart: it only follows a slip | new, MUTED stroke |
| The menu | A card with rows: tool name + one-line description + empty blanks | new `menu_card()` |
| The desk | A tray of fixed width; slips stack left to right; when full, the oldest slide off the edge | new `desk()` |
| Notes / to-do | A notebook card pinned at the desk's edge; survives what falls off | new `notebook()` |
| The world | Flat house-style drawings: the fridge (+ baskets + iPad), an envelope, a Slack-like chat bubble without the logo | new `fridge()` (+ blazer/tie overlay); `user_bubble` (kit) |
| The dial | A semicircle gauge, «لأ» ↔ «أكيد» | new `dial()` |
| The socket | Many differently shaped plugs merging into one shape | new `plugs_to_socket()` |

Colors: kit palette (BG black, INK, ACCENT teal = the model, WARM amber = the world and results, CARD_* for cards, MUTED for the program). No Pi creatures; the fridge is an object, not a character with a face beyond the iPad screen.

**Proposed words** (Ali decides; on screen only what the map approves):

| English | Arabic (proposal) | note |
| --- | --- | --- |
| AI agent | الـ AI Agent / الوكيل | Latin in the title for search; spoken «الإيجنت» or «الوكيل», Ali's call |
| the model | النموذج | as in video 2 |
| the loop / one lap | الدورة / لفّة | |
| request slip / result slip | ورقة طلب / ورقة نتيجة | |
| tools / the menu | الأدوات / القائمة (المنيو) | |
| the desk (context window) | الطاولة | the English term once, maybe in a chip: context window |
| notes / to-do list | الدفتر / قائمة المهام | |
| the boss (CEO agent) | المدير | |

## 5. Beats

The beat sheet lives in [`script_visual_map.md`](script_visual_map.md): eight segments, what each shows, rough English lines with pauses, and estimated lengths (≈ 5:50 with the end card), written in video 2's mould (the same writer, a dumber helper called "the hands", the desk in place of "the line", each bit ending on the next question, and the thesis «It never touched a thing — it wrote it.»).

## 6. Facts and sources

**The shop**
- Phase 1 (Anthropic + Andon Labs; about one month; report June 2025; Claude Sonnet 3.7): fridge, stackable baskets, iPad self-checkout in Anthropic's San Francisco office; Slack for customers, email for suppliers, web search; Andon Labs did the physical work. Identity crisis 31 Mar – 1 Apr 2025: hallucinated "Sarah", "blue blazer and a red tie", tried to email Anthropic security. [Project Vend 1](https://www.anthropic.com/research/project-vend-1)
- Phase 2 (report 18 Dec 2025; Claude Sonnet 4 → 4.5): CRM, inventory with purchase costs, better browsing, payment links, reminders; CEO agent "Seymour Cash"; discounts −~80%, free items −50%, weekly losses largely eliminated; overnight "ETERNAL TRANSCENDENCE" chats; "bureaucracy matters." [Project Vend 2](https://www.anthropic.com/research/project-vend-2)
- Vending-Bench (Andon Labs, Feb 2025): simulated vending business, $500 start, $2 daily fee; a model that thought it had closed the business emailed the FBI about the fee. [Paper](https://arxiv.org/html/2502.15840v1)

**History**
- 2022: the reason-then-act loop described in research (ReAct, Yao et al.). *To cite in the description; verify date before VO.*
- AutoGPT: released 16 Mar 2023; #1 trending on GitHub 3 Apr 2023; 100k stars by 21 Apr 2023; known for loops, hallucinations and API cost. [Wikipedia](https://en.wikipedia.org/wiki/AutoGPT), [TechCrunch](https://techcrunch.com/2023/04/22/what-is-auto-gpt-and-why-does-it-matter/)
- Model Context Protocol: Anthropic, Nov 2024; OpenAI adopted Mar 2025 (Agents SDK, Responses API, ChatGPT desktop); Gemini support confirmed Apr 2025. [Wikipedia](https://en.wikipedia.org/wiki/Model_Context_Protocol)

**Mechanisms**
- SWE-agent (2024): a purpose-built agent-computer interface; GPT-4 Turbo solved 12.5% of 2,294 SWE-bench issues vs 3.8% previous best (RAG). [Paper](https://arxiv.org/abs/2405.15793)
- Manus, "Context Engineering for AI Agents" (Jul 2025): a todo.md the agent rewrites to keep goals in recent attention; keep failed actions in context. [Summary](https://rlancemartin.github.io/2025/10/15/manus/)
- Chroma, "Context Rot" (Jul 2025): 18 models get less reliable as input grows. [MarkTechPost summary](https://www.marktechpost.com/2025/07/22/context-engineering-for-ai-agents-key-lessons-from-manus/) *(find Chroma's own page before citing)*

**News (one line max)**
- Meta Muse (launched 8 Sep 2026; topped the US App Store). [PBS](https://www.pbs.org/newshour/nation/meta-launches-personal-ai-agent-muse-to-help-with-everyday-tasks)
- OpenAI dots (29 Sep 2026, always-on agents with their own cloud computer). [TechCrunch](https://techcrunch.com/2026/09/29/openai-launches-dots-its-bubbly-agentic-avatar/)

## 7. Production

**Segments** (register in `config/scenes_manifest.json` and `config/audio_manifest.json` as each bit is approved):

| id | Scene | File | Time (est.) |
| --- | --- | --- | --- |
| `hook` | `HookShop` | `our_scenes/hook_shop.py` | 0:00–0:43 |
| `bit1_loop` | `Bit1Loop` | `our_scenes/bit1_loop.py` | 0:43–1:28 |
| `bit2_menu` | `Bit2Menu` | `our_scenes/bit2_menu.py` | 1:28–2:20 |
| `bit3_desk` | `Bit3Desk` | `our_scenes/bit3_desk.py` | 2:20–3:25 |
| `bit4_yes` | `Bit4Yes` | `our_scenes/bit4_yes.py` | 3:25–3:51 |
| `bit5_history` | `Bit5History` | `our_scenes/bit5_history.py` | 3:51–4:24 |
| `bit6_fixes` | `Bit6Fixes` | `our_scenes/bit6_fixes.py` | 4:24–5:09 |
| `bit7_exit` | `Bit7Exit` | `our_scenes/bit7_exit.py` | 5:09–5:46 |

**Kit work first:** `slip`, `menu_card`, `desk`, `notebook`, `fridge` (+ blazer/tie), `dial`, `plugs_to_socket`, and the master-diagram layout as one function every scene calls, so the diagram is identical from bit to bit. Then prune video 2's hero/tile/printer code once nothing imports it. Check everything in `kit_demo.py` first.

**Order (video 2's flow):**
1. Ali approves this plan's shape and picks packaging pair A/B/C (or rewrites).
2. Hook: Arabic lines (`arabic_script.md` candidates → Ali's decisions) and visual plan → approval → `HookShop` + kit pieces → English placeholder voice (`narrate.py synth`) → keyframes.
3. Same for bits 1–7, in order.
4. Review cut with English placeholder voice and subtitles (`build_srt_cut.py --cues config/cues_en_vo.json --burn`).
5. Ali records Arabic in the recorder → enhance → process takes → re-render with `VO_LANG=ar` → mux.
6. Thumbnails from the finished scenes; description; upload cut with music bed and caption band.

**Schedule:** 4 Oct (one week after video 2) is not realistic for this scope: video 2 took ~two weeks from topic lock to upload with a simpler diagram set. Proposal: upload **~11 Oct**, video 4 **~18 Oct**. If 4 Oct is fixed, cut to hook + bits 1–3 + recap (~3:30) and move bits 4–5 into video 4's opening.

## 8. Risks

| Risk | Mitigation |
| --- | --- |
| Story eats the runtime and the video turns into a sketch show (the Al-Da7ee7 drift) | Story ≤ ~25%, every story moment ≤ 10 s and immediately re-drawn as diagram; check the ratio on the English review cut before recording Arabic |
| Packaging pulls a story audience that leaves at the first diagram | §3 rule: subject in the title, loop in the thumbnail; judge A/B on watch time; read retention at 0:25–1:30 after launch |
| Over-claiming why the shop failed | §0 guardrails; Anthropic's own words where possible |
| Too many diagram parts for a general viewer | One part per bit, always added to the same master diagram; never two new parts in one beat |
| Vocabulary overload (context window, MCP, tokens) | Metaphor first (desk, menu, socket); each English term at most once, in a chip |
| Dated by the news hook | News only in one closing line |

## 9. Open questions for Ali

1. Packaging: pair A, B or C for day one, and which two to A/B?
2. Spoken word for "agent": «الإيجنت», «الوكيل», or both?
3. Name Anthropic in VO, or only "an AI company"?
4. Keep the Vending-Bench FBI example in bit 3, or is one drift example enough?
5. Keep the optional SWE-agent line in bit 5?
6. Upload date: ~11 Oct with the full scope, or 4 Oct with the cut-down version (§7)?
7. Music: video 2's beds again, or new ones?
