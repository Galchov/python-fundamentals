pair_of_rows = int(input())

students_data = {}

for _ in range(pair_of_rows):
    student = input()
    grade = float(input())

    if student not in students_data:
        students_data[student] = [grade]
    else:
        students_data[student].append(grade)

for key, value in students_data.items():
    average_grade = sum(value) / len(value)
    students_data[key] = average_grade

students_data = dict(sorted(students_data.items(), key=lambda x: -x[1]))

for key, value in students_data.items():
    if value >= 4.50:
        print(f"{key} -> {value:.2f}")