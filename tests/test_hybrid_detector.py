# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
from repository.change_detector.hybrid import HybridChangeDetector\ndef test_hybrid():\n    assert HybridChangeDetector().detect(1, 2) == 'CHANGED'