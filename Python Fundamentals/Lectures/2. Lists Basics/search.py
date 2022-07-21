lines = int(input())
word = input()
my_list = []

for _ in range(lines):
    strings = input()
    my_list.append(strings)

print(my_list)

for i in range(len(my_list) - 1, -1, -1):
    element = my_list[i]
    if word not in element:
        my_list.remove(element)

print(my_list)
