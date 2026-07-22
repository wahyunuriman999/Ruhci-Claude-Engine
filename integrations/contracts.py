# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class IntegrationContract:
    """Defines the formal contract between two integrated systems."""
    name: str
    version: str
    required_capabilities: List[str] = field(default_factory=list)
    optional_capabilities: List[str] = field(default_factory=list)

    def validate(self, system_capabilities: List[str]) -> bool:
        """Return True if all required capabilities are present."""
        cap_set = set(system_capabilities)
        return all(c in cap_set for c in self.required_capabilities)

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "version": self.version,
            "required_capabilities": self.required_capabilities,
            "optional_capabilities": self.optional_capabilities,
        }

    def satisfied_optionals(self, system_capabilities: List[str]) -> List[str]:
        cap_set = set(system_capabilities)
        return [c for c in self.optional_capabilities if c in cap_set]
