# ==========================================
# AEGIS COGNITIVE RUNTIME PLATFORM
# PROPRIETARY AND CONFIDENTIAL
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import os
import sys

# Tambahkan root directory ke sys.path untuk import ruhci
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from ruhci.agents import AgentContext, AgentResult, RuhciAgent, AgentRegistry

@AgentRegistry.register("mock_planner")
class MockPlannerAgent(RuhciAgent):
    def observe(self, context: AgentContext) -> None:
        context.memory.append({"step": "observe", "status": "done"})
        context.state["observed_data"] = "data_from_repo"
        
    def plan(self, context: AgentContext) -> dict:
        context.memory.append({"step": "plan", "status": "done"})
        return {"action": "refactor", "target": context.state["observed_data"]}
        
    def execute(self, context: AgentContext, plan_data: dict) -> dict:
        context.memory.append({"step": "execute", "status": "done"})
        return {"refactored": True, "target": plan_data["target"]}
        
    def reflect(self, context: AgentContext, execution_data: dict) -> AgentResult:
        context.memory.append({"step": "reflect", "status": "done"})
        if execution_data["refactored"]:
            return AgentResult(success=True, data={"final": "success"}, metrics={"score": 1.0})
        return AgentResult(success=False)

def test_agent_pipeline():
    print("Testing AEGIS Elite Agent Pipeline...")
    
    agent = AgentRegistry.get_agent("mock_planner")
    assert agent is not None, "Gagal mendapatkan agent dari registry"
    
    context = AgentContext(
        task_id="task_001",
        query="Fix tests",
        repository_path="/fake/repo"
    )
    
    result = agent.run(context)
    
    print("Result Success:", result.success)
    print("Result Data:", result.data)
    print("Result Metrics:", result.metrics)
    print("Agent Memory Log:")
    for m in context.memory:
        print("  -", m)
        
    assert result.success is True
    assert len(context.memory) == 4
    assert context.memory[0]["step"] == "observe"
    assert context.memory[1]["step"] == "plan"
    assert context.memory[2]["step"] == "execute"
    assert context.memory[3]["step"] == "reflect"
    
    print("[SUCCESS] All AEGIS Ticks (OBSERVE -> PLAN -> EXECUTE -> REFLECT) executed sequentially!")

if __name__ == "__main__":
    test_agent_pipeline()
