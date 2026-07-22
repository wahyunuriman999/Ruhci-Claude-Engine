# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from loguru import logger

class ServiceRegistry:
    def __init__(self):
        self.services = {}
    def register(self, name, service):
        self.services[name] = service
        logger.info(f"Registered service: {name}")
    def get(self, name):
        return self.services.get(name)
