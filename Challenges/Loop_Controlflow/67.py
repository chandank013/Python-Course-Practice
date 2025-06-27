# Match case means in switch case

# day = int(input("Enter the number of day:"))

# if day == 1:
#     print('Monday')
# elif day == 2:
#     print('Tuesday')
# elif day == 3:
#     print('Wednesday')
# elif day == 4:
#     print('Thursday')
# elif day == 5:
#     print('Friday')
# elif day == 6:
#     print('Saturday')
# elif day == 7:
#     print('Sunday')
# else:
#      print('Holiday')

# Using MAtch case

day = int(input("Enter the number of day:"))


match day:
    case 1:
        print('Monday')
    case 2:
        print('Tuesday')
    case 3:
        print('Wednesday')
    case 4:
        print('Thursday')
    case 5:
        print('Friday')
    case 6:
        print('Saturday')
    case 7:
        print('Sunday')
    case _:
        print('Holiday')