number_of_students = int(input())
students = {}

for i in range(number_of_students):
    name = input()
    grade = float(input())

    if name not in students.keys():
        students[name] = grade
    else:
        students[name] = (students[name] + grade) / 2

for key, value in students.items():
    if value >= 4.5:
        print(f"{key} -> {value:.2f}")





