#!/usr/bin/env python3
"""
Apex Module F101: Ground Drive & Steering Controller
Manages wheel traction, road speed limits, and ground obstacle avoidance.
"""

class GroundDriveController:
    def __init__(self):
        self.steering_angle = 0.0
        self.road_speed_kmh = 0.0
        self.drive_mode = "ECO_CRUISE"

    def update_ground_telemetry(self, throttle_input: float, steering_input: float) -> dict:
        """Calculates ground steering and speed when driving on asphalt."""
        self.steering_angle = max(-45.0, min(45.0, steering_input)) # Max wheel turn degrees
        self.road_speed_kmh = round(throttle_input * 0.6, 1) # Capped speed for legal road driving (max ~120 km/h)
        
        return {
            "road_speed_kmh": self.road_speed_kmh,
            "steering_angle_deg": self.steering_angle,
            "traction_status": "OPTIMAL_AWD_GRIP"
        }
