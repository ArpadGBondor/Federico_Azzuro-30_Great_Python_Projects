import json
import requests
from typing import Final

from datetime import datetime, timezone
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

# Constants
BASE_URL: Final[str] = "http://api.exchangeratesapi.io/v1/latest"
API_KEY: Final[str] = os.getenv("EXCHANGERATESAPI_KEY") or ""


def get_exchange_data(mock: bool = False, cache: bool = False):
    if mock:
        with open("rates.json", "r") as file:
            return json.load(file)

    payload: dict = {"access_key": API_KEY}
    request = requests.get(url=BASE_URL, params=payload)
    data: dict = request.json()

    if cache:
        with open("rates.json", "w") as file:
            json.dump(data, file)

    return data


def get_currency(base: str, rates: dict) -> float:
    currency: str = base.upper()
    if currency in rates:
        return rates.get(currency)

    raise ValueError(f'"{currency}" currency exchange data is not available')


def convert_currency(
    amount: float, convert_from: str, convert_to: str, rates: dict
) -> float:
    from_rate: float = get_currency(convert_from, rates)
    to_rate: float = get_currency(convert_to, rates)

    return round(amount * (to_rate / from_rate), 2)


def main():
    try:
        # data = get_exchange_data(mock=False, cache=True)
        data = get_exchange_data(mock=True)
    except Exception as e:
        print("Failed to fetch exchange rate data.")
        print(f"Details: {e}")
        return

    # Validate required fields
    if not data or "timestamp" not in data or "rates" not in data:
        print("Invalid exchange data received.")
        return

    dt = datetime.fromtimestamp(data["timestamp"], tz=timezone.utc)
    rates = data["rates"]

    print(f"Exchange rates loaded successfully.")
    print(f"Last updated: (UTC): {dt.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Available currencies: {', '.join(rates.keys())}")

    print("\nType 'exit' at any time to quit.\n")

    while True:
        print("--------------------------------------------------")
        print("Enter the currency codes and amount to convert:")

        convert_from: str = input("Convert from: ").strip().upper()
        amount_str: str = input("Amount: ").strip().upper()
        convert_to: str = input("Convert to: ").strip().upper()

        if "EXIT" in (convert_from, convert_to, amount_str):
            print("Goodbye!")
            break

        try:
            amount: float = float(amount_str)
            converted_amount: float = convert_currency(
                amount=amount,
                convert_from=convert_from,
                convert_to=convert_to,
                rates=rates,
            )

            print(
                f"{amount:,.2f} ({convert_from}) is: {converted_amount:,.2f} ({convert_to})"
            )

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print("An unexpected error occurred.")
            print(f"Details: {e}")


if __name__ == "__main__":
    main()
