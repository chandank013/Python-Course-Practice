                # Object Oriented Programming

class Cuboid:
    def __init__(self,l,b,h):
        self.length = l
        self.breadth = b
        self.height = h

    def lidarea(self):
        return self.length * self.breadth
    
    def totalarea(self):
        return (self.length * self.breadth + self.breadth * self.height + self.length * self.height )
    
    def volume(self):
        return self.length * self.breadth * self.height
    
c1 = Cuboid( 4,7,9)
print(c1.volume())
c1 = Cuboid( 14,74,29)
print(c1.volume())



# Self and constructor
  # (self and c1 are same can br=e cheaked by it's  id's)
class Cuboid:
    def __init__(self,l,b,h):
        self.length = l
        self.breadth = b
        self.height = h

    def lidarea(self):
        return self.length * self.breadth
    
    def totalarea(self):
        return (self.length * self.breadth + self.breadth * self.height + self.length * self.height )
    
    def volume(self):
        print(id(self))
        return self.length * self.breadth * self.height
c1 = Cuboid( 14,74,29)
print(id(c1))
print(c1.volume())

c2 = Cuboid( 15,7,2)
print(id(c2))
print(c2.volume())


#Q can we write more than one constructor (YES but at a time only one can execute)

class Cuboid:
    def __init__(self,l,b,h):
        self.length = l
        self.breadth = b
        self.height = h
    def __init___(self):
        pass

    def lidarea(self):
        return self.length * self.breadth
    
    def totalarea(self):
        return (self.length * self.breadth + self.breadth * self.height + self.length * self.height )
    
    def volume(self):
        print(id(self))
        return self.length * self.breadth * self.height
c1 = Cuboid( 14,74,29)
print(id(c1))
print(c1.volume())

c2 = Cuboid( 15,7,2)
print(id(c2))
print(c2.volume())

    

        # we can make value optional 

class Cuboid:
    def __init__(self,l=1,b=1,h=1):
        self.length = l
        self.breadth = b
        self.height = h
    def lidarea(self):
        return self.length * self.breadth
    
    def totalarea(self):
        return (self.length * self.breadth + self.breadth * self.height + self.length * self.height )
    
    def volume(self):
        print(id(self))
        return self.length * self.breadth * self.height
    

c1 = Cuboid()
c1 = Cuboid(10)
c1 = Cuboid(10,3)
c4 = Cuboid( 14,74,29)
print(id(c4))
print(c4.volume())

c2 = Cuboid( 15,7,2)
print(id(c2))
print(c2.volume())


#Instance variable and Instance method: 
#creating instance variable under constructor and any else places

class Test:
    def __init__(self):
        self.a=10
    def fun(self):
        self.b=20
t1 = Test()
t1.fun()
t1.c=30
print(dir(t1))
#['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__',  'a', 'b','c', 'fun']
# Note: we can create instance variable at three places and the method of accessing is called instance method.


# Class method and Class variable:
class Rectangle:
    count = 0   # Class/Static variable i.e belong to both instance or object

    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
        Rectangle.count+=1
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    def area(self):
        return self.length * self.breadth
    
    @classmethod
    def countRect(cls):   # count how many rectangles are created
        print(cls.count)

r1 = Rectangle(3,8)
# print(Rectangle.count)
r2 = Rectangle(5,8)
# print(Rectangle.count)

r1 or r2.countRect()    # any one at a time , common for both



# Static Method: 
class Rectangle:

    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
       
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    def area(self):
        return self.length * self.breadth
    @staticmethod       # decorator
    def issquare(len,bre):
        return len == bre

r1 = Rectangle(23,49)
print(r1.issquare(10,10))



# Accessor and Mutator:
class Rectangle:

    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    def area(self):
        return self.length * self.breadth
    def getlength(self):     # give the value of length
        return self.length
    def setlength(self,l):   # Modify the value of length
        self.length = l
    
r = Rectangle(10,3)
print(r.getlength())
print(r.setlength(24))
print(r.getlength())


# What is inheritence:
class Rectangle:

    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    def area(self):
        return self.length * self.breadth
class Cubiod(Rectangle):

    def __init__(self,h):
        self.heigh = h
        def volume(self):
            return self.length*self.breadth*self.heigh



# Constructor in Inheritence:
class Rectangle:

    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    def area(self):
        return self.length * self.breadth
class Cubiod(Rectangle):

    def __init__(self,l,b,h):
        self.heigh = h
        super().__init__(l,b)    # It called the constructor of parent class
    def volume(self):
        return self.length*self.breadth*self.heigh

c = Cubiod(5,2,7)
print(c.volume())


# Inner / Nested class
class customer:

    def __init__(self,id,name,billing_door_no,billing_street,billing_city,billing_country,billing_pin_code,shipping_door_no,shipping_street,shipping_city,shipping_country,shipping_pin_code):
        self.custid = id
        self.custname = name
        self.billing_add = self.Address(billing_door_no,billing_street,billing_city,billing_country,billing_pin_code)
        self.shpping_add = self.Address(shipping_door_no,shipping_street,shipping_city,shipping_country,shipping_pin_code)
    class Address:
        def __init__(self,door_no,street,city,country,pin_code):
            self.door_no = door_no
            self.street = street
            self.city = city
            self.country = country
            self.pin_code = pin_code
        
        def Display(self):
            print(self.door_no)
            print(self.street)
            print(self.city)
            print(self.country)
            print(self.pin_code)

