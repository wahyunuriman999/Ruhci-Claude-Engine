# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import os
from typing import Dict, List


class RepositoryExplorer:
    """Scans a repository directory tree and returns structured file info."""

    def scan(self, root_dir: str, extensions: List[str] = None) -> List[str]:
        """Return all file paths matching the given extensions."""
        if extensions is None:
            extensions = [".py"]
        result: List[str] = []
        for dirpath, _, filenames in os.walk(root_dir):
            for fname in filenames:
                if any(fname.endswith(ext) for ext in extensions):
                    result.append(os.path.join(dirpath, fname))
        return result

    def get_file_tree(self, root_dir: str) -> Dict:
        """Return a nested dict representing the directory tree."""
        tree: Dict = {}
        for dirpath, dirnames, filenames in os.walk(root_dir):
            rel = os.path.relpath(dirpath, root_dir)
            node = tree
            if rel != ".":
                for part in rel.split(os.sep):
                    node = node.setdefault(part, {})
            for fname in filenames:
                node[fname] = None
        return tree