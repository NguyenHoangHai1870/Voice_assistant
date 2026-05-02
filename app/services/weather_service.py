import requests
from app.config.settings import WEATHER_API_KEY, WEATHER_CITY

def get_weather():
    try:
        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={WEATHER_CITY}"
            f"&appid={WEATHER_API_KEY}"
            f"&units=metric"
            f"&lang=vi"
        )

        print("[WEATHER URL]:", url)

        res = requests.get(url, timeout=10)

        print("[WEATHER STATUS]:", res.status_code)
        print("[WEATHER BODY]:", res.text)

        data = res.json()

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]

        return f"Hôm nay ở {WEATHER_CITY} {desc}, nhiệt độ khoảng {temp}°C."

    except Exception as e:
        print("[WEATHER ERROR]:", repr(e))
        return "Không lấy được thông tin thời tiết."