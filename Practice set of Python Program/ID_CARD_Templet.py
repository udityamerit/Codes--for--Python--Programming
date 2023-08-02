#Creating the id card info templets

import time

def info():
    year = str(input("Enter the Year: "))
    name = str(input("Enter the name of Student: "))
    rollno = int(input("Enter the Roll No of the Student: "))
    std = str(input("Enter the Class of the Student: "))
    c = time.asctime(time.localtime(time.time()))
    print(" ")

    print("***********INFO OF THE STUDENT*********** ")
    print(" ")
    print(f" Year: {year} \n Name : {name}\n Roll No: {rollno}\n Class: {std}")
    print(f" Time is: {c}")

print("Enter the Basic details of the student: ")
print(" ")
info()