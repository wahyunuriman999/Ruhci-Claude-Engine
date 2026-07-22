# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import Dict, Any, List
import time

class CognitiveStateManager:
    """Manages overarching cognitive state transitions and snapshots across segments."""
    
    def __init__(self):
        self.history: List[Dict[str, Any]] = []
        
    def capture_state(self, blackboard_snapshot: Dict[str, Any], segments_snapshot: Dict[str, Any]) -> str:
        """Takes a full snapshot of the cognitive apparatus."""
        state_id = f"cog_{int(time.time() * 1000)}"
        self.history.append({
            "id": state_id,
            "timestamp": time.time(),
            "blackboard": blackboard_snapshot,
            "segments": segments_snapshot
        })
        return state_id
        
    def get_state(self, state_id: str) -> Dict[str, Any]:
        """Retrieves a specific cognitive state by ID."""
        for state in self.history:
            if state["id"] == state_id:
                return state
        raise KeyError(f"Cognitive state {state_id} not found.")
