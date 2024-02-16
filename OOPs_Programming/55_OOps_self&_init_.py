class Employee1:
    no_of_leaves = 8 # this is the class variable:
    def __init__(self, aname, aId) : #_init_ method is a constructor
        # self is used to pass the itself as a argument
        self.name= aname
        self.Id = aId
     
harry = Employee1("harray",34)

print(harry.Id,harry.name)
