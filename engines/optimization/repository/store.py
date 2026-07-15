# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import List
from .models import KnowledgeRecord

class KnowledgeStore:
    def __init__(self):
        self.records: List[KnowledgeRecord] = []
        
    def add(self, record: KnowledgeRecord):
        self.records.append(record)
        
    def get_all(self) -> List[KnowledgeRecord]:
        return self.records
        
    def query(self, **kwargs) -> List[KnowledgeRecord]:
        results = self.records
        for k, v in kwargs.items():
            results = [r for r in results if getattr(r, k, None) == v]
        return results
