from weather_api import get_weather, get_weather_details, Weather


def main():
    user_city = input("Enter city: ")

    # Get the current weather details
    weather_data: dict = get_weather(user_city, mock=True, cache=True)
    weather_details: list[Weather] = get_weather_details(weather_data)

    # get the current days
    dfmt: str = "%d/%m/%y"
    days: list[str] = sorted(
        list({f"{forecast.date:{dfmt}}" for forecast in weather_details})
    )

    for day in days:
        print("")
        print(day)
        print("-" * 5)

        grouped: list[Weather] = [
            forecast for forecast in weather_details if f"{forecast.date:{dfmt}}" == day
        ]
        for element in grouped:
            print(element)


if __name__ == "__main__":
    main()
