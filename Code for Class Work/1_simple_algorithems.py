# add the digits of a number:

n =  int(input("Enter the number: "))
sum = 0
r = n % 10
p = int(n/10)
r1 = p % 10
q = int(p/10)
r2 = q % 10
sum = r+r1+r2
print(int(sum))


# Reverse the given number

m = int(input("Enter the number:"))
sum = 0
r = m % 10
p = r*100
print(p)
q = int(m/10)
r1 = q % 10
t = r1*10
print(t)
z = int(q/10)
r2 = z % 10
s = r2*1
print(s)
sum =int(p+t+s)
print("Your reversed number is: ",sum)

