# Program to convert kilometers to miles

def km_to_miles(kilometers):
    # Conversion factor
    conversion_factor = 0.621371
    # Calculate miles
    miles = kilometers * conversion_factor
    return miles

# Input from user
kilometers = float(input("Enter distance in kilometers: "))
miles = km_to_miles(kilometers)

print(f"{kilometers} kilometers is equal to {miles} miles.")



# code for calculating displacement not using functions by taking input from user

def calculate_displacement(x1, y1, x2, y2):
    # Calculate displacement using the distance formula
    displacement = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return displacement


# Input coordinates from user
x1 = float(input("Enter x1 coordinate: "))
y1 = float(input("Enter y1 coordinate: "))
x2 = float(input("Enter x2 coordinate: "))
y2 = float(input("Enter y2 coordinate: "))

displacement = calculate_displacement(x1, y1, x2, y2)
print(f"The displacement between the points ({x1}, {y1}) and ({x2}, {y2}) is: {displacement}")




# code for surface area of cubiod

def surface_area_cuboid(length, width, height):
    # Calculate surface area using the formula: 2(lw + lh + wh)
    surface_area = 2 * (length * width + length * height + width * height)
    return surface_area


# Input dimensions from user
length = float(input("Enter length of the cuboid: "))
width = float(input("Enter width of the cuboid: "))
height = float(input("Enter height of the cuboid: "))


surface_area = surface_area_cuboid(length, width, height)
print(f"The surface area of the cuboid is: {surface_area}")







