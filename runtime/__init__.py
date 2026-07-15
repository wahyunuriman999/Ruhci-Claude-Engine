# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from loguru import logger
import sys

def init_runtime():
    """
    Initializes global runtime configurations like logging, 
    signal handlers, and global metrics.
    """
    logger.remove()
    logger.add(sys.stdout, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>")
    logger.info("Ruhci-Claude Engine Runtime Initialized")

# Automatically initialize on import
init_runtime()
