# Step 7 — Build Time: Polish & Open Your PR (3:00 – 3:30)

## Goal

Take your feature from "works on my machine" to **a pull request the host can merge**. This is the half hour where your work goes from a private experiment to something everyone in the room plays with on the shared server.

## Priorities (in order)

1. **End-to-end working > perfect code.** If the server logic works but the UI is plain, that's totally fine.
2. **One happy path > all edge cases.** Cancel-timer works on a normal reveal? Ship it. Don't yet worry about "what if they cancel a ghost click."
3. **Demo-able > theoretically correct.** If you can't show it working in two browser tabs, it's not ready to PR.
4. **Then polish.** Once happy path works and the PR is open, layer in edge cases and UI niceties.

## Edge Cases to Think About

Once your happy path works, these are the kinds of questions to ask your AI agent (or a neighbor) about. The right answer is usually "your call as the designer" — pick something defensible and ship it.

| Feature | Edge Case | Reasonable Default |
|---------|-----------|--------------------|
| Cancel Timer | Player tries to cancel their **own** pending action | Allow it — you can cancel yourself or your opponent |
| Cancel Timer | Timer expires in the same instant as the cancel arrives | Whichever message the server processes first wins |
| Block Tile | Player blocks a tile that already has a pending reveal | Block fails, OR cancel + block — your call |
| Block Tile | Player tries to reveal their own blocked tile | Blocks only affect the opponent |
| Nuke 'Em | Player nukes an area with no mines | Nuke is consumed, nothing happens — or reveal-all-safe-tiles for points? |
| Ghost Click | Two ghost clicks at once from the same player | Allow / rate-limit / queue — your design choice |
| Decoy Tile | Opponent reveals the decoy normally | Decoy disappears, the real cell behind it is what gets revealed |

You don't have to handle every row. Pick the ones that matter for your feature, decide what they should do, and tell your AI agent: "if X happens, do Y."

## Opening Your Pull Request

When your happy path works in two browser tabs, **open the PR**. Don't wait for it to be perfect — small PRs that work get merged faster than big PRs that try to do everything.

What a good PR looks like for this workshop:

- **Branch named after your feature** (`feature/cancel-timer`, `feature/block-tile`)
- **One feature per PR** — don't bundle unrelated changes
- **Short description** — what the feature does, how to test it (which tile to click, what to expect)
- **Small diff** — server handler + minimal frontend hook is plenty. If the diff is huge, ask your AI to split it
- **Doesn't break existing features** — open two tabs, play a normal round, make sure regular reveals still work

Once you open the PR, **ping the host**. I'll review it on screen so the whole room sees the merge happen and gets to play with your feature on the shared server within minutes.

## Reading Your AI's Diff

Before you commit anything, read the diff. Things to push back on:

- **Files you didn't expect to be touched** — "why did you change `board.py`? Revert that, my feature is in `game.py` only"
- **Refactors you didn't ask for** — "stop renaming things, only add the new branch"
- **New dependencies** — "remove the `redis` import, we're in-memory only"
- **Speculative error handling** — "remove the try/except, let it crash if input is bad"

This is the contractor metaphor in action: you're the architect, the AI is doing the typing. **Read what got typed.**

## If You're Stuck at 3:00

In order:

1. **Reduce scope.** Forget the UI — just get the server to accept the action and `print()` it. That alone is PR-able as "feature scaffolding."
2. **Pair with a neighbor** for 5 minutes — explain your plan out loud, they'll usually spot the gap
3. **Switch to Lovable.** Fork the working app, add one button that sends a message. Less ambitious but demo-able.
4. **Flag the host.** Don't grind alone past 3:15 — wave me over.

## 5-Minute Warning (3:25)

When you hear the 5-min call:

- **Stop adding features.** Whatever you have, get it into a PR.
- **Broken-but-explainable** is a fine demo. "Here's what I built, here's the bug I didn't fix."
- **Push your branch** even if the PR isn't perfect. We can talk through it during demos.

## Where You Should Be by 3:30

- Most people: working feature with a happy path, PR open, host has reviewed it
- Some: also handled an edge case or two, polished UI
- A few: partially working, can explain what you built and what got in the way
- **Everyone:** ready to do a 2-minute demo or walkthrough

The goal of the demo isn't a perfect feature — it's showing what you learned about commanding the AI to do what you wanted.
