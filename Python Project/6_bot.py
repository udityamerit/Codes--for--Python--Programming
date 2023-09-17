# Write a program to read the sum number and 30% of that number is deleted and than calculate the average of that list:
list = []
n = int(input("Enter the number of the to store the value "))
for i in range(n):
        a = int(input())
        list.append(a)

for e in range(round(len(list)*0.3)):
        del list[e]

list.sort()
print(list)
print(sum(list))
print(sum(list)/(len(list)))

