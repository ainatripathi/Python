#remove method
n=[1,2,3]
print(n)
n.remove(1)
print(n)

#pop method
n=[1,2,3,4,5]
print(n.pop(1))
print(n)
print(n.pop())
print(n)

#reverse method
n=[1,2,3,4,"two"]
print(n)
n.reverse()
print(n)

#sort method
n=[1,4,2,3,5]
print(n)
n.sort()
print(n)
s=["Suresh", "Ramesh", "Arjun"]
s.sort()
print(s)

#Aliasing: change in original also modifies new one
x=[10,20,30]
y=x
print(x)
print(y)
print(id(x))
print(id(y))
x[1]=99
print(x)
print(y)
print(id(x))
print(id(y))

#Cloning: change in original doesn't affect new one
#using slicing
x=[10,20,30]
y=x[:]
print(x)
print(y)
print(id(x))
print(id(y))
x[1]=99
print(x)
print(y)
print(id(x))
print(id(y))

#using copy() method
x=[10,20,30]
y=x.copy()
print(x)
print(y)
print(id(x))
print(id(y))
x[1]=99
print(x)
print(y)
print(id(x))
print(id(y))

#Mathematical operators
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)

a=[1,2,3]
print(a)
print(2*a)

#comparison of two lists
print([1,2,3]<[2,2,3])
print([1,2,3]<[1,2,3])
print([1,2,3]<=[1,2,3])
print([1,2,3]<[1,2,4])
print([1,2,3]<[0,2,3])
print([1,2,3]==[1,2,3])

x=["abc", "def", "ghi"]
y=["abc", "def", "ghi"]
z=["ABC", "DEF", "GHI"]
a=["abc", "def", "ghi", "jkl"]
print(x==y)
print(x==z)
print(x==a)

#Membership operator in list
x=[10,20,30,40,50]
print(20 in x)
print(20 not in x)
print(90 in x)
print(90 not in x)

#nested list
a=[80,90]
b=[10, 20, 30, a]
print(b[0])
print(b[1])
print(b[2])
print(b[3])
print(type(b[0]))
print(type(b[1]))
print(type(b[2]))
print(type(b[3]))

#List Comprehension
x=[1,2,3,4]
y=[]
for i in x:
    y.append(i*2)
print(y)

x=[1,2,3,4]
y=[i*2 for i in x]
print (y)

s=range(1,20,3)
for i in s:
    print(i)
m=[x for x in s if x%2==0]
print(m)
n=[x for x in s if x%2!=0]
print(n)
