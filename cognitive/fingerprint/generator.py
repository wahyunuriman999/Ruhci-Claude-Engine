# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import hashlib
from loguru import logger

class FingerprintGenerator:
    @staticmethod
    def get_fast_fingerprint(content: str) -> str:
        return hashlib.sha256(content.encode('utf-8')).hexdigest()
        
    @staticmethod
    def get_ast_fingerprint(ast_tree, normalized_code: str, deps_version: str) -> str:
        base = f"{str(ast_tree)}_{normalized_code}_{deps_version}"
        return hashlib.sha256(base.encode('utf-8')).hexdigest()
        
    @staticmethod
    def get_semantic_fingerprint(embedding_vector) -> str:
        # Stub
        return hashlib.md5(str(embedding_vector).encode('utf-8')).hexdigest()
