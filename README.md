# ai-agents-explainer (Manim)

Video 3 of the channel: Arabic **visual explainer** of how AI agents work: a model that only writes, in a loop, with a menu of tools and a desk of limited size. Running case study: the AI shopkeeper (Anthropic's Project Vend, 2025).

Working title (not locked): «خلّوا الذكاء الاصطناعي يدير محل لحالو… شهر كامل»

> [!WARNING]
> **Packaging must say "explainer", not "funny story".** This channel is a visual explainer of technical concepts
> (Computerphile balance, a little less technical), **not Al-Da7ee7 style**. The story is the case study; the diagrams
> are the video. Before locking a title + thumbnail, a cold viewer who sees only those two must be able to say what
> this video explains. Details and directions: the plan's warning box.

## Read first

| File | Purpose |
| ---- | ------- |
| [`docs/agents_plan.md`](docs/agents_plan.md) | Structure, story facts, accuracy guardrails, packaging |
| [`docs/context.md`](docs/context.md) | Goals, siblings, what this is not |
| [`docs/instructions.md`](docs/instructions.md) | **Agent system prompt:** roles, approve-then-build, render/mux, voice pipeline |
| [`docs/script_visual_map.md`](docs/script_visual_map.md) | **Contract:** Arabic lines ↔ visuals |
| [`docs/arabic_script.md`](docs/arabic_script.md) | Arabic candidates + decisions → `config/narration_ar.json` |
| [`docs/ADDING_SEGMENTS.md`](docs/ADDING_SEGMENTS.md) | Checklist for the next bit |

## Repo layout

Same as video 2 ([`../ai-image-explainer`](../ai-image-explainer)):

| Path | Role |
| ---- | ---- |
| `manim/` | 3b1b ManimGL engine (**not committed**; clone or link, below) |
| `our_scenes/` | This video's scenes. `kit.py` is video 2's kit (palette, chat bubble, model box, `NarratedScene`); `kit_demo.py` is its test bench |
| `config/` | Manifests and narration, empty until the first bit |
| `scripts/` | Render / mux / assemble / keyframes, the voice pipeline (narrate, recorder, enhance, process takes) and the subtitle/upload cut |
| `assets/` | Amiri font (OFL), icons |
| `media/music/` | Video 2's music beds (Esther Abrami) |
| `media/` | Renders, VO, muxed output (gitignored except `.gitkeep`) |

## Setup

```bash
python3 -m venv .venv && . .venv/bin/activate
ln -s ../1-hour-challenge/manim manim   # the checkout videos 1 and 2 run (or: git clone --depth 1 https://github.com/3b1b/manim.git manim)
pip install -e ./manim
pip install -r manim/requirements.txt
# ffmpeg on PATH
```

## Status

All eight segments built and rendered (3 Oct 2026); upload cut and Arabic SRT in `media/output/` (`build_srt_cut.py`, see `docs/to_do.md`). Packaging decided and publish pack ready (5 Oct 2026): [`docs/youtube/publish_pack.md`](docs/youtube/publish_pack.md); publish planned for Fri 9 Oct, 15:00 Syria time.
