# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
from decision.consensus import ConsensusEngine\ndef test_con():\n    c = ConsensusEngine()\n    p1 = {'agent': 'A', 'confidence': 0.8}\n    p2 = {'agent': 'B', 'confidence': 0.9}\n    assert c.resolve([p1, p2])['agent'] == 'B'