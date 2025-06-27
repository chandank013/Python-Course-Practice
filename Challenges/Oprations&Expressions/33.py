# Program for findings roos of the equaion

import math

a = int(input("Enter the vavlue of coefficient a:"))
b = int(input("Enter the vavlue of coefficient b:"))
c = int(input("Enter the vavlue of coefficient c:"))

r1 = (-b + math.sqrt(b** - 4*a*c))/(2*a)
r2 = (-b - math.sqrt(b** - 4*a*c))/(2*a)

print("roots are:", r1, r2)
