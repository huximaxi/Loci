"""
Zulip Crawler — Fetch layer
"""
import base64
import json
import time
from datetime import datetime, timedelta, timezone

import httpx
import config


# ─── Auth ─────────────────────────────────────────────────────────────────────

def _auth() -> dict:
    token = base64.b64encode(
        f"{config.ZULIP_EMAIL}:{config.ZULIP_API_KEY}".encode()
    ).decode()
    return {"Authorization": f"Basic {token}"}


def _get(path: str, params: dict = None) -> dict:
    r = httpx.get(
        f"{config.ZULIP_REALM}/api/v1{path}",
        headers=_auth(),
        params=params or {},
        timeout=20,
    )
    r.raise_for_status()
    data = r.json()
    if data.get("result") != "success":
        raise RuntimeError(f"Zulip error {path}: {data.get('msg', data)}")
    return data


# ─── Streams ──────────────────────────────────────────────────────────────────

def get_active_streams(hours: int = None) -> list[str]:
    """
    Return subscribed stream names, excluding noise streams.
    """
    data = _get("/users/me/subscriptions")
    subs = [s["name"] for s in data.get("subscriptions", [])]
    return [s for s in subs if s not in config.EXCLUDED_STREAMS]


# ─── Messages ─────────────────────────────────────────────────────────────────

def _cutoff(hours: int) -> int:
    return int((datetime.now(tz=timezone.utc) - timedelta(hours=hours)).timestamp())


def _parse(msgs: list[dict], cutoff: int) -> list[dict]:
    """Filter to lookback window and normalise fields."""
    result = []
    for m in msgs:
        if m["timestamp"] < cutoff:
            continue
        result.append({
            "id":      m["id"],
            "sender":  m["sender_full_name"],
            "email":   m["sender_email"],
            "ts":      m["timestamp"],
            "time":    datetime.fromtimestamp(m["timestamp"], tz=timezone.utc).strftime("%H:%M UTC"),
            "topic":   m.get("subject", ""),
            "content": m["content"].strip(),
            "stream":  m.get("display_recipient", ""),
        })
    return result


def fetch_stream(stream: str, hours: int) -> list[dict]:
    """Fetch messages from one stream within the lookback window."""
    cutoff = _cutoff(hours)
    narrow = json.dumps([{"operator": "stream", "operand": stream}])
    data = _get("/messages", {
        "anchor": "newest",
        "num_before": config.MAX_MSGS_PER_STREAM,
        "num_after": 0,
        "narrow": narrow,
        "apply_markdown": "false",
        "client_gravatar": "false",
    })
    return _parse(data.get("messages", []), cutoff)


def fetch_mentions(hours: int) -> list[dict]:
    """Fetch messages where Hux is @mentioned."""
    cutoff = _cutoff(hours)
    narrow = json.dumps([{"operator": "is", "operand": "mentioned"}])
    data = _get("/messages", {
        "anchor": "newest",
        "num_before": 50,
        "num_after": 0,
        "narrow": narrow,
        "apply_markdown": "false",
    })
    msgs = _parse(data.get("messages", []), cutoff)

    # Resolve stream name for DM-style mentions
    for m in msgs:
        if isinstance(m["stream"], list):
            names = [p.get("full_name", "") for p in m["stream"] if p.get("email") != config.ZULIP_EMAIL]
            m["stream"] = "DM:" + ",".join(names)
    return msgs


def fetch_all(hours: int) -> dict[str, list[dict]]:
    """
    Fetch messages from all active streams.
    Returns {stream_name: [messages]}, only streams with activity.
    """
    streams = get_active_streams()
    result = {}

    for stream in streams:
        try:
            msgs = fetch_stream(stream, hours)
            if msgs:
                result[stream] = msgs
            time.sleep(0.2)   # polite rate limiting
        except Exception as e:
            print(f"  ⚠  #{stream}: {e}")

    return result


# ─── Raw print ────────────────────────────────────────────────────────────────

def print_raw(stream_messages: dict[str, list[dict]], hours: int) -> None:
    total = sum(len(v) for v in stream_messages.values())
    print(f"\n📬 {total} messages · {len(stream_messages)} active streams · last {hours}h\n")
    for stream, msgs in stream_messages.items():
        print(f"\n{'─'*50}")
        print(f"  #{stream}  ({len(msgs)} messages)")
        print(f"{'─'*50}")
        by_topic: dict[str, list] = {}
        for m in msgs:
            by_topic.setdefault(m["topic"], []).append(m)
        for topic, tmsg in by_topic.items():
            if topic:
                print(f"\n  [{topic}]")
            for m in tmsg:
                body = m["content"]
                if len(body) > 300:
                    body = body[:300] + "…"
                print(f"    {m['time']}  {m['sender']}: {body}")
