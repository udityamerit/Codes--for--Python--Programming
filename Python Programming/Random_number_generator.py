import random

'''
 1. random()===>> Generates a random float number between 0.1 and 1.0(exclude).

 2. shuffle(variable/list)===>> Allows a sequence and returns the sequence in a random order.

 3. uniform(_,_)===>> Returns a random float number between two given parameters.

 4. randint(_,_)===> Returns a random integer number between two given parameters.

 5. choice(variable/list)===>> Returns a random element  which presents in the list.

 6. seed()===>> Initialize the random number generator.

 7. sample()===>> Generates a random floating number from the given range of specified numbers.

 8. randrange(_,_)===>> Generates the random number between the given range with specified step.

 9. choice(variable/list)===>> Generates a random element from the given sequence.

 10. choices(variable/list)===>> Generates a list with a random selection from the given sequence.

'''


# n=random.randint(10,100) # for integer value
# print(n) 

# l = [
def game():
 l = ['water','snack','gun']
 lac = random.choice(l)
 print(lac)

gun = 1
water = 2
snack = 3

water = int(input())


if (game()== 1 and water == 2):
 print("you won")


