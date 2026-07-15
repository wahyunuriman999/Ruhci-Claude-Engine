# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
from engine.context_object import ExecutionContext\ndef test_immutable():\n    ctx = ExecutionContext()\n    new_ctx = ctx.clone(user_objective='test')\n    assert new_ctx.user_objective == 'test'