#--------------MAP FUNCTION --------------

numbers = ["3","34","43"]
numbers = list(map (int,numbers))
numbers[2] = numbers[2] +1
print(numbers[2])

num = [2,3,4,56,7,8]
sq = list(map(lambda x:x*x,num))
print(sq)  

def squre(a):
    return a*a

def cube(a):
    return a*a*a
func = [squre,cube]
for i in range(5):
    val = list(map(lambda x:x(i) , func))
    print (val)

#-------------FILTER FUNCTION -------------

list1 = [1,2,3,4,5,6,87,9,0]
def is_greater_8(num):
    return num<8
gr_then_8 = list(filter(is_greater_8,list1))
print(gr_then_8)

# -------------REDUCE FUNCTION --------------

from functools import reduce

list2 = [1,2,4,5,6]
add = reduce(lambda x,y:x+y,list2)
multi = reduce(lambda x,y:x*y,list2)
print(add)
print(multi)
