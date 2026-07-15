# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

class RuntimeGraph:
    def __init__(self):
        self.edges = []
    def add_dependency(self, source, target):
        self.edges.append((source, target))
