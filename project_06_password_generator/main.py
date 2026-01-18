import string
import secrets


def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    return False


def contains_number(password: str) -> bool:
    for char in password:
        if char.isnumeric():
            return True
    return False


def contains_symbol(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
    return False


def generate_password(length: int, symbol: bool, uppercase: bool, number: bool) -> str:
    combination: str = string.ascii_lowercase

    if symbol:
        combination += string.punctuation

    if uppercase:
        combination += string.ascii_uppercase

    if number:
        combination += string.digits

    # Pick 3 distinct indexes
    sysrand = secrets.SystemRandom()
    required_indexes = sysrand.sample(range(length), 3)
    upper_i, number_i, symbol_i = required_indexes

    # print(f"Guaranteed indexes: U:{upper_i}, S: {symbol_i}, N: {number_i}")

    new_password: str = ""

    for i in range(length):
        if uppercase and i == upper_i:
            new_password += sysrand.choice(string.ascii_uppercase)
        elif number and i == number_i:
            new_password += sysrand.choice(string.digits)
        elif symbol and i == symbol_i:
            new_password += sysrand.choice(string.punctuation)
        else:
            new_password += sysrand.choice(combination)

    return new_password


if __name__ == "__main__":
    for i in range(1, 6):
        new_pass: str = generate_password(
            length=3, symbol=True, uppercase=True, number=True
        )
        specs: str = (
            f"(U: {contains_upper(new_pass)}, S: {contains_symbol(new_pass)}, N: {contains_number(new_pass)})"
        )
        print(f"{i}: {new_pass} {specs}")
