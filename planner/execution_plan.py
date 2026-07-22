# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
import time

@dataclass
class Task:
    id: str
    description: str
    status: str = "pending"  # pending, in_progress, completed, failed
    dependencies: List[str] = field(default_factory=list)
    result: Optional[Any] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "dependencies": self.dependencies,
            "result": self.result
        }

class ExecutionPlan:
    """Manages the state of a multi-step execution plan."""
    
    def __init__(self, plan_id: str, objective: str):
        self.plan_id = plan_id
        self.objective = objective
        self.tasks: Dict[str, Task] = {}
        self.created_at = time.time()
        
    def add_task(self, task: Task) -> None:
        """Adds a task to the execution plan."""
        self.tasks[task.id] = task
        
    def get_next_runnable_tasks(self) -> List[Task]:
        """Returns all pending tasks whose dependencies are completed."""
        runnable = []
        for task in self.tasks.values():
            if task.status == "pending":
                if all(self.tasks[dep].status == "completed" for dep in task.dependencies):
                    runnable.append(task)
        return runnable
        
    def update_task_status(self, task_id: str, status: str, result: Optional[Any] = None) -> None:
        """Updates the status and result of a specific task."""
        if task_id in self.tasks:
            self.tasks[task_id].status = status
            if result is not None:
                self.tasks[task_id].result = result
                
    def is_complete(self) -> bool:
        """Returns True if all tasks are completed."""
        if not self.tasks:
            return False
        return all(t.status == "completed" for t in self.tasks.values())
        
    def to_dict(self) -> Dict[str, Any]:
        """Serializes the entire plan."""
        return {
            "plan_id": self.plan_id,
            "objective": self.objective,
            "tasks": [t.to_dict() for t in self.tasks.values()],
            "is_complete": self.is_complete()
        }
