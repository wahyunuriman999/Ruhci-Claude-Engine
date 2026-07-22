# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import Any, Callable, Dict, List, Optional


class MCPAdapter:
    """Adapter for Model Context Protocol (MCP) tool registration and invocation."""

    def __init__(self):
        self._tools: Dict[str, Dict] = {}

    def register_tool(
        self,
        name: str,
        description: str,
        input_schema: Dict,
        handler: Callable,
    ) -> None:
        self._tools[name] = {
            "description": description,
            "input_schema": input_schema,
            "handler": handler,
        }

    def call_tool(self, name: str, params: Dict) -> Any:
        tool = self._tools.get(name)
        if tool is None:
            raise KeyError(f"Tool '{name}' not found in MCP registry.")
        # Validate required params based on schema
        required = tool["input_schema"].get("required", [])
        missing = [r for r in required if r not in params]
        if missing:
            raise ValueError(f"Missing required params for '{name}': {missing}")
        return tool["handler"](**params)

    def get_tool_manifest(self) -> List[Dict]:
        return [
            {
                "name": name,
                "description": meta["description"],
                "input_schema": meta["input_schema"],
            }
            for name, meta in self._tools.items()
        ]

    def list_tools(self) -> List[str]:
        return list(self._tools.keys())
