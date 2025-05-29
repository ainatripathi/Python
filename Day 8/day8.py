#Indexing
wish="Hello World"
print(wish[0])
print(wish[1])
print(wish[-1])
print(wish[-2])
name="Python"
for a in name:
    print(a)

#Slicing
#[start:end:step]
print(wish[::])
print(wish[:])
print(wish[0:9:1])
print(wish[0:9:2])
print(wish[2:4:1])
print(wish[::2])
print(wish[2::])
print(wish[:4:])
print(wish[-4:-1])

#Strings are immutable
name="Aina"
print(name[0])
#name[0]="x" (Error)

#Concatenation
a="Python"
b="Programming"
print(a+b)

#Repetition
a="Python"
b=4
#print(a+b) (Error)
print(a*b)

#Length of string
course="Python"
print("Length of string: ", len(course))

#Membership operator
print('p' in 'python')
print('z' in 'python')
print('on' in 'python')
print('pa' in 'python')

main=input("Enter a string")
s=input("Enter substring")
if s in main:
    print(s, " is found in main string")
else:
    print(s, " is not found in main string")

#Comparing two strings
s1="abcde"
s2="abcdefg"
print(s1==s2)
if(s1==s2):
    print("Same")
else:
    print("Not same")

user_name="rahul"
name=input("Please Enter user name: ")
if user_name==name:
    print("Welcome to Gmail!", name)
else:
    print("Invalid user name. Please try again")

s1="abcd"
s2="abcd "
print(s1==s2)
if s1==s2:
    print("Same")
else:
    print("Not same")

course="Python  "
print("with spaces course length is: ",len(course))
x=course.strip()
print("After removing spaces course length is: ",len(x))

course="Python programming language"
print(course.find("p"))
print(course.find("a",1,20))

s="Python programming language"
print(s.index("Python"))
print(s.index("programming"))
print(s.index("language"))

s="Python programming language, Python is easy"
print(s.count("Python"))
print(s.count("Hello"))

s1="Java programming language"
s2=s1.replace("Java", "Python")
print(s1)
print(s2)
print(id(s1))
print(id(s2))

message="Python programing language"
n=message.split()
print("Before splitting: ", message)
print("After splitting: ", n)
print(type(n))
for x in n:
    print(x)
