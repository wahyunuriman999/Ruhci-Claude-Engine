# ==========================================
# AEGIS COGNITIVE RUNTIME PLATFORM
# PROPRIETARY AND CONFIDENTIAL
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from dataclasses import dataclass, field
from typing import Dict, Any, List, Optional

@dataclass
class AgentContext:
    """
    Konteks standar yang diberikan kepada setiap Agen.
    Menyimpan state lingkungan, parameter input, dan history observasi.
    """
    task_id: str
    query: str
    repository_path: str
    state: Dict[str, Any] = field(default_factory=dict)
    memory: List[Dict[str, Any]] = field(default_factory=list)

@dataclass
class AgentResult:
    """
    Output standar yang dikembalikan oleh setiap Agen setelah eksekusi.
    """
    success: bool
    data: Dict[str, Any] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)
    metrics: Dict[str, float] = field(default_factory=dict)
