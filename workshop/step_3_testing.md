# Step 3 — Test & Debug Together (1:00 – 1:30)

## Goal

Smoke-test the boilerplate as a group on the **two shared servers** everyone will play and test on for the rest of the day. Establish the **PR → merge → redeploy** loop that drives every change for the rest of the workshop.

## The Setup: Two Shared Servers

Nobody runs the game server on their own laptop. Instead, everyone connects to one of two shared instances:

1. **The Python server** — running on my machine (the boilerplate we just live-coded). This is the canonical workshop build.
2. **The Lovable server** — the visual-builder version, hosted by Lovable. This is the lighter parallel track for participants who picked Lovable in step 1.

Both URLs go up on the screen and into the chat. Two browser tabs per person — one of each — and we can compare how the same game feels on both stacks.

## The Workflow: PR → Merge → Redeploy

This is the loop that shapes the rest of the day:

1. A participant builds a feature (locally with Claude Code / Codex / Imp, or in Lovable's editor)
2. They **open a pull request** against the workshop repo
3. I review the PR live on screen — we discuss scope, naming, edge cases
4. If it's good, I **merge** and **redeploy the Python server**
5. Everyone refreshes their browser and the new feature is live for everyone to play with

This is on purpose:
- Mirrors real open-source / team workflow
- Forces features to be **small and reviewable** — if the PR is too big, we'll send it back to be split
- Bugs surface immediately because everyone is hammering the same server at the same time
- The host (me) is the gatekeeper, the same way a tech lead or contractor manager would be

## Agenda

### 1. Group Test on Both Servers (10 min)

- Everyone opens both URLs side-by-side
- We walk through the flow together on the Python server first:
  - Player 1 clicks a tile → pending action appears for both
  - Player 2 clicks a different tile at the same time → second pending action appears
  - Both 5-second countdowns run in parallel
  - Tiles reveal independently as their timers complete
  - Try both players clicking the same tile → server rejects the duplicate
  - Try hitting a mine → penalty for that player, game continues
  - Race to reveal the most safe tiles
- Then everyone hops to the Lovable server and we do the same — note differences in feel, latency, what's missing

### 2. Live Bug Hunt & First PR Walkthrough (10 min)

The boilerplate will have bugs — 20+ people clicking simultaneously surfaces things a solo test doesn't. Common things to expect and fix on the spot:

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| WebSocket disconnects under load | Server task not awaiting cleanly | Wrap in try/finally, log errors |
| Board not rendering for some users | Initial state not sent on connect | Send full state on `connect` |
| Flood fill freezes | Missing visited set in BFS | Add `visited` set |
| Both players see mines | `to_dict()` not hiding mine locations | Filter unrevealed mines from state |
| Timer not working | Async timing issue | Use `asyncio.sleep` + task |

If a fix is non-trivial, **I open it as a PR live** so everyone sees the merge-redeploy loop end-to-end before they have to do it themselves.

### 3. Code Walkthrough — What's Extensible (10 min)

Show participants the hooks they'll be extending. The action handler is the main extension point — every feature is "add a new action type, wire it through pending/resolve, broadcast the result."

- Walk through the `PendingAction` model — most features hook into the pending/resolve cycle
- Show where the frontend render loop picks up new state
- Point out the `Player` model fields that are already stubbed (`blocks_remaining`, `has_nuke`, `decoys_remaining`) — features just need to use them
- Show the repo's PR template / branch naming convention so participants know what a "good" PR looks like before they open theirs

## Checkpoint

By 1:30, everyone should:
- Be connected to **both** shared servers (Python + Lovable) and have played a round on each
- Understand the codebase structure and which file/function to extend
- Have cloned/forked the repo and confirmed they can open a PR
- Know the loop: **build → PR → review → merge → redeploy → test together**
- Be ready to pick a feature
