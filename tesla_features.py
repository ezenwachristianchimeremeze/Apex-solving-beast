#!/usr/init/env python3
"""
Apex Module F1002: Tesla-Inspired Smart Cabin & Security Suite
Includes Sentry Mode, Dog Mode, Car Wash Mode, and OTA Climate Pre-Conditioning.
"""

class TeslaSmartCabinEngine:
    def __init__(self):
        self.sentry_active = False
        self.dog_mode_active = False
        self.car_wash_mode = False
        self.cabin_temperature_c = 22.0

    def toggle_sentry_mode(self, enable: bool) -> dict:
        """Activates 360-degree surround cameras and ultrasonic sensors for vehicle security."""
        self.sentry_active = enable
        return {
            "sentry_mode": "ACTIVE" if enable else "STANDBY",
            "cameras": "360_DEGREE_SURROUND_RECORDING",
            "threat_detection": "AI_MOTION_SENSORS_ARMED",
            "alarm_status": "READY"
        }

    def set_dog_mode(self, enable: bool, target_temp: float = 21.0) -> dict:
        """Keeps the cabin at a safe, comfortable temperature for pets with a touchscreen status display."""
        self.dog_mode_active = enable
        return {
            "dog_mode": "ACTIVE" if enable else "OFF",
            "cabin_temperature": f"{target_temp}°C",
            "screen_message": "My owner will be back soon. Relax, the AC is on!" if enable else "None"
        }

    def activate_car_wash_mode(self) -> dict:
        """Closes all windows, locks charge port, disables wipers, and neutralizes active sensors for car washes."""
        self.car_wash_mode = True
        return {
            "car_wash_mode": "ACTIVATED",
            "windows_and_ports": "SEALED_AND_LOCKED",
            "auto_wipers": "SUSPENDED",
            "parking_chimes": "MUTED"
        }

    def ota_pre_condition_cabin(self, target_temp: float) -> dict:
        """Remotely pre-heats or pre-cools the vehicle cabin before entry."""
        self.cabin_temperature_c = target_temp
        return {
            "hvac_status": "PRE_CONDITIONING_COMPLETE",
            "target_temperature": f"{target_temp}°C",
            "battery_thermal_management": "OPTIMIZED"
        }

if __name__ == "__main__":
    tesla = TeslaSmartCabinEngine()
    print("Sentry Test:", tesla.toggle_sentry_mode(True))
    print("Dog Mode Test:", tesla.set_dog_mode(True, 22.0))
    print("Car Wash Test:", tesla.activate_car_wash_mode())
