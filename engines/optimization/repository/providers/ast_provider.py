# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from .base import BaseProvider

class ASTProvider(BaseProvider):
    def provide(self, repo_path: str):
        return {"type": "ast", "data": "dummy_ast_tree"}
