import string
from view import view


def cipher(sentence: str, action: str, shift: int = 3) -> str:
    alphabet, crypt = list(string.ascii_lowercase), ""

    for letter in sentence:
        if letter.isalpha():
            index = alphabet.index(letter)
            index += shift if action == "encrypt" else -shift
            crypt += alphabet[index % 26]
        else:
            crypt += letter if letter != " " else ""

    return crypt


def main():
    print(view.CAESAR_CIPHER_ART)

    while True:
        action = input("""Type "encrypt" to encrypt a statement or "decrypt" to decrypt it:\n""")

        if action not in ["encrypt", "decrypt"]:
            print("Sorry, I wasn't designed for it.")

        statement = input(f"Type the statement to {action}:\n").lower()
        shift = int(input("Type the shift value:\n"))

        print(f"The {action}ed statement is: {cipher(statement, action, shift)}")

        if input("Would you like to try again? (y/n) ").lower() == "n":
            break


if __name__ == "__main__":
    main()
