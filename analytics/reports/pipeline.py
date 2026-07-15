# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from loguru import logger

class PipelineReport:
    def __init__(self, claude_calls: int, input_tokens: int, optimized_tokens: int):
        self.claude_calls = claude_calls
        self.input_tokens = input_tokens
        self.optimized_tokens = optimized_tokens
        self.reduction = ((input_tokens - optimized_tokens) / input_tokens) * 100 if input_tokens > 0 else 0
        self.estimated_cost_saved = self.reduction * 0.8  # dummy heuristic
        
    def print_report(self):
        logger.info("=== Pipeline Report ===")
        logger.info(f"Claude Calls: {self.claude_calls}")
        logger.info(f"Input Tokens: {self.input_tokens}")
        logger.info(f"Optimized Tokens: {self.optimized_tokens}")
        logger.info(f"Reduction: {self.reduction:.2f}%")
        logger.info(f"Estimated Cost Saved: {self.estimated_cost_saved:.2f}%")
