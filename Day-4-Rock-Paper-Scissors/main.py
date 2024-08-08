from random import randint
import emoji


def main() -> None:
    choices = [
        {
            "name": "Rock",
            "emoji": emoji.emojize(":raised_fist:", language="en")
        },
        {
            "name": "Paper",
            "emoji": emoji.emojize(":raised_back_of_hand:", language="en")
        },
        {
            "name": "Scissors",
            "emoji": emoji.emojize(":victory_hand:", language="en")},
    ]

    user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n")

    if user_choice not in ["0", "1", "2"]:
        print("Your choice is invalid. Try again!")
        return

    user_choice = int(user_choice)
    computer_choice = randint(0, 2)

    print(f"You chose: {choices[user_choice]["emoji"]}")
    print(f"Computer chose: {choices[computer_choice]["emoji"]}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice - computer_choice) % 3 == 1:
        print("You win!")
    else:
        print("You lose!")


if __name__ == "__main__":
    main()
