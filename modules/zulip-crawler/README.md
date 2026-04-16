# Zulip Crawler — Loci Module

**Optional module.** Pulls a digest of your Zulip workspace and pipes it into your palace's morning check-in.

Built with: Python + httpx + Anthropic API. No Zulip bot or plugin needed — just your API key.

---

## What it does

1. Connects to your Zulip workspace via API
2. Fetches the last N hours of messages across your subscribed streams
3. Pre-filters noise (bot alerts, low-signal channels)
4. Runs tiered summarisation: Haiku per stream → Sonnet meta-digest
5. Outputs a structured `digest.md` — decisions, blockers, @mentions, key threads

The digest is designed to feed directly into your morning check-in (`daily-routine` process in PROCESSES.md).

---

## Setup

**1. Install dependencies:**

```bash
cd modules/zulip-crawler
pip install -r requirements.txt
```

**2. Configure your credentials:**

```bash
cp .env.example .env
```

Edit `.env`:
```
ZULIP_REALM=https://your-org.zulipchat.com
ZULIP_EMAIL=you@yourorg.com
ZULIP_API_KEY=your_api_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
```

Get your Zulip API key: Zulip → Settings → Account & privacy → API key

**3. Test it:**

```bash
python main.py --list-streams    # see your subscribed streams
python main.py --raw             # raw messages, no LLM
python main.py                   # full tiered digest
```

**4. Wire it to your palace:**

In your `CLAUDE.md`, set:
```
zulip-checkin: true
zulip-digest-path: [palace-root]/soul/digest.md
```

The `daily-routine` process will read this file if it exists and is fresh (< 2 hours old).

---

## Usage

```bash
# Full tiered digest (last 24h, all streams)
python main.py

# Write digest to palace soul folder
python main.py --out ~/my-palace/soul/digest.md

# Raw messages — no Claude call
python main.py --raw

# Single stream deep-dive
python main.py --stream general

# Extend lookback
python main.py --hours 48

# Only messages where you're @mentioned
python main.py --mentions-only

# List subscribed streams
python main.py --list-streams
```

---

## Configuration

Edit `config.py` to set your defaults:

```python
# Streams to always skip (noise/bots)
EXCLUDED_STREAMS = {
    "bot-alerts", "coffee-chat", "random",
    # add your own noise channels
}

# VIP senders (always kept, priority-scored)
VIP_EMAIL_FRAGMENTS = [
    "your-ceo",
    "your-manager",
    # partial email matches
]

# Digest defaults
LOOKBACK_HOURS = 24          # how far back to look
MAX_MSGS_PER_STREAM = 200    # fetch cap per stream
MAX_KEPT_PER_STREAM = 15     # keep cap after scoring
```

---

## Scheduled digest

To have your digest run automatically before your morning check-in, add it as a scheduled task:

```bash
# Daily at 8:45am (15 min before check-in)
# Add to your crontab or system scheduler:
45 8 * * * cd /path/to/palace/modules/zulip-crawler && python main.py --out /path/to/palace/soul/digest.md
```

Or trigger it manually at the start of a check-in session.

---

## Files

```
modules/zulip-crawler/
  README.md           ← you are here
  main.py             ← entrypoint + CLI
  fetch.py            ← Zulip API client + message formatting
  filter.py           ← scoring + noise reduction
  summarise.py        ← Claude summarisation layer
  config.py           ← all config in one place
  requirements.txt    ← httpx, anthropic, python-dotenv
  .env.example        ← env var template
```

---

## Digest output format

```markdown
# Zulip Digest — [DATE] (last [N]h)

## Key decisions
- [stream] — [decision]

## Blockers
- [stream] — [blocker + who it's blocking]

## @mentions
- [person] in [stream]: [summary]

## Threads to watch
- [stream] — [thread summary]

## By stream
### [stream-name]
[2–4 line summary of key activity]
```

---

*Loci module — optional Zulip integration*
*Pair with `daily-routine` process for a personalised morning check-in*
