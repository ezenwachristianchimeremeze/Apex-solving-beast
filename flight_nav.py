#!/usr/bin/env python3
"""
Apex Module F101/F001: GPS Autonomous Flight & Drive Router
Handles retractable ducted fan deployment, thrust vectoring, speed, and altitude.
"""

class FlightNavRouter:
    def __init__(self):
        self.current_speed_kmh = 0.0
        self.current_altitude_m = 0.0
        self.fan_vector_angle_deg = 0
        self.fan_deployment_state = "STOWED_FLUSH"  # Fans hidden inside body for ground driving

    def set_flight_vector(self, mode: str, throttle_pct: float):
        """Adjusts fan deployment doors, vectoring, speed, and altitude based on mode."""
        if mode == "AIRBORNE_CRUISE":
            self.fan_deployment_state = "FULLY_DEPLOYED_LOCKED" # Fans swung/slid out
            self.fan_vector_angle_deg = 0
            self.current_altitude_m = 250.0
            self.current_speed_kmh = round(throttle_pct * 3.5, 1)
        elif mode == "FLIGHT_TRANSITION":
            self.fan_deployment_state = "OPENING_AND_VECORING" # Doors sliding open, fans tilting
            self.fan_vector_angle_deg = 90
            self.current_altitude_m = 50.0
            self.current_speed_kmh = 20.0
        else:  # GROUND_AUTONOMOUS or GROUND_IDLE
            self.fan_deployment_state = "STOWED_FLUSH_BODY"  # Hidden inside body
            self.fan_vector_angle_deg = 0
            self.current_altitude_m = 0.0
            self.current_speed_kmh = round(throttle_pct * 0.8, 1)

        return {
            "speed_kmh": self.current_speed_kmh,
            "altitude_m": self.current_altitude_m,
            "vector_angle": self.fan_vector_angle_deg,
            "fan_state": self.fan_deployment_state
        }

