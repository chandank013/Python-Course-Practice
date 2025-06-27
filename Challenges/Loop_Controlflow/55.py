# WAP to find the sum of given number as input.

num_of_num =int(input("Enter the number of number have you going to put in:"))

sum = 0
count = 0
while count < num_of_num:
    n = int(input("Enter the number:"))

    sum += n
    count+=1
print(sum)




# WAP to find sum of positive and negative number

num_of_num =int(input("Enter the number of number have you going to put in:"))

Nsum = 0
Psum = 0
count = 0
while count < num_of_num:
    n = int(input("Enter the number:"))
    if n > 0:
      Psum += n
    else:
        Nsum += n
    count+=1


print('Positive sum', Psum)
print('Negative sum', Nsum)
