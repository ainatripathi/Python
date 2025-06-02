#list of python
list1=[]
print(list1)
print(type(list1))

list2=["raman", "puneet", "rama"]
print(list2)
print(type(list2))

#uses of list function
r=range(0,10)
l=list(r)
print(l)
print(type(l))
name="pooja"
l1=list(name)
print(l1)
print(type(l1))

#List is mutable
l=[1,2,3,4,5]
print(l)
print("Before modifying [0]: ",l[0])
l[0]=20
print("After modifying [0]: ",l[0])
print(l)

#List element accessing through indexing
names=["pooja","supriya","aman"]
print(names)
print(names[0])
print(names[1])
print(names[2])
print(list(names))
print (type(names[0]))
print (type(names[1]))
print (type(names[2]))

#List elements accessing through slicing
n=[1,2,3,4,5,6]
print(n)
print(n[2:5:2])
print(n[4:2])
print(n[3:5])

#List element accessing through loops
a=[10,20,30,40,50]
for x in a:
    print(x)
a=[30,40,50,60,70]
x=0
while x<len(a):
    print(a[x])
    x+=1

#predefine in list
n=[1,2,3,4,5]
print(len(n))
n=[1,2,3,3,4,5,5,6]
print(n.count(5))
print(n.count(3))
print(n.count(2))
l=[]
l.append("pooja")
l.append("anjali")
l.append("prayan")
print(l)
n=[10,20,30,40,50]
n.insert(0,76)
print(n)
l=[20,40,50,60]
print(l)
l.insert(1,111)
l.insert(-1,222)
print(l)
l.insert(-2,444)
print(l)
l1=[4,5,6]
l2=["amrita","preeti","tanvi"]
print("Before extend l1 is: ",l1)
print("Before extend l2 is: ",l2)
l2.extend(l1)
print("After extend l1 is: ",l1)
print("After extend l2 is: ",l2)

august_txns=[10,20,30,40,50,60,70,80,90]
sept_txns=[11,22,33,44,55,66,77,88,99]
print("August month Transactions: ",august_txns)
sept_txns.extend(august_txns)
print("August and September total transaction amount: ", sum(sept_txns))
