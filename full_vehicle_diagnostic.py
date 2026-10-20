#!/usr/bin/env python3
"""
Apex Module F1016: Full Vehicle Pre-Flight Diagnostic System
Scans battery, VTOL morphing arms, motors, flight control sensors, and mechanical systems.
"""

class FullVehicleDiagnosticEngine:
    def __init__(self):
        # Operational limits
        self.max_range_km = 800.0
        self.routes = {
            "LAGOS_TO_ABUJA": 511.0,
            "ABUJA_TO_LAGOS": 511.0,
            "LAGOS_TO_PORT_HARCOURT": 447.0,
            "ABUJA_TO_KANO": 350.0
        }

    def run_preflight_diagnostics(self, origin: str, destination: str, vehicle_telemetry: dict) -> dict:
        """
        Scans all vehicle hardware components, flight mechanisms, and energy reserves.
        """
        route_key = f"{origin.upper()}_TO_{destination.upper()}"
        if route_key not in self.routes:
            return {
                "request_status": "VOID / DENIED",
                "failure_reason": f"Route {origin.title()} to {destination.title()} not in registered flight map."
            }

        required_distance_km = self.routes[route_key]
        print(f"\n[APEX PRE-FLIGHT DIAGNOSTIC]: Initiating System Scan for Route ({origin.title()} -> {destination.title()})...")
        print(f"  -> Required Flight Distance: {required_distance_km} km")

        failed_components = []

        # 1. Battery & Power Check
        battery_pct = vehicle_telemetry.get("battery_pct", 0)
        available_range_km = (battery_pct / 100.0) * self.max_range_km
        if available_range_km < required_distance_km:
            failed_components.append(
                f"BATTERY_LOW: {battery_pct}% charge provides {available_range_km:.1f} km range (Needed: {required_distance_km} km)."
            )

        # 2. VTOL Morphing Arms & Actuators Check
        vtol_arms = vehicle_telemetry.get("vtol_arms_status", "UNKNOWN")
        if vtol_arms != "100%_FUNCTIONAL":
            failed_components.append(f"VTOL_MORPHING_ARMS_FAULT: Status is '{vtol_arms}'. Deployment mechanism restricted.")

        # 3. Quantum-Vortex Motors Check
        motors = vehicle_telemetry.get("motors_status", "UNKNOWN")
        if motors != "100%_OPERATIONAL":
            failed_components.append(f"PROPULSION_MOTOR_FAULT: Status is '{motors}'. Insufficient thrust for target distance.")

        # 4. Flight Sensors & Avionics Check
        avionics = vehicle_telemetry.get("avionics_status", "UNKNOWN")
        if avionics != "ONLINE_OPTIMAL":
            failed_components.append(f"AVIONICS_SENSOR_FAULT: Navigation/Flight sensors reporting '{avionics}'.")

        # 5. Landing Vision PC & Camera Check
        vision_pc = vehicle_telemetry.get("vision_pc_status", "UNKNOWN")
        if vision_pc != "ACTIVE":
            failed_components.append(f"LANDING_VISION_PC_FAULT: Ground scan PC is '{vision_pc}'. Landing safety cannot be guaranteed.")

        # Decision Logic
        if len(failed_components) == 0:
            return {
                "route": route_key,
                "distance_km": required_distance_km,
                "request_status": "REQUEST APPROVED",
                "message": "All systems operating at 100% capacity. Apex is cleared for flight!",
                "system_health": "ALL_SYSTEMS_GO"
            }
        else:
            return {
                "route": route_key,
                "distance_km": required_distance_km,
                "request_status": "REQUEST VOID / DENIED",
                "failure_reasons": failed_components,
                "message": "Flight request canceled for security and safety precautions."
            }

if __name__ == "__main__":
    diagnostic = FullVehicleDiagnosticEngine()
    
    # Healthy Telemetry Data
    healthy_car = {
        "battery_pct": 90,
        "vtol_arms_status": "100%_FUNCTIONAL",
        "motors_status": "100%_OPERATIONAL",
        "avionics_status": "ONLINE_OPTIMAL",
        "vision_pc_status": "ACTIVE"
    }
    
    # Faulty Telemetry Data (Fault in VTOL Arms)
    faulty_car = {
        "battery_pct": 85,
        "vtol_arms_status": "ARM_3_ACTUATOR_JAMMED",
        "motors_status": "100%_OPERATIONAL",
        "avionics_status": "ONLINE_OPTIMAL",
        "vision_pc_status": "ACTIVE"
    }

    print("\n--- TEST 1: All Systems Healthy ---")
    print(diagnostic.run_preflight_diagnostics("Lagos", "Abuja", healthy_car))

    print("\n--- TEST 2: Mechanical Arm Fault ---")
    print(diagnostic.run_preflight_diagnostics("Lagos", "Abuja", faulty_car))
