# Check if a year is a leap year or not

year = int(input("Enter a year to check if it's a leap year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

    

# Cheak if the person is authorise foe admin access

str_name = input("Enter the name of the user to be admin:")

if (str_name == 'Prem_kishan') or (str_name == 'Ravi_Ranjan'):
    print("Authorise fo admin access.")
else:
    print("You are not access user admin.")



# Nested if and elif.

# Enter the name of the student from user and find who is eldest.

john = int(input("Enter the age of john:" ))
prem = int(input("Enter the age of prem:" ))
ravi = int(input("Enter the age of ravi:"))

if (john > prem) and (john > ravi):
    print("john is eldest.")
elif prem > ravi:
    print("Prem is eldest.")
else:
    print("ravi is eldest.")

# else:
#     if prem > ravi:
#         print("prem is eldest.")
#     else:
#         print("ravi is eldest.")
