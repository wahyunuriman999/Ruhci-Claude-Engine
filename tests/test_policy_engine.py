# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
from policy.profiles import get_enterprise_profile\ndef test_policy():\n    p = get_enterprise_profile()\n    assert p.policy.retry_limit == 5