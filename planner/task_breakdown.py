# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import json
from typing import List, Dict, Any

class TaskBreakdown:
    """
    Bertanggung jawab untuk memecah prompt kompleks manusia menjadi 
    sub-tugas yang terstruktur, kecil, dan dapat dieksekusi secara otonom.
    """
    
    def __init__(self, llm_client=None):
        self.llm_client = llm_client
        
    def breakdown_prompt(self, user_prompt: str) -> List[Dict[str, Any]]:
        """
        Memecah prompt besar menggunakan LLM.
        """
        if not self.llm_client:
            # Fallback jika belum ada LLM client terinjeksi
            return self._mock_breakdown(user_prompt)
            
        system_instruction = (
            "Anda adalah AI Planner. Pecah tugas dari user ke dalam sub-tugas kecil. "
            "Keluarkan murni array JSON dengan format: "
            "[{\"id\": 1, \"title\": \"nama tugas\", \"description\": \"deskripsi detail\", \"dependencies\": []}]"
        )
        
        try:
            # Asumsi interface dasar LLM client
            response = self.llm_client.chat(
                messages=[
                    {"role": "system", "content": system_instruction},
                    {"role": "user", "content": user_prompt}
                ]
            )
            # Membersihkan tag markdown jika ada
            clean_json = response.strip().strip("```json").strip("```").strip()
            return json.loads(clean_json)
        except Exception as e:
            print(f"[TaskBreakdown] Gagal memecah tugas via LLM: {e}")
            return self._mock_breakdown(user_prompt)
            
    def _mock_breakdown(self, prompt: str) -> List[Dict[str, Any]]:
        """Mock sederhana jika LLM gagal atau tidak tersedia."""
        return [
            {
                "id": 1,
                "title": "Analisa Kebutuhan",
                "description": f"Menganalisa prompt user: '{prompt}'",
                "dependencies": []
            },
            {
                "id": 2,
                "title": "Eksekusi Utama",
                "description": "Menulis kode implementasi berdasarkan analisa.",
                "dependencies": [1]
            },
            {
                "id": 3,
                "title": "Verifikasi Kode",
                "description": "Melakukan pengujian pada kode yang dihasilkan.",
                "dependencies": [2]
            }
        ]
