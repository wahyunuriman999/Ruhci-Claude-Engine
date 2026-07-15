# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import re
from loguru import logger

class TextCompressor:
    @staticmethod
    def compress_python_code(code: str) -> str:
        # Remove docstrings
        code = re.sub(r'"""[\s\S]*?"""', '', code)
        code = re.sub(r"'''[\s\S]*?'''", '', code)
        # Remove single-line comments
        code = re.sub(r'#.*', '', code)
        # Remove empty lines
        lines = [line for line in code.split('\n') if line.strip()]
        compressed = '\n'.join(lines)
        
        logger.debug(f"Compressed code from {len(code)} to {len(compressed)} chars.")
        return compressed
