# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from router.registry import UniversalRegistry, Registry

def test_router_registry_structure():
    assert "Router" in UniversalRegistry._registry
    assert "Tool" in UniversalRegistry._registry

def test_router_register():
    @Registry.Router("TestRouter")
    def my_router(): pass
    assert 'TestRouter' in UniversalRegistry._registry['Router']