import os

base_dir = r"C:\Users\ROG G532 LV\.gemini\antigravity\scratch\Ruhci-Claude-Engine"

header = """# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
"""

prompts_py = header + """
PLANNER_SYSTEM_PROMPT = \"\"\"
You are the Lead Architect for the Ruhci-Claude Engine.
Your job is to breakdown complex tasks into a precise Task Graph.

You must determine the optimal execution strategy (Sequential, Concurrent, or Mixed) 
and return a JSON array matching the Pydantic TaskGraph model.

Focus on creating independent tasks where possible, but strictly sequence tasks that depend on earlier outputs.
\"\"\"
"""

agent_py = header + """
from typing import List, Optional, Literal
from pydantic import BaseModel, Field
from loguru import logger
from planner.prompts import PLANNER_SYSTEM_PROMPT

class PlannerStrategy(BaseModel):
    mode: Literal["AUTO", "SEQUENTIAL", "CONCURRENT", "MIXED"] = "AUTO"

class TaskNode(BaseModel):
    task_id: str
    description: str
    priority: int = 1
    dependencies: List[str] = Field(default_factory=list)
    estimated_token: int = 0
    estimated_cost: float = 0.0
    estimated_time: int = 0  # in seconds
    route_target: str = "auto" # The router to use

class TaskGraph(BaseModel):
    strategy: PlannerStrategy = Field(default_factory=PlannerStrategy)
    nodes: List[TaskNode] = Field(default_factory=list)
    
class PlanningAgent:
    def __init__(self, llm_client=None):
        self.client = llm_client
        logger.info("Initialized PlanningAgent with Hybrid Strategy support.")
        
    async def create_plan(self, user_prompt: str) -> TaskGraph:
        logger.info("PlanningAgent: Analyzing dependencies and building Task Graph...")
        # Stub: In real execution, this calls Claude with tools/structured output
        # to generate a JSON adhering to TaskGraph.
        
        # Simulating a mock graph
        node1 = TaskNode(
            task_id="task_1",
            description="Generate Model",
            route_target="WorkflowRouter",
            estimated_token=500,
            estimated_time=10
        )
        node2 = TaskNode(
            task_id="task_2",
            description="Generate API",
            dependencies=["task_1"],
            route_target="ToolRouter",
            estimated_token=800,
            estimated_time=15
        )
        
        graph = TaskGraph(
            strategy=PlannerStrategy(mode="SEQUENTIAL"),
            nodes=[node1, node2]
        )
        logger.success(f"Task Graph generated with {len(graph.nodes)} nodes. Strategy: {graph.strategy.mode}")
        return graph
"""

registry_py = header + """
from loguru import logger
from typing import Callable, Dict, Any

class RouterRegistry:
    _routes: Dict[str, Callable] = {}
    
    @classmethod
    def register(cls, route_name: str):
        def decorator(func: Callable):
            if route_name in cls._routes:
                logger.warning(f"Route {route_name} is being overwritten in registry.")
            cls._routes[route_name] = func
            logger.debug(f"Registered route: {route_name}")
            return func
        return decorator
        
    @classmethod
    def get_route(cls, route_name: str) -> Callable:
        return cls._routes.get(route_name)
        
    @classmethod
    def list_routes(cls) -> list:
        return list(cls._routes.keys())
"""

dispatcher_py = header + """
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
"""

test_router_py = header + """
import pytest
from router.registry import RouterRegistry
from router.dispatcher import TaskRouter
from planner.agent import PlanningAgent

def test_registry_registration():
    routes = RouterRegistry.list_routes()
    assert "FileRouter" in routes
    assert "ToolRouter" in routes
    assert "ValidationRouter" in routes
    assert "ToolRouter::bash_execution" in routes

def test_dispatcher_routing():
    router = TaskRouter()
    result = router.dispatch("ToolRouter", {"tool_name": "grep_search"})
    assert "Handled by ToolRouter -> grep_search" in result

def test_dispatcher_unknown_route():
    router = TaskRouter()
    with pytest.raises(ValueError):
        router.dispatch("UnknownRouter", {})

@pytest.mark.asyncio
async def test_planning_agent_graph():
    agent = PlanningAgent()
    graph = await agent.create_plan("Build me an app")
    
    assert graph.strategy.mode in ["AUTO", "SEQUENTIAL", "CONCURRENT", "MIXED"]
    assert len(graph.nodes) > 0
    assert graph.nodes[0].task_id == "task_1"
"""

files = {
    "planner/prompts.py": prompts_py,
    "planner/agent.py": agent_py,
    "router/registry.py": registry_py,
    "router/dispatcher.py": dispatcher_py,
    "tests/test_router.py": test_router_py
}

for rel_path, content in files.items():
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)

print("Planner & Task Router Implementation Complete.")
