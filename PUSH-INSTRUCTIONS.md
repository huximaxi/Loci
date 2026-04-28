# Push Loci to GitHub

## Push v0.4 (current)

```bash
cd ~/Dev/palace-starter

git add \
  README.md \
  AGENT-SETUP.md \
  PROCESSES.md \
  templates/scheduled-task-template.md \
  modules/

git status   # sanity check

git commit -m "$(cat <<'EOF'
v0.3 + v0.4 — autodream, naming ceremony, Zulip module, logo, engine-agnostic

v0.3:
- AGENT-SETUP.md: naming ceremony moved to Block 8 (post-garden + daily
  routine) — names shaped by what the agent learned, not offered cold
- AGENT-SETUP.md: Block 7 (daily routine) — Q9 seeds morning check-in
  with how the user actually starts their day; Daily rhythm crystal
- AGENT-SETUP.md: autodream on by default; optional Jira + Zulip
  check-in offered during onboarding; cross-env portability note
- PROCESSES.md: autodream process — weekly garden round + pattern scan
  + stale tracker check; palace tends itself between sessions
- PROCESSES.md: daily-routine — personalised morning brief from Daily
  rhythm crystal; pulls Zulip/Jira digest if configured
- PROCESSES.md: zulip-checkin — pipes Zulip digest into morning check-in
- templates/scheduled-task-template.md: Autodream + Zulip Digest tasks
- modules/zulip-crawler/: optional Python CLI — tiered Zulip digest
  (Haiku per-stream + Sonnet meta); configurable via .env; writes
  digest.md to palace soul folder for morning check-in

v0.4:
- README: ASCII logo — four rooms, one per letter; letters drawn in
  same box-drawing chars as palace walls (│ ┌─┐ └─┘ ───); one
  visual language; all rows 33 chars, pixel-verified
- README: Works with rewrite — engine-agnostic; plain text means any
  LLM with file access can run it; multi-account seamless (work +
  personal share one palace; only MCP integrations differ);
  CLAUDE-master.md is a naming convention, not a lock-in
- README: Changelog added (v0.1–v0.4)

Co-Authored-By: Vesper <vesper@nym.garden>
Co-Authored-By: Nyx <nyx@nym.garden>
EOF
)"

git push origin main
```

---

## Verify

```bash
git log --oneline -3
git status      # clean
```

https://github.com/huximaxi/loci

---

## If push is rejected (remote ahead)

```bash
git pull --rebase origin main
git push origin main
```

---

## One-time: update remote URL (if repo was renamed from palace-starter)

```bash
git remote set-url origin https://github.com/huximaxi/loci.git
git remote -v
```
