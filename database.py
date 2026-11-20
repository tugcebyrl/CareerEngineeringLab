
import sqlite3
from pathlib import Path
from datetime import datetime, timezone

DB_PATH = Path(__file__).parent / "battery.db"


def initialize_database(db_path=DB_PATH):
    with sqlite3.connect(db_path) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS battery_readings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                device_id TEXT NOT NULL,
                voltage REAL NOT NULL,
                percentage REAL NOT NULL,
                created_at TEXT NOT NULL
            )
        """)

        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_device_created
            ON battery_readings(device_id, created_at DESC)
        """)


def save_reading(
    device_id: str,
    voltage: float,
    percentage: float,
    db_path=DB_PATH
) -> int:
    if not device_id.strip():
        raise ValueError("Cihaz kimligi bos olamaz")

    if not 3.0 <= voltage <= 4.2:
        raise ValueError("Gecersiz batarya gerilimi")

    if not 0 <= percentage <= 100:
        raise ValueError("Gecersiz batarya yuzdesi")

    timestamp = datetime.now(timezone.utc).isoformat()

    with sqlite3.connect(db_path) as conn:
        cursor = conn.execute(
            """
            INSERT INTO battery_readings
            (device_id, voltage, percentage, created_at)
            VALUES (?, ?, ?, ?)
            """,
            (device_id, voltage, percentage, timestamp)
        )
        return cursor.lastrowid


def get_readings(device_id: str, db_path=DB_PATH) -> list[dict]:
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row

        rows = conn.execute(
            """
            SELECT *
            FROM battery_readings
            WHERE device_id = ?
            ORDER BY created_at DESC, id DESC
            """,
            (device_id,)
        ).fetchall()

        return [dict(row) for row in rows]
