# Writting code to display
#the calandar of the year:

# --------------Calandar Module-----------------


# import calendar
# y = int(input("Enter the Year: "))
# m = int(input("Enter the Month: "))
# c = calendar.month(y,m)
# print(f"Calandar of the Month: {m} Year: {y} \n",c)
# list = dir(calendar) '''This is used to display all the keywords present in the calendar module'''
# print(list)


# ---------------Math Module----------------------

# import math
# list1 = dir(math)
# print(list1)

# -------------Time Module--------------------------


# import time
# list2 = dir(time)
# print(list2)
# localtime = time.asctime(time.localtime(time.time()))
# print("Time and date is : " ,localtime)

import random
a = [2,4,5,6,78,4]
b= random.choice(a)
print(b)
random.shuffle(a)
c = random.randint(1,100)
print(c)