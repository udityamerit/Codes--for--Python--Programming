# 60 Lacture: Single Inheritance;

class Employee:
    def __init__(self,name,salary,roll) :
        self.name = name
        self.salary = salary
        self.roll = roll
    
    def fulldetail(self):
        return f" Name is: {self.name}\n Salary is:\
              {self.salary}\n Roll is : {self.roll} "

    #using of inheritane:

class programmar(Employee):#Here programmar class is inheritance OR access all the properties of the empoloyee class 
    def __init__(self, name, salary, roll,language):
        self.name = name
        self.salary = salary
        self.roll = roll
        self.language = language
    
    def printprog(self):
        
           print(f" Programmar name is: {self.name}\n Salary is: {self.salary}\n Roll is: {self.roll}")
           return f" Programing language \
            name is: {self.language}"

e = Employee("anuj",345,"instructor")
print(e.fulldetail())

p = programmar("Uditya",777,"Programmar",["Python"])
print(p.printprog())

#----------------------------------------------------------#

# 61: Multiple Inheritance;

class Employee:
    def __init__(self,name,salary,roll) :
        self.name = name
        self.salary = salary
        self.roll = roll
    
    def fulldetail(self):
        return f" Name is: {self.name}\n Salary is: \
            {self.salary}\n Roll is : {self.roll} "

class Player():
    def __init__(self,name,game):
        self.name = name
        self.game = game

    def det(self):
        return f" Name is: {self.name}\n Game is:\
              {self.game}"

class Coolpro(Employee,Player):
    pass

e = Employee("anuj",345,"instructor")

p = Coolpro("karan",3456,"Cool Programmar")
det = p.fulldetail()
print(det)

#---------------------------------------------------------#

# 62: Multilevel Inheritance;

class Dad:
    ball = 1

class Son(Dad):
    dance = 1
    def isdance(self):
        return f"Yes I dance {self.dance} times"

class Grandson(Son):
    dance = 2
    def isdance(self):
        return f" yes i dance very awesomely {self.dance}"
    
d = Dad()
s = Son()
g = Grandson()
print(g.isdance())
print(g.ball)

#-----------------------------------------------------------
# Multiple Inheritance;

class Phone:
    def __init__(self,name,modle,price) :
        self.name = name
        self.modle = modle
        self.price = price
    
    def fulldetail(self):
        return f" Details is: {self.name}  {self.modle} {self.price} "

class Smartphone(Phone):
    def __init__(self,name,modle,price,power,life):
       super().__init__(name,modle,price)
       self.power = power
       self.life = life
    def det(self):
           return f" Details is: {self.name}  {self.modle} {self.price} {self.power} {self.life}"


class SuperPhone(Smartphone):
    def __init__(self,name,modle,price,power,life,frontcamera,rearcamera):
        super().__init__(name,modle,price,power,life)
        self.frontcamera = frontcamera
        self.rearcamera = rearcamera
    def deets(self):
           return f" Details is: {self.name}  {self.modle} {self.price} {self.power} {self.life} {self.frontcamera} {self.rearcamera}"

p = Phone("oppo","34rt43",2000)
s = Smartphone("vivo","23rt43",23000,80,34)
sp = SuperPhone("one pluse","34rty34a",34000,100,38,"12MP", "16MP")
print(p.fulldetail())
print(s.det())
print(sp.deets())

# Quiz on multilevel inheritance

# Define the classes of the phone & smartphone

class Phone:
    def __init__(self,name,modle,price):
        self.name = name
        self.modle = modle
        self.price = price

    def full_detail(self):
            return f" Name is: {self.name} \n\
        modle name is: {self.modle} \n \
         Price is: {self.price} rs."
        
class Smartphone(Phone):
    def __init__(self, name, modle, price,life,capacity):
        super().__init__(name, modle, price)
        self.life = life
        self.capacity = capacity

    def full_details(self):
          return f" Name is: {self.name}\n modle name is: {self.modle} \n Price is: {self.price} rs. \n Life is: {self.life} days\n Capacity is: {self.capacity} percent"

p = Phone("vivo","34rt43",32000)
print("Phone details is: ", p.full_detail())
print("--------------------------------------")
p2 = Smartphone("onepluse","35tu34rt43",52000,45,100)
print("SmartPhone details is: ", p2.full_details())