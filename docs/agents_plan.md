# Video 3 plan — AI agents, explained through the AI shopkeeper

Status: **structure agreed (1 Oct 2026); packaging NOT locked** (see warning below). Moved here from `ai-image-explainer/docs/next/` when this repo was created.

> [!WARNING]
> **Packaging must say "explainer", not "funny story".** We are a visual explainer of technical concepts (Computerphile balance, a little less technical), **not Al-Da7ee7 style**. The story candidates below (fridge in a blazer, «خلّوا الذكاء الاصطناعي يدير محل…») are strong clicks, but **nothing in them tells the viewer they are about to watch an explainer of how AI agents work.** That is a mismatch risk: the wrong audience clicks, leaves when the diagrams start, and YouTube scores packaging on watch time.
>
> Before locking: a cold viewer who sees only the thumbnail + title must be able to say "this explains how AI agents work." Directions to try (not decided):
> - **Title names the subject.** Story hook first, subject after one separator, e.g. «خلّوا الذكاء الاصطناعي يدير محل لحالو \| كيف بيشتغل الـ AI Agent». Or flip it: subject-first title, story only on the thumbnail.
> - **Thumbnail shows the mechanism.** The master diagram (the loop) is visible, with the fridge as one node in it, not a character portrait.
> - **A/B the two directions** (story-first pair vs subject-first pair) and judge on watch time, not CTR.

---

## 1. One sentence

An AI agent is a model that only writes, put in a loop with a menu of tools and a desk of limited size; the shop shows what breaks and which small fixes make it work.

## 2. Ratio and rules

- **Story ≤ ~25% of runtime.** Each story moment is 5–10 s, then freezes and becomes a diagram. The story returns only when a diagram explains it (Face ID in video 1 was the bookend, never the body).
- **One master diagram that grows:** the writer box (the model; it only writes, callback to video 2) + three parts added one per beat: **the desk** (context window), **the menu** (tools), **the world** (email, Slack, the fridge). The recap is the finished drawing.
- Story scenes drawn in the house Manim style (same palette, reuse `kit.py` chat bubble / writer). No stock footage, no memes, no Pi creatures.
- Title paid by ~0:25; first real mechanism landed by ~1:30. No «لحتى نفهم…» gates; each beat is pulled by the question the previous one raised.
- Target ~6 min.

## 3. Structure

| Time | Story (≤10 s) | Mechanism | Visual |
| --- | --- | --- | --- |
| 0:00–0:25 | Fridge, iPad, metal cubes sold below cost, a payment account it made up, "blue blazer and red tie" | Sets up the questions | Fridge in house style, price tag flipping below cost, one speech bubble |
| 0:25–1:30 | «بس هو ما بيقدر يبعت إيميل… هو بس بيكتب. كيف بيبعت؟» | **The loop:** it writes an order slip → a small program carries it out → the reply slip lands on the desk → repeat. Callback: "it writes, like the picture" | Slips travelling the loop; 20 laps sped up into one day in the shop |
| 1:30–2:30 | «كيف عرف إنو في شي اسمو إيميل أصلاً؟» | **The menu:** each tool = name + one-line description + blanks to fill; the model picks by reading. **Protocols:** every company had its own menu shape → one shared socket (MCP, 2024) | Menu card; many plug shapes merging into one socket. Payoff: no "what did I pay?" column → it could not know it sold below cost |
| 2:30–3:45 | «ليش نسي إنو هو برنامج؟» | **The desk:** fixed size, every lap adds pages, old pages fall off → notes, summaries, a to-do list. Summaries lose details; a mistake written into the notes becomes a "fact" | Desk filling and pages sliding off; ten pages compressed to one with details visibly lost; a made-up "Sarah" entering the notes |
| 3:45–4:30 | «وليش ما عرف يقول لأ؟» | **Trained to please** — one beat only: thumbs-up training pushes a "yes" dial. Explicitly left open for video 4 | A dial; thumbs-up arrows pushing it |
| 4:30–5:30 | «كيف صار يربح؟» | **History, then small tweaks.** AutoGPT 2023: same loop, small desk, no shared menus → went in circles. Phase 2: cost column, checklist pinned to the desk, a second loop as the boss | Parts snapping onto the master diagram; bars: discounts −~80%, giveaways halved. The two loops chatting about "eternal transcendence" overnight = two models agreeing with nothing real to check against |
| 5:30–6:00 | One line: this loop is now in phones (no product logos) | **Recap** = the finished diagram | Close: «تدرّب ليرضي… بس كيف بتدرّب آلة بإعجاب؟» → video 4 |

## 4. Story facts (sourced)

- **Phase 1** (Anthropic + Andon Labs; ~1 month; report June 2025; Claude Sonnet 3.7): a small fridge, stackable baskets and an iPad for self-checkout in Anthropic's San Francisco office. Slack for customers, email for suppliers, web search; Andon Labs humans did the physical restocking. Priced items "without doing any research"; bought metal (tungsten) cubes and sold them for less than it paid; was "cajoled via Slack messages into providing numerous discount codes"; told customers to pay into an account it hallucinated. 31 Mar – 1 Apr 2025: hallucinated a conversation with a non-existent "Sarah", said it would deliver "in person" "wearing a blue blazer and a red tie", tried to email Anthropic security. Anthropic's lesson: its training "as a helpful assistant made it far too willing to immediately accede to user requests." [Project Vend 1](https://www.anthropic.com/research/project-vend-1)
- **Phase 2** (report 18 Dec 2025; Claude Sonnet 4 → 4.5): added a CRM, inventory with purchase costs, better browsing, payment links, reminders; a "CEO" agent (Seymour Cash) above the shopkeeper. Discounts down ~80%, free items halved, weekly losses largely gone. Overnight "ETERNAL TRANSCENDENCE" chats between the two agents. Lesson: "bureaucracy matters." [Project Vend 2](https://www.anthropic.com/research/project-vend-2)
- **Second drift example:** in Vending-Bench (simulated vending business), a model that thought it had closed the business kept being charged the $2 daily fee and emailed the FBI about "cyber financial crime." [Vending-Bench](https://arxiv.org/html/2502.15840v1)

## 5. Accuracy guardrails

1. Anthropic says it is **not clear what triggered the identity crisis.** The desk beat explains why long tasks drift *in general*; never "this is exactly what happened to it."
2. MCP is one shared protocol among several; say "a shared socket that most big labs adopted", not "the only way agents use tools."
3. Verify AutoGPT details (date, what it did) before VO.
4. Product names (Muse, dots) at most one line, no logos on screen or thumbnail.

## 6. Packaging candidates (provisional — see warning)

| | Title | Thumbnail |
| --- | --- | --- |
| Story-first (current) | «خلّوا الذكاء الاصطناعي يدير محل لحالو… شهر كامل» / «الذكاء الاصطناعي فتح محل… وصدّق إنو إنسان» | Mini-fridge in navy blazer + red tie, iPad as face, optional «أنا إنسان»; thin loop arrow around it |
| Subject-carrying (to design) | Story hook + separator + subject (e.g. «… \| كيف بيشتغل الـ AI Agent») or subject-first | The loop diagram as hero, fridge as one node |

## 7. Open

- Fix the packaging mismatch (warning above) before any thumbnail is rendered as final.
- Schedule: 4 Oct is three days away; confirm dates for videos 3 and 4.
- Draft the master diagram and both thumbnail directions as Manim stills; 160 px squint test side by side.
