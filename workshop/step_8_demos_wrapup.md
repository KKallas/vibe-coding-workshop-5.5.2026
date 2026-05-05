# Step 8 — Demos & Wrap-Up (3:30 – 4:00)

## Goal

Each team demos their feature, we play a round with everything combined (if possible), and close with takeaways about AI-assisted development.

## Demo Format (20 min)

### Structure: 2–3 minutes per team

1. **What feature did you build?** (10 sec — everyone already knows)
2. **Live demo** — show it working in two browser tabs (1.5 min)
3. **How did you build it?** — show one key prompt you gave the AI and what it produced (30 sec)
4. **What surprised you?** — one thing that was easier or harder than expected (30 sec)

### Demo Order

Go from simplest to most complex:
1. Cancel Timer
2. Block Tile
3. Decoy Tile
4. Ghost Click
5. Nuke 'Em

### If a Feature Doesn't Fully Work

That's totally fine! Have the team:
- Show what they got working (even if it's just the server accepting the action)
- Explain their design (show the code / prompts)
- Say what they'd do with 30 more minutes

## Combined Playtest (5 min — if time allows)

If multiple features work and are mergeable:
- One brave team merges 2–3 features into one server
- Everyone connects and we play a chaotic round together
- This is purely for fun — don't stress about merge conflicts

## Wrap-Up Discussion (5 min)

### Key Takeaways

1. **AI doesn't replace understanding** — you still needed to know what "simultaneous actions" means, what a WebSocket does, and where to hook into the code
2. **Prompting is a skill** — being specific about the game model ("shared board, no turns, parallel pending actions") made the AI 10x more useful
3. **The abstraction ladder continues** — assembly → C → Python → frameworks → AI-assisted. Each layer lets you think bigger, but the thinking still matters
4. **Iteration > perfection** — the teams that shipped fastest gave small, focused prompts and tested after each one

### What's Next?

- The repo is yours — keep building, add more features, make it 4-player
- Try combining all 5 features into one game — the interactions get wild
- Bring vibe-coding into your own projects — start with a clear spec, small prompts, test often

## Logistics

- Share the repo link one more time
- Collect feedback (quick survey or just a thumbs-up/down)
- Thank everyone for participating

---

*Total workshop time: 4 hours*
*Actual coding time for participants: ~60 minutes*
*That's the whole point — AI compresses build time, but you still architect the solution.*
