from math import ceil

number_of_people = int(input())
capacity = int(input())

courses = 0

if not capacity == 0:
    courses = ceil(number_of_people / capacity)

print(courses)
