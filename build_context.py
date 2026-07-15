import os

base_dir = r"C:\Users\ROG G532 LV\.gemini\antigravity\scratch\Ruhci-Claude-Engine"

header = """# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
"""

compressor_py = header + """
import re
from loguru import logger

class TextCompressor:
    @staticmethod
    def compress_python_code(code: str) -> str:
        # Remove docstrings
        code = re.sub(r'\"\"\"[\\s\\S]*?\"\"\"', '', code)
        code = re.sub(r"'''[\\s\\S]*?'''", '', code)
        # Remove single-line comments
        code = re.sub(r'#.*', '', code)
        # Remove empty lines
        lines = [line for line in code.split('\\n') if line.strip()]
        compressed = '\\n'.join(lines)
        
        logger.debug(f"Compressed code from {len(code)} to {len(compressed)} chars.")
        return compressed
"""

summarizer_py = header + """
from loguru import logger

class ContextSummarizer:
    def __init__(self, llm_client=None):
        self.client = llm_client
        
    async def summarize(self, text: str, max_tokens: int = 500) -> str:
        # Stub for LLM summarization (e.g. Claude Haiku)
        logger.debug("Summarizing long context via LLM stub...")
        return f"[SUMMARIZED: {text[:50]}...]"
"""

window_py = header + """
from loguru import logger

class ContextWindow:
    def __init__(self, max_tokens: int = 150000):
        self.max_tokens = max_tokens
        self.current_tokens = 0
        
    def fits(self, estimated_tokens: int) -> bool:
        return (self.current_tokens + estimated_tokens) <= self.max_tokens
        
    def add(self, tokens: int):
        self.current_tokens += tokens
        logger.debug(f"Context Window updated: {self.current_tokens}/{self.max_tokens}")
"""

selector_py = header + """
from loguru import logger
from typing import List, Dict, Any

class ContextSelector:
    def __init__(self, graph=None):
        self.graph = graph
        
    def select_relevant_context(self, task_description: str) -> List[str]:
        # Stub logic: In a real scenario, we embed the task_description and 
        # search the FAISS vector DB, then use NetworkX graph for BFS neighbors.
        logger.info(f"Selecting context for task: {task_description[:30]}...")
        # Simulating returning relevant file paths or symbols
        return ["core.py", "core.py::EngineState"]
"""

builder_py = header + """
from loguru import logger
from typing import List

class PromptBuilder:
    def build_prompt(self, system_prompt: str, context_blocks: List[str], task: str) -> str:
        logger.info("Assembling final prompt...")
        
        prompt = f"<system>\\n{system_prompt}\\n</system>\\n\\n"
        
        if context_blocks:
            prompt += "<context>\\n"
            for idx, block in enumerate(context_blocks):
                prompt += f"<file index=\\"{idx}\\">\\n{block}\\n</file>\\n"
            prompt += "</context>\\n\\n"
            
        prompt += f"<task>\\n{task}\\n</task>"
        return prompt
"""

manager_py = header + """
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
                    compressed_blocks.append(f"# --- {key} ---\\n{compressed}")
                else:
                    logger.warning(f"Window full! Dropping {key}")
                    break
                    
        # 3. Build
        system_prompt = "You are Ruhci-Claude, an elite AI orchestrator."
        final_prompt = self.builder.build_prompt(system_prompt, compressed_blocks, task)
        return final_prompt
"""

test_context_py = header + """
import pytest
import asyncio
from context.manager import ContextManager
from context.compressor import TextCompressor

def test_compressor():
    code = \"\"\"
    def hello():
        \"\"\"This is a docstring\"\"\"
        # This is a comment
        print("Hello")
        
    \"\"\"
    compressed = TextCompressor.compress_python_code(code)
    assert "docstring" not in compressed
    assert "comment" not in compressed
    assert "print(\\"Hello\\")" in compressed

@pytest.mark.asyncio
async def test_context_manager():
    manager = ContextManager(max_tokens=5000)
    raw_files = {
        "core.py": "def test():\\n    # comment\\n    pass",
        "core.py::EngineState": "class EngineState:\\n    pass"
    }
    
    prompt = await manager.prepare_context("Fix state bug", raw_files)
    
    assert "<system>" in prompt
    assert "<context>" in prompt
    assert "def test():" in prompt
    assert "# comment" not in prompt
    assert "<task>" in prompt
"""

files = {
    "context/compressor.py": compressor_py,
    "context/summarizer.py": summarizer_py,
    "context/window.py": window_py,
    "context/selector.py": selector_py,
    "context/builder.py": builder_py,
    "context/manager.py": manager_py,
    "tests/test_context.py": test_context_py
}

for rel_path, content in files.items():
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)

print("Context Manager Implementation Complete.")
