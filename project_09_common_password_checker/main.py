def check_password(password: str) -> str:
    with open("passwords.text") as file:
        common_passwords: list[str] = file.read().splitlines()
        for i, common_password in enumerate(common_passwords, start=1):
            if common_password == password:
                return f'"{password}": ❌ password is common (#{i})'
    return f'"{password}": ✅ password is unique'


def main():
    user_password: str = ""
    while len(user_password) < 1:
        user_password = input("Enter a password: ")
    print(check_password(user_password))


if __name__ == "__main__":
    main()
