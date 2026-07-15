# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from loguru import logger
from router.registry import RouterRegistry

class TaskRouter:
    def __init__(self):
        logger.info("Initializing Enterprise TaskRouter (Registry Pattern).")
        
    def dispatch(self, route_target: str, context: dict) -> Any:
        handler = RouterRegistry.get_route(route_target)
        if not handler:
            logger.error(f"No handler registered for route: {route_target}")
            raise ValueError(f"Unknown route: {route_target}")
            
        logger.info(f"Dispatching to route: {route_target}")
        return handler(context)

# ==========================================
# BASE ROUTERS REGISTRATION
# ==========================================

@RouterRegistry.register("FileRouter")
def file_router(context):
    return "Handled by FileRouter"

@RouterRegistry.register("ToolRouter")
def tool_router(context):
    tool = context.get('tool_name')
    # Can further delegate to specific tool handlers
    return f"Handled by ToolRouter -> {tool}"

@RouterRegistry.register("SkillRouter")
def skill_router(context):
    return "Handled by SkillRouter"

@RouterRegistry.register("ContextRouter")
def context_router(context):
    return "Handled by ContextRouter"

@RouterRegistry.register("MemoryRouter")
def memory_router(context):
    return "Handled by MemoryRouter"

@RouterRegistry.register("ModelRouter")
def model_router(context):
    return "Handled by ModelRouter"

@RouterRegistry.register("PromptRouter")
def prompt_router(context):
    return "Handled by PromptRouter"

@RouterRegistry.register("WorkflowRouter")
def workflow_router(context):
    return "Handled by WorkflowRouter"

@RouterRegistry.register("RecoveryRouter")
def recovery_router(context):
    return "Handled by RecoveryRouter"

@RouterRegistry.register("ValidationRouter")
def validation_router(context):
    return "Handled by ValidationRouter"

# Example of registering specific tools under ToolRouter namespace (for v0.1 extensibility)
@RouterRegistry.register("ToolRouter::bash_execution")
def bash_tool(context): pass

@RouterRegistry.register("ToolRouter::python_execution")
def python_tool(context): pass

@RouterRegistry.register("ToolRouter::file_edit")
def edit_tool(context): pass
