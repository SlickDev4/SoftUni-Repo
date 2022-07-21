sum_list_strings = input().split(", ")
beggars_count = int(input())

index_count = 0

final_list = []
sum_list_digits = [int(i) for i in sum_list_strings]

while index_count < beggars_count:
    current_sum = 0

    for index in range(index_count, len(sum_list_digits), beggars_count):
        current_sum += sum_list_digits[index]

    index_count += 1
    final_list.append(current_sum)

print(final_list)
