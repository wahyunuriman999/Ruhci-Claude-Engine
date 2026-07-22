# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import Dict, Any, List, Optional

class SelfEvaluator:
    """Evaluates the outcome of actions and determines if they succeeded or failed."""
    
    def __init__(self):
        pass
        
    def evaluate_result(self, intent: str, action_taken: str, output: Any, expected_state: Optional[Any] = None) -> Dict[str, Any]:
        """
        Analyzes the result of an action against expectations.
        """
        # Naive keyword-based failure detection
        output_str = str(output).lower()
        has_error = any(kw in output_str for kw in ["error", "exception", "failed", "traceback", "not found"])
        
        if has_error:
            return {
                "success": False,
                "reason": "Detected error keywords in output.",
                "severity": "high"
            }
            
        return {
            "success": True,
            "reason": "Action completed without detectable errors.",
            "severity": "none"
        }
