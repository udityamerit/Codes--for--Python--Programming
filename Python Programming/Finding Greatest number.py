# Question 1 : Finding the greatest number input by user

def gtr_number():
    print("Enter the 3 number:")
    n=int(input())
    n1=int(input())
    n2=int(input())
    if n>n1 and n>n2:
        print("gtr_ number is ",n)
    elif n1>n and n1>n2:
        print("gtr_number is ",n1)
    else:
        n2>n and n2>n1
        print("gtr_number is ",n2)
        
# Callling the function:
gtr_number() #This is the function
