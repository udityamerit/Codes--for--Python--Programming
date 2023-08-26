# a=9
# b=3
# c= sum((a,b)) # This is the built in function 
# print(c)

# User defined function 
# def function1 ():
#     print("hello you are in function1")
# function1()


# def function1 (a,b):
#     print("hello you are in function1",a+b )
# function1(5,7)

# def fun2 (a,b ):
#     avg = (a+b)/2
#     print(avg)
# fun2(5,7)

# def fun2 (a,b ):
#     """This is a function which will calculate avg of two numbers and only work on two numbers"""
#     avg = (a+b)/2
#     print(avg)
#     return avg
# v = fun2(5,7)
# print(v)
# print(fun2.__doc__)

def func1():
    name = str(input("Enter the name :"))
    print("Good day",name)
func1()
