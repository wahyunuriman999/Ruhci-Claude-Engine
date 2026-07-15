# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from enum import Enum
from loguru import logger

class Decision(Enum):
    CONTINUE = "CONTINUE"
    RETRY = "RETRY"
    ROLLBACK = "ROLLBACK"
    FORK = "FORK"
    REPLAN = "REPLAN"
    ASK_USER = "ASK_USER"
    STOP = "STOP"

class DecisionEngine:
    def evaluate(self, confidence, policy) -> Decision:
        logger.info("DecisionEngine evaluating based on Policy and Confidence.")
        if confidence.score < policy.confidence_threshold:
            return Decision.REPLAN
        return Decision.CONTINUE
