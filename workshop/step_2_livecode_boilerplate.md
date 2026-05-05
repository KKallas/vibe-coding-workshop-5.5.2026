# Step 2 — Live-Code: Minesweeper with Multiplayer (0:30 – 1:00)

## Goal

Live-code the entire working boilerplate in 30 minutes: board generation, game logic, multiplayer state, WebSocket server, and minimal frontend. **One shared board — both players click freely, no turns.**

## The Starting Prompt

This is the actual prompt I'll feed Claude Code on stage to kick the whole thing off:

> can you make a multiplayer version of the classic minesweeper. medium size board any user who comes to the page can open any slab, extra feature opening will start 5 second countdown so other user can cancel this (or yourself).
>
> keep it barebones: **no database, no user accounts, no login**. all game state lives in the python server's memory only — never written to disk, never persisted. every new game = fresh state, gone when the server restarts. python backend (FastAPI + websockets is fine), and the simplest possible frontend (plain HTML/JS, no framework, no build step).

Note what's in the prompt and what's not:
- **In:** the game, the multiplayer twist, the 5-second cancel mechanic, the "no persistence / no auth" guardrails, rough stack
- **Out:** file layout, scoring rules, win condition, exact data shapes
- **Why the guardrails?** — without them, LLMs default to "professional" choices: SQLite or Postgres for state, a user table with login, a React frontend with a build step. All wrong for a 30-minute live-code. We're explicit about what we *don't* want
- The model fills in the remaining gaps. We watch what it picks, and steer when it goes somewhere we don't want

## Live-Coding Walkthrough

### 1. Board & Cells (7 min)

- Random mine placement on a 16×16 grid with ~40 mines
- 8-direction neighbor counting for the adjacency numbers
- Each cell tracks `revealed_by` so we know which player gets the point

### 2. Game Logic & Players (8 min)

- A `Player` carries a score plus resource slots for the power-ups participants will add later (blocks, nuke, decoys)
- A `PendingAction` is any in-flight click — has an ID, owner, target cell, start time, 5s duration, and a `cancelled` flag
- The `Game` holds the board, the connected players, and a *list* of pending actions

Key points to explain:
- **No turns** — both players fire actions whenever they want
- Multiple pending actions can exist simultaneously
- Every reveal goes through a 5-second pending phase before it resolves
- Power-up slots are stubbed on the player object so participants have a place to plug in later

### 3. Action Handler (7 min)

- One handler dispatches on `action` type: `reveal`, `flag`, and a clearly-marked spot where participants will add `cancel`, `block`, `nuke`, `ghost`, `decoy`
- Reveal flow: a click creates a pending action (broadcast to both players) → 5-second timer → if not cancelled, resolve
- Resolve rules: mine = score penalty (game continues!), safe cell = +1 point and flood-fill any connected zero-cells
- Win condition: all non-mine cells revealed — highest score wins

### 4. WebSocket Server + Frontend (8 min)

- FastAPI websocket endpoint per `(game_id, player_id)` — server keeps games in memory
- `broadcast()` pushes state to **all** connected players on every change
- Minimal canvas frontend: click → send `reveal`, listen for state → render
- Pending actions shown as pulsing/highlighted cells; scores visible to both players

## Architecture in Words

Player A clicks (3,4) → server creates a pending action → both browsers see the pulsing cell and a 5s timer. Meanwhile Player B clicks (7,2) → second pending action, runs in parallel. Either player can fire `cancel` on either pending action during the window. When timers expire un-cancelled, the server resolves them and broadcasts the final state to both clients.

## Key Teaching Moments

- **Why 5 seconds?** — Creates the space for cancel, ghost click, and mind games
- **Why no turns?** — More exciting, more chaotic, more room for power-ups to matter
- **Why track `revealed_by`?** — Scoring. It's a race.
- **Show a prompting moment**: "If I were using Claude Code right now, I'd say: 'Add flood-fill BFS to the reveal resolver that reveals all connected zero-cells and awards each to the player'"

## Checkpoint

By 1:00, the server should be running and two browser tabs can:
- Connect to the same game (shared board)
- Both click tiles freely at the same time
- See 5-second pending animations
- See tiles reveal after timer
- See scores update
