# Assumptions

- Paywall design reference images were not present in the attached artifacts, so the paywall refresh in `Blink/Subscriptions/Intro.swift` follows Blink's existing dark/teal palette and layout conventions while adding a card-based layout and stronger hierarchy.
- The requested "opencode" CLI is implemented as `scripts/opencode_cli.py` with an OpenAI-compatible HTTP API; it expects `LLM_API_KEY` and optional `LLM_API_URL`/`LLM_MODEL` secrets in GitHub Actions.
- The "GitHub Pages website" URL was not specified; no automated screenshot target was configured until a URL is provided.
