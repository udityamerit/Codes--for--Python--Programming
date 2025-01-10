import pickle

# pickling a python objects

# cars = ['Audi', 'bmw', 'maruti suzuki']
# file = "mycar.pkl"
# fileobj = open(file, 'wb')
# pickle.dump(cars, fileobj)
# fileobj.close()

# extracting the pickle object
file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))
