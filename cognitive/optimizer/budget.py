# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

class TokenBudgetManager:
    """Tracks and enforces LLM context window limits."""
    
    def __init__(self, max_tokens: int = 150000):
        self.max_tokens = max_tokens
        self.current_usage = 0
        self.reserves = {
            "system_prompt": 2000,
            "safety_margin": 1000,
            "output_generation": 4000
        }
        
    @property
    def available_context(self) -> int:
        """Calculates how many tokens are available for dynamic context."""
        reserved = sum(self.reserves.values())
        return max(0, self.max_tokens - reserved - self.current_usage)
        
    def consume(self, tokens: int) -> bool:
        """Attempts to consume tokens. Returns False if budget exceeded."""
        if tokens > self.available_context:
            return False
        self.current_usage += tokens
        return True
        
    def release(self, tokens: int) -> None:
        """Frees up token budget."""
        self.current_usage = max(0, self.current_usage - tokens)
        
    def reset(self) -> None:
        """Resets the usage tracker."""
        self.current_usage = 0
