# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from pydantic import BaseModel
from typing import Dict, Any

class KernelMessage(BaseModel):
    msg_type: str  # COMMAND, RESPONSE, EVENT, SNAPSHOT
    payload: Dict[str, Any]
