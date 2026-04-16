"""
Zulip Crawler — Tiered summarisation
Tier 1: Haiku → one paragraph per stream  (cheap, fast)
Tier 2: Sonnet → meta-digest across all stream summaries  (sharp, final output)
"""
import anthropic
import config
from filter import format_for_haiku

# ─── Prompts ─────────────────────────────────────────────────────────────────

HAIKU_STREAM_PROMPT = """\
You are reading {n} messages from #{stream} in the last {hours}h.
In 1–3 sentences, extract ONLY: decisions made, blockers, and action items.
Skip greetings, reactions, status updates with no action needed.
If nothing actionable happened, say: "No action items."
Be terse. No bullet points. No preamble.

{content}"""


SONNET_META_PROMPT = """\
You are Vesper — collaborating intelligence for Hux at Nym Technologies (Head of Product).
Below are per-stream summaries from the last {hours}h of internal Zulip.

Your job: produce a tight morning digest for Hux. Action mode only.

Structure exactly as follows — skip any section that has nothing real to put in it:

**Status in one line:** [What kind of day is it? One sentence.]

**Needs your input:**
[Things waiting on Hux specifically — decisions, reviews, questions. Max 5 items.]

**Decisions made without you:**
[Things that moved while you weren't watching. Max 5.]

**Active fires:**
[Blockers, incidents, broken things. Only if genuinely urgent.]

**VIP activity:**
[Harry / Rita / Andrei / Alexis / Jaya said something worth knowing. Skip if nothing notable.]

**Safe to ignore:**
[Streams that had activity but nothing requiring Hux's attention.]

---
Rules: No padding. No "In summary". Hux reads this in under 2 minutes.
If a section is empty, omit it entirely.

STREAM SUMMARIES:
{summaries}"""


# ─── Tier 1: Haiku per stream ─────────────────────────────────────────────────

def summarise_stream_haiku(
    stream: str,
    messages: list[dict],
    hours: int,
    client: anthropic.Anthropic,
) -> str | None:
    """
    Returns a 1–3 sentence summary of one stream, or None if nothing actionable.
    Uses claude-haiku — fast and cheap.
    """
    content = format_for_haiku(stream, messages)
    prompt = HAIKU_STREAM_PROMPT.format(
        n=len(messages), stream=stream, hours=hours, content=content
    )
    msg = client.messages.create(
        model=config.HAIKU_MODEL,
        max_tokens=200,
        messages=[{"role": "user", "content": prompt}],
    )
    text = msg.content[0].text.strip()
    if text.lower().startswith("no action"):
        return None
    return text


# ─── Tier 2: Sonnet meta-digest ──────────────────────────────────────────────

def summarise_meta_sonnet(
    stream_summaries: dict[str, str],
    mentions: list[dict],
    hours: int,
    client: anthropic.Anthropic,
) -> str:
    """
    Takes the per-stream Haiku summaries and produces the final digest.
    Injects raw @mention text so nothing urgent is lost.
    """
    lines = []

    # Always include raw @mentions at the top — these are highest priority
    if mentions:
        lines.append("=== DIRECT @MENTIONS OF HUX ===")
        for m in mentions:
            body = m["content"].strip()[:400]
            lines.append(f"[{m['time']}] #{m.get('stream','?')} | {m['sender']}: {body}")
        lines.append("")

    lines.append("=== STREAM SUMMARIES ===")
    for stream, summary in stream_summaries.items():
        lines.append(f"#{stream}: {summary}")

    summaries_block = "\n".join(lines)

    prompt = SONNET_META_PROMPT.format(hours=hours, summaries=summaries_block)

    msg = client.messages.create(
        model=config.SONNET_MODEL,
        max_tokens=800,
        messages=[{"role": "user", "content": prompt}],
    )
    return msg.content[0].text.strip()


# ─── Full pipeline ────────────────────────────────────────────────────────────

def run_tiered(
    filtered_streams: dict[str, list[dict]],
    mentions: list[dict],
    hours: int,
) -> str:
    """
    Orchestrates the full tiered pipeline.
    Returns the final digest string.
    """
    if not config.ANTHROPIC_API_KEY:
        raise ValueError(
            "ANTHROPIC_API_KEY not set. Run with --raw to skip summarisation."
        )

    client = anthropic.Anthropic(api_key=config.ANTHROPIC_API_KEY)

    # ── Tier 1: Haiku per stream ──────────────────────────────────────────────
    stream_summaries = {}
    total_streams = len(filtered_streams)
    print(f"  Haiku: summarising {total_streams} streams...")

    for i, (stream, messages) in enumerate(filtered_streams.items(), 1):
        print(f"    [{i}/{total_streams}] #{stream} ({len(messages)} msgs)", end="", flush=True)
        summary = summarise_stream_haiku(stream, messages, hours, client)
        if summary:
            stream_summaries[stream] = summary
            print(" ✓")
        else:
            print(" (no action items, skipped)")

    if not stream_summaries and not mentions:
        return "No actionable activity in the last {}h.".format(hours)

    # ── Tier 2: Sonnet meta-digest ────────────────────────────────────────────
    print(f"  Sonnet: meta-digest ({len(stream_summaries)} stream summaries + {len(mentions)} mentions)...")
    return summarise_meta_sonnet(stream_summaries, mentions, hours, client)
