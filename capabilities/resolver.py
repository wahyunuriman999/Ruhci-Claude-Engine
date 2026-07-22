# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import Dict, List


class CapabilityResolver:
    """Resolves which system capabilities are needed for a given task description."""

    def __init__(self):
        self._map: Dict[str, List[str]] = {}  # capability_name -> [keywords]

    def register_capability(self, name: str, keywords: List[str]) -> None:
        self._map[name] = [kw.lower() for kw in keywords]

    def resolve(self, task: str) -> List[str]:
        """Return capability names whose keywords match the task description."""
        task_lower = task.lower()
        matched = []
        for cap, keywords in self._map.items():
            if any(kw in task_lower for kw in keywords):
                matched.append(cap)
        return matched

    def list_capabilities(self) -> List[str]:
        return list(self._map.keys())
