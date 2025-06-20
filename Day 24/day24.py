#constructor,class, static and instance methods of parent class accessible through constructor of child class using this method
class P:
    def __init__(self):
        print("Parent class Constructor")
    def m1(self):
        print("Parent instance method")
    @classmethod
    def m2(cls):
        print("Parent class method")
    @staticmethod
    def m3():
        print("Parent static method")
class C(P):
    def __init__(self):
        super().__init__()
        super().m1()
        super().m2()
        super().m3()
c=C()
    
#class and static methods of parent class accessible through class method of child class
class P:
    def __init__(self):
        print("Parent class Constructor")
    def m1(self):
        print("Parent instance method")
    @classmethod
    def m2(cls):
        print("Parent class method")
    @staticmethod
    def m3():
         print("Parent static method")
class C(P):
    @classmethod
    def m1(cls):
        super().m2()
        super().m3()
C.m1()

#constructor and instance method of parent class not accessible through class method of child class
class P:
    def __init__(self):
        print("Parent class Constructor")
    def m1(self):
        print("Parent instance method")
    @classmethod
    def m2(cls):
        print("Parent class method")
    @staticmethod
    def m3():
        print("Parent static method")
class C(P):
    @classmethod
    def m1(cls):
        super().__init__()
        super().m1()
#C.m1()

#constructor and instance method of parent class accessible through class method of child class using this method
class P:
    def __init__(self):
        print("Parent class Constructor")
    def m1(self):
        print("Parent instance method")
    @classmethod
    def m2(cls):
        print("Parent class method")
    @staticmethod
    def m3():
        print("Parent static method")
class C(P):
    @classmethod
    def m1(cls):
        super(C,cls).__init__(cls)
        super(C,cls).m1(cls)
C.m1()

#Operator Overloading
print(10+20)
print("Python"+"Programming")
print([1,2,3]+[4,5,6])

print(10*20)
print("Python"*3)
print([1,2,3]*3)

##class Student:
##    def __init__(self,name,marks):
##        self.name=name
##        self.marks=marks
##s1=Student("Samvida",97)
##s2=Student("Surya",85)
##print("s1>s2: ",s1>s2)
##print("s1<s2: ",s1<s2)
##print("s1>=s2: ",s1>=s2)
##print("s1<=s2: ",s1<=s2)

class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __gt__(self,other):
        return self.marks>other.marks
    def __lt__(self,other):
        return self.marks<other.marks
    def __ge__(self,other):
        return self.marks>=other.marks
    def __lt__(self,other):
        return self.marks<=other.marks
s1=Student("Samvida",97)
s2=Student("Surya",85)
print("s1>s2: ",s1>s2)
print("s1<s2: ",s1<s2)
print("s1>=s2: ",s1>=s2)
print("s1<=s2: ",s1<=s2)

class Book:
    def __init__(self,pages):
        self.pages=pages
b1=Book(100)
b2=Book(200)
print(type(b1))
print(type(b2))
print(type(b1.pages))
print(type(b2.pages))
print(b1.pages+b2.pages)
print((b1.pages).__add__(b2.pages))

#Method overloading
class Demo:
    def m1(self):
        print("no-arg method")
    def m1(self,a):
        print("One-arg method")
    def m1(self,a,b):
        print("two-arg method")
d=Demo()
#d.m1() (Error)
#d.m1(10) (Error)
d.m1(10,20)

class Demo:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("The sum of 3 numbers: ",(a+b+c))
        elif a!=None and b!=None:
            print("The sum of 2 numbers: ",(a+b))
        else:
            print("Please provide 2 or 3 arguments")
d=Demo()
d.sum(10,20,30)
d.sum(10,20)
d.sum(10)
