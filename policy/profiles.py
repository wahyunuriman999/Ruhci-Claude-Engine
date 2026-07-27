# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from pydantic import BaseModel
from loguru import logger

class EnginePolicy(BaseModel):
    confidence_threshold: float = 0.85
    retry_limit: int = 3
    rollback_enabled: bool = True
    ask_user_on_security: bool = True
    max_cost_usd: float = 0.5
    max_tokens: int = 120000
    ponytail_mode: bool = False

class Profile(BaseModel):
    name: str
    policy: EnginePolicy
    
def get_enterprise_profile() -> Profile:
    return Profile(name="Enterprise", policy=EnginePolicy(retry_limit=5))

def get_ponytail_profile() -> Profile:
    return Profile(name="Ponytail", policy=EnginePolicy(retry_limit=3, ponytail_mode=True))
