work_hour = [int(x) for x in input("Enter hours per day, separated by space: ").split()]
wage = int(input("Enter hourly wage: "))
total = sum(work_hour)
salary = total * wage
print("Salary is", salary)
