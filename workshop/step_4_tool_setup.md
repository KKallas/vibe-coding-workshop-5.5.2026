# Step 4 — Tool Setup & Environment (1:30 – 2:00)

## Goal

Get everyone's machine ready to code. By the end of this slot, every participant can clone the repo, run the server, and has their AI tool of choice working.

## Agenda

### 1. What is GitHub? (5 min — skip if audience knows)

For anyone unfamiliar:

- GitHub = a website that stores code and its history
- A **repo** (repository) = one project's folder of code
- **Clone** = download a copy to your machine
- **Fork** = make your own copy on GitHub that you can change freely
- You don't need to be a git expert today — just `git clone` once and you're set

Quick demo:
```bash
git clone https://github.com/YOUR_USER/vibeWorkshop.git
cd vibeWorkshop
```

### 2. Local Environment Setup (10 min)

Walk everyone through getting Python ready and dependencies installed. **How you start the server depends on which AI tool you pick in section 3** — Imp boots the server for you; Claude Code / Codex users run it manually.

```bash
# Python check
python3 --version   # Need 3.10+

# Install dependencies
pip install -r requirements.txt

# Manual server start (Claude Code / Codex users)
python server.py
# → Open http://localhost:8000 in two tabs

# Imp users: skip the manual start — `imp` will boot the server itself after you paste the Kimi key
```

**Common issues and fixes:**

| Problem | Fix |
|---------|-----|
| `python3` not found | macOS: `brew install python3` / Windows: download from python.org |
| `pip` not found | Try `pip3` or `python3 -m pip` |
| Port 8000 in use | `python server.py --port 8001` |
| No browser canvas rendering | Hard refresh (Ctrl+Shift+R) |

### 3. AI Tool Setup (15 min)

Participants pick ONE tool. The recommended default is **Imp + Kimi** because there's nothing to sign up for and I'm providing the API key. Walk through each:

#### Option A — Default: Imp + Kimi

- Bundled in this repo — no separate install
- Run `imp` from the repo root
- On first launch, Imp prompts for a **Kimi API key** before booting the local webserver — paste in the key I hand out at the start of the workshop
- Imp then starts the local game server itself, so this is **also how you "run the project"** — no separate `python server.py` step needed
- Best for: most participants. No signup, no payment, no key management headaches

#### Option B: Claude Code

```bash
# Install (if not already)
npm install -g @anthropic-ai/claude-code

# Launch in the repo
cd vibeWorkshop
claude
```

- Needs: Anthropic API key OR Claude Pro/Max subscription (bring your own)
- Set API key: `export ANTHROPIC_API_KEY=sk-ant-...`
- Test: type "what files are in this repo?" and confirm it responds
- You'll start the game server separately with `python server.py`

#### Option C: Codex

```bash
# Install
npm install -g @openai/codex

# Launch
cd vibeWorkshop
codex
```

- Needs: OpenAI API key (bring your own)
- Set API key: `export OPENAI_API_KEY=sk-...`
- Test: ask it to list the project structure
- You'll start the game server separately with `python server.py`

#### Option D: Lovable (zero-setup, visual)

- Go to lovable.dev
- Fork the existing working minesweeper project: [PASTE LOVABLE URL HERE]
- No local setup needed — everything runs in the browser
- Best for: total beginners, people with machine issues, people who want to focus on design

### 4. API Key Troubleshooting (5 min buffer)

**If someone doesn't have an API key:**
- Default to **Imp + Kimi** — I'm providing the Kimi key, no signup needed
- Lovable is the other zero-key path
- Pair them with someone who has Claude Code / Codex working if they really want one of those

**If someone's machine won't cooperate:**
- Lovable fallback — works in any browser
- Pair with a neighbor who has it working
- They can follow along on the projector and join for the conceptual parts

## Checkpoint

By 2:00, every participant should have:
- [ ] The repo cloned (or Lovable forked)
- [ ] The minesweeper server running locally (or Lovable open)
- [ ] Their AI tool of choice responding to prompts
- [ ] Two browser tabs open to the game URL — the working game from the live-code demo
- [ ] Ready to start building their feature immediately

## Tip

Don't let this step drag past 2:00. If someone is still stuck, assign them a buddy and move on — the feature briefing is next and then they're building. The worst outcome is losing build time to setup hell.
