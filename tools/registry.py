# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import Dict, Any, Callable, Optional

class ToolRegistry:
    """Central registry for all available agent tools."""
    
    def __init__(self):
        self.tools: Dict[str, Dict[str, Any]] = {}
        
    def register(self, name: str, description: str, func: Callable, required_args: list = None) -> None:
        """Registers a new tool in the system."""
        self.tools[name] = {
            "description": description,
            "func": func,
            "required_args": required_args or []
        }
        
    def get_tool(self, name: str) -> Optional[Dict[str, Any]]:
        """Retrieves a tool's metadata and function reference."""
        return self.tools.get(name)
        
    def list_available_tools(self) -> Dict[str, str]:
        """Returns a mapping of tool names to their descriptions."""
        return {name: meta["description"] for name, meta in self.tools.items()}
