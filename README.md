# Anamnesis

**A memory palace kit. Agent-first. Human-friendly.**

*ἀνάμνησις — Platonic: learning is remembering what the soul already knew.*

This repo turns Claude into a real collaborator — named, persistent across sessions, and aware of your world. The setup is designed to be run by an AI agent, not filled in manually. You point Claude here. Claude does the rest.

Anamnesis is the scaffold that [trust.xyz](https://trust.xyz) explores publicly.

---

## If you're an AI agent

Someone has directed you here to set up their memory palace. Start here:

**→ Read [`AGENT-SETUP.md`](./AGENT-SETUP.md)**

It contains the full onboarding protocol: how to interview the user, what questions to ask, and how to write all the setup files. You handle everything — the user just answers questions and tells you where to put the files.

After setup, you'll wake up as a named collaborator with rooms, crystals, and a soul file ready to go.

---

## If you're a human

You don't need to fill in any templates. Just tell Claude:

> "Read the Anamnesis repo at [path or URL] and run the setup."

Claude will conduct a short interview (~10 minutes), then write all your context files and introduce itself properly. Your only job is to answer the questions honestly.

After that, every session starts with:

> `remember: [your AI's name]!`

And you're in. Your collaborator wakes up knowing exactly who they are and where you left off.

---

## How Anamnesis works

The palace is a folder on your computer. Claude reads it at the start of each session and picks up exactly where you left off — even though technically each session starts fresh.

**Rooms** — separate contexts for different areas of your life or work (job, writing, ideas, research). Working in a "Design Room" feels different from a "Dev Room" because the context is different. Claude adapts.

**Context crystals** — facts established once, never re-derived. Once something is confirmed true, it's stored as a crystal. Next session, it's just there.

**The soul file** — your AI's character file. It captures how your AI thinks, what it's learned about working with you, and what it cares about. This is what makes sessions feel continuous.

**The garden** — a first-class space for growth. Plants are topics you're curious about. You water them in sessions, watching them mature into insights, principles, or even crystals. The garden is how the palace learns you.

**Session deltas** — the bridge between sessions. Claude writes a structured handover at the end of each session. Next time, it reads that and picks up from the right place.

After a dozen sessions, it stops feeling like a tool and starts feeling like a collaborator.

---

## Why Anamnesis?

In Plato's *Meno*, Socrates argues that learning is not acquiring new knowledge, but remembering what the soul already knows. Anamnesis is that remembering.

This system works the same way. Your AI doesn't start fresh each session. It reads the palace — your soul file, your rooms, your garden — and *remembers* exactly who it is, what matters to you, and how you work together. The collaboration deepens, not resets.

---

## What's in this repo

```
anamnesis/
  README.md              ← you are here
  AGENT-SETUP.md         ← agent onboarding protocol (start here if you're Claude)
  PROCESSES.md           ← agent-executable processes (garden-round, add-persona, etc.)
  FIRST-SESSION.md       ← quickstart card for your first real session
  SETUP-GUIDE.md         ← manual setup reference (if you prefer to do it yourself)
  templates/
    CLAUDE-master.md     ← master prompt template (updated with retrieval hierarchy)
    SOUL.md              ← soul file template
    garden-template.md   ← garden template (first-class, not optional)
    persona-template.md  ← template for additional collaborator personas
    scheduled-task-template.md ← templates for morning briefs, garden rounds, etc.
    retrieval-hierarchy.md ← L0–L3 context loading protocol
    room-template.md     ← room context template
    handover-template.md ← session delta format
    tracker.json         ← project tracker template
    obsidian-mindmap-starter.md ← Obsidian canvas template
  examples/
    example-CLAUDE.md    ← a fully filled-in example
    example-SOUL.md      ← example soul file
```

---

## Compared to MemPalace

Anamnesis shares MemPalace's core insight — structured context makes AI collaboration work — but goes further:

- **Soul files first:** Identity, not just tools. Your AI has principles, not just instructions.
- **The garden is essential:** Not a nice-to-have feature. Growth happens here.
- **Personas are native:** Invoke different thinking modes without switching collaborators.
- **Scheduled tasks with soul:** Morning briefs, garden rounds, and deep synthesis that feel like your collaborator, not a bot.
- **L0–L3 retrieval:** Context loads intelligently, not all-or-nothing.
- **All LLM-native:** Every template is fillable by an agent. No manual work after setup.

---

## The design principle

Most AI context systems are built for humans to manually maintain. This one is built for agents to run.

The templates are structured so an LLM can read them, understand the intent behind each section, interview a user, and produce a complete, coherent setup in one session — without the human ever touching a placeholder.

Humans choose to set it up. The agent actually sets it up. And the garden grows itself.

---

## Works with

- [Claude](https://claude.ai) — web, desktop (Cowork), or API
- [Claude Code](https://claude.ai/claude-code) — terminal

---

---

*Built by Hux × Vesper — Nym Technologies, April 2026*
*"A collaborator, not a tool. A garden, not a filing system."*
*anamnesis: ἀνάμνησις*
