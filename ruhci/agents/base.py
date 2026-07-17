# ==========================================
# AEGIS COGNITIVE RUNTIME PLATFORM
# PROPRIETARY AND CONFIDENTIAL
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from abc import ABC, abstractmethod
from typing import Any, Dict
from loguru import logger
import time

from .contracts import AgentContext, AgentResult

class RuhciAgent(ABC):
    """
    Base Agent yang diatur oleh AEGIS Elite Cognitive Pipeline Compiler (v12.0.0).
    Mewajibkan eksekusi sekuensial yang ketat: OBSERVE -> PLAN -> EXECUTE -> REFLECT.
    """
    
    def __init__(self, name: str):
        self.name = name
        
    def run(self, context: AgentContext) -> AgentResult:
        """
        Entry point utama untuk mengeksekusi agen berdasarkan protokol AEGIS.
        Metode ini membungkus eksekusi dengan Timer dan logging.
        """
        logger.info(f"[{self.name}] Initiating AEGIS Cognitive Pipeline for task: {context.task_id}")
        start_time = time.time()
        
        try:
            # Tick 1: OBSERVE
            logger.debug(f"[{self.name}] Tick 1: OBSERVE")
            self.observe(context)
            
            # Tick 4: PLAN
            logger.debug(f"[{self.name}] Tick 4: PLAN")
            plan_data = self.plan(context)
            
            # Tick 8: EXECUTE
            logger.debug(f"[{self.name}] Tick 8: EXECUTE")
            execution_data = self.execute(context, plan_data)
            
            # Tick 9: REFLECT
            logger.debug(f"[{self.name}] Tick 9: REFLECT")
            result = self.reflect(context, execution_data)
            
            elapsed = time.time() - start_time
            result.metrics["execution_time_sec"] = elapsed
            
            logger.info(f"[{self.name}] Pipeline completed successfully in {elapsed:.3f}s")
            return result
            
        except Exception as e:
            elapsed = time.time() - start_time
            logger.error(f"[{self.name}] Pipeline failed at runtime: {str(e)}")
            return AgentResult(
                success=False,
                errors=[str(e)],
                metrics={"execution_time_sec": elapsed}
            )

    @abstractmethod
    def observe(self, context: AgentContext) -> None:
        """
        Tick 1: OBSERVE. Mengumpulkan informasi, membaca state, melakukan pencarian dasar.
        Hasilnya harus disimpan di dalam context.memory atau context.state.
        """
        pass

    @abstractmethod
    def plan(self, context: AgentContext) -> Dict[str, Any]:
        """
        Tick 4: PLAN. Merumuskan strategi, mendekomposisi tugas, memformulasikan pemanggilan alat.
        Mengembalikan blueprint data plan untuk dieksekusi.
        """
        pass

    @abstractmethod
    def execute(self, context: AgentContext, plan_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Tick 8: EXECUTE. Melakukan aksi berdasarkan plan_data.
        Memanggil tool, menulis file, merender struktur, dsb.
        Mengembalikan data hasil eksekusi mentah.
        """
        pass

    @abstractmethod
    def reflect(self, context: AgentContext, execution_data: Dict[str, Any]) -> AgentResult:
        """
        Tick 9: REFLECT. Memvalidasi hasil eksekusi, merapikan data, dan 
        mengembalikan hasil final sebagai AgentResult.
        """
        pass
