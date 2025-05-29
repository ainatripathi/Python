print("---------FACTORIAL-----------")
num=int(input("Enter any number: "))
a=1
while num>0:
    a=a*num
    num-=1
print("Factorial: ",a)

print("---------REVERSE-----------")
x=int(input("Enter any digit: "))
rem=int(0)
rev=int(0)
while x>0:
    rem=x%10
    x//=10
    rev=rev*10+rem
print("Reverse: ",rev)

print("---------Palindrome number-----------")
y=int(input("Enter any digit: "))
rem=int(0)
rev=int(0)
while x>0:
    rem=x%10
    x//=10
    rev=rev*10+rem
if rev==y:
    print("Palindrome")
else:
    print("Not palindrome")

print("---------Table-----------")
a=int(input("Enter any number"))
b=1
while b<=10:
    r=a*b
    print(a,"x", b,"=", r)
    b+=1

print("---------Prime-----------")
a=int(input("Enter any number"))
b=1
fact=0
while b<=a:
    if a%b==0:
        fact+=1
    b+=1
if fact==2:
    print("Prime")
else:
    print("Not prime")

print("---------Fibonacci Series-----------")
a=-1
b=1
c=0
i=1
n=int(input("Enter no. of terms: "))
while i<=n:
    c=a+b
    print(c)
    a=b
    b=c
    i+=1

print("---------Sum of Digits-----------")
num=int(input("Enter a digit"))
sum=int(0)
rem=0
while num>0:
    rem=num%10
    num//=10
    sum+=rem
print(sum)
