def convert_time(originTime_str: str, originOffset: int, targetOffset: int) -> str:
    # 1. Split "HH:MM" into integer hours and minutes
    # 2. Calculate the hour difference between target_offset and origin_offset
    # 3. Handle wrap-around past 23:59 (next day) or below 00:00 (previous day)
    # 4. Format hours and minutes back to two digits (e.g., "09:05")

    # 1
    (hour_str, min_str) = originTime_str.split(":")

    # 2
    hourDiff = targetOffset - originOffset % 24

    targetTimeHour = int(hour_str) + hourDiff
    targetTimeMin = int(min_str)

    # 3
    if targetTimeHour > 24 :
        targetTimeHour -= 24
    elif targetTimeHour < 0 :
        targetTimeHour += 24

    # 4
    targetTime_str = f"{targetTimeHour:02d}:{targetTimeMin:02d}"
    return targetTime_str

# --- Test Cases ---

# 1. London (UTC+0) to New York (UTC-5) -> Same Day
print(convert_time("14:30", 0, -5))
# Expected: "09:30 (same day)"

# 2. London (UTC+0) to Tokyo (UTC+9) -> Next Day
print(convert_time("18:15", 0, 9))
# Expected: "03:15 (next day)"

# 3. Tokyo (UTC+9) to Los Angeles (UTC-8) -> Previous Day
print(convert_time("04:05", 9, -8))
# Expected: "11:05 (previous day)"

# 4. Midnight Edge Case: New York (UTC-5) to London (UTC+0)
print(convert_time("19:00", -5, 0))
# Expected: "00:00 (next day)"
