#Method Overloading with variable number of arguments
class Demo:
    def sum(self,*a):
        total=0
        for x in a:
            total+=x
        print("The Sum: ",total)
d=Demo()
d.sum(10,20,30)
d.sum(10,20)
d.sum(10)

#Constructor overloading
class Demo:
    def __init__(self):
        print("No-Arg Constructor")
    def __init__(self,a):
        print("One-Arg Constructor")
    def __init__(self,a,b):
        print("Two-Arg Constructor")
#d1=Demo() (Error)
#d2=Demo(10) (Error)
d3=Demo(10,20)

class Demo:
    def __init__(self,a=None,b=None,c=None):
        print(a)
        print(b)
        print(c)
d1=Demo()
d2=Demo(10,20)
d3=Demo(10,20,30)

class Demo:
    def __init__(self,*a):
        print("Constructor with variable number of arguments")
        total=0
        for x in a:
            total+=x
        print("The Sum: ",total)
d1=Demo()
d2=Demo(10,20)
d3=Demo(10,20,30)
d4=Demo(10,20,30,40)

#Method Overriding
class P:
    def properties_status(self):
        print("Money, Land, Gold")
    def to_marry(self):
        print("Anushka")
class C(P):
    def study_status(self):
        print("Studies done waiting for job")
    def to_marry(self):
        print("Megha")
c=C()
c.properties_status()
c.to_marry()
c.study_status()

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Employee(Person):
    def __init__(self,name,age,empno,empsal):
        super().__init__(name,age)
        self.empno=empno
        self.empsal=empsal
    def display(self):
        print("Employee Name: ",self.name)
        print("Employee Age: ",self.age)
        print("Employee Number: ",self.empno)
        print("Employee Salary: ",self.empsal)
e1=Employee("Megha",23,464,74156)
e2=Employee("Arushi",30,662,71454)
e1.display()
e2.display()

#Abstraction
from abc import *
class Demo1(ABC):
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass
    def m3(self):
        print("Implemented method")
class Child(Demo1):
    def  m1(self):
        print("Abstract method m1() defined")
    def  m2(self):
        print("Abstract method m2() defined")
ch=Child()
ch.m3()
ch.m1()
ch.m2()

from abc import ABC, abstractmethod
class Bank(ABC):
    def bank_info(self):
        print("Welcome to Bank!")
    @abstractmethod
    def interest(self):
        pass
class SBI(Bank):
    def interest(self):
        print("In SBI, interest is Rs. 5")
s=SBI()
s.bank_info()
s.interest()

from abc import ABC, abstractmethod
class Bank(ABC):
    def bank_info(self):
        print("Welcome to Bank!")
##    @abstractmethod
##    def interest(self): (It will throw a TypeError because Abstract method is not defined in child class)
##        pass
class SBI(Bank):
    def balance(self):
        print("Balance is 100")
s=SBI()
s.bank_info()
s.balance()

from abc import ABC, abstractmethod
class Bank(ABC):
    def bank_info(self):
        print("Welcome to Bank!")
    @abstractmethod
    def interest(self):
        pass
class SBI(Bank):
    def balance(self):
        print("Balance is 100")
    def interest(self):
        print("Interest is 10%")
s=SBI()
s.bank_info()
s.balance()
s.interest()

#Hierarchical Inheritance in Abstract Classes
from abc import ABC, abstractmethod
class Bank(ABC):
    def bank_info(self):
        print("Welcome to Bank!")
    @abstractmethod
    def interest(self):
        pass
    def offers(self):
        print("Providing offers")
class SBI(Bank):
    def interest(self):
        print("In SBI, interest is Rs. 5")
class HDFC(Bank):
    def interest(self):
        print("In HDFC, interest is Rs. 7")
s=SBI()
h=HDFC()
s.bank_info()
s.interest()
s.offers()
h.bank_info()
h.interest()
h.offers()

from abc import ABC,abstractmethod
class One(ABC):
    @abstractmethod
    def calculate(self,a):
        pass
    def m1(self):
        print("Implemented method")
class Square(One):
    def calculate(self,a):
        print("Square: ",(a*a))
class Cube(One):
    def calculate(self,a):
        print("Cube: ",(a*a*a))
c=Cube()
s=Square()
s.calculate(2)
c.calculate(2)

