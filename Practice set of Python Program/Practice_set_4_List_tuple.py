#  Question 1: printing the list==>

list = []
print("enter the items:")
a = input()
list.append(a)
b = input()
list.append(b)
c = input()
list.append(c)
e = input()
list.append(e)
f = input()
list.append(f)
g = input()
list.append(g)
print(list)

# Question 2: print marks in sorting manner==>

print("Enter your subject wise marks:")
marks = []
s = input()
marks.append(s)
m = input()
marks.append(m)
h = input()
marks.append(h)
e = input()
marks.append(e)
a = input()
marks.append(a)
# print(marks)
marks.sort()
print(marks)

# sorting the match:

match = [45, 67, 90, 78, 66, 2112, 34]
match.sort()
print(match)

#  Question 3 : topple ==>

tp = (1, 45, 32, 45)
tp[3] = 89
print(tp)

# Question 4: sum of the list element==>

list = [23, 12, 45, 67]
print(sum(list))

# Question 5: counting==>

a = (7, 0, 8, 0, 0, 9)

print(a.count(0))
