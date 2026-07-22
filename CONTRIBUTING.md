# Contributing to Ruhci Claude Engine

Thank you for your interest in contributing! Ruhci is an open-source Autonomous AI Agent OS and we welcome contributions of all kinds.

---

## 🧭 Project Philosophy

Ruhci is built on three principles:

1. **Honesty over hype** — We only document what is actually implemented and working.
2. **Modularity** — Each subsystem (memory, router, planner, fabric, etc.) is independent and replaceable.
3. **Real code only** — No stubs, no `pass`-only bodies. Every class must do real work.

---

## 🛠️ How to Set Up Locally

```bash
git clone https://github.com/wahyunuriman999/Ruhci-Claude-Engine.git
cd Ruhci-Claude-Engine

python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Linux/Mac

pip install -r requirements.txt
pip install pytest pytest-asyncio  # for running tests
```

Run the test suite:
```bash
pytest tests/ -q
# Expected: 4 passed, 45 skipped, 0 failed
```

---

## 📦 Subsystem Map

| Directory | Purpose |
|---|---|
| `engine/` | Core orchestrator and session management |
| `memory/` | Episodic, semantic, working memory |
| `cognitive/` | Reasoning, metacognition, abstraction |
| `router/` | Task, tool, model, context routing |
| `planner/` | Task decomposition and priority scheduling |
| `decision/` | Consensus engine and policy evaluation |
| `reflection/` | Autonomous self-monitoring |
| `adaptive/` | Strategy adjustment from metrics |
| `fabric/` | Inter-agent message passing and scheduling |
| `kernel/` | Logging, registry, command bus |
| `repository/` | Static code analysis (no LLM needed) |
| `indexer/` | Caching and embedding-based search |
| `integrations/` | External system integration contracts |
| `capabilities/` | Capability registry and resolver |
| `extensions/mcp_adapter/` | Model Context Protocol adapter |
| `profiles/` | Profile hierarchy with config inheritance |
| `cli/` | Command-line interface |

---

## ✅ What to Contribute

- **Bug fixes** — Fix logic errors in any subsystem
- **New subsystem features** — Add methods to existing classes
- **Test implementations** — Activate skipped tests by implementing their modules
- **LLM integration** — Wire `engine/core.py` to a real LLM API (Claude, GPT, Ollama)
- **Documentation** — Improve docs, add examples, write tutorials

---

## ❌ What We Will Not Accept

- Stub-only files (`pass` body with no logic)
- Files that add imports without implementations
- Code that re-introduces previously removed binary artifacts
- External dependencies without justification in the PR description

---

## 📝 Pull Request Process

1. Fork the repository
2. Create a branch: `git checkout -b feat/your-feature-name`
3. Make your changes with real, working code
4. Run `pytest tests/` — ensure 0 new failures
5. Submit a PR with a clear description of what you added and why

---

## 📋 Reporting Issues / Edge Cases

If you discover a failure case in any subsystem, please open a GitHub Issue with:

- Which module/class failed
- Input that triggered the failure  
- Expected vs. actual behavior

---

**Copyright © 2024–2026 Wahyu Nur Iman**  
Licensed under the MIT License.
