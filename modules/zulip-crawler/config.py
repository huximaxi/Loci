"""
Zulip Crawler — Configuration
Loci module · configure via .env
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Always load .env from the crawler's own directory, regardless of cwd
load_dotenv(dotenv_path=Path(__file__).parent / ".env", override=True)

# ─── Zulip connection ─────────────────────────────────────────────────────────
ZULIP_REALM   = os.getenv("ZULIP_REALM",  "https://your-org.zulipchat.com")
ZULIP_EMAIL   = os.getenv("ZULIP_EMAIL",  "")
ZULIP_API_KEY = os.getenv("ZULIP_API_KEY", "")

# ─── Digest settings ──────────────────────────────────────────────────────────
LOOKBACK_HOURS       = int(os.getenv("LOOKBACK_HOURS", "24"))
MAX_MSGS_PER_STREAM  = int(os.getenv("MAX_MSGS_PER_STREAM", "200"))

# Streams to always skip — add your own noise/bot channels here
EXCLUDED_STREAMS = set(
    s.strip() for s in os.getenv("EXCLUDED_STREAMS", "").split(",") if s.strip()
) or {
    # defaults — replace with your own
    "bot-alerts",
    "random",
    "coffee-chat",
}

# ─── VIP senders (always kept, get priority scoring) ─────────────────────────
# Match by partial email — tolerant of exact address variation
# Set via comma-separated VIP_EMAILS env var, or edit the list below
VIP_EMAIL_FRAGMENTS = [
    s.strip() for s in os.getenv("VIP_EMAILS", "").split(",") if s.strip()
] or [
    # add partial email fragments for people whose messages you always want
    # e.g. "ceo", "lead", "manager"
]

# ─── Pre-filter thresholds ───────────────────────────────────────────────────
MIN_SCORE           = int(os.getenv("MIN_SCORE", "1"))  # drop messages below this
MAX_KEPT_PER_STREAM = int(os.getenv("MAX_KEPT_PER_STREAM", "15"))  # hard cap after scoring

# ─── Output ──────────────────────────────────────────────────────────────────
OUTPUT_FILE = os.getenv("OUTPUT_FILE", "")  # path to write digest.md; empty = stdout

# ─── Summarisation models ────────────────────────────────────────────────────
ANTHROPIC_API_KEY   = os.getenv("ANTHROPIC_API_KEY", "")
HAIKU_MODEL         = os.getenv("HAIKU_MODEL", "claude-haiku-4-5-20251001")  # per-stream: cheap + fast
SONNET_MODEL        = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-6")         # meta-digest
