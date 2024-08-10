# F string

# me = "anuj"
# a1 = 3
# a2 = "This is %s"%me
# # print(a)

# '''Concept of the Fstring '''

# a = f"this is {me} {a1} {4*54}"
# print(a)



# a = open(r'C:\Users\Uditya\Downloads\assi 1 chy.txt','w')
# for i in range(1,10):
#         print("please enter the data")
#         line = input()
#         l.append(line)
# a.writelines(l)
# a.close()

# a1 = open(r'C:\Users\Uditya\Downloads\assi 1 chy.txt','r')
# print(a1.read())
# a1.close()

info = dict()
l = []
m= []
c = int(input("Enter the no of student: "))

print(l)
print(m)

a  = open('text1.txt','w')
for i in range(c):
        n = input("enter the name of the student: ")
        d = float(input("Enter the cgpa: "))
        l.append(n)
        m.append(d)
        a.write(n)
        a.write(": ")
        a.write(str(d))
        a.write("\n ")



print("DATA written succesfully")


a.close()

a1 = open('text2.txt','w')
for i in range(len(l)):
        if int(m[i]) > 7.5:
                a1.write(" eligible for placement ")
a1.close()

