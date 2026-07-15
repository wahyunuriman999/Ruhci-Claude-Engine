# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from pydantic import BaseModel
from typing import List

class StrategyMetadata(BaseModel):
    name: str
    cost: str
    latency: str
    accuracy: str
    recommended_for: List[str]

class BaseStrategy:
    metadata: StrategyMetadata

class ArchitectureStrategy(BaseStrategy):
    metadata = StrategyMetadata(
        name="Architecture Strategy",
        cost="high", latency="slow", accuracy="high",
        recommended_for=["refactor", "redesign", "review"]
    )
