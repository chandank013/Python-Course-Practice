# Find day month and year from date

mydate = input("Enter the date in form of dd/mm/yy:")


j = mydate.split('/')
print(j)


print('Day',j[0])
print('mont',j[1])
print('year',j[2])
