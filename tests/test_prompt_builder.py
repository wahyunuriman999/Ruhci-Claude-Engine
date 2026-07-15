# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
from cognitive.optimizer.builder import PromptBuilder\nfrom cognitive.optimizer.budget import BudgetManager\ndef test_builder():\n    pb = PromptBuilder(BudgetManager())\n    assert 'built' in pb.build({})