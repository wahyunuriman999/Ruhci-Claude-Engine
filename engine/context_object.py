# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import copy
from typing import Any
from pydantic import BaseModel, ConfigDict
from loguru import logger

class ExecutionContext(BaseModel):
    model_config = ConfigDict(frozen=True)  # Immutable Snapshot
    
    user_objective: str = ""
    planning_result: Any = None
    repository_snapshot: Any = None
    knowledge_facts: Any = None
    token_budget: Any = None
    confidence: Any = None
    metadata: dict = {}
    
    def clone(self, **kwargs):
        logger.debug("Cloning ExecutionContext for immutability")
        new_data = self.model_dump()
        new_data.update(kwargs)
        return ExecutionContext(**new_data)
