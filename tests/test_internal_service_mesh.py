# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
from kernel.registry import ServiceRegistry\ndef test_mesh():\n    r = ServiceRegistry()\n    r.register('planner', object())\n    assert r.get('planner') is not None