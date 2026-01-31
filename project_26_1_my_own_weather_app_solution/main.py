import requests, os
from dataclasses import dataclass
from collections import defaultdict
from typing import Any, Final
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env

# Constants
WEATHER_API_KEY: Final[str] = os.getenv("WEATHER_API_KEY") or ""
if not WEATHER_API_KEY:
    raise ValueError("WEATHER_API_KEY is missing in environment variables.")


@dataclass
class WeatherInfo:
    date: str
    time: str
    temp: float
    weather_description: str


def fetch_weather_data(city: str) -> dict[str, Any]:
    url: str = (
        f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={WEATHER_API_KEY}"
    )
    headers: dict = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    return response.json()


def retrieve_weather_data(city: str) -> list[WeatherInfo]:
    info: list[WeatherInfo] = []

    data: dict = fetch_weather_data(city)

    for forecast in data["list"]:
        date_time: list[str] = str(forecast["dt_txt"]).split()
        info.append(
            WeatherInfo(
                date=date_time[0],
                time=date_time[1],
                temp=float(forecast["main"]["temp"]),
                weather_description=forecast["weather"][0]["description"],
            )
        )

    return info


def group_by_date(info: list[WeatherInfo]) -> dict[str, list[WeatherInfo]]:
    grouped: dict[str, list[WeatherInfo]] = defaultdict(list)

    for item in info:
        grouped[item.date].append(item)

    return grouped


def display_weather(city: str):
    try:
        data = retrieve_weather_data(city)
        grouped_data = group_by_date(data)

        for date in grouped_data.keys():
            print(f"\n{date}")
            print("-" * 5)
            for forecast in grouped_data[date]:
                print(
                    f"[{forecast.time[:5]:>5}] {forecast.temp:5.1f}°C ({forecast.weather_description})"
                )
            print("-" * 40)
    except requests.HTTPError:
        print("City not found or API error.")
        return
    except requests.RequestException:
        print("Network error.")
        return


def main():
    print("-" * 40)
    print("Please enter a city.")
    print("Type 'exit' at any time to quit.")
    print("-" * 40)
    while True:
        city: str = input("Enter city: ")
        if "exit" == city.strip().lower():
            print("Bye!")
            break
        display_weather(city)
        print("")


if __name__ == "__main__":
    main()
