# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from loguru import logger

class CommandBus:
    def __init__(self):
        self.handlers = {}
    def register(self, command_type, handler):
        self.handlers[command_type] = handler
    def execute(self, command_type, data):
        logger.info(f"CommandBus executing: {command_type}")
        if command_type in self.handlers:
            return self.handlers[command_type](data)
        raise ValueError(f"No handler for command {command_type}")
