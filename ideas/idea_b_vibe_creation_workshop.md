# Idea B — Vibe Creation Workshop (full v2 redesign)

A reframe of the workshop from "vibe coding" to "vibe creation," based on the v1 retro (2026-05-05) and the resulting audience analysis.

## What changed in the framing

**v1 was:** teach non-technical adults to vibe-code a multiplayer minesweeper with feature briefings, using Lovable / Imp / Claude Code / Codex.

**v2 is:** teach non-technical adults to *command AI tools to produce credible artifacts they can use at work*, with the data-integrity habit baked into the tooling and the narration. The artifact medium shifts from "working software" (which they refuse) to "polished work-shaped outputs" (which they want).

## Audience model (sharpened from v1)

The people who pay for a weekend workshop are **strivers, not established bosses**. Established bosses don't come to weekend workshops — they have assistants for that. Strivers are middle-career, ambitious, looking for a leverage point, hungry to be visibly productive at scale. They are trying to *perform their way into* the boss position the established bosses already occupy.

Implications:
- They have organizational ambition but **not yet senior-position self-preservation reflex** — they're climbing, and slop production is one of the rungs.
- They have the **opposite incentive structure** from established bosses: speed beats accuracy, because they need to be visible at volume to get noticed, and the audit they'd fail won't happen until after they've been promoted past it.
- They already have ChatGPT and Nano Banana on their phones. The workshop is **calibration, not first contact**.
- Their stated goal in v1 was "personal homepage." This is a failure of imagination — most actually want internal-tool shapes (lead tracker, meeting notes organizer, contact list with photos, project status form). They didn't have the vocabulary to ask for what they actually wanted.

## The win condition

Not "convert them into makers" — they refused that in v1 and will refuse it again. Not "make them better at slop production" — that drifts the workshop toward McKinsey ammunition.

**The win is exposure.** Get them to listen to a maker for three hours and let what sticks stick. Realistic absorption rate: ~30%. That means six of twenty walk out slightly more grounded — with the data-integrity habit, with a vague sense that there's craft underneath their commanding, or both. The other fourteen got a tool and a polished artifact. All outcomes are acceptable.

This dissolves the "do I become one of them" fear: you don't. You stay fully yourself, audibly and visibly, in front of them for three hours. *That visibility* is what they paid for whether they realize it or not.

## The pitch (positioning for the strivers' actual interest)

Don't sell ethics — sell career risk management. Slop saturates fast. Within 18–24 months every LinkedIn feed, every internal deck, every quarterly report is 70% AI-generated, and the differentiator stops being "I produced an artifact" and starts being **"my artifact doesn't look like AI slop and holds up under five minutes of scrutiny from someone with a grudge."**

The careful workflow — real numbers, decorative finish, defensible substance — becomes a moat in the post-slop equilibrium, not a virtue. Frame the data-integrity habit as **not getting caught at the wrong end of the slop curve when the inevitable backlash arrives.** That speaks to their real interest, which isn't the artifact, it's not getting caught, and ideally being promoted past the people who did.

## Curriculum redesign

### Cut from v1
- Intel 4004 / assembly / abstraction-ladder section. Compress to one sentence: "every generation of programming made the gap between idea and result smaller; today the gap is just talking."
- Imp / bash / git tooling references (Lovable was the right call for v1; commit to it for v2)
- Multiplayer minesweeper as the shared example (it triggered "I'm not making a stupid game" rejections)
- Feature briefing with Ghost Click / Decoy Tile / Nuke (these only make sense to people who can already see themselves as builders)

### Keep
- Lovable as the primary tool (lowest friction, no terminal)
- The "command precisely or get the wrong thing" core lesson — but reframed in their vocabulary as briefs / specs / acceptance criteria

### Add
- **Familiar work-shaped templates** — start them on a shape they recognize, not a blank canvas. Candidates: table view with filters, form view with required fields, list-with-detail master/detail screen, basic KPI dashboard. They've stared at these for fifteen years; the "what do you want?" question shrinks from invention to slot-filling.
- **Live build of the graph beautifier tool** (see Idea A) — central demo. 30–45 min of narrated maker-thinking on a problem they care about.
- **Pie-graph reflection gate** — the closing exercise and demos. Each person produces a pie graph using a familiar template, polishes it via the tool you just built in front of them, and presents in 90 seconds.

