#Membership operator

text="Welcome to python programming"
print("Welcome" in text)
print("welcome" in text)
print("nireekshan" in text)
print("Hari" not in text)
print("-------")

#List: data stored in a sequence. Different types of data is stored.

names=["Hari", "Ramesh", "Prasad", "Arjun"]
print("Hari" in names)
print("Nireekshan" in names)
print("Hema" not in names)
print("-------------------")

#Identity operator

a=25
b=25
print(id(a))
print(id(b))
print(a is b)
print("----------")

#Bitwise Operator

a=10
b=7
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<2)
print(a>>2)

#Control Flow Statements: 1. Sequenting 2. Condtioning 3. Looping

#Conditional

num=int(input("Enter a number "))
if num>=0:
    print("Positive Number")
else:
    print("Negative number")

#User-input example
company_name=input("Enter a company name ")
stu_name=input("Enter Student Name ")
per=float(input("Enter Student Percentage "))
print("Company Name is ", company_name)
print("Student Name is ", stu_name)
print("Student Percentage is ", per)
if per>=65.0:
    print("Student eligible for Placement Drive.")
else:
    print("Student not eligible for Placement Drive.")

a=int(input("Enter a number "))
b=int(input("Enter a number "))
c=int(input("Enter a number "))
if a>b:
    if a>c:
        print(a, " is greatest")
    else:
        print(c, " is greatest")
else:
    if b>c:
        print(b, " is greatest")
    else:
        print(c, " is greatest")

a=float(input("Enter percentage"))
if a>=85.0:
    print("Grade A")
elif a>=65.0:
    print("Grade B")
elif a>=45.0:
    print("Grade C")
else:
    print("Grade D")
