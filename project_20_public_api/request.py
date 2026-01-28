import requests

if __name__ == "__main__":
    # calling flask script hosted on pythonanywhere.com
    request = requests.get(
        "https://arpadgbondor.pythonanywhere.com/api/random?number=1000&text=API"
    )
    data = request.json()

    print(data)
