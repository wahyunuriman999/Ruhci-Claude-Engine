# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from enum import Enum

class FailureTaxonomy(Enum):
    RUNTIME = "RUNTIME"
    PLANNER = "PLANNER"
    REPOSITORY = "REPOSITORY"
    CONTEXT = "CONTEXT"
    MEMORY = "MEMORY"
    TOOL = "TOOL"
    SDK = "SDK"
    CLAUDE = "CLAUDE"
    PROMPT = "PROMPT"
    NETWORK = "NETWORK"
    FILESYSTEM = "FILESYSTEM"
    PERMISSION = "PERMISSION"
    DEPENDENCY = "DEPENDENCY"
    UNKNOWN = "UNKNOWN"
