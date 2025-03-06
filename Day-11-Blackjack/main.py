import random
from typing import NamedTuple, List


class Card(NamedTuple):
    rank: str
    suit: str


SUITS = ["♥", "♦", "♣", "♠"]
RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
CARD_TEMPLATE = (
    "┌──────┐\n"
    "| {number: <5}|\n"
    "|   {symbol}  |\n"
    "|      |\n"
    "└──────┘"
)


def build_deck() -> List[Card]:
    deck = [Card(rank, suit) for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck


def get_score(hand: List[Card], is_dealer_turn=True) -> int:
    safe_hand = hand.copy()
    if not is_dealer_turn:
        safe_hand.pop(0)

    hand_score = 0
    aces_count = 0

    for card in safe_hand:
        if card.rank.isdigit():
            hand_score += int(card.rank)
        elif card.rank in ["J", "Q", "K"]:
            hand_score += 10
        else:
            hand_score += 11
            aces_count += 1

    while hand_score > 21 and aces_count:
        hand_score -= 10
        aces_count -= 1

    return hand_score


def draw_hand(hand: List[Card], is_dealer_turn=True) -> None:
    display_hand = hand.copy()
    if not is_dealer_turn:
        display_hand[0] = Card(rank=" ", suit=" ")

    cards = [CARD_TEMPLATE.format(number=card.rank, symbol=card.suit) for card in display_hand]
    for line in zip(*[card.split("\n") for card in cards]):
        print("  ".join(line))


def get_dealer_choice(dealer_score: int) -> str:
    return "H" if dealer_score < 17 else "S"


def print_hand(hand: List[Card], is_dealer: bool, reveal: bool = False) -> None:
    title = "Dealer's" if is_dealer else "Your"
    print(f"{title} Hand:")
    draw_hand(hand, is_dealer_turn=reveal or not is_dealer)
    
    if is_dealer and not reveal:
        score = get_score(hand, is_dealer_turn=False)
        print(f"Dealer's Known Score: {score}")
    else:
        score = get_score(hand)
        print(f"{title} Score: {score}")


def handle_player_turn(player_hand: List[Card], dealer_hand: List[Card], deck: List[Card]) -> bool:
    while True:
        print_hand(dealer_hand, is_dealer=True, reveal=False)
        print_hand(player_hand, is_dealer=False)

        choice = input("Do you want to [H]it or [S]tand? ").upper()

        if choice == "H":
            player_hand.append(deck.pop())
            player_score = get_score(player_hand)

            print_hand(dealer_hand, is_dealer=True, reveal=False)
            print_hand(player_hand, is_dealer=False)

            if player_score > 21:
                print("You busted. The dealer wins!")
                return True
            if player_score == 21:
                print("You got a Blackjack!")
                return True
        else:
            return False


def handle_dealer_turn(dealer_hand: List[Card], player_hand: List[Card], deck: List[Card]) -> None:
    while True:
        dealer_score = get_score(dealer_hand)
        player_score = get_score(player_hand)

        if dealer_score >= 17:
            print("The dealer decided to stand!")
            print_hand(dealer_hand, is_dealer=True, reveal=True)
            print_hand(player_hand, is_dealer=False)

            print("\nDealer's Final Score:", dealer_score)
            print("Your Final Score:", player_score)

            if dealer_score > player_score:
                print("\nThe dealer wins!")
            elif dealer_score < player_score:
                print("\nYou win!")
            else:
                print("\nIt's a tie!")
            return

        dealer_hand.append(deck.pop())
        print("The dealer decided to hit!")
        print_hand(dealer_hand, is_dealer=True, reveal=True)
        print_hand(player_hand, is_dealer=False)

        if get_score(dealer_hand) > 21:
            print("The dealer busted. You win!")
            return
        if get_score(dealer_hand) == 21:
            print("The dealer got a Blackjack!")
            return

        input("Press Enter to continue...\n")


def main():
    deck = build_deck()
    dealer_hand = [deck.pop(), deck.pop()]
    player_hand = [deck.pop(), deck.pop()]

    game_ended = handle_player_turn(player_hand, dealer_hand, deck)

    if not game_ended:
        print("\n\n")
        handle_dealer_turn(dealer_hand, player_hand, deck)


if __name__ == "__main__":
    main()