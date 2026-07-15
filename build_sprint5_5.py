import os
import json

base_dir = r"C:\Users\ROG G532 LV\.gemini\antigravity\scratch\Ruhci-Claude-Engine"

def write_file(rel_path, content):
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip() + "\n")

# 1. benchmark/community/README.md
write_file("benchmark/community/README.md", """# Ruhci Community Validation Hub

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
""")

# 2. benchmark/community/submit_template.json
write_file("benchmark/community/submit_template.json", """{
  "id": "community_case_000",
  "repository": "pandas",
  "task_type": "bug_fix",
  "query": "Describe the complex issue to solve here",
  "required_files": [
    "path/to/expected_file.py"
  ],
  "optional_files": [],
  "forbidden_files": [],
  "required_symbols": [],
  "difficulty": "hard",
  "notes": "Explain why this case is challenging for a static analysis engine."
}
""")

# 3. benchmark/community/evaluation_rules.md
write_file("benchmark/community/evaluation_rules.md", """# Community Evaluation Rules

To maintain scientific integrity, all submitted cases are evaluated against rigid deterministic metrics. We do not use LLMs to "guess" if the retrieval was good.

## 1. MRR (Mean Reciprocal Rank)
Did Ruhci place the `primary_file` (or highest priority `required_files`) at the top of the context?
- Rank 1: MRR 1.00
- Rank 2: MRR 0.50

## 2. Context Sufficiency Score (CSS)
Can Claude 3.5 Sonnet (Temp=0) pass the associated test suite when given ONLY the context files selected by Ruhci?
- Pass: CSS 100%
- Fail: CSS 0%

## 3. Regression Failure
Did the native approach (Full Repo Context) pass the test suite, but Ruhci failed because it pruned a vital dependency?
- If Yes: **Regression Failure Detected (FAIL)**

## Verdict
- **PASS**: CSS 100% and MRR > 0.5
- **FAIL**: CSS 0% or Regression Failure Detected
""")

# 4. benchmark/community/leaderboard.md
write_file("benchmark/community/leaderboard.md", """# Community Validation Scoreboard

This table tracks the performance of Ruhci against community-submitted edge cases. It serves as a transparency board, not a competition. We welcome failures.

| Case ID | Repository | Task Type | Contributor | Result | Notes |
|---------|------------|-----------|-------------|--------|-------|
| 001 | pandas | bug_fix | @wahyunuriman999 | ⏳ PENDING | Testing large scale DataFrame core logic |
| 002 | langchain | architecture | @userB | ⏳ PENDING | Testing highly dynamic abstractions |
| 003 | django | refactor | @userC | ⏳ PENDING | Testing extensive framework inheritance |

*Submit your cases to see them evaluated here!*
""")

# 5. benchmark/community/examples/
write_file("benchmark/community/examples/example_bug_fix.json", """{
  "id": "community_example_001",
  "repository": "fastapi",
  "task_type": "bug_fix",
  "query": "Fix silent validation error in JWT dependency",
  "required_files": [
    "fastapi/security/oauth2.py"
  ],
  "optional_files": ["fastapi/dependencies/utils.py"],
  "forbidden_files": [],
  "required_symbols": ["OAuth2PasswordBearer"],
  "difficulty": "medium",
  "notes": "Classic dependency injection bug."
}""")

write_file("benchmark/community/examples/example_feature.json", """{
  "id": "community_example_002",
  "repository": "requests",
  "task_type": "feature",
  "query": "Implement automatic retry on 429 Too Many Requests",
  "required_files": [
    "requests/adapters.py",
    "requests/sessions.py"
  ],
  "optional_files": [],
  "forbidden_files": [],
  "required_symbols": ["HTTPAdapter", "Session"],
  "difficulty": "medium",
  "notes": "Requires modifying the underlying urllib3 adapter."
}""")

write_file("benchmark/community/examples/example_architecture.json", """{
  "id": "community_example_003",
  "repository": "flask",
  "task_type": "architecture",
  "query": "How is the application context pushed and popped during a request lifecycle?",
  "required_files": [
    "flask/ctx.py",
    "flask/app.py"
  ],
  "optional_files": ["flask/globals.py"],
  "forbidden_files": [],
  "required_symbols": ["AppContext", "push", "pop"],
  "difficulty": "hard",
  "notes": "Heavily reliant on globals and thread-local state which can confuse static analysis."
}""")

# 6. docs/failure_cases.md
write_file("docs/failure_cases.md", """# Known Failure Modes

We believe an engineering tool is only as trustworthy as its known limitations. Ruhci relies on static AST parsing and deterministic graph resolution. Here are the documented edge cases where Ruhci currently fails.

## Case 001 — Dynamic Import
**Situation:**
```python
module = importlib.import_module(name)
```
**Expected Context:**
Ruhci should retrieve `plugins/auth_provider.py` which is dynamically loaded.

**Actual Result:**
**Missed.** The Context Pruner dropped the file because there was no static import linking it to the execution path.

**Root Cause:**
AST static analysis does not evaluate runtime resolution strings.

**Planned Improvement:**
Introduce `Runtime Dependency Hints` via docstring parsing or manual `__dependencies__` declarations to anchor dynamic modules.

---

## Case 002 — Framework Magic (Decorators)
**Situation:**
A routing framework registers routes via implicit decorators without direct class instantiation.
```python
@app.route("/login")
def login():
    pass
```
**Expected Context:**
Ruhci should retrieve the core `Router` class that handles the request lifecycle for this endpoint.

**Actual Result:**
**Missed.** Ruhci retrieves the endpoint file but trims the routing engine, leading to Regression Failures if a core routing bug needs fixing.

**Root Cause:**
Ruhci's Hybrid Ranker heavily weights explicit class inheritance and function calls. Decorator registration often registers functions to a global or app-level dictionary dynamically.

**Planned Improvement:**
Increase Intent weighting for framework-specific `Role` keywords (e.g., `Router`, `Middleware`) during architecture-related queries.
""")

# 7. Update setup_repos.py
write_file("benchmark/setup_repos.py", """import argparse

# Supported Gold-Standard Repositories
SUPPORTED_REPOS = ["fastapi", "requests", "flask", "django", "sqlalchemy"]

# Future Validation Repositories (Sprint 5.5 Target Expansion)
# These repositories represent massive scale, dynamic architectures, or code generation challenges.
FUTURE_VALIDATION_REPOS = ["pytorch", "langchain", "pandas"]

def main():
    parser = argparse.ArgumentParser(description="Download and setup benchmark repositories.")
    parser.add_argument("--targets", nargs="+", help="List of repositories to setup", required=True)
    args = parser.parse_args()

    for target in args.targets:
        if target in SUPPORTED_REPOS:
            print(f"[SETUP] Preparing official benchmark repository: {target}")
            # Mock git clone logic
        elif target in FUTURE_VALIDATION_REPOS:
            print(f"[SETUP] Preparing future validation repository: {target} (Community Benchmark Only)")
            # Mock git clone logic
        else:
            print(f"[WARNING] Unknown repository target: {target}")

if __name__ == "__main__":
    main()
""")
