# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from loguru import logger

class ContextWindow:
    def __init__(self, max_tokens: int = 150000):
        self.max_tokens = max_tokens
        self.current_tokens = 0
        
    def fits(self, estimated_tokens: int) -> bool:
        return (self.current_tokens + estimated_tokens) <= self.max_tokens
        
    def add(self, tokens: int):
        self.current_tokens += tokens
        logger.debug(f"Context Window updated: {self.current_tokens}/{self.max_tokens}")
