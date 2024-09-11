from weather_api_service import Weather

def format_weather(weather: Weather) -> str:
    """Formats weather data in string"""
    return (f"{weather.city}, temperature {weather.temperature}°C, "
            f"{weather.weather_type}\n"
            f"sunrise: {weather.sunrise.strftime('%H:%M')}\n"
            f"sunset: {weather.sunset.strftime('%H:%M')}\n")


if __name__ == "__main__":
    from datetime import datetime
    from weather_api_service import WeatherType
    print(format_weather(Weather(
        temperature=24,
        weather_type=WeatherType.CLEAR,
        sunrise=datetime.fromisoformat("2024-07-29 05:00:00"),
        sunset=datetime.fromisoformat("2024-07-29 21:00:00"),
        city="Stockholm"
    )))
