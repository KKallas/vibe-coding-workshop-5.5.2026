# Step 1 — The Big Picture (0:00 – 0:30)

## Goal

Set the stage: where computers came from, what code actually is, and why we're here today building a game with AI instead of writing assembly by hand.

## Outline

### 1. From Switches to Software (10 min)

- A computer is just a rock we tricked into thinking — transistors, logic gates, binary
- Assembly language: the first human-readable layer over machine code
- Show a real x86 snippet that adds two numbers — appreciate how painful this is
- High-level languages (C, Python, JS) as layers of abstraction on top

### 2. The Abstraction Ladder (5 min)

- Each generation of tools lets you think at a higher level
- Assembly → C → Python → frameworks → no-code → **vibe-coding**
- The constant: you still need to *think about what you want*

### 3. What is Vibe-Coding? (10 min)

- Using AI (Claude Code, Codex, Cursor, Lovable, Imp) to describe intent and get working code
- Live demo: open Claude Code, type a one-liner prompt, get a working script
- It's not magic — it's a new abstraction layer. You're the architect, AI is the contractor
- When it shines vs. when it breaks (hallucinations, context limits, wrong assumptions)

### 4. Today's Mission (5 min)

- We're building **Multiplayer Minesweeper** — one shared board, both players click freely, no turns
- 5 wild power-up features you'll implement with AI tools
- Next up: I'll live-code the boilerplate so you see what we're working with, then you set up your AI tools and immediately start building
- Tools you'll choose from (set up after the live-code demo):
  - **Claude Code** — terminal-based AI coding agent
  - **Codex** — OpenAI's coding agent
  - **Imp** — project manager + coding agent (this repo's built-in tool)
  - **Lovable** — visual builder (lightest option — a working minesweeper is already there to fork)

## Materials

- Slides or terminal screen-share
- Pre-made assembly snippet to show on screen
- Claude Code open and ready for the quick demo
