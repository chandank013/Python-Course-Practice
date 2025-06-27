# WAP to Cheak if number is prime or not.

num_1 = int(input("Enter the number to cheak prime or not:"))

count = 0
for i in range(1,num_1 + 1):
    if num_1 % i == 0:
        
       
        count +=1
     
     
if count == 2 :
    print(f"{num_1} is prime number.")
else:
    print(f"{num_1} is  not prime number.")




# # Using while loop

# num_1 = int(input("Enter the number to cheak prime or not:"))

# count = 1
# while count <= num_1:
#     if (num_1 % count)  == 0:
       
#        count += 1
#        print(count)
       
        

#        if count == 2:
        
#         print(" PRime")
#        else:
#         print(" Not PRime")
  
#      not run



