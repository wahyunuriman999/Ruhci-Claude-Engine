# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
from adaptive.model.resolution import ModelRegistry\ndef test_model():\n    m = ModelRegistry()\n    assert m.resolve_model('very_high') == 'claude-haiku'