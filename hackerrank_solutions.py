# print the maximun and minimum sum of a list
list = [1,2,3,4,5]
list1 = []

for i in range(len(list)):
        a = sum(list) - list[i]
        list1.append(a)
print(min(list1)," ",max(list1))

list2 = [1,2,3]
list2 = str(list2)
print(list2)