#Palindrome Number

def palin(n):
    rem=0
    rev=0
    while n>0:
        rem=n%10
        rev=rev*10+rem
        n//=10
    return rev
num=int(input("Enter a number: "))
pal=palin(num)
if(num==pal):
    print(num," is Palindrome")
else:
    print(num," is not Palindrome")

#Prime number

def prime(n):
    c=0
    for i in range(2,n+1):
        if n%i==0:
            c+=1
    return c
num=int(input("Enter a number: "))
check=prime(num)
if check==1:
    print(num," is a Prime Number")
else:
    print(num," is not a Prime Number")

#Factorial

def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
num=int(input("Enter a number: "))
factorial=fact(num)
print("Factorial of ",num," is ",factorial)
