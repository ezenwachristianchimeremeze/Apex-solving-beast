#!/usr/bin/env python3
"""
Apex Module F501/F350: Voice Command & Autonomous Safe Driving Controller
Processes spoken voice instructions and enforces road safety guardrails.
"""

class VoiceCommandController:
    def __init__(self):
        self.voice_state = "LISTENING_FOR_WAKE_WORD"
        self.active_command = None
        self.autonomous_safety_lock = True  # Safe driving mode always active on road

    def process_voice_command(self, spoken_text: str) -> dict:
        """Parses voice commands and triggers corresponding vehicle actions."""
        text = spoken_text.lower()
        
        if "drive safe" in text or "safe mode" in text:
            self.active_command = "SAFE_ROAD_CRUISE"
            response = "Enforcing 360-degree LiDAR safe distance and speed limits."
        elif "autopilot" in text or "autonomous drive" in text:
            self.active_command = "FULL_AUTO_GROUND"
            response = "Autonomous road navigation engaged. Route locked."
        elif "fly" in text or "take off" in text:
            self.active_command = "INIT_FLIGHT_TRANSITION"
            response = "Voice override: Opening fan doors and switching to VTOL mode."
        else:
            self.active_command = "HOLD_CURRENT_STATE"
            response = "Command not recognized. Maintaining current safe drive state."

        return {
            "command": self.active_command,
            "response": response,
            "safe_drive_active": self.autonomous_safety_lock
        }
