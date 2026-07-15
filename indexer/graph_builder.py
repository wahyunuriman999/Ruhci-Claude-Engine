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
