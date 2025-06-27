# Details of an Employee
# Using Instance and Class Variable

class Employee:

    employee_count = 101
    
    def __init__(self,name,designation,salary):
        self.name = name
        self.designation = designation
        self.salary = salary
        self.imp_id = 'e' + str(Employee.employee_count)

        Employee.employee_count += 1
    
    def show_details(self):
        print('Name:',self.name)
        print('Imp_Id:',self.imp_id)
        print('Designation:',self.designation)
        print('Salary:',self.salary)
        
        

    @classmethod
    def total_emp(cls):
        return cls.employee_count - 101
    
e1 = Employee('John','Manager',100000)
e2 = Employee('Mark','Director',125000)
        
e1.show_details()
print(' ')
e2.show_details()
print(' ')
print('Total No. of Employee:',e1.total_emp())