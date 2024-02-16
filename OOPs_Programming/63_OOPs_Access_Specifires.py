class Employee1:
    no_of_leaves = 8 # this is the class variable: and type is public
    _daywork = 23 # this is a protected type variable
    __workout = 34 # this is a private type 
    def __init__(self, aname, aId) : #_init_ method is a constructor
        self.name= aname
        self.Id = aId

     
harry = Employee1("harray",34)
# Access the public variable:
print(harry.Id,harry.name)
# Aceess the protected variable:
print(harry._daywork)
# Aceess the Private variable:
print(harry._Employee1__workout)