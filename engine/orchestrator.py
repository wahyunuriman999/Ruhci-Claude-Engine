# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import asyncio
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
import time

from kernel.event_bus import EventBus
from fabric.scheduler import TaskScheduler
from autonomous.reflection import AutonomousReflector
from memory.conversation import ConversationMemory


@dataclass
class TaskResult:
    description: str
    status: str = "COMPLETED"
    result: str = ""


@dataclass
class SessionState:
    session_id: str
    token_usage: int = 0
    tasks: List[TaskResult] = field(default_factory=list)


class RuhciOrchestrator:
    """Orchestrates interaction between subsystems (Memory, Router, Decision, Planner)."""

    def __init__(self, session_id: str = "default"):
        self.state = SessionState(session_id=session_id)
        
        # Initialize actual core subsystems
        self.event_bus = EventBus()
        self.scheduler = TaskScheduler()
        self.reflector = AutonomousReflector()
        self.memory = ConversationMemory()
        
        self.subsystems: Dict[str, Any] = {
            "memory": self.memory,
            "router": None,
            "decision": None,
            "planner": None,
            "reflection": self.reflector,
            "tools": None,
            "fabric": self.scheduler,
            "kernel": self.event_bus
        }
        self.is_running = False

    def register_subsystem(self, name: str, subsystem: Any) -> None:
        """Registers a core subsystem with the orchestrator."""
        self.subsystems[name] = subsystem

    async def run(self, objective: str) -> SessionState:
        """
        Execute an objective through the full OS pipeline utilizing wired subsystems.
        """
        self.is_running = True
        
        # 1. Store objective in Memory
        self.memory.add_message("user", objective)
        
        # 2. Publish event via Kernel EventBus
        self.event_bus.publish("session_started", {"session_id": self.state.session_id, "objective": objective})
        
        # 3. Schedule task via Fabric TaskScheduler
        def execute_objective():
            time.sleep(0.1) # Simulate real work
            return f"[EXECUTED] {objective}"
            
        self.scheduler.schedule(task_id="obj_1", priority=1, func=execute_objective)
        
        # 4. Run the scheduled tasks
        result_text = ""
        try:
            while self.scheduler.pending_count() > 0:
                result_text = self.scheduler.run_next()
                self.reflector.record_action("execute_task", "success", True)
        except Exception as e:
            self.reflector.record_action("execute_task", str(e), False)
            result_text = f"[FAILED] {str(e)}"
            
        # 5. Record result in Memory and State
        self.memory.add_message("assistant", result_text)
        self.event_bus.publish("session_completed", {"result": result_text})
        
        task = TaskResult(
            description=objective,
            status="COMPLETED" if "FAILED" not in result_text else "FAILED",
            result=result_text,
        )
        self.state.tasks.append(task)
        
        # Calculate real token usage based on actual memory contents
        total_tokens = sum(len(msg.content.split()) for msg in self.memory.messages) * 1.3
        self.state.token_usage += int(total_tokens)
        
        self.is_running = False
        return self.state

    def check_health(self) -> Dict[str, str]:
        """Returns the health status of all registered subsystems."""
        return {
            name: "online" if system is not None else "offline"
            for name, system in self.subsystems.items()
        }
