# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
from profiles.hierarchy import HierarchicalProfiles\ndef test_prof():\n    h = HierarchicalProfiles()\n    assert h.resolve('sess', 'repo', 'work', 'glob') == 'sess'