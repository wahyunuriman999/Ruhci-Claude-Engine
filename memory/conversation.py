# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
import time

@dataclass
class Message:
    role: str
    content: str
    timestamp: float = field(default_factory=time.time)
    metadata: Dict[str, Any] = field(default_factory=dict)
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "role": self.role,
            "content": self.content,
            "timestamp": self.timestamp,
            "metadata": self.metadata
        }

class ConversationMemory:
    """Manages short-term conversational context (working memory)."""
    
    def __init__(self, max_tokens: int = 100000):
        self.messages: List[Message] = []
        self.max_tokens = max_tokens
        
    def add_message(self, role: str, content: str, metadata: Optional[Dict[str, Any]] = None) -> None:
        """Appends a new message to the conversation history."""
        msg = Message(role=role, content=content, metadata=metadata or {})
        self.messages.append(msg)
        
    def get_messages(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        """Retrieves formatted message history."""
        msgs = self.messages[-limit:] if limit else self.messages
        return [m.to_dict() for m in msgs]
        
    def clear(self) -> None:
        """Clears the short-term memory."""
        self.messages.clear()
        
    def summary(self) -> Dict[str, Any]:
        """Provides a statistical summary of the current conversation."""
        return {
            "total_messages": len(self.messages),
            "roles_count": {
                "user": sum(1 for m in self.messages if m.role == "user"),
                "assistant": sum(1 for m in self.messages if m.role == "assistant"),
                "system": sum(1 for m in self.messages if m.role == "system")
            }
        }
