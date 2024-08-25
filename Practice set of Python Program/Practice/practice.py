# class A:
#         def __init__(self,name, age, sub):
#                 self.name = name
#                 self.age = age
#                 self.sub = sub
        
#         def display(self):
#                 return (f"Name is: {self.name}\nage is: {self.age}\nsubject is: {self.sub}")

# a = A("uditya", 59, "math")
# print(a.display())

# m = A("malishka",78,"python")
# print(m.display())

class A:
        def __init__(self,name, age, sub):
                self.name = name
                self.age = age
                self.sub = sub
        
        def output(self):
                return (f"Name is: {self.name}\nage is: {self.age}\nsubject is: {self.sub}")

class B(A):
        def __init__(self,name, age, sub,branch):
                self.branch = branch
                super().__init__(name,age,sub)
        
        def display(self):
                return (f"Name is: {self.name}\nage is: {self.age}\nsubject is: {self.sub}\nbranch is: {self.branch}")

a = A("uditya", 59, "math")
print(a.output())

m = B("malishka",78,"python","AIML")
print(m.display())


