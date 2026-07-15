# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from loguru import logger
from typing import Callable, Dict, Any

class RouterRegistry:
    _routes: Dict[str, Callable] = {}
    
    @classmethod
    def register(cls, route_name: str):
        def decorator(func: Callable):
            if route_name in cls._routes:
                logger.warning(f"Route {route_name} is being overwritten in registry.")
            cls._routes[route_name] = func
            logger.debug(f"Registered route: {route_name}")
            return func
        return decorator
        
    @classmethod
    def get_route(cls, route_name: str) -> Callable:
        return cls._routes.get(route_name)
        
    @classmethod
    def list_routes(cls) -> list:
        return list(cls._routes.keys())
