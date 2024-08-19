import random
from typing import cast, AnyStr, Tuple

import src.visual as visual
import src.data as d


def pick_difficulty() -> d.Level:
    game_difficulty = input("Choose a difficulty level: Easy (1), Medium (2), or Difficult (3): ")

    if game_difficulty not in ["1", "2", "3"]:
        print("The chosen difficulty level is invalid! The game will start on easy level.")
        game_difficulty = "1"  # Default to Easy level

    return cast(d.Level, game_difficulty)


def pick_word(level: d.Level) -> Tuple[AnyStr, d.Category]:
    word_set: d.WordSet = d.WORD_SET[level]
    category: d.Category = random.choice(d.CATEGORY_SET)
    word: AnyStr = random.choice(word_set[category])

    return word, category


def get_hint(category: d.Category) -> AnyStr:
    article = "an" if category[0] in "aeiou" else "a"
    return f"Is {article} {category}"


def main():
    print(visual.GAME_TITLE)
    game_difficulty = pick_difficulty()

    random_word, category = pick_word(level=game_difficulty)
    hidden_word = ["_" for _ in random_word]

    player_life = len(visual.HANGMANPIC) - 1

    while True:
        has_guessed = "_" not in hidden_word
        still_alive = player_life > 0

        if has_guessed or not still_alive:
            break

        print(f"Word to Guess: {"".join(hidden_word)}")
        print(f"Hint: {get_hint(category)}")

        guessed_letter = input(f"\nGuess a Letter: ").lower()

        go_it_right = False
        for i in range(len(random_word)):
            if guessed_letter == random_word[i]:
                hidden_word[i] = guessed_letter if i > 0 else guessed_letter.upper()
                go_it_right = True

        if not go_it_right:
            player_life -= 1
            visual.HANGMANPIC.popleft()
            print(f"You guessed {guessed_letter}, but that letter is not part of the word. You lose a life!")

        print(visual.HANGMANPIC[0])
        print(f"Life: {"💀" if player_life == 0 else ""} {" ".join(["❤" for _ in range(player_life)])}")

    if player_life > 0:
        print(f"You're right! The word is {random_word}. Great effort!")
    else:
        print(f"You've lost! The word was {random_word}. You can try again.")


if __name__ == "__main__":
    main()
