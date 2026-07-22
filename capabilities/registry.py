# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import Any, Callable, Dict, List, Optional


class CapabilityRegistry:
    """Central registry for all system capabilities."""

    def __init__(self):
        self._caps: Dict[str, Dict] = {}

    def register(
        self,
        name: str,
        description: str,
        handler: Optional[Callable] = None,
        metadata: Optional[Dict] = None,
    ) -> None:
        self._caps[name] = {
            "description": description,
            "handler": handler,
            "metadata": metadata or {},
        }

    def get(self, name: str) -> Optional[Dict]:
        return self._caps.get(name)

    def list_all(self) -> List[str]:
        return list(self._caps.keys())

    def invoke(self, name: str, **kwargs) -> Any:
        cap = self._caps.get(name)
        if cap is None:
            raise KeyError(f"Capability '{name}' not registered.")
        if cap["handler"] is None:
            raise RuntimeError(f"Capability '{name}' has no handler.")
        return cap["handler"](**kwargs)
