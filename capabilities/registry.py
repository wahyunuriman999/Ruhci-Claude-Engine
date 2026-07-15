# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from loguru import logger

class CapabilityRegistry:
    def __init__(self):
        self.installed = ["python", "typescript", "json", "dockerfile"]
        
    def detect(self, repo_path: str):
        logger.info("Building Capability Graph (Python, Docker, MCP, React, etc.)")
        return ["python", "docker"]
