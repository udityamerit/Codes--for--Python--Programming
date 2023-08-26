#  printing the star pattern using while loop==>

n = int(input("Enter the number to print the star pattern: "))
i = 1
while i <= n:
    print("*" * i)
    i = i + 1

# printing the star pattern using for loop==>

n = int(input("Enter the number to print star pattern :"))
for i in range(1, n + 1):
    print("*" * i)
