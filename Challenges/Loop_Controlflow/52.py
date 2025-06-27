# WAP to print table using while loop.

num_1 = int(input("Enter the number to get their table:"))

i = 1
while i <= 10:
    print(num_1, 'X', i,'=', num_1 *i)
    i+=1
