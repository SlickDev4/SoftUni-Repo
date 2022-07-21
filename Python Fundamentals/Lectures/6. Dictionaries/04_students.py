my_dict = {}
final_course = ""
while True:
    students = input().split(":")
    final_course = students[0]

    if len(students) == 1:
        break
    else:
        name = students[0]
        ids = int(students[1])
        course = students[2]

    if course not in my_dict:
        my_dict[course] = {}
    my_dict[course][name] = name
    my_dict[course][name] = ids

if "_" in final_course:
    final_course = final_course.replace("_", " ")

for key, value in my_dict[final_course].items():
    print(f"{key} - {value}")


