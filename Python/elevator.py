from cgi import test
import time

# print and pause function
def print_pause(str):
    print(str)
    time.sleep(1)

print_pause("You have just arrived at your new job!")
print_pause("You are in the elevator.")

while True:
    floor = input("Please enter the number for the floor you would like to visit: \n1. Lobby \n2. Human resources \n3. Engineering department\n")
    if floor == "1":
        print_pause("You push the button for the first floor.")
        print_pause("After a few moments, you find yourself in the lobby.")
        print_pause("Where would you like to go next?")
    elif floor == "2":
        print_pause("You push the button for the second floor.")
        print_pause("After a few moments, you find yourself in the human resources department.")
        print_pause("Where would you like to go next?")
    elif floor == "3":
        print_pause("You push the button for the third floor.")
        print_pause("After a few moments, you find yourself in the engineering department.")
        print_pause("Where would you like to go next?")
    else:
        print_pause("I'm sorry I didn't understand...")