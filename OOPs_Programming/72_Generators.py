'''
Iterable = __iter__() or __getitem__() are difines
Iterator = __next__()
Iteration = 



yield is a generator 
'''

def gen(n):
        for i in range(n):
                yield i

g = gen(3)
print(g)
print(g.__next__())

for i in g:
        print(i)


h = "Uditya"  # string is iterable
ite = iter(h) # this is return the iterator object
print(ite.__next__())  # this is return the iterator value  of the object h

print(ite.__next__())
print(ite.__next__())