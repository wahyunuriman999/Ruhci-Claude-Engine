# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from enum import Enum
from loguru import logger

class EngineState(Enum):
    BOOT = "BOOT"
    INITIALIZE = "INITIALIZE"
    INDEX = "INDEX"
    ANALYZE = "ANALYZE"
    PLAN = "PLAN"
    PREPARE = "PREPARE"
    EXECUTE = "EXECUTE"
    VALIDATE = "VALIDATE"
    REFLECT = "REFLECT"
    DECIDE = "DECIDE"
    CHECKPOINT = "CHECKPOINT"
    CONTINUE = "CONTINUE"
    FINISHED = "FINISHED"
    RECOVERY = "RECOVERY"
    REPLAN = "REPLAN"
    SUSPENDED = "SUSPENDED"
    RESUME = "RESUME"

class StateMachine:
    def __init__(self):
        self.state = EngineState.BOOT
        
    def transition(self, next_state: EngineState):
        logger.info(f"State transition: {self.state.name} -> {next_state.name}")
        self.state = next_state
