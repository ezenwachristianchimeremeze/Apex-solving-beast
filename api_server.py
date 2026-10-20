#!/usr/bin/env python3
"""
Apex Module F520: Local Telemetry REST API Server
Exposes JSON telemetry endpoints for mobile web apps and external HUD screens.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Global status buffer
latest_telemetry = {
    "system": "APEX LUXURY SKY-ROADER",
    "mode": "GROUND_AUTONOMOUS",
    "speed_kmh": 0.0,
    "fan_state": "STOWED_FLUSH_BODY",
    "battery_soc": 92.0
}

class ApexAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(latest_telemetry).encode("utf-8"))

    def log_message(self, format, *args):
        return # Suppress default HTTP console logs

def start_api_server(port=8080):
    server = HTTPServer(('0.0.0.0', port), ApexAPIHandler)
    print(f"[REST API]: Server live on http://localhost:{port}/telemetry")
    return server

if __name__ == "__main__":
    server = start_api_server()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nAPI Server stopped.")
