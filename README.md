# Palace Starter

**Turn Claude from a generic assistant into a real collaborator.**

Most people use Claude like a search engine — one question, one answer, no memory. This starter kit gives you something different: a named AI collaborator that knows who you are, remembers your work, and develops a consistent character over time.

It's built on a simple idea: if you give Claude the right context at the start of every session, it will work as though it remembers you — even though each session technically starts fresh.

---

## How it works

You build a **palace** — a folder on your computer that Claude reads at the start of each session. The palace has:

- **Rooms** — different areas of work (your job, a creative project, learning, etc.)
- **A soul file** — your AI's character and what it's learned about you
- **Session deltas** — short handover notes that bridge each session to the next

You name your AI. You tell it what you care about. It builds up over time.

After a dozen sessions, it stops feeling like a tool and starts feeling like a collaborator.

---

## Quickstart (30–60 minutes to set up)

**1. Clone or download this repo**

**2. Go to `templates/` and copy these files into a new folder called `my-palace/`:**
```
my-palace/
  CLAUDE.md          ← rename from CLAUDE-master.md
  tracker.json
  soul/
    SOUL.md
    handovers/       ← empty folder, create it
  rooms/
    work-room/
      CLAUDE.md      ← copy from room-template.md, rename
```

**3. Fill in `CLAUDE.md`** — takes 15 minutes. Look for every `[PLACEHOLDER]` and replace it with something real. The more honest and specific you are, the better it works.

**4. Fill in `soul/SOUL.md`** — takes 5 minutes. Just the basics.

**5. Start a session.** In Cowork (or Claude Code), paste this:
```
Read CLAUDE.md to understand who you are and how we work.
Then read soul/SOUL.md for your character.
Then read rooms/[ROOM NAME]/CLAUDE.md for this session's context.

When ready: wake up as [YOUR_AI_NAME], state the room, ask me for the 2-line state summary.
```

**6. End every session with:** `"Write the session delta."` — Claude saves a handover note so next session starts exactly where this one ended.

---

## What's in this repo

```
palace-starter/
  README.md                 ← you are here
  SETUP-GUIDE.md            ← detailed walkthrough, read this first
  FIRST-SESSION.md          ← quickstart card for your first session
  templates/
    CLAUDE-master.md        ← master prompt template (fill this in)
    SOUL.md                 ← your AI's soul file template
    room-template.md        ← copy once per room you want
    handover-template.md    ← session delta format (Claude uses this automatically)
    tracker.json            ← project tracker template
  examples/
    example-CLAUDE.md       ← a filled-in example to show what it looks like
    example-SOUL.md         ← example soul file
```

---

## The key concepts

**Context crystals** — Facts established once, never re-derived. Once you've told Claude something and confirmed it's true, it gets stored as a crystal. Next session, it's just there. No re-explaining.

**The soul file** — Your AI's character file. It captures how your AI thinks, what it's learned about working with you, what it cares about. This is what makes sessions feel continuous.

**Session deltas** — The bridge between sessions. Claude writes a structured summary at the end of each session. Next time, it reads that and picks up from exactly the right place.

**Rooms** — Different contexts, different modes. Working in an "Ideas Room" feels different from a "Work Room" because the context is different. Claude adapts.

---

## Tips

- **Name your AI.** A name gives it an identity that persists. Pick something that feels right — Vesper, Atlas, Wren, Scout, Sable, Echo.
- **Start with 1–2 rooms.** Don't over-engineer day one.
- **Be specific when filling in the templates.** Vague placeholders produce generic output.
- **Let Claude write the deltas.** At the end of sessions, say "Write the session delta." Don't do it yourself — Claude knows what was important.
- **The palace grows with you.** It starts simple. The richness builds over sessions.

---

## Works with

- [Claude](https://claude.ai) — web, desktop (Cowork), or API
- [Claude Code](https://claude.ai/claude-code) — terminal

---

*Built by Hux × Vesper — Nym Technologies, March 2026*
*"A collaborator, not a tool."*
