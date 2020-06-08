from functions import *

print("Welcome to Geography quiz! Guess the capital city of the country. Enter exit if you want to quit the game.")
play_game()

while True:
    select = input("Do you want to play more? yes/no: ")
    if select.lower() == "yes":
        play_game()
    else:
        print("Goodbye!")
        break


