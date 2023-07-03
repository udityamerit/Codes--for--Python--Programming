# Number Guessing Game:

n = 18
number_of_guesses= 1
print("Number of guesses is limited to only 9 times : ")
while (number_of_guesses<=9):
    guess_number = int(input("Guess the number.\n"))
    if guess_number>18:
        print("You entered the bigger number please enter the smaller number.\n ")
    elif guess_number<18:
        print("You entered the smaller number please entered the bigger number.\n")
    else:
        print("You won\n")
        print(number_of_guesses,"no. of gusses you took to finish.")
        break
    print(9-number_of_guesses,"no. of guesses left")
    number_of_guesses = number_of_guesses+1
if (number_of_guesses>9):
    print("Game over")    
           