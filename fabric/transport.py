# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import time
from collections import deque
from typing import Any, Dict, Deque, Optional


class MessageTransport:
    """In-memory per-agent message queue for agent-to-agent communication."""

    def __init__(self):
        self._queues: Dict[str, Deque[Dict[str, Any]]] = {}

    def _ensure_queue(self, agent_id: str) -> None:
        if agent_id not in self._queues:
            self._queues[agent_id] = deque()

    def send(self, sender: str, recipient: str, message: Dict[str, Any]) -> None:
        """Enqueue a message for the recipient."""
        self._ensure_queue(recipient)
        envelope = {
            "sender": sender,
            "recipient": recipient,
            "message": message,
            "timestamp": time.time(),
        }
        self._queues[recipient].append(envelope)

    def receive(self, agent_id: str) -> Optional[Dict[str, Any]]:
        """Pop and return the oldest message for agent_id, or None if empty."""
        self._ensure_queue(agent_id)
        if self._queues[agent_id]:
            return self._queues[agent_id].popleft()
        return None

    def queue_size(self, agent_id: str) -> int:
        self._ensure_queue(agent_id)
        return len(self._queues[agent_id])
