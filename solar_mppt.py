#!/usr/bin/env python3
"""
Apex Module F201: Solar MPPT Power Manager
Tracks photovoltaic input and manages battery state of charge.
"""

class SolarPowerManager:
    def __init__(self, max_panel_watts: float = 500.0):
        self.max_panel_watts = max_panel_watts
        self.current_solar_watts = 0.0
        self.battery_soc = 85.0  # State of Charge (%)

    def update_solar_input(self, sunlight_factor: float) -> float:
        """Calculates solar watts generated based on sunlight factor (0.0 to 1.0)."""
        self.current_solar_watts = round(self.max_panel_watts * max(0.0, min(1.0, sunlight_factor)), 2)
        return self.current_solar_watts

    def calculate_power_flow(self, motor_consumption_watts: float) -> dict:
        net_watts = self.current_solar_watts - motor_consumption_watts
        # Adjust SoC based on 1-second interval simulation
        soc_delta = (net_watts / 3600.0) * 0.1
        self.battery_soc = max(0.0, min(100.0, round(self.battery_soc + soc_delta, 2)))
        
        return {
            "solar_watts": self.current_solar_watts,
            "motor_watts": motor_consumption_watts,
            "net_watts": round(net_watts, 2),
            "battery_soc": self.battery_soc
        }

