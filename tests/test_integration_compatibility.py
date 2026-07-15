# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
import pytest\nfrom integrations.pipeline import IntegrationPipeline\ndef test_compat():\n    p = IntegrationPipeline()\n    with pytest.raises(ValueError):\n        p.load({'requires_engine': '1.0'})