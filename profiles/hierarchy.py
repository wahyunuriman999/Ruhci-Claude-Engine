# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from loguru import logger

class HierarchicalProfiles:
    def resolve(self, session=None, repo=None, workspace=None, global_cfg=None):
        logger.info("Resolving profile Session > Repo > Workspace > Global")
        return session or repo or workspace or global_cfg
