print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/__[Dave]
*******************************************************************************
''')


def main() -> None:
    print("Welcome to Treasure Island!")
    print("You're at a cross road. Where do you want to go?")

    direction = input("""Type "left" or "right"\n""").lower()

    if direction != "left":
        print("Fallen into the abyss. Game Over.")
    else:
        print("You've come to a lake. There is an island in the middle of the lake.")
        decision = input("""Type "wait" to wait for a boat. Type "swim" to swim across.\n""").lower()

        if decision != "wait":
            print("Assaulted by the trout. Game Over.")
        else:
            print("You arrive at the island unharmed. There is a house with 3 doors.")
            door = input("""One red, one yellow and one blue. Which colour do you choose?\n""").lower()

            if door == "blue":
                print("Devoured by the beasts. Game Over.")
            elif door == "red":
                print("Consumed by the flames. Game Over.")
            elif door == "yellow":
                print("Congratulations! You've discovered the treasure! Victory is yours!")
            else:
                print("Defeat! Game Over.")


main()
