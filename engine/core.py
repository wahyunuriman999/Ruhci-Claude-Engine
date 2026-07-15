# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class Task(BaseModel):
    id: str
    description: str
    status: str = "PENDING"
    priority: int = 1
    result: Optional[str] = None

class ExecutionConfig(BaseModel):
    max_tokens: int = 8000
    model_name: str = "claude-3-5-sonnet-20240620"
    temperature: float = 0.0
    debug_mode: bool = False

class EngineState(BaseModel):
    session_id: str
    config: ExecutionConfig = Field(default_factory=ExecutionConfig)
    tasks: List[Task] = Field(default_factory=list)
    memory_context: Dict[str, Any] = Field(default_factory=dict)
    token_usage: int = 0
    
    def get_pending_tasks(self) -> List[Task]:
        return [t for t in self.tasks if t.status == "PENDING"]
