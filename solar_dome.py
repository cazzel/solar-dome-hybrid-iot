import requests
import time
from datetime import datetime
from zoneinfo import ZoneInfo


# Konfigurasi
BLYNK_TOKEN = ""

# Perkiraan titik tengah Suli Barat, Kabupaten Luwu
LATITUDE = -3.4746
LONGITUDE = 120.3057

# Update interval
UPDATE_INTERVAL = 300  # 300 seconds = 5 minutes


# Fungsi BLYNK
def send_to_blynk(values):

    blynk_url = "https://blynk.cloud/external/api/update"

    for pin, value in values.items():

        try:

            response = requests.get(
                blynk_url,
                params={
                    "token": BLYNK_TOKEN,
                    pin: value
                },
                timeout=15
            )

            print(
                f"{pin}: {value} → HTTP {response.status_code}"
            )

        except requests.RequestException as e:

            print(f"{pin}: FAILED → {e}")


# MAIN LOOP
while True:

    try:

        print("\n" + "=" * 50)
        print("GETTING WEATHER DATA...")
        print("=" * 50)

        # Mengambil data cuaca dari OPEN-METEO
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {

            "latitude": LATITUDE,
            "longitude": LONGITUDE,

            "current": (
                "temperature_2m,"
                "relative_humidity_2m,"
                "precipitation,"
                "cloud_cover,"
                "shortwave_radiation"
            ),

            "timezone": "Asia/Makassar"
        }

        weather_response = requests.get(
            weather_url,
            params=weather_params,
            timeout=15
        )

        weather_response.raise_for_status()

        weather = weather_response.json()

        # Ekstraksi Data
        current = weather["current"]

        temperature = current["temperature_2m"]
        humidity = current["relative_humidity_2m"]
        solar_radiation = current["shortwave_radiation"]
        precipitation = current["precipitation"]
        cloud_cover = current["cloud_cover"]

        print("\n=== SULI BARAT WEATHER ===")

        print(f"Temperature: {temperature} °C")
        print(f"Humidity: {humidity} %")
        print(f"Solar radiation: {solar_radiation} W/m²")
        print(f"Precipitation: {precipitation} mm")
        print(f"Cloud cover: {cloud_cover} %")


        # Menentukan mode energi
        if precipitation > 0 or solar_radiation < 200:

            energy_mode = "BIOMASS"

        elif solar_radiation >= 600 and precipitation == 0:

            energy_mode = "SOLAR"

        else:

            energy_mode = "SOLAR + BIOMASS"

        print(f"Energy mode: {energy_mode}")


        # Menentukan kondisi pengeringan 
        if (
            solar_radiation >= 600
            and precipitation == 0
            and humidity < 70
        ):

            drying_condition = "FAVORABLE"

        elif (
            solar_radiation < 200
            or precipitation > 0
            or humidity > 85
        ):

            drying_condition = "UNFAVORABLE"

        else:

            drying_condition = "MODERATE"

        print(f"Drying condition: {drying_condition}")


        # Generate timestamp baru
        last_update = datetime.now(
            ZoneInfo("Asia/Makassar")
        ).strftime("%d %b %Y, %H:%M WITA")

        print(f"Last update: {last_update}")


        # Data BLYNK
        blynk_values = {

            "v0": temperature,

            "v1": humidity,

            "v2": solar_radiation,

            "v3": precipitation,

            "v4": cloud_cover,

            "v5": energy_mode,

            "v6": drying_condition,

            "v7": last_update
        }


        # Mengirim data ke BLYNK

        print("\n=== BLYNK ===")

        send_to_blynk(blynk_values)


        # Menunggu update data berikutnya

        print("\nUpdate complete.")
        print("Next update in 5 minutes...")

        time.sleep(UPDATE_INTERVAL)


    # ERROR HANDLING
    except Exception as e:

        print(f"\nERROR: {e}")

        print("Retrying in 60 seconds...")

        time.sleep(60)