# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from decision.engine import DecisionEngine
from policy.profiles import get_ponytail_profile, EnginePolicy
from prompts import PONYTAIL_SYSTEM_PROMPT

def test_ponytail_evaluator():
    # Load decision engine with ponytail mode
    policy = get_ponytail_profile().policy
    engine = DecisionEngine(policy=policy)
    
    # 1. Action that writes large custom code
    bad_action = {
        "type": "write_file",
        "description": "Write a huge custom datepicker framework from scratch",
        "model_certainty": 0.9
    }
    
    # 2. Action that uses a one-liner
    good_action = {
        "type": "write_file",
        "description": "Use native HTML input type=date one-liner",
        "model_certainty": 0.9
    }
    
    # Context with enough fake evidence to pass the base 0.85 threshold
    context = {"relevant_items": ["f1.py", "f2.py", "f3.py", "f4.py", "f5.py"]}
    
    # Let's see what happens to the confidence score of bad action
    decision_bad = engine.make_decision(context, [bad_action])
    decision_good = engine.make_decision(context, [good_action])
    
    # The bad action should be penalized and not confident, 
    # making the decision fall back to "ask_human" or "wait" if no confident actions
    assert decision_bad.get("action") in ["ask_human", "wait"]
    
    # The good action should pass and be chosen
    assert decision_good.get("status") == "success"
    # Wait, the action dict itself didn't have 'action', it had 'type'. ConsensusEngine copies 'action'.
    # We just care that it succeeded.
    
    # Ensure system prompt is loaded properly
    assert "laziest" in PONYTAIL_SYSTEM_PROMPT.lower()
