input_data = input()

courses = {}

while not input_data == "end":
    course_info = input_data.split(" : ")
    course_name = course_info[0]
    student_name = course_info[1]

    if course_name not in courses:
        courses[course_name] = [student_name]
    else:
        courses[course_name].append(student_name)

    input_data = input()

for course, students in sorted(courses.items(), key=lambda kvp: -(len(kvp[1]))):
    print(f"{course}: {len(students)}")

    for name in sorted(students):
        print(f"-- {name}")