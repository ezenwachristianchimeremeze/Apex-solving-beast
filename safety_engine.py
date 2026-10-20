#!/usr/bin/env python3
"""
Apex Module F350: AI Proximity, Night-Vision & 3D Narrow Gap Evasion Engine
Calculates evasion maneuvers and banking roll angles to squeeze between obstacles.
"""

class AISafetyEngine:
    def __init__(self):
        self.risk_threshold = 80.0

    def evaluate_environment(self, obstacle_distance_m: float, gap_width_m: float = 10.0, is_night: bool = True) -> dict:
        """Evaluates proximity, night vision, and decides roll/tilt angle for narrow gaps."""
        if obstacle_distance_m < 50.0:
            risk_score = max(50.0, float(100.0 - (obstacle_distance_m * 1.0)))
            
            # Squeeze-Through / Banking Logic between two buildings
            if gap_width_m < 4.0:  # Gap is narrower than horizontal wingspan
                roll_angle_deg = 55.0
                evasion_maneuver = f"NIGHT_SQUEEZE_BANK (Roll: {roll_angle_deg}° Sideways)"
                status = f"NIGHT LIDAR: Narrow gap ({gap_width_m}m) detected. Bending posture to pass through."
            else:
                roll_angle_deg = 0.0
                evasion_maneuver = "DYNAMIC_BANK_LEFT_OR_RIGHT"
                status = f"WARNING: Obstacle at {obstacle_distance_m}m. Clearing path."
                
            suggested_throttle = 35.0  # Safe reduced speed for tight clearance
        else:
            risk_score = 15.0
            roll_angle_deg = 0.0
            evasion_maneuver = "NOMINAL_FLIGHT_PATH"
            status = "CLEAR: Night airspace nominal."
            suggested_throttle = 85.0

        return {
            "safety_score": risk_score,
            "status": status,
            "suggested_throttle": suggested_throttle,
            "evasion_vector": evasion_maneuver,
            "roll_angle_deg": roll_angle_deg,
            "night_vision_active": is_night
        }

if __name__ == "__main__":
    safety = AISafetyEngine()
    print(safety.evaluate_environment(25.0, gap_width_m=2.8, is_night=True))
