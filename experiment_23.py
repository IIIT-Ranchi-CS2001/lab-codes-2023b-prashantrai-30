students = {}
for i in range(5):
    name = input(f"Enter the name of student {i+1}: ")
    marks = float(input(f"Enter the marks of {name} (in percentage): "))
    students[name] = marks

high_performers = []
average_performers = []
low_performers = []

for name, marks in students.items():
    if marks >= 85:
        high_performers.append(name)
    elif 60 <= marks < 85:
        average_performers.append(name)
    else:
        low_performers.append(name)

print("Number of High Performers:",{len(high_performers)})
print(", ".join(high_performers))

print("Number of Average Performers:",{len(average_performers)})
print(", ".join(average_performers))

print("Number of Low Performers:",{len(low_performers)})
print(", ".join(low_performers))

top_student = max(students, key=students.get)
print("\nThe student with the highest marks is:",top_student,"with",students[top_student],"%")
