# Community Evaluation Rules

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
