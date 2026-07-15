# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import networkx as nx
from loguru import logger
from typing import List
from indexer.metadata import FileMetadata

class DependencyGraph:
    def __init__(self):
        self.graph = nx.DiGraph()
        
    def build_from_metadata(self, metadatas: List[FileMetadata]):
        logger.info("Building Dependency Graph...")
        
        module_to_path = {}
        # Pass 1: Build nodes and module mapping
        for meta in metadatas:
            self.graph.add_node(meta.filepath, type="file")
            
            # Create a module path
            clean_path = meta.filepath.replace('\\', '/').replace('.py', '')
            if clean_path.endswith('/__init__'):
                module_name = clean_path[:-9].replace('/', '.')
            else:
                module_name = clean_path.replace('/', '.')
                
            module_to_path[module_name] = meta.filepath
            
            for symbol in meta.symbols:
                node_id = f"{meta.filepath}::{symbol.name}"
                self.graph.add_node(node_id, type=symbol.symbol_type)
                self.graph.add_edge(meta.filepath, node_id, relation="contains")
                
        # Pass 2: Resolve imports to create file-to-file edges
        for meta in metadatas:
            for imp in meta.imports:
                target_path = module_to_path.get(imp)
                if target_path and target_path != meta.filepath:
                    self.graph.add_edge(meta.filepath, target_path, relation="imports")
                else:
                    # Prefix matching for submodule imports
                    for mod, path in module_to_path.items():
                        if path != meta.filepath and (imp == mod or imp.startswith(f"{mod}.")):
                            self.graph.add_edge(meta.filepath, path, relation="imports")
                
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
