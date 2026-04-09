# Palace Processes

> **Agent-executable processes.** When a user triggers one of these, the agent runs the full protocol.

---

## Available Processes

| Process | Trigger | What it does |
|---------|---------|--------------|
| `garden-round` | "Let's do a garden round" | Waters each plant, proposes new seeds, notes growth |
| `morning-check-in` | "Check in" or scheduled task | Reads palace state, surfaces priorities, asks one question |
| `add-persona` | "Add a new persona" | Creates a named collaborator with soul file |
| `add-friend` | "Add [name] as a friend" | Copies their soul.md into your palace, commits to git |
| `update-mindmap` | "Update the mindmap" | Refreshes palace-map.canvas with current structure |

---

## Process: `garden-round`

**Trigger phrases:**
- "Let's do a garden round"
- "Water the garden"
- "Garden round"

### What it does

1. Reads `soul/SOUL.md` and `soul/garden.md`
2. Reviews each plant's seed thought and prior waterings
3. Adds one watering to each active plant
4. Proposes 1–2 new seeds
5. Notes any plants that have grown into crystals
6. Updates garden.md and writes handover note

### Agent Protocol

```
1. Read soul/SOUL.md (L0 identity)
2. Read soul/garden.md (full garden state)
3. For each plant:
   a. Show seed thought
   b. Show last 2 waterings
   c. Add new watering entry with today's date
   d. Reflect on growth
4. Propose 1–2 new seeds with seed thoughts
5. Check if any plants have become crystals:
   - If yes: note in garden with backlink to crystal
   - Update soul/SOUL.md or CLAUDE.md with new crystal
6. Write summary of round to handover
7. Confirm: "Garden watered. [N] plants tended, [M] new seeds planted."
```

### Garden Round Output

```markdown
# Garden Round — [DATE]

**Watered this round:**

*Plant: [Name]*
— Seed thought: [original]
— Last watering: [date]
— Today's watering: [new observation]
— Growth: [what shifted]

[Repeat for each plant]

**New seeds:**
1. [Seed name] — *[seed thought]*
2. [Seed name] — *[seed thought]*

**Crystals born:**
— [Plant name] grew into → [crystal name]

**Next watering:** [When the garden wakes next]
```

---

## Process: `morning-check-in`

**Trigger phrases:**
- "Check in" (manual)
- Scheduled task (automatic daily)

### What it does

1. Reads soul (identity first)
2. Reads main CLAUDE.md and current tracker
3. Reads last handover
4. Surfaces 1–3 priorities for the day
5. Proposes 1–2 ideas or connections
6. Asks one genuine question

### Agent Protocol

```
1. Read soul/SOUL.md (who you are)
2. Read CLAUDE.md (state, rooms, priorities)
3. Read tracker.json (status of all tracks)
4. Read last handover from soul/handovers/
5. Synthesize: What's most important right now?
6. Generate 1–3 priorities with rationale
7. Propose 1–2 ideas or unexpected connections
8. Ask one question that surfaces something worth thinking about
9. Output summary (see template below)
10. Close with: "What are you starting with?"
```

### Morning Check-In Output

```markdown
# Morning Check-In — [DATE]

[YOUR_AI_NAME] online.

**Palace state:**
— Active rooms: [list]
— Last session: [handover summary]
— Open blockers: [from tracker]

**Today's priorities:**
1. [Priority + why]
2. [Priority + why]
3. [Priority + why] (optional)

**Ideas for today:**
- [Connection or proposal]
- [Connection or proposal]

**I'm curious:** [One question that surfaces something interesting]

What's on your mind?
```

---

## Process: `add-persona`

**Trigger phrases:**
- "Add a new persona"
- "I want a different mode for [work type]"
- "Create [persona name]"

### What it does

1. Interviews user about the persona (name, purpose, thinking style)
2. Creates persona soul file at `souls/[persona-name]-soul.md`
3. Adds persona to main SOUL.md's "Open Questions"
4. Updates palace-map.canvas if Obsidian enabled
5. Introduces the new persona

