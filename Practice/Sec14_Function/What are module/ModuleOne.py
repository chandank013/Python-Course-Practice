
# What are module

# Variable
# Function     # Can be imported in another program as module
# Classes
total_amount = 2000

def add_(x,y):
    return x+y

def sub_(x,y):
    return x-y
# print(__name__)    # Here __name__ is printed as __main__ but name of file will print where this file act as module
# print('from Module One',add_(20,30))
# print('from Module One',sub_(40,30))
if __name__ == '__main__':
    print(__name__)
    print('from Module One',add_(20,30))
    print('from Module One',sub_(40,30))
