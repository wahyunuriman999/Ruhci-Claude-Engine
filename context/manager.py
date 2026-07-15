# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from loguru import logger
from context.selector import ContextSelector
from context.compressor import TextCompressor
from context.summarizer import ContextSummarizer
from context.builder import PromptBuilder
from context.window import ContextWindow

class ContextManager:
    def __init__(self, max_tokens: int = 100000):
        self.selector = ContextSelector()
        self.compressor = TextCompressor()
        self.summarizer = ContextSummarizer()
        self.builder = PromptBuilder()
        self.window = ContextWindow(max_tokens=max_tokens)
        
    async def prepare_context(self, task: str, raw_files_content: dict) -> str:
        logger.info("ContextManager: Preparing Context...")
        
        # 1. Select
        relevant_keys = self.selector.select_relevant_context(task)
        
        # 2. Compress & Enforce Window
        compressed_blocks = []
        for key in relevant_keys:
            if key in raw_files_content:
                compressed = self.compressor.compress_python_code(raw_files_content[key])
                # Dummy token estimation (1 char ~ 0.25 tokens)
                est_tokens = len(compressed) // 4
                if self.window.fits(est_tokens):
                    self.window.add(est_tokens)
                    compressed_blocks.append(f"# --- {key} ---\n{compressed}")
                else:
                    logger.warning(f"Window full! Dropping {key}")
                    break
                    
        # 3. Build
        system_prompt = "You are Ruhci-Claude, an elite AI orchestrator."
        final_prompt = self.builder.build_prompt(system_prompt, compressed_blocks, task)
        return final_prompt
