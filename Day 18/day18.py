#Exception Handling
try:
    #x=int("hello")
    #y=10/0
    x=("hello")
    y=10
except ValueError:
    print(x)
    print("ValueError occured")
except ZeroDivisionError:
    print(y)
    print("ZeroDivisionError occured")

#catching any exception
try:
    a=int("abc")
except Exception as e:
    print("Error: ",e)
    
try:
    a=10/0
except Exception as e:
    print("Error: ",e)

try:
    a="23"+1
except Exception as e:
    print("Error: ",e)

#try, except, else, finally
try:
    x=int(input("Enter a number: "))
    print("Square: ",x*x)
except ValueError:
    print("Invalid input")
else:
    print("Executed without error")
finally:
    print("This block always executes")

#raise error
age=int(input("Enter age: "))
if age<18:
    raise ValueError("Age must be 18 or older")
else:
    print("Access granted")

#nested try
try:
    try:
        x=int('abc')
    except ValueError:
        print("Inner Try Block")
    print("Outer Try Block")
except Exception:
    print("Outer Except Block")

#File Handling
f=open("aina.txt",'w')
print("File Name: ",f.name)
print("File mode: ",f.mode)
print("Is file readable: ",f.readable())
print("Is file writable: ",f.writable())
print("Is file closed: ",f.closed)
f.close()
print("Is file closed: ",f.closed)

#write(str)
f=open("aina.txt",'w')
f.write("Welcome\n")
f.write("to\n")
f.write("Python world\n")
print("Data written to the file successfully")
f.close()

f=open("aina.txt",'w')
f.write("Welcome\n")
f.write("to\n")
f.write("Python world\n")
print("Data written to the file successfully")
f.close()

f=open("aina.txt",'a')
f.write("Welcome\n")
f.write("to\n")
f.write("Python world\n")
print("Data written to the file successfully")
f.close()

#writelines(list)
f=open("aina.txt",'a')
list=["aina\n","gauri\n","pragati\n"]
f.writelines(list)
print("List written to the file successfully")
f.close()

#read()
f=open("aina.txt",'r')
data=f.read()
print(data)

#read(n)
f=open("aina.txt",'r')
data=f.read(20)
print(data)

#readline()
f=open("aina.txt",'r')
line1=f.readline()
print(line1,end="")
line2=f.readline()
print(line2,end="")
line3=f.readline()
print(line3,end="")
line4=f.readline()
print(line4,end="")

#readlines()
f=open("aina.txt",'r')
lines=f.readlines()
for line in lines:
    print(line,end="")
f.close()
