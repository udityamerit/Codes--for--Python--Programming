# def factorial_iterative(n):
#     fac = 1 
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac
    
# number = int(input("Enter the number"))
# print(factorial_iterative(number))

def factorial_recursive(n):
    if n==1 and n==0:
        return 1
    else:
        return n * factorial_recursive(n-1)
number = int(input("Enter the number"))
print(factorial_recursive(number))