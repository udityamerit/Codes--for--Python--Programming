def out(a,b):
        def iner(c,d):
                return c+d
        return iner(a,b)

res = out(5,10)
print(res)

def dis(**kwargs):
        for i in kwargs:
                print(i)

dis(emp = "kelly", salary = 9000)

def fun1(num):
        return num+ 25
fun1(5)
print(num)