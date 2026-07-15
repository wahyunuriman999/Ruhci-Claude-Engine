# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from loguru import logger

class ConsensusEngine:
    def resolve(self, proposals):
        logger.info("ConsensusEngine resolving conflicting proposals...")
        # Voting -> Confidence -> Policy -> Decision
        best_proposal = max(proposals, key=lambda p: p.get('confidence', 0))
        logger.info(f"Consensus reached. Winner: {best_proposal['agent']}")
        return best_proposal
