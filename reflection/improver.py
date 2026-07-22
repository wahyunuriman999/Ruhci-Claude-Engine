# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import Dict, Any, List, Optional
from .evaluator import SelfEvaluator

class SelfImprover:
    """Takes evaluation feedback and modifies the plan or context to try again."""
    
    def __init__(self):
        self.evaluator = SelfEvaluator()
        
    def generate_correction(self, failed_action: Dict[str, Any], evaluation: Dict[str, Any]) -> Dict[str, Any]:
        """
        Suggests a corrected action or prompts for additional context based on failure.
        """
        reason = evaluation.get("reason", "")
        
        # Naive correction strategies
        if "not found" in reason.lower():
            return {
                "strategy": "search_broader",
                "instruction": "The required element was not found. Try searching globally or asking for the exact file path."
            }
        elif "syntax" in reason.lower() or "exception" in reason.lower():
            return {
                "strategy": "fix_code",
                "instruction": "There was a code execution error. Analyze the traceback, fix the syntax, and retry."
            }
        else:
            return {
                "strategy": "re-evaluate",
                "instruction": "General failure detected. Stop and ask the human for clarification."
            }
