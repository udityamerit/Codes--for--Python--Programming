# Project-1 : Write a program to run  a lift
import time

def func1():
    print("Number of floors is : 21")
    user_floor = input("Press 0 to open the door:")
    current_floor = 0
    difference = int(user_floor) - int(current_floor)
    if difference == 0:
        print("Opening the Door:")
        print("Enter the floor number:")
        user_floor = int(input())
        print("Closing the Door")
        i = 1
        while i < user_floor:
            print("Floor No: " + str(i) + " Lift is moving up")
            time.sleep(1)
            i = i + 1
    print("Reached at " + str(user_floor) + " floor:\n door opning:")


def func2():
    print("For going down Please:")
    current_floor = int(input("Enter your current floor: "))
    destination_floor = int(input("Enter the destination_floor :"))
    difference = destination_floor - current_floor
    if difference < 0:
        i = current_floor
    while i > destination_floor:
          print("Floor No: " + str(i) + " Lift is moving down")
          time.sleep(1)
          i = i - 1
    print("Reached at " + str(destination_floor) + " floor:\n door opning:")

def func3():
    user_floor = int(input("Enter the destination floor:"))
    current_floor = int(input("Enter the current floor:"))
    difference = int(user_floor) - int(current_floor)
    if difference > 0:
        print("Opening the door:")
        print( "Going up to :" + str(user_floor)) 
        print("Closing the Door:")
        i = current_floor
        while i < user_floor:
            print("Floor No: " + str(i) + " Lift is moving up")
            time.sleep(1)
            i = i + 1
    print("Reached at " + str(user_floor) + " floor:\n door opning:")


print("Please enter:\n 1. for going up:\n 2. for going down:\n 3. for moving up between 1 to 21")
num = int(input())
if num == 1:
    func1()

if num == 2:
    func2()
if num == 3:
    func3()
