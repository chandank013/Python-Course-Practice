# WAP to  find maximum number from given number

num_of_num =int(input("Enter the number of number have you going to put in:"))

max = 0
count = 0
while count < num_of_num:
    n = int(input("Enter the number:"))

    if n > max:
        max = n
    count+=1
print(max)
