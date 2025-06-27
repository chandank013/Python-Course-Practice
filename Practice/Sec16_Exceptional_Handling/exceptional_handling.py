                    # Exceptional handling

L = [10,20,30,40,50]
ndex = int(input("Enter the index"))
#print(L[index])

val = int('abc')
print(type(val))    # Value error

a = 10
s = 'number'
print(a + s)         # type error

d = {1:'a',2:'b',3:'c'}

key = (input("enter a key:"))
print(d[key])       # Key error

a = 20
b = 0
d = a//b
print(d)            # Zero division error



#How to handle error
          #We an use error by using try-except syntex statement

L = [10,20,30,40,50]
try:
    index = int(input("Enter the index:"))
    print(L[index])      # if index will be from out of range program jump in to except block
    print('End of try block')   # then it will not print
except:
    print("Invalid index")
print('Terminated Gracefully')



#How to handle multiple exception
L = [10,20,30,40,50]
try:
    index = int(input("Enter the index:"))
    print(L[index])      
    print('End of try block')   
except IndexError:    # it only handle index error if other error will be there it cannothandle. 
    print("Invalid index")
print('Terminated Gracefully')



L = [10,20,30,40,50]   # handle multiple error
try:
    index = int(input("Enter the index:"))
    print(L[index])      
    print('End of try block')   
except IndexError:      # now this program can handle two error one valueError and IndexError
    print("Invalid index")
except ValueError:
    print('Enter only integer value')
print('Terminated Gracefully')



L = [10,20,30,40,50]   # handle multiple error
try:
    index = int(input("Enter the index:"))
    print(L[index])      
    print('End of try block')   
except IndexError:      # now this program can handle two error one valueError and IndexError
    print("Invalid index")
except ValueError:
    print('Enter only integer value')
except:                    # If you don't know what is error theadd this in last
    print('Some error') 
print('Terminated Gracefully')



# How to handle multiple exception and getting dription of error also
L = [10,20,30,40,50]
try:
    index = int(input("Enter the index:"))
    print(L[index])      
    print('End of try block')   
except IndexError as msg:   # msg give discription of error
    print("Invalid index",msg)
print('Terminated Gracefully')



# How to handle multiple exception in single except block
L = [10,20,30,40,50]
try:
    index = int(input("Enter the index:"))
    print(L[index])      
    print('End of try block')   
except (IndexError, ValueError) as msg:   # a singlr except can handle multiple exceptional error
    print(msg)
print('Terminated Gracefully')



# Why try - Except  # help in handling exceptional cases

a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))

if b!= 0:
    res = a//b
    print(res)
else:
    print("ZeroDivision Error")

def error_detecting(x,y):
    if y!=0:
        c = x//y
        return c
    else:
        return -1

x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))

c = error_detecting(x,y)
if c == -1:
    print('zeroDivisionError')
else:
    print(c)  # it also show zerodivision error when we take -10 and 10


def error_detecting(x,y):
    if y!=0:
        c = x//y
        return c
    else:
        raise ZeroDivisionError



x = int(input("Enter the first number:"))
y = int(input("Enter the second number:"))

try:
    c = error_detecting(x,y)
    print(c)
except:
    print('ZeroDivisionError')


# try-except-else
print('before try')

try:
    a = int(input('Enter the first num:'))
    b = int(input('Enter the second num:'))
    c = a//b
    print('Try block executed successfully')
except ZeroDivisionError as err:
    print(err)

else:
    print('Division is',c)
print('Outside try-except-else')


# finally block
print('before try')

try:
    a = int(input('Enter the first num:'))
    b = int(input('Enter the second num:'))
    c = a//b
    print('Try block executed successfully')
except ZeroDivisionError as err:
    print(err)

else:
    print('Division is',c)
finally:
    print('finally block.')
print('Outside try-except-else')

def div(a,b):
    try:
        c = a//b
        return c
    except  ZeroDivisionError as err:
        raise ZeroDivisionError 
        
    finally:
        print('finally block')
print(div(10,0))
    


#User define exception
class Myerror(Exception):
    pass
try:
    raise Myerror ('some error')
except Myerror as e:
    print(e)

class Myerror(SystemExit):
    def __init__(self, msg):
        self.msg=msg
    def __str__(self):
        return 'chandan'
try:
    raise Myerror ('some error')
except Myerror as e:
    print(e)



#Nested try-except
try:
    a = int(input('Enter first number:'))
    try:
        b = int(input('Enter second number:'))
        try:
            c = a//b
            print(c)
        except ZeroDivisionError as msg2:
            print(msg2)
    except ValueError as msg1:
        print(msg1)
except ValueError as msg:
    print(msg)


# Using multiple except block
try:
    a = int(input('Enter first number:'))
    b = int(input('Enter second number:'))
    c = a//b
    print(c)
except ZeroDivisionError as msg2:
            print(msg2)
except ValueError as msg:
    print(msg)



