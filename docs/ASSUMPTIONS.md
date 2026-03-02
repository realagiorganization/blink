# Assumptions

- The available reference images in `/out/_media/` are repository UI screenshots rather than paywall mocks, so the paywall in `Blink/Subscriptions/Intro.swift` keeps Blink's existing dark/teal styling while presenting the "TRY IT FREE FOR 14 DAYS" CTA and entitlement highlights.
- The `scripts/screenshot_pages.js` workflow defaults to `https://realagiorganization.github.io/blink/`; set the `PAGES_URL` secret to point the Pages screenshot action at a different site.
- The "opencode" CLI lives at `scripts/opencode_cli.py`, uses an OpenAI-compatible HTTP API, and relies on encrypted GitHub Actions secrets (`LLM_API_KEY` with optional `LLM_API_URL`/`LLM_MODEL`), including when invoked inside the tmux/VHS recording for the BDD run.
