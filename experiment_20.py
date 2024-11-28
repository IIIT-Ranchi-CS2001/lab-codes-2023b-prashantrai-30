n = int(input("Enter total studnets:"))
names = [str(input(f"Enter name of {i+1} student: ")) for i in range(n)]
roll = [int(input(f"Enter roll number of {name}: ")) for name in names]
marks = [float(input(f"Enter physics marks of {name}: ")) for name in names]

student_data = list(zip(names, roll, marks))

sorted_student_data = sorted(student_data, key=lambda x: x[2], reverse=True)

print("\nSorted Student Data (Name, Roll No, Physics Marks):")
for student in sorted_student_data:
    print(f"{student[0]}, {student[1]}, {student[2]}")