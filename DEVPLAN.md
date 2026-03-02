# Development Plan

## Local setup
1. Install Xcode (matching the CI version) and command-line tools.
2. Clone with submodules and fetch resources:
   - `./get_frameworks.sh`
   - `./get_resources.sh`
3. Copy `template_setup.xcconfig` to `developer_setup.xcconfig` and set your Apple Developer team IDs.
4. Open `Blink.xcodeproj` in Xcode and build `Blink` or `BlinkTests`.

## Core development workflow
1. Make code changes in `Blink/`, `BlinkCode/`, `BlinkFiles/`, etc.
2. Run unit tests via Xcode or `xcodebuild` (see `.github/workflows/build.yml`).
3. For paywall or subscription changes, focus in `Blink/Subscriptions/` and verify CTAs, entitlements, and copy.
4. Update docs (README, BUILD.md) when workflows or dependencies change.

## BDD suite
1. BDD specs live in `bdd/features/` and are executed by `behave`.
2. Install deps: `python -m pip install -r bdd/requirements.txt`.
3. Run: `behave bdd/features`.
4. The LLM request scenario requires `LLM_API_KEY` and optionally `LLM_API_URL` + `LLM_MODEL`.

## CI/CD
1. CI tests run in `.github/workflows/build.yml` on macOS.
2. BDD tests + VHS recording run in `.github/workflows/bdd.yml` on Ubuntu.
3. TestFlight deployment uses fastlane in `.github/workflows/testflight.yml`.

## Release to TestFlight (fastlane)
1. Install Ruby + bundler and run `bundle install`.
2. Configure secrets:
   - `ASC_KEY_ID`, `ASC_ISSUER_ID`, `ASC_KEY_P8` (App Store Connect API key)
   - `APP_IDENTIFIER` (bundle id), `APPLE_ID`
   - Optional signing secrets if using match (e.g., `MATCH_PASSWORD`, `MATCH_GIT_URL`).
3. Run `bundle exec fastlane beta`.

## External dependencies
- Xcode + Xcode CLT (build/test)
- Swift + SwiftPM packages (e.g., `ConfettiSwiftUI`)
- RevenueCat Purchases SDK (subscriptions)
- Fastlane + Ruby (TestFlight)
- Python + behave/requests (BDD)
- VHS + tmux (CLI recording)
- OpenAI-compatible LLM API (BDD LLM scenario)
