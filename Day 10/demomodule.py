import addmul
print(addmul.x)
m=int(input("Enter a number: "))
n=int(input("Enter a number: "))
addmul.sum(m,n)
addmul.multiply(m,n)

#Alias
import addmul as am
print(am.x)
m=int(input("Enter a number: "))
n=int(input("Enter a number: "))
am.sum(m,n)
am.multiply(m,n)

#from keyword
from addmul import x, multiply
print(x)
multiply(72,65)

#import *
from addmul import *
print(x)
multiply(72,65)
sum(2,8)

#aliasing members
from addmul import x as a, multiply as mply
print(a)
mply(72,65)

