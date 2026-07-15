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
