# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from .base import BaseProvider

class GitProvider(BaseProvider):
    def provide(self, repo_path: str):
        return {"type": "git_history", "data": "dummy_blame_log"}
