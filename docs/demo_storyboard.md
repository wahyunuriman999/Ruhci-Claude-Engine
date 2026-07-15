# Ruhci Demo Video Storyboard

**Duration:** 3-5 Minutes
**Tone:** Professional, Engineering-Focused, Research-Backed

## Scene 1: The Context Challenge
*Visual: A fast-scrolling terminal showing an endless stream of code files being loaded.*
**Narrator/Text:** Modern AI coding agents are powerful, but repository-scale reasoning introduces unnecessary context overhead. 

## Scene 2: The Native Approach
*Visual: An architecture diagram showing a raw query pulling an entire repository into a generic LLM. A loading spinner spins for 10+ seconds. A massive API cost ticker flashes.*
**Narrator/Text:** The traditional approach provides everything. The model spends precious time and tokens parsing noise to find the signal.

## Scene 3: The Ruhci Intervention
*Visual: The user types a query: "Fix JWT refresh bug". The query passes through the `Ruhci Context Intelligence Engine`. Visuals show the AST Analyzer firing, building a Dependency Graph, and the Context Pruner aggressively slicing away irrelevant files, leaving exactly 2 files.*
**Narrator/Text:** Ruhci identifies high-confidence evidence. It deterministically ranks and prunes files based on symbols, dependencies, and execution paths.

## Scene 4: The Result
*Visual: Split screen. Left: Claude Native (500k tokens, 10s latency, $1.50). Right: Claude + Ruhci (8k tokens, 0.5s latency, $0.08). Both screens show "All Tests Passed!"*
**Narrator/Text:** The AI receives less noise and focuses strictly on relevant engineering context. The result? 92.1% net token reduction. The exact same engineering quality. Ruhci: The Deterministic Context Intelligence Engine.\n