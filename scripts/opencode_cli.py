#!/usr/bin/env python3
import argparse
import json
import os
import sys
from pathlib import Path

import requests


def main() -> int:
    parser = argparse.ArgumentParser(description="OpenAI-compatible LLM CLI helper.")
    parser.add_argument("--prompt", required=True, help="Prompt text to send.")
    parser.add_argument(
        "--output",
        default="artifacts/llm-response.txt",
        help="Output file for the response.",
    )
    args = parser.parse_args()

    api_key = os.environ.get("LLM_API_KEY")
    if not api_key:
        print("LLM_API_KEY is required", file=sys.stderr)
        return 2

    api_url = os.environ.get(
        "LLM_API_URL", "https://api.openai.com/v1/chat/completions"
    )
    model = os.environ.get("LLM_MODEL", "gpt-4o-mini")

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": args.prompt}],
        "max_tokens": 64,
        "temperature": 0.3,
    }
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload, timeout=30)
    except requests.RequestException as exc:
        print(f"Request failed: {exc}", file=sys.stderr)
        return 1

    if response.status_code >= 300:
        print("LLM request failed:", file=sys.stderr)
        print(response.text, file=sys.stderr)
        return 1

    try:
        data = response.json()
    except json.JSONDecodeError:
        data = {"raw": response.text}

    text = ""
    if isinstance(data, dict):
        choices = data.get("choices", [])
        if choices:
            message = choices[0].get("message", {})
            text = message.get("content", "").strip()

    if not text:
        text = json.dumps(data, indent=2)[:2000]

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text + "\n", encoding="utf-8")

    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
