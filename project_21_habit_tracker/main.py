import pandas as pd
from tabulate import tabulate
from datetime import datetime

from habit_tracker import track_habit, Habit


def main():
    habits: list[Habit] = [
        track_habit("coffee", datetime(2023, 6, 6, 8), cost=1, minutes_used=5),
        track_habit(
            "wasting time", datetime(2024, 6, 5, 6), cost=60, minutes_used=60 * 12
        ),
        track_habit(
            "quit smokingwasting time",
            datetime(2024, 6, 7, 6),
            cost=15,
            minutes_used=30,
        ),
    ]

    df = pd.DataFrame(habits)

    print(tabulate(df, headers="keys", tablefmt="psql"))


if __name__ == "__main__":
    main()
