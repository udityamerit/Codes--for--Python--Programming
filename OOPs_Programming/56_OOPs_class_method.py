class Employee1:
    no_of_leaves = 8 # this is the class variable/class attribute:
    def __init__(self, aname, aId) :
        self.name= aname
        self.Id = aId

    def printd(self):
        return f"Name is {self.name} Id is {self.Id}"
    
    
    @classmethod   
    def change_leaves(cls,newleaves):

        cls.no_of_leaves = newleaves


h = Employee1("harray",34)
r = Employee1("rahan",45)
h.change_leaves(34)

print(Employee1.no_of_leaves)