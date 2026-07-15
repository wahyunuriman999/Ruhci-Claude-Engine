# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
from repository.ranking.importance import ContextRanking\ndef test_ranking():\n    assert ContextRanking().calculate_importance('core.py') > 1.0