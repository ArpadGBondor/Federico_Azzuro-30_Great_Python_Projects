from bs4 import BeautifulSoup
import requests
import re


def get_soup() -> BeautifulSoup:
    headers: dict = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
    }

    request = requests.get("https://www.bbc.com/news", headers=headers)
    request.raise_for_status()

    html: bytes = request.content

    return BeautifulSoup(html, "html.parser")


def get_headlines(soup: BeautifulSoup) -> list[str]:
    headlines: set[str] = set()

    for h in soup.find_all("h2"):
        headline: str = h.get_text(strip=True).lower()
        headlines.add(headline)

    return sorted(headlines)


def check_headlines(headlines: list[str], term: str):
    term_list: list[str] = []
    terms_found: int = 0

    # raw f-string -> !!!don't touch my backslashes!!! -> better for regex
    pattern = rf"\b{term.lower()}\b"

    for i, headline in enumerate(headlines, start=1):
        if re.search(pattern=pattern, string=headline):
            terms_found += 1
            term_list.append(headline)

    print("-" * 40)
    if terms_found:
        print(f'Term "{term}" was mentioned {terms_found} times.')
        print("-" * 40)
        for i, headline in enumerate(term_list, start=1):
            print(f'{i}: "{headline.capitalize()}"')
    else:
        print(f'No matches found for term: "{term}"')
    print("-" * 40)


def main():
    soup = get_soup()
    headlines = get_headlines(soup)

    print("-" * 40)
    print(f"{len(headlines)} headlines scraped from BBC news.")
    print("-" * 40)
    for i, headline in enumerate(headlines, start=1):
        print(f'{i}: "{headline.capitalize()}"')
    print("-" * 40)
    print("Type 'exit' at any time to quit.")
    print("-" * 40)
    while True:
        user_input: str = input("Please enter search term: ")
        if user_input.lower() == "exit":
            print("Bye!")
            break
        check_headlines(headlines, user_input)


if __name__ == "__main__":
    main()
