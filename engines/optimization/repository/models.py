# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class Evidence:
    type: str          # e.g., "Import", "AST_Class", "Regex"
    source: str        # e.g., "main.py"
    description: str   # e.g., "FastAPI imported"
    confidence: float  # e.g., 99.0
    timestamp: int     # Unix timestamp

@dataclass
class KnowledgeRecord:
    id: str
    kind: str          # e.g., "function", "class", "import"
    language: str
    repository: str
    path: str
    symbol: str
    signature: str
    visibility: str    # "public", "private"
    relationships: List[Dict[str, str]] = field(default_factory=list)
    importance: float = 0.0
    confidence: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)
    source: str = ""
    evidence: List[Evidence] = field(default_factory=list)
