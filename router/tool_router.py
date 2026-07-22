# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import Any, Callable, Dict, List


class ToolRouter:
    """Routes tool call requests to the correct executor callable."""

    def __init__(self):
        self._tools: Dict[str, Callable] = {}

    def register_tool(self, tool_name: str, executor_func: Callable) -> None:
        self._tools[tool_name] = executor_func

    def route(self, tool_name: str, params: Dict) -> Any:
        executor = self._tools.get(tool_name)
        if executor is None:
            raise KeyError(f"No executor registered for tool: '{tool_name}'")
        return executor(**params)

    def list_tools(self) -> List[str]:
        return list(self._tools.keys())

    def unregister_tool(self, tool_name: str) -> None:
        self._tools.pop(tool_name, None)
