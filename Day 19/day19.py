#File handling
f=open("aina.txt",'w')
with open("aina.txt",'a') as f:
    f.write("Learning python\n")
    f.write("file handling\n")
print("Is file closed: ",f.closed)
f=open("aina.txt",'r')
#print(f.tell(1))
#print(f.tell(2))
print(f.tell())
print(f.read(3))
print(f.tell())
print(f.read(5))

data="Kalki movie is excellent."
f=open("aina.txt",'w')
f.write(data)
with open("aina.txt",'r+') as f:
    text=f.read()
    print((text))
    print("the current cursor position: ",f.tell())
    f.seek(22)
    print("the current cursor position: ",f.tell())
    f.write("Britannia biscuit")
    f.seek(0)
    text=f.read()
    print("Data after modification: ")
    print(text)

#not working
f1=open("download1.jpg",'wb')
f2=open("download2.jpg",'wb')
bytes=f1.read()
f2.write(bytes)
print("New image is available with the name: download2.jpg")

f1=open("download1.jpg",'rb')
f2=open("download2.jpg",'wb')
bytes=f1.read()
f2.write(bytes)
print("new printed")

#csv file
import csv
with open("employee.csv",'w',newline='') as f:
    w=csv.writer(f)
    w.writerow(["EMP NO","EMP NAME","EMP SAL","EMP ADDR"])
    n=int(input("Enter number of employees"))
    for i in range(n):
        eno=int(input("Enter no of employees"))
        ename=input("Enter employee name")
        esal=int(input("Enter salary"))
        eaddr=input("Enter address")
        w.writerow([eno,ename,esal,eaddr])
    print("Total employees data written in csv file successfully")

import csv
with open("employee.csv",newline='') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)
