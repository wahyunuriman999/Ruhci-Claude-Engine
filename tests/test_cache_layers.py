# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
from cognitive.cache.hierarchy import MultiLevelCache\ndef test_cache():\n    c = MultiLevelCache()\n    assert c.l1 is not None