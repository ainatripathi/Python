#Keywords arguments - **kwargs
def print_kwargs(**kwargs):
    print(kwargs)
print_kwargs(id=1, name="Aina Tripathi", course="Python")
print("-------------------------------------")

#ex2
def m1(**x):
    for k,v in x.items():
        print(k,"=",v)
m1(id=1, name='aina', course='python')
m1(id=2, name='sneha', course='java')
print("-------------------------------------")

#Recursion
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
fact=factorial(5)
print("The factorial of 5 is: ", fact)
print("-------------------------------------")

#lambda function
s=lambda a:a*a
print("The square using lambda function is: ",s(5))
print("-------------------------------------")

add=lambda a,b: a+b
print("Addition using lambda function is: ",add(5,9))
print("-------------------------------------")

#filter function
item_cost=[999,888,1100,1200,1300,777]
gt_thsnd=filter(lambda x: x>1000, item_cost)
x=list(gt_thsnd)
print("Eligible for discount: ",x)
print("-------------------------------------")

#ex2
percent=[62.5,75,89.7,60.4,78.9,84.2,51.0,77.6]
check=filter(lambda x: x>75.0, percent)
eligible=list(check)
print("Candidates with these % are eligible for placement drive: ",eligible)
print("-------------------------------------")

#map function
item_cost=[999,888,1100,1200,1300,777]
gst_cost=map(lambda x: x+10, item_cost)
x=list(gst_cost)
print("Cost without gst: ",item_cost)
print("Cost with gst: ",x)
print("-------------------------------------")

#ex2
item_cost=[999,888,1100,1200,1300,777]
gt_thsnd=filter(lambda x: x>1000, item_cost)
x=list(gt_thsnd)
disc_app=map(lambda y: y-(y*0.2), x)
y=list(disc_app)
print("Eligible for discount: ",x)
print("Cost after discount applied: ",y)
print("-------------------------------------")

#ex3
percent=[62.5,75,89.7,60.4,78.9,84.2,51.0,77.6]
check=filter(lambda x: x>75.0, percent)
eligible=list(check)
marks=map(lambda y: y+(y*0.1), eligible)
y=list(marks)
print("Candidates with these % are eligible for placement drive: ",eligible)
print("Marks after written exam: ",y)
print("-------------------------------------")

#reduce function
from functools import reduce
each_cost=[111,222,333,444]
total=reduce(lambda x,y:x+y, each_cost)
print("Each cost is: ",each_cost)
print("Total cost is: ",total)
