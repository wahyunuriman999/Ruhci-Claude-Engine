# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from pydantic import BaseModel
from loguru import logger

class ReflectionReport(BaseModel):
    execution_score: float
    architecture_score: float
    code_quality: float
    performance: float
    complexity: float
    maintainability: float
    recommendations: str
