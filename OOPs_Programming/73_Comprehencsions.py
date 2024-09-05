# list comprihensions

l = [ i for i in range(5) if i>2]
print(l)

# dictionary comprihensions

dict1 = {i: f"items {i}" for i in range(10) if i>4}
print(dict1)

# change the place of key and values

dict2 = { value:key for key, value in dict1.items()}
print(dict2)

# set complihensions

dresses = {dress for dress in ["dress1","dress2", "dress1","dress2"] }
print(dresses)



# Ganerator comprihensions
even = (i for i in range(10) if i%2 == 0)
print(type(even))
print(even.__next__())
print(even.__next__())

for item in even:
        print(item)
