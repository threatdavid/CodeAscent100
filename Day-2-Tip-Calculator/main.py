# Tip Calculator
def main() -> None:
    print("Welcome to the tip calculator!")
    try:
        bill = float(input("What was the total bill? $"))
        tip = int(input("How much tip would you like to give? 10 %, 12 %, or 15 %: "))

        if tip not in [10, 12, 15]:
            raise ValueError

        people = int(input("How many people to split the bill? "))
        charge = bill * (1 + tip / 100) / people

        print(f"Each person should pay: ${charge:.2f}")
    except ValueError:
        print("That's not a valid value!")


main()
