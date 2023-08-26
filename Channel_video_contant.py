# 1.
# Importing some important modules
#---calendar module------

# import calendar
# c = calendar.month(2023,3)
# print(c)

# -------time module-----
# import time
# t = time.asctime(time.localtime(time.time()))
# print(t)


# -----random module----
# import random
# a=[2,3,4,5,65]
# c = random.choice(a)
# print(f"random number is :",{c})
# random.shuffle(a)
# print(f"randam list is: {a}")
# random.shuffle(a)
# print(f"randam list is: {a}")
# random.shuffle(a)
# print(f"randam list is: {a}")
# random.shuffle(a)
# print(f"randam list is: {a}")

#--------------------------------------------------------------------------

# 2.
# Making of the basic info of a student
# def info():
#     name = str(input("Enter the Student name: "))
#     roll_no = int(input("Enter the Roll of the Student: "))
#     std = str(input("Enter the Class of the Student: "))
#     print(" ")
#     print("*************INFO OF THE STUDENT**********")
#     print(" ")
#     print(f" Name: {name} \n Roll No: {roll_no}\n Class: {std}")

# print("Enter the details of the Student: ") 
# info()

#--------------------------------------------------------------------------

# 3.
# create a class to print the name of the 
#laptop and his modle name and price:

# class Laptop:
#     def __init__(self,name,modle,price):
#         self.name = name
#         self.modle = modle
#         self.price = price
#     def discount(self,num):
        
#         return (self.price) - ((self.price)*num/100)
        
# l = Laptop("Hp","rtl8723de",35000)
# print(f"Name of the laptop is: {l.name}")
# print(f"Modle number of the laptop is: {l.modle}")
# print(f"Price of the laptop is: {l.price}")
# print(f" New price {l.discount(10)}")

#--------------------------------------------------------------------------

# 4.
#use of NORMAL methods

# a = int(23)
# name = str("Hi NCERT SOLUTION!")
# print("integer value is: ",a)
# print("Name is : ",name)

#use f-string

# print(f" Integer is: {a} \n Name of the channel is: {name}")

#--------------------------------------------------------------------------

# 5.
# Create a multilevel inheritance

# class Phone:
#     def __init__(self,name,modle,price):
#         self.name = name
#         self.modle = modle
#         self.price = price

#     def full_detail(self):
#             return f" Name is: {self.name} \n\
#                 modle name is: {self.modle} \n \
#                         Price is: {self.price} rs."
        
# class Smartphone(Phone):
#     def __init__(self, name, modle, price,life,capacity):
#         super().__init__(name, modle, price)
#         self.life = life
#         self.capacity = capacity

#     def full_details(self):
#           return f" Name is: {self.name}\n modle name is: {self.modle} \n Price is: {self.price} rs. \n Life is: {self.life} days\n  Capacity is: {self.capacity} percent"

# p = Phone("vivo","34rt43",32000)
# print("Phone details is: ", p.full_detail())
# print("--------------------------------------")
# p2 = Smartphone("onepluse","35tu34rt43",52000,45,100)
# print("SmartPhone details is: ", p2.full_details())

#--------------------------------------------------------------------------

#6.
# Sorting in the python

# list = []
# n = int(input("Enter the number of valuse do you want to add in the list:"))
# i = 0
# while(i<n):
#     m = int(input("Enter the number: "))
#     list.append(m)

#     i = i+1

# print(list)
# print("List after sorting: ")
# list.sort()
# print(list)
#--------------------------------------------------------------------------

# 7.

# Access Specifiers in python
'''1. Public
   2. Protected
   3. Private'''

# class Work:
#     age = 34 # this is the public variable
#     _salary = 34000 # this is a protected variable
#     __phone_no = 23453212 # this is a privete variable
#     def __init__(self,name, roll ):
#         self.name = name
#         self.roll = roll

#     def det(self):
#         return f" Name is: {self.name}\n Roll is: {self.roll}"

# emp = Work("Uditya","Programar")
# # Access the public variable:
# print(emp.det())
# # Access the protected variable:
# print(emp._salary)
# # Access the privete variable:
# print(emp._Work__phone_no) 

#--------------------------------------------------------------------------
#8.
# Question 3: Detecting the spam massages

# print("Write Your massage:")
# massage = str(input())
# spam = {"make a lots of money", "buy now", "subscribe this", "click this"}
# for element in spam:
#     print(element)
#     if massage in spam:
#         print("This massage is a spam massage.")


# print("Enter the name :")
# name = str(input())
# list = ["ram", "shyam", "ram", "bala", "mala", "gullu"]
# for element in list:
#     if name in list:
#         print("This name is present in list.")
#         break
#     else:
#         print("Name is not present in the list")
# print(f" numbers of name present in the list: {list.count(name)}")

# creating a function in python

# Access of the element of a list

# list = [34,56,32,"Anuj","Ram","Manoj",34.5,"set"]

# print(list)
# for element in list:
#     print(element)


# Making of Basic Calculator
# def opretor():
#     print("Enter the opretor:")
#     opretor = int(input())
#     if opretor == 1: 
#        print(f"{num1} + {num2} = {num1+num2}")
#     elif opretor == 2:
#         print(f"{num1} - {num2} = {num1-num2}")
#     elif opretor == 3:
#         print(f"{num1} * {num2} = {num1*num2}")
#     elif opretor == 4:
#         print(f"{num1} / {num2} = {num1/num2}")
    

    

# print("Enter the number 1:")
# num1 = float(input())
# print("Enter the number 2:")
# num2 = float(input())
# print("Enter the oprator:\
#    1 for +\n 2 for -\n 3 for *\n 4 for /:   ")
# opretor()
# ------------------------------------------------------------------------------------------
'''
Write a program to add element from one list to another but if the element if present in the other list do not add the element 
eg:-
[1,2,3,4,4,4,5,6,7,7,8]

Index element Choose - 
5 -> element at index 5 is4
1 -> element at index 1 is 2
3 -> element at index 3 is 4
[4,2]

'''

print("Enter the elements  of list:")
list = [1,2,1,2,33,2,1,2,3,4,5,4,3,2,1,] #isme 5 hi kyu hai
list1 = []
# a = int(input())
# list.append(a)
# b = int(input())
# list.append(b)
# c = int(input())
# list.append(c)
# d = int(input())
# list.append(d)
# e = int(input())
# list.append(e)
# print(" ")

print(f"Your first list:{list}")
print(" ") 


#CIdhar 3 hi kyu hai

print("Enter your indexes:")
x = int(input())
y = int(input())
z = int(input())
print(" ")


if (list[x]==list[y]==list[z]):
    list1.append(list[x])

elif(list[x]==list[y]!=list[z]):
    list1.append(list[y])
    list1.append(list[z])

elif(list[x]!=list[y]==list[z]):
    list1.append(list[x])
    list1.append(list[z])

else:
    list1.append(list[x])
    list1.append(list[y])
    list1.append(list[z])

print(" ")

print(f"Your second list:{list1}")