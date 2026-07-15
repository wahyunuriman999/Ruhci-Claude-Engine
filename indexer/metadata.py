# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import List, Optional
from pydantic import BaseModel

class CodeSymbol(BaseModel):
    name: str
    symbol_type: str  # "class", "function", "method"
    start_line: int
    end_line: int
    docstring: Optional[str] = None
    dependencies: List[str] = []

class FileMetadata(BaseModel):
    filepath: str
    language: str
    imports: List[str] = []
    symbols: List[CodeSymbol] = []
    token_count: int = 0
