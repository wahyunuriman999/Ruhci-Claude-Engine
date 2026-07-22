# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import Any, Callable, Dict, List


class WorkerPool:
    """Manages a pool of named callable workers and broadcasts messages to them."""

    def __init__(self):
        self._workers: Dict[str, Callable] = {}

    def add_worker(self, name: str, func: Callable) -> None:
        self._workers[name] = func

    def remove_worker(self, name: str) -> None:
        self._workers.pop(name, None)

    def broadcast(self, message: Dict) -> Dict[str, Any]:
        """Call every worker with the message. Returns {name: result}."""
        results: Dict[str, Any] = {}
        for name, func in self._workers.items():
            try:
                results[name] = func(message)
            except Exception as e:
                results[name] = {"error": str(e)}
        return results

    def get_worker_count(self) -> int:
        return len(self._workers)

    def list_workers(self) -> List[str]:
        return list(self._workers.keys())
