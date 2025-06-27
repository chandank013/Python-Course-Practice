# Find the birthday of a person

birthday = {
    'Sachin':'03/14/2003',
    'Carl':'09/17/2001',
    'Khan':'07/10/2006',
    'Donald':'08/08/2010',
    'Rohan':'01/o6/2005',
}

name_of_boy = input("Enter the name of the boy:")


# for name in birthday:                      # Method 1
#     if name ==name_of_boy:
#         print(birthday[name])
#         break
#     else:
#         print("Name not found in given dictonary.")



if name_of_boy in birthday:                  # Method 2
    print(birthday[name_of_boy])
else:
    print("Not found")