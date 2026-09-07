import csv
import datetime
import random
import requests

URL = "https://api.open-meteo.com/v1/forecast?latitude=9.025&longitude=38.7468&current_weather=true"

def log_entry():
    try:
        response = requests.get(URL)
        data = response.json()["current_weather"]
        temp = data["temperature"]
        wind = data["windspeed"]
    except Exception:
        # Fallback values if API rate-limits
        temp, wind = 20.0, 5.0

    today = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    # Add a slight random noise identifier for data variation
    batch_id = random.randint(1000, 9999)

    file_exists = True
    try:
        with open("weather_log.csv", "r"): pass
    except FileNotFoundError:
        file_exists = False

    with open("weather_log.csv", "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["timestamp_utc", "temperature_c", "windspeed_kmh", "sample_id"])
        writer.writerow([today, temp, wind, batch_id])

if __name__ == "__main__":
    log_entry()
