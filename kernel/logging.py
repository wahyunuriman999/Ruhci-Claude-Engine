# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import json
import logging
import time
from typing import Any


class RuhciLogger:
    """Structured JSON logger wrapping Python's standard logging."""

    def __init__(self, name: str):
        self._logger = logging.getLogger(name)
        if not self._logger.handlers:
            handler = logging.StreamHandler()
            handler.setFormatter(logging.Formatter("%(message)s"))
            self._logger.addHandler(handler)
        self._logger.setLevel(logging.DEBUG)
        self._name = name

    @classmethod
    def get_logger(cls, name: str) -> "RuhciLogger":
        return cls(name)

    def _emit(self, level: str, msg: str, **context: Any) -> None:
        record = {"ts": time.time(), "level": level, "module": self._name, "msg": msg}
        record.update(context)
        line = json.dumps(record)
        getattr(self._logger, level.lower(), self._logger.info)(line)

    def info(self, msg: str, **ctx: Any) -> None:
        self._emit("INFO", msg, **ctx)

    def warning(self, msg: str, **ctx: Any) -> None:
        self._emit("WARNING", msg, **ctx)

    def error(self, msg: str, **ctx: Any) -> None:
        self._emit("ERROR", msg, **ctx)

    def debug(self, msg: str, **ctx: Any) -> None:
        self._emit("DEBUG", msg, **ctx)
