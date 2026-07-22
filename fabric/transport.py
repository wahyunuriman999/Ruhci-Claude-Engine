# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from loguru import logger

class BaseTransport:
    def send(self, message):
        pass

class LocalTransport(BaseTransport):
    def send(self, message):
        logger.info(f"LocalTransport sending message: {message}")
        return True
