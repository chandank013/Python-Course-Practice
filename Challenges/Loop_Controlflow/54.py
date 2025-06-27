# WAP to reversing a number.

num_1 = int(input("Enter the number to be get reverse:"))

rev = 0
while num_1 > 0:
    remain = num_1 % 10
    num_1 = num_1 // 10
    rev = rev*10 + remain
    
    print(rev)



# WAP to cheak the number is pelindrome or not;

num_1 = int(input("Enter the number to be get reverse:"))

m=num_1
rev = 0
while num_1 > 0:
    remain = num_1 % 10
    num_1 = num_1 // 10
    rev = rev*10 + remain
    
if m == rev:
    print("Number is Pelindrome.")
else:
    print("Number is not Pelindrome")