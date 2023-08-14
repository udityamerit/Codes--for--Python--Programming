# Making of Basic Calculator

def opretor():
    print("Enter the opretor:")
    opretor = int(input())
    if opretor == 1: 
       print(f"{num1} + {num2} = {num1+num2}")
    elif opretor == 2:
        print(f"{num1} - {num2} = {num1-num2}")
    elif opretor == 3:
        print(f"{num1} * {num2} = {num1*num2}")
    elif opretor == 4:
        print(f"{num1} / {num2} = {num1/num2}")
    

    

print("Enter the number 1:")
num1 = float(input())
print("Enter the number 2:")
num2 = float(input())
print("Enter the oprator:\
   1 for +\n 2 for -\n 3 for *\n 4 for /:   ")
opretor()