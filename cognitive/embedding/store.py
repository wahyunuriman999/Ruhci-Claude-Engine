# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import List, Dict, Any
import math

class EmbeddingStore:
    """Wrapper for handling and comparing cognitive vector embeddings."""
    
    def __init__(self):
        self.vectors: Dict[str, List[float]] = {}
        
    def add_embedding(self, key: str, vector: List[float]) -> None:
        """Stores a vector embedding."""
        self.vectors[key] = vector
        
    def _cosine_similarity(self, vec1: List[float], vec2: List[float]) -> float:
        """Calculates cosine similarity between two vectors."""
        if not vec1 or not vec2 or len(vec1) != len(vec2):
            return 0.0
            
        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        norm_a = math.sqrt(sum(a * a for a in vec1))
        norm_b = math.sqrt(sum(b * b for b in vec2))
        
        if norm_a == 0 or norm_b == 0:
            return 0.0
            
        return dot_product / (norm_a * norm_b)
        
    def find_nearest(self, query_vector: List[float], top_k: int = 5) -> List[Dict[str, Any]]:
        """Finds the most similar stored vectors to the query."""
        results = []
        for key, vec in self.vectors.items():
            sim = self._cosine_similarity(query_vector, vec)
            results.append({"key": key, "score": sim})
            
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:top_k]
