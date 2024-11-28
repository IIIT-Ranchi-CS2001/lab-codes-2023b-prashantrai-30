n = int(input("Enter total studnets:"))
names = [str(input(f"Enter name of {i+1} student: ")) for i in range(n)]
roll = [int(input(f"Enter roll number of {name}: ")) for name in names]
marks = [float(input(f"Enter physics marks of {name}: ")) for name in names]

student_data = []
for i in range(n):
    student_data.append([names[i], roll[i], marks[i]])

for i in range(n):
    for j in range(0, n-i-1):
        if student_data[j][2] < student_data[j+1][2]:
            student_data[j], student_data[j+1] = student_data[j+1], student_data[j]

print("\nSorted Student Data (Name, Roll No, Physics Marks):")
for student in student_data:
    print(f"{student[0]}, {student[1]}, {student[2]}")
