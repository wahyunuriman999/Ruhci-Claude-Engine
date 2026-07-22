# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import Dict, List


class CapabilityNegotiator:
    """Negotiates which capabilities are satisfied when two systems connect."""

    def negotiate(self, offered: List[str], required: List[str]) -> Dict[str, bool]:
        """Return {capability: satisfied} for each required capability."""
        offered_set = set(offered)
        return {cap: cap in offered_set for cap in required}

    def get_missing(self, offered: List[str], required: List[str]) -> List[str]:
        """Return the list of required capabilities not present in offered."""
        offered_set = set(offered)
        return [cap for cap in required if cap not in offered_set]

    def is_compatible(self, offered: List[str], required: List[str]) -> bool:
        """Return True if all required capabilities are offered."""
        return not self.get_missing(offered, required)
