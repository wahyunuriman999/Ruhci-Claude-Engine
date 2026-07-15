# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from loguru import logger

class MissionRuntime:
    def __init__(self, objective):
        self.objective = objective
        self.phases = []
        self.milestones = []
        
    def add_milestone(self, name):
        self.milestones.append({"name": name, "status": "pending"})
        
    def complete_milestone(self, name):
        for m in self.milestones:
            if m["name"] == name:
                m["status"] = "completed"
                logger.info(f"Milestone {name} completed!")
