# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import hashlib
import os
from typing import Dict, List


class HybridChangeDetector:
    """Detects file changes by comparing MD5 hashes."""

    def __init__(self):
        self._hashes: Dict[str, str] = {}

    def _md5(self, filepath: str) -> str:
        h = hashlib.md5()
        try:
            with open(filepath, "rb") as f:
                for chunk in iter(lambda: f.read(8192), b""):
                    h.update(chunk)
        except OSError:
            return ""
        return h.hexdigest()

    def snapshot(self, filepath: str) -> str:
        """Compute and store the current hash of a file."""
        digest = self._md5(filepath)
        self._hashes[filepath] = digest
        return digest

    def has_changed(self, filepath: str) -> bool:
        """Return True if the file hash differs from the stored snapshot."""
        current = self._md5(filepath)
        return self._hashes.get(filepath) != current

    def get_changed_files(self, root_dir: str) -> List[str]:
        """Walk root_dir and return paths of files that changed since last snapshot."""
        changed = []
        for dirpath, _, filenames in os.walk(root_dir):
            for fname in filenames:
                path = os.path.join(dirpath, fname)
                if path not in self._hashes:
                    self.snapshot(path)  # first-time snapshot
                elif self.has_changed(path):
                    changed.append(path)
                    self.snapshot(path)  # update hash
        return changed
