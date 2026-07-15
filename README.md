# Ruhci (Research Preview v0.1)
**Deterministic Context Intelligence Engine for AI Coding Agents**

AI coding agents are powerful. But software repositories contain massive amounts of irrelevant information.

Ruhci reduces repository context complexity by identifying, ranking, and compressing high-confidence code evidence before it reaches an AI model.

## Why Ruhci?

**Without Ruhci:**
```
Repository (500,000 tokens) 
        |
        v
       LLM
```

**With Ruhci:**
```
Repository
        |
        v
Ruhci Intelligence Engine
        |
        v
Relevant Context (8,000 tokens)
        |
        v
       LLM
```

## Core Features
- **Deterministic Retrieval**: Prioritizes strict AST-based symbol evidence over fuzzy semantic matching.
- **Hybrid Ranking**: Fuses dependency graphs, intent classification, and semantic paths into a mathematically sound rank.
- **Confidence Pruning**: Aggressively eliminates context noise via dynamic thresholding and dependency lock rules.

## Benchmark Results (Real API Simulation)
Tested on 25 complex engineering queries across 5 major repositories (FastAPI, Requests, Flask, Django, SQLAlchemy) using Claude 3.5 Sonnet:
- **Token Reduction**: 92.1% (Net)
- **Cost Reduction**: 92.1% (Net)
- **Context Sufficiency**: 100.0% (Quality equal to Native)
- **Regression Failure**: 0

*Read the full [Scientific Evaluation Report](docs/scientific_report_v1.0.md).*

## Current Limitations
To ensure transparency, we disclose the following limitations:
- **Language Coverage**: Current implementation focuses on languages with strong static analysis capabilities.
- **Dynamic Behavior**: Runtime-generated code, reflection, and highly dynamic patterns may reduce analysis accuracy.
- **Framework Knowledge**: Performance may vary depending on framework-specific patterns.
- **Repository Scale**: Large-scale repositories may require incremental indexing strategies.

## Getting Started
View the [Reproducibility Guide](docs/reproduce_results.md) to run the benchmark pipeline locally.\n