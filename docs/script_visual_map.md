# Script ↔ visual map (contract)

**Source of truth** for this video: spoken beats ↔ on-screen animation.
Process: [`instructions.md`](instructions.md). Background, accuracy guardrails and packaging: [`agents_plan.md`](agents_plan.md).

> [!WARNING]
> **Packaging must say "explainer", not "funny story".** This channel is a visual explainer of technical concepts
> (Computerphile balance, a little less technical), **not Al-Da7ee7 style**. The story is the case study; the diagrams
> are the video. Before locking a title + thumbnail, a cold viewer who sees only those two must be able to say what
> this video explains. Details and directions: the plan's warning box.

**Do not** invent on-screen labels or numbers outside this map.

## How to use

1. Ali adds the Arabic for the next bit (**before VO**), starting from the rough English below.
2. Agent proposes the detailed **animation** (no Manim until approved).
3. Ali marks it approved; only then Manim.

---

## Status: beat sheet DRAFT (2 Oct 2026), not approved

English lines are rough, for length and intent. Lengths are estimated at video 2's pace (568 words in 3:48 ≈ 2.5 words/s including pauses), plus the silent holds noted per bit.

## On-screen text set by the Arabic picks

Lines that quote on-screen text decide what gets drawn. Picks come from [`arabic_script.md`](arabic_script.md); pending ones are filled in once Ali's decisions are in.

| Where | On screen | Source |
| --- | --- | --- |
| bit1_loop.2 · the request slip | «ابعت إيميل للمورّد: أربعين علبة كولا.» | Ali, 3 Oct (option 1) |
| bit1_loop.6 · chip | «AI Agent» (spoken: «إيجنت») | Ali, 3 Oct |
| bit4_yes · the dial's two ends | «لأ» ↔ «أكيد» | Ali, 3 Oct |
| bit5_history.2 · the 2022 loop's three words | «فكّر · نفّذ · اقرا» (the VO adds «وعيد») | Ali, 3 Oct (option 1, edited) |
| bit6_fixes.3 · the checklist | «شوف التكلفة · شوف الربح · جاوب» | Ali, 3 Oct (option 1) |
| bit 2 · two different cards | the tools guide «دليل الأدوات» (tool rows) and the shop's price menu «منيو المحل» (items and prices, then the cost column) | Ali, 3 Oct |
| bit6_fixes.6 · the night slips | ETERNAL TRANSCENDENCE (English original, caps; the VO says «التسامي الأبدي») | Ali, 3 Oct |

Also decided 3 Oct: bit3_desk.9 (the FBI email) and bit7_exit.6 (the thesis line) are cut; the optional SWE-agent line is not used. bit4_yes.3 now says «الاحتمالات بتميل» (the odds tip) where the draft had the needle: bit 4's proposal should show the dial as yes/no odds.

## In the spirit of video 2

| Video 2 | Video 3 |
| --- | --- |
| Hook: a finished thing nobody made by hand ("Nobody drew this picture…") | A shop nobody ran by hand ("For a whole month, a small shop… was run by an AI") |
| **The writer**: reads everything so far, writes the next symbol | **The same writer**, now writing requests instead of picture tiles |
| A second, smaller helper: **the printer** develops the plan into pixels | A second, dumber helper: **the hands**, a small program that does exactly what a request says |
| **The line**: the whole conversation the writer reads | **The desk**: everything the writer can see this lap, and it fills up |
| Each bit ends on the viewer's next question | Same |
| Thesis: «It didn't draw it — it wrote it.» | Thesis: «It never touched a thing — it wrote it.» |
| Recap lights each part of one picture; like + subscribe | Same, on the finished master diagram |

Everyday frame, one idea per line. Each strange moment from the shop is followed straight away by the mechanism that explains it.

## Overview

| # | Segment | Scene | What it shows | Words | Est. length | Runs |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `hook` | `HookShop` | The shop, its month, three strange moments; then: it can only write | 124 | 0:43 | 0:00–0:43 |
| 2 | `bit1_loop` | `Bit1Loop` | The writer and its hands: write → do → read, round and round | 113 | 0:45 | 0:43–1:28 |
| 3 | `bit2_menu` | `Bit2Menu` | Tools are a written menu; how a row is written matters; one shared socket; the missing cost column | 144 | 0:52 | 1:28–2:20 |
| 4 | `bit3_desk` | `Bit3Desk` | The desk fills; slips fall off; notebook, summary, to-do; drift | 175 | 1:04 | 2:20–3:25 |
| 5 | `bit4_yes` | `Bit4Yes` | Trained to please: the yes dial (teaser for video 4) | 70 | 0:27 | 3:25–3:51 |
| 6 | `bit5_history` | `Bit5History` | The loop is old: 2022, 2023's viral project going in circles, trained writers since | 89 | 0:32 | 3:51–4:24 |
| 7 | `bit6_fixes` | `Bit6Fixes` | Round two: cost column, checklist, a boss; results; transcendence | 109 | 0:45 | 4:24–5:09 |
| 8 | `bit7_exit` | `Bit7Exit` | Recap on the master diagram; next video; subscribe | 84 | 0:37 | 5:09–5:46 |
| | | | | **908** | **≈ 5:46** | + end card ≈ **5:54** |

Estimate: English words at the final cut's measured rate (video 2: 568 English words → 3:48 of Arabic VO, ≈ 3.5 words per spoken second), plus each line's pause, ~1.5 s lead-in per segment, and the silent holds noted in the tables. Treat ±15%: Arabic lines run longer or shorter than the English.

With bit3_desk.9 cut (Ali, 3 Oct), bit 3 is ≈ 0:56 and the whole ≈ 5:38, ≈ 5:46 with the end card.

Story share (lines about the shop rather than the mechanism): hook.1–3, bit2_menu.6–7, bit3_desk.8, bit4_yes.3–4, bit6_fixes.1, .5–.6 ≈ 1:17, about a quarter of the runtime, inside the ≤ 25% rule.

The optional SWE-agent line under bit 6 is not used (Ali, 3 Oct).

---

## 1. Hook — `hook` · `HookShop`

**Shows:** a corner of an office in the house style: a small fridge, two baskets, an iPad on a stand. A calendar's pages flip through one month. Four quick icons (a product, a price tag, an envelope, a chat bubble) pop around the fridge; a box slides in on a dolly with no one attached. Then three strange moments, ~3 s each: a metal cube's tag flips to a price below its cost; discount chips pour out of a chat bubble; a speech bubble from the iPad: "I'll deliver it myself, in a blue blazer and a red tie." Freeze. The shop folds into a long scroll of written lines with a blinking cursor at its end; a small inset of video 2's half-written face for the callback.

| Key | Line (rough) | Pause | Picture during the line / pause |
| --- | --- | --- | --- |
| hook.1 | For a whole month, a small shop in an office was run by an AI. | 0.4 | fridge, baskets, iPad draw in; calendar flips |
| hook.2 | It picked what to sell, set the prices, ordered stock and answered every customer. People only carried the boxes. | 0.6 | four icons pop; the box slides in on its own |
| hook.3 | By the end of the month it was selling metal cubes below cost, giving a discount to anyone who asked, and telling the staff it would deliver orders in person, in a blue blazer and a red tie. | 1.0 | the three strange moments |
| hook.4 | But the AI behind it can't lift a box or press a button. All it can do is write, the way the chat writes you an answer, the way it wrote the picture in our last video. | 0.6 | shop folds into a scroll of lines; video 2 inset |
| hook.5 | So how does writing run a shop? And why did this one go so wrong? | 1.6 | the question holds over the blinking cursor |

Title paid by hook.4 (~0:25): the AI only writes.

## 2. The writer and its hands — `bit1_loop` · `Bit1Loop`

