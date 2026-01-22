import itertools
import string
import time


def common_guess(word: str) -> str | None:
    with open("10000-words.txt", "r") as file:
        common_words: list[str] = file.read().splitlines()

    for i, common_word in enumerate(common_words, start=1):
        if common_word == word:
            return f'Common match: "{common_word} (#{i:,})'

    return None


def brute_force(
    word: str,
    length: int,
    contains_symbol: bool = False,
    contains_uppercase: bool = False,
    contains_number: bool = False,
) -> str | None:
    chars: str = string.ascii_lowercase

    if contains_symbol:
        chars += string.punctuation
    if contains_uppercase:
        chars += string.ascii_uppercase
    if contains_number:
        chars += string.digits

    target = tuple(word)

    attempts: int = 0

    for guess in itertools.product(chars, repeat=length):
        attempts += 1
        if guess == target:  # compare tuples to speed it up
            return f'Brute force match: "{''.join(guess)}" (#{attempts:,})'

    return None


def main():
    user_password: str = ""
    while len(user_password) < 1 or len(user_password) > 5:
        user_password = input("Enter a 1-5 digi password: ")

    start_time: float = time.perf_counter()
    if common_match := common_guess(user_password):
        print(common_match)
    else:
        print(f"No common match...")
        for i in range(1, 6):
            if brute_force_match := brute_force(
                word=user_password,
                length=i,
                contains_number=True,
                contains_symbol=True,
                contains_uppercase=True,
            ):
                print(brute_force_match)
                break
            else:
                print(f"No {i} digit match...")
    end_time: float = time.perf_counter()

    print(round(end_time - start_time, 2), "s")


if __name__ == "__main__":
    main()
