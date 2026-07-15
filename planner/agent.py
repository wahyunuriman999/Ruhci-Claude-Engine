# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

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
