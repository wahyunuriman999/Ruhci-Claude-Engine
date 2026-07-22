# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import threading
from typing import Any, Dict, List


class _KernelRegistryMeta(type):
    """Metaclass ensuring KernelRegistry is a singleton."""
    _instance = None
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class KernelRegistry(metaclass=_KernelRegistryMeta):
    """Thread-safe singleton registry for kernel-level services."""

    def __init__(self):
        self._services: Dict[str, Any] = {}
        self._lock = threading.Lock()

    def register(self, name: str, service: Any) -> None:
        with self._lock:
            self._services[name] = service

    def get(self, name: str) -> Any:
        with self._lock:
            return self._services.get(name)

    def list_services(self) -> List[str]:
        with self._lock:
            return list(self._services.keys())

    def unregister(self, name: str) -> None:
        with self._lock:
            self._services.pop(name, None)
