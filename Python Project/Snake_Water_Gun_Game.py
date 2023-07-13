# # Poject-3 : Snake_Water and Gun_Game:

import random

def game(comp, user):
    if comp == user:
        return 0

    if comp == 0 and user == 1:
        return -1

    if comp == 1 and user == 2:
        return -1

    if comp == 2 and user == 0:
        return -1

    return 1


comp = random.randint(0, 2)
print("Welcome to the Snake_Water and Gun_Game :")

user = int(input(" Please select : 0 for snack, 1 for water and 2 for gun:\n"))

score = game(comp, user)
print("you selected :", user)
print("computer selected :", comp)

if score == 0:
    print("game is draw")
elif score == 1:
    print("You won")
else:
    print("You lose")
