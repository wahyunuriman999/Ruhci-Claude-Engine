# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
import pytest\nfrom router.dispatcher import Dispatcher\ndef test_dispatcher():\n    d = Dispatcher()\n    res = d.dispatch('ToolRouter', {})\n    assert 'ToolRouter' in res