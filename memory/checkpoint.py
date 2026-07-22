# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import time
from typing import Dict, Any, List

class CheckpointManager:
    """Creates and manages snapshots of the memory state to allow rollbacks."""
    
    def __init__(self):
        self.checkpoints: List[Dict[str, Any]] = []
        
    def create_checkpoint(self, state: Dict[str, Any], label: str = "") -> str:
        """Captures a snapshot of the current state."""
        checkpoint_id = f"ckpt_{int(time.time() * 1000)}"
        snapshot = {
            "id": checkpoint_id,
            "label": label,
            "timestamp": time.time(),
            "state": state
        }
        self.checkpoints.append(snapshot)
        return checkpoint_id
        
    def rollback_to(self, checkpoint_id: str) -> Dict[str, Any]:
        """Returns the state of a specific checkpoint and drops subsequent ones."""
        for i, ckpt in enumerate(self.checkpoints):
            if ckpt["id"] == checkpoint_id:
                state = ckpt["state"]
                # Truncate history after this checkpoint
                self.checkpoints = self.checkpoints[:i+1]
                return state
        raise ValueError(f"Checkpoint {checkpoint_id} not found.")
        
    def get_history(self) -> List[Dict[str, Any]]:
        """Returns metadata for all available checkpoints."""
        return [{"id": c["id"], "label": c["label"], "timestamp": c["timestamp"]} for c in self.checkpoints]
