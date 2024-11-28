course_codes = ["CS2001", "CS2003", "CS2005", "MA2001", "HS2001"]
course_names = ["Python", "COA", "TOC", "Mathematics", "Management"]
combined_courses = []
for i in range(len(course_codes)):
    combined_courses.append(course_codes[i] + ":" + course_names[i])
print("Combined Courses:", combined_courses)