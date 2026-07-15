# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import re

class PromptCanonicalizer:
    def canonicalize(self, raw_prompt: str, analysis: dict) -> str:
        # Menghapus basa-basi
        text = raw_prompt
        pleasantries = [r"(?i)tolong dong", r"(?i)bisakah anda", r"(?i)aku mau kamu", r"(?i)please", r"(?i)tolong"]
        for p in pleasantries:
            text = re.sub(p, "", text).strip()
            
        # Standarisasi Task format if missing
        if "Task:" not in text and "Constraints:" not in text:
            text = f"Task:\n{text}\n\nConstraints:\n- Be concise.\n\nOutput:\n- Direct answer."
            
        return text
