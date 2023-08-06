# 58 Lecture: staticmethod
class Person:
        
    @staticmethod
    def hello(string):
        print("hello static method")
        print('hello method' , string)

Person.hello("rohan")
   
# ----------------------------------------------------

# 59 Lacture: incapsulation & Abstraction:

# ===> Incapsulation : Hide all the technicle detales of the program is incapsulation: <== OR ==> When we hide the code or properties of  the any machine or background process of the machine than it is called the incapsulation 
# ==> Attributes is nothing but a function

# 60 Lacture: Inheritance

class Employee:
    def __init__(self,name,salary,roll) :
        self.name = name
        self.salary = salary
        self.roll = roll
    
    def fulldetail(self):
        return f" Name is: {self.name}\n Salary is: {self.salary}\n Roll is : {self.roll} "

    #using of inheritane:

class programmar(Employee):#Here programmar class is inheritance OR access all the properties of the empoloyee class 
    def __init__(self, name, salary, roll,language):
        self.name = name
        self.salary = salary
        self.roll = roll
        self.language = language
    
    def printprog(self):
        
           print(f" Programmar name is: {self.name}\n Salary is: {self.salary}\n Roll is: {self.roll}")
           return f" Programing language name is: {self.language}"

e = Employee("anuj",345,"instructor")
print(e.fulldetail())

p = programmar("Uditya",777,"Programmar",["Python"])
print(p.printprog())