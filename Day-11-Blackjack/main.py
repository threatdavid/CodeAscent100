from typing import NamedTuple, List


class Card(NamedTuple):
    rank: str
    suit: str


def build_deck() -> List[Card]:
    suit_set = ["Heart", "Diamond", "Club", "Spade"]
    rank_set = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    deck: List[Card] = []

    for suit in suit_set:
        for rank in rank_set:
            card = Card(rank=rank, suit=suit)
            deck.append(card)

    return deck


def shuffle(deck: List[Card]) -> List[Card]:
    pass


def main():
    pass


if __name__ == "__main__":
    main()
