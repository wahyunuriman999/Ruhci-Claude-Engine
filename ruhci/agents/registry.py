# ==========================================
# AEGIS COGNITIVE RUNTIME PLATFORM
# PROPRIETARY AND CONFIDENTIAL
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import Dict, Type, Optional
from loguru import logger
from .base import RuhciAgent

class AgentRegistry:
    """
    Registry pusat untuk mendaftarkan dan memanggil agen-agen secara dinamis.
    """
    _agents: Dict[str, Type[RuhciAgent]] = {}

    @classmethod
    def register(cls, name: str):
        """
        Dekorator untuk mendaftarkan class agen ke dalam registry.
        """
        def wrapper(agent_class: Type[RuhciAgent]):
            if not issubclass(agent_class, RuhciAgent):
                raise ValueError(f"Class {agent_class.__name__} must inherit from RuhciAgent")
            
            if name in cls._agents:
                logger.warning(f"Overwriting existing agent registration for '{name}'")
                
            cls._agents[name] = agent_class
            logger.debug(f"Agent '{name}' registered successfully.")
            return agent_class
        return wrapper

    @classmethod
    def get_agent(cls, name: str, **kwargs) -> Optional[RuhciAgent]:
        """
        Menginstansiasi dan mengembalikan agen berdasarkan namanya.
        """
        agent_class = cls._agents.get(name)
        if not agent_class:
            logger.error(f"Agent '{name}' not found in registry.")
            return None
            
        return agent_class(name=name, **kwargs)
        
    @classmethod
    def list_agents(cls) -> list[str]:
        return list(cls._agents.keys())