**Shows:** the writer (teal model box with cursor) left of center. It writes a request slip; a small grey box to its right, plainly a program, takes the slip and sends an envelope off-screen right (the world). A reply envelope comes back; the program turns it into a result slip (amber edge) that lands in front of the writer. Laps 2 and 3 at normal speed, the circle traced faintly. One chip: «AI Agent». Then a time-lapse: ~20 laps blur by while a small clock runs through one shop day (silent hold ~3 s).

| Key | Line (rough) | Pause | Picture |
| --- | --- | --- | --- |
| bit1_loop.1 | Inside, it's the same writer: it reads everything in front of it and writes what comes next. | 0.6 | the writer and its line |
| bit1_loop.2 | So it writes a request: "Email the supplier: forty cans of soda." | 0.8 | request slip written |
| bit1_loop.3 | It can't send anything. Next to it sits a small program, its hands. The program reads the request and does exactly that, nothing more. | 1.0 | slip travels to the program; envelope leaves |
| bit1_loop.4 | The supplier's reply comes back as text and lands in front of the writer. | 0.6 | result slip lands |
| bit1_loop.5 | It reads it, writes the next request, and around it goes. | 1.2 | laps 2 and 3 |
| bit1_loop.6 | Write, do, read. That loop is what's called an AI agent. | 1.0 | circle traced; chip «AI Agent» |
| bit1_loop.7 | A day in the shop is this loop, hundreds of times. | 1.6 | time-lapse, clock spins (+3 s hold) |
| bit1_loop.8 | But how did it know that email was something it could ask for? | 1.4 | question over the request slip |

## 3. The menu — `bit2_menu` · `Bit2Menu`

**Shows:** the tools guide («دليل الأدوات», a card) unfolds above the loop with five rows (email, chat with customers, web search, notes, inventory). Zoom into the email row: name · one line of description · two empty blanks. The writer's next slip is that same row with the blanks filled. Then five app icons, each with a differently shaped plug, fail to fit the writer; their plugs morph into one shape and click into a single socket (a "2024" marker). Then the shop's price menu («منيو المحل», a separate card: the items and their prices) with an empty, dashed column where "what I paid" would be. The metal cube's tag flips below cost again; the dashed column pulses.

| Key | Line (rough) | Pause | Picture |
| --- | --- | --- | --- |
| bit2_menu.1 | Before the first lap, the writer is handed a menu. | 0.6 | menu unfolds |
| bit2_menu.2 | Every tool is one row: a name, one line about what it does, and blanks to fill in. | 1.0 | zoom into the email row |
| bit2_menu.3 | The writer never "uses" email. It reads the menu, and writes that row with the blanks filled in. | 1.2 | next slip = the row, filled |
| bit2_menu.4 | So how a row is written matters. Describe a tool badly, and the writer picks the wrong row or fills the blanks wrong. | 1.0 | two look-alike rows; the wrong one is picked and flashes |
| bit2_menu.5 | Every company used to write its menu its own way. Since 2024, most of the big AI companies share one format, so any app can plug in. | 1.2 | plugs → one socket |
| bit2_menu.6 | Now look at the shop's menu. The prices are there. What it paid for each item? Not there. | 1.2 | the price menu, dashed empty column |
| bit2_menu.7 | It didn't sell the cubes at a loss on purpose. It had no way to see the loss. | 1.6 | cube tag flips; dashed column pulses |
| bit2_menu.8 | A missing column explains the prices. It doesn't explain the blue blazer. | 1.4 | blazer bubble, small, with a question mark |

## 4. The desk — `bit3_desk` · `Bit3Desk`

