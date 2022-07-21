list_of_numbers = input().split()
numbers_to_remove = int(input())
final = ''
list_of_ints = [int(i) for i in list_of_numbers]

for number in range(numbers_to_remove):
    list_of_ints.remove(min(list_of_ints))

print(*list_of_ints, sep=", ")
