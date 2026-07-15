# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

class StructuredPacker:
    def pack(self, ranked_files: list) -> str:
        output = "# Repository Context\n\n"
        output += "## Project Summary\n"
        output += "## Relevant Modules\n"
        for f in ranked_files:
            output += f"- {f['file']} (Confidence: {f['score']}%)\n"
        return output
