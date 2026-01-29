Feature: Core Blink use cases
  The core app capabilities should stay discoverable in the repo.

  Scenario: Build instructions are available
    Given the Blink repository is present
    Then the README mentions how to build
    And the build scripts are present

  Scenario: Paywall CTA is wired
    Given the paywall view exists
    Then the paywall has a trial CTA

  Scenario: Entitlements are defined
    Then entitlements include "unlimited_screen_time"
    And entitlements include "build"
