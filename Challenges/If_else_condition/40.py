# This program checks age for work
age = int(input("Enter your age: "))
if 18 <= age <= 60:
    print("You are eligible to work.")
else:
    print("You are not eligible to work.")


# This program checks if the entered marks are valid
marks = int(input("Enter your marks: "))
if 0 <= marks <= 100:
    print("The marks entered are valid.")
else:
    print("The marks entered are invalid.")


# Program for gender cheak
gender = input("Enter your gender (M/F): ").strip().upper()
if gender == "M":
    print("You are Male.")
elif gender == "F":
    print("You are Female.")
else:
    print("Invalid input for gender.")