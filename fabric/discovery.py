# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import time
from typing import Any, Dict, List


class ServiceDiscovery:
    """Service registry with capability-based lookup and heartbeat tracking."""

    def __init__(self):
        self._services: Dict[str, Dict[str, Any]] = {}

    def register_service(self, name: str, endpoint: str, capabilities: List[str]) -> None:
        self._services[name] = {
            "endpoint": endpoint,
            "capabilities": capabilities,
            "last_seen": time.time(),
        }

    def discover(self, capability: str) -> List[str]:
        """Return names of all services that expose the requested capability."""
        return [
            name
            for name, meta in self._services.items()
            if capability in meta.get("capabilities", [])
        ]

    def heartbeat(self, name: str) -> bool:
        """Update the last_seen timestamp for a service. Returns False if unknown."""
        if name not in self._services:
            return False
        self._services[name]["last_seen"] = time.time()
        return True

    def deregister(self, name: str) -> None:
        self._services.pop(name, None)

    def all_services(self) -> Dict[str, Dict]:
        return dict(self._services)
