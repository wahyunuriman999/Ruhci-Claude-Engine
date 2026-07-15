# Security & Quality Audit
As an open-source tool that processes arbitrary code repositories, Ruhci adheres to the following security guidelines:

## 1. Benchmark Exploitation
- **Is the benchmark exploitable?** No runtime code execution is performed during analysis. Benchmark test execution occurs strictly in isolated sandboxes or Docker containers. Ruhci only generates the contextual output; it does not evaluate the generated code outside of the test runner environment.

## 2. Parser Safety against Malicious Repositories
- **Is the AST parser safe?** Python's `ast.parse()` is safe against arbitrary code execution. Ruhci statically analyzes the tree without invoking `exec()` or `eval()` on target repositories.

## 3. Path Traversal
- **Are there path traversal vulnerabilities?** Path resolution is strictly constrained to the target repository's root directory. The parser rejects any relative paths navigating upwards (`../`) outside the repository boundary.

## 4. Dependencies
- **Are there dangerous dependencies?** Ruhci limits third-party dependencies to widely trusted parsing and graph-building libraries. All dependencies are regularly audited for CVEs.
