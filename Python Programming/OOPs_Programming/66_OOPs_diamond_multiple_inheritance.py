class A:
        def meth(self):
             print("This is a method from class A")
class B(A):
         def meth(self):
           print("This is a method from class b")

class C(A):
         def meth(self):
                print("This is a method from class c")

class D(B,C):
        def meth(self):
            print("This is a method from class d")

a= A() 
b= B() 
c= C() 
d= D() 
a.meth()
c.meth()
 