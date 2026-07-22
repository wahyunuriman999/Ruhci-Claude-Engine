# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import threading
from copy import deepcopy
from typing import Dict


class StateSynchronizer:
    """Synchronises shared state between multiple agents using version counters."""

    def __init__(self):
        self._state: Dict = {}
        self._version: int = 0
        self._lock = threading.Lock()

    def push(self, agent_id: str, state_delta: Dict) -> int:
        """Merge agent's state delta into global state. Returns new version."""
        with self._lock:
            self._state.update(state_delta)
            self._version += 1
            return self._version

    def pull(self, agent_id: str) -> Dict:
        """Return a copy of the current global state for the agent."""
        with self._lock:
            return deepcopy(self._state)

    def get_version(self) -> int:
        with self._lock:
            return self._version

    def reset(self) -> None:
        with self._lock:
            self._state = {}
            self._version = 0
