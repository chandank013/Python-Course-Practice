# Sorting sting challenge

# str1 = 'bghiamporcd'
# print(sorted(str1))

# str1 = 'qwertyuioplkjhgfdsazxcvbnm'
# ff = (sorted(str1))

# # print(ff)

# str2 = ''.join(ff)
# print(str2)


# Displaying Data in given format (25 letters)
              # Product Name.....price
                   # Chicken pizza....300
name1 = input("Enter the name of things:")
price = input("Enter the price:")

total_name = len(name1) + len(price)
print(total_name)

dot = '.' * (25 - total_name)
print(name1 + dot + price)


# Chek if the password and confirmed are same

# pass1 = input("Enter the first password:")
# pass2 = input("Enter the second password:")

# if pass1 == pass2:
#     print(f"{pass1} and {pass2} are same:")
# elif pass1.casefold() == pass2.casefold():
#     print("Please cheak for the cases and try again.")
# else:
#     print("No the password is not matching try again")
