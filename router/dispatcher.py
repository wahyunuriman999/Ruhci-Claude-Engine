# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from loguru import logger
from typing import Dict, Any
from engine.base import BaseDispatcher
from router.registry import Registry, UniversalRegistry

class Dispatcher(BaseDispatcher):
    def dispatch(self, route_target: str, context: Dict[str, Any]) -> Any:
        handler = UniversalRegistry.get("Router", route_target)
        if not handler:
            # Fallback to look up in Tool if namespaced
            if "::" in route_target:
                cat, name = route_target.split("::", 1)
                handler = UniversalRegistry.get(cat.replace("Router", ""), name)
            
        if not handler:
            raise ValueError(f"No handler registered for route: {route_target}")
            
        logger.info(f"Dispatching to: {route_target}")
        return handler(context)

# ---------------------------------
# HIERARCHICAL ROUTERS
# ---------------------------------
@Registry.Router("ToolRouter")
def tool_router(context): return "ToolRouter Executed"

@Registry.Router("ContextRouter")
def context_router(context): return "ContextRouter Executed"

@Registry.Router("WorkflowRouter")
def workflow_router(context): return "WorkflowRouter Executed"

@Registry.Router("SkillRouter")
def skill_router(context): return "SkillRouter Executed"

@Registry.Router("ValidationRouter")
def validation_router(context): return "ValidationRouter Executed"

@Registry.Router("MemoryRouter")
def memory_router(context): return "MemoryRouter Executed"

@Registry.Router("EventRouter")
def event_router(context): return "EventRouter Executed"

@Registry.Router("PluginRouter")
def plugin_router(context): return "PluginRouter Executed"

# ---------------------------------
# MINIMAL TOOL STUBS
# ---------------------------------
tools = [
    "bash_execution", "python_execution", "file_read", "file_write", "file_edit",
    "repository_scan", "directory_scan", "git_operation", "semantic_search",
    "embedding_search", "grep_search", "vector_search", "documentation_lookup",
    "package_lookup", "dependency_scan", "test_runner", "lint_runner", "formatter",
    "security_scan", "benchmark", "profiler", "docker", "terminal",
    "patch_generation", "patch_validation", "rollback", "commit"
]

def make_stub(tool_name):
    @Registry.Tool(tool_name)
    def stub_func(context):
        return f"Tool Executed: {tool_name}"
    return stub_func

for t in tools:
    make_stub(t)
