# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from loguru import logger
import time

class SoftSandbox:
    def __init__(self, timeout_sec=5):
        self.timeout_sec = timeout_sec
    
    def run(self, func, *args, **kwargs):
        start = time.time()
        logger.info("Sandbox started")
        result = func(*args, **kwargs)
        if time.time() - start > self.timeout_sec:
            logger.error("Sandbox Timeout Exceeded")
            raise TimeoutError("Execution took too long")
        return result
