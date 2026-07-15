# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

class BaseEvaluator:
    def evaluate(self, native_output, ruhci_output) -> float:
        raise NotImplementedError
