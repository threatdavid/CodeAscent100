# Band Name Generator
def main() -> None:
    print("Welcome to the Band Name Generator!")

    city = input("What's name of the city you grew up in?\n").strip()
    pet = input("What's your pet's name?\n").strip()

    if not city or not pet:
        print("Both the city name and pet name are required to generate a cool band name.")
        return

    band_name = f"{city.capitalize()} {pet.capitalize()}"

    print(f"Your band name could be {band_name}")

main()