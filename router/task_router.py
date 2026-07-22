# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import Callable, Dict, List, Optional


class TaskRouter:
    """Routes incoming tasks to registered agents based on task-type keywords."""

    def __init__(self):
        self._routes: Dict[str, str] = {}  # task_type -> agent_name

    def register_agent(self, agent_name: str, task_types: List[str]) -> None:
        for task_type in task_types:
            self._routes[task_type.lower()] = agent_name

    def route(self, task_description: str) -> Optional[str]:
        """Return agent name matching any task_type keyword in the description."""
        task_lower = task_description.lower()
        for task_type, agent in self._routes.items():
            if task_type in task_lower:
                return agent
        return None

    def list_routes(self) -> Dict[str, str]:
        return dict(self._routes)
