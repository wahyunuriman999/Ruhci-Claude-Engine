# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from typing import List, Dict, Any, Optional

class ExecutionPlan:
    """
    Mengelola DAG (Directed Acyclic Graph) dari tugas-tugas.
    Menentukan urutan eksekusi tugas berdasarkan dependensi.
    """
    def __init__(self, tasks: List[Dict[str, Any]]):
        self.tasks = {t["id"]: t for t in tasks}
        self.completed = set()
        self.in_progress = set()
        
    def get_next_available_tasks(self) -> List[Dict[str, Any]]:
        """
        Mengembalikan daftar tugas yang siap dieksekusi 
        (semua dependensinya sudah selesai).
        """
        available = []
        for task_id, task in self.tasks.items():
            if task_id in self.completed or task_id in self.in_progress:
                continue
                
            deps = task.get("dependencies", [])
            # Jika semua dependensi sudah ada di dalam set 'completed'
            if all(dep in self.completed for dep in deps):
                available.append(task)
                
        return available
        
    def mark_in_progress(self, task_id: int):
        self.in_progress.add(task_id)
        
    def mark_completed(self, task_id: int):
        if task_id in self.in_progress:
            self.in_progress.remove(task_id)
        self.completed.add(task_id)
        
    def is_fully_completed(self) -> bool:
        """Cek apakah seluruh rencana eksekusi telah selesai."""
        return len(self.completed) == len(self.tasks)
