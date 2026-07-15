# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
from planner.agent import PlanningResult\ndef test_strategy():\n    pr = PlanningResult(objective='x')\n    assert pr.strategy == 'ADAPTIVE'