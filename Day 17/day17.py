#decorator func()
def decor(func):
    def inner_func(x,y):
        if x>0:
            x=0
        if y<0:
            y=0
        return func(x,y)
    return inner_func
def add(a,b):
    res=a*b
    return res
add=decor(add)
print(add(-20,30))
print(add(-10,5))

def decor(func):
    def inner_func(x,y):
        if x>0:
            x=0
        if y<0:
            y=0
        return func(x,y)
    return inner_func

def add(a,b):
    res=a+b
    return res
add=decor(add)
print(add(-20,30))
print(add(-10,5))

def decor(func):
    def inner_func(x,y):
        if x>0:
            x=0
        if y<0:
            y=0
        return func(x,y)
    return inner_func
@decor
def add(a,b):
    res=a+b
    return res
add=decor(add)
print(add(-20,30))
print(add(-10,5))

#generator func()
def m():
    yield "Rumi"
    yield "Rose"
g=m()
print(g)
print(type(g))
for y in g:
    print(y)

def m(x,y):
    while x<=y:
        yield x
        x+=1
g=m(5,10)
for y in g:
    print(y)

#generators with next func()
def m(x,y):
    while x<=y:
        yield x
        x+=1
g=m(5,10)
print(type(g))
print(next(g))
print(next(g))
print(next(g))

#Exception handling
print('one')
print('2')
try:
    print(10/0)
except ZeroDivisionError:
    print("Exception occured")
print('three')
print('four')

x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
res1=x/(x+y)
print(res1)
res2=x/(x-y)
print(res2)
