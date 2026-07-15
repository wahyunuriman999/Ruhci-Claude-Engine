# Changelog

All notable changes to the Ruhci Claude Engine will be documented in this file.

## [v0.3.4] - 2026-07-16

### 🚀 Milestone: Functional Research Preview
Version 0.3.4 marks the transition of the Ruhci Engine from a theoretical architectural scaffold into a genuine, working empirical research preview. The end-to-end AST pipeline is now operational and runs live against real repositories.

### Important Disclaimer Regarding Performance Metrics
*Please note that the "92.1% Semantic Match" metric stated in the README is a **Simulated Baseline Target Metric** established during early theoretical modeling. It is an aspirational benchmark and does not represent the empirical output of the current v0.3.4 build.*

### Changes from v0.1 to v0.3.4
- **End-to-End Pipeline Execution:** The engine (`RuhciEngine`) can now clone, scan, parse, build dependency graphs, select candidates, and rank them live. Empirical runs are saved under `benchmark/proof/`.
- **AST Parser Improvements:** Replaced surface-level parsing with a fully recursive AST parser capable of deep method and nested-class extraction across Python files.
- **Dependency Graph Enhancements:** Implemented dynamic module resolution and relative import handling (e.g., resolving `src-layout` paths), ensuring that the `DependencyGraph` builds functional edge relationships.
- **Organic Candidate Selection:** Replaced the hardcoded 'whitelist' approach with a deterministic, graph-aware `CandidateSelector`. The selector now identifies critical hub files (e.g., `sessions.py`) organically by utilizing degree centrality (both in-degree and out-degree).
- **Hybrid Ranker Recalibration:** 
  - Overhauled symbol scoring to eliminate large-file bias (inflated counts on large files) by strictly calculating the ratio of unique query terms mapped to symbols.
  - Replaced hardcoded test file penalties with a static post-fusion multiplier (`0.5`) to push test files down organically without compromising their inherent symbol or dependency strengths.
  - Implemented 'safe stemming' via regex with a whitelist of exceptions (securing words like `does`, `status`, `process`) to allow singular/plural token matching without text corruption.
- **Removed Debug Artefacts:** Completely scrubbed the codebase of manual `override` blocks, forced filenames, and leftover debug scripts (e.g., `debug.py`).

### Known Limitations (v0.4 Roadmap)
1. **Blind to Content:** Files devoid of top-level AST symbols (e.g., `certs.py` or config files) receive zero symbol scores and often fall behind structurally complex files. Content-based semantic matching (TF-IDF/Vector Embeddings) is targeted for v0.4.
2. **Dependency Dominance:** High in-degree utility files (e.g., `models.py` or `compat.py`) can heavily dominate the ranking due to the weight of the dependency score. Future iterations will require cross-validating structural centrality with deep semantic relevance to minimize false positives.
