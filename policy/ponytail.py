# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import Dict, Any

class PonytailPolicy:
    """
    Implements the 'Ponytail' mindset: 
    The best code is the code you never wrote.
    
    Ladder of evaluation:
    1. YAGNI (Does this need to exist?)
    2. Reuse (Already in codebase?)
    3. Stdlib (Stdlib does it?)
    4. Native (Native platform feature?)
    5. Dependency (Installed dependency?)
    6. One-liner (One line?)
    7. Minimum (Only then: the minimum that works)
    """

    def evaluate_action(self, action: Dict[str, Any]) -> float:
        """
        Evaluates a proposed action and returns a penalty multiplier (0.0 to 1.0).
        1.0 means no penalty (passes Ponytail criteria).
        Lower values mean heavy penalty (over-engineered).
        """
        action_type = action.get("type", "unknown")
        description = action.get("description", "").lower()
        
        # We assume actions that don't involve writing code are fine.
        if action_type not in ["write_file", "modify_file", "create_component"]:
            return 1.0
            
        # If the action proposes a lot of new code, penalize heavily 
        # unless it explicitly mentions it checked native/stdlib features.
        is_large_write = "custom" in description or "new component" in description or "framework" in description
        checked_native = "native" in description or "stdlib" in description or "built-in" in description or "reuse" in description
        
        if is_large_write and not checked_native:
            # Huge penalty for trying to build custom things without checking native first
            return 0.3
            
        if "one line" in description or "one-liner" in description:
            # Bonus (no penalty) for one-liners
            return 1.0
            
        # Default mild penalty for writing code to encourage looking for existing solutions
        return 0.8
