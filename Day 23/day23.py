#Method Resolution Order
class A:
    def m1(self):
        print("m1 from A")
class B(A):
    def m1(self):
        print("m1 from B")
class C(A):
    def m1(self):
        print("m1 from C")
class D(B,C):
    def m1(self):
        print("m1 from D")
print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro())

class A:
    def m1(self):
        print("m1 from A")
class B(A):
    def m1(self):
        print("m1 from B")
class C(A):
    def m1(self):
        print("m1 from C")
class D(B,C):
    def m1(self):
        print("m1 from D")
c=C()
c.m1()
print(C.mro())

class A:
    def m1(self):
        print("m1 from A")
class B(A):
    def m1(self):
        print("m1 from B")
class C(A):
    def m1(self):
        print("m1 from C")
class D(B,C):
    def m1(self):
        print("m1 from D")
d=D()
d.m1()
print(D.mro())

class A:
    def m1(self):
        print("m1 from A")
class B(A):
    def m2(self):
        print("m2 from B")
class C(A):
    def m1(self):
        print("m1 from C")
class D(B,C):
    def m3(self):
        print("m3 from D")
d=D()
d.m1()
print(D.mro())

class A:
    def m1(self):
        print("m1 from A")
class B:
    def m1(self):
        print("m1 from B")
class C:
    def m1(self):
        print("m1 from C")
class X(A,B):
    def m1(self):
        print("m1 from X")
class Y(B,C):
    def m1(self):
        print("m1 from Y")
class P(X,Y,C):
    def m1(self):
        print("m1 from P")

print(A.mro())
print(B.mro())
print(C.mro())
print(X.mro())
print(Y.mro())
print(P.mro())

class A:
    def __init__(self):
        print("Super class A constructor")
class B(A):
    def __init__(self):
        print("Child class B constructor")
        super().__init__()
b=B()

class A:
    x=10
    def m1(self):
        print("Super class A: m1 method")
class B(A):
    x=20
    def m1(self):
        print("Child class variable: ",self.x)
        print("Super clas variable: ",super().x)
b=B()
b.m1()

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
class Employee(Person):
    def __init__(self,name,age,empno,address):
        super().__init__(name,age)
        self.empno=empno
        self.address=address
    def display(self):
        super().display()
        print("Employee No: ",self.empno)
        print("Address: ",self.address)
e1=Employee("Aina",18,101,"Kanpur")
e1.display()

class A:
    def m1(self):
        print("m1 from A")
class B(A):
    def m1(self):
        print("m1 from B")
class C(B):
    def m1(self):
        print("m1 from C")
class D(C):
    def m1(self):
        print("m1 from D")
class E(D):
    def m1(self):
        print("m1 from E")
        A.m1(self)
        B.m1(self)
        C.m1(self)
        D.m1(self)
e=E()
e.m1()

class A:
    def m1(self):
        print("m1 from A")
class B(A):
    def m1(self):
        print("m1 from B")
class C(B):
    def m1(self):
        print("m1 from C")
class D(C):
    def m1(self):
        print("m1 from D")
class E(D):
    def m1(self):
        print("m1 from E")
        super(D,self).m1()
e=E()
e.m1()

class P:
    def __init__(self):
        self.a=20
class A(P):
    def m1(self):
       # print("a: ",super().a) #Error
        print(self.a)

a=A()
a.m1()

class P:
    a=20
class A(P):
    def m1(self):
        print("a: ",super().a)

a=A()
a.m1()
