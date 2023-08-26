class A:
    classvar1 = "I am a class var A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class a"
        self.special = "Special"

class B(A):
    classvar1 = "I am in class B"
    def __init__(self):
        super().__init__()
        self.var1  = " I am in side class B's constructor"
        self.classvar1 = "Insance var in class B"
        print(super().classvar1)
a = A()
b = B()
print(a.special)
print(b.classvar1)