# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================
from experience.pipeline import ExperiencePipeline, ExperienceObject\ndef test_exp():\n    p = ExperiencePipeline()\n    o = ExperienceObject(id='1', repository_fingerprint='a', failure_type='t', strategy='s', solution='sol', success=True, tags=[])\n    p.store(o)