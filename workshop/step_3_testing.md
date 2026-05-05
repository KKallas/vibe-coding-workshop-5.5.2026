# Step 3 — Test & Debug Together (1:00 – 1:30)

## Goal

Smoke-test the boilerplate as a group. Fix bugs live. Make sure everyone can run the server and connect two players.

## Agenda

### 1. Group Test (10 min)

- I start the server on my machine (or a shared cloud instance)
- Everyone connects via their browser to the same game URL — **one shared board**
- We walk through the flow together:
  - Player 1 clicks a tile → pending action appears for both
  - Player 2 clicks a different tile at the same time → second pending action appears
  - Both 5-second countdowns run in parallel
  - Tiles reveal independently as their timers complete
  - Try both players clicking the same tile → server rejects the duplicate
  - Try hitting a mine → penalty for that player, game continues
  - Race to reveal the most safe tiles

### 2. Common Issues & Live Fixes (10 min)

Walk through things that probably broke and fix them live:

| Problem | Likely Cause | Fix |
|---------|-------------|-----|
| WebSocket won't connect | CORS or wrong port | Add CORS middleware, check URL |
| Board not rendering | Canvas sizing or coordinate math | Debug in browser console |
| Flood fill freezes | Missing visited set in BFS | Add `visited` set |
| Both players see mines | `to_dict()` not hiding mine locations | Filter unrevealed mines from state |
| Timer not working | Async timing issue | Use `asyncio.sleep` + task |

### 3. Code Walkthrough — What's Extensible (10 min)

Show participants the hooks they'll be extending:

```python
# game.py — the action handler is the main extension point
def handle_action(self, player_id: str, msg: dict):
    action = msg["action"]
    if action == "reveal":
        return self._start_reveal(player_id, msg["row"], msg["col"])
    elif action == "flag":
        return self._toggle_flag(player_id, msg["row"], msg["col"])
    # FEATURES GO HERE:
    # elif action == "cancel": ...
    # elif action == "block": ...
    # elif action == "nuke": ...
    # elif action == "ghost": ...
    # elif action == "decoy": ...
```

- Explain the `PendingAction` model — most features hook into the pending/resolve cycle
- Show where the frontend render loop picks up new state
- Point out the `Player` model fields that are already there (`blocks_remaining`, `has_nuke`, etc.)

## Checkpoint

By 2:00, everyone should:
- Have the server running locally (or access to a shared instance)
- Understand the codebase structure
- Know which file to edit and which function to extend
- Be ready to pick a feature
