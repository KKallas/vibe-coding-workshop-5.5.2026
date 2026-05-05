# Vibe-coding Workshop · 5 May 2026

A 4-hour, hands-on intro to **vibe-coding** — using AI agents (Claude Code, Codex, Imp, Lovable) to go from idea to running code. We learn the tools by building one project together: a chaotic, real-time **multiplayer Minesweeper** with Mario-Kart-style power-ups.

## What You'll Walk Away With

- A working multiplayer game you helped ship to a shared server
- Hands-on experience commanding an LLM coding agent on a real codebase
- The **PR → review → merge → redeploy** loop that lets a team of vibe-coders ship without breaking each other's work
- A taste of where the abstraction ladder is going next: from Python-with-AI today toward **idea → implementation** as the default interface

## How the Day Works

- We share **two live servers** (a Python build on the host's machine + a Lovable build) — nobody runs the game on their laptop
- You build features locally with your AI tool of choice, **open a pull request**, and once it's reviewed and merged the host redeploys so everyone can play with it immediately
- Default tooling is **Imp + Kimi** (the host hands out a Kimi API key on the day — no signup, no payment); Claude Code and Codex are also supported if you bring your own key, and Lovable is the zero-setup visual track

## Time Plan (4 hours)

| Time | Step | What happens |
|------|------|--------------|
| 0:00 – 0:30 | [1. The Big Picture](workshop/step_1_intro.md) | From transistors → assembly → Python → vibe-coding. Why we're here, what an LLM is good and bad at |
| 0:30 – 1:00 | [2. Live-Code the Boilerplate](workshop/step_2_livecode_boilerplate.md) | Host live-codes the multiplayer Minesweeper boilerplate from a single starting prompt |
| 1:00 – 1:30 | [3. Test & Debug Together](workshop/step_3_testing.md) | Everyone connects to the two shared servers, smoke-tests, and walks through the PR → merge → redeploy workflow |
| 1:30 – 2:00 | [4. Tool Setup](workshop/step_4_tool_setup.md) | Get your AI tool working. Imp + Kimi is the default — Claude Code, Codex, and Lovable are alternatives |
| 2:00 – 2:30 | [5. Feature Briefing & Teams](workshop/step_5_feature_briefing.md) | Five power-up features briefed — Cancel Timer, Block Tile, Nuke 'Em, Ghost Click, Decoy Tile. Pick one (solo or in a small team) |
| 2:30 – 3:00 | [6. Build Sprint 1](workshop/step_6_build_time_1.md) | First implementation pass with your AI agent. Host circulates and coaches prompting |
| 3:00 – 3:30 | [7. Build Sprint 2 — Polish](workshop/step_7_build_time_2.md) | Edge cases, polish, open the PR. Host reviews and merges live |
| 3:30 – 4:00 | [8. Demos & Wrap-Up](workshop/step_8_demos_wrapup.md) | Every team demos. We play one chaotic round with all features merged. Takeaways and where to go next |

## The Game

**Multiplayer Minesweeper, no turns.** One shared 16×16 board, both players click freely. Every reveal triggers a **5-second pending timer** during which either player can cancel — that mechanic is the hook every power-up plugs into. Score = +1 per safe reveal, –1 for hitting a mine, game continues either way.

## Repo Layout

- [workshop/](workshop/) — the eight step-by-step session plans (this is the curriculum)
- [Imp/](Imp/) — the bundled Imp agent that participants run as the default option
- The Minesweeper boilerplate itself is live-coded in step 2 — it doesn't live in the repo until then

## A Note on the Docs

All documentation in this repo — this README, the eight step files, comments, anything that explains "why" — is **the best understanding of whoever wrote it at the time they wrote it**. It is almost certainly wrong somewhere. Tools change, models change, my own opinions change, and a workshop plan written weeks before the day will collide with reality on the day.

**Read it critically.** If something doesn't match what you see in the code, or contradicts a newer source, or just feels off — trust your eyes over the doc. And if you spot a mistake, a stale instruction, or a better way to explain something, please open a PR or issue. Improvements from people running into the rough edges are exactly how this gets better.

## Tools and notes

Lovable [project](https://lovable.dev/projects/06500f2a-c2b4-4ff0-b1b3-5e101f531568?magic_link=mc_6363ceb5-92aa-4787-a611-c386719423bc)

[new lovable](https://blast-buddies-race.lovable.app)

## License

[MIT License](LICENSE)
