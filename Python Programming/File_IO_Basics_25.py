# File IO Basics:

"""
Some very common commands :

"r"-- Open file for reading
"w"-- Open a file for writing 
"x"-- Creat file if not exists
"a"-- Add more content to a file
"t"-- Text mode
"b"-- Binary mode 
"+"-- Read and write
 """
'''f = open("anuj.txt","r")
# content = f.read()
# print( "1", content)

# content = f.read()
# print("2", content)
print(f.readlines())  #===> to print the text in the list use this command :
print(f.readline()) #===> print the text line use this command:
print(f.readline())

f.close()'''


# File writing in python:
f = open("anuj.txt","w")
f.write("Ram ek badiya aadmi hai")
f.close( )


# Add the content in the file.txt:
f = open("anuj.txt","a") #===> 'a' is use for to add sentences in the file.txt
f.write("Ram ek badiya aadmi hai\n")
f.close( )


# Handle read and write both:
f = open("anuj1.txt",'r+') #===> Handle read and write use r+ command:
print(f.read())
f.write("My college is started 5 september onwards\n")
f.write("Thank you\n ")

f.close( )

# use of f.tell() command:
f = open ("anuj1.txt")
print(f.tell()) #===> this commad tell the location of the pointer
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())

f.close()


''' f.seek() ===>> This command use to take the pointer in that location where you want ,just give the command in the parenthesis [OR] you can say this command reset the pointer and starts with the Zero index:<<===
''' 
f = open("anuj.txt") #===> this is open the file according  the given "file name .txt" :
print(f.read()) #===> this is read all the content present in the text file :
print(f.tell()) #===> this is show the location of the pointer where is it in that time:
f.seek(0) #===> this is reset the location of the pointer according to the given argument in it :
print(f.tell())

f.close()



# ===>> Open the file using with block:
with open ("anuj1.txt") as f:
    a = f.read()
    print(a)