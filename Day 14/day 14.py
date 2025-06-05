#add function in setrs
s={10,20,30}
s.add(40)
print(s)

#update method in sets
s={10,20,30}
l={40,50,60,10}
s.update(l)
print(s)

#ex2
s={10,20,30}
l={40,50,60,10}
s.update(l,range(5))
print(s)

#copy method
s={10,20,30}
s1=s.copy()
print(s1)

#pop method
s={40,10,30,20}
print(s)
print(s.pop())
print(s)

#remove method
s={40,10,30,20}
s.remove(30)
print(s)

#clear method
s={10,20,30}
print(s)
s.clear()
print(s)

#union method
x={10,20,30,40}
y={30,40,50,60}
print(x.union(y))
print(x|y)

#intersection method
x={10,20,30,40}
y={30,40,50,60}
print(x.intersection(y))
print(x&y)

#difference method
x={10,20,30,40}
y={30,40,50,60}
print(x.difference(y))
print(x-y)
print(y-x)

#symmetric_difference method
x={10,20,30,40}
y={30,40,50,60}
print(x.symmetric_difference(y))
print(x^y)

#membership operators in sets
s={1,2,3,"Sharukh"}
print(s)
print(1 in s)
print('S'in s)
print(2 not in s)

#comprehensions in sets
s={x*x for x in range(5)}
print(s)

#remove duplicate elements in sets
l={10,20,30,10,20,40}
s=set(l)
print(s)

#Creating a frozen set
vowels={'a','e','i','o','u'}
fSet=frozenset(vowels)
print(fSet)
print(type(fSet))

#dict basic example
d={1:'Ramesh', 2:'Suresh', 3:'Mahesh'}
print(d)
print(type(d))

#creating an empty dictionary and addidng the items
d={}
d[1]="Ramesh"
d[2]="Suresh"
d[3]="Mahesh"
print(d)

#Accessing dictionary values by using keys
d={1:"Ramesh", 2:"Suresh",3:"Mahesh"}
print(d[1])
print(d[2])
print(d[3])

#KeyError
##d={1:"Ramesh", 2:"Suresh",3:"Mahesh"}
##print(d[10])

#Handle KeyError in Python Dictionary
d={1:"Ramesh", 2:"Suresh",3:"Mahesh"}
if 400 in d:
    print(d[400])
else:
    print("Key not found")

#Employee info program by using a dictionary
d={}
n=int(input("Enter number of employees: "))
i=1
while i<=n:
    name=input("Enter Employee Name: ")
    salary=input("Enter Employee Salary: ")
    d[name]=salary
    i+=1
for x in d:
    print("The name is: ",x," and his salary is: ",d[x])
print(d)
