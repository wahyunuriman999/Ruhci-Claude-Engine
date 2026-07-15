# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import re

class PromptCompressor:
    def compress(self, text: str) -> str:
        # Hapus stop-words umum yang tidak mengubah makna
        stop_words = [" yang ", " dari ", " pada ", " ke ", " sebuah ", " adalah ", " dan ", " atau ", " dengan ", " untuk ", " di "]
        compressed = text
        for word in stop_words:
            compressed = re.sub(word, " ", compressed, flags=re.IGNORECASE)
            
        # Deduplikasi kata yang berulang secara berurutan (agresif)
        # contoh: "teks redundan panjang teks redundan panjang" -> "teks redundan panjang"
        compressed = re.sub(r'\b(.+?)(?:\s+\1\b)+', r'\1', compressed)
            
        # Hapus multi-space dan baris kosong ganda
        compressed = re.sub(r" +", " ", compressed)
        compressed = re.sub(r"\n{3,}", "\n\n", compressed)
        return compressed.strip()
