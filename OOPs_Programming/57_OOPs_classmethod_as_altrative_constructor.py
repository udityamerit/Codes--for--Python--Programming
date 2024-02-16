class Employee2:
    no_of_leaves = 8 # this is the class variable:
    def __init__(self, aname, aId) :
        self.name= aname
        self.Id = aId

    def printd(self):
        return f"Name is {self.name} Id is {self.Id}"
    
    
    @classmethod
    def change_leaves(cls,newleaves):

        cls.no_of_leaves = newleaves

    @classmethod
    def from_string(cls, string):
        param = string.split("-") #.split("-") is used to split the string where "-" this occures

        # return cls(param[0],param[1])
        return cls(*string.split("-")) #here *string.split("-") is used to take the whole string and split it and store in the list name is  param and show the istances


harry = Employee2("harray",34)
rohan = Employee2("rahan",45)
aman = Employee2.from_string("aman-345")
harry.change_leaves(34)
print(aman.name)
print(harry.no_of_leaves)
