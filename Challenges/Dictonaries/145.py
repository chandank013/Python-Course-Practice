#  Create dictonary with student details

# student = {
#     'Jenny':{'Roll_no':10,
#              'Name':'Jenny',
#              'Dept_name':'DSAI'},
#     'Sam':{'Roll_no':36,
#              'Name':'Sam',
#              'Dept_name':'CSE'},
#     'Peter':{'Roll_no':45,
#              'Name':'Peter',
#              'Dept_name':'ECE'},
#     'Mark':{'Roll_no':55,
#              'Name':'Mark',
#              'Dept_name':'IT'}}

student1 = {}

for i in range(3):
    name = input("Enter the Name:")
    roll_no = int(input('Enter the roll_no:'))
    dept_name = (input('Enter the dept_name:'))

    student1[name] = {'Roll_no' : roll_no,'Name' : name,'Dept_name' : dept_name}
print(student1)





