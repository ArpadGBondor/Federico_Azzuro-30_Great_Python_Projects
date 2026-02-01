import json
import requests, os
from typing import Final
from dotenv import load_dotenv
from model import Weather, dt

load_dotenv()  # Load variables from .env

# Constants
WEATHER_API_KEY: Final[str] = os.getenv("WEATHER_API_KEY") or ""
if not WEATHER_API_KEY:
    raise ValueError("WEATHER_API_KEY is missing in environment variables.")
WEATHER_BASE_URL: Final[str] = "https://api.openweathermap.org/data/2.5/forecast"


def get_weather(city: str, mock: bool = False, cache: bool = False) -> dict:
    if mock:
        with open("mock_data.json", "r") as file:
            return json.load(file)

    payload: dict = {"q": city, "units": "metric", "appid": WEATHER_API_KEY}

    response = requests.get(url=WEATHER_BASE_URL, params=payload)
    response.raise_for_status()

    data: dict = response.json()

    if cache:
        with open("mock_data.json", "w") as file:
            json.dump(data, file)

    return data


def get_weather_details(weather: dict) -> list[Weather]:
    forecasts: list[dict] = weather["list"]

    if not forecasts:
        raise Exception(f"Problem with json: {weather}")

    list_of_weather: list[Weather] = []

    for forecast in forecasts:
        w: Weather = Weather(
            date=dt.fromtimestamp(forecast["dt"]),
            details=(details := forecast["main"]),
            temp=details["temp"],
            weather=(weather := forecast["weather"]),
            description=weather[0]["description"],
        )
        list_of_weather.append(w)

    return list_of_weather


if __name__ == "__main__":
    data: dict = get_weather(city="Tokyo", mock=True)
    weather: list[Weather] = get_weather_details(data)
    for w in weather:
        print(w)
