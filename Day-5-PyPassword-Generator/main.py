import string
import random
from typing import List


def main() -> None:
    print("Welcome to the PyPassword Generator!")

    password: List[str] = []

    min_letter = int(input("How many letters do you want in your password?\n"))
    for letter in range(min_letter):
        password.append(random.choice(string.ascii_letters))

    min_symbol = int(input("How many symbols would you like?\n"))
    for symbol in range(min_symbol):
        password.append(random.choice(string.punctuation))

    min_number = int(input("How many numbers would you like?\n"))
    for number in range(min_number):
        password.append(random.choice(string.digits))

    random.shuffle(password)

    print(f"Your password is: {"".join(password)}")


if __name__ == '__main__':
    main()
