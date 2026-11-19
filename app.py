
from typing import Annotated

from fastapi import FastAPI, Query

from battery import battery_status, battery_percentage

app = FastAPI(
    title="Career Engineering Lab API",
    version="1.0.0",
    description="Battery monitoring REST API"
)


@app.get("/")
def home():
    return {
        "message": "Career Engineering Lab API"
    }


@app.get("/battery/status")
def get_battery_status(
    voltage: Annotated[float, Query(ge=0, le=5)]
):
    return {
        "voltage": voltage,
        "status": battery_status(voltage)
    }


@app.get("/battery/percentage")
def get_battery_percentage(
    voltage: Annotated[float, Query(ge=3.0, le=4.2)]
):
    return {
        "voltage": voltage,
        "percentage": battery_percentage(voltage)
    }
