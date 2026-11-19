
def battery_status(voltage: float) -> str:
    if not 0 <= voltage <= 5:
        raise ValueError("Geçersiz gerilim")

    if voltage < 3.3:
        return "CRITICAL"
    if voltage < 3.6:
        return "LOW"

    return "NORMAL"
def battery_percentage(voltage: float) -> float:
    if not 3.0 <= voltage <= 4.2:
        raise ValueError("Geçersiz batarya gerilimi")

    percentage = (voltage - 3.0) / 1.2 * 100
    return round(percentage, 1)