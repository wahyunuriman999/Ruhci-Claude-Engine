import os

base_dir = r"C:\Users\ROG G532 LV\.gemini\antigravity\scratch\Ruhci-Claude-Engine"

header = """# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
"""

metadata_py = header + """
from typing import List, Optional
from pydantic import BaseModel

class CodeSymbol(BaseModel):
    name: str
    symbol_type: str  # "class", "function", "method"
    start_line: int
    end_line: int
    docstring: Optional[str] = None
    dependencies: List[str] = []

class FileMetadata(BaseModel):
    filepath: str
    language: str
    imports: List[str] = []
    symbols: List[CodeSymbol] = []
    token_count: int = 0
"""

scanner_py = header + """
import os
from pathlib import Path
from typing import List
from loguru import logger

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
"""

ast_parser_py = header + """
import tree_sitter_python as tspython
from tree_sitter import Language, Parser
from indexer.metadata import FileMetadata, CodeSymbol
from loguru import logger

class ASTParser:
    def __init__(self):
        try:
            self.PY_LANGUAGE = Language(tspython.language())
            self.parser = Parser(self.PY_LANGUAGE)
            logger.info("Initialized Tree-sitter AST Parser for Python.")
        except Exception as e:
            logger.error(f"Failed to initialize Tree-sitter: {e}")
            self.parser = None

    def parse_python_file(self, filepath: str) -> FileMetadata:
        if not self.parser:
            return FileMetadata(filepath=filepath, language="python")
            
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            tree = self.parser.parse(bytes(content, "utf8"))
            root_node = tree.root_node
            
            symbols = []
            imports = []
            
            # Simple traversal stub for finding classes and functions
            for child in root_node.children:
                if child.type == "class_definition":
                    name_node = child.child_by_field_name("name")
                    if name_node:
                        symbols.append(CodeSymbol(
                            name=content[name_node.start_byte:name_node.end_byte],
                            symbol_type="class",
                            start_line=child.start_point[0] + 1,
                            end_line=child.end_point[0] + 1
                        ))
                elif child.type == "function_definition":
                    name_node = child.child_by_field_name("name")
                    if name_node:
                        symbols.append(CodeSymbol(
                            name=content[name_node.start_byte:name_node.end_byte],
                            symbol_type="function",
                            start_line=child.start_point[0] + 1,
                            end_line=child.end_point[0] + 1
                        ))
                elif child.type in ["import_statement", "import_from_statement"]:
                    imports.append(content[child.start_byte:child.end_byte])
            
            return FileMetadata(
                filepath=filepath, 
                language="python", 
                symbols=symbols,
                imports=imports
            )
        except Exception as e:
            logger.error(f"Error parsing {filepath}: {e}")
            return FileMetadata(filepath=filepath, language="python")
"""

graph_builder_py = header + """
import networkx as nx
from loguru import logger
from typing import List
from indexer.metadata import FileMetadata

class DependencyGraph:
    def __init__(self):
        self.graph = nx.DiGraph()
        
    def build_from_metadata(self, metadatas: List[FileMetadata]):
        logger.info("Building Dependency Graph...")
        for meta in metadatas:
            self.graph.add_node(meta.filepath, type="file")
            for symbol in meta.symbols:
                node_id = f"{meta.filepath}::{symbol.name}"
                self.graph.add_node(node_id, type=symbol.symbol_type)
                self.graph.add_edge(meta.filepath, node_id, relation="contains")
                
        logger.info(f"Graph built with {self.graph.number_of_nodes()} nodes and {self.graph.number_of_edges()} edges.")
        
    def get_related_context(self, node_id: str, depth: int = 1) -> List[str]:
        if not self.graph.has_node(node_id):
            return []
        
        # Simple BFS for nearest neighbors
        related = set()
        for u, v in nx.bfs_edges(self.graph, source=node_id, depth_limit=depth):
            related.add(u)
            related.add(v)
            
        return list(related)
"""

test_indexer_py = header + """
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
"""

files = {
    "indexer/metadata.py": metadata_py,
    "indexer/scanner.py": scanner_py,
    "indexer/ast_parser.py": ast_parser_py,
    "indexer/graph_builder.py": graph_builder_py,
    "tests/test_indexer.py": test_indexer_py
}

for rel_path, content in files.items():
    full_path = os.path.join(base_dir, rel_path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)

print("Repository Indexer Implementation Complete.")
