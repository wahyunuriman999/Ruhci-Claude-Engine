# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
import time, pytest\nfrom integrations.sandbox import SoftSandbox\ndef test_sandbox():\n    s = SoftSandbox(timeout_sec=0.1)\n    def slow(): time.sleep(0.2)\n    with pytest.raises(TimeoutError):\n        s.run(slow)