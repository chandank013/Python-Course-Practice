                        # Basics

## Basic Syntax Rules In Python
## Case sensitivity- Python is case sensitive
name="Chandan"
Name="Kumar"

print(name)
print(Name)


## Indentation
## Python uses indentation to define blocks of code. Consistent use of spaces (commonly 4) or a tab is required.

age=32
if age>30:
    
    print(age)
    
print(age)


## Line Continuation
##Use a backslash (\) to continue a statement to the next line

total=1+2+3+4+5+6+7+\
4+5+6

print(total)


## Multiple Statements on a single line
x=5;y=10;z=x+y
print(z)

type(age)
type(name)


## Type Inference
variable=10
print(type(variable))
variable="Chandan"
print(type(variable))


## Code exmaples of indentation
if True:
    print("Correct Indentation")
    if False:
        print("This ont print")
    print("This will print")
print("Outside the if block")



                        # Variables

a=100

## Declaring And Assigning Variables

age=20
height=5.9
name="Chandan"
is_student=True

## printing the variables

print("age :",age)
print("Height:",height)
print("Name:",name)


## Naming Conventions
## Variable names should be descriptive
## They must start with a letter or an '_' and contains letter,numbers and underscores
## variables names case sensitive

#valid variable names

first_name="CHanDan"
last_name="Kumar"


# Invalid variable names
#2age=20
#first-name="Chandan"
##@name="Chandan"


## case sensitivity
name="Chandan"
Name="Kumar"


## Understnading Variable types
## Python is dynamically typed,type of a variable is determined at runtime
age=20 #int
height=6.1 #float
name="CHandan" #str
is_student=True #bool

print(type(name))
## Type Checking and Conversion

height=5.9
type(height)

age=25
print(type(age))

# Type conversion
age_str=str(age)
print(age_str)
print(type(age_str))


## Dynamic Typing
## Python allows the type of a vraible to change as the program executes
var=10 #int
print(var,type(var))

var="Hello"
print(var,type(var))

var=3.14
print(var,type(var))


## input

age=int(input("What is the age"))
print(age,type(age))


### Simple calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2
quotient = num1 / num2

print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
