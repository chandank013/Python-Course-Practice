 # WAP to find the factorial of given number.

num_1 = int(input("Enter the number to get Factorial:"))

# using for loop
fact = 1
for count in range(1,num_1+1):
    fact*=count
print(fact)


# using While loop.
count = 1
fact = 1
while count <(num_1 +1):
    fact*=count
    count+=1
print(fact)