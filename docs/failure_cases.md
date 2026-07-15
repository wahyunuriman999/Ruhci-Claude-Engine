# Known Failure Modes

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
