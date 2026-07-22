# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from collections import Counter
from typing import Dict, List


class AutonomousReflector:
    """Records agent actions and reflects on performance to enable self-correction."""

    def __init__(self):
        self._log: List[Dict] = []

    def record_action(self, action: str, outcome: str, success: bool) -> None:
        self._log.append({"action": action, "outcome": outcome, "success": success})

    def reflect(self) -> Dict:
        if not self._log:
            return {"success_rate": 0.0, "most_failed_actions": [], "total": 0}
        total = len(self._log)
        successes = sum(1 for e in self._log if e["success"])
        failures = [e["action"] for e in self._log if not e["success"]]
        top_failures = [item for item, _ in Counter(failures).most_common(5)]
        return {
            "success_rate": round(successes / total, 3),
            "most_failed_actions": top_failures,
            "total": total,
            "failures": len(failures),
        }

    def should_pause(self) -> bool:
        """Return True if success rate has dropped below 30%."""
        stats = self.reflect()
        return stats["total"] >= 5 and stats["success_rate"] < 0.3

    def clear(self) -> None:
        self._log.clear()
