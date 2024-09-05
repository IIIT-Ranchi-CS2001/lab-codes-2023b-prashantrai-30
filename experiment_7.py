name = str(input("Enter name of student"))
roll_number = int(input("Enter roll number of student"))
marks = int(input("Enter marks of student"))
grade_point = 0
remark = ""

if(marks >= 90):
    grade_point=10
    remark="OUTSTANDING"

if((marks < 90) and (marks >=80)):
    grade_point=9
    remark="VERY GOOD"

if((marks < 80) and (marks >=70)):
    grade_point=8
    remark="GOOD"

if((marks < 70) and (marks >=60)):
    grade_point=7
    remark="AVERAGE"

if((marks < 60) and (marks >=50)):
    grade_point=6
    remark="PASS"

if((marks < 50)):
    grade_point=0
    remark="FAIL"


print("name:",name,'\n',"roll number:",roll_number,'\n',"marks:",marks,'\n',"grade point:",grade_point,'\n',"remark:",remark)
