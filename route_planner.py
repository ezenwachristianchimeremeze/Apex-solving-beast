#!/usr/bin/env python3
"""
Apex Module F126: Geofenced Waypoint Flight Planner
Calculates navigation legs, distance, and flight vectors for destination routes.
"""

import math

class RoutePlanner:
    def __init__(self):
        # Sample coordinates (Latitude, Longitude)
        self.waypoints = [
            {"name": "Lagos Island Hub", "lat": 6.4549, "lon": 3.4246},
            {"name": "Lekki Phase 1 Pad", "lat": 6.4474, "lon": 3.4723},
            {"name": "Victoria Island Terminal", "lat": 6.4281, "lon": 3.4219}
        ]

    def calculate_distance(self, wp1: dict, wp2: dict) -> float:
        """Calculates distance in kilometers between two GPS points."""
        R = 6371.0  # Earth radius in km
        dlat = math.radians(wp2["lat"] - wp1["lat"])
        dlon = math.radians(wp2["lon"] - wp1["lon"])
        a = math.sin(dlat / 2)**2 + math.cos(math.radians(wp1["lat"])) * math.cos(math.radians(wp2["lat"])) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return round(R * c, 2)

    def execute_route(self):
        """Generates waypoint trajectory legs."""
        route_summary = []
        for i in range(len(self.waypoints) - 1):
            start = self.waypoints[i]
            end = self.waypoints[i+1]
            dist = self.calculate_distance(start, end)
            route_summary.append({
                "leg": f"{start['name']} -> {end['name']}",
                "distance_km": dist,
                "est_flight_time_min": round((dist / 280.0) * 60, 2)  # Based on 280 km/h cruise speed
            })
        return route_summary

