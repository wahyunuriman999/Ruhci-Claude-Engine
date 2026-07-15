# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from loguru import logger
from typing import Callable, Dict

class UniversalRegistry:
    _registry: Dict[str, Dict[str, Callable]] = {
        "Router": {},
        "Planner": {},
        "Skill": {},
        "Tool": {},
        "Workflow": {},
        "Validator": {}
    }
    
    @classmethod
    def _register(cls, category: str, name: str):
        def decorator(func: Callable):
            if name in cls._registry[category]:
                logger.warning(f"{category} '{name}' is being overwritten.")
            cls._registry[category][name] = func
            logger.debug(f"Registered {category}: {name}")
            return func
        return decorator

    @classmethod
    def get(cls, category: str, name: str) -> Callable:
        return cls._registry.get(category, {}).get(name)

class Registry:
    @staticmethod
    def Router(name: str): return UniversalRegistry._register("Router", name)
    
    @staticmethod
    def Planner(name: str): return UniversalRegistry._register("Planner", name)
    
    @staticmethod
    def Skill(name: str): return UniversalRegistry._register("Skill", name)
    
    @staticmethod
    def Tool(name: str): return UniversalRegistry._register("Tool", name)
    
    @staticmethod
    def Workflow(name: str): return UniversalRegistry._register("Workflow", name)
    
    @staticmethod
    def Validator(name: str): return UniversalRegistry._register("Validator", name)
