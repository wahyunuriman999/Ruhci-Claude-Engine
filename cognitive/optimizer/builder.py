# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import List, Dict, Any
from .budget import TokenBudgetManager

class ContextBuilder:
    """Assembles prompt context dynamically while strictly adhering to token budgets."""
    
    def __init__(self, budget_manager: TokenBudgetManager):
        self.budget = budget_manager
        
    def build_context(self, prioritized_items: List[Dict[str, Any]]) -> str:
        """
        Greedily packs items into a context string until the budget is exhausted.
        Assumes each item has 'content' and 'estimated_tokens'.
        """
        assembled_blocks = []
        
        for item in prioritized_items:
            tokens = item.get("estimated_tokens", 0)
            if self.budget.consume(tokens):
                assembled_blocks.append(item.get("content", ""))
            else:
                # Stop assembling if the next most important item doesn't fit
                break
                
        return "\n\n".join(assembled_blocks)
