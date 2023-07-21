class Employee:
    employee_count = 101
    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation
        self.eid = 'E' + str(Employee.employee_count)
        Employee.employee_count += 1
    def show_details(self):
        print('Name: ', self.name)
        print('Eid: ', self.eid)
        print('Designation: ', self.designation)
        print('Salary: ', self.salary)
    @classmethod
    def total_employees(cls):
        return cls.employee_count - 101
e1 = Employee('John', 'Manager', '10000')
e2 = Employee('Smith', 'Team Leader', '8000')
e1.show_details()
print('')
e2.show_details()
print('')
print('Total employee count: ', e1.total_employees())        
        
        
        
        