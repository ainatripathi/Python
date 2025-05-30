#join function
profile=['Roshan', 'Actor', 'India']
candidate='-'.join(profile) #to connect list items with whatever string you want
print(profile)
print(candidate)

#Case functions
a='ThE dAy iS FinE'
print(a.upper())
print(a.lower())
print(a.swapcase())
print(a.title())
print(a.capitalize())

#format operator
name='Rakesh'
salary=1000
age=19
print("{}'s salary is {} and his age is {}".format(name, salary, age))
print("{0}'s salary is {1} and his age is {2}".format(name, salary, age))
print("{z}'s salary is {y} and his age is {x}".format(z=name, y=salary, x=age))

#User-defined functions
#with no return, no arguments
def display():
    print("Welcome to function")
display()

def calc():
    a=int(input("Enter a number"))
    b=int(input("Enter a number"))
    print("Addition is: ",(a+b))
    print("Subtraction is: ",(a-b))
    print("Multiplication is: ",(a*b))
    print("Division is: ",(a/b))
    print("FLoor Division is: ",(a//b))
    print("Exponent is: ",(a**b))
for i in range(1,6):
    calc()
    
#with no return and with arguments
def arg(x,y):
    print("Addition is: ",(x+y))
    print("Subtraction is: ",(x-y))
    print("Multiplication is: ",(x*y))
    print("Division is: ",(x/y))
    print("Floor Division is: ",(x//y))
    print("Exponent is: ",(x**y))
a=int(input("Enter a number"))
b=int(input("Enter a number"))
arg(a,b)

#with return and no arguments
def add():
    a=int(input("Enter a number"))
    b=int(input("Enter a number"))
    return (a+b)
n=add()
print(n)

#with return and with arguments
def arg(x,y):
    z=x+y
    return z
a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=arg(a,b)
print("Addition is: ",c)

#Multi-return
def arg(x,y):
    add=x+y
    sub=x-y
    mul=x*y
    return add,sub,mul
a=int(input("Enter a number"))
b=int(input("Enter a number"))
r1,r2,r3=arg(a,b)
print("Addition is: ",r1)
print("Subtraction is: ",r2)
print("Multiplication is: ",r3)
