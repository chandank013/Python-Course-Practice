# WAP to print prime number between 1 to 100

lower = int(input("Enter the lower number:"))
upper = int(input("Enter the upper number:"))

for n in range(lower,upper + 1):
    count = 0

    for i in range(1,n + 1):
        if n % i == 0:
            count+=1
        

    if count == 2:
            print(n)
        
   

