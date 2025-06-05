#del keyword
d={1:'Ramesh', 2:'Suresh', 3:'Mahesh'}
print("Before deleting key: ",d)
del d[1]
print("After deleting key: ",d)
print("-------------------------------")

#clear method
d={1:'Ramesh',2:'Suresh',3:'Mahesh'}
print("Before clearing all the entries: ",d)
d.clear()
print("After clearing all the entries: ",d)
print("-------------------------------")

#key error
##d={1:'Ramesh', 2:'Suresh', 3:'Mahesh'}
##print("Before deleting key: ",d)
##del d[10]
##print("After deleting key: ",d)

#Deleting complete dict by del
d={1:'Ramesh', 2:'Suresh', 3:'Mahesh'}
print("Before deleting key: ",d)
del d
#print("After deleting key: ",d)
print("-------------------------------")

#creating dictionary by dict funtion
d=dict({1:"Ramesh", 2:"Suresh",3:"Mahesh"})
print(d)
print("-------------------------------")

#creating dict using tuple
d=dict([(1,"Arjun"), (2,"Karan"),(3,"Ramesh"),(4,"Suresh"),(5,"Mahesh")])
print(d)
print("-------------------------------")

#len function
d=dict([(1,"Arjun"), (2,"Karan"),(3,"Ramesh"),(4,"Suresh"),(5,"Mahesh")])
print("Length of dictionary is: ",len(d))
print("-------------------------------")

#get funtion case 1
d=dict([(1,"Arjun"), (2,"Karan"),(3,"Ramesh"),(4,"Suresh"),(5,"Mahesh")])
print(d.get(1))
print(d.get(100))
print("-------------------------------")

#get funtion case 2
d=dict([(1,"Arjun"), (2,"Karan"),(3,"Ramesh"),(4,"Suresh"),(5,"Mahesh")])
print(d.get(1))
print(d.get(100, "No key found"))
print("-------------------------------")

#pop method
d={1:"Ramesh",2:"Suresh",3:"Mahesh"}
print("Before pop: ",d)
d.pop(1)
print("After pop: ",d)
print("-------------------------------")

#pop method throw an error when key not available
##d={1:"Ramesh",2:"Suresh",3:"Mahesh"}
##d.pop(23)

#popitem method
d={1:"Ramesh",2:"Suresh",3:"Mahesh"}
print("Before popitem: ",d)
d.popitem()
print("After pop: ",d)
print("-------------------------------")

#popitem throws an error if dictionary is empty
##d={}
##d.popitem()
##print("After popitem: ",d)

#keys method
d={1:"Ramesh",2:"Suresh",3:"Mahesh"}
print(d)
for k in d.keys():
    print(k)
print("-------------------------------")

#values method
d={1:"Ramesh",2:"Suresh",3:"Mahesh"}
print(d)
for k in d.values():
    print(k)
print("-------------------------------")

#items method
d={1:"Ramesh",2:"Suresh",3:"Mahesh"}
print(d)
for k in d.items():
    print(k)
print("-------------------------------")

#copy method
d1={1:"Ramesh",2:"Suresh",3:"Mahesh"}
d2=d1.copy()
print(d1)
print(d2)
print("-------------------------------")

#dictionary comprehensions
d={a:a*a for a in range(1,6)}
print(d)
print("-------------------------------")


#Types of arguments
#Keyword arguments
def cart(item,price):
    print(item,"cost is: ",price)
cart(item="electronics", price=20000)
cart(item="motorbike", price=100000)
cart(price=1200,item="shirt")
print("-------------------------------")

#ex2
def details(id, name):
    print("Emp id is: ",id)
    print("Emp name is: ",name)
details(id=1,name="Aina Tripathi")
details(id=2,name="Python")
print("-------------------------------")

#Positional and Keyword arguments
def details(id, name):
    print("Emp id is: ",id)
    print("Emp name is: ",name)
details(1,name="Aina Tripathi")
details(2,name="Python")
print("-------------------------------")

#default arguments
def details(name,id=212):
    print("Emp id is: ",id)
    print("Emp name is: ",name)
details(id=1,name="Aina Tripathi")
details(name="Python")
print("-------------------------------")

#Variable-length argument (*args)
def total(x,*y):
    sum=0
    for i in y:
        sum+=i
    print(sum)
    print(x+sum)
total(110,)
total(110,234)
total(110,234,534)
total(110,234,534,678)
print("-------------------------------")

