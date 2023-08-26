#  Project  on  Helth Management system:

#  Important instruction is ===> First make all the file which is used in the programming : 


print("WELCOME TO THE HELTH MANAGEMENT SYSTEM :\n")


def Harry():
    f= open("Harry.txt", "r+")
    name = str(input("Enter your name: \n"))
    f.write(name)
    print("Successfully added")

    f.close()


def Rohan():
    f= open("Rohan.txt", "r+")
    name = str(input("Enter your name: \n"))
    f.write(name)
    print("Successfully added")

    f.close()


def Harry_Exercise():
    f = open("Harry_Exercise.txt", "r+")
    exe = str(input(" You are in Harry_Exercise file:\n  Please Enter your exersice do you want to practice : \n"))
    f.write("\n")
    f.write(exe)
    print("Successfully added")

    f.close()


def Rohan_Exercise():
    f = open("Rohan_Exercise.txt", "r+")
    exe = str(input(" You are in Rohan_Exercise file:\n Please Enter your exersice do you want to practice : \n"))
    f.write("\n")
    f.write(exe)
    print("Successfully added")

    f.close()


def Harry_Diet():
    f = open("Harry_Diet.txt", "r+")
    diet = str(input(" You are in Harry_Diet file:\n  Please Enter your diet do you want to eat for fit your body: \n"))
    f.write("\n")
    f.write(diet)
    print("Successfully added")

    f.close()


def Rohan_Diet():
    f = open("Rohan_Diet.txt", "r+")
    diet = str(input(" You are in Rohan_Diet file: \n  Please Enter your diet do you want to eat for fit your body : \n"))
    f.write("\n")
    f.write(diet)
    print("Successfully added")

    f.close()

# def harry_readexe():
#     f= open("Harry_Exercise.txt", "r")
#     content = (f.read)
#     print(content)
#     f.close()

with open ("Harry_Exercise.txt") as f:
    b = f.read()

# def harry_readdiet():
#     f= open("Harry_Diet.txt", "r")
#     content = (f.read)
#     print(content)
#     f.close()

with open ("Harry_Diet.txt") as f:
    a = f.read()
    # print(a)


def rohan_readexe():
    f= open("Rohan_Exercise.txt", "r")
    content = (f.read())
    print(content)
    f.close()


def rohan_readdiet():
    f= open("Rohan_Diet.txt", "r")
    content = (f.read())
    print(content)
    f.close()



print("Please Enter \n 1. for Add something OR write in Harry's File: \n 2. for Add something OR write in  Rohan's File : \n 3. to see the contant of the Harry's Exercise File: \n 4. to see the contant of the Rohan's Exercise File \n 5. to see the contant of the Harry's Diet File: \n 6. to see the contant of the Rohan's Diet File :")
num = int(input())
if(num==1):
    Harry()
    number = int(input("Enter 1. for Add something OR write in  Harry's Exercise: \n 2. for Add something OR write in Harry's Diet : "))

    if(number==1):
        Harry_Exercise()

    if(number==2):
        Harry_Diet()

if(num==2):
    Rohan()
    n = int(input("Enter 1. for Add something OR write in Rohan's Exercise: \n 2. for Add something OR write in Rohan's Diet :\n "))
    
    if(n==1):
        Rohan_Exercise()
        
    if(n==2):
        Rohan_Diet()

if (num == 3):
    # harry_readexe()
    print("Harry_Exercise file is : \n", b)

if (num == 4):
    rohan_readexe()

if (num == 5):
    # harry_readdiet()
    print( "Harry_Diet file is : \n ", a)

if (num == 6):
    rohan_readdiet()
