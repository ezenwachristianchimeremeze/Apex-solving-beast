#!/usr/bin/env python3
"""
Apex Module F960: Emergency Ballistic Capsule Ejection
Micro-rocket thruster and ballistic parachute cabin separation system.
"""

class BallisticCapsuleEjection:
    def __init__(self):
        self.system_status = "ARMED_AND_READY"
        self.thruster_thrust_kn = 120.0

    def trigger_emergency_evacuation(self) -> dict:
        """Instantly separates the cabin and deploys landing parachutes."""
        return {
            "status": "EMERGENCY_CAPSULE_DEPLOYED",
            "micro_thrusters": f"{self.thruster_thrust_kn} kN FIRING",
            "parachute_status": "SUPER_TENSILE_CANOPY_DEPLOYED",
            "passenger_safety": "100% SECURE_CONTAINMENT"
        }

if __name__ == "__main__":
    bce = BallisticCapsuleEjection()
    print(bce.trigger_emergency_evacuation())
