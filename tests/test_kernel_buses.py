# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
from kernel.event_bus import EventBus\nfrom kernel.command_bus import CommandBus\ndef test_buses():\n    e = EventBus()\n    c = CommandBus()\n    assert e is not None and c is not None