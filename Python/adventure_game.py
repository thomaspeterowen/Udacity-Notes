import random
import time


def print_pause(str, delay=1):
    print(str)
    time.sleep(delay)


def play_game():
    enemyList = ["Troll", "Vampire", "Ghost", "Gremlin", "Beast", "Caveman"]
    toolBelt = []
    intro()
    adventure(toolBelt, enemyList)


def intro():
    print_pause("\nYou find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.\n")
    print_pause("Rumor has it that something wicked is around here, "
                "and has been terrifying the nearby village.\n")
    print_pause("You look around and can see a small house in the "
                "distance... there is a river below the field...\n")
    print_pause("It looks like the river flows out of a cave...\n")


def adventure(toolBelt, enemyList):
    print_pause("Where would you like to go?\n")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to walk into the river.")
    print_pause("Enter 3 to enter the cave.\n")
    print_pause("What would you like to do?")

    option = valid_input("(Please enter 1, 2 or 3).\n", ['1', '2', '3'])
    if option == "1":
        print_pause("You entered 1.", 1)
        print_pause("You proceed to walk to the house and knock on the "
                    "door...\n")
        house(toolBelt, enemyList)
    elif option == "2":
        print_pause("You entered 2.", 1)
        print_pause("You proceed to walk to the river...\n")
        river(toolBelt, enemyList)
    else:
        print_pause("You entered 3.", 1)
        print_pause("You proceed to enter the cave...\n", 3)
        cave(toolBelt, enemyList)


def house(toolBelt, enemyList):
    print_pause("A witchy looking figure opens the door.")

    if "potion" in toolBelt:
        print_pause("She scowls at you and mutters something under her "
                    "breath... let's get out of here...\n")
        adventure(toolBelt, enemyList)
    else:
        print_pause("What would you like to do?.\n")
        print_pause("Enter 1 to recoil and run away.")
        print_pause("Enter 2 to hear what she has to say.")
        option = valid_input("(Please enter 1 or 2).\n", ['1', '2'])

        if option == "1":
            print_pause("You run away from the woman and head back to "
                        "the field...")
            adventure(toolBelt, enemyList)
        else:
            print_pause("She gives you a potion...")
            toolBelt.append("potion")
            adventure(toolBelt, enemyList)


def river(toolBelt, enemyList):
    print_pause("A water nymph appears.")

    if "dagger" in toolBelt:
        print_pause("It scowls at you and mutters something under it's "
                    "breath... let's get out of here...\n")
        adventure(toolBelt, enemyList)
    else:
        print_pause("I know what you need... and I could help you if I "
                    "wanted to...\n")
        print_pause("It depends on my mood and my mood changes very "
                    "quickly...\n")
        print_pause("What would you like to do?.\n")
        print_pause("Enter 1 to recoil and run away.")
        print_pause("Enter 2 to hear what it has to say.")
        option = valid_input("(Please enter 1 or 2).\n", ['1', '2'])

        if option == "1":
            print_pause("You run away from the water nymph and head back "
                        "to the field...")
            adventure(toolBelt, enemyList)
        else:
            mood = random.choice(["good", "good", "bad"])
            print_pause("My mood now is..." + mood + "!!!")
            if mood == "good":
                print_pause("It reveals a dagger and hands it to you...")
                toolBelt.append("dagger")
                adventure(toolBelt, enemyList)
            else:
                print_pause("The nymph screams at you to leave...")
                print_pause("You should probably visit again when its "
                            "mood is better!")
                adventure(toolBelt, enemyList)


def cave(toolBelt, enemyList):
    enemy = random.choice(enemyList)
    print_pause("A... " + enemy + " appears !!!")

    if "dagger" in toolBelt and "potion" in toolBelt:
        print_pause("The potion magically levitates from your pocket and "
                    "wraps around the " + enemy + ", rendering it as stiff "
                    "as a board...\n")
        print_pause("You take the dagger and kill the " + enemy + ". Well "
                    "done, the villagers will be happy with your work!!\n")
    else:
        print_pause("The " + enemy + " attacks you and you barely escape "
                    "with your life... Maybe next time I should be more "
                    "prepared!\n")
        adventure(toolBelt, enemyList)

def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is invalid. Try again!')

def play_again():
    print_pause("Well done, you played well!\n")
    play_again = valid_input("Play again? y/n \n", ['y', 'n'], 0)
    if play_again == "n":
        print_pause("Thanks for playing, goodbye! :)")
        exit(0)

def game():
    while True:
        play_game()
        play_again()

game()