c = customer(10,'john',101,'abc','Delhi','India',500001,201,'ijk','mumbai','India',431001)
c.billing_add.Display()
c.shpping_add.Display()



# Polymorphism:
# DuckTyping

#Eg01:
def Driver(Car):
    Car.drive()

class Creta:
    def drive(self):
        print('Creta is driving.')

class Mercedes:
    def drive(self):
        print('Mercedes is driving.')

c = Creta()
Driver(c)
m = Mercedes()
Driver(m)

#Eg02
def PetLover(pet):
    pet.talk()
    pet.walk()

class Duck:
    def talk(self):
        print('Duck is talking.')
    def walk(self):
        print('Duck is walking.')
class Dog:
    def talk(self):
        print('Dog is talking.')
    def walk(self):
        print('Dog is walking.')

# d = Duck()
# PetLover(d)
d_g = Dog()
PetLover(d_g)

#if any method is not persent like pet.walk() then it's show error then error can remove:
#Eg of removing error:
def PetLover(pet):
    pet.talk()
    if hasattr(pet,'walk'):
        pet.walk()

class Duck:
    def talk(self):
        print('Duck is talking.')
    def walk(self):
        print('Duck is walking.')
class Dog:
    def talk(self):
        print('Dog is talking.')


# d = Duck()
# PetLover(d)
d_g = Dog()
PetLover(d_g)



#Method Overloading:
class Arith:
    def sum(x,y):
        return x+y

a = Arith
print(a.sum(10,6))        # Single method adding int, float and string at different achiving polymorphism
print(a.sum(10.6,6.8))
print(a.sum('Hello',' World'))

class Arith:
    def sum(x,y):
        return x+y
    def sum(x,y,z):
        return x+y+z

a = Arith
print(a.sum(10,6,9))        # Single method adding int, float and string at different achiving polymorphism
print(a.sum(10.6,6.8))



# Modification of code to execute multiple parameter in single method  at different time:
class Arith:
    def sum(self,x,y,z = None):
        s = x+y
        if z == None:
            return s
        else:
            return s + z
a = Arith()
print(a.sum(10,6,9))     
print(a.sum(10.6,6.8))



# Method Overriding:   # It's mean inherit the parent class to child in modified form by child in their on style
class iPhone_VI:
    def home(self):
        print('Home button is pressed.')
class iPhone_X(iPhone_VI):
    def home(self):
        print('Home tab is touched.')
        super().home()       # Through this we can called parent class to chiild class
    
i_VI = iPhone_VI()
i_VI.home()

i_X =iPhone_X()
i_X.home()



# Operator Overloading:
class Rational():
    def __init__(self,p=1,q=1):
        self.p = p
        self.q = q
    
    def __add__(self,other):
        s = Rational()
        s.p = self.p*other.q + self.q*other.p
        s.q = self.q * other.q
        return s
    def __str__(self):    # used to get the rational number as in the form of p/q
        return str(self.p) + '/' + str(self.q)
        
    
r1 = Rational(2,3)
r2 = Rational(2,5)
sum = r1 + r2
# print(sum.p ,sum.q)
print(sum)



# Abstract Class and Interface:
from abc import ABC , abstractmethod

class Parent(ABC):              # Any calss inherited from ABC it's become a abstract class
    @abstractmethod
    def show(self):
        pass

    def display(self):         # Any method which have body called concrete
        print('Parent Display')

class Child(Parent):
    def show(self):               # Inherit from parent it must override show method
        print('Show from Child')
c = Child()
c.show()
c.display()



#Method Resolution Order (MRO)
#classname.mro()

class A:
    pass
class B():
    def show(self):
        print('B')

b = B()
b.show()

class A:
    def show(self):
        print('A')
class B(A):
    pass

b = B()
b.show()


print(B.mro())
#[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

# Multilevel Inheritance
class A:
    def show(self):
        print('A')
class B(A):
    pass
class C(B):
    pass

c = C()
c.show()

print(C.mro())
#[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

# Multiple Inheritance
class A:
    def show(self):
        print('A')

class B:
    def show(self):
        print('B')
class C(A,B):
    pass


c = C()
c.show()

print(C.mro())
#[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

class A:
    def show(self):
        print('A')

class B(A):
    pass

class C:
    pass

class D(C):
    pass
class E(B,D):
    pass


e = E()
e.show()
print(E.mro())
#[<class '__main__.E'>, <class '__main__.A'>, <class '__main__.D'>, <class '__main__.C'>, <class 'object'>]

class P:
    pass
class A(P):
    def show(self):
        print('A')

class B(A):
    pass

class X(P):
    pass


class Y(X):
    pass
class C(B,Y):
    pass


c = C()
c.show()
print(C.mro())
#[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.Y'>, <class '__main__.X'>, <class '__main__.P'>, <class 'object'>]


             #It is called as depth first left - right
              #Also called as C3 linearisation 