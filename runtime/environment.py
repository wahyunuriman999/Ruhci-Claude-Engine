# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import os
from typing import Dict, Any

class RuntimeEnvironment:
    """Manages environment variables, secrets, and configuration for the runtime."""
    
    def __init__(self):
        self.config: Dict[str, Any] = {}
        self.load_defaults()
        
    def load_defaults(self) -> None:
        """Loads basic system defaults."""
        self.config["MAX_CONCURRENT_AGENTS"] = 5
        self.config["SANDBOX_TIMEOUT"] = 60
        self.config["WORKSPACE_DIR"] = os.getcwd()
        
    def set_var(self, key: str, value: Any) -> None:
        """Sets a runtime configuration variable."""
        self.config[key] = value
        
    def get_var(self, key: str, default: Any = None) -> Any:
        """Gets a runtime configuration variable."""
        return self.config.get(key, default)
