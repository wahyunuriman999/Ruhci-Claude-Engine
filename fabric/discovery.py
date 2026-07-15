# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from loguru import logger

class NodeRegistry:
    def __init__(self):
        self.nodes = {}
    
    def register(self, node_id, capabilities, health):
        logger.info(f"Registering node {node_id} with capabilities {capabilities}")
        self.nodes[node_id] = {"capabilities": capabilities, "health": health}
