import time
from crypto_data import get_coins, Coin


def alert(symbol: str, bottom: float, top: float, coins_list: list[Coin]):
    for coin in coins_list:
        if symbol == coin.symbol:
            if coin.current_price < bottom or coin.current_price > top:
                print(coin, "!!!TRIGGERED!!!")
            else:
                print(coin)


if __name__ == "__main__":
    while True:
        coins: list[Coin] = get_coins()
        alert("btc", bottom=73_000, top=75_000, coins_list=coins)
        alert("eth", bottom=1800, top=1900, coins_list=coins)
        alert("apt", bottom=0.74, top=1.40, coins_list=coins)
        time.sleep(60)
