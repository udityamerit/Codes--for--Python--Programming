# Snake Water Gun Game:
import random

num = random.randint(0, 2)

print("Welcome to Snack-Water and Gun game: ")
print("Number_of_chances is only 10")
comp = []
User = []
draw = []

def game(num, user):
    a = "Match is draw"
    b = "computer won the game"
    c = "You won the game"
        
    if num == user:
        print(a)
        draw.append(a)
    elif num == 0 and user == 1:
        print(b)
        comp.append(b)
    elif num == 1 and user == 2:
        print(b)
        comp.append(b)
    elif num == 2 and user == 0:
        print(b)
        comp.append(b)
    else:
        print(c)
        User.append(c)


Number_of_chances = 1
while Number_of_chances <= 10:
    print(" Plese Enter the: \n 0 for snake: \n 1 for Water:\n 2 for Gun:")
    user = int(input("Select the number:"))
    print("comp is selected:", num)
    print("user is selected:", user)

    game(num, user)
    print("Number_of_chances left", Number_of_chances - 10)
    Number_of_chances = Number_of_chances + 1
    print(" ")

# print(comp)
print("Computer won ",len(comp),"times")
# print(User)
print("You won ",len(User),"times")
# print(draw)
print("Game is draw ",len(draw),"times")
print(" ")

if len(comp)>len(User):
    print(" Finaly Computer won the game")
elif len(comp)<len(User):
    print(" Finaly You won the game")
else:
    print("Game is draw")
print(" ")
print("Game is ended")
