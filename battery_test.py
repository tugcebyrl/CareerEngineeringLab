import pytest
from battery import battery_status

@pytest.mark.parametrize(
    "voltage, expected",
    [
        (3.0, "CRITICAL"),
        (3.3, "LOW"),
        (3.6, "NORMAL"),
        (4.2, "NORMAL"),
    ]
)
def test_battery_status(voltage, expected):
    assert battery_status(voltage) == expected

def test_invalid_voltage():
    with pytest.raises(ValueError):
        battery_status(-1)
from battery import battery_percentage

def test_battery_percentage_full():
    assert battery_percentage(4.2) == 100.0

def test_battery_percentage_empty():
    assert battery_percentage(3.0) == 0.0