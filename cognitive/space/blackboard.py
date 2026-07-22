# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import Dict, Any, List, Callable
import threading

class Blackboard:
    """A shared space for multiple agents/components to read and write state."""
    
    def __init__(self):
        self._state: Dict[str, Any] = {}
        self._lock = threading.RLock()
        self._subscribers: Dict[str, List[Callable]] = {}
        
    def write(self, key: str, value: Any) -> None:
        """Writes data to the blackboard and notifies subscribers."""
        with self._lock:
            self._state[key] = value
            self._notify(key, value)
            
    def read(self, key: str, default: Any = None) -> Any:
        """Reads data from the blackboard."""
        with self._lock:
            return self._state.get(key, default)
            
    def subscribe(self, key: str, callback: Callable) -> None:
        """Registers a callback to be executed when a key is updated."""
        with self._lock:
            if key not in self._subscribers:
                self._subscribers[key] = []
            self._subscribers[key].append(callback)
            
    def _notify(self, key: str, value: Any) -> None:
        """Internal method to trigger callbacks for a specific key."""
        if key in self._subscribers:
            for callback in self._subscribers[key]:
                try:
                    callback(key, value)
                except Exception:
                    # Log error in real implementation
                    pass
                    
    def snapshot(self) -> Dict[str, Any]:
        """Returns a copy of the entire blackboard state."""
        with self._lock:
            return dict(self._state)
