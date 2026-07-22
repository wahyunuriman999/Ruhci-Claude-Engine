# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from loguru import logger

class ModelRegistry:
    MODELS = {
        "claude-opus": {"quality": "high", "cost": "high", "speed": "medium"},
        "claude-sonnet": {"quality": "high", "cost": "medium", "speed": "high"},
        "claude-haiku": {"quality": "medium", "cost": "low", "speed": "very_high"}
    }
    
    def resolve_model(self, req_speed: str) -> str:
        for m, meta in self.MODELS.items():
            if meta["speed"] == req_speed:
                return m
        return "claude-sonnet"