### Critical: don't make the templates ironic-ugly
"Bad ERP UI" is a joke that lives in the facilitator's head, not in the audience's. To them, SAP-style functional ugliness is *trustworthy* — that's what real software at work looks like. Honest and generic, not parodic. But also not designer-pretty: the v1 facilitator (Kaspar) has 15 years of experience that says daily ERP users hate "nice" redesigns. The workshop is not real ERP though — they're not doing 8-hour data entry, they're prototyping in three hours and showing off — so a notch above production-ERP ugliness is probably right. Empirical question; test before committing.

## Structural beats (gates)

1. **Gate 1 — Exposure:** Watch a maker think out loud during the live build of the graph beautifier tool. Passive, but concentrated. The thing they cannot get from a YouTube grifter, because grifters don't reason in public — they perform a finished result.
2. **Gate 2 — Production:** Pick a familiar template, customize it, run an exercise that produces a pie graph, polish it via the tool from Gate 1.
3. **Gate 3 — Reflection:** 90-second presentation per person, plus one reflection question that surfaces editorial choice. Twenty people × 2 minutes = ~40 minutes of closing. This *is* the demos-and-wrap-up that v1 didn't get to.

The reflection prompt matters more than the chart. "Reflect on your pie graph" is too soft and they'll fill it with corporate filler. Use something narrower:
- *"What did you leave off the chart, and why?"*
- *"If your boss saw this and asked one question, what would it be?"*

These force the editorial choice into the open and you cannot fake your way through them with vibes.

## The reframe to embed throughout the workshop

Strivers have spent careers commanding *people*, who fill in their gaps, ask clarifying questions, smooth over their vagueness, and protect them from their own imprecision. AI does not do that — it builds whatever sloppy thing they said, fast, in three variations. That gap — between commanding a person and commanding a tool that takes you literally — is the entire skill being taught. Frame it in their language: writing a good brief, writing tight specs, defining acceptance criteria. They already understand briefs. They already write briefs at work. They write *bad* ones, and the org silently corrects them. Strip the human mediator away for three hours and let them feel what their own briefs actually contain.

## Open questions for next iteration

- **Which 4 starter templates exactly?** Table+form+list+dashboard is one mix. Or replace dashboard with "contact card with photo" since v1's lead-data woman wanted that. Test before committing.
- **Pricing/positioning:** does this still get sold as "vibe-coding" (existing brand) or rebadged as "vibe-creation" (better fit) or "AI artifact workshop" (most honest)? Trade brand recognition vs audience-fit clarity.
- **Graceful escape path** for people who refuse the templates and want their own thing. v1 lesson: a meaningful fraction will. Have a path that doesn't leave them stranded — maybe "you can use the templates as scaffolding for your own thing, here's how to fork."
- **How to handle the lead-data-woman archetype** — the participant who wants AI to figure out what she wants and refuses to elaborate. Possibly a structured pair exercise: *interview your neighbor about what they want until you can write the prompt for them.* Forces articulation through dialogue rather than introspection. Worth piloting.
- **Empirical pre-test:** put one template + the graph beautifier tool in front of three friends-of-friends from the demographic before committing the curriculum. The instinct is right; the specific shapes that resonate are an empirical question.

## Facilitator notes (for Kaspar, future-self)

- The fear you started with (the room scares you) is partly fear of being absorbed into their world. The pivot to vibe-creation can either inoculate against that or accelerate it depending on where you draw the line. Draw it in advance, before you're standing in front of twenty people.
- **Keep the discomfort.** It's load-bearing. The day you stop worrying about whether your tools will be misused is the day the curriculum drifts toward the slop end, because nothing internal is pulling it back.
- You don't have to like the room. You just have to find the version of the lesson the room can hear, and *"you are a commander, you command imprecisely, today we fix that — as career insurance"* is a lesson Dilbert's boss-in-training will sit still for, because it flatters him while teaching him.
- The marmoset-with-nukes image: the marmosets aren't the established bosses (they're risk-averse and won't show up). They're the climbers — exactly your audience, exactly why teaching slop-resistance to them matters. Untaught marmosets still have nukes; they just operate them worse.
