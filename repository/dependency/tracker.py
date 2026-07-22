# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import ast
import os
from typing import Dict, List


class DependencyTracker:
    """Parses Python source files to extract import dependencies."""

    def __init__(self):
        self._all_deps: Dict[str, List[str]] = {}

    def track(self, filepath: str) -> Dict[str, List[str]]:
        """Parse a single Python file and return its imports."""
        imports: List[str] = []
        try:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                source = f.read()
            tree = ast.parse(source, filename=filepath)
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append(alias.name)
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        imports.append(node.module)
        except (SyntaxError, OSError):
            pass
        self._all_deps[filepath] = imports
        return {filepath: imports}

    def get_all_dependencies(self) -> Dict[str, List[str]]:
        """Return all tracked dependencies so far."""
        return dict(self._all_deps)