# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import re
from collections import Counter
from typing import Dict, List, Tuple


class EmbeddingIndexer:
    """Bag-of-words document indexer with cosine-style similarity search."""

    def __init__(self):
        self._docs: Dict[str, Dict[str, int]] = {}  # doc_id -> word_count

    def _vectorize(self, text: str) -> Dict[str, int]:
        words = re.findall(r"[a-zA-Z_][a-zA-Z0-9_]{2,}", text.lower())
        return dict(Counter(words))

    def index(self, doc_id: str, text: str) -> None:
        self._docs[doc_id] = self._vectorize(text)

    def similarity(self, doc_id_a: str, doc_id_b: str) -> float:
        """Word-overlap Jaccard similarity between two indexed docs."""
        a = set(self._docs.get(doc_id_a, {}).keys())
        b = set(self._docs.get(doc_id_b, {}).keys())
        if not a and not b:
            return 1.0
        if not a or not b:
            return 0.0
        return len(a & b) / len(a | b)

    def search(self, query_text: str) -> List[Tuple[str, float]]:
        """Return all docs sorted by overlap score with the query."""
        q_words = set(self._vectorize(query_text).keys())
        if not q_words:
            return []
        scores: List[Tuple[str, float]] = []
        for doc_id, word_count in self._docs.items():
            doc_words = set(word_count.keys())
            overlap = len(q_words & doc_words) / len(q_words | doc_words)
            if overlap > 0:
                scores.append((doc_id, round(overlap, 4)))
        return sorted(scores, key=lambda x: x[1], reverse=True)
