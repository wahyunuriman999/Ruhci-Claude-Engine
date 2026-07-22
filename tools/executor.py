# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import Dict, Any
from .registry import ToolRegistry

class ToolExecutor:
    """Executes registered tools safely and captures their output."""
    
    def __init__(self, registry: ToolRegistry):
        self.registry = registry
        
    def execute(self, tool_name: str, **kwargs) -> Dict[str, Any]:
        """Runs a tool with the provided arguments and catches exceptions."""
        tool_meta = self.registry.get_tool(tool_name)
        
        if not tool_meta:
            return {
                "status": "error",
                "output": f"Tool '{tool_name}' not found in registry."
            }
            
        try:
            # Validate required args
            for req in tool_meta["required_args"]:
                if req not in kwargs:
                    raise ValueError(f"Missing required argument: {req}")
                    
            # Execute
            result = tool_meta["func"](**kwargs)
            return {
                "status": "success",
                "output": result
            }
        except Exception as e:
            return {
                "status": "error",
                "output": f"Execution failed: {str(e)}"
            }
