#Tuples with same elements
employee_ids=(1,2,3,4,5)
print("same type of objects: ",employee_ids)
print(type(employee_ids))
print("---------------------------------------------")

#Tuple with different elements
employee_details=(1,"RGV",1000.123)
print("different type of objects: ",employee_details)
print("---------------------------------------------")

#Tuple without parenthesis
employee_detail=1,"RGV",1000.123
print("without parenthesis: ",employee_detail)
print("---------------------------------------------")

#Single value tuple
name=("Sushant")
print(name)
print(type(name)) #string type
name=("Sushant",) 
print(name)
print(type(name)) #tuple type
print("---------------------------------------------")

#tuple() funcion
l=[11,22,33]
t=tuple(l)
print(t)

t=tuple(range(1,10,2))
print(t)
print("---------------------------------------------")

#tuple elements accessing through indexing
t=(10,20,30,40,50)
print(t[0])
print(t[-1])
#print(t[100])
print("---------------------------------------------")

#tuple elements accessing through slicing
t=(10,20,30,40,50,60)
print(t[2:5])
print(t[2:100])
print(t[::2])
print("---------------------------------------------")

#tuple elements accessing through looping
t=(10,20,30,40,50,60,70,80,90,100)
for i in t:
    print(i)
print("---------------------------------------------")

#Tuple immutability
##t=(10,20,30)
##t[1]=70
##print(t)
##print("---------------------------------------------")

#Concatenation
t1=(10,20,30)
t2=(40,50,60)
t3=t1+t2
print(t3)
print("---------------------------------------------")

#Multiplication operator
t1=(10,20,30)
t2=2
print(t1*t2)
print("---------------------------------------------")

#Various functions on tuple list
t=(10,20,50,30,10,40,50,30,60)
print(len(t))
print(t.index(10))
print(t.count(10))
print(sorted(t))
print(sorted(t,reverse=True))
print(min(t))
print(max(t))
print("---------------------------------------------")

#Tuple Packing
a=10
b=20
c=30
d=40
t=a,b,c,d
print(t)
print(type(t))
print("---------------------------------------------")

#Tuple Unpacking
t=(10,20,30,40)
a,b,c,d=t
print("a=", a," b= ", b, " c= ",c," d= ",d)
print("---------------------------------------------")

#Tuple comprehension
t=(x**2 for x in range(1,6))
print(type(t))
for i in t:
    print(i)
print("---------------------------------------------")

#Sets
s={10,20,30,40,50}
print(s)
print(type(s))
print("---------------------------------------------")

s={10,100.23,"RGB"}
print(s)
print(type(s))
print("---------------------------------------------")

#Creating set using range function
s=set(range(5))
print(s)
print("---------------------------------------------")

s={10,20,30,10,40,60,20,30,40}
print(s)
print(type(s))
print("---------------------------------------------")

r=range(0,10)
print(r)
print(type(r))
s=set(r)
print(s)
print(type(s))
print("---------------------------------------------")

#Empty Set
d={}
print(d)
print(type(d))
s=set()
print(s)
print(type(s))
print("---------------------------------------------")

