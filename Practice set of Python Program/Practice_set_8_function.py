# Quick quiz:
# Date : 8/7/23
def func1():
    name = str(input("Enter the name :"))
    print("Good day " + name)


func1()


# Question 1 : find the gratest number==>
def gtr_number():
    print("Enter the 3 number:")
    n = int(input())
    n1 = int(input())
    n2 = int(input())
    if n > n1 and n > n2:
        print("gtr_ number is ", n)
    elif n1 > n and n1 > n2:
        print("gtr_number is ", n1)
    else:
        n2 > n and n2 > n1
        print("gtr_number is ", n2)


# Callling the function:
gtr_number()  # This is the function

# Question 2 : Conversion of the celcius in farenheit==>


def change():
    print("Enter the tempature to convert in to fahrenheit:")
    c = float(input())
    change = (9 / 5) * c + 32
    print("Tempature in fahrenheit is : ", change)
    return c


change()

# Question 3: ans==> To prevent the new line charecter in python using [end = ""]
print("hi ", end="")
print("hello sir")

# Question 4: sum of first n natural number using recursion==>


def recursion():
    print("Enter the number do you want to sum: ")
    n = int(input())
    sum = n * (n + 1) / 2
    print("Sum of the", n, "natural numbers is :", sum)


recursion()

# Question 5: Printing the star pattern:==>


def star():
    n = int(input("Enter the number to printing the  star pattern: "))
    for i in range(1, n + 1):
        print("*" * i)


star()


# Question 6:Conversion==>
def change():
    n = int(input("Enter the number to change inches to cms: "))
    change = n * 2.50
    print(n, " inches to cms is: ", change)


change()


#  Question 8:Multiplecation table:==>
def multi():
    n = int(input("Enter the number which multiplecation table to be printed: "))
    i = 1
    while i <= 10:
        print(n, " x ", i, " = ", n * i)
        i = i + 1


multi()
