# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2026-07-22

### Breaking: Scope Reduction
Removed aspirational modules (`context/`, `engine/`, `router/`, `memory/`, `planner/`, `cli/`, etc.) to align codebase with v1.0 production scope (AST-based context optimizer for Python repos, consisting of `indexer/` and ranking pipelines). 
These modules are tracked as v2.0 roadmap items. The badge status has been updated to Beta to accurately reflect the current maturity.

### Fixed
- Fixed bug `i > 0` in ContextPruner (dependency lock skip index 0)
- Fixed Hub injection not respecting `max_candidates`
- Fixed Exploration mode thresholds
- Unified stemmer logic in `ruhci/utils/text.py` and fixed suffix iteration ordering for deterministic stemming
- Made `penalized_containers` configurable via constructor injection
- Removed unused `diskcache` and `xxhash` from dependencies
- Removed tracked `__pycache__` artifacts from git
- Skipped unimplemented tests via `@pytest.mark.skip`

### Added
- Added `--explain` flag in CLI (`ruhci_ask.py`)
- Added `pyproject.toml` with hatchling build system and proper metadata
- Moved `empirical_test.py` to `benchmark/`
- Improved docs with `design_philosophy.md`, `failure_cases.md`, and explicit architectural decisions.

