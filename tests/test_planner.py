# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
import pytest\nfrom planner.agent import PlanningAgent\n@pytest.mark.asyncio\nasync def test_planner():\n    agent = PlanningAgent()\n    res = await agent.create_plan('x')\n    assert res.strategy == 'ADAPTIVE'