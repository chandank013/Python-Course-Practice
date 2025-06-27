# Program to calculate the area of a triangle

# Input the base and height of the triangle
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

# Calculate the area
area = 0.5 * base * height

# Display the result
print(f"The area of the triangle is: {area}")



# Program to calculate the area of a rectangle

# Input the length and width of the rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate the area
area = length * width

# Display the result
print(f"The area of the rectangle is: {area}")


# Program to calculate the area of a circle

# Input the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Calculate the area
area = 3.14 * radius ** 2

# Display the result
print(f"The area of the circle is: {area}")



# Program to calculate the area of a trapezoid

# Input the lengths of the two parallel sides and the height of the trapezoid
base1 = float(input("Enter the length of the first parallel side: "))
base2 = float(input("Enter the length of the second parallel side: "))
height = float(input("Enter the height of the trapezoid: "))

# Calculate the area
area = 0.5 * (base1 + base2) * height

# Display the result
print(f"The area of the trapezoid is: {area}")
