                     # More about Function
                            
                            # Function as object
                            # Nested function
                            # Function as Parameter
                            # Funcrion returning a functions

 # Function as object

def display(name):
    print('Hello',name)

# print(display('Chandan'))      # Calling of function

 # Now we can call like this and function treated as an object
               # But we can assigned the function the function in other cariable
d = display  # function assigned in another     variable object like list,set,dictonary,string etc... (function is also a object)
print(d('Chandan'))     # Now we can call like this and function treated as an object



# Nested function

def outer():
    print('Chandan')
    def inner():
        return 'I am a inner function'
    # I can call inner function from Hastack of this line
    print(inner())
# I can call outer function from Hastack of this line
print(outer())


#Function as Parameter

#Ex 01
         # We can pas a function as a parameter
def display():
    print("Hello World")

def fun(d):
    d()
print(fun(display))    # Display function pass to the 'd' so that display() will be called  i.e "Hello World"

# Ex 02
def add(x,y):
    print(x+y)
def sub(x,y):
    print(x-y)

def fun(f,x,y):         # Here f is function as parameter
    f(x,y)
# when we call fun then f is taken as parameter with two assigning value at place of f we tak add function
print(fun(add,10,6))    # Same function behave as two different behavier
print(fun(sub,10,3))



# Funcrion returning a functions

def outer():
    def display():
        print('Hello World')
    return display   # Outer function give display function
d = outer()
print(d())   # One function print another function



                     # Closure Functions

                                # Nested function
                                # Accessing Non-Local Variables
                                # Return Nested function
                                # Caller class

def closure(msg ):
       def display():
        print('*'*10)
        print(msg)
             # msg is non-local variable  i.e # Accessing Non-Local Variables of closure function
        print('*'*10)
      #return display
d = closure('Hello')
print(d())   # d is a function which is refering to inner function which access to a local data 'msg'



# caller class
class Dept:
    def __init__(self):
        self.depts = {'hr': 'Human Resourse',
        'acc': 'Accounts and finance',
        'sd': 'Sales and Distribution',
        'mkt': 'Marketing Department'}
    def __call__(self,dept):
        return self.depts[dept]
d = Dept()
s = d('hr')
print(s)



# converted a caller class in to a closure function
def Depts():
    depts = {'hr': 'Human Resourse',
        'acc': 'Accounts and finance',
        'sd': 'Sales and Distribution',
        'mkt': 'Marketing Department'}
    def dname(dept):
        return depts[dept]
    return dname

d = Depts()
s = d('hr')
print(s)



              #Decorator function
                               #similer to closure function

                            #Passing function as parameter
                            #Nested function calling parameter function
                            #return nested function
                            #@ for decoration

def decorator(fun):   # outer function must take function as parameter
    def wrapper():
        print('*'*10)    # do something
        fun()      # print Hello   # so that the function that is recevied as parameter inside outer function should called whithin a nested function
        print('*'*10)    # do something
    return wrapper
def my_fun():
    print('Hello')
w = decorator(my_fun)    # display goes and take plase of fun
print(w())


def decorator(fun):   # outer function must take function as parameter
    def wrapper(msg):
        print('*'*10)    # do something
        fun(msg)      # print Hello   # so that the function that is recevied as parameter inside outer function should called whithin a nested function
        print('*'*10)    # do something
    return wrapper

@decorator       # same work as 151
def my_fun(msg):
    print('Hello')
# w = decorator(my_fun)    # display goes and take plase of fun
print(my_fun('Welcome'))



               # Lambda Functions
                           # Anonymous function
                           # Single line expression
                           # Any number of argument

# lambda argument:Expressin

#01
# def miles2km(miles):
#     kms = 1.6*miles
#     return kms
# print(miles2km(10))

# at plase of avobe code we can write
# km = lambda miles:1.6*miles   # when lambda use then not use of name of variable lambda itself act as variable
# print(km(10))

#02
def sum_(x,y):
    return x+y
print(sum_(7,7))

sum = lambda a,b: a+b
print(sum_(7,7))

# we can write conditional statements also by using lambda

f = lambda a,b:a if a>b else b
print(f(7,8))