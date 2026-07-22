# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from collections import defaultdict
from typing import Dict, List


class AdaptiveOrchestrator:
    """Adjusts agent execution strategy based on rolling performance metrics."""

    def __init__(self, window: int = 10):
        self._window = window
        self._metrics: Dict[str, List[float]] = defaultdict(list)

    def update_metrics(self, metric_name: str, value: float) -> None:
        buf = self._metrics[metric_name]
        buf.append(value)
        if len(buf) > self._window:
            buf.pop(0)

    def _avg(self, metric_name: str) -> float:
        buf = self._metrics.get(metric_name, [])
        return sum(buf) / len(buf) if buf else 0.5

    def get_strategy(self) -> str:
        """Returns 'aggressive', 'balanced', or 'conservative'."""
        success_rate = self._avg("success_rate")
        latency = self._avg("latency")

        if success_rate >= 0.8 and latency <= 2.0:
            return "aggressive"
        elif success_rate >= 0.5:
            return "balanced"
        else:
            return "conservative"

    def adapt(self, current_performance: Dict) -> str:
        """Feed a performance dict into metrics and return the updated strategy."""
        for key, val in current_performance.items():
            if isinstance(val, (int, float)):
                self.update_metrics(key, float(val))
        return self.get_strategy()
