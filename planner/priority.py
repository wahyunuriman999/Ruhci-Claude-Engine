# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import List
from .execution_plan import Task

class TaskPrioritizer:
    """Prioritizes tasks within an execution plan."""
    
    def __init__(self):
        pass
        
    def prioritize(self, tasks: List[Task]) -> List[Task]:
        """
        Sorts runnable tasks by priority. 
        In this naive implementation, it just sorts alphabetically by ID.
        """
        return sorted(tasks, key=lambda t: t.id)
