# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
from engine.state_machine import StateMachine, EngineState\ndef test_suspend():\n    sm = StateMachine()\n    sm.transition(EngineState.SUSPENDED)\n    assert sm.state == EngineState.SUSPENDED