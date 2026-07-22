# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from loguru import logger

class RuntimeWorker:
    def __init__(self, worker_id, capabilities):
        self.worker_id = worker_id
        self.capabilities = capabilities
        self.load = 0.0
        self.health = "OK"
