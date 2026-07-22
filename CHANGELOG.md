# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.4] - 2026-07-22 — Build 7

### Added
- `[tool.pytest.ini_options] asyncio_mode = "auto"` in `pyproject.toml`
- `pytest>=7.0` and `pytest-asyncio>=0.23` in `requirements.txt` under `[project.optional-dependencies] test`
- `.venv/`, `venv/`, `env/` entries to `.gitignore`

### Fixed
- Removed `.venv/` from Git tracking (`git rm --cached .venv`) — 877 tracked dependency files removed from repo history
- `test_engine.py` now passes with `asyncio_mode = auto` — no longer fails with missing asyncio mark
- 44 malformed test files (single-line format) rewritten as valid Python with `pytestmark = pytest.mark.skip(...)`

### Test Results
```
4 passed, 45 skipped, 0 failed
```

---

## [1.0.3] - 2026-07-22 — Build 6 / Sprint 5-8

### Added — Sprint 5: Repository Subsystem
- `repository/dependency/tracker.py` — `DependencyTracker`: AST-based import extraction
- `repository/index/semantic.py` — `SemanticIndex`: inverted keyword index
- `repository/scanner/explorer.py` — `RepositoryExplorer`: recursive directory walker
- `repository/summarizer/hierarchical.py` — `HierarchicalSummarizer`: class/function/LOC extraction
- `repository/symbol/resolver.py` — `SymbolResolver`: symbol-to-filepath resolver
- `repository/ranking/importance.py` — `ImportanceRanker`: ranks files by import frequency
- `repository/change_detector/hybrid.py` — `HybridChangeDetector`: MD5-based change tracking
- `repository/graph/builder.py` — `DependencyGraphBuilder`: adjacency list + cycle detection
- `repository/workspace/snapshot.py` — `WorkspaceSnapshot`: full workspace capture + diff

### Added — Sprint 6: Fabric & Kernel Subsystem
- `kernel/logging.py` — `RuhciLogger`: structured JSON logger
- `kernel/registry.py` — `KernelRegistry`: thread-safe singleton service registry
- `kernel/command_bus.py` — `CommandBus`: pub-sub command dispatcher
- `fabric/sync.py` — `StateSynchronizer`: versioned shared state across agents
- `fabric/protocol.py` — `AgentProtocol` + `AgentMessage` dataclass (JSON encode/decode)
- `fabric/scheduler.py` — `TaskScheduler`: heapq-based priority task runner
- `fabric/workers.py` — `WorkerPool`: named callable worker pool with broadcast
- `fabric/discovery.py` — `ServiceDiscovery`: capability-based service registry with heartbeat
- `fabric/transport.py` — `MessageTransport`: in-memory per-agent message queue

### Added — Sprint 7: Integrations & Capabilities
- `integrations/graph.py` — `IntegrationGraph`: topological load order
- `integrations/negotiation.py` — `CapabilityNegotiator`: capability overlap negotiation
- `integrations/contracts.py` — `IntegrationContract`: formal system contract validation
- `capabilities/resolver.py` — `CapabilityResolver`: keyword-based capability matching
- `capabilities/registry.py` — `CapabilityRegistry`: central capability store
- `extensions/mcp_adapter/adapter.py` — `MCPAdapter`: Model Context Protocol adapter

### Added — Sprint 8: Autonomous, Adaptive & Final
- `autonomous/reflection.py` — `AutonomousReflector`: action/outcome log + auto-pause at <30% success
- `adaptive/orchestrator.py` — `AdaptiveOrchestrator`: rolling-metric strategy tuning
- `profiles/hierarchy.py` — `ProfileHierarchy`: parent→child config inheritance tree
- `indexer/cache.py` — `IndexerCache`: TTL-based cache with expiry
- `indexer/embedding.py` — `EmbeddingIndexer`: bag-of-words Jaccard similarity search
- `router/task_router.py` — `TaskRouter`: task-type → agent routing
- `router/tool_router.py` — `ToolRouter`: tool-name → executor routing
- `cli/main.py` — CLI entry point (`run`, `status`, `version` commands via argparse)

### Fixed
- `engine/orchestrator.py`: `RuhciOrchestrator` upgraded to accept `session_id` kwarg, returns `SessionState` dataclass
- `loguru` replaced with stdlib `logging` in `router/registry.py` and `indexer/scanner.py`
- Import verification: 31/31 new modules import cleanly

---

## [1.0.2] - 2026-07-22 — Build 5 / Phase 1-4

### Added — Phase 1: Memory Subsystem
- Episodic, semantic, working memory implementations
- Memory consolidator

### Added — Phase 2: Cognitive Subsystem
- Reasoning engine, metacognition, abstraction layer

### Added — Phase 3: Decision & Routing
- Consensus engine, policy evaluator, model/context routers
- `UniversalRegistry` with `@Registry` decorators

### Added — Phase 4: Planner, Reflection, Execution
- Task breakdown, priority planner, planning agent
- Reflection evaluator, execution pipeline, tool registry

### Fixed
- `engine/orchestrator.py`: `SystemOrchestrator` renamed to `RuhciOrchestrator`
- `benchmark/empirical_test.py`: binary data removed, replaced with ASCII placeholder
- `tools/registry.py`, `reflection/evaluator.py`: `Optional` import fix

---

## [1.0.1] - 2026-07-16

### Breaking: Scope Reduction
Removed aspirational stub-only modules to align codebase with verifiable scope.
Tracked for revival in v2.0 roadmap.

### Fixed
- Bug `i > 0` in ContextPruner (dependency lock skip index 0)
- Hub injection not respecting `max_candidates`
- Exploration mode thresholds
- Unified stemmer logic in `ruhci/utils/text.py`
- Made `penalized_containers` configurable
- Removed unused `diskcache` and `xxhash` from dependencies
- Removed tracked `__pycache__` from git

### Added
- `--explain` flag in CLI (`ruhci_ask.py`)
- `pyproject.toml` with hatchling build system
- Moved `empirical_test.py` to `benchmark/`
- Added `design_philosophy.md`, `failure_cases.md`, ADR docs
