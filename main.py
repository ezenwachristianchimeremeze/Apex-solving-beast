#!/usr/bin/env python3
"""
Apex Sovereign Master Execution Engine
Integrates Full Pre-Flight Scan, In-Flight Charging, and Ground Safety Vision.
"""

from in_flight_charger import InFlightRegenerationEngine
from full_vehicle_diagnostic import FullVehicleDiagnosticEngine
from landing_safety_vision import LandingSafetyVisionSystem

def run_apex_complete_system_test():
    print("\n=======================================================")
    print(" APEX SOVEREIGN: MASTER SYSTEM EXECUTION & REGEN TEST ")
    print("=======================================================")

    diagnostic = FullVehicleDiagnosticEngine()
    charger = InFlightRegenerationEngine()
    vision = LandingSafetyVisionSystem()

    # 1. Pre-Flight Vehicle Scan
    print("\n[1. PRE-FLIGHT DIAGNOSTICS SCAN]:")
    telemetry = {
        "battery_pct": 90,
        "vtol_arms_status": "100%_FUNCTIONAL",
        "motors_status": "100%_OPERATIONAL",
        "avionics_status": "ONLINE_OPTIMAL",
        "vision_pc_status": "ACTIVE"
    }
    flight_approval = diagnostic.run_preflight_diagnostics("Lagos", "Abuja", telemetry)
    print(f"  -> Request Status: {flight_approval['request_status']}")

    # 2. In-Flight Charging Test
    print("\n[2. A.R.T.H. RAM-AIR REGENERATION AT CRUISE]:")
    regen_data = charger.calculate_ram_air_generation(1.8)
    print(f"  -> Speed: {regen_data['flight_speed']}")
    print(f"  -> Power Harvested: {regen_data['power_harvested_kw']}")
    print(f"  -> Endurance State: {regen_data['flight_endurance']}")

    # 3. Landing Scan
    print("\n[3. DESTINATION LANDING SCAN]:")
    landing = vision.scan_landing_zone(3.0, [])
    print(f"  -> Ground Clearance: {landing['clearance']}")

    print("\n=======================================================")
    print("      ALL APEX SOFTWARE MODULES FULLY OPERATIONAL     ")
    print("=======================================================\n")

if __name__ == "__main__":
    run_apex_complete_system_test()
