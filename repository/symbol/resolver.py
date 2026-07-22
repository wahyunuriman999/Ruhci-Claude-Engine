# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import ast
from typing import Dict, Optional


class SymbolResolver:
    """Resolves where a Python class or function is defined."""

    def __init__(self):
        self._symbol_map: Dict[str, str] = {}  # symbol_name -> filepath

    def index_symbols(self, filepath: str, content: str) -> None:
        """Parse a file and record all class/function definitions."""
        try:
            tree = ast.parse(content, filename=filepath)
            for node in ast.walk(tree):
                if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
                    # Don't overwrite: first definition wins
                    if node.name not in self._symbol_map:
                        self._symbol_map[node.name] = filepath
        except SyntaxError:
            pass

    def resolve(self, symbol_name: str) -> Optional[str]:
        """Return the filepath where symbol_name is defined, or None."""
        return self._symbol_map.get(symbol_name)

    def all_symbols(self) -> Dict[str, str]:
        """Return the full symbol -> filepath map."""
        return dict(self._symbol_map)