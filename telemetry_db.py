#!/usr/bin/env python3
"""
Apex Module F550: Persistent SQLite Telemetry Logger
Stores real-time flight, ground, solar, and safety logs in a local database.
"""

import sqlite3
import os
from datetime import datetime

class ApexTelemetryDB:
    def __init__(self, db_path="apex_telemetry.db"):
        self.db_path = os.path.expanduser(f"~/apex_project/{db_path}")
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS telemetry (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                mode TEXT,
                speed_kmh REAL,
                altitude_m REAL,
                battery_soc REAL,
                solar_watts REAL,
                safety_score REAL,
                fan_state TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def log_record(self, mode: str, speed: float, alt: float, battery: float, solar: float, safety: float, fan_state: str):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO telemetry (timestamp, mode, speed_kmh, altitude_m, battery_soc, solar_watts, safety_score, fan_state)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (datetime.now().isoformat(), mode, speed, alt, battery, solar, safety, fan_state))
        conn.commit()
        conn.close()

    def get_log_count(self) -> int:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM telemetry')
        count = cursor.fetchone()[0]
        conn.close()
        return count

if __name__ == "__main__":
    db = ApexTelemetryDB()
    db.log_record("GROUND_AUTONOMOUS", 45.0, 0.0, 90.0, 300.0, 100.0, "STOWED_FLUSH_BODY")
    print(f"Database active. Total logged telemetry records: {db.get_log_count()}")
