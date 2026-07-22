# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import logging

class KernelLogger:
    @staticmethod
    def get_logger(name):
        # A centralized logger for all subsystems
        logging.basicConfig(level=logging.INFO)
        return logging.getLogger(name)
