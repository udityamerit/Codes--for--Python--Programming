class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"
    @property
    def email(self):
        return f"{self.fname}.{self.lname}@gmail.com"


hs = Employee("hindustani", "supporter")
np = Employee("nikhil", "raj")

# print(hs.explain())
# print(hs.email)

hs.fname = "US"
print(hs.email)
#"Note: Constractor is run at the time od object creation"

