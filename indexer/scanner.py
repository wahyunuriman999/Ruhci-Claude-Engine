# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import os
from pathlib import Path
from typing import List
import logging
logger = logging.getLogger(__name__)

class RepositoryScanner:
    def __init__(self, root_dir: str):
        self.root_dir = Path(root_dir)
        self.ignore_dirs = {'.git', 'node_modules', 'venv', '__pycache__', '.pytest_cache', 'dist', 'build'}
        self.ignore_exts = {'.pyc', '.so', '.dll', '.exe', '.bin', '.zip', '.tar', '.gz'}
        
    def scan(self) -> List[str]:
        valid_files = []
        logger.info(f"Scanning repository at: {self.root_dir}")
        for root, dirs, files in os.walk(self.root_dir):
            # In-place modification to skip ignored directories
            dirs[:] = [d for d in dirs if d not in self.ignore_dirs and not d.startswith('.')]
            
            for file in files:
                ext = os.path.splitext(file)[1]
                if ext not in self.ignore_exts:
                    valid_files.append(os.path.join(root, file))
                    
        logger.info(f"Found {len(valid_files)} valid source files.")
        return valid_files
