# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import ast
import os
from typing import Dict, List


class HierarchicalSummarizer:
    """Extracts structural summary from Python source files using AST."""

    def summarize(self, filepath: str) -> Dict:
        """Return a dict with classes, functions, and line count."""
        classes: List[str] = []
        functions: List[str] = []
        loc = 0
        docstring = ""
        try:
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                source = f.read()
            loc = source.count("\n") + 1
            tree = ast.parse(source, filename=filepath)
            # Module-level docstring
            if (
                tree.body
                and isinstance(tree.body[0], ast.Expr)
                and isinstance(tree.body[0].value, ast.Constant)
            ):
                docstring = str(tree.body[0].value.value)[:200]
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    classes.append(node.name)
                elif isinstance(node, ast.FunctionDef):
                    functions.append(node.name)
        except (SyntaxError, OSError):
            pass
        return {"classes": classes, "functions": functions, "loc": loc, "docstring": docstring}