# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

import logging
from engines.optimization.prompt.pipeline import PromptOptimizationEngine

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

def run_benchmark():
    dataset = [
        "Tolong dong buatkan saya sebuah fungsi python yang bisa membaca file dari sistem operasi lalu mengubahnya ke dalam format base64. Aku mau kamu menjelaskannya dengan detail pada setiap barisnya please.",
        "Bisakah anda menganalisa kode berikut ini yang adalah sebuah implementasi dari algoritma sorting pada array yang sangat besar ke arah efisiensi yang lebih baik. Tolong ya.",
        " ".join(["teks redundan yang panjang"] * 100) # simulates a very bloated prompt
    ]
    
    engine = PromptOptimizationEngine()
    
    total_in = 0
    total_out = 0
    total_similarity = 0.0
    
    for i, prompt in enumerate(dataset):
        res = engine.execute(prompt)
        total_in += res.input_tokens
        total_out += res.output_tokens
        total_similarity += res.quality_score
        
        logger.info(f"--- Prompt {i+1} ---")
        logger.info(f"Input: {res.input_tokens} tokens")
        logger.info(f"Output: {res.output_tokens} tokens")
        logger.info(f"Reduction: {res.reduction_percent:.2f}%")
        logger.info(f"Similarity: {res.quality_score * 100:.1f}%")
        logger.info(f"Optimized Text:\n{res.optimized_text}\n")
        
    overall_reduction = ((total_in - total_out) / total_in) * 100 if total_in > 0 else 0
    avg_similarity = total_similarity / len(dataset)
    
    logger.info("=== CORE 1 BENCHMARK SUMMARY ===")
    logger.info(f"Overall Token Reduction: {overall_reduction:.2f}% (Target: >=50%)")
    logger.info(f"Average Prompt Similarity: {avg_similarity * 100:.1f}% (Target: >=95%)")
    
    if overall_reduction >= 50.0 and avg_similarity >= 0.95:
        logger.info("✅ CORE 1 KPIs MET!")
    else:
        logger.error("❌ CORE 1 KPIs FAILED!")

if __name__ == "__main__":
    run_benchmark()
