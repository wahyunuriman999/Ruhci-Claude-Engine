# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import Any, Callable, Dict


class CommandBus:
    """Pub-sub style command dispatcher."""

    def __init__(self):
        self._handlers: Dict[str, Callable] = {}

    def register_handler(self, command_type: str, handler: Callable) -> None:
        """Register a handler for the given command type."""
        self._handlers[command_type] = handler

    def dispatch(self, command: Dict) -> Any:
        """Route a command dict to its registered handler."""
        cmd_type = command.get("type")
        if not cmd_type:
            raise ValueError("Command must have a 'type' key.")
        handler = self._handlers.get(cmd_type)
        if handler is None:
            raise ValueError(f"No handler registered for command type: '{cmd_type}'")
        return handler(command)

    def registered_types(self):
        return list(self._handlers.keys())
