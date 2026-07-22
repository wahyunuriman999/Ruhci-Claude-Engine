# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from copy import deepcopy
from typing import Any, Dict, List, Optional


class ProfileHierarchy:
    """Manages user/agent profiles in a parent-child tree. Child overrides parent."""

    def __init__(self):
        self._profiles: Dict[str, Dict] = {}
        self._parents: Dict[str, Optional[str]] = {}

    def add_profile(
        self, name: str, parent: Optional[str] = None, metadata: Optional[Dict] = None
    ) -> None:
        if parent and parent not in self._profiles:
            raise ValueError(f"Parent profile '{parent}' does not exist.")
        self._profiles[name] = metadata or {}
        self._parents[name] = parent

    def get_profile(self, name: str) -> Dict:
        if name not in self._profiles:
            raise KeyError(f"Profile '{name}' not found.")
        return dict(self._profiles[name])

    def get_inherited_config(self, name: str) -> Dict:
        """Merge ancestors' config (root first) then overlay child config."""
        chain: List[str] = []
        current = name
        while current is not None:
            chain.append(current)
            current = self._parents.get(current)
        chain.reverse()  # root → ... → child
        merged: Dict[str, Any] = {}
        for profile_name in chain:
            merged.update(self._profiles.get(profile_name, {}))
        return merged

    def list_profiles(self) -> List[str]:
        return list(self._profiles.keys())
