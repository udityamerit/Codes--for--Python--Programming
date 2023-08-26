class Employee:
    no_of_leaves = 8 # this is the class variable:
    pass

h = Employee()
a = Employee()

h.name = "Harry"
h.Id = 234

a.name = "Anuj"
a.Id = 235

print(a.name)
print(h.__dict__)
print(a.__dict__)