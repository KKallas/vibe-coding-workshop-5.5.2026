# Step 2 — Live-Code: Minesweeper with Multiplayer (0:30 – 1:00)

## Goal

Live-code the entire working boilerplate in 30 minutes: board generation, game logic, multiplayer state, WebSocket server, and minimal frontend. **One shared board — both players click freely, no turns.**

## What We're Building

```
minesweeper/
  server.py          # FastAPI websocket server
  game.py            # Game state, players, pending actions
  board.py           # Board generation & cell state
  requirements.txt
  static/
    index.html       # Minimal canvas frontend
```

## Live-Coding Walkthrough

### 1. Board & Cells (7 min)

```python
# board.py
@dataclass
class Cell:
    is_mine: bool = False
    is_revealed: bool = False
    revealed_by: str = None    # player_id who revealed it
    adjacent_count: int = 0
    is_flagged: bool = False

class Board:
    def __init__(self, width=16, height=16, mines=40):
        self.width = width
        self.height = height
        self.grid = [[Cell() for _ in range(width)] for _ in range(height)]
        self._place_mines(mines)
        self._calculate_numbers()
```

- Random mine placement
- 8-direction neighbor counting
- `revealed_by` tracks who gets the point

### 2. Game Logic & Players (8 min)

```python
# game.py
class Player:
    id: str
    name: str
    score: int = 0              # +1 per safe reveal
    blocks_remaining: int = 3   # for Feature 2
    has_nuke: bool = False      # for Feature 3
    decoys_remaining: int = 1   # for Feature 5

class PendingAction:
    id: str                     # unique action ID
    player_id: str
    action_type: str            # "reveal" | "ghost" | "block" | "nuke" | "decoy"
    row: int
    col: int
    started_at: float           # time.time()
    duration: float = 5.0
    cancelled: bool = False

class Game:
    def __init__(self, game_id: str):
        self.board = Board()
        self.players: dict[str, Player] = {}
        self.pending_actions: list[PendingAction] = []
        self.state = "waiting"  # waiting | active | finished
```

Key points to explain:
- **No turns** — both players fire actions whenever they want
- Multiple `PendingAction`s can exist simultaneously
- Every reveal goes through a 5-second pending phase
- `Player` has resource slots for power-ups (participants will implement these later)

### 3. Action Handler (7 min)

```python
def handle_action(self, player_id: str, msg: dict):
    action = msg["action"]
    if action == "reveal":
        return self._start_reveal(player_id, msg["row"], msg["col"])
    elif action == "flag":
        return self._toggle_flag(player_id, msg["row"], msg["col"])
    # FEATURES GO HERE — participants will add:
    # elif action == "cancel": ...
    # elif action == "block": ...
    # elif action == "nuke": ...
    # elif action == "ghost": ...
    # elif action == "decoy": ...

def _start_reveal(self, player_id, row, col):
    # Create pending action (5-second timer)
    pending = PendingAction(player_id=player_id, row=row, col=col)
    self.pending_actions.append(pending)
    return {"type": "pending", "action": pending.to_dict()}

def _resolve_reveal(self, action: PendingAction):
    # Called after 5 seconds if not cancelled
    cell = self.board.grid[action.row][action.col]
    if cell.is_mine:
        self.players[action.player_id].score -= 1  # penalty
    else:
        cell.is_revealed = True
        cell.revealed_by = action.player_id
        self.players[action.player_id].score += 1
        # Flood-fill if zero adjacent
```

- Reveal logic: mine = penalty (game continues!), safe = +1 point
- Win condition: all non-mine cells revealed — highest score wins
- Flood-fill for zero-cells

### 4. WebSocket Server + Frontend (8 min)

```python
# server.py — FastAPI + websockets
@app.websocket("/ws/{game_id}/{player_id}")
async def ws(websocket, game_id, player_id):
    game = games[game_id]
    game.connect(player_id, websocket)
    async for msg in websocket.iter_json():
        result = game.handle_action(player_id, msg)
        await game.broadcast(result)
```

```html
<!-- static/index.html — minimal -->
<canvas id="board"></canvas>
<div id="scores"></div>
<script>
  const ws = new WebSocket(`ws://localhost:8000/ws/${gameId}/${playerId}`);
  ws.onmessage = (e) => renderBoard(JSON.parse(e.data));
  canvas.onclick = (e) => {
    const [row, col] = pixelToCell(e.offsetX, e.offsetY);
    ws.send(JSON.stringify({action: "reveal", row, col}));
  };
</script>
```

- `broadcast()` sends state to ALL connected players
- Pending actions shown as pulsing/highlighted cells
- Scores visible to both players

## Architecture Diagram

```
Player A (browser)          Server              Player B (browser)
     |                        |                        |
     |── reveal(3,4) ────────>|                        |
     |                        |── pending(3,4) ───────>|
     |<── pending(3,4) ───────|                        |
     |                        |                        |
     |                  Player B clicks (7,2)          |
     |                        |<── reveal(7,2) ────────|
     |<── pending(7,2) ───────|                        |
     |                        |── pending(7,2) ───────>|
     |                        |                        |
     |    ... both 5s timers run in parallel ...        |
     |                        |                        |
     |<── resolved(3,4) ──────|── resolved(3,4) ──────>|
     |<── resolved(7,2) ──────|── resolved(7,2) ──────>|
```

## Key Teaching Moments

- **Why 5 seconds?** — Creates the space for cancel, ghost click, and mind games
- **Why no turns?** — More exciting, more chaotic, more room for power-ups to matter
- **Why track `revealed_by`?** — Scoring. It's a race.
- **Show a prompting moment**: "If I were using Claude Code right now, I'd say: 'Add flood-fill BFS to _resolve_reveal that reveals all connected zero-cells and awards each to the player'"

## Checkpoint

By 1:00, the server should be running and two browser tabs can:
- Connect to the same game (shared board)
- Both click tiles freely at the same time
- See 5-second pending animations
- See tiles reveal after timer
- See scores update
