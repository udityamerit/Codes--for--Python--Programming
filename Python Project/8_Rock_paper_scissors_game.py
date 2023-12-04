import random
print("*******\tWelcome to the rock paper scissors Game*******\t")
paper = '''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

rock = '''---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
scissor = '''   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

while(True):
        ty = input("Do You want to play the Game: Type Y or N: ").upper()
        # ty = ty.upper()
        game_image = [rock, paper, scissor]
        if ty == 'Y':
                user = int(input("What do you choose? Type 0 for Rock, 1 for Paper of 2 for Scissors: "))
                comp = random.randint(0,2)
                if user == 0 and comp == 1:
                        print(f"Computer choice is: ")
                        print(game_image(comp))
                        print(" ")
                        print(f"User choice is: ")
                        print(game_image(user))
                        print("You lose\n")
                elif user == 1 and comp == 2:
                        print(f"Computer choice is: ")
                        print(game_image(comp))
                        print(" ")
                        print(f"User choice is:")
                        print(game_image(user))
                        print("You lose\n")
                elif user == 2 and comp == 0:
                        print(f"Computer choice is: ")
                        print(game_image(comp))
                        print(" ")
                        print(f"User choice is:")
                        print(game_image(user))
                        print("You lose\n")
                elif user == comp:

                        print(f"Computer choice is: ")
                        print(game_image[comp])
                        print(" ")
                        print(f"User choice is: ")
                        print(game_image[user])
                        print(" ")
                        print("Match is drawn!")
                else:
                        print(f"Computer choice is: ")
                        print(game_image[comp])
                        print(" ")
                        print(f"User choice is:")
                        print(game_image[user])
                        print("You won!")
                        print(" ")

        else:
                print("Thankyou!")
                break