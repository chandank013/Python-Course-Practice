# # Calculating salary, weekly working hours given in the list

work_hours = [int(x) for x in input("Enter the number of working hours:").split()]
sum=0
for i in work_hours:
    if isinstance(i,int):     
        sum+=i
# print(sum)              # sum using loop

wage_per_hour = int(input("Enter the wages per hour of worker:"))

salary = sum(work_hours) * wage_per_hour
print(salary)
