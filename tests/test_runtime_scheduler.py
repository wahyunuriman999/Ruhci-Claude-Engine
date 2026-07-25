# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from fabric.scheduler import TaskScheduler

def test_task_scheduler_priority():
    scheduler = TaskScheduler()
    
    execution_order = []
    
    def task1():
        execution_order.append("T1")
        return "Res1"
        
    def task2():
        execution_order.append("T2")
        return "Res2"
        
    def task3():
        execution_order.append("T3")
        return "Res3"
        
    # Schedule with priorities (lower int = higher priority)
    scheduler.schedule("t1", 10, task1)
    scheduler.schedule("t2", 1, task2)  # Should run first
    scheduler.schedule("t3", 5, task3)  # Should run second
    
    assert scheduler.pending_count() == 3
    
    res2 = scheduler.run_next()
    assert res2 == "Res2"
    
    res3 = scheduler.run_next()
    assert res3 == "Res3"
    
    res1 = scheduler.run_next()
    assert res1 == "Res1"
    
    assert execution_order == ["T2", "T3", "T1"]
    assert scheduler.pending_count() == 0
