# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import time
from typing import Any, Dict, List, Optional, Tuple


class IndexerCache:
    """TTL-based cache for indexer results with LRU-style expiry."""

    def __init__(self):
        self._store: Dict[str, Tuple[Any, float]] = {}  # key -> (value, expiry_ts)

    def set(self, key: str, value: Any, ttl_seconds: int = 300) -> None:
        expiry = time.time() + ttl_seconds
        self._store[key] = (value, expiry)

    def get(self, key: str) -> Optional[Any]:
        entry = self._store.get(key)
        if entry is None:
            return None
        value, expiry = entry
        if time.time() > expiry:
            del self._store[key]
            return None
        return value

    def invalidate(self, key: str) -> None:
        self._store.pop(key, None)

    def clear_expired(self) -> int:
        now = time.time()
        expired = [k for k, (_, exp) in self._store.items() if now > exp]
        for k in expired:
            del self._store[k]
        return len(expired)

    def size(self) -> int:
        return len(self._store)
