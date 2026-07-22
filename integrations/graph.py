# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import Dict, List


class IntegrationGraph:
    """Tracks external integrations and resolves their load order via topological sort."""

    def __init__(self):
        self._graph: Dict[str, List[str]] = {}

    def add_integration(self, name: str, depends_on: List[str] = None) -> None:
        self._graph[name] = depends_on or []

    def is_connected(self, name: str) -> bool:
        return name in self._graph

    def get_load_order(self) -> List[str]:
        """Return a topologically sorted list of integration names."""
        visited = set()
        result: List[str] = []

        def visit(node: str) -> None:
            if node in visited:
                return
            visited.add(node)
            for dep in self._graph.get(node, []):
                visit(dep)
            result.append(node)

        for name in self._graph:
            visit(name)
        return result
