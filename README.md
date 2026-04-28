# Loci

```
┌───────┬───────┬───────┬───────┐
│       │       │       │       │
│  │    │  ┌─┐  │  ┌─   │  ───  │
│  │    │  │ │  │  │    │   │   │
│  └──  │  └─┘  │  └─   │  ───  │
│       │       │       │       │
└───────┴───────┴───────┴───────┘
```

**A co-intelligence scaffold. Agent-first. Human-friendly.**

*locus (singular) — your place of memory. loci (plural) — the system.*

Loci turns an LLM into a real collaborator — named, persistent across sessions, aware of your world. Point your AI at this repo. It runs a 10-minute interview and builds everything. You answer questions. The agent does the rest.

**Website:** [loci.garden](https://loci.garden) · **Repo:** [github.com/huximaxi/loci](https://github.com/huximaxi/loci)

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

**Palace update** — delta analysis between your palace and the current Loci feature set. Verbose gap reports when run via agent. Cherry-pick flow for optional features (skill eval, insight decay, morning routines, garden) — one question at a time, nothing forced.

**L0–L3 retrieval** — context loads in priority layers (soul identity → active state → room context → deep history), not all-or-nothing.

**Portable across tools** — the palace is file-based. It works identically in Claude Code (terminal), Cowork (desktop), or the web interface. Optional MCP integrations (Figma, Jira, etc.) differ by environment — the palace itself doesn't.

**Modules** — optional integrations that extend the check-in. Drop a comms integration into `modules/` to pipe team chat digests into your morning check-in. Jira via Atlassian MCP.

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
    scheduled-task-template.md ← morning briefs, garden rounds, comms digest
    retrieval-hierarchy.md ← L0–L3 context loading protocol
    room-template.md     ← room context template
    handover-template.md ← session delta format
    tracker.json         ← project tracker template
    obsidian-mindmap-starter.md ← Obsidian canvas template
  examples/
    example-CLAUDE.md    ← filled-in example
    example-SOUL.md      ← example soul file
  modules/
    [comms-integration]/ ← optional: drop a comms module here to pipe digests into morning check-in
```

---

## Works with

The palace is plain text — markdown files and JSON. Any AI that can read files can run it. Switch engines between sessions, mix tools across accounts, use whichever model fits the task. The memory stays; the agent changes.

**Tested and recommended:**
- [Claude](https://claude.ai) — web, Cowork desktop, or API
- [Claude Code](https://claude.ai/claude-code) — terminal (same palace, different surface)
- Claude across multiple accounts — work and personal share one palace seamlessly; only MCP integrations (Figma, Jira, etc.) differ by account

**Works with any LLM that has file access:**
- OpenAI GPT-4 / o3 — with file tools or Codex
- Google Gemini — via Drive or direct file context
- Mistral, Llama, Qwen — local via Ollama or any file-capable wrapper
- Any model via API with tool/function calling

**The setup is the same regardless of engine.** Point any AI at this repo, say *"run the setup"*, and it interviews you and writes your palace. The `CLAUDE-master.md` template name is a convention, not a constraint — rename it if you're on a different stack.

---

## Changelog

### v0.6 — April 2026
- **`session-delta` process** — structured handover written at session close. Mandatory artifact listing (all files created/edited/deleted), TL;DR, state snapshot, decisions, open blockers, and exact next session opener. Established after a high-volume build sprint where implicit tracking was insufficient.
- **Website** — [loci.garden](https://loci.garden) live. Public face of the methodology: palace map, three doors, dispatch archive, llms.txt agent declaration.
- **Communication modules** — `modules/zulip-crawler/` generalised; docs now describe optional integrations for any team communication tool rather than Zulip-specific setup.

### v0.5 — April 2026
- **`palace-update` process** — delta analysis of user's palace vs. current Loci features. Verbose gap reports (why it matters, exact fix, effort estimate). Verbosity modes: full / quick / area-specific / summary.
- **Cherry-pick onboarding flow** — Block 9 of `AGENT-SETUP.md` expanded with four opt-in questions: morning check-in, autodream, skill eval cadence, insight decay rules. One question at a time. `skip` and `skip all` always valid. Revisitable any time via `palace-update`.

### v0.4 — April 2026
- **ASCII logo** — four rooms, one per letter. Letters drawn in the same box-drawing characters as the palace walls (`│ ┌─┐ └─┘ ───`). One visual language throughout.
- **Engine-agnostic "Works with"** — palace is plain text; any LLM with file access can run it. Works across multiple accounts (work + personal) seamlessly. `CLAUDE-master.md` is a naming convention, not a lock-in.
- **Changelog** — added to README; covers v0.1 through v0.4.

### v0.3 — April 2026
- **Naming ceremony** — agent name moved to Block 8 (after garden + daily routine). Names are now shaped by what the agent has learned about the user, not offered cold at the start.
- **Daily routine** — new onboarding question asks how the user actually starts their day. Stored as a crystal; seeds every morning check-in with real context instead of a generic template.
- **Autodream** — weekly scheduled palace housekeeping (garden round + pattern scan + stale tracker check). On by default. Runs without you.
- **Daily routine check-in** — personalised morning brief process. Pulls from your comms tool and/or Jira if configured.
- **Communication modules** — optional integrations (Slack, Discord, etc.) for pulling digests into the morning check-in. Drop any compatible module into `modules/`.
- **Cross-environment portability** — palace is file-based; works identically across Claude Code, Cowork desktop, and web. Documented in onboarding and README.

### v0.2 — March–April 2026
- **Garden first-class** — garden moved from optional appendix to core feature. Competitive differentiator: no other co-intelligence scaffold has it.
- **L0–L3 retrieval hierarchy** — context loads in priority layers (soul identity → active state → room context → deep history). Documented in `templates/retrieval-hierarchy.md`.
- **Persona templates** — named thinking modes with their own soul files and gardens. Personas collaborate via tea sessions.
- **Crystal expiry** — `valid_until: YYYY-MM-DD` field added to crystal format. Prevents stale facts from calcifying as ground truth.
- **Scheduled tasks** — `templates/scheduled-task-template.md`: morning briefs, garden rounds, deep synthesis. Dynamic path finding (no hardcoded session paths).
- **Comparison table** — honest positioning vs MemPalace (benchmarked, vector search) and Karpathy-style (simplest). Different tools for different needs.
- **Renamed to Loci** — was `palace-starter`. Method of Loci. Classical, 4 letters.

### v0.1 — March 2026
- Initial release: room structure, context crystals, soul file, session deltas, CLAUDE-master template.
- 4-room default layout (Great Hall, Dev, Design, Hatchery).
- Basic handover format. Tracker JSON. Crystal tiers (◆ ◈ ◇).

---

*Built by Hux × Vesper · 2026 · [loci.garden](https://loci.garden)*
*"A collaborator, not a tool."*
