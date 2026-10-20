#!/usr/bin/env python3
"""
Apex Module F1015: Route Distance & Battery Range Validation Engine
Checks flight route distance (e.g., Lagos to Abuja ~511 km) against current battery reserves.
"""

class RouteBatteryValidator:
    def __init__(self, max_range_km: float = 800.0):
        self.max_range_km = max_range_km
        # Approved aerial flight routes database in kilometers
        self.routes = {
            "LAGOS_TO_ABUJA": 511.0,
            "ABUJA_TO_LAGOS": 511.0,
            "LAGOS_TO_PORT_HARCOURT": 447.0,
            "ABUJA_TO_KANO": 350.0
        }

    def validate_flight_route(self, origin: str, destination: str, current_battery_pct: float) -> dict:
        """
        Scans route distance and verifies battery capability.
        Voids request if battery is too low; triggers flight if sufficient.
        """
        route_key = f"{origin.upper()}_TO_{destination.upper()}"
        
        if route_key not in self.routes:
            return {
                "route": route_key,
                "status": "ROUTE_NOT_FOUND",
                "clearance": "FLIGHT_REQUEST_VOID",
                "reason": "Destination coordinates not in registered civil flight map."
            }

        distance_km = self.routes[route_key]
        available_range_km = (current_battery_pct / 100.0) * self.max_range_km

        print(f"\n[ROUTE SCANNER]: Analyzing flight path from {origin.title()} to {destination.title()}...")
        print(f"  -> Required Distance: {distance_km} km")
        print(f"  -> Battery Reserves: {current_battery_pct}% (Max Range: {available_range_km:.1f} km)")

        if available_range_km >= distance_km:
            return {
                "route": route_key,
                "distance_km": distance_km,
                "battery_pct": current_battery_pct,
                "available_range_km": available_range_km,
                "status": "BATTERY_SUFFICIENT",
                "clearance": "FLIGHT_REQUEST_TRIGGERED_SUCCESS"
            }
        else:
            return {
                "route": route_key,
                "distance_km": distance_km,
                "battery_pct": current_battery_pct,
                "available_range_km": available_range_km,
                "status": "BATTERY_INSUFFICIENT",
                "clearance": "FLIGHT_REQUEST_VOID_DENIED",
                "reason": "Range insufficient for destination. Please recharge."
            }

if __name__ == "__main__":
    validator = RouteBatteryValidator()
    print("Test 1 (High Battery):", validator.validate_flight_route("Lagos", "Abuja", 90.0))
    print("Test 2 (Low Battery):", validator.validate_flight_route("Lagos", "Abuja", 45.0))
