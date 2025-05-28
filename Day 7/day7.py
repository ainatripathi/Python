#Pattern Question
for i in range(1,6):
    for j in range(1,6):
        print(j, end="")
    print("")

#Question 1
    
for i in range(1,6):
    for j in range(1,(i+1)):
        print(j,end="")
    print("")

#Question 2
    
for i in range(1,6):
    for j in range(1,(i+1)):
        print(i,end="")
    print("")

#Question 3

for i in range(1,6):
    for j in range(1,(i+1)):
        print("*",end="")
    print("")

#Question 4

a=1
b=0
for i in range(1,6):
    for j in range(1, (i+1)):
        if i%2==0:
            if j%2==0:
                print(a, end="")
            else:
                print(b,end="")
        else:
            if j%2==0:
                print(b, end="")
            else:
                print(a,end="")
    print("")
        
#Question 5
a=5;
for i in range(1,6):
    for j in range(a):
        print("*", end="")
    print("")
    a-=1

#Question 6

a=5
b=1
for i in range(1,6):
    for k in range((a-1)):
        print(" ",end="")
    for j in range(b):
        print("*", end="")
    a-=1
    b+=1
    print("")

#Question 7

a=5
for i in range(1,6):
    for k in range((a-1)):
        print(" ",end="")
    for j in range(1,i+1):
        print("* ", end="")
    print("")
    a-=1

#Question 8

a=5
b=1
for i in range(1,6):
    for k in range((a-1)):
        print(" ",end="")
    for j in range(b):
        print("*",end="")
    a-=1
    b+=2
    print("")

#Question 9

a=5
b=1
z=0
n=0
x=0
for i in range(1,6):
    for k in range((a-1)):
        print(" ",end="")
    for j in range(1, i+1):
        print(b,end="")
        b+=1
    for m in range(n):
        print(y,end="")
        y-=1
    a-=1
    b-=z
    z+=1
    n+=1
    x+=2
    y=x
    print("")

#Question 10

a=5
n=0
x=0
for i in range(1,6):
    for k in range((a-1)):
        print(" ",end="")
    for j in range(1,(i+1)):
        print(j,end="")
    for m in range(n):
        print(y,end="")
        y-=1
    a-=1
    x+=1
    y=x
    n+=1
    print("")
