# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
from cognitive.optimizer.budget import BudgetManager\ndef test_budget():\n    bm = BudgetManager()\n    assert bm.can_fit('context', 1000) == True