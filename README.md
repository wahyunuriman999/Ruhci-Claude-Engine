# Ruhci-Claude Engine

Ruhci-Claude Engine is a complete AI Engineering Engine optimized for Anthropic Claude.
It is NOT a Claude wrapper, but a full orchestration framework.

## Vision
To build the most token-efficient, context-aware, and autonomous AI engineering runtime for Claude.

## Architecture
```
User -> CLI -> Runtime -> Planner -> Task Queue -> Router -> Skill Loader -> Context Builder -> Repository Indexer -> Memory -> Checkpoint -> Claude SDK -> Reflection -> Validator -> Logger -> Output
```

## Features
- Maximum token efficiency and budget optimization
- AST-based Repository Indexer (Tree-sitter)
- Smart Context Management (compress, select, summarize)
- Intelligent Routing (Opus vs Sonnet vs Haiku)
- Autonomous Execution and Planning
- Advanced Reflection and Cognitive Validation

## Modules
- `engine/` - Core orchestration and runtime loop
- `indexer/` - AST parsing and dependency graph
- `context/` - Smart context building and windowing
- `token_optimizer/` - Token tracking and budget estimation
- `planner/` - Execution plan and task breakdown
- `memory/` - Semantic and conversation memory
- `router/` - Dynamic model and skill routing

## Installation
```bash
pip install -r requirements.txt
```

## Roadmap
**Phase 1:** Project Structure, SDK, Config, Logger, CLI (Current)
**Phase 2:** Repository Scanner, AST (Tree-sitter), File Ranking
**Phase 3:** Context Manager, Prompt Builder, Token Optimizer
**Phase 4:** Planner, Executor, Reflection, Skill System
**Phase 5:** Autonomous Loop, Continuous Mode, Checkpoint, Recovery

## License
PROPRIETARY AND CONFIDENTIAL
Copyright (c) 2024-2026 Wahyu Nur Iman. All rights reserved.
