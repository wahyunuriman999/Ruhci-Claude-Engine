# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from pydantic import BaseModel
from loguru import logger

class TokenAllocation(BaseModel):
    system: int = 15000
    skills: int = 10000
    context: int = 80000
    history: int = 25000
    tool: int = 20000
    response: int = 30000
    reserve: int = 20000
    
class BudgetManager:
    def __init__(self, total_budget: int = 200000):
        self.total = total_budget
        self.allocation = TokenAllocation()
        logger.info(f"BudgetManager initialized with {total_budget} tokens.")
        
    def can_fit(self, category: str, requested: int) -> bool:
        allowed = getattr(self.allocation, category, 0)
        return requested <= allowed
