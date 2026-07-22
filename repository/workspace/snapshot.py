# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import hashlib
import os
import time
from typing import Dict


class WorkspaceSnapshot:
    """Captures and diffs workspace file states."""

    def _file_md5(self, filepath: str) -> str:
        h = hashlib.md5()
        try:
            with open(filepath, "rb") as f:
                for chunk in iter(lambda: f.read(8192), b""):
                    h.update(chunk)
        except OSError:
            return ""
        return h.hexdigest()

    def capture(self, root_dir: str) -> Dict:
        """Capture all files under root_dir with hash + size + mtime."""
        snapshot: Dict[str, Dict] = {}
        for dirpath, _, filenames in os.walk(root_dir):
            for fname in filenames:
                path = os.path.join(dirpath, fname)
                try:
                    stat = os.stat(path)
                    snapshot[path] = {
                        "md5": self._file_md5(path),
                        "size": stat.st_size,
                        "mtime": stat.st_mtime,
                    }
                except OSError:
                    pass
        return {"timestamp": time.time(), "files": snapshot}

    def diff(self, snap_a: Dict, snap_b: Dict) -> Dict:
        """Compare two snapshots and return added/removed/modified sets."""
        files_a = snap_a.get("files", {})
        files_b = snap_b.get("files", {})
        keys_a, keys_b = set(files_a), set(files_b)
        added = list(keys_b - keys_a)
        removed = list(keys_a - keys_b)
        modified = [
            k for k in keys_a & keys_b if files_a[k]["md5"] != files_b[k]["md5"]
        ]
        return {"added": added, "removed": removed, "modified": modified}
