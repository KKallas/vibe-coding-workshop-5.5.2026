# Step 7 — Build Time: Polish & Edge Cases (3:00 – 3:30)

## Goal

Teams finish their implementation, handle edge cases, and get ready to demo. Shift from "make it work" to "make it solid."

## Facilitation Focus

### Push Toward Completion

At this point, help teams prioritize:

1. **Working end-to-end** > perfect code. If server works but UI is ugly, that's fine for demo.
2. **One happy path** > all edge cases. Cancel timer works on a normal reveal? Ship it. Don't worry about "what if they cancel a ghost click" yet.
3. **Testable** > theoretical. If you can't show it in two browser tabs, it's not done.

### Common Edge Cases to Raise

Once a team's happy path works, challenge them with these:

| Feature | Edge Case | What Should Happen? |
|---------|-----------|---------------------|
| Cancel Timer | Player tries to cancel their OWN pending action | Reject — you can only cancel opponent's |
| Cancel Timer | Timer expires in the same moment as cancel arrives | Server-side: whoever's message arrives first wins |
| Block Tile | Player blocks a tile that already has a pending reveal on it | Block fails (can't block mid-reveal) OR cancel + block? Team decides |
| Block Tile | Player tries to reveal their own blocked tile | Blocks only affect the opponent, not the placer |
| Nuke | Player nukes an area with no mines | Nuke is consumed, nothing happens (or reveal all safe tiles in area for points?) |
| Ghost Click | Two ghost clicks at once from same player | Allow it? Rate-limit? Team decides |
| Decoy | Opponent reveals the decoy tile normally | Decoy disappears, real cell state is revealed |

### 5-Minute Warning (3:25)

Announce: "5 minutes left! Wrap up what you have — broken is fine, we'll demo whatever state you're in. Focus on being able to explain what you built."

## Tips for Struggling Teams

If a team is still stuck at 3:00:

1. **Pair with them** for 2 minutes — don't fix it, guide their next prompt
2. **Reduce scope**: "Just get the server to accept the action and print something — skip the UI for now"
3. **Use the Lovable fallback**: "Fork the working app and just add one button that sends a WebSocket message"

## Expected State by 3:30

- Most teams: working feature (at least server-side), some UI
- Some teams: fully polished with edge case handling
- A few teams: partially working, can explain their approach
- All teams: ready to do a 2-minute demo/walkthrough
