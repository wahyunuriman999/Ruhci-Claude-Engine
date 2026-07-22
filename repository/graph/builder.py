# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import Dict, List, Set


class DependencyGraphBuilder:
    """Builds an adjacency list dependency graph and detects cycles."""

    def build(self, dependencies: Dict[str, List[str]]) -> Dict[str, List[str]]:
        """Return an adjacency list: {file: [files_it_depends_on]}."""
        return {k: list(v) for k, v in dependencies.items()}

    def find_cycles(self) -> List[List[str]]:
        """
        Detect cycles using iterative DFS.
        Returns a list of cycles (each cycle is a list of node names).
        """
        return []  # Placeholder — real graph needed to find cycles

    def find_cycles_in(self, graph: Dict[str, List[str]]) -> List[List[str]]:
        """Detect cycles within the provided adjacency list using DFS."""
        visited: Set[str] = set()
        rec_stack: Set[str] = set()
        cycles: List[List[str]] = []

        def dfs(node: str, path: List[str]) -> None:
            visited.add(node)
            rec_stack.add(node)
            path.append(node)
            for neighbour in graph.get(node, []):
                if neighbour not in visited:
                    dfs(neighbour, path)
                elif neighbour in rec_stack:
                    # Found a cycle — extract the cycle portion
                    idx = path.index(neighbour)
                    cycles.append(path[idx:])
            path.pop()
            rec_stack.discard(node)

        for node in graph:
            if node not in visited:
                dfs(node, [])
        return cycles
