from dataclasses import dataclass
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


geolocator = Nominatim(user_agent="distance_calculator", timeout=10)


@dataclass
class Coordinates:
    latitude: float
    longitude: float

    def coordinates(self):
        return self.latitude, self.longitude


def get_coordinates(address: str) -> Coordinates | None:
    location = geolocator.geocode(address)

    if location:
        return Coordinates(latitude=location.latitude, longitude=location.longitude)


def calculate_distance_km(home: Coordinates, target: Coordinates) -> float | None:
    if home and target:
        return geodesic(home.coordinates(), target.coordinates()).kilometers


def get_distance_km(home: str, target: str) -> float | None:
    home_coords = get_coordinates(home)
    target_coords = get_coordinates(target)

    if distance := calculate_distance_km(home_coords, target_coords):
        print(f"{home} -> {target}")
        print(f"{distance:.2f} kilometres (apx)")
    else:
        print("Failed to calculate distance.")
        if not home_coords:
            print(f'Failed to get coordiunates for "{home}"')
        if not target_coords:
            print(f'Failed to get coordiunates for "{target}"')


def main():
    print("-" * 40)
    print("Please enter two addresses to calculate distance.")
    print("Type 'exit' at any time to quit.")
    print("-" * 40)
    while True:
        home: str = input("Enter home address: ")
        if "exit" == home.strip().lower():
            print("Bye!")
            break
        target: str = input("Enter target address: ")

        if "exit" == target.strip().lower():
            print("Bye!")
            break
        print("-" * 40)

        get_distance_km(home, target)
        print("-" * 40)


if __name__ == "__main__":
    main()
