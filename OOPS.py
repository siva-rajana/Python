#                         ****** OOPS(object oriented programming structure) *******

'''
OOPS:- The Main Concepts in oops are:
    
       1. Class/Object
       2. Inheritance
       3. Polymorphism
       4. Encapsulation
       5. Abstract class/Method





1.Class:-
             A class is a blue print of an object.it is a logical structure does not exist physically.
             It does not have physical view.

             note:- The group of objects are exist in one place is called "class".

 Object:-   An object is an instance of a class.


#Creation Of simple class:-
'''
'''
 class student:
    id=100
    name="Siva"
    age=21

    def display(self):
        print("the id is:",self.id)
        print("the name is",self.name)
        print("the age  is",self.age)
s=student()
s.display()

'''
#Constructor:- It is a special method is used to initialize instance variable.

#Q.)creation of class with consturctor
'''

class student:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
    def display(self):
        print("the id is:",self.id)
        print("the name is:",self.name)
        print("the age is:",self.age)
obj=student(21,"siva",23)
obj.display()

'''

#Q.)To create dynamic representaion of class with constructor?
'''
class student:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
    def display(self):
        print("the id is:",self.id)
        print("the name is:",self.name)
        print("the age is:",self.age)

id=int(input("enter id:",))
name=input("enter name:")
age=int(input("enter age:"))

obj=student(id,name,age)
obj.display()

'''

#Q.)To find the area and perimeter of the rectangle when press 1 and square when press 2?


'''

num=int(input("enter the number:"))
if(num==1):
    class rectangle:
        def __init__(self,length,breadth,height):
             self.length=length
             self.breadth=breadth
             self.height=height
        def areaperi(self):
            print("the area of the rectangle is:",self.length*breadth)
            print("the perimeter of the rectangle is:",self.length*breadth*height)

    length=int(input("enter the length:"))
    breadth=int(input("enter the breadth:"))
    height=int(input("enter the height:"))
    
    obj=rectangle(length,breadth,height)
    obj.areaperi()
     
elif(num==2):
    class square:
        def __init__(self,side):
            self.side=side
            
        
        
        def areaperi(self):
            print("the are of the rectangle is:",self.side*side)
            print("the perimeter of the rectangle is:",self.side*side*side)

    side=int(input("enter the side:"))
    
    obj=square(side)
    obj.areaperi()
else:
    print("You entered invalid number")

'''
#                                  ****** Inheritance ******

#2.Inheritance:-
#              The ability of accessing one class properties and methods into in another class is known as "Inheritance".

#    Types of inheritance:-

#    1. Single inheritance
#    2. Multilevel inheritance
#    3. Hiererechical inheritance
#    4. Multiple inheritance.


#1.Single inheritance:- It is a type of inheritance.in this one parent class and one child class.
#                     >> In this,can acessing the parent class properties into the child class is called single inheritance.
                     
'''
# Creation single inheritance:-
'''
'''
class parent:
    def Father(self):
        print("this is parent class")
class child(parent):    
    def Son(self):
        print("this is child class")
obj=child()
obj.Father()
obj.Son()
'''
'''
#Q. To print the result required no.of times in opps concepts by using inheritance?
'''
'''
class parent:
    def Father(self):
        print("this is parent class")
class child(parent):    
    def Son(self):
        print("this is child class")

for i in range(5):        
    obj=child()
    print()
    obj.Father()
    obj.Son()
'''


#2.Multilevel inheritance:-
#                         >> In this one parent class one child class one grand class.


'''
class A:
    def father(self):
        print("I am in class A")
class B(A):
    def Child(self):
        print("I am in class B")
class C(B):
    def grandchild(self):
        print("I am in class c")
obj=C()
obj.grandchild()
obj.father()
obj.Child()

'''
#3.Multiple inheritance
'''
class a:
    x=100
    def m1(self):
        print(self.x)
class b:
    x2=200
    def m2(self):
        print(self.x2)
class c:
    x3=300
    def m3(self):
        print(self.x3)
class d(a,b,c):
    x4=400
    def m4(self):
        print(self.x4)
o=d()
o.m1()
o.m2()
o.m3()
o.m4()
'''
#4.Hiererchical inheritance:- one parent class and different no.of child class
'''
class parent:
    x=100
    def m1(self):
        print(self.x)
class child1(parent):
    x2=200
    def m2(self):
        print(self.x2)
class child2:
    x3=300
    def m3(self):
        print(self.x3)
class child3(parent):
    x4=400
    def m4(self):
        print(self.x4)
o=child3()
o.m1()
o.m4()
'''



        
#                            ************ Polymorphism *****************
#3. Polymorphism:-
#                 Polymorphism came from greek words "poly" means "many", "morphase" means "forms".
#                 In Python Operators and methods Exibhits polymorphism.
'''
There are two types of polymerphism:-
1.Compile time polymorphism
  a.operator overloading(method overloading)
2.Run time polymorphism
 a.Method over riding(method overloading)

1.Operator overloading(method overloading):- the + operator acs in 2 ways if the data type is string then it act as concatenation.
                                             if thge data is int type then act as addition opereation
                                              ex:- x=10,y=20,z=30     x="10",y="20",z=1020

2.method over riding(overloading):- it comes from inheritance concepts.


def display(id=none,name="none",age=none):
            print("the id is:",id)
            print("the name is:",name)
            print("the age is:",age)
display(10)
display(10,"siva")
display(10,"siva",21)
'''

#                 ************** Encapsulation ****************
#4. Encapsulation:-
#                > Binding up of instance variables with the method is known as Encapsulation.
#                > The main purpose of Encapsulation is to secure data without hacked by others
#                -- = private the details,it does not change only change in back.
'''
class bank:
    __acno=1020
    __name="siva"
    __bal=10000
    def show(self):
        print(self.__acno)
        print(self.__name)
        print(self.__bal)
b=bank()
b.show()

'''

#                               ************* Abstract class/method **************

#5. Abstract Class/Method:-
#                          A method which is having only definition but no implementation is called Abstract method.
#                          If any method is abstract method the total class is a "abstract class".
#                          If no abstract method,the total class is "normal class".
#                          If all methods are abstract method the total class is "interface".
''''
from abc import ABC
class dummy(abc):
    def sqrnum(n1)
    def cubenum(n2)
class caluculate(dummy):
    def sqrnum(n1):
        print("the sqr of num is:",n1*n1)
    def cubenum(n2):
        print("the cube of no os:",n2*n2*n2)
c=caluculate()
c.sqrnum(2)
c.cubenum(3)

'''
























                          
                
