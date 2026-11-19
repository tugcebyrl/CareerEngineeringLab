
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_battery_status():
    response = client.get(
        "/battery/status",
        params={"voltage": 3.5}
    )

    assert response.status_code == 200
    assert response.json()["status"] == "LOW"


def test_battery_percentage():
    response = client.get(
        "/battery/percentage",
        params={"voltage": 3.9}
    )

    assert response.status_code == 200
    assert response.json()["percentage"] == 75.0


def test_invalid_voltage():
    response = client.get(
        "/battery/percentage",
        params={"voltage": 5.0}
    )

    assert response.status_code == 422
