# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import pytest
import os
from indexer.scanner import RepositoryScanner
from indexer.ast_parser import ASTParser
from indexer.graph_builder import DependencyGraph
from indexer.metadata import FileMetadata, CodeSymbol

def test_scanner_ignores_system_dirs(tmp_path):
    git_dir = tmp_path / ".git"
    git_dir.mkdir()
    (git_dir / "config").touch()
    
    src_dir = tmp_path / "src"
    src_dir.mkdir()
    (src_dir / "main.py").touch()
    
    scanner = RepositoryScanner(str(tmp_path))
    files = scanner.scan()
    
    assert len(files) == 1
    assert "main.py" in files[0]
    assert "config" not in str(files)

def test_graph_builder():
    builder = DependencyGraph()
    
    meta = FileMetadata(
        filepath="core.py",
        language="python",
        symbols=[
            CodeSymbol(name="Engine", symbol_type="class", start_line=1, end_line=10)
        ]
    )
    
    builder.build_from_metadata([meta])
    
    assert builder.graph.has_node("core.py")
    assert builder.graph.has_node("core.py::Engine")
    
    context = builder.get_related_context("core.py", depth=1)
    assert "core.py::Engine" in context
