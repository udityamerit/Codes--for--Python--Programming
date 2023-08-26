class Worker:
    def __init__(self,name,role,salary):
        self.name = name
        self.role = role
        self.salary = salary
    def fulldetail(self):
         return f"the name is: {self.name}  role is :{self.role}  salary is : {self.salary}"
    
    def __add__(self,other): #this is operator overloading
        return  f"total salary {self.salary +other.salary}"
    
    def __repr__(self):
        return self.fulldetail()
    
w = Worker("Ram","programmar",345) 
# print(w.fulldetail())
print(w)

w2 = Worker("Mohan","coder",349)
# print(w2.fulldetail())
print(w2)

print(w+w2) #addition of salary
