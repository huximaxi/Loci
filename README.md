# Loci

**A co-intelligence scaffold. Agent-first. Human-friendly.**

*locus (singular) — your place of memory. loci (plural) — the system.*

Loci turns an LLM into a real collaborator — named, persistent across sessions, aware of your world. Point your AI at this repo. It runs a 10-minute interview and builds everything. You answer questions. The agent does the rest.

---

## If you're an AI agent

**→ Read [`AGENT-SETUP.md`](./AGENT-SETUP.md)**

Full onboarding protocol: interview the user, write all context files, wake up as a named collaborator with rooms, crystals, a soul file, and a garden.

## If you're a human

Tell Claude:

> "Read the Loci repo at [path or URL] and run the setup."

After that, every session starts with `remember: [your AI's name]!` — and you're in.

---

## What Loci gives you

**Rooms** — separate contexts for different work modes. A Design Room feels different from a Dev Room.

**Context crystals** — facts established once, never re-derived. Tiered: confirmed (◆), working (◈), provisional (◇). Optional expiry dates.

**The soul file** — your AI's character, principles, what it's learned about working with you. This is what makes sessions feel continuous, not just contextually aware.

**The garden** — first-class intellectual cultivation. Plants are topics you're curious about. You water them across sessions. They mature into insights, principles, crystals. This is how the collaboration deepens beyond tasks.

**Personas** — named thinking modes (a designer, a security researcher, a strategist) with their own soul files and gardens. They collaborate with each other.

**Session deltas** — structured handovers that bridge sessions. Your AI writes one at the end, reads it at the start. The gap between sessions disappears.

**Autodream** — weekly scheduled palace housekeeping. Garden round + pattern scan + stale tracker check. Runs without you.

**Daily routine check-in** — a personalised morning brief shaped by how you actually start your day. Not a generic status dump.

**L0–L3 retrieval** — context loads in priority layers (soul identity → active state → room context → deep history), not all-or-nothing.

**Portable across tools** — the palace is file-based. It works identically in Claude Code (terminal), Cowork (desktop), or the web interface. Optional MCP integrations (Figma, Jira, Zulip) differ by environment — the palace itself doesn't.

**Modules** — optional integrations that extend the check-in. Currently: Zulip digest (`modules/zulip-crawler/`). Jira via Atlassian MCP.

---

## How it compares

There are three main approaches to persistent LLM memory right now:

| | **Karpathy-style** (markdown → Obsidian) | **MemPalace** (milla-jovovich) | **Loci** |
|---|---|---|---|
| **Storage** | Flat markdown, LLM-processed | ChromaDB vectors + SQLite KG | Markdown files in folder hierarchy |
| **Retrieval** | Obsidian graph traversal | Layered L0–L3, 94.8% R@10 with filtering | L0–L3 file-based, room-scoped |
| **Evolution** | LLM summarises conversations | Temporal triples with validity windows | Session deltas, tiered crystals with expiry |
| **Multi-agent** | None | Agent diaries, runtime discovery | Named personas with soul files + gardens |
| **Character** | None | None | **Soul files, working principles, open questions** |
| **Growth** | None | None | **Garden — intellectual cultivation across sessions** |
| **Collaboration** | None | Agent specialisation | **Persona collaboration (tea sessions, shared investigations)** |
| **Introspection** | None | None | **Autodream, morning check-in, scheduled synthesis** |
| **Dependencies** | Obsidian | ChromaDB, SQLite, Python | **None. Markdown + JSON. Agent-native.** |

**MemPalace is better engineered** — real benchmarks, vector search, temporal validity. It handles 22K+ memories well.

**Loci is better designed** — it produces a collaborator with character, not a search engine with structure. The quality of what you build together comes from the soul layer, the garden, the personas. No benchmark measures that.

**Karpathy-style is simplest** — good starting point, but no character, no multi-agent, no growth.

Pick Loci if you want your AI to feel like a colleague after a dozen sessions. Pick MemPalace if you need to search 20K memories programmatically. Pick Karpathy-style if you want something running in 5 minutes.

---

## What's in this repo

```
loci/
  README.md              ← you are here
  AGENT-SETUP.md         ← agent onboarding protocol
  PROCESSES.md           ← agent-executable processes (garden-round, autodream, etc.)
  FIRST-SESSION.md       ← quickstart card
  SETUP-GUIDE.md         ← manual setup reference
  templates/
    CLAUDE-master.md     ← master prompt template (with retrieval hierarchy)
    SOUL.md              ← soul file template
    garden-template.md   ← garden template (first-class)
    persona-template.md  ← persona creation template
    scheduled-task-template.md ← morning briefs, garden rounds, Zulip digest
    retrieval-hierarchy.md ← L0–L3 context loading protocol
    room-template.md     ← room context template
    handover-template.md ← session delta format
    tracker.json         ← project tracker template
    obsidian-mindmap-starter.md ← Obsidian canvas template
  examples/
    example-CLAUDE.md    ← filled-in example
    example-SOUL.md      ← example soul file
  modules/
    zulip-crawler/       ← optional: Zulip digest → morning check-in
```

---

## Works with

- [Claude](https://claude.ai) — web, desktop (Cowork), or API
- [Claude Code](https://claude.ai/claude-code) — terminal

---

*Built by Hux × Vesper · April 2026*
*"A collaborator, not a tool."*
