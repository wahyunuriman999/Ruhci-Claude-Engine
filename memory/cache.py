# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import time
from typing import Any, Optional, Dict

class MemoryCache:
    """Fast, short-lived in-memory cache for frequently accessed context."""
    
    def __init__(self, ttl_seconds: int = 300):
        self._cache: Dict[str, Dict[str, Any]] = {}
        self.ttl = ttl_seconds
        
    def set(self, key: str, value: Any) -> None:
        """Stores a value in the cache with the current timestamp."""
        self._cache[key] = {
            "value": value,
            "timestamp": time.time()
        }
        
    def get(self, key: str) -> Optional[Any]:
        """Retrieves a value if it exists and has not expired."""
        entry = self._cache.get(key)
        if not entry:
            return None
            
        if time.time() - entry["timestamp"] > self.ttl:
            del self._cache[key]
            return None
            
        return entry["value"]
        
    def invalidate(self, key: str) -> None:
        """Explicitly removes a key from the cache."""
        if key in self._cache:
            del self._cache[key]
            
    def clear(self) -> None:
        """Clears all cached items."""
        self._cache.clear()
