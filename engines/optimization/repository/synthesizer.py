# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import time
from typing import List, Dict, Any
from .store import KnowledgeStore
from .models import Evidence

class KnowledgeSynthesizer:
    def synthesize(self, store: KnowledgeStore) -> Dict[str, Any]:
        intelligence = {
            "Profile": {
                "Language": {"value": "Unknown", "confidence": 0.0, "evidence": []},
                "Framework": {"value": "Unknown", "confidence": 0.0, "evidence": []},
                "Architecture": {"value": "Unknown", "confidence": 0.0, "evidence": []},
                "Database": {"value": "Unknown", "confidence": 0.0, "evidence": []}
            },
            "Health": {
                "Maintainability": "B",
                "Complexity": "B+",
                "Testing": "C",
            },
            "Stats": {
                "RecordCount": len(store.get_all()),
                "EntryPoints": 0
            }
        }
        
        # Simple framework detection rule
        imports = [r for r in store.query(kind="import")]
        framework_evidence = []
        fastapi_detected = False
        django_detected = False
        
        for imp in imports:
            if "fastapi" in imp.symbol.lower():
                fastapi_detected = True
                framework_evidence.append(Evidence("Import", imp.path, "fastapi imported", 99.0, int(time.time())))
            if "uvicorn" in imp.symbol.lower():
                framework_evidence.append(Evidence("Import", imp.path, "uvicorn imported", 95.0, int(time.time())))
            if "django" in imp.symbol.lower():
                django_detected = True
        
        if fastapi_detected and django_detected:
            # False positive handling or hybrid
            intelligence["Profile"]["Framework"] = {"value": "Hybrid (FastAPI/Django)", "confidence": 60.0, "evidence": framework_evidence}
        elif fastapi_detected:
            intelligence["Profile"]["Framework"] = {"value": "FastAPI", "confidence": 99.0, "evidence": framework_evidence}
        elif django_detected:
            intelligence["Profile"]["Framework"] = {"value": "Django", "confidence": 99.0, "evidence": framework_evidence}
            
        # Language detection
        python_records = store.query(language="Python")
        if python_records:
            intelligence["Profile"]["Language"] = {
                "value": "Python", 
                "confidence": 100.0, 
                "evidence": [Evidence("FileExt", "multiple", ".py files detected", 100.0, int(time.time()))]
            }
            
        return intelligence
