import os

base_dir = r"C:\Users\ROG G532 LV\.gemini\antigravity\scratch\Ruhci-Claude-Engine"

files = {}

# 1. Advanced Python AST Parser
files["engines/optimization/repository/sources/python_ast.py"] = """
import ast
from typing import List, Dict, Any

class PythonASTSource:
    def _get_decorator_name(self, decorator) -> str:
        if isinstance(decorator, ast.Name):
            return decorator.id
        elif isinstance(decorator, ast.Call):
            return self._get_decorator_name(decorator.func)
        elif isinstance(decorator, ast.Attribute):
            return f"{self._get_decorator_name(decorator.value)}.{decorator.attr}"
        return "unknown_decorator"

    def _get_annotation(self, annotation) -> str:
        if isinstance(annotation, ast.Name):
            return annotation.id
        elif isinstance(annotation, ast.Subscript):
            return f"{self._get_annotation(annotation.value)}[{self._get_annotation(annotation.slice)}]"
        elif isinstance(annotation, ast.Constant):
            return str(annotation.value)
        return "Any"

    def parse(self, file_path: str, content: str) -> List[Dict[str, Any]]:
        raw_records = []
        try:
            tree = ast.parse(content)
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        raw_records.append({
                            "type": "import",
                            "name": alias.name,
                            "path": file_path,
                            "line": node.lineno
                        })
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        for alias in node.names:
                            raw_records.append({
                                "type": "import_from",
                                "module": node.module,
                                "name": alias.name,
                                "path": file_path,
                                "line": node.lineno
                            })
                elif isinstance(node, ast.ClassDef):
                    bases = [self._get_annotation(b) for b in node.bases]
                    decorators = [self._get_decorator_name(d) for d in node.decorator_list]
                    raw_records.append({
                        "type": "class",
                        "name": node.name,
                        "bases": bases,
                        "decorators": decorators,
                        "path": file_path,
                        "line": node.lineno
                    })
                elif isinstance(node, ast.FunctionDef) or isinstance(node, ast.AsyncFunctionDef):
                    decorators = [self._get_decorator_name(d) for d in node.decorator_list]
                    returns = self._get_annotation(node.returns) if node.returns else "None"
                    
                    # Extract calls inside function
                    calls = []
                    for child in ast.walk(node):
                        if isinstance(child, ast.Call):
                            if isinstance(child.func, ast.Name):
                                calls.append(child.func.id)
                            elif isinstance(child.func, ast.Attribute):
                                calls.append(child.func.attr)

                    raw_records.append({
                        "type": "function",
                        "name": node.name,
                        "decorators": decorators,
                        "returns": returns,
                        "calls": calls,
                        "path": file_path,
                        "line": node.lineno
                    })
        except SyntaxError:
            pass
        return raw_records
"""

# 2. Queryable RepositoryKnowledge
files["engines/optimization/repository/knowledge.py"] = """
from typing import List, Dict, Any
from .models import KnowledgeRecord

class RepositoryKnowledge:
    def __init__(self, store):
        self.store = store
        self.profile = {}
        self.health = {}
        self.stats = {}
        self.evidence = []

    def set_intelligence(self, intelligence: Dict[str, Any]):
        self.profile = intelligence.get("Profile", {})
        self.health = intelligence.get("Health", {})
        self.stats = intelligence.get("Stats", {})
        self.evidence = intelligence.get("Evidence", [])

    def find_symbol(self, name: str) -> List[KnowledgeRecord]:
        results = []
        for r in self.store.get_all():
            if r.symbol == name:
                results.append(r)
        return results

    def find_module(self, path_substring: str) -> List[KnowledgeRecord]:
        results = []
        for r in self.store.get_all():
            if path_substring in r.path:
                results.append(r)
        return results

    def callers(self, function_name: str) -> List[KnowledgeRecord]:
        results = []
        for r in self.store.get_all():
            if r.kind == "function":
                calls = r.metadata.get("calls", [])
                if function_name in calls:
                    results.append(r)
        return results
"""

# 3. Update Normalizer to pass new metadata
files["engines/optimization/repository/normalizer.py"] = """
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
"""

# Write files
for rel_path, content in files.items():
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content.strip())

print("Advanced Python AST Parser and Queryable RepositoryKnowledge written.")
