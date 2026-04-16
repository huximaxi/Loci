#!/usr/bin/env python3
"""
Zulip Crawler — Hux × Vesper · Nym Technologies
Tiered digest: Python pre-filter → Haiku per-stream → Sonnet meta-digest

Usage:
  python main.py                         # full tiered digest
  python main.py --raw                   # raw messages, no LLM
  python main.py --raw --filtered        # raw messages after pre-filter (debug)
  python main.py --stream 2-nymvpn       # single stream deep-dive
  python main.py --hours 48              # extend lookback
  python main.py --list-streams          # show active streams
  python main.py --out digest.md         # write to file
  python main.py --mentions-only         # only messages where you're @mentioned
"""
import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

import config


def parse_args():
    p = argparse.ArgumentParser(description="Zulip digest — Hux × Vesper")
    p.add_argument("--raw",           action="store_true", help="No LLM — print messages")
    p.add_argument("--filtered",      action="store_true", help="With --raw: show post-filter messages")
    p.add_argument("--stream",        metavar="NAME",      help="Single stream only")
    p.add_argument("--hours",         type=int, default=config.LOOKBACK_HOURS)
    p.add_argument("--list-streams",  action="store_true", help="List active streams and exit")
    p.add_argument("--mentions-only", action="store_true", help="Only @mentions — fastest mode")
    p.add_argument("--out",           metavar="FILE",      help="Write digest to file")
    return p.parse_args()


def validate():
    if not config.ZULIP_API_KEY:
        print("❌  ZULIP_API_KEY not set. Add it to .env or environment.")
        sys.exit(1)


def write(text: str, path: str = None):
    if path:
        Path(path).write_text(text, encoding="utf-8")
        print(f"✅  Written to {Path(path).resolve()}")
    else:
        print(text)


def main():
    args = parse_args()
    validate()

    import fetch, filter as flt

    # ── List streams ──────────────────────────────────────────────────────────
    if args.list_streams:
        streams = fetch.get_active_streams()
        print(f"\n{len(streams)} active streams (excluding noise):\n")
        for s in sorted(streams):
            print(f"  #{s}")
        sys.exit(0)

    hours = args.hours
    now   = datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # ── Mentions-only mode ────────────────────────────────────────────────────
    if args.mentions_only:
        print(f"🔍  Fetching @mentions (last {hours}h)...")
        mentions = fetch.fetch_mentions(hours)
        print(f"   Found {len(mentions)} mentions\n")
        fetch.print_raw({"@mentions": mentions}, hours)
        sys.exit(0)

    # ── Fetch ─────────────────────────────────────────────────────────────────
    if args.stream:
        print(f"🔍  #{args.stream} — last {hours}h...")
        raw = fetch.fetch_stream(args.stream, hours)
        stream_messages = {args.stream: raw} if raw else {}
    else:
        print(f"🔍  Fetching all streams — last {hours}h...")
        stream_messages = fetch.fetch_all(hours)

    total_raw = sum(len(v) for v in stream_messages.values())
    print(f"   {total_raw} messages across {len(stream_messages)} active streams")

    # Also fetch @mentions (always included as priority signal)
    mentions = fetch.fetch_mentions(hours)
    print(f"   {len(mentions)} direct @mentions")

    # ── Raw mode (no filter, no LLM) ──────────────────────────────────────────
    if args.raw and not args.filtered:
        fetch.print_raw(stream_messages, hours)
        sys.exit(0)

    # ── Pre-filter ────────────────────────────────────────────────────────────
    print("\n⚡  Pre-filtering...")
    filtered = flt.filter_all(stream_messages)

    if args.raw and args.filtered:
        fetch.print_raw(filtered, hours)
        sys.exit(0)

    # ── Tiered summarisation ──────────────────────────────────────────────────
    if not config.ANTHROPIC_API_KEY:
        print("\n⚠   ANTHROPIC_API_KEY not set — showing filtered messages instead.\n")
        fetch.print_raw(filtered, hours)
        sys.exit(0)

    print("\n🤖  Summarising...")
    import summarise
    digest_body = summarise.run_tiered(filtered, mentions, hours)

    header = f"# Zulip Digest · last {hours}h · {now}\n\n"
    output = header + digest_body

    print()
    write(output, args.out or config.OUTPUT_FILE if hasattr(config, "OUTPUT_FILE") else args.out)


if __name__ == "__main__":
    main()
