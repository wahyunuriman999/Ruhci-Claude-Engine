# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import json
from pathlib import Path
from typing import Dict, Any, Optional

class MemoryRepository:
    """Interface for saving and loading memory state to/from disk."""
    
    def __init__(self, storage_path: str = ".ruhci/memory/"):
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(parents=True, exist_ok=True)
        
    def save_state(self, session_id: str, data: Dict[str, Any]) -> str:
        """Serializes and saves memory state to a JSON file."""
        file_path = self.storage_path / f"{session_id}.json"
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        return str(file_path)
        
    def load_state(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Loads and deserializes memory state from a JSON file."""
        file_path = self.storage_path / f"{session_id}.json"
        if not file_path.exists():
            return None
            
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return None
            
    def list_sessions(self) -> list[str]:
        """Returns a list of saved session IDs."""
        return [f.stem for f in self.storage_path.glob("*.json")]
