class Employee1:
    no_of_leaves = 8 # this is the class variable:
    def __init__(self, aname, aId) :
        self.name= aname
        self.Id = aId

    def printd(self):
        return f"Name is {self.name} Id is {self.Id}"
harry = Employee1("harray",34)
# h = Employee1("harry",345)
# a = Employee1("anuj",235)

# h.name = "Harry"
# h.Id = 234

# a.name = "Anuj"
# a.Id = 235

# print(a.Id)
# print(h.name)
print(harry.Id)