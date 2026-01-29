from pathlib import Path
import os
import subprocess

from behave import given, when, then

REPO_ROOT = Path(__file__).resolve().parents[3]
ARTIFACTS_DIR = REPO_ROOT / "artifacts"
LLM_RESPONSE_PATH = ARTIFACTS_DIR / "llm-response.txt"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


@given("the Blink repository is present")
def step_repo_present(context):
    assert (REPO_ROOT / "Blink.xcodeproj").exists(), "Blink.xcodeproj is missing"


@then("the README mentions how to build")
def step_readme_mentions_build(context):
    content = read_text(REPO_ROOT / "README.md")
    assert "Build" in content and "xcode-select" in content, "Build instructions missing"


@then("the build scripts are present")
def step_build_scripts_present(context):
    assert (REPO_ROOT / "get_frameworks.sh").exists(), "get_frameworks.sh missing"
    assert (REPO_ROOT / "get_resources.sh").exists(), "get_resources.sh missing"


@given("the paywall view exists")
def step_paywall_view_exists(context):
    content = read_text(REPO_ROOT / "Blink/Subscriptions/Intro.swift")
    assert "struct NewOfferingsView" in content, "Paywall view missing"


@then("the paywall has a trial CTA")
def step_paywall_cta(context):
    content = read_text(REPO_ROOT / "Blink/Subscriptions/Intro.swift")
    assert "TRY IT FREE FOR 14 DAYS" in content, "Trial CTA missing"


@then('entitlements include "{entitlement_id}"')
def step_entitlements_include(context, entitlement_id):
    content = read_text(REPO_ROOT / "Blink/Subscriptions/EntitlementsManager.swift")
    assert entitlement_id in content, f"Entitlement {entitlement_id} missing"


@given("the opencode cli is installed")
def step_opencode_cli_exists(context):
    assert (REPO_ROOT / "scripts/opencode_cli.py").exists(), "opencode CLI missing"


@when("I request a completion from the LLM")
def step_request_completion(context):
    api_key = os.environ.get("LLM_API_KEY")
    if not api_key:
        raise RuntimeError("LLM_API_KEY is required to run the LLM BDD scenario")

    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
    command = [
        "python",
        str(REPO_ROOT / "scripts/opencode_cli.py"),
        "--prompt",
        "Give one short Blink Shell tip.",
        "--output",
        str(LLM_RESPONSE_PATH),
    ]
    result = subprocess.run(command, check=False, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(
            "opencode cli failed: " + result.stdout + "\n" + result.stderr
        )


@then("the response is saved")
def step_response_saved(context):
    assert LLM_RESPONSE_PATH.exists(), "LLM response file missing"
    assert LLM_RESPONSE_PATH.read_text(encoding="utf-8").strip(), "LLM response empty"
