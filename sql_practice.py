
import sqlite3
from database import DB_PATH

with sqlite3.connect(DB_PATH) as conn:
    conn.row_factory = sqlite3.Row

    print("\n1. TUM KAYITLAR")
    rows = conn.execute("""
        SELECT * FROM battery_readings
    """).fetchall()

    for row in rows:
        print(dict(row))

    print("\n2. DUSUK BATARYALAR")
    rows = conn.execute("""
        SELECT *
        FROM battery_readings
        WHERE voltage < 3.8
    """).fetchall()

    for row in rows:
        print(dict(row))

    print("\n3. CIHAZ BAZINDA ORTALAMA")
    rows = conn.execute("""
        SELECT
            device_id,
            COUNT(*) AS total_readings,
            ROUND(AVG(voltage), 2) AS avg_voltage
        FROM battery_readings
        GROUP BY device_id
    """).fetchall()

    for row in rows:
        print(dict(row))
