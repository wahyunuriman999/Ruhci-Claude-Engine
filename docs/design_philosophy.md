# Ruhci Design Philosophy

## Why Ruhci Exists
In the era of massive LLM context windows, a common misconception has emerged: *Large context window equals large understanding*. 

However, feeding an AI half a million tokens of raw repository files introduces extreme noise, destroys reasoning efficiency (the "Lost in the Middle" problem), and drives up API costs unnecessarily.

## Core Principle
**Evidence before Context.**

We believe that an AI coding agent should only be given files that have deterministic, mathematically verifiable relationships to the developer's intent. 

## Design Rules
1. **Never send unnecessary files.** If a file cannot prove its relevance via AST dependencies or explicit symbols, drop it.
2. **Never trust semantic similarity alone.** Fuzzy keyword matching retrieves noise. Structural graphs retrieve logic.
3. **Never hide uncertainty.** If the engine encounters dynamic imports or reflection, it must warn the user (and the LLM) that its confidence is degraded.
4. **Prefer deterministic evidence over probabilistic guessing.** We do not use LLMs to rank files. We use LLMs to *reason* over files that a deterministic engine has already ranked.
