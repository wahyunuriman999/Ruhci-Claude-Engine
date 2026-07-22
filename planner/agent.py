# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import Dict, Any, Optional
import uuid
from .task_breakdown import TaskBreakdownEngine
from .execution_plan import ExecutionPlan
from .priority import TaskPrioritizer

class PlannerAgent:
    """Agent responsible for creating and overseeing the execution of plans."""
    
    def __init__(self):
        self.breakdown_engine = TaskBreakdownEngine()
        self.prioritizer = TaskPrioritizer()
        self.active_plans: Dict[str, ExecutionPlan] = {}
        
    def create_plan(self, objective: str) -> str:
        """Creates a new execution plan for the given objective and returns its ID."""
        plan_id = str(uuid.uuid4())
        plan = self.breakdown_engine.breakdown(objective, plan_id)
        self.active_plans[plan_id] = plan
        return plan_id
        
    def get_next_step(self, plan_id: str) -> Optional[Dict[str, Any]]:
        """Gets the next highest-priority task to execute."""
        plan = self.active_plans.get(plan_id)
        if not plan or plan.is_complete():
            return None
            
        runnable = plan.get_next_runnable_tasks()
        if not runnable:
            return None
            
        prioritized = self.prioritizer.prioritize(runnable)
        return prioritized[0].to_dict()
        
    def report_result(self, plan_id: str, task_id: str, status: str, result: Any = None) -> None:
        """Reports the result of a task back to the plan."""
        plan = self.active_plans.get(plan_id)
        if plan:
            plan.update_task_status(task_id, status, result)
