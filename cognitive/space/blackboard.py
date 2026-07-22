# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from loguru import logger

class SharedWorkspace:
    def __init__(self):
        self.goal = ""
        self.plan = ""
        self.context = ""
        self.risks = []
        self.assumptions = []
        self.open_questions = []
        
    def write_proposal(self, agent_role, proposal):
        logger.info(f"{agent_role} wrote a proposal to the Blackboard.")
        
    def read_context(self):
        return self.context
