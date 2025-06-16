class Employee:
    def __init__(self):
        self.eno=1
        self.ename="aina"
        self.esal=1000
e=Employee()
print("Enter Employee number: ",e.eno)
print("Enter Employee name: ",e.ename)
print("Enter Employee salary: ",e.esal)

print(e.__dict__)

class Student:
    def m1(self):
        self.a=11
        self.b=22
        self.c=44
        print(self.a)
        print(self.b)
        print(self.c)
s=Student()
s.m1()
print(s.__dict__)

class Test:
    def __init__(self):
        print("This is Constructor")
    def m1(self):
        print("This is instance method")
t=Test()
t.m1()
t.a=20
t.b=40
t.c=60
print(t.a)
print(t.b)
print(t.c)
print(t.__dict__)

class Student:
    college_name="VSICS"
    def __init__(self,name,id):
        self.name=name
        self.id=id
s1=Student("aina",1)
s2=Student("prayan",2)
print("Student1 info: ")
print("Name: ",s1.name)
print("Id: ",s1.id)
print("Student2 info: ")
print("Name: ",s2.name)
print("Id: ",s2.id)
print("College name is: ",Student.college_name)

class Demo:
    def __init__(self,a):
        self.a=a
    def m(self):
        print(self.a)
d=Demo(101)
d.m()

#Setter and Getter Methods
class Customer:
    def set_name(self,name):
        self.name=name
    def set_id(self,id):
        self.id=id
    def get_name(self):
        return self.name
    def get_id(self):
        return self.id
c=Customer()
c.set_name("Aina")
c.set_id(101)
res1=c.get_name()
res2=c.get_id()
print("Name: ",res1)
print("Id: ",res2)

class Customer:
    def set_name(self,name):
        self.name=name
    def set_id(self,id):
        self.id=id
    def get_name(self):
        return self.name
    def get_id(self):
        return self.id
c=Customer()
n=input("Enter Name: ")
i=int(input("Enter Id: "))
c.set_name(n)
c.set_id(i)
res1=c.get_name()
res2=c.get_id()
print("Name: ",res1)
print("Id: ",res2)

class Pizza:
    radius=200
    @classmethod
    def get_radius(cls):
        return cls.radius
print(Pizza.get_radius())

class Demo:
    @staticmethod
    def sum(x,y):
        print(x+y)
    @staticmethod
    def multiply(x,y):
        print(x*y)
Demo.sum(2,3)
Demo.multiply(3,4)

class A:
    def __init__(self):
        print("Enter class object creation")
    class B:
        def __init__(self):
            print("Enter class object creation")
        def m1(self):
            print("Enter class method")

a=A()
b=a.B()
b.m1()
