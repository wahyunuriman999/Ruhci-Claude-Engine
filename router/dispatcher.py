# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import Dict, Any, List, Optional
import time

class Dispatcher:
    """Main entry point for routing requests to the appropriate subsystem."""
    
    def __init__(self):
        self.routes: Dict[str, Any] = {}
        
    def register_route(self, intent: str, handler: Any) -> None:
        """Registers a handler for a specific intent type."""
        self.routes[intent] = handler
        
    def dispatch(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Analyzes a request and routes it to the registered handler."""
        intent = request.get("intent", "general")
        
        handler = self.routes.get(intent)
        if not handler:
            return {
                "status": "error",
                "message": f"No handler registered for intent: {intent}",
                "timestamp": time.time()
            }
            
        try:
            # Assumes handler has a handle() method
            response = handler.handle(request)
            return {
                "status": "success",
                "data": response,
                "timestamp": time.time()
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e),
                "timestamp": time.time()
            }
