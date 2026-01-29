Output docs/assets/llm-bdd.gif

Set Shell "bash"
Set Width 1200
Set Height 700
Set FontSize 18

Type "tmux new -s llm"
Enter
Sleep 500ms
Type "python scripts/opencode_cli.py --prompt \"Give one short Blink Shell tip.\" --output artifacts/llm-response.txt"
Enter
Sleep 2s
Type "exit"
Enter
