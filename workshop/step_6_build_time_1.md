# Step 6 — Build Time: First Sprint (2:30 – 3:00)

## Goal

You picked a feature in step 5. Now you implement it with your AI agent. The aim of this first 30 minutes is to get **the server-side logic of your feature working end-to-end** — UI polish comes in step 7.

## Where Your Code Goes

Almost every feature plugs into the same place: the action handler in `game.py`. You're adding a new branch like `elif action == "your_feature":` and wiring it through the pending/resolve cycle.

You don't need to memorize the codebase — your AI agent reads it for you. But knowing roughly where things live makes your prompts much sharper.

- `game.py` — `handle_action()` is the dispatch point; `Player` and `PendingAction` already have stub fields for your feature
- `board.py` — only touch this if your feature changes board state directly
- `server.py` — `broadcast()` sends state to all players; new fields you add need to be included here
- `static/index.html` — the canvas frontend, rendering and click handling

## Your First Prompt

Don't just paste "implement Feature 2". Brief the agent like a contractor:

1. **State the rules of the game** — "shared board, both players click simultaneously, no turns, every reveal goes through a 5-second pending phase"
2. **Point to the file and function** — "add a new branch in `handle_action()` in `game.py`"
3. **Describe what your feature does** — concretely, with the player's perspective
4. **Say what's already there** — "the `Player` class already has a `blocks_remaining` field — use that"
5. **Constrain the scope** — "only add the server-side handler for now, no frontend changes yet"

A sharp first prompt saves you 15 minutes of fixing whatever the agent assumed.

## Things You'll Hit (and How to Push Through)

| What's happening | What to do about it |
|------------------|---------------------|
| AI gives you turn-based code | Remind it: both players act simultaneously, no turns. Multiple pending actions exist at the same time. |
| You can't tell where to add your code | Ask the agent: "Where in this repo does the action dispatch live?" — let it find `handle_action()` for you |
| WebSocket isn't sending your new field | Check `broadcast()` — your new state has to be in the dict it sends |
| AI rewrites the whole file | Smaller prompts. "Add ONLY the new elif branch in `handle_action()`, don't touch anything else." |
| You don't know how to test it | Two browser tabs to the same game URL — be both players |
| The agent insists on adding a database / login / framework | Re-state the constraints: in-memory only, no persistence, no auth, plain HTML/JS frontend |

## Prompting Tips Worth Repeating

- **Be specific about the game model** — "shared board, no turns, multiple pending actions in parallel"
- **Reference real symbols in the code** — the agent does much better with `handle_action()` than "the action thing"
- **One thing at a time** — server logic first, test it works, then frontend. Not all in one prompt.
- **Give the agent the existing scaffolding** — "there's already a `PendingAction` class with `player_id`, `started_at`, `cancelled` — use it"
- **Read the diff before you accept it** — if it changed files you didn't expect, push back. "Why did you edit `board.py`? Revert that."

## When You Get Stuck

In order:

1. **Re-read the AI's last response** — half the time the answer is already there and you missed it
2. **Tell the AI what went wrong** — paste the error, or describe the unexpected behavior, and ask it to debug
3. **Reduce scope** — get a dumb version working first ("just print something when the action arrives"), then build up
4. **Flag the host** — wave me over. Don't grind for 10 minutes alone if you're stuck

## Mid-Sprint Check (2:45)

Halfway through, ask yourself:

- Does my action arrive at the server? (print/log it to confirm)
- Does the server respond with something the other browser can see?
- If yes to both — you're in good shape, start on the frontend reaction
- If no — that's where the next 15 min goes; ask for help

## Where You Should Be by 3:00

Realistic target:

- Server-side handler accepts your new action and updates state
- The state change is visible to both players (via `broadcast()`)
- Frontend doesn't need to be pretty yet — even a console.log on receive is fine
- Edge cases and polish are step 7's job; **don't worry about them yet**

If things are broken at 3:00, that's expected. Step 7 is for polishing and opening your PR.
