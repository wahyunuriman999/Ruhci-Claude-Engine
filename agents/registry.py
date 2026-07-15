# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from loguru import logger

class AgentRegistry:
    def __init__(self):
        self.agents = {}
    def register(self, role, agent):
        self.agents[role] = agent
        logger.info(f"Registered Agent: {role}")