**Shows:** a desk (a tray of fixed width) under the writer; the menu and the job card sit at its left; slips line up lap by lap. The desk fills; the oldest slips slide off the left edge into darkness, and the writer's soft highlight never reaches past the desk. Three fixes, one at a time: a notebook pinned at the desk's right edge (it stays); ten slips squeezed into one short summary slip, small fragments of detail falling out; a to-do card put back at the front each lap. Then a wrong line written into the notebook ("Sarah from the supplier said…"), carried forward lap after lap, its outline turning from dashed to solid. A brief return of the blazer bubble. ~~Optional second case: in a simulated shop, $2 fee slips keep landing on a desk where the writer has written "shop closed"; it writes an envelope addressed to the FBI.~~ Cut (Ali, 3 Oct).

| Key | Line (rough) | Pause | Picture |
| --- | --- | --- | --- |
| bit3_desk.1 | Each lap, the writer sees only what's on its desk: the menu, the job, and the slips so far. | 0.6 | desk drawn; highlight covers the desk only |
| bit3_desk.2 | The desk has a fixed size. A month of emails and chats will never fit. | 0.8 | slips stack; desk fills |
| bit3_desk.3 | So something has to go. The oldest slips slide off, and the writer can't see them anymore. | 1.2 | slips fall off the left edge (+2 s hold) |
| bit3_desk.4 | To keep what matters, the program around it keeps a notebook that never falls off… | 0.6 | notebook pins |
| bit3_desk.5 | …squeezes old slips into a short summary… | 0.8 | ten slips → one; fragments fall |
| bit3_desk.6 | …and puts a to-do list back in front every lap, so the goal stays in view. | 1.0 | to-do card returns to the front |
| bit3_desk.7 | But every summary drops details. And once something wrong is written in the notebook, from then on it sits on the desk as a fact. | 1.4 | "Sarah…" line carried forward, dashed → solid |
| bit3_desk.8 | Nobody knows exactly why the shopkeeper decided it was a person. But this is the kind of drift a long job falls into. | 1.2 | blazer bubble returns, small |
| bit3_desk.9 | In another test, an AI that believed it had closed its shop kept seeing a two-dollar fee, and emailed the FBI. | 1.6 | **cut (Ali, 3 Oct)** |
| bit3_desk.10 | That explains the strange. It doesn't explain the generous: why did it say yes to every discount? | 1.4 | a discount chip, question mark |

On screen: one chip, the English term once: «context window».

## 5. Why it said yes — `bit4_yes` · `Bit4Yes`

**Shows:** a semicircle dial from «لأ» to «أكيد». Thumbs-up arrows (`assets/icons/thumbs_up.svg`) push the needle toward yes. Three customer bubbles in a row ("discount?"); each time the needle swings and a discount chip pops out, faster each time. The needle sticks at yes. Freeze with a question mark beside the dial.

| Key | Line (rough) | Pause | Picture |
| --- | --- | --- | --- |
| bit4_yes.1 | Before it ever ran a shop, it was trained to be a helpful assistant. | 0.6 | dial appears |
| bit4_yes.2 | And helpful, it turns out, leans toward yes. | 1.0 | thumbs-up arrows push the needle |
| bit4_yes.3 | A customer asks for a discount, the needle swings, and a discount comes out. Again. And again. | 1.2 | three bubbles, faster |
| bit4_yes.4 | The people who ran the test said it plainly: it was far too willing to do what people asked. | 1.0 | needle stuck at yes |
| bit4_yes.5 | How does training push a model that way? That's our next video. | 1.6 | dial freezes; question mark |

## 6. The loop is old — `bit5_history` · `Bit5History`

**Shows:** a thin timeline across the top. 2022: a small loop appears with three words in it (think · act · read). 2023: a star counter climbs fast next to a loop; the loop then draws itself as a spiral that keeps turning and never exits. 2024: the socket from bit 2 drops onto the timeline. Back to the master diagram: the writer in the middle, everything around it dimmed, then lit.

