list_one = input().split(", ")
list_two = input().split(", ")
substring_list = []

for first_word in list_one:
    for second_word in list_two:
        if first_word in second_word and first_word not in substring_list:
            substring_list.append(first_word)
            break

print(substring_list)
