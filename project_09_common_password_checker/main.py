def check_password(password: str) -> str:

    # with ... as ...:
    #   works with context managers
    #       context manager is any object that defines:
    #           __enter__() -> returns value used in "as ..."
    #               (set up context)
    #           __exit__()
    #               (clean up context)
    with open("passwords.text") as file:
        common_passwords: list[str] = file.read().splitlines()

    # the scope of common_passwords is check_password function
    #   - if, for, with, etc. do not create a new scope
    #   - Only functions, classes, and modules create scopes
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
