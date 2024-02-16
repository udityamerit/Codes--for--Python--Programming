class Employee:
    no_of_leaves = 8 # this is the class variable:
    # this variable is accessable to all of the objects of the employee
    pass

h = Employee() # here h is a first object of a class employee
a = Employee() # here a is second object of a class employee

h.name = "Harry" 
h.Id = 234

a.name = "Anuj"
a.Id = 235

print(a.name)
print(h.__dict__) #__dict__ is a method which is return a dictionary which contain the all variables of that object where it is called
print(a.__dict__)