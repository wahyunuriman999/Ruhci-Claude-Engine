# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import json
import csv
import os
from datetime import datetime

class ProofGenerator:
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        
    def generate(self, results: dict):
        # 1. summary.json
        with open(os.path.join(self.output_dir, "summary.json"), "w", encoding="utf-8") as f:
            json.dump(results, f, indent=4)
            
        # 2. summary.csv
        with open(os.path.join(self.output_dir, "summary.csv"), "w", encoding="utf-8", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Metric", "Value"])
            for k, v in results.items():
                writer.writerow([k, v])
                
        # 3. README_TABLE.md
        table = f"""### Golden Benchmark Result
| Metric | Claude Native | Claude + Ruhci | Impact |
|---|---|---|---|
| Average Input Tokens | {results.get('native_tokens', 0)} | {results.get('ruhci_tokens', 0)} | **{results.get('token_saved_pct', 0)}% Saved** |
| Average Cost | ${results.get('native_cost', 0)} | ${results.get('ruhci_cost', 0)} | **{results.get('cost_saved_pct', 0)}% Saved** |
| Average Latency | {results.get('native_latency', 0)} s | {results.get('ruhci_latency', 0)} s | **{results.get('latency_faster_pct', 0)}% Faster** |
| Quality | 100% | {results.get('quality_score', 0)}% | **{results.get('quality_score', 0)}% Retained** |
| API Calls | {results.get('native_calls', 1)} | {results.get('ruhci_calls', 1)} | - |
| Relevant Context | N/A | {results.get('relevant_context_pct', 0)}% | - |
"""
        with open(os.path.join(self.output_dir, "README_TABLE.md"), "w", encoding="utf-8") as f:
            f.write(table)
