numbers_list = input().split()
opposite_numbers_list = []

for element in numbers_list:
    opposite_numbers_list.append(-int(element))

print(opposite_numbers_list)
