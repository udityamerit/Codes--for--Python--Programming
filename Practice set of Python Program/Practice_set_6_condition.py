# Date = 3/7/23:

# Question 1 : find the greatest number
print("Enter the four numbers:")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a > b and a > c and a > d:
    print("Greatest number is: ", a)
elif b > a and b > c and b > d:
    print("Greatest number is: ", b)
elif c > a and c > b and d > b:
    print("Greatest number is: ", c)
elif d > a and d > c and d > b:
    print("Greatest number is: ", d)

# Question 2:display the result

print("Enter your marks of three subject:")
a = int(input())
b = int(input())
c = int(input())
avg = (a + b + c) / 3
print("your percentage is = ", avg)
if a == b == c > 33 and avg > 40:
    print("Congretulation!,You have pramoted")
else:
    print("Sorry!,you hav't prometed")

# Question 3: Detecting the spam massages

print("Write Your massage:")
massage = str(input())
spam = {"make a lots of money", "buy now", "subscribe this", "click this"}
for element in spam:
    # print(element)
    if massage in element:
        print("This massage is a spam massage.")


#  Question 4: Calculate the length of the charecter

print("Enter Your name :")
name = str(input())
# print(len(name))
if len(name) > 10:
    print("Length contains more than 10 character")

# Question 5: Find name is present in list or not

print("Enter the name :")
name = str(input())
list = ["ram", "shyam", "lala", "bala", "mala", "gullu"]
for element in list:
    if name in list:
        print("This name is present in list.")
        break
    else:
        print("Name is not present in the list")

# Question 6: Grade Calculator

print("Enter Your Totle Marks:")
marks = int(input())
if 90 <= marks < 100:
    print("Your Grade is =  Ex")
elif 80 <= marks < 90:
    print("Your Grade is = A")
elif 70 <= marks < 80:
    print("Your Grade is = B")
elif 60 <= marks < 70:
    print("Your Grade is = C")
elif 50 <= marks < 60:
    print("Your Grade is = D")
elif marks < 50:
    print("Your Grade is = F")

# Question 7: detecting the massage==>

print("Enter the post:")
post = str(input())
list = ["harry"]
for element in list:
    if element in post:
        print("Yes this post is talking about the harray")
    else:
        print("No this post is not talking about the harry")
