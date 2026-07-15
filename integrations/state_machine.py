# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from enum import Enum

class IntegrationState(Enum):
    DISCOVERED = 1
    INSTALLED = 2
    REGISTERED = 3
    VALIDATED = 4
    INITIALIZED = 5
    READY = 6
    ACTIVE = 7
    SUSPENDED = 8
    STOPPED = 9
    UNLOADED = 10
