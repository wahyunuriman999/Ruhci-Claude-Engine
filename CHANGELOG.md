# Changelog

## v0.1 Research Preview
Initial release of the Ruhci Deterministic Context Intelligence Engine.

**Added:**
- AST Parser for structural code analysis.
- Hybrid Ranker fusing Symbol, Dependency, Semantic, and Intent weights.
- Context Pruner with Dynamic Top-K and Cascade Gap Filtering.
- Scientific Benchmark framework covering 5 repositories and 25 complex queries.
- Community Validation Hub for external validation.

**Known Limitations:**
- Dynamic imports are currently missed by static analysis.
- Runtime-generated code (framework magic) reduces dependency resolution accuracy.
