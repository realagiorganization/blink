Feature: LLM request via opencode cli
  The opencode CLI should be able to call the LLM with a secret key.

  Scenario: Request a completion using encrypted key
    Given the opencode cli is installed
    When I request a completion from the LLM
    Then the response is saved
