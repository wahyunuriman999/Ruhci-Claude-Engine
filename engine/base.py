# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from abc import ABC, abstractmethod
from typing import Any, Dict

class BasePlanner(ABC):
    @abstractmethod
    async def create_plan(self, prompt: str) -> Any:
        pass

class BaseRouter(ABC):
    @abstractmethod
    def route(self, task: Any) -> str:
        pass

class BaseDispatcher(ABC):
    @abstractmethod
    def dispatch(self, route_target: str, context: Dict[str, Any]) -> Any:
        pass

class BaseExecutor(ABC):
    @abstractmethod
    async def execute(self, task: Any) -> Any:
        pass

class BaseValidator(ABC):
    @abstractmethod
    def validate(self, result: Any) -> bool:
        pass

class BaseSkill(ABC):
    @abstractmethod
    def execute_skill(self, context: Dict[str, Any]) -> Any:
        pass

class BaseTool(ABC):
    @abstractmethod
    def run_tool(self, **kwargs) -> Any:
        pass