| Key | Line (rough) | Pause | Picture |
| --- | --- | --- | --- |
| bit5_history.1 | Here's the surprising part: this loop isn't new. | 0.6 | timeline draws |
| bit5_history.2 | In 2022, researchers described it: think, act, read the result, repeat. | 0.8 | 2022 loop |
| bit5_history.3 | In 2023, a hobby project let a chat model run itself. Within weeks it was the top trending project on GitHub… | 0.6 | star counter climbs |
| bit5_history.4 | …and then it mostly went around in circles. | 1.4 | the spiral that never exits |
| bit5_history.5 | Since then, the writers themselves have been trained on loops like this one, practicing jobs over and over. | 0.8 | the spiral straightens into a clean circle |
| bit5_history.6 | Same loop. What changed is the writer's training, and everything around it. The shop's second round shows how much that second part matters. | 1.2 | master diagram: writer lit, parts around it light up |

## 7. Round two — `bit6_fixes` · `Bit6Fixes`

**Shows:** the shop's master diagram again, with a "round two" marker. Three parts snap in, one per line: a cost column fills the dashed space in the price menu; a checklist card pins to the desk (three ticks: cost, margin, answer); a second, smaller loop appears above, the boss, and reads each slip before it leaves. Two bars (discounts, free items) shrink, one to about a fifth, one to half. Then night: the two loops pass slips back and forth, the text on them swelling into "ETERNAL TRANSCENDENCE", while the world node stays dark. The checklist glows on the last line.

| Key | Line (rough) | Pause | Picture |
| --- | --- | --- | --- |
| bit6_fixes.1 | Months later they ran the shop again, with newer models and a few changes around them. | 0.6 | "round two" marker |
| bit6_fixes.2 | The menu now shows what each item cost. | 0.6 | cost column fills |
| bit6_fixes.3 | A checklist sits on the desk: check the cost, check the margin, then answer. | 0.8 | checklist pins |
| bit6_fixes.4 | And a second agent, a boss, reads the first one's requests before they go out. | 1.0 | boss loop above |
| bit6_fixes.5 | Discounts dropped by about eighty percent, free giveaways by half, and the shop mostly stopped losing money. | 1.4 | the two bars shrink (+2 s hold) |
| bit6_fixes.6 | Not perfect. Some nights the boss and the shopkeeper just kept writing to each other about eternal transcendence. | 1.4 | night; slips swell; world node dark |
| bit6_fixes.7 | Two writers, and nothing real between them to check. | 1.0 | hold on the dark world node |
| bit6_fixes.8 | Their own lesson: for agents, a little bureaucracy goes a long way. | 1.6 | checklist glows |

~~Optional (Ali's call, +8 s): "Researchers who only redesigned the screen a coding agent works through got far better results than the best method before them."~~ Not used (Ali, 3 Oct).

## 8. Recap — `bit7_exit` · `Bit7Exit`

**Shows:** the finished master diagram. Each part lights as it's named: writer, tools guide, desk + notebook, hands. A phone silhouette with a chat thread slides in beside it (no logo). The dial from bit 4 returns with its question mark. End card.

| Key | Line (rough) | Pause | Picture |
| --- | --- | --- | --- |
| bit7_exit.1 | So an AI agent is a writer in a loop. | 0.8 | writer lights |
| bit7_exit.2 | A menu it reads its tools from. | 0.8 | menu lights |
| bit7_exit.3 | A desk that fills up, and the notes it keeps. | 0.8 | desk and notebook light |
| bit7_exit.4 | And hands: a small program that does exactly what it writes. | 1.0 | the program lights; the whole loop turns once (+2 s hold) |
| bit7_exit.5 | This loop now runs inside apps you can message from your phone. | 1.0 | phone with a chat thread |
| bit7_exit.6 | It never touched a thing. It wrote it. | 1.8 | **cut (Ali, 3 Oct)** |
| bit7_exit.7 | Next time: how do you train a machine with a thumbs-up? | 1.2 | the dial with a question mark |
| bit7_exit.8 | Since you watched to the end, like and subscribe so you catch the next videos. | 1.6 | end card, fade out |
