# Idea A — Graph Beautifier App (Lovable + Nano Banana)

A small web tool that takes a pasted screenshot, lets you crop it, accepts a text prompt, sends it to Nano Banana (Gemini 2.5 Flash Image) for *decorative finishing*, and returns a polished image you can copy-paste into PowerPoint or Google Slides.

## Why this for this audience

Every corporate/govt employee puts screenshots into decks. The tool fits a workflow they already do daily, just with better output. They walk out of the workshop with a working URL they can use Monday morning — that alone justifies the workshop fee in their internal accounting and gives you word-of-mouth.

It also doubles as the workshop's central live-coded demo: the act of *building it* in front of them is the "watch a maker think out loud" lesson, and the tool's *design* embodies the data-integrity lesson (Nano Banana for finishing only, not content generation).

## Architecture

- **Frontend:** Lovable (React + Tailwind, what it generates by default)
- **Clipboard paste of screenshots:** browser `paste` event with `ClipboardEvent.clipboardData.items` filtering for images. Well-supported, trivial.
- **Crop UI:** `react-image-crop` or similar; Lovable handles this fine.
- **Text prompt input:** trivial.
- **Nano Banana call:** Gemini 2.5 Flash Image API takes image + text and returns image. **Do not put the API key client-side** — anyone with DevTools steals it. Right architecture is a Supabase edge function as a proxy (Lovable supports this). Pre-stage the secret-handling part before the live demo.
- **Copy result to clipboard:** `navigator.clipboard.write([new ClipboardItem({'image/png': blob})])`. Works reliably in Chrome and Edge, mostly in Safari, less so in Firefox. Most corporate/govt audiences are on Chrome — fine. Test on the conference-room machine before workshop day.

Estimated build time live: 30–45 minutes if rehearsed once cold. Don't try to build it cold for the first time live — small infrastructure things go wrong and undermine you.

## The critical design constraint (this is the lesson, not just a UX detail)

Nano Banana is **not pixel-faithful with content**. If someone pastes a chart screenshot and prompts "make this look polished," it can quietly change bar heights, relabel axes, or invent legend entries — that's how image-edit models work. They regenerate, they don't strictly transform.

So the tool — and your demo narration — must be specifically positioned for **decorative polish**:
- Backgrounds, frames, brand color palettes
- Slide-template harmonization
- Removing UI chrome from the screenshot
- Adding tasteful typography around the chart

Not for:
- "Improve the content of this chart"
- Anything that asks the model to interpret or rewrite the data

Bake this into the tool's UI copy (placeholder prompts, helper text) and into how you talk about it while building. The data-integrity habit then lives **in the tool's affordances and your narration**, not as a separate lecture later.

## Pedagogical role in the workshop

1. **Live build of the tool (30–45 min)** — the central demo. You narrate prompts, hit failures, recover, iterate. They watch a maker think out loud about a real piece of work, on a problem they care about.
2. **Tool becomes their finishing station** — the pie-graph exercise (see Idea B) uses *this tool* as the polish step. Workshop's demo becomes the workshop's exercise's final stage. Every part compounds into the next part.
3. **Take-home artifact** — they leave with a URL and a habit, not just a memory.

## Pre-workshop checklist

- [ ] Decide whether you ship your own Gemini key (with rate-limit guards) or have each user enter their own
- [ ] Pre-stage the Supabase edge function before the live build, or rehearse building it in <5 minutes
- [ ] Test clipboard write on the actual conference-room machine and projector setup
- [ ] Pick a placeholder screenshot to use during the demo build — ideally something representative of what they'll bring
- [ ] Have a fallback if Gemini API has an outage (cached pre-rendered example, screenshot of expected output)
- [ ] Rehearse the build cold once, end to end, so the live version is your second time not your first

## Open questions for next session

- Should the tool be pre-built before the workshop and demoed running, or built live? Lean: built live with rehearsal, because the build is the lesson — but a pre-built backup version should exist in case of disaster.
- One-shot prompt UX, or template chips ("polish background", "add brand colors", "remove window chrome")? Template chips reduce the failure surface for first-time users but reduce the precision-of-intent practice. Maybe both — template chips that pre-fill the prompt, which they can then edit.
- What demo screenshot to use? A pie chart from Excel feels too on-the-nose given Idea B's pie-graph exercise. Maybe a table screenshot, so you don't telegraph the exercise.
