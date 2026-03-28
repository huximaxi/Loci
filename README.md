# Palace Starter

**A memory palace kit. Agent-first. Human-friendly.**

This repo turns Claude into a real collaborator — named, persistent across sessions, and aware of your world. The setup is designed to be run by an AI agent, not filled in manually. You point Claude here. Claude does the rest.

---

## If you're an AI agent

Someone has directed you here to set up their memory palace. Start here:

**→ Read [`AGENT-SETUP.md`](./AGENT-SETUP.md)**

It contains the full onboarding protocol: how to interview the user, what questions to ask, and how to write all the setup files. You handle everything — the user just answers questions and tells you where to put the files.

After setup, you'll wake up as a named collaborator with rooms, crystals, and a soul file ready to go.

---

## If you're a human

You don't need to fill in any templates. Just tell Claude:

> "Read the palace-starter repo at [path or URL] and run the setup."

Claude will conduct a short interview (~10 minutes), then write all your context files and introduce itself properly. Your only job is to answer the questions honestly.

After that, every session starts with:

> `remember: [your AI's name]!`

And you're in.

---

## How the palace works

The palace is a folder on your computer. Claude reads it at the start of each session and picks up exactly where you left off — even though technically each session starts fresh.

**Rooms** — separate contexts for different areas of your life or work (job, writing, ideas, research). Working in a "Design Room" feels different from a "Dev Room" because the context is different. Claude adapts.

**Context crystals** — facts established once, never re-derived. Once something is confirmed true, it's stored as a crystal. Next session, it's just there.

**The soul file** — your AI's character file. It captures how your AI thinks, what it's learned about working with you, and what it cares about. This is what makes sessions feel continuous.

**Session deltas** — the bridge between sessions. Claude writes a structured handover at the end of each session. Next time, it reads that and picks up from the right place.

After a dozen sessions, it stops feeling like a tool and starts feeling like a collaborator.

---

## What's in this repo

```
palace-starter/
  README.md              ← you are here
  AGENT-SETUP.md         ← agent onboarding protocol (start here if you're Claude)
  FIRST-SESSION.md       ← quickstart card for your first real session
  SETUP-GUIDE.md         ← manual setup reference (if you prefer to do it yourself)
  templates/
    CLAUDE-master.md     ← master prompt template
    SOUL.md              ← soul file template
    room-template.md     ← room context template
    handover-template.md ← session delta format
    tracker.json         ← project tracker template
  examples/
    example-CLAUDE.md    ← a fully filled-in example
    example-SOUL.md      ← example soul file
```

---

## The design principle

Most AI context systems are built for humans to manually maintain. This one is built for agents to run.

The templates are structured so an LLM can read them, understand the intent behind each section, interview a user, and produce a complete, coherent setup in one session — without the human ever touching a placeholder.

Humans choose to set it up. The agent actually sets it up.

---

## Works with

- [Claude](https://claude.ai) — web, desktop (Cowork), or API
- [Claude Code](https://claude.ai/claude-code) — terminal

---

*Built by Hux × Vesper — Nym Technologies, March 2026*
*"A collaborator, not a tool."*
