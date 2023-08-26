def function1():
    print("hello pagal")

func2 = function1
func2()
# ------------------------------------------------------


def funcret(num):
    if num == 0:
        return print
    if num ==1 :
        return sum
a = funcret(1)
print(a)

# ----------------------------------------------------

def executor(func):
    func("this")
executor(print)


# -----------------------------------------------
def dec1(func1):
    def nowexec():
        print("executing now")
        func1()
        print("executed")
    return nowexec


@dec1
def who_is_harry():
    print("harry is  a good boy")

# who_is_harry() = dec1(who_is_harry)
who_is_harry()