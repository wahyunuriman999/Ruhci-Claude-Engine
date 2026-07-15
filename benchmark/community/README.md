# Ruhci Community Validation Hub

Welcome to the **Ruhci Community Validation Hub**. Ruhci is an open research project that investigates whether AI coding agents can achieve comparable software engineering performance using a smaller, evidence-driven context.

We do not claim Ruhci is perfect. We want you to break it.

This hub is designed for external developers to submit challenging real-world queries to see where Ruhci's deterministic AST approach succeeds and where it fails. 

**IMPORTANT RULE:**
> A valid benchmark case may prove success OR failure. We do not cherry-pick. If Ruhci fails a well-formed query, it goes on the scoreboard and helps us improve the engine.

## How to Submit a Case
1. Copy the `submit_template.json` format.
2. Define a complex software engineering query for one of the supported (or future) repositories.
3. Submit a Pull Request with your JSON file to the `benchmark/community/` folder.
4. If valid, your case will be executed and recorded on the `leaderboard.md`.

Please review the `evaluation_rules.md` to understand how we measure Success (F1, MRR, Context Sufficiency).
