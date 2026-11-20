
import pytest

from database import (
    initialize_database,
    save_reading,
    get_readings
)


@pytest.fixture
def test_db(tmp_path):
    db_path = tmp_path / "test_battery.db"
    initialize_database(db_path)
    return db_path


def test_save_reading(test_db):
    record_id = save_reading(
        "collar-001", 3.9, 75.0, test_db
    )

    readings = get_readings("collar-001", test_db)

    assert record_id == 1
    assert len(readings) == 1
    assert readings[0]["voltage"] == 3.9


def test_device_filter(test_db):
    save_reading("collar-001", 3.9, 75.0, test_db)
    save_reading("collar-002", 4.1, 91.7, test_db)

    readings = get_readings("collar-001", test_db)

    assert len(readings) == 1
    assert readings[0]["device_id"] == "collar-001"


def test_multiple_readings(test_db):
    save_reading("collar-001", 3.9, 75.0, test_db)
    save_reading("collar-001", 3.7, 58.3, test_db)

    readings = get_readings("collar-001", test_db)

    assert len(readings) == 2


def test_invalid_voltage(test_db):
    with pytest.raises(ValueError):
        save_reading("collar-001", 5.0, 100.0, test_db)


def test_empty_device_id(test_db):
    with pytest.raises(ValueError):
        save_reading("", 3.9, 75.0, test_db)
