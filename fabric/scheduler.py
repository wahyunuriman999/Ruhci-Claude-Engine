# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import heapq
from typing import Any, Callable, List, Tuple


class TaskScheduler:
    """Priority-queue-based task scheduler (lower priority number = higher priority)."""

    def __init__(self):
        self._queue: List[Tuple[int, int, str, Callable]] = []
        self._counter = 0  # tie-breaker for equal priorities

    def schedule(self, task_id: str, priority: int, func: Callable) -> None:
        """Add a task with the given priority. Lower int = runs first."""
        heapq.heappush(self._queue, (priority, self._counter, task_id, func))
        self._counter += 1

    def run_next(self) -> Any:
        """Execute the highest-priority pending task and return its result."""
        if not self._queue:
            raise RuntimeError("No pending tasks in scheduler.")
        _, _, task_id, func = heapq.heappop(self._queue)
        return func()

    def pending_count(self) -> int:
        return len(self._queue)

    def clear(self) -> None:
        self._queue.clear()
