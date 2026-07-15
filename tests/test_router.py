# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

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
