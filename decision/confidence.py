# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from pydantic import BaseModel
from typing import List
from loguru import logger

class ConfidenceObject(BaseModel):
    score: float
    reason: str
    evidence: List[str]
    risks: List[str]
    recommendation: str
