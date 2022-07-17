courses = {}

while True:
    command = input().split(" : ")
    if command[0] == "end":
        break

    course = command[0]
    student = command[1]

    if course not in courses.keys():
        courses[course] = [student]
    if student not in courses[course]:
        courses[course].append(student)

for key, value in courses.items():
    print(f"{key}: {len(value)}")
    for name in value:
        print(f"-- {name}")

