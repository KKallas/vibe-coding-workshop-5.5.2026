# Step 1 — The Big Picture (0:00 – 0:30)

## Goal

Set the stage: where computers came from, what code actually is, and why we're here today building a game with AI instead of writing assembly by hand.

## Outline

### 1. From Switches to Software (10 min)

- A computer is just a rock we tricked into thinking — transistors, logic gates, binary
- The **Intel 4004 (1971)** — the first commercial general-purpose CPU on a single chip. Why it matters: collapsed a room of hardware into a component anyone could buy, and started the line that runs through every Intel chip since
- Assembly language: the first human-readable layer over machine code
- Show a real x86 snippet that adds two numbers — appreciate how painful this is
- **Assembly today isn't what it looks like** — modern CPUs do out-of-order execution, branch prediction, deep pipelines, cache hierarchies, multiple cores. Code that *looks* fast on paper often isn't, because timing and parallelization are hidden from the programmer
- Cautionary tale: Intel's **Pentium D (2005)**, the first desktop dual-core. Architecture was so hostile to hand-tuned assembly (two dies sharing a front-side bus, NetBurst's deep pipeline) that real-world performance disappointed — compilers won because humans couldn't keep the whole machine in their head anymore
- High-level languages (C, Python, JS) as layers of abstraction on top

### 2. The Abstraction Ladder (5 min)

- Each generation of tools lets you think at a higher level
- Assembly → C → Python → frameworks → no-code → **vibe-coding**
- Python is today's sweet spot, but it's not the end — even Python will fade as the loop tightens to **idea → implementation**, with Python as the training substrate underneath the model
- The pattern: use today's tool to build a slightly more exact tool for tomorrow — each iteration brings the gap between intent and result closer to zero
- The constant: you still need to *think about what you want* — and **test it by hand, many times, over and over**. That experience of tuning the feel is what turns a working prototype into **a product other people actually want to use**

### 3. What is Vibe-Coding? (10 min)

- Using AI (Claude Code, Codex, Cursor, Lovable, Imp) to describe intent and get working code
- Live demo: open Claude Code, type a one-liner prompt, get a working script
- It's not magic — it's a new abstraction layer. You're the architect, AI is the contractor
- When it shines vs. when it breaks (hallucinations, context limits, wrong assumptions)
- **Beyond code:** I keep my school coursework as a GitHub repo in Markdown — then use Claude Code to draft revisions, refactor essays, and iterate on assignments the same way I'd iterate on code. Anything that fits in plain text + version control becomes a vibe-coding workflow

### 4. Today's Mission (5 min)

- Everyone in this room has their own goal. Today we learn the **tools** to chase those goals — by building one project together, where we practice commanding this strange beast called the LLM
- Getting *something close* to your idea is easy. Getting the **exact** implementation you wanted is much trickier — that's the skill we're here to build
- We'll harness some Git magic to handle scope and review edits — the same way you'd manage a contractor you hired off Fiverr: clear briefs, small reviewable chunks, the ability to roll back when something goes sideways
- We're building **Multiplayer Minesweeper** — one shared board, both players click freely, no turns
- 5 wild power-up features you'll implement with AI tools
- Next up: I'll live-code the boilerplate so you see what we're working with, then you set up your AI tools and immediately start building
- Tools you'll choose from (set up after the live-code demo):
  - **Imp + Kimi** — *default option*. This repo's built-in agent. Imp boots the local webserver for you, and I'll hand out a Kimi API key on the day so there's nothing to sign up for or pay for
  - **Claude Code** — terminal/VS Code based AI coding agent (bring your own Anthropic key or Claude Pro/Max)
  - **Codex** — OpenAI's coding agent (bring your own OpenAI key)
  - **Lovable** — visual builder (lightest option — a working minesweeper is already there to fork)
