#class and object
#class variables
class Employee:
    name="Aina"
    id=101
    salary=20000
emp=Employee()
print(emp.name)
print(emp.id)
print(emp.salary)
print("------------------------------------------")

#class method
class Demo:
    def disp(self):
        print("This is a member function of Demo Class")

d=Demo()
d.disp()
print("------------------------------------------")

#Question 1
class Employee:
    def __init__(self):
        print("Constructor invoked successfully")
    def input(self):
        self.name=input("Enter Employee Name: ")
        self.id=int(input("Enter Employee Id: "))
        self.salary=int(input("Enter Employee Salary: "))
    def output(self):
        print("Employee Name is: ",self.name)
        print("Employee Id is: ",self.id)
        print("Employee Salary is: ",self.salary)
emp=Employee()
emp.__init__()
emp.input()
emp.output()
print("------------------------------------------")

#Parameterized constructor
class Employee:
    def __init__(self,name,id,salary):
     self.name=name
     self.id=id
     self.salary=salary
    def output(self):
        print("Employee Name is: ",self.name)
        print("Employee Id is: ",self.id)
        print("Employee Salary is: ",self.salary)
emp=Employee("Aina",2,46543)
emp.output()
print("------------------------------------------")

#Question 2
class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def rect_parameter(self):
        self.parameter=2*(self.length+self.breadth)
    def rect_area(self):
        self.area=self.length*self.breadth
    def putdata(self):
        print("Length of Rectangle: ",self.length)
        print("Breadth of Rectangle: ",self.breadth)
        print("Parameter of Rectangle: ",self.parameter)
        print("Area of Rectangle: ",self.area)
l=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))
rect=Rectangle(l,b)
rect.rect_parameter()
rect.rect_area()
rect.putdata()

