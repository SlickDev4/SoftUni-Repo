number_of_lines = int(input())
pos_list = []
neg_list = []
count_positives = 0
sum_of_negatives = 0

for _ in range(number_of_lines):
    num = int(input())

    if num >= 0:
        pos_list.append(num)
        count_positives += 1
    else:
        neg_list.append(num)
        sum_of_negatives += num

print(pos_list)
print(neg_list)
print(f"Count of positives: {count_positives}")
print(f"Sum of negatives: {sum_of_negatives}")
