import random

'''Method	Description
seed() ===>	Initialize the random number generator

getstate() ===>	Returns the current internal state of the random number generator 

setstate() ===>	Restores the internal state of the random number generator

getrandbits() ===>	Returns a number representing the random bits

randrange() ===>	Returns a random number between the given range

randint() ===>	Returns a random number between the given range

choice() ===>	Returns a random element from the given sequence

choices() ===>	Returns a list with a random selection from the given sequence

shuffle() ===>	Takes a sequence and returns the sequence in a random order

sample() ===>	Returns a given sample of a sequence

random() ===>	Returns a random float number between 0 and 1

uniform() ===>	Returns a random float number between two given parameters

triangular() ===>	Returns a random float number between two given parameters, you can also set a mode parameter to specify the midpoint between the two other parameters

betavariate() ===>	Returns a random float number between 0 and 1 based on the Beta distribution (used in statistics)

expovariate() ===>	Returns a random float number based on the Exponential distribution (used in statistics)

gammavariate() ===>	Returns a random float number based on the Gamma distribution (used in statistics)

gauss() ===>	Returns a random float number based on the Gaussian distribution (used in probability theories)

lognormvariate() ===>	Returns a random float number based on a log-normal distribution (used in probability theories)

normalvariate() ===>	Returns a random float number based on the normal distribution (used in probability theories)

vonmisesvariate() ===>	Returns a random float number based on the von Mises distribution (used in directional statistics)

paretovariate() ===>	Returns a random float number based on the Pareto distribution (used in probability theories)

weibullvariate() ===>	Returns a random float number based on the Weibull distribution (used in statistics)'''

random_number = random.randint (0 , 6)
print(random_number)

list = ["harry","anuj","ram","dhaamu"]
ptr = random.choice(list)
print(ptr)
