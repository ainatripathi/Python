#Single Inheritance
class A:
    def m1(self):
        print("A class m1 method")
class B(A):
    def m2(self):
        print("B class m2 method")
b=B()
b.m1()
b.m2()

#Multilevel Inheritance
class A:
    def m1(self):
        print("A class m1 method")
class B(A):
    def m2(self):
        print("B class m2 method")
class C(B):
    def m3(self):
        print("C class is derived from class B and this is the m3 method of class C")
c=C()
c.m1()
c.m2()
c.m3()

#Hierarchical Inheritance
class A:
    def m1(self):
        print("This is the parent class of class B and class C and A class m1 method")
class B(A):
    def m2(self):
        print("B class is derived from class A and B class m2 method")
class C(A):
    def m3(self):
        print("C class is derived from class A and this is the m3 method of class C")
b=B()
c=C()
b.m1()
b.m2()
c.m1()
c.m3()

#Multiple Inheritance
class P1:
    def m1(self):
        print("m1 method of P1 class")
class P2:
    def m2(self):
        print("m2 method of P2 class")
class C(P1,P2):
    def m3(self):
        print("m3 method of Child class")

c=C()
c.m1()
c.m2()
c.m3()

#Hybrid Inheritance
class A:
    def m1(self):
        print("Class A method call")
class B(A):
    def m2(self):
        print("Class B method call")
class C(A):
    def m3(self):
        print("Class C method call")
class D(B,C):
    def m4(self):
        print("Class D method call")

d=D()
d.m1()
d.m2()
d.m3()
d.m4()

#Constructor in Parent Class
class P:
    def __init__(self):
        print("Super class constructor invoked")
class C(P):
    def m1():
        print("Child class C: member function")
c=C() #parent class constructor

#Constructors in both parent class and child class
class P:
    def __init__(self):
        print("Super class constructor invoked")
class C(P):
    def __init__(self):
        print("Child class constructor invoked")
        super().__init__() #Parent class constructor
c=C() #Child class constructor

#Question
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def disp(self):
        print("Length: ",self.length)
        print("Breadth: ",self.breadth)
class Area(Rectangle):
    def calc_area(self):
        self.ar=self.length*self.breadth
        print("Area: ",self.ar)
class Perimeter(Rectangle):
    def calc_peri(self):
        self.pm=2*(self.length+self.breadth)
        print("Perimeter: ",self.pm)

l=int(input("Enter Length of Rectangle: "))
b=int(input("Enter Breadth of Rectangle: "))
rect_area=Area(l,b)
rect_peri=Perimeter(l,b)
rect_area.disp()
rect_area.calc_area()
rect_peri.calc_peri()

