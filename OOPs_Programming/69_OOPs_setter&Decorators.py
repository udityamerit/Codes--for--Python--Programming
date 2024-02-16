class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    @property # to set the property of the email
    def email(self):
        if self.fname or self.lname == None:
            return "Email is not set yet"
        return f"{self.fname}.{self.lname}@gmail.com"
    
    @email.setter
    def email(self,string):
        print("setting now...")
        name = string.split("@")[0]
        self.fname = name.split(".")[0]
        self.lname = name.split(".")[1]

    @email.deleter  # to delet the email
    def email(self):
        self.fname = None
        self.lname = None

hs = Employee("hindustani", "supporter")
np = Employee("nikhil", "raj")

# print(hs.explain())
# print(hs.email)

hs.fname = "US"
print(hs.email)
#"Note: Constractor is run at the time od object creation"

hs.email = "this.that@gmail.com"
print(hs.fname)
print(hs.lname)
print(hs.email)

#for delet the email you have to create the deleter first inside the class

del hs.email
print(hs.email)
