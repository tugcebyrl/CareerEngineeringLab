
def battery_status(voltage: float) -> str:
    if not 0 <= voltage <= 5:
        raise ValueError("Geçersiz gerilim")

    if voltage < 3.3:
        return "CRITICAL"
    if voltage < 3.6:
        return "LOW"

    return "NORMAL"
