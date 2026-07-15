# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import pytest
import asyncio
from context.manager import ContextManager
from context.compressor import TextCompressor

def test_compressor():
    code = """
    def hello():
        """This is a docstring"""
        # This is a comment
        print("Hello")
        
    """
    compressed = TextCompressor.compress_python_code(code)
    assert "docstring" not in compressed
    assert "comment" not in compressed
    assert "print(\"Hello\")" in compressed

@pytest.mark.asyncio
async def test_context_manager():
    manager = ContextManager(max_tokens=5000)
    raw_files = {
        "core.py": "def test():\n    # comment\n    pass",
        "core.py::EngineState": "class EngineState:\n    pass"
    }
    
    prompt = await manager.prepare_context("Fix state bug", raw_files)
    
    assert "<system>" in prompt
    assert "<context>" in prompt
    assert "def test():" in prompt
    assert "# comment" not in prompt
    assert "<task>" in prompt
