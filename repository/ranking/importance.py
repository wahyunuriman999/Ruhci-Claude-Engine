# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from collections import defaultdict
from typing import Dict, List, Tuple


class ImportanceRanker:
    """Ranks files by how many other files import them."""

    def rank(self, dependency_graph: Dict[str, List[str]]) -> List[Tuple[str, int]]:
        """
        Given {file: [imported_modules]}, count how many times each
        module appears as a dependency. Returns sorted list (most-imported first).
        """
        import_count: Dict[str, int] = defaultdict(int)
        for _importer, imports in dependency_graph.items():
            for module in imports:
                import_count[module] += 1
        # Also seed files that import nothing so they appear in the result
        for filepath in dependency_graph:
            if filepath not in import_count:
                import_count[filepath] = 0
        return sorted(import_count.items(), key=lambda x: x[1], reverse=True)
