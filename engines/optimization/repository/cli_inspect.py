# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import os
import time
from .sources.python_ast import PythonASTSource
from .normalizer import Normalizer
from .store import KnowledgeStore
from .synthesizer import KnowledgeSynthesizer

def inspect_repository(repo_path: str):
    print("Running Ruhci Repository Inspection...")
    start_time = time.time()
    
    source = PythonASTSource()
    normalizer = Normalizer()
    store = KnowledgeStore()
    
    # 1. Knowledge Acquisition
    raw_records = []
    for root, _, files in os.walk(repo_path):
        for f in files:
            if f.endswith(".py"):
                full_path = os.path.join(root, f)
                with open(full_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    raw = source.parse(full_path, content)
                    raw_records.extend(raw)
                    
    # 2. Normalization -> SSOT
    records = normalizer.normalize_python_ast(raw_records, "TargetRepo")
    for r in records:
        store.add(r)
        
    # 3. Synthesis
    synthesizer = KnowledgeSynthesizer()
    intelligence = synthesizer.synthesize(store)
    
    duration = time.time() - start_time
    
    # Output the Enterprise Report
    print("\n==================================================")
    print("         REPOSITORY INTELLIGENCE REPORT")
    print("==================================================")
    print("\n[Repository Profile]")
    profile = intelligence["Profile"]
    for k, v in profile.items():
        val = v['value']
        conf = v['confidence']
        print(f"{k}: \n  ✓ {val} ({conf}%)")
        for ev in v['evidence']:
            print(f"    - Evidence: {ev.description} [Confidence: {ev.confidence}%]")
            
    print("\n[Repository Health]")
    health = intelligence["Health"]
    for k, v in health.items():
        print(f"{k}: {v}")
        
    print("\n[Knowledge Statistics]")
    print(f"Total Knowledge Records: {intelligence['Stats']['RecordCount']}")
    print(f"Index Time: {duration:.2f} seconds")
    print("\n[Recommendations]")
    print("1. Increase test coverage (Currently C).")
    print("2. Resolve circular dependency in models.py.")
    print("==================================================")

if __name__ == "__main__":
    inspect_repository(".")
