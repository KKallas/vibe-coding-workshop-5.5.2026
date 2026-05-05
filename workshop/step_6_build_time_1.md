# Step 6 — Build Time: First Sprint (2:30 – 3:00)

## Goal

Teams start implementing their chosen feature using AI tools. You circulate, unblock, and coach prompting techniques.

## Your Role as Facilitator

### Circulate & Unblock

- Walk around (or monitor screens) every 3–5 minutes
- Common blockers and how to help:

| Blocker | Coaching Response |
|---------|-------------------|
| "AI gave me turn-based code" | "Remind it: both players act simultaneously, no turns. Multiple pending actions exist at once." |
| "Where do I add my action?" | "Look at `handle_action()` in `game.py` — add an `elif action == 'your_feature':` branch" |
| "The WebSocket isn't sending my new field" | "Check `broadcast()` — make sure your new state is included in the dict" |
| "AI rewrote the whole file" | "Use smaller prompts. Ask it to ONLY add the new elif branch, nothing else." |
| "How do I test this?" | "Open two browser tabs to the same game URL and try both sides" |

### Prompting Tips to Share

Share these with teams who are struggling:

1. **Be specific about the game model**: "This is a shared board — both players click freely, no turns. Multiple pending actions run in parallel."
2. **Reference existing code**: "Add a new branch in `handle_action()` that handles action type 'cancel'"
3. **One thing at a time**: Don't ask for server + client + UI in one prompt. Do server logic first, test it, then UI.
4. **Give context on what exists**: "There's already a `PendingAction` class with `player_id`, `started_at`, and `cancelled` fields"

### Quick Wins to Celebrate

If a team gets something working early:
- Have them demo to a neighbor
- Suggest edge cases to handle (what if both players cancel each other simultaneously?)
- Challenge: make the UI feedback clearer

## Progress Checkpoints

At **2:45** (halfway), quickly poll teams:

- "Who has server logic working?" → celebrate
- "Who is stuck?" → spend 2 min pairing
- "Who hasn't started yet?" → help with first prompt

## Expected State by 3:00

Most teams should have:
- Server-side logic partially working (action handler responds)
- Maybe not fully tested end-to-end yet
- Some UI changes started

It's fine if things are broken — that's what the next 30 min is for.
