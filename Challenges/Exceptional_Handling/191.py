# Negative age 

class Negative_Age_Exception(Exception):
    pass
def stage(age):
    if age < 0:
        raise Negative_Age_Exception('Age should not be negative')
    elif age >= 0 and age < 13:
        print('Kid')
    elif age >= 13 and age < 20:
        print('Teen')
    elif age >= 20 and age < 50:
        print('Young')
    else:
        print('Old')

age = int(input('Enter the age of human:'))
try:
    stage(age)
except Negative_Age_Exception as e:
    print(e)

