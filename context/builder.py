# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from loguru import logger
from typing import List

class PromptBuilder:
    def build_prompt(self, system_prompt: str, context_blocks: List[str], task: str) -> str:
        logger.info("Assembling final prompt...")
        
        prompt = f"<system>\n{system_prompt}\n</system>\n\n"
        
        if context_blocks:
            prompt += "<context>\n"
            for idx, block in enumerate(context_blocks):
                prompt += f"<file index=\"{idx}\">\n{block}\n</file>\n"
            prompt += "</context>\n\n"
            
        prompt += f"<task>\n{task}\n</task>"
        return prompt
