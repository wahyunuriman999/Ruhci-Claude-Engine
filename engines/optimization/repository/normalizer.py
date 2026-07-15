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
                description=f"Found {raw['type']} '{raw.get('name')}' at line {raw.get('line', 0)}",
                confidence=100.0,
                timestamp=int(time.time())
            )
            
            metadata = {
                "line": raw.get("line"),
                "decorators": raw.get("decorators", []),
                "bases": raw.get("bases", []),
                "returns": raw.get("returns", ""),
                "calls": raw.get("calls", []),
                "module": raw.get("module", "")
            }
            
            name = raw.get("name", "unknown")
            record = KnowledgeRecord(
                id=str(uuid.uuid4()),
                kind=raw["type"],
                language="Python",
                repository=repository_name,
                path=raw["path"],
                symbol=name,
                signature="",
                visibility="public" if not name.startswith("_") else "private",
                relationships=[],
                importance=50.0,
                confidence=100.0,
                metadata=metadata,
                source="PythonASTSource",
                evidence=[evidence]
            )
            records.append(record)
        return records