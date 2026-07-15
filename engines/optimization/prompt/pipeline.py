# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import time
from .analyzer import PromptAnalyzer
from .canonicalizer import PromptCanonicalizer
from .compressor import PromptCompressor
from .validator import PromptValidator
from .metrics import MetricsCollector
from engines.optimization.framework.base import BaseOptimizer, OptimizationResult

class PromptOptimizationEngine(BaseOptimizer):
    def __init__(self):
        self.analyzer = PromptAnalyzer()
        self.canonicalizer = PromptCanonicalizer()
        self.compressor = PromptCompressor()
        self.validator = PromptValidator()
        self.metrics = MetricsCollector()
        
    def execute(self, prompt: str, **kwargs) -> OptimizationResult:
        start_t = time.time()
        
        analysis = self.analyzer.analyze(prompt)
        canonical = self.canonicalizer.canonicalize(prompt, analysis)
        compressed = self.compressor.compress(canonical)
        
        similarity = self.validator.validate_similarity(prompt, compressed)
        
        latency_ms = (time.time() - start_t) * 1000
        
        result = self.metrics.collect(prompt, compressed, similarity, latency_ms)
        # Pass the optimized text as a dynamic property for the consumer
        result.optimized_text = compressed
        return result
