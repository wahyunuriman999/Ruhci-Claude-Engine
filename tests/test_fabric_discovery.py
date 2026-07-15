# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
from fabric.discovery import NodeRegistry\ndef test_disc():\n    r = NodeRegistry()\n    r.register('nodeA', ['GPU', 'Python'], 'OK')\n    assert 'nodeA' in r.nodes