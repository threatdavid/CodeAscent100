import os
from typing import TypedDict, List


class Bettor(TypedDict):
    name: str
    bid: float


def get_winner(betting_pool: List[Bettor]) -> Bettor:
    winner = Bettor(name="", bid=0)
    for bettor in betting_pool:
        if bettor["bid"] > winner["bid"]:
            winner = bettor
    return winner


def clear():
    os.environ["TERM"] = "xterm"
    os.system("clear") if os.name == "posix" else os.system("cls")


def main():
    betting_pool: List[Bettor] = []
    while True:
        bettor_name = input("What is your name?: ")
        bettor_bid = float(input("What is your bid?: $"))

        betting_pool.append(Bettor(name=bettor_name, bid=bettor_bid))

        if input("Are there any other bidder? (Y/n): ").lower() == "n":
            break

        clear()

    winner = get_winner(betting_pool)

    print(f"Winner is {winner["name"].capitalize()} with a bid of {winner["bid"]}")


if __name__ == "__main__":
    main()
