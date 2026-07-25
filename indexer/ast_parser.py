# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import os
import json
import tree_sitter_python as tspython
from tree_sitter import Language, Parser
from indexer.metadata import FileMetadata, CodeSymbol
from loguru import logger

# Default location for the on-disk parse cache. One JSON file per target
# repo, keyed by filepath -> (mtime, size, serialized FileMetadata). This is
# separate from indexer.cache.IndexerCache (in-memory/TTL) because that cache
# is process-local and is useless for a CLI tool that starts a fresh
# process on every invocation — every call to compile_context() previously
# re-ran tree-sitter over 100% of the repo, every time, even when nothing
# had changed since the last query.
DEFAULT_CACHE_DIR = ".ruhci_cache"
CACHE_FILE_NAME = "ast_index.json"


class ASTParser:
    def __init__(self, cache_dir: str = None, use_cache: bool = True):
        try:
            self.PY_LANGUAGE = Language(tspython.language())
            self.parser = Parser(self.PY_LANGUAGE)
            logger.info("Initialized Tree-sitter AST Parser for Python.")
        except Exception as e:
            logger.error(f"Failed to initialize Tree-sitter: {e}")
            self.parser = None

        self.use_cache = use_cache
        self.cache_dir = cache_dir or DEFAULT_CACHE_DIR
        self._cache_path = os.path.join(self.cache_dir, CACHE_FILE_NAME)
        self._disk_cache: dict = {}
        self._cache_dirty = False
        if self.use_cache:
            self._load_cache()

    def _load_cache(self) -> None:
        try:
            if os.path.exists(self._cache_path):
                with open(self._cache_path, "r", encoding="utf-8") as f:
                    self._disk_cache = json.load(f)
        except Exception as e:
            logger.warning(f"Could not read AST cache ({self._cache_path}): {e}")
            self._disk_cache = {}

    def save_cache(self) -> None:
        """Persist the in-memory cache dict to disk. Call once after a batch
        of parse_python_file() calls (e.g. at the end of compile_context)."""
        if not self.use_cache or not self._cache_dirty:
            return
        try:
            os.makedirs(self.cache_dir, exist_ok=True)
            with open(self._cache_path, "w", encoding="utf-8") as f:
                json.dump(self._disk_cache, f)
            self._cache_dirty = False
        except Exception as e:
            logger.warning(f"Could not write AST cache ({self._cache_path}): {e}")

    def parse_python_file(self, filepath: str) -> FileMetadata:
        if not self.parser:
            return FileMetadata(filepath=filepath, language="python")

        # Cache lookup keyed on (mtime, size) — cheap stat(), no hashing.
        # Any change to the file's size or mtime invalidates the entry.
        if self.use_cache:
            try:
                stat = os.stat(filepath)
                cache_key = filepath
                entry = self._disk_cache.get(cache_key)
                if entry and entry.get("mtime") == stat.st_mtime and entry.get("size") == stat.st_size:
                    return FileMetadata(**entry["metadata"])
            except OSError:
                stat = None
        else:
            stat = None

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

            metadata = FileMetadata(
                filepath=filepath, 
                language="python", 
                symbols=symbols,
                imports=imports
            )

            if self.use_cache and stat is not None:
                self._disk_cache[filepath] = {
                    "mtime": stat.st_mtime,
                    "size": stat.st_size,
                    "metadata": metadata.model_dump(),
                }
                self._cache_dirty = True

            return metadata
        except Exception as e:
            logger.error(f"Error parsing {filepath}: {e}")
            return FileMetadata(filepath=filepath, language="python")
