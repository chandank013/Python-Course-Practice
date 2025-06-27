# # WAP to counting the number of digits in a number

# num = int(input(" Enter the number:"))

# count_number = 0
# while num  > 0 :
#     num = num//10
#     count_number+=1
 
#     print(count_number)
   




# # Find the sum of digit in a number
num = int(input(" Enter the number:"))

sum = 0
while num > 0:
    r = num % 10
    num = num//10
   
    # print(num)
    # print(r)
    sum+=r
 
print(sum)
