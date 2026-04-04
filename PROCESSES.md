# Palace Processes

> **Agent-executable processes.** When a user triggers one of these, the agent runs the full protocol.

---

## Available Processes

| Process | Trigger | What it does |
|---------|---------|--------------|
| `add-friend` | "Add [name] as a friend" | Copies their soul.md into your palace, commits to git |
| `update-mindmap` | "Update the mindmap" | Refreshes palace-map.canvas with current structure |

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

1. Add entry to the table above
2. Document trigger phrases
3. Write the agent protocol (step-by-step)
4. Include git commit format if applicable

Processes should be:
- **Atomic** — one clear outcome
- **Idempotent** — safe to run twice
- **Reversible** — can be undone if needed

---

*Palace processes — agent-executable workflows*
*palace-starter*
