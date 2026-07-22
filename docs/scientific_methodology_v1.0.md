# Ruhci Scientific Evaluation Report v1.0

## 1. Abstract
Ruhci is a deterministic context intelligence engine designed to reduce repository context size for AI coding agents while preserving task-solving capability. By prioritizing AST-based evidence and deterministic ranking over naive retrieval, Ruhci bridges the gap between context efficiency and model reasoning quality.

## 2. Introduction
**Problem: Context Overload**
Modern AI coding agents are powerful, but repository-scale reasoning introduces unnecessary context overhead. Feeding an LLM with 500,000 tokens of raw repository files leads to high latency, exorbitant costs, and potential context-window degradation (the "Lost in the Middle" phenomenon).

**Why Brute-Force Retrieval Fails**
Traditional retrieval systems (like simple RAG) pull files based on semantic similarity. They often fetch noisy, irrelevant files that share keywords but lack functional relationships, while missing hidden execution dependencies.

## 3. Research Question
Can deterministic repository analysis reduce LLM context requirements without degrading software engineering performance?

## 4. Hypothesis
A deterministic repository intelligence layer can reduce LLM context requirements while preserving software engineering task performance.

## 5. System Overview
Ruhci employs a multi-stage deterministic pipeline:
1. **Candidate Selector**: Filters 5000+ files down to a manageable subset.
2. **Hybrid Ranker**: Scores files based on Symbol Evidence, Dependency Relevance, Intent, and Semantic paths.
3. **Context Pruner**: Aggressively drops files lacking strong dependency links and executes threshold and gap filtering to achieve maximum compression.

## 6. Experimental Setup
- **Model**: Claude 3.5 Sonnet
- **Temperature**: 0.0 (Locked)
- **Dataset**: 25 Complex Engineering Queries (including Hidden Dependency traps)
- **Repositories**: FastAPI, Requests, Flask, Django, SQLAlchemy
- **Evaluation**: Blind Comparison between Claude Native (Full Repo) and Claude + Ruhci (Pruned Context)

## 7. Evaluation Metrics
- **Token Reduction**: Percentage reduction in input tokens.
- **Cost Reduction**: Percentage reduction in total cost (including Ruhci compute overhead).
- **Latency Reduction**: Percentage reduction in response time.
- **Task Success**: Correctness evaluated by passing test suites.
- **Context Sufficiency Score (CSS)**: Ratio of Ruhci success to Native success.
- **Regression Failure**: Number of tasks where Native passed but Ruhci failed due to missing dependencies.

## 8. Results

> **DISCLAIMER**: The following metrics are *Simulated Baseline Target Metrics* generated during the initial framework scaffolding to validate the evaluation pipeline. They do not represent empirical measurements of the live v0.1 engine. We are actively transitioning from simulation to real empirical benchmarking.

| Metric | Native | Claude + Ruhci |
|---|---|---|
| Context Size (Net Input) | 100% | 7.9% |
| Total Cost | 100% | 7.9% |
| Task Success | 22/22 | 22/22 |
| Context Sufficiency Score | - | 100.0% |
| Regression Failure | - | 0 |

## Core Findings

Ruhci targets a **92.1% net reduction** in token usage and cost. The theoretical Context Sufficiency Score of 100.0% alongside 0 Regression Failures aims to prove that deterministic context pruning successfully filters noise without stripping vital execution graphs or hidden dependencies.


## 9.5. Threats to Validity

**Internal Validity**
*Is the benchmark overfitted to Ruhci's architecture?* 
To mitigate this, we rely on unseen repositories and an open community benchmark hub to continuously test edge cases.

**External Validity**
*Does this apply to all programming languages?*
Currently, no. The AST analysis is Python-first. Dynamic languages with heavy runtime evaluation may see degraded ranking accuracy.

**Construct Validity**
*Does Context Sufficiency accurately measure AI quality?*
We currently use task completion (passing test suites) as a proxy for understanding. Future work may include time-to-first-success and human preference metrics.

## 10. Limitations
- **Language Coverage**: Current implementation focuses on languages with strong static analysis capabilities.
- **Dynamic Behavior**: Runtime-generated code, reflection, and highly dynamic patterns may reduce analysis accuracy.
- **Framework Knowledge**: Performance may vary depending on framework-specific patterns.
- **Repository Scale**: Large-scale repositories may require incremental indexing strategies.

## 11. Future Work
Subsequent versions will explore cross-language AST standardization, dynamic execution tracing, and incremental indexing for monorepos exceeding 10 million lines of code.\n