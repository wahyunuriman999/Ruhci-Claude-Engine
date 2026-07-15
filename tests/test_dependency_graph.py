# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
from planner.agent import PlanningResult\ndef test_graph():\n    pr = PlanningResult(objective='x')\n    assert isinstance(pr.dependency_graph, dict)