def add():
    print("for the Addition of two numbers...")
    n1 = float(input("Enter the number:"))
    n2 = float(input("Enter the number:"))
    c = n1+n2
    print("Your sum of two numbers = ",c )
    print("************************************ ")
    print(" ")

def substract():
    print("for the Substraction of two number...")
    n1 = float(input("Enter the number:"))
    n2 = float(input("Enter the number:"))
    c = n1-n2
    print("Your substraction of two numbers = ",c)
    print("************************************ ")
    print(" ")

def multiplication():
    print("for the Multiplication of two number...")
    n1 = float(input("Enter the number:"))
    n2 = float(input("Enter the number:"))
    c = n1*n2
    print("Your multiplication of two numbers = ",c)
    print("************************************ ")
    print(" ")

def divide():
    print("for the Division of two number...")
    n1 = float(input("Enter the number:"))
    n2 = float(input("Enter the number:"))
    c = n1/n2
    print("Your division of two numbers = ",c)
    print("************************************ ")
    print(" ")

print("\n\t *************Welcome to the calculator**************** ")
print(" ")
while(True):
    print(f" Please enter the==>\n 1 for Addition:\n 2 for Substraction:\n 3 for Multiplication:\n 4 for Division:\n 0 for Quit the calculation:")
    x = int(input("Enter the number: "))
    if x == 1:
        add()

    elif x == 2:
        substract()

    elif x == 3:
        multiplication()

    elif x == 4:
        divide()

    elif x == 0:
        print("*************Exit the calculator**************** ")
        break
    else:
        print("Enter the valid input...")
        