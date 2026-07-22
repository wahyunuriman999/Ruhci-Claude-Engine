# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import Dict, Any, List

class ContextRouter:
    """Routes and filters raw context into specialized semantic channels."""
    
    def __init__(self):
        self.channels = {
            "code": [],
            "docs": [],
            "issues": []
        }
        
    def route_context(self, items: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        """Categorizes context items into channels based on type or metadata."""
        routed = {k: [] for k in self.channels.keys()}
        routed["unclassified"] = []
        
        for item in items:
            ctype = item.get("type", "").lower()
            if ctype in ("python", "javascript", "typescript", "code"):
                routed["code"].append(item)
            elif ctype in ("markdown", "txt", "doc"):
                routed["docs"].append(item)
            elif ctype in ("issue", "pr", "discussion"):
                routed["issues"].append(item)
            else:
                routed["unclassified"].append(item)
                
        return routed
        
    def handle(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handler implementation for Dispatcher routing."""
        items = request.get("items", [])
        return {
            "routed_context": self.route_context(items)
        }
