import time

def func1():
    print("Number of floors is : 21")
    current_floor = int(input("Enter the current floor:"))
    user_floor = int(input("Enter the destination floor:"))
    print(" ")
    difference = int(user_floor) - int(current_floor)
    if current_floor == 0:
        print("Opening the Door:")
        print("Closing the Door:")
        i = 1
        while i < user_floor:
            print("Floor No: " + str(i) + " Lift is moving up...")
            time.sleep(1)
            i = i + 1
    else:
        difference > 0
        print("Opening the door:")
        print("Closing the Door:")
        print(" ") 
        print( "Going up to :" + str(user_floor)) 
        print(" ")
        
        i = current_floor
        while i < user_floor:
            print("Floor No: " + str(i) + " Lift is moving up...")
            time.sleep(1)
            i = i + 1
               
    print("Reached at " + str(user_floor) + " floor:\n door opning:")
    

def func2():
    print("For going down Please:")
    current_floor = int(input("Enter your current floor: "))
    destination_floor = int(input("Enter the destination_floor :"))
    print(" ")
    print("Closing the Door:")
    difference = destination_floor - current_floor
    if difference < 0:
        i = current_floor
    while i > destination_floor:
          print("Floor No: " + str(i) + " Lift is moving down...")
          time.sleep(1)
          i = i - 1
    print("Reached at " + str(destination_floor) + " floor:\n door opning:")


print("Please enter:\n 1. for going up :\n 2. for going down:")
num = int(input())
if num == 1:
    func1()

if num == 2:
    func2()

