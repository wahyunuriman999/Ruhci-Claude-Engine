# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import time
import uuid
from typing import List
from .models import KnowledgeRecord, Evidence

class Normalizer:
    def normalize_python_ast(self, raw_records: List[dict], repository_name: str) -> List[KnowledgeRecord]:
        records = []
        for raw in raw_records:
            evidence = Evidence(
                type="AST_Node",
                source=raw["path"],
                description=f"Found {raw['type']} '{raw['name']}' at line {raw.get('line', 0)}",
                confidence=100.0,
                timestamp=int(time.time())
            )
            record = KnowledgeRecord(
                id=str(uuid.uuid4()),
                kind=raw["type"],
                language="Python",
                repository=repository_name,
                path=raw["path"],
                symbol=raw["name"],
                signature="",
                visibility="public" if not raw["name"].startswith("_") else "private",
                relationships=[],
                importance=50.0,
                confidence=100.0,
                metadata={"line": raw.get("line")},
                source="PythonASTSource",
                evidence=[evidence]
            )
            records.append(record)
        return records
