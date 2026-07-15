# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import pytest
import asyncio
from engine.orchestrator import RuhciOrchestrator

@pytest.mark.asyncio
async def test_orchestrator_initialization():
    orchestrator = RuhciOrchestrator(session_id="test-session")
    assert orchestrator.state.session_id == "test-session"
    assert orchestrator.state.token_usage == 0

@pytest.mark.asyncio
async def test_orchestrator_run_loop():
    orchestrator = RuhciOrchestrator(session_id="test-session")
    final_state = await orchestrator.run("Create a hello world function")
    
    assert len(final_state.tasks) == 1
    assert final_state.tasks[0].status == "COMPLETED"
    assert "[REVIEWED]" in final_state.tasks[0].result
    assert final_state.token_usage > 0
