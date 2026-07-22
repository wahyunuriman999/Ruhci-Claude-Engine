# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import hashlib
import json
from typing import Any

class StateFingerprint:
    """Generates deterministic hashes for cognitive states to identify duplication or cycles."""
    
    @staticmethod
    def generate(state_dict: dict[str, Any]) -> str:
        """Creates an MD5 hash representing the normalized JSON of a state dictionary."""
        # Sort keys to ensure deterministic ordering
        try:
            serialized = json.dumps(state_dict, sort_keys=True, separators=(',', ':'))
            return hashlib.md5(serialized.encode('utf-8')).hexdigest()
        except TypeError:
            # Fallback if state contains non-serializable objects
            return hashlib.md5(str(state_dict).encode('utf-8')).hexdigest()
