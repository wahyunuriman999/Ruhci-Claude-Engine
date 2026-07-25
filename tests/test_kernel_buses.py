# ==========================================
# RUHCI-CLAUDE ENGINE
# Open Source AI Engineering Engine
# Copyright (c) 2024-2026 Wahyu Nur Iman. 
# All rights reserved.
# ==========================================

from kernel.event_bus import EventBus

def test_event_bus_publish_subscribe():
    bus = EventBus()
    received_data = []

    def sample_handler(data):
        received_data.append(data)

    bus.subscribe("test_event", sample_handler)
    
    bus.publish("test_event", {"key": "value1"})
    bus.publish("test_event", {"key": "value2"})
    bus.publish("other_event", {"key": "value3"}) # Should not trigger

    assert len(received_data) == 2
    assert received_data[0]["key"] == "value1"
    assert received_data[1]["key"] == "value2"
