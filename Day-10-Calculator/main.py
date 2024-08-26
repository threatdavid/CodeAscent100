def sum(a: float, b: float) -> float:
    return round(a + b, 2)


def subtract(a: float, b: float) -> float:
    return round(a - b, 2)


def multiply(a: float, b: float) -> float:
    return round(a * b, 2)


def divide(a: float, b: float) -> float:
    return round(a / b, 2)


def main():
    result = None
    while True:
        a = float(input("What's the first number?: ")) if result is None else result
        operation = input("Pick an operation: +, -, *, /\n")
        b = float(input("What's the next number?: "))

        if operation == "+":
            result = sum(a, b)
        elif operation == "-":
            result = subtract(a, b)
        elif operation == "*":
            result = multiply(a, b)
        elif operation == "/":
            result = divide(a, b)
        else:
            print("I'm not designed for it!")

        print(f"The result of {a} {operation} {b} is {result}")

        if input(f"Would you like to continue calculating with {result}? [Y/n]: ").lower() == "n":
            break


if __name__ == "__main__":
    main()
