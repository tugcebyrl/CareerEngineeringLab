
from battery import battery_percentage
from database import (
    initialize_database,
    save_reading,
    get_readings
)

initialize_database()

devices = [
    ("collar-001", 3.9),
    ("collar-001", 3.7),
    ("collar-002", 4.1)
]

for device_id, voltage in devices:
    percentage = battery_percentage(voltage)

    save_reading(
        device_id,
        voltage,
        percentage
    )

print("Kayitlar basariyla eklendi!")

print("\ncollar-001 olcum gecmisi:")

readings = get_readings("collar-001")

for reading in readings:
    print(reading)
