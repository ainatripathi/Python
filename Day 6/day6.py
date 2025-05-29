print("-----------Table----------")
n=int(input("Enter any number"))
for i in range(1,11):
    c=n*i
    print(n,"x",i,"=",c)

print("-----------Factorial----------")
y=int(input("Enter a number"))
fact=1
for i in range(1,y+1):
    if y>0:
        fact=fact*i
        i+=1
print(fact)
print("---------------------------")

name="Aina"
for i in name:
    print(i)
print("---------------------------")

x=[10,20,40,"Python"]
for i in x:
    print(i)
print("---------------------------")

items_cost=[10,20,40]
gst=5
for x in items_cost:
    print(x+gst)
print("---------------------------")

for x in range(1,5):
    print(x)
print("---------------------------")

for x in range(2,25,3):
    print(x)

print("------------Multiplication of digit---------------")
num=int(input("Enter a digit"))
mul=int(1)
rem=0
while num>0:
    rem=num%10
    num//=10
    mul*=rem
print(mul)

print("------------Armstrong---------------")
real_num=int(input("Enter a digit"))
num=real_num
rem=int(0)
count=int(0)
sum=int(0)
count=len(str(real_num))
num=real_num
while real_num>0:
    rem=real_num%10
    real_num//=10
    sum=sum+rem**count
if sum==num:
    print("Armstrong")
else:
    print("Not armstrong")
