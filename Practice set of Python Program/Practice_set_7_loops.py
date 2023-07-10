# Question 1 :Multiplication table using for loop==>
# Date= 8/7/23:
print("Enter the number to print the table:")
num = int(input())
print("Table of the ", num, "is:")
for i in range(1, 11):
    print(num, " X ", i, " = ", num * i)

#     Question 2: identify the name in the list==>

l = ["Harry", "Sohan", "Sachin", "Rahul"]
for element in l:
    if element in l:
        if s in element:
            print(s, "Good Morning")

# Question 3:Multiplication table using while loop==>

print("Enter the number to print the table:")
num = int(input())
print("Table of the", num, "is:")
i = 1
while i < 11:
    print(num, " X ", i, " = ", num * i)
    i = i + 1

# Question 7: printing the star pattern==>

n = int(input("Enter the number to print the star pattern: "))
i = 0
while i < n:
    print("*" * (i + i + 1))
    i = i + 1

# Question 8: printing the star pattern using while loop==>

n = int(input("Enter the number to print the star pattern: "))
i = 1
while i <= n:
    print("*" * i)
    i = i + 1

# Question 9: printing the star pattern in for loop==>
n = int(input("Enter the number to print star pattern :"))

for i in range(1, n + 1):
    print("*" * i)

# Question 10: multiplecation table in reverse order==>

print("Enter the number to print the multiplecation table: ")
n = int(input())
for i in range(10, 0, -1):  # -1 is use to take the loop in reverse order
    print(n, " X ", i, " = ", n * i)
