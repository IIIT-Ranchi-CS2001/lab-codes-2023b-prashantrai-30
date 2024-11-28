
employees = {}

for i in range(5):
    name = input(f"Enter the name of employee {i+1}: ")
    salary = float(input(f"Enter the salary of {name}: "))
    employees[name] = salary

employee_list = list(employees.items())

n = len(employee_list)
for i in range(n):
    for j in range(0, n - i - 1):
        if employee_list[j][1] < employee_list[j + 1][1]:
            employee_list[j], employee_list[j + 1] = employee_list[j + 1], employee_list[j]

# Display sorted employees with rank
print("\nEmployee Salary Ranking (Highest salary first):")
for rank, (name, salary) in enumerate(employee_list, start=1):
    print(f"Rank {rank}: {name} with a salary of ${salary:.2f}")
