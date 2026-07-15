# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
from decision.confidence import ConfidenceObject\ndef test_conf():\n    c = ConfidenceObject(score=0.9, reason='', evidence=[], risks=[], recommendation='')\n    assert c.score == 0.9