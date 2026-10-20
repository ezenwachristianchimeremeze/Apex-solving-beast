#!/usr/bin/env python3
"""
Apex Module F990: Emergency Voice Urgency & Dynamic Mode Switcher
Detects user urgency, calculates distance vs time, and selects road or aerial boost.
"""

class EmergencyUrgencyEngine:
    def __init__(self):
        # Coordinates / air distance between major hubs (in km)
        self.routes = {
            "LAGOS_TO_ABUJA": {"air_dist_km": 533.0, "road_dist_km": 750.0},
            "WORK_COMMUTE": {"air_dist_km": 25.0, "road_dist_km": 30.0}
        }

    def process_urgency_command(self, command_text: str, route_key: str, target_time_minutes: float) -> dict:
        """
        Calculates required speed to meet target time and engages flight/road boost.
        """
        route = self.routes.get(route_key, {"air_dist_km": 50.0, "road_dist_km": 60.0})
        target_hours = target_time_minutes / 60.0
        
        # Calculate required air speed
        req_air_speed = route["air_dist_km"] / target_hours
        
        if req_air_speed > 450.0:
            mode = "AIR_SUB_ORBITAL_SONIC_BOOST"
            status = f"CRITICAL URGENCY: Engaging Hypersonic Thrusters at {req_air_speed:.1f} km/h"
        elif req_air_speed > 320.0:
            mode = "FULL_AIR_VTOL_MAX"
            status = f"HIGH URGENCY: Transitioning to Flight Mode at {req_air_speed:.1f} km/h"
        else:
            mode = "GROUND_MAX_PERFORMANCE"
            status = f"ROAD BOOST: Maximizing Asphalt Speed at {req_air_speed:.1f} km/h"

        return {
            "command": command_text,
            "target_time_min": target_time_minutes,
            "selected_mode": mode,
            "required_speed_kmh": round(req_air_speed, 1),
            "safety_envelope": "100% QUANTUM_EVASION_ACTIVE",
            "dispatch_status": status
        }

if __name__ == "__main__":
    urgency = EmergencyUrgencyEngine()
    print(urgency.process_urgency_command("Drive from Lagos to Abuja in less than 30 minutes!", "LAGOS_TO_ABUJA", 25.0))
