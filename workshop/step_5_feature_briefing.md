# Step 5 — Feature Briefing & Team Formation (2:00 – 2:30)

## Goal

Present the 5 power-up features, form teams (or solo), pick a feature, and get set up with the right AI tool.

## The 5 Features

Explain each feature, show a quick diagram or mockup, and clarify how it hooks into the existing code.

### Feature 1: Cancel Timer

> Revealing a tile takes 5 seconds. During that window, the other player can cancel the reveal. The pending action is visible to both players.

- Hooks into: `PendingAction` resolve cycle
- New action: `{"action": "cancel", "target_action_id": "..."}`
- Server logic: if pending action still active and requester is the *other* player → mark cancelled
- UI: show a "cancel" button on opponent's pending tiles

### Feature 2: Block Tile

> Place a 30-second block on any unrevealed tile, preventing the opponent from revealing it. 3 uses per player per game.

- Hooks into: `handle_action` + reveal validation
- New action: `{"action": "block", "row": r, "col": c}`
- Server logic: mark tile as blocked for 30s, reject opponent's reveals on it, decrement `blocks_remaining`
- UI: show a lock/shield icon on blocked tiles (visible to both)

### Feature 3: Nuke 'Em

> Detonate all bombs within a 9×9 area. One bomb on the board is hidden under a special slab — whichever player reveals that slab gets the nuke charge.

- Hooks into: board generation (place one "slab" tile) + new action type
- New action: `{"action": "nuke", "center_row": r, "center_col": c}`
- Server logic: find all mines in 9×9 area around target, reveal them safely (no penalty), award points
- Discovery: when the slab tile's pending reveal resolves, set `player.has_nuke = True`
- UI: highlight the nuke button when charged, show 9×9 target zone on hover

### Feature 4: Ghost Click

> Start a fake 5-second reveal animation on a tile you're not actually revealing. Opponent sees a pending action, but you're really revealing tile Y (or nothing). Unlimited uses, same 5-second timer. Opponent only learns it was fake when the timer completes and nothing is revealed.

- Hooks into: `PendingAction` + broadcast logic
- New action: `{"action": "ghost", "fake_row": r, "fake_col": c, "real_row": r2, "real_col": c2}` (or `real_row: null` for pure bluff)
- Server logic: broadcast shows a normal pending action on fake tile to opponent; real reveal (if any) is hidden until resolve
- Key: opponent's view sees a normal pending action — they can't tell it's fake until it resolves empty
- UI: from *your* perspective, show which is your ghost vs real. Opponent sees them identically.

### Feature 5: Decoy Tile

> Place a fake number indicator (or fake flag) on an unrevealed tile, making it look safe or mined to your opponent. 1 use per game.

- Hooks into: `to_dict()` — per-player state rendering
- New action: `{"action": "decoy", "row": r, "col": c, "fake_value": 3}` (or `"fake_value": "flag"`)
- Server logic: store decoy in game state, when rendering board for *opponent*, replace that cell's display
- Key: the tile is still unrevealed — decoy only changes what the opponent *sees*
- UI: show decoy-marked tiles differently to the placer (e.g., dashed border), normal to opponent

## Team Formation (10 min)

- Teams of 2–3, or work solo
- Each team picks ONE feature to implement
- Harder features (Ghost Click, Nuke) → stronger teams or more members
- Easier entry points (Cancel Timer, Block Tile) → good for solo or first-timers

## Tool Setup (5 min)

Help everyone get their tool running:

| Comfort Level | Tool | Setup |
|---------------|------|-------|
| Terminal-comfortable | **Claude Code** | `claude` in the repo directory |
| Terminal-comfortable | **Codex** | `codex` in the repo directory |
| Wants a project manager | **Imp** | Already in this repo, `imp` to start |
| Visual / lowest friction | **Lovable** | Fork the working minesweeper at [URL], copy-paste feature spec |

## Checkpoint

By 2:30, every team should:
- Have picked their feature
- Have their AI tool open and connected to the repo
- Understand which files to modify (`game.py` for server logic, `index.html` for UI)
- Have a clear first prompt in mind (e.g., "Add a cancel action that stops a pending reveal")
