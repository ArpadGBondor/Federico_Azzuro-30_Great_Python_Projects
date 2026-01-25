from typing import Final
from dotenv import load_dotenv
import os
import requests

load_dotenv()  # Load variables from .env
CUTTLY_API_KEY: Final[str] = os.getenv("CUTTLY_API_KEY") or ""
if not CUTTLY_API_KEY:
    raise ValueError("CUTTLY_API_KEY is missing in environment variables.")
CUTTLY_BASE_URL: Final[str] = "https://cutt.ly/api/api.php"


def shorten_link(full_link: str):
    try:
        payload: dict = {"key": CUTTLY_API_KEY, "short": full_link}
        request = requests.get(CUTTLY_BASE_URL, params=payload)
        data: dict = request.json()

        if url_data := data.get("url"):
            if url_data["status"] == 7:
                short_link: str = url_data["shortLink"]
                print("Link:", short_link)
            else:
                print(f"API Error: status {url_data['status']}")
        else:
            print("Error: Invalid API response")
    except requests.RequestException as e:
        print(f"Network or HTTP error: {e}")
        return
    except ValueError:
        print("Error: Unable to decode JSON from response")
        return


def main():
    input_link: str = input("Enter link:")
    shorten_link(input_link)


if __name__ == "__main__":
    main()
