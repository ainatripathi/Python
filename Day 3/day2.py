#eg

##name=input("Enter Student Name: ")
##print("Student name is ", name)
##print("Type of identifier name is ", type(name))

#user-input data

name1=input("Enter Student Name: ")
roll=int(input("Enter Student Roll No: "))
grade=input("Enter Student Grade: ")
per=float(input("Enter Student Percentage: "))

print("------------------STUDENT DETAILS------------------")

print("Student name is ", name1)
print("Student Roll No is ", roll)
print("Student Grade is ", grade)
print("Student Percentage is ", per)

print("Type of identifier name is ", type(name1))
print("Type of identifier Roll No is ", type(roll))
print("Type of identifier grade is ", type(grade))
print("Type of identifier Percentage is ", type(per))

#Operators
#Arithematic
a=6
b=2
print("Addition is ",(a+b))
print("Subtraction is ",(a-b))
print("Multiplication is ",(a*b))
print("Division is ",(a/b))
print("Floor Division is ",(a//b))
print("Expon. is ",(a**b)) #a power b
print("-------------------------------")
#Assignment
a=6
b=2
c=a+b
print("Addition is ", c)
c+=100
print(c)
print("-------------------------------")
#Relational
print(a>b)
print(a>=b)
print(a<b)
print(a<=b)
print(a==b)
print(a!=b)
print("-------------------------------")
#Logical
a=True
b=False
print(a and b)
print(a or b)
print(not a)
print(a and a)

x=10
y=5
print((x>y) and (x>5))
print((x>y) or (x<5))


