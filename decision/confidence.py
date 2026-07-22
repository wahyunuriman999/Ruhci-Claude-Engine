# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import Dict, Any, List

class ConfidenceScorer:
    """Evaluates the confidence level of a proposed agent action."""
    
    def __init__(self, threshold: float = 0.75):
        self.threshold = threshold
        
    def evaluate(self, evidence_items: List[Dict[str, Any]], model_certainty: float = 0.5) -> Dict[str, Any]:
        """
        Calculates a confidence score based on concrete evidence and model certainty.
        """
        if not evidence_items:
            base_score = 0.1
        else:
            # Score scales logarithmically with the amount of evidence
            base_score = min(0.9, 0.3 + (len(evidence_items) * 0.15))
            
        final_score = (base_score * 0.7) + (model_certainty * 0.3)
        
        return {
            "score": final_score,
            "is_confident": final_score >= self.threshold,
            "threshold": self.threshold
        }
