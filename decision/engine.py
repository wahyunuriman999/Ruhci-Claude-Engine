# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import Dict, Any, List
from .confidence import ConfidenceScorer
from .consensus import ConsensusEngine
from policy.ponytail import PonytailPolicy
from policy.profiles import EnginePolicy

class DecisionEngine:
    """Orchestrates the decision-making process for the agent."""
    
    def __init__(self, policy: EnginePolicy = None):
        self.scorer = ConfidenceScorer()
        self.consensus = ConsensusEngine()
        self.policy = policy or EnginePolicy()
        self.ponytail_evaluator = PonytailPolicy() if self.policy.ponytail_mode else None
        
    def make_decision(self, context: Dict[str, Any], possible_actions: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Evaluates possible actions against the current context and returns the best decision.
        """
        if not possible_actions:
            return {"action": "wait", "reason": "No actions available."}
            
        evaluated_actions = []
        for action in possible_actions:
            # Fake evidence evaluation for now
            evidence = context.get("relevant_items", [])
            certainty = action.get("model_certainty", 0.5)
            
            conf_result = self.scorer.evaluate(evidence, certainty)
            
            # Apply Ponytail penalty if active
            penalty = 1.0
            if self.ponytail_evaluator:
                penalty = self.ponytail_evaluator.evaluate_action(action)
            
            action_copy = dict(action)
            action_copy["score"] = conf_result["score"] * penalty
            
            # Demote confidence if score drops below threshold due to penalty
            if penalty < 1.0 and action_copy["score"] < self.policy.confidence_threshold:
                action_copy["is_confident"] = False
            else:
                action_copy["is_confident"] = conf_result["is_confident"]
                
            evaluated_actions.append(action_copy)
            
        # Filter to confident actions
        confident_actions = [a for a in evaluated_actions if a["is_confident"]]
        
        if not confident_actions:
            return {"action": "ask_human", "reason": "No confident actions available."}
            
        # Build consensus among confident actions
        decision = self.consensus.reach_consensus(confident_actions)
        
        return decision
