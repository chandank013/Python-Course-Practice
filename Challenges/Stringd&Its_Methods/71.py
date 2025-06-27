# Cheaking a string is a pelindrome or not


pelin_1 = input("Enter the name to chaek pelindrome:")

straight = pelin_1[:len(pelin_1):]
rev = pelin_1[::-1]

if straight == rev:
    print("The given string is pelindrome.")
else:
    print("The given string is not pelindrome.")



# Convert the string in to prlindrome

pelin_1 = input("Enter the name to chaek pelindrome:")

rev = pelin_1[::-1]

print(pelin_1 + rev)


