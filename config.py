USE_ROUNDED_COORDS = False
OPENWEATHER_API = ""  # paste API token here
OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/3.0/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + OPENWEATHER_API + "&lang=en&"
    "units=metric"
)
