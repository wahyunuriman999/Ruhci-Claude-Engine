# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import json
import time
from dataclasses import dataclass, field, asdict
from typing import Any, Dict


@dataclass
class AgentMessage:
    sender: str
    recipient: str
    message_type: str
    payload: Dict[str, Any]
    timestamp: float = field(default_factory=time.time)


class AgentProtocol:
    """Encodes and decodes AgentMessage objects to/from JSON strings."""

    def encode(self, msg: AgentMessage) -> str:
        return json.dumps(asdict(msg))

    def decode(self, raw: str) -> AgentMessage:
        data = json.loads(raw)
        return AgentMessage(
            sender=data["sender"],
            recipient=data["recipient"],
            message_type=data["message_type"],
            payload=data.get("payload", {}),
            timestamp=data.get("timestamp", time.time()),
        )
