# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
from capabilities.registry import CapabilityRegistry\ndef test_reg():\n    r = CapabilityRegistry()\n    assert 'python' in r.installed