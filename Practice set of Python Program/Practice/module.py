
# with open("re.txt",'r+') as f:
#         a = f.readlines()
#         l = ""
#         for i in a:
#                 l = l+str(i)+""

# f.close()

# print(type(l))
# l = l.split()

# print(l)
# # for i in l:
# #         print(l.count(i))

# c = [ l.count(i) for i in l if max([l.count(i) for i in l]) == l.count(i)]
# print(c[0])


# # using counters
# from collections import Counter
# l = Counter(l)
# k = []
# for key, value in l.items():
#         k.append(value)
#         if max(k)==value:
#                 print(key)


# from tkinter import *

# win = Tk()


# def Submit():
#         print(f"Name is: {name}\n mobile no is: {mob}\n")

# win.title("Menu card")
# win.geometry("400x400")

# win.config(bg="lightblue")


# Label(win,text="MenuCard options",font="robotomono,15,bold",bg="orange",borderwidth=5).grid(row=0,column=3)

# Label(win,text="Name",font="robotomono,10,bold",bg="lightblue").grid(row=1,column=2,pady=5)

# Label(win, text="Mobile No. ", font="robotomono,10,bold",bg="lightblue").grid(row=2,column=2)

# Label(win, text = "Price", font = "robotomono,10,bold",bg= "lightblue").grid(row=3,column=2)



# name = StringVar()
# mob = StringVar()
# price = IntVar()

# Entry(win,textvariable = name,font="robotomono,10").grid(row=1,column=3)
# Entry(win, textvariable =mob, font = "robotomono,10" ).grid(row=2,column=3)
# Entry(win, textvariable = price, font = "robotomono,10").grid(row=3,column=3)

# Button(text="Submit",font = "robotomono,10,bold",bg="lightblue",command=Submit).grid(row=6,column=3)

# win.mainloop()








from tkinter import *

root = Tk()
root.title("GUI dashboard")
root.geometry("500x500")
root.config(background="lightblue")

def detail():
        print(f"name: {namevalue}\n mobile no: {mobvalue}\n Price: {pricevalue}")

        with open("gui.txt","a") as f:
                f.write(f"name: {namevalue}\n mobile no: {mobvalue}\n Price: {pricevalue}")

def exit():
        root.destroy()

Label(root,text="My first menucard",font="robotomono,25,bold",borderwidth=5,foreground="black",bg="gold").grid(row=0,column=2)

# name of some menu 
Label(root,text="Name ",font=("robotomono",15,"bold"),bg="white",fg="black",borderwidth=5).grid(row=1,column=2,pady=10)

Label(root,text="mobile",font="robotomono,15,bold",bg="white",fg="black",borderwidth=5).grid(row=2,column=2,pady=10)

Label(root,text="Price",font="robotomono,15,bold",fg="black",bg="white",borderwidth=5).grid(row=3,column=2,pady=10)

# user input
namevalue = StringVar()
mobvalue = StringVar()
pricevalue = IntVar()

#Entry

Entry(root,textvariable=namevalue,font="robotomono,15,bold",fg="blue").grid(row=1,column=3)
Entry(root,textvariable=mobvalue,font="robotomono,15,bold",fg="blue").grid(row=2,column=3)
Entry(root,textvariable=pricevalue,font="robotomono,15,bold",fg="blue").grid(row=3,column=3)


Button(root,text="Submit",font="robotomono,15",background="green",fg="white",relief="raised",borderwidth=5,command=detail).grid(column=3)

Button(root,text="Exit",font="robotomono,15,bold",fg="red",bg="white",relief="groove",borderwidth=5,command=exit).grid(column=3,pady=15)


root.mainloop()






# mat1 = [[0,0,0],
#         [0,0,0],
#         [0,0,0]]

# for i in range(len(mat1)):
#         for j in range(len(mat1[i])):
#                 c = int(input(f"Plese enter the value at the index of matrix: {i,j} : "))
#                 mat1[i][j]=c
                

# print(mat1)