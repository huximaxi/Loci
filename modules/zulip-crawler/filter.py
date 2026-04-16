"""
Zulip Crawler — Pre-filter layer
Scores messages in Python before any LLM token is spent.
Goal: drop ~70-80% of messages, keep signal.
"""
import re
import config

# ─── Signal keywords (action mode) ───────────────────────────────────────────
SIGNAL_KEYWORDS = [
    # Decisions & outcomes
    "decided", "decision", "agreed", "confirmed", "approved", "rejected",
    "signed off", "go ahead", "green light", "blocking",
    # Action items
    "action", "please", "can you", "could you", "need you", "waiting on",
    "assigned", "take this", "own this", "follow up",
    # Priority / urgency
    "urgent", "asap", "critical", "priority", "deadline", "by eod",
    "by tomorrow", "this week", "time-sensitive",
    # Problems
    "broken", "down", "error", "fail", "issue", "incident", "bug",
    "regression", "blocked", "blocker", "stuck",
    # Shipping
    "ship", "deploy", "release", "merge", "pr", "review", "approve",
    "staging", "production", "rollback",
    # Questions needing input
    "what's the plan", "what do you think", "thoughts?", "lgtm?",
    "any concerns", "input needed", "open question",
]

# ─── Bot / noise patterns ─────────────────────────────────────────────────────
BOT_EMAIL_FRAGMENTS = [
    "bot@", "noreply@", "notifications@", "zabbix", "rewarder",
    "alerter", "alert@", "webhook", "github@", "gitlab@",
]

PURE_NOISE_PATTERNS = [
    r"^[\+\-]1$",                    # "+1", "-1"
    r"^(ok|okay|sure|noted|👍|✅|🙏|lol|haha|😂|🎉|thanks?!?)$",
    r"^@\*\*topic\*\*\s*$",         # bare @topic mention
    r"^\s*$",
]

# ─── Hux's own identifiers (to catch @mentions) ──────────────────────────────
HUX_IDENTIFIERS = [
    "daniel.nemet", "hꀎꊼ", "hux", "@**hꀎꊼ", "@**daniel",
]


def _is_bot(email: str) -> bool:
    e = email.lower()
    return any(frag in e for frag in BOT_EMAIL_FRAGMENTS)


def _is_noise(content: str) -> bool:
    c = content.strip()
    for pat in PURE_NOISE_PATTERNS:
        if re.match(pat, c, re.IGNORECASE):
            return True
    return len(c) < 8


def _is_vip(email: str) -> bool:
    e = email.lower()
    return any(frag in e for frag in config.VIP_EMAIL_FRAGMENTS)


def _mentions_hux(content: str) -> bool:
    c = content.lower()
    return any(ident in c for ident in HUX_IDENTIFIERS)


def _has_signal(content: str) -> bool:
    c = content.lower()
    return any(kw in c for kw in SIGNAL_KEYWORDS)


def score(msg: dict) -> int:
    """
    Score a single message 0–15. Returns -1 to hard-drop.
    """
    email   = msg.get("email", "").lower()
    content = msg.get("content", "")
    length  = len(content.strip())

    # Hard drops — never pay Claude to read these
    if _is_bot(email):
        return -1
    if _is_noise(content):
        return -1

    s = 0

    # VIP sender — almost always worth reading
    if _is_vip(email):
        s += 5

    # Direct mention of Hux — always relevant
    if _mentions_hux(content):
        s += 4

    # Contains actionable signal keywords
    if _has_signal(content):
        s += 3

    # Length bonus — longer = more likely substantive
    if length > 200:
        s += 2
    elif length > 80:
        s += 1

    return s


def filter_stream(messages: list[dict]) -> list[dict]:
    """
    Score and filter a list of messages from one stream.
    Returns top MAX_KEPT_PER_STREAM messages above MIN_SCORE, sorted by score desc.
    """
    scored = []
    for m in messages:
        s = score(m)
        if s >= config.MIN_SCORE:
            scored.append((s, m))

    # Sort by score descending, then by timestamp descending (newest first within same score)
    scored.sort(key=lambda x: (-x[0], -x[1]["ts"]))

    kept = [m for _, m in scored[: config.MAX_KEPT_PER_STREAM]]
    return kept


def filter_all(stream_messages: dict[str, list[dict]]) -> dict[str, list[dict]]:
    """
    Apply filter_stream to every stream. Drops empty streams after filtering.
    Returns filtered dict + stats.
    """
    result = {}
    total_in, total_out = 0, 0

    for stream, messages in stream_messages.items():
        total_in += len(messages)
        kept = filter_stream(messages)
        total_out += len(kept)
        if kept:
            result[stream] = kept

    reduction = 100 * (1 - total_out / total_in) if total_in else 0
    print(f"  Pre-filter: {total_in} → {total_out} messages "
          f"({reduction:.0f}% dropped, {len(result)} streams with signal)")

    return result


def format_for_haiku(stream: str, messages: list[dict]) -> str:
    """Compact plain-text format for the Haiku per-stream call."""
    lines = [f"Stream: #{stream}"]
    for m in messages:
        body = m["content"].strip()
        if len(body) > 300:
            body = body[:300] + "…"
        lines.append(f"[{m['time']}] {m['sender']}: {body}")
    return "\n".join(lines)
