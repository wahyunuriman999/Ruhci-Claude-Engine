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