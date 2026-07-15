# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

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
            content_bytes = bytes(content, "utf8")
            
            def traverse(node):
                if node.type == "class_definition":
                    name_node = node.child_by_field_name("name")
                    if name_node:
                        name = content_bytes[name_node.start_byte:name_node.end_byte].decode("utf8", errors="ignore")
                        symbols.append(CodeSymbol(
                            name=name,
                            symbol_type="class",
                            start_line=node.start_point[0] + 1,
                            end_line=node.end_point[0] + 1
                        ))
                elif node.type == "function_definition":
                    name_node = node.child_by_field_name("name")
                    if name_node:
                        name = content_bytes[name_node.start_byte:name_node.end_byte].decode("utf8", errors="ignore")
                        symbols.append(CodeSymbol(
                            name=name,
                            symbol_type="function",
                            start_line=node.start_point[0] + 1,
                            end_line=node.end_point[0] + 1
                        ))
                elif node.type == "import_statement":
                    for child in node.children:
                        if child.type == "dotted_name":
                            imports.append(content_bytes[child.start_byte:child.end_byte].decode("utf8", errors="ignore"))
                elif node.type == "import_from_statement":
                    module_node = node.child_by_field_name("module_name")
                    if module_node:
                        imports.append(content_bytes[module_node.start_byte:module_node.end_byte].decode("utf8", errors="ignore"))
                
                for child in node.children:
                    traverse(child)
                    
            traverse(root_node)
            
            return FileMetadata(
                filepath=filepath, 
                language="python", 
                symbols=symbols,
                imports=imports
            )
        except Exception as e:
            logger.error(f"Error parsing {filepath}: {e}")
            return FileMetadata(filepath=filepath, language="python")