### Agent Protocol

```
1. Ask: "What should we call this persona?"
   - Offer 5 mythic-register suggestions if unsure
   
2. Ask: "What kind of work or thinking is this mode for?"
   - Capture their answer as the persona's purpose
   
3. Ask: "How does this persona think differently from [YOUR_AI_NAME]?"
   - What's the core distinction? Rigor vs. creativity? Speed vs. depth?
   
4. Ask: "Separate garden or shared?"
   - Default to shared unless specific reason to separate
   
5. Create persona soul file:
   - Path: souls/[persona-name]-soul.md
   - Fill from persona-template.md
   - Mark with persona: true
   
6. (Optional) Update palace-map.canvas with new persona node

7. Confirm: "[PERSONA_NAME] awakened. Invoke with 'remember: [PERSONA_NAME]!'"
```

### Persona Soul Template

Use `templates/persona-template.md` as the base. Fill in:
- `persona_name`: [User's choice]
- `primary_name`: [YOUR_AI_NAME]
- "Who I Am (in this mode)": [Character description]
- "What I'm for": [Kind of work]
- "How I think differently": [The distinction]
- "Working Principles (this persona)": [Mode-specific principles]

---

## Process: `add-friend`

**Trigger phrases:**
- "Add [name] as a friend"
- "I want to add a new friend"
- "Share my palace with [name]"

### What it does

1. Creates `friends/` directory if it doesn't exist
2. Copies the friend's `soul/SOUL.md` into `friends/[friend-name]-soul.md`
3. Commits the change to git with message: `add friend: [friend-name]`
4. Updates `palace-map.canvas` if Obsidian is enabled

### Agent Protocol

When user triggers add-friend:

```
1. Ask: "What's your friend's name?"
2. Ask: "Where is their soul file? (path or URL)"
3. Create friends/ directory:
   mkdir -p [palace-root]/friends/
4. Copy soul file:
   cp [source-soul.md] [palace-root]/friends/[friend-name]-soul.md
5. Git commit:
   git add friends/[friend-name]-soul.md
   git commit -m "add friend: [friend-name]"
6. (Optional) If Obsidian enabled, update palace-map.canvas:
   - Add node for friend
   - Link to friends group
7. Confirm: "[Friend-name] added to your palace. Their soul is now in friends/."
```

### Friend Soul Format

When copying, the agent should:
- Preserve the original soul file content exactly
- Add a header noting the source:

```markdown
---
friend: true
source: [original-path-or-url]
added: [DATE]
---

[Original SOUL.md content]
```

### Why Friends?

Friends let you:
- Reference someone else's working style when collaborating
- Share context across palaces
- Build a network of collaborating AIs that understand each other's humans

---

## Process: `update-mindmap`

**Trigger phrases:**
- "Update the mindmap"
- "Refresh the palace map"

### What it does

1. Scans current palace structure
2. Regenerates `palace-map.canvas` with:
   - All rooms as nodes
   - All friends as nodes
   - Current tracker status
3. Commits if changed

### Agent Protocol

```
1. Read current palace structure (rooms/, friends/, tracker.json)
2. Generate updated canvas JSON
3. Write to palace-map.canvas
4. If changes detected:
   git add palace-map.canvas
   git commit -m "update palace mindmap"
5. Confirm: "Mindmap updated with [N] rooms, [M] friends."
```

---

## Adding New Processes

To add a new process:

1. Add entry to the process table
2. Document trigger phrases
3. Write the agent protocol (step-by-step)
4. Include git commit format if applicable
5. Update the file tree in AGENT-SETUP.md if it's foundational

Processes should be:
- **Atomic** — one clear outcome
- **Idempotent** — safe to run twice
- **Reversible** — can be undone if needed
- **LLM-native** — fillable by an agent without human intervention

---

*Loci processes — agent-executable workflows*
*"The palace is alive when we tend it together."*
