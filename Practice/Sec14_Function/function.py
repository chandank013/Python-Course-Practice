                        #Functions
def add_3(a,b,c):
    add = a+b+c
    return add

print(add_3(5,7,4))
#Only for cheaking the id of outside and inside function
#print('inside function:',id(a),id(b),id(c)) 

x,y,z = 10,14,6
print('outside function:',id(x),id(y),id(z))
add_3(x,y,z)



def net_sal(basic,allowance,deduction):
    print('allowance',allowance)
    print('basic',basic)
    print('deduction',deduction)
    net=basic+allowance-deduction
    return net

print(net_sal(8000,6000,2000))
print(net_sal(basic=8000,allowance=6000,deduction=2000))
print(net_sal(8000,allowance=6000,deduction=2000))   # it's also work as same keyword argument



#Default argument
def add_3(a,b,c):
    return a+b+c

print(add_3(6,7,4))

def add_3(a,b=0,c=0):
    return a+b+c

print(add_3(6,7))

def additem(item,L = []):
    L.append(item)
    return L

L1 = [1,2,3,4]
additem(5,L1)
print(L1)

print(additem(34))       # # in this case again and again new list not created
print(additem(33))
print(additem(53))

print(additem(34,L=[]))   # in this case again and again new list created
print(additem(33,L=[]))
print(additem(53,L=[]))


def fun1(*args):
    print(type(args),args)

fun1()
fun1(1,2)
fun1(10,20,30,40,50,60,70,80,90,100)
fun1(10,'hello',24,75,True)


def fun1(a,b,*args):
    print(a,b,args)

# fun1()
fun1(1,2)
fun1(10,20,30,40,50,60,70,80,90,100)
fun1(10,'hello',24,75,True)

def fun2(a,b,c):
    print(a,b,c)
# list1 = [10,45,25]
# tuple1 = (10,45,25)
# set1 = {10,45,25}
string1 = 'CKG'

# print(fun2((list1[0]),(list1[1]),(list1[2])))
print(fun2(*string1 ))


def fun2(a,b,c):
    return a+1,b+1,c+1
# x,y,z = fun2(10,20,30)
# print(x,y,z)
t = fun2(10,20,30)   # t will be in the form of tuple
print(t)
print(type(t))       # tuple


def funs(**chandan_add):
    for x in chandan_add:
        print(x,chandan_add[x])

funs(name = 'Chandan.k',roll_no = '24BDS013',add = 'Bagaha')


def funs(a,b,*args,**chandan_add):
    print(a,b,args,chandan_add)
funs(10,30,1,2,3,4,name = 'Chandan')



#Iterator and generators

l1 = {1,2,3,4,5}       # Also tuple,dict,list and string
itr = iter(l1)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

l1 = {1:'A',2:'B',3:'C',4:'D',5:'E'}       # Also tuple,set,list and string
itr = iter(l1)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
     
def Days():
    l = ['mon','tue','wed','thu','fri','sat','sun']
    i = 0
    while True:
        x = l[i]
        i = (i+1)%7
        yield x
d = Days()          # Act as generator
print(next(d))
print(next(d))
print(next(d))

g = 10
print('outside',g)
def fun1(a,b):
    c = a+b
    print('local variable becouse belong to within the function',c)
    print('global variable becouse belong to entire function',g)
print('outside',g)
#print(c)           # show error we can't access the local variable outside the function
fun1(4,8)


g = 10              # global variable
def fun1():         
    g = 20          # local variable
    print('inside',g)
fun1()
print('outside',g)

g = 10              # global variable
def fun1(): 
    global g        
    g = g + 35         # local variable
    print('inside',g)
fun1()
print('outside',g)


a,b,c,f = 10,20,30,40
def fun9 ():
    x,y,z = 11,22,33
    print(locals())
fun9()
print(globals())     # gives output as dictonary



#Recursive function (function call itself)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(4))

def sum_of_natural_number(n):
    if n <= 1:
        return 1
    else:
        return n + sum_of_natural_number(n-1)
print(sum_of_natural_number(5))   #method 1
    
# Examole use                     #method 2
num = int(input("Enter a positive integer: "))
if num < 0:
    print("Please enter a positive integer.")
else:
    result = sum_of_natural_number(num)
    print(f"The sum of natural numbers up to {num} is: {result}")



#Built-in-Functions

# 01 abs()
a = -15
b = -17.5
c = 34
d = 4+6j     # give absolute value sqrt a^2 + b^2
print(abs(a))
print(abs(b))
print(abs(c))
print(abs(d))

#02 ascii()
letter = '\u0521'
print(letter)
print(ascii(letter))

# 03 bin()
print(bin(5))

# 04 bool()
print(bool('A'))
print(bool(0))

# 05 bytearray(),bytes() # Both are similer
print(bytearray(5))
s = 'abcde'
s1 = bytearray(s.encode())

for i in s1:     # we can get ascii code by using loop
    print(i)

s1.append(102)   # we can also append
print(s1)        # bytes() has same work but it is immutable

#What are module
    #ModuleOne.py
    #MyProgram.py





