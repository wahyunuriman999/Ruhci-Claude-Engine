# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import re
from collections import defaultdict
from typing import Dict, List


class SemanticIndex:
    """Inverted index mapping keywords to file paths."""

    def __init__(self):
        self._index: Dict[str, List[str]] = defaultdict(list)

    def _tokenize(self, text: str) -> List[str]:
        words = re.findall(r"[a-zA-Z_][a-zA-Z0-9_]{2,}", text)
        return [w.lower() for w in words]

    def index_file(self, path: str, content: str) -> None:
        """Index all tokens in the file content."""
        tokens = set(self._tokenize(content))
        for token in tokens:
            if path not in self._index[token]:
                self._index[token].append(path)

    def search(self, query: str) -> List[str]:
        """Return file paths matching any token in the query."""
        hits: Dict[str, int] = defaultdict(int)
        for token in self._tokenize(query):
            for path in self._index.get(token, []):
                hits[path] += 1
        return sorted(hits, key=hits.get, reverse=True